
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter

GENRES = {
    "The Human Mind": "psychology",
    "Romance": "romance",
    "Fantasy": "fantasy",
    "Science Fiction": "science_fiction",
    "Mystery & Thriller": "mystery",
    "Horror": "horror",
    "Historical Fiction": "historical_fiction",
    "Young Adult": "young_adult_fiction",
    "Classics": "classic_literature",
    "Adventure": "adventure",
    "Literary Fiction": "literary_fiction",
    "Philosophy": "philosophy",
    "Self-Help": "self_help",
    "Business & Money": "business",
    "Science": "science",
    "History": "history",
    "Biography & Memoir": "biography",
    "Politics & Society": "politics",
    "True Crime": "true_crime",
    "Poetry": "poetry",
}

TARGET_PER_GENRE = 50
PAGE_SIZE = 100
MAX_PAGES = 8
DELAY_SECONDS = 1.5
MAX_RETRIES = 3

HEADERS = {
    "User-Agent": (
        "RABBITBookDiscovery/0.3 "
        "(GitHub: ashmitamanikandan-sys/Rabbit.)"
    ),
    "Accept": "application/json",
}


def request_json(url):
    for attempt in range(MAX_RETRIES):
        try:
            request = urllib.request.Request(
                url, headers=HEADERS
            )
            with urllib.request.urlopen(
                request, timeout=30
            ) as response:
                return json.load(response)

        except (
            urllib.error.URLError,
            TimeoutError,
            ValueError,
        ) as error:
            print(
                f"Request failed: {error}",
                flush=True
            )

            if attempt == MAX_RETRIES - 1:
                raise

            time.sleep(3 * (attempt + 1))


def search_books(subject, page):
    params = urllib.parse.urlencode({
        "subject": subject,
        "page": page,
        "limit": PAGE_SIZE,
        "fields": (
            "key,title,author_name,cover_i,"
            "language,edition_key"
        ),
    })

    url = (
        "https://openlibrary.org/search.json?"
        + params
    )

    return request_json(url).get("docs", [])


def english_evidence(item):
    languages = item.get("language") or []
    return "eng" in languages


def valid_candidate(item):
    work_id = item.get("key")
    title = item.get("title")
    authors = item.get("author_name") or []
    cover_id = item.get("cover_i")

    if not isinstance(work_id, str):
        return False, "missing_work_id"

    if not work_id.startswith("/works/"):
        return False, "invalid_work_id"

    if not isinstance(title, str) or not title.strip():
        return False, "missing_title"

    if not authors or not authors[0]:
        return False, "missing_author"

    if not isinstance(cover_id, int) or cover_id <= 0:
        return False, "missing_cover"

    if not english_evidence(item):
        return False, "no_english_evidence"

    return True, "accepted"


def cover_works(cover_id):
    # Test a small image, not the full-size cover.
    url = (
        "https://covers.openlibrary.org/b/id/"
        f"{cover_id}-S.jpg?default=false"
    )

    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": HEADERS["User-Agent"]
            },
            method="GET",
        )

        with urllib.request.urlopen(
            request, timeout=15
        ) as response:
            content_type = response.headers.get(
                "Content-Type", ""
            )
            return (
                response.status == 200
                and content_type.startswith("image/")
                and bool(response.read(32))
            )

    except (urllib.error.URLError, TimeoutError):
        return False


def make_book(item, genre):
    cover_id = item["cover_i"]

    return {
        "open_library_work_id": item["key"],
        "title": item["title"].strip(),
        "author": item["author_name"][0].strip(),
        "cover_url": (
            "https://covers.openlibrary.org/b/id/"
            f"{cover_id}-L.jpg?default=false"
        ),
        "cover_id": cover_id,
        "genres": [genre],
        "language": "eng",
        "catalog_status": "pending",
    }


def save_json(filename, data):
    with open(
        filename, "w", encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False,
        )


def main():
    books = {}
    rejected = Counter()
    genre_counts = {}
    failed_requests = []
    checked_covers = {}

    for genre, subject in GENRES.items():
        print(
            f"\nSearching {genre}...",
            flush=True
        )

        accepted_in_genre = set()

        for page in range(1, MAX_PAGES + 1):
            if len(accepted_in_genre) >= TARGET_PER_GENRE:
                break

            try:
                results = search_books(subject, page)
            except Exception as error:
                failed_requests.append({
                    "genre": genre,
                    "page": page,
                    "error": str(error),
                })
                time.sleep(DELAY_SECONDS)
                continue

            if not results:
                break

            for item in results:
                if len(accepted_in_genre) >= TARGET_PER_GENRE:
                    break

                valid, reason = valid_candidate(item)

                if not valid:
                    rejected[reason] += 1
                    continue

                work_id = item["key"]

                if work_id in accepted_in_genre:
                    continue

                if work_id in books:
                    if genre not in books[work_id]["genres"]:
                        books[work_id]["genres"].append(
                            genre
                        )
                    accepted_in_genre.add(work_id)
                    continue

                cover_id = item["cover_i"]

                if cover_id not in checked_covers:
                    checked_covers[cover_id] = (
                        cover_works(cover_id)
                    )
                    time.sleep(0.3)

                if not checked_covers[cover_id]:
                    rejected["cover_unavailable"] += 1
                    continue

                books[work_id] = make_book(
                    item, genre
                )

                accepted_in_genre.add(work_id)

            print(
                f"Page {page}: "
                f"{len(accepted_in_genre)} accepted",
                flush=True
            )

            time.sleep(DELAY_SECONDS)

        genre_counts[genre] = len(accepted_in_genre)

    preview = list(books.values())

    report = {
        "unique_books": len(preview),
        "target_unique_books": 1000,
        "genre_counts": genre_counts,
        "rejection_reasons": dict(rejected),
        "failed_requests": failed_requests,
        "publication_ready": 0,
        "note": (
            "Catalog candidates only. Summaries, "
            "genre accuracy, cover rights, and "
            "publication readiness remain unverified."
        ),
    }

    save_json(
        "rabbit_books_preview.json",
        preview
    )

    save_json(
        "rabbit_import_report.json",
        report
    )

    print("\nRABBIT IMPORT COMPLETE")
    print(f"Unique candidates: {len(preview)}")
    print("Publication-ready books: 0")
    print("Preview and report saved.")


if __name__ == "__main__":
    main()
