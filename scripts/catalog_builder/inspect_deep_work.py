import json

with open("catalog/hero_mind.json", "r", encoding="utf-8") as f:
    books = json.load(f)

for b in books:
    if b["id"] == "deep-work":
        print(f"Deep work chapters: len={len(b['chapters'])}")
        print("Chapter 0:", b['chapters'][0])
