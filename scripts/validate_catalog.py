# -*- coding: utf-8 -*-
"""
validate_catalog.py
Official quality gate validator for RABBIT 2.0 Catalog.

Quality gate rules:
1. Fails if any two books share a sentence of 8+ words.
2. Fails if any banned phrase appears:
   - "masterwork"
   - "unmask"
   - "dismantle"
   - "radical clarity"
   - "architecture of your attention"
   - "safely mediocre"
   - "the rabbit hole runs deep"
   - "superficial trivia"
   - "hyper-modern algorithmic world"
3. Fails if a chapter is missing any deck field:
   (n, title, hook, spark, key_ideas, line, in_your_life, connects_to, spoiler_level)
   or if a spark is shorter than 6 lines.
4. Fails if connects_to points to a missing book or chapter.
5. Fails if a hero book has fewer than 6 chapters.
6. Fails if hook has more than 18 words.
"""

import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
CATALOG_PATH = os.path.join(ROOT_DIR, "catalog", "rabbit-catalog-v2.json")

BANNED = [
    "masterwork", "unmask", "dismantle", "radical clarity",
    "architecture of your attention", "safely mediocre",
    "the rabbit hole runs deep", "superficial trivia",
    "hyper-modern algorithmic world"
]

HERO_BOOKS = {
    # The Human Mind (12)
    "atomic-habits", "thinking-fast-and-slow", "the-psychology-of-money",
    "the-48-laws-of-power", "surrounded-by-idiots", "deep-work", "flow",
    "predictably-irrational", "the-power-of-habit", "influence-psychology-of-persuasion",
    "the-laws-of-human-nature", "nudge",
    # Self Discovery (12)
    "the-subtle-art-of-not-giving-a-fuck", "mans-search-for-meaning", "meditations",
    "thirukkural", "siddhartha", "gitanjali", "the-alchemist", "can-t-hurt-me",
    "the-courage-to-be-disliked", "the-mountain-is-you", "the-power-of-now", "the-untethered-soul",
    # Science Fiction (12)
    "dune", "frankenstein", "1984-george-orwell", "brave-new-world",
    "neuromancer", "the-three-body-problem", "foundation", "do-androids-dream-of-electric-sheep",
    "the-time-machine", "fahrenheit-451", "snow-crash", "i-robot"
}

REQUIRED_FIELDS = [
    "n", "title", "hook", "spark", "key_ideas", "line",
    "in_your_life", "connects_to", "spoiler_level"
]

def run_validation():
    print("==================================================")
    print("  RABBIT 2.0 Catalog Quality Gate Validator")
    print("==================================================\n")

    if not os.path.exists(CATALOG_PATH):
        print(f"FATAL: Catalog file not found at {CATALOG_PATH}")
        sys.exit(1)

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    print(f"Catalog loaded: {len(catalog)} books\n")

    book_map = {b["id"]: b for b in catalog}
    failures = []
    warnings = []

    # 1. Verify all 36 Hero Books present and have >= 6 chapters
    found_heroes = set()
    for b_id in HERO_BOOKS:
        if b_id not in book_map:
            failures.append(f"MISSING HERO BOOK: '{b_id}' not found in catalog")
        else:
            found_heroes.add(b_id)
            ch_count = len(book_map[b_id].get("chapters", []))
            if ch_count < 6:
                failures.append(f"HERO BOOK INCOMPLETE: '{b_id}' has {ch_count} chapters (must be >= 6)")

    print(f"Hero books verified: {len(found_heroes)} / {len(HERO_BOOKS)}")

    # 2. Check each chapter in all books
    sentence_to_book = {}
    dupe_sentences = []

    total_chapters = 0

    for b in catalog:
        b_id = b.get("id", "UNKNOWN")
        chapters = b.get("chapters", [])
        if not chapters or not isinstance(chapters, list):
            failures.append(f"Book '{b_id}' has no valid chapters list")
            continue

        total_chapters += len(chapters)

        for ch in chapters:
            n = ch.get("n", "?")

            # Check required fields
            for rf in REQUIRED_FIELDS:
                if rf not in ch:
                    failures.append(f"Book '{b_id}' ch {n} missing field: '{rf}'")

            # Check spark line count (>= 6)
            spark = ch.get("spark", "")
            lines = [l for l in spark.split("\n") if l.strip()]
            if len(lines) < 6:
                failures.append(f"Book '{b_id}' ch {n} spark too short: {len(lines)} lines (must be >= 6)")

            # Check hook length (<= 18 words)
            hook = ch.get("hook", "")
            words = hook.split()
            if len(words) > 18:
                failures.append(f"Book '{b_id}' ch {n} hook too long: {len(words)} words (max 18)")

            # Check banned phrases
            ch_str = json.dumps(ch, ensure_ascii=False).lower()
            for bp in BANNED:
                if bp in ch_str:
                    failures.append(f"Book '{b_id}' ch {n} contains banned phrase: '{bp}'")

            # Check connects_to validity
            connects = ch.get("connects_to", [])
            for conn in connects:
                target_id = conn.get("book_id")
                target_ch = conn.get("chapter")
                if target_id not in book_map:
                    failures.append(f"Book '{b_id}' ch {n} connects_to missing target book: '{target_id}'")
                else:
                    target_ch_count = len(book_map[target_id].get("chapters", []))
                    if target_ch > target_ch_count:
                        failures.append(f"Book '{b_id}' ch {n} connects to invalid ch {target_ch} in '{target_id}' (has {target_ch_count})")

            # Check sentence duplication (>= 8 words)
            text_corpus = spark + " " + " ".join(ch.get("in_your_life", []))
            raw_sentences = re.split(r'[.!?]+', text_corpus)
            for raw_s in raw_sentences:
                clean_s = " ".join(raw_s.strip().lower().split())
                s_words = clean_s.split()
                if len(s_words) >= 8:
                    if clean_s in sentence_to_book:
                        prev_book = sentence_to_book[clean_s]
                        if prev_book != b_id:
                            dupe_sentences.append((clean_s, prev_book, b_id))
                    else:
                        sentence_to_book[clean_s] = b_id

    print(f"Total chapters validated: {total_chapters}")
    print(f"Total unique 8+ word sentences indexed: {len(sentence_to_book)}")

    if dupe_sentences:
        failures.append(f"Found {len(dupe_sentences)} duplicate sentence(s) of 8+ words across books")
        for ds in dupe_sentences[:5]:
            print(f"  DUPE: '{ds[0]}' in '{ds[1]}' and '{ds[2]}'")

    print("\n--------------------------------------------------")
    print(f"Total Quality Gate Failures: {len(failures)}")
    print(f"Total Warnings: {len(warnings)}")
    print("--------------------------------------------------\n")

    if failures:
        print("FAILURES DETECTED:")
        for f in failures[:20]:
            print("  ❌", f)
        if len(failures) > 20:
            print(f"  ... and {len(failures) - 20} more failures.")
        sys.exit(1)
    else:
        print("✅ QUALITY GATE PASSED 100%! All rules satisfied with zero errors.")
        sys.exit(0)

if __name__ == "__main__":
    run_validation()
