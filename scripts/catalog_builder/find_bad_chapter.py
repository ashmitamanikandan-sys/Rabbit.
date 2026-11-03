import json
import os

for fname in ["hero_mind.json", "hero_self.json", "hero_scifi.json"]:
    with open(os.path.join("catalog", fname), "r", encoding="utf-8") as f:
        books = json.load(f)
        for b in books:
            chs = b.get("chapters", [])
            for i, c in enumerate(chs):
                if not isinstance(c, dict):
                    print(f"ERROR in {fname}: book '{b['id']}' chapter {i} is type {type(c)}")
print("Check complete.")
