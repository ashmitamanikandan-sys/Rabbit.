# -*- coding: utf-8 -*-
"""
extract_catalog.py
Extracts all raw books from rabbit-genres-catalog.js.
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("rabbit-genres-catalog.js", "r", encoding="utf-8") as f:
    text = f.read()

# Match window.RABBIT_GENRES_CATALOG["..."] = [ ... ];
genre_blocks = re.findall(r'window\.RABBIT_GENRES_CATALOG\["([^"]+)"\]\s*=\s*(\[[\s\S]*?\]);', text)

print(f"Found {len(genre_blocks)} genre blocks.")

all_raw_books = []
genres_map = {}

for gname, block in genre_blocks:
    try:
        books_list = json.loads(block)
        genres_map[gname] = books_list
        all_raw_books.extend(books_list)
        print(f"Genre: '{gname}' -> {len(books_list)} books")
    except Exception as e:
        print(f"Error parsing genre '{gname}':", e)

print(f"Total raw books extracted: {len(all_raw_books)}")

with open("catalog/raw_catalog.json", "w", encoding="utf-8") as f:
    json.dump(all_raw_books, f, indent=2, ensure_ascii=False)

print("Saved to catalog/raw_catalog.json")
