
import json
import os
import urllib.request
import urllib.parse

BASE = os.environ["SUPABASE_URL"].rstrip("/")
KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]

HEADERS = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

def request(path, method="GET", data=None, prefer=None):
    headers = dict(HEADERS)
    if prefer:
        headers["Prefer"] = prefer

    payload = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(
        BASE + "/rest/v1/" + path,
        data=payload,
        headers=headers,
        method=method
    )
    with urllib.request.urlopen(req, timeout=40) as response:
        return json.loads(response.read().decode() or "[]")

with open("rabbit_books_preview.json", encoding="utf-8") as f:
    books = json.load(f)

genres = request("genres?select=id,name")
genre_ids = {g["name"]: g["id"] for g in genres}

saved = 0

for book in books:
    work_id = book["open_library_work_id"]

    payload = {
        "open_library_work_id": work_id,
        "title": book["title"],
        "author": book["author"],
        "cover_url": book["cover_url"],
        "catalog_status": "pending"
    }

        lookup = urllib.parse.quote(
        work_id, safe=""
    )

    existing = request(
        "books?select=id&open_library_work_id=eq."
        + lookup
    )

    if existing:
        rows = existing
    else:
        rows = request(
            "books?on_conflict=open_library_work_id",
            method="POST",
            data=payload,
            prefer="resolution=ignore-duplicates,return=representation"
        )

        if not rows:
            rows = request(
                "books?select=id&open_library_work_id=eq."
                + lookup
            )

    if not rows:
        raise RuntimeError(f"Book not saved: {work_id}")

    book_id = rows[0]["id"]

    for name in book["genres"]:
        if name not in genre_ids:
            raise RuntimeError(f"Unknown genre: {name}")

        request(
            "book_genres?on_conflict=book_id,genre_id",
            method="POST",
            data={"book_id": book_id, "genre_id": genre_ids[name]},
            prefer="resolution=ignore-duplicates,return=minimal"
        )

    saved += 1

print(f"Successfully imported {saved} books into Supabase.")
