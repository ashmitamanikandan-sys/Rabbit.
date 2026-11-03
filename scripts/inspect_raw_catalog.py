import re
import json

with open('rabbit-genres-catalog.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Look for genres structure
genres = re.findall(r'genre:\s*["\']([^"\']+)["\']', content)
unique_genres = list(dict.fromkeys(genres))
print(f"Total genre matches: {len(genres)}")
print(f"Unique genres ({len(unique_genres)}): {unique_genres[:10]}")

# Look for books
ids = re.findall(r'id:\s*["\']([^"\']+)["\']', content)
print(f"Total book IDs found: {len(ids)}, Unique: {len(set(ids))}")
