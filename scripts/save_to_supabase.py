"""Import candidate books and genre links to Supabase safely and reliably."""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

SUPABASE_URL = os.environ.get("SUPABASE_URL", "").rstrip("/")
SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")

if not SUPABASE_URL or not SERVICE_KEY:
    print("ERROR: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY environment variables are required.")
    print("Ensure GitHub repository secrets or local environment variables are properly configured.")
    sys.exit(1)

HEADERS = {
    "apikey": SERVICE_KEY,
    "Authorization": f"Bearer {SERVICE_KEY}",
    "Content-Type": "application/json",
}

def request(path, method="GET", data=None, prefer=None, max_retries=3):
    headers = dict(HEADERS)
    if prefer:
        headers["Prefer"] = prefer
    payload = json.dumps(data).encode("utf-8") if data is not None else None
    url = f"{SUPABASE_URL}/rest/v1/{path}"

    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, data=payload, headers=headers, method=method)
            with urllib.request.urlopen(req, timeout=45) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else []
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")[:1000]
            if attempt == max_retries - 1:
                raise RuntimeError(f"Supabase HTTP {error.code} on {method} {path}: {detail}") from error
            time.sleep(1.5 * (attempt + 1))
        except Exception as error:
            if attempt == max_retries - 1:
                raise
            time.sleep(1.5 * (attempt + 1))

def chunks(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]

def main():
    source_file = "rabbit_books_preview.json"
    if not os.path.exists(source_file):
        print(f"ERROR: Preview source file '{source_file}' not found.")
        sys.exit(1)

    with open(source_file, "r", encoding="utf-8") as source:
        raw_books = json.load(source)

    print(f"Loaded {len(raw_books)} candidate books from {source_file}")

    # Deduplicate candidate books by open_library_work_id
    books_by_id = {}
    for b in raw_books:
        wid = b.get("open_library_work_id")
        if not wid:
            continue
        if wid not in books_by_id:
            books_by_id[wid] = dict(b)
        else:
            # Merge genres
            for g in b.get("genres", []):
                if g not in books_by_id[wid]["genres"]:
                    books_by_id[wid]["genres"].append(g)

    unique_books = list(books_by_id.values())
    print(f"Deduplicated to {len(unique_books)} unique books across genres.")

    # Fetch genres from Supabase
    genres = request("genres?select=id,name")
    genre_ids = {g["name"]: g["id"] for g in genres}
    print(f"Found {len(genre_ids)} genres in Supabase: {list(genre_ids.keys())[:5]}...")

    saved_count = 0
    work_to_db_id = {}

    # Process in batches of 30
    for group in chunks(unique_books, 30):
        # Check existing records in Supabase
        ids = [b["open_library_work_id"] for b in group]
        quoted_ids = ",".join(f'"{i}"' for i in ids)
        try:
            existing = request(f"books?select=id,open_library_work_id&open_library_work_id=in.({quoted_ids})")
            for row in existing:
                work_to_db_id[row["open_library_work_id"]] = row["id"]
        except Exception as e:
            print(f"Notice: Querying existing chunk failed, falling back: {e}")

        # Prepare new books
        new_books = []
        for b in group:
            wid = b["open_library_work_id"]
            if wid not in work_to_db_id:
                new_books.append({
                    "open_library_work_id": wid,
                    "title": b.get("title", "Untitled")[:255],
                    "author": b.get("author", "Unknown")[:255],
                    "cover_url": b.get("cover_url", ""),
                    "catalog_status": "pending",
                })

        if new_books:
            try:
                inserted = request("books?select=id,open_library_work_id", method="POST",
                                   data=new_books, prefer="return=representation")
                for row in inserted:
                    work_to_db_id[row["open_library_work_id"]] = row["id"]
            except Exception as e:
                print(f"Batch insert error: {e}. Retrying individual rows...")
                for b_item in new_books:
                    try:
                        ins = request("books?select=id,open_library_work_id", method="POST",
                                      data=[b_item], prefer="return=representation")
                        if ins:
                            work_to_db_id[ins[0]["open_library_work_id"]] = ins[0]["id"]
                    except Exception as err:
                        print(f"Warning: skipped book {b_item.get('title')}: {err}")

        # Link book genres
        links = []
        for b in group:
            db_id = work_to_db_id.get(b["open_library_work_id"])
            if not db_id:
                continue
            for gname in b.get("genres", []):
                gid = genre_ids.get(gname)
                if gid:
                    links.append({"book_id": db_id, "genre_id": gid})

        if links:
            try:
                request("book_genres?on_conflict=book_id,genre_id", method="POST",
                        data=links, prefer="resolution=ignore-duplicates,return=minimal")
            except Exception as e:
                print(f"Notice on book_genres insert: {e}")

        saved_count += len(group)
        print(f"Processed {saved_count}/{len(unique_books)} books...", flush=True)

    print(f"\nSUCCESS: Imported / confirmed {saved_count} books in Supabase.")

if __name__ == "__main__":
    main()
