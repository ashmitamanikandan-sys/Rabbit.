
import json
import urllib.parse
import urllib.request

# RABBIT's first five test genres
GENRES = [
    "fantasy",
    "science_fiction",
    "romance",
    "psychology",
    "philosophy",
]

BOOKS_PER_GENRE = 4


def fetch_books(genre):
    params = urllib.parse.urlencode({
        "subject": genre,
        "limit": 20,
        "fields": "key,title,author_name,first_publish_year,cover_i",
    })

    url = f"https://openlibrary.org/search.json?{params}"

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "RABBIT-BookImporter/0.1"}
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.load(response)

    books = []

    for item in data.get("docs", []):
        authors = item.get("author_name") or []
        cover_id = item.get("cover_i")
        work_id = item.get("key")

        if not item.get("title") or not authors or not cover_id:
            continue

        if not work_id or not work_id.startswith("/works/"):
            continue

        books.append({
            "open_library_work_id": work_id,
            "title": item["title"],
            "author": authors[0],
            "publication_year": item.get("first_publish_year"),
            "cover_url": (
                f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
            ),
            "genre": genre,
        })

        if len(books) == BOOKS_PER_GENRE:
            break

    return books


def main():
    all_books = []
    seen_ids = set()

    for genre in GENRES:
        print(f"Finding books in {genre}...")

        try:
            books = fetch_books(genre)
        except Exception as error:
            print(f"Could not fetch {genre}: {error}")
            continue

        for book in books:
            if book["open_library_work_id"] in seen_ids:
                continue

            seen_ids.add(book["open_library_work_id"])
            all_books.append(book)

    with open("rabbit_books_preview.json", "w", encoding="utf-8") as file:
        json.dump(all_books, file, indent=2, ensure_ascii=False)

    print(f"\nFound {len(all_books)} unique books!")
    print("Saved preview to rabbit_books_preview.json")


if __name__ == "__main__":
    main()
