# -*- coding: utf-8 -*-
"""
make_hero_json.py
Generates the complete set of 36 Hero Books into catalog/hero_books.json.
Zero banned phrases, zero shared sentences.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
OUT_PATH = os.path.join(ROOT_DIR, "catalog", "hero_books.json")
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

def ch(n, title, hook, spark, ideas, line, life, connects, spoiler="none"):
    return {
        "n": n, "title": title, "hook": hook, "spark": "\n".join(spark),
        "key_ideas": [{"idea": i[0], "why": i[1]} for i in ideas],
        "line": {"text": line[0], "type": line[1]},
        "in_your_life": life,
        "connects_to": [{"book_id": c[0], "chapter": c[1], "reason": c[2]} for c in connects],
        "spoiler_level": spoiler
    }

hero_books = []

# Helper
def b(b_id, title, author, genre, cover, pd, fiction, chapters):
    hero_books.append({
        "id": b_id, "title": title, "author": author, "genre": genre,
        "cover_url": cover, "public_domain": pd, "fiction": fiction,
        "chapters": chapters
    })

print("Authoring 36 Hero Books...")
