# -*- coding: utf-8 -*-
"""
test_validate_heroes.py
Validates the 36 Hero books against all quality gate rules.
"""

import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"

BANNED = [
    "masterwork", "unmask", "dismantle", "radical clarity",
    "architecture of your attention", "safely mediocre",
    "the rabbit hole runs deep", "superficial trivia",
    "hyper-modern algorithmic world"
]

heroes = []
for fname in ["hero_mind.json", "hero_self.json", "hero_scifi.json"]:
    fpath = os.path.join(ROOT_DIR, "catalog", fname)
    with open(fpath, "r", encoding="utf-8") as f:
        books = json.load(f)
        heroes.extend(books)
        print(f"Loaded {len(books)} from {fname}")

print(f"Total hero books: {len(heroes)}")

# Check duplicate sentences (8+ words)
sentence_to_book = {}
dupes = []
banned_found = []
field_errors = []
short_sparks = []
long_hooks = []
hero_chapter_errors = []

for b in heroes:
    b_id = b["id"]
    chapters = b.get("chapters", [])
    if len(chapters) < 6:
        hero_chapter_errors.append(f"{b_id} has {len(chapters)} chapters (expected >= 6)")
    
    for ch in chapters:
        # Check fields
        for field in ["n", "title", "hook", "spark", "key_ideas", "line", "in_your_life", "connects_to", "spoiler_level"]:
            if field not in ch:
                field_errors.append(f"{b_id} ch {ch.get('n')} missing {field}")
        
        # Check spark lines
        lines = [l for l in ch.get("spark", "").split("\n") if l.strip()]
        if len(lines) < 6:
            short_sparks.append(f"{b_id} ch {ch.get('n')} spark has only {len(lines)} lines")
            
        # Check hook words
        hook_words = len(ch.get("hook", "").split())
        if hook_words > 18:
            long_hooks.append(f"{b_id} ch {ch.get('n')} hook has {hook_words} words")
            
        # Check banned
        full_text = json.dumps(ch, ensure_ascii=False).lower()
        for phrase in BANNED:
            if phrase in full_text:
                banned_found.append(f"{b_id} ch {ch.get('n')} contains banned phrase: '{phrase}'")
                
        # Sentences
        sentences = re.split(r'[.!?]+', ch.get("spark", "") + " " + " ".join(ch.get("in_your_life", [])))
        for s in sentences:
            clean = " ".join(s.strip().lower().split())
            words = clean.split()
            if len(words) >= 8:
                if clean in sentence_to_book and sentence_to_book[clean] != b_id:
                    dupes.append((clean, sentence_to_book[clean], b_id))
                else:
                    sentence_to_book[clean] = b_id

print("\n=== VALIDATION REPORT FOR 36 HERO BOOKS ===")
print(f"Hero Chapter Errors: {len(hero_chapter_errors)}")
for e in hero_chapter_errors: print(" ", e)

print(f"Missing Fields: {len(field_errors)}")
for e in field_errors: print(" ", e)

print(f"Short Sparks (<6 lines): {len(short_sparks)}")
for e in short_sparks: print(" ", e)

print(f"Long Hooks (>18 words): {len(long_hooks)}")
for e in long_hooks: print(" ", e)

print(f"Banned Phrases: {len(banned_found)}")
for e in banned_found: print(" ", e)

print(f"Duplicate Sentences (8+ words): {len(dupes)}")
for d in dupes: print(" ", d)
