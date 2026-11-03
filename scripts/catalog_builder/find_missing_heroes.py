import json

with open("catalog/raw_catalog.json", "r", encoding="utf-8") as f:
    raw = json.load(f)
raw_ids = {b["id"] for b in raw}

import os
hero_ids = set()
for hf in ["hero_mind.json", "hero_self.json", "hero_scifi.json"]:
    with open(os.path.join("catalog", hf), "r", encoding="utf-8") as f:
        for b in json.load(f):
            hero_ids.add(b["id"])

missing_in_raw = hero_ids - raw_ids
print("Hero IDs missing in raw catalog IDs:", missing_in_raw)

# Let's search raw books for matching titles
for m in missing_in_raw:
    print(f"\nLooking for matches for '{m}':")
    for b in raw:
        if m in b["id"] or b["id"] in m:
            print(f"  found id: '{b['id']}', title: '{b['title']}'")
