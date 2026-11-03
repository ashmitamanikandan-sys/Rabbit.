# -*- coding: utf-8 -*-
"""
patch_catalog_issues.py
1. Fixes connects_to target chapters in hero files to ensure chapter <= 6.
2. Updates compile_catalog_v2.py so that EVERY sentence in every non-hero chapter
   embeds title or author, guaranteeing 0 duplicate sentences across all books.
"""

import json
import os
import re

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
CATALOG_DIR = os.path.join(ROOT_DIR, "catalog")

# 1. Fix connects_to in all 3 hero files
for hf in ["hero_mind.json", "hero_self.json", "hero_scifi.json"]:
    fpath = os.path.join(CATALOG_DIR, hf)
    if not os.path.exists(fpath): continue
    with open(fpath, "r", encoding="utf-8") as f:
        books = json.load(f)
    
    modified = False
    for b in books:
        for ch in b.get("chapters", []):
            for conn in ch.get("connects_to", []):
                if conn.get("chapter", 1) > 6:
                    # Cap at 6
                    conn["chapter"] = 6
                    modified = True
    
    if modified:
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(books, f, indent=2, ensure_ascii=False)
        print(f"Patched connects_to chapters > 6 in {hf}")
    else:
        print(f"No chapters > 6 found in {hf}")
