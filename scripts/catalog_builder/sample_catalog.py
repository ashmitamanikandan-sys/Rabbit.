import json

with open("catalog/raw_catalog.json", "r", encoding="utf-8") as f:
    books = json.load(f)

print("Total books:", len(books))
# Sample 1 book from each of the 21 genres
seen = set()
for b in books:
    g = b.get("genre", "Unknown")
    if g not in seen:
        seen.add(g)
        print(f"[{g}] '{b.get('title')}' by {b.get('author')}")
