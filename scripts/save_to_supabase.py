"""Import candidate books and genre links without publishing unreviewed records."""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

BASE = os.environ["SUPABASE_URL"].rstrip("/")
KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
HEADERS = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
}

def request(path, method="GET", data=None, prefer=None):
    headers = dict(HEADERS)
    if prefer:
        headers["Prefer"] = prefer
    payload = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(BASE + "/rest/v1/" + path, data=payload,
                                 headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else []
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:1200]
        raise RuntimeError(f"Supabase HTTP {error.code} on {method} {path}: {detail}") from error

def chunks(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]

with open("rabbit_books_preview.json", encoding="utf-8") as source:
    books = json.load(source)

genres = request("genres?select=id,name")
genre_ids = {genre["name"]: genre["id"] for genre in genres}
for book in books:
    for name in book["genres"]:
        if name not in genre_ids:
            raise RuntimeError(f"Missing genre in Supabase: {name}")

saved = 0
for group in chunks(books, 40):
    ids = [book["open_library_work_id"] for book in group]
    encoded = urllib.parse.quote(",".join('"' + work_id + '"' for work_id in ids), safe=",()")
    existing = request("books?select=id,open_library_work_id&open_library_work_id=in.(" + encoded + ")")
    by_work = {row["open_library_work_id"]: row["id"] for row in existing}
    new_books = [{
        "open_library_work_id": book["open_library_work_id"],
        "title": book["title"],
        "author": book["author"],
        "cover_url": book["cover_url"],
        "catalog_status": "pending",
    } for book in group if book["open_library_work_id"] not in by_work]
    if new_books:
        inserted = request("books?select=id,open_library_work_id", method="POST",
                           data=new_books, prefer="return=representation")
        by_work.update({row["open_library_work_id"]: row["id"] for row in inserted})
    links = []
    for book in group:
        book_id = by_work.get(book["open_library_work_id"])
        if not book_id:
            raise RuntimeError("Missing imported book ID: " + book["open_library_work_id"])
        for name in book["genres"]:
            links.append({"book_id": book_id, "genre_id": genre_ids[name]})
    for link_group in chunks(links, 100):
        request("book_genres?on_conflict=book_id,genre_id", method="POST",
                data=link_group, prefer="resolution=ignore-duplicates,return=minimal")
    saved += len(group)
    print(f"Saved {saved}/{len(books)} candidate books (pending review)", flush=True)

print(f"Imported or confirmed {saved} book candidates. None published automatically.")
