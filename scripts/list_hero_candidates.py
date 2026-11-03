import json
import re

with open(r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app\rabbit-genres-catalog.js", "r", encoding="utf-8") as f:
    text = f.read()

def get_genre_books(genre_key):
    m = re.search(r'window\.RABBIT_GENRES_CATALOG\["' + re.escape(genre_key) + r'"\]\s*=\s*\[(.*?)\];', text, re.DOTALL)
    if not m:
        return []
    items = []
    # match each object { ... }
    raw = m.group(1)
    # find all "id": "...", "title": "...", "author": "..."
    matches = re.findall(r'\{\s*"id":\s*"([^"]+)",\s*"title":\s*"([^"]+)",\s*"author":\s*"([^"]+)"', raw)
    return matches

for g in ["the human mind", "self discovery", "science fiction", "classics", "philosophy"]:
    books = get_genre_books(g)
    print(f"=== {g} ({len(books)} books) ===")
    for b in books[:15]:
        print(f"  - {b[0]}: {b[1]} by {b[2]}")
