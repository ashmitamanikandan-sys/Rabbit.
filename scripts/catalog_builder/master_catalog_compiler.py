# -*- coding: utf-8 -*-
"""
master_catalog_compiler.py
Compiles the full 36 Hero Books and all 1,014 other catalog books.
Exports:
- catalog/rabbit-catalog-v2.json
- catalog/genres/*.js
- rabbit-catalog-v2.js (with compatibility adapter)
Runs validation gate at the end.
"""

import sys
import json
import re
import os
import hashlib

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
CATALOG_DIR = os.path.join(ROOT_DIR, "catalog")
GENRES_DIR = os.path.join(CATALOG_DIR, "genres")
os.makedirs(GENRES_DIR, exist_ok=True)

def ch(n, title, hook, spark, ideas, line, life, connects, spoiler="none"):
    return {
        "n": n, "title": title, "hook": hook, "spark": "\n".join(spark),
        "key_ideas": [{"idea": i[0], "why": i[1]} for i in ideas],
        "line": {"text": line[0], "type": line[1]},
        "in_your_life": life,
        "connects_to": [{"book_id": c[0], "chapter": c[1], "reason": c[2]} for c in connects],
        "spoiler_level": spoiler
    }

ALL_HERO_BOOKS = []

# Load Human Mind (12 books)
mind_path = os.path.join(CATALOG_DIR, "hero_mind.json")
if os.path.exists(mind_path):
    with open(mind_path, "r", encoding="utf-8") as f:
        ALL_HERO_BOOKS.extend(json.load(f))
    print(f"Loaded {len(ALL_HERO_BOOKS)} Human Mind hero books.")

# Load Self Discovery initial (3 books)
self_path = os.path.join(CATALOG_DIR, "hero_self.json")
if os.path.exists(self_path):
    with open(self_path, "r", encoding="utf-8") as f:
        ALL_HERO_BOOKS.extend(json.load(f))
    print(f"Total hero books loaded: {len(ALL_HERO_BOOKS)}")
