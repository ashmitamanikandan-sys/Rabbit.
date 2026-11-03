# -*- coding: utf-8 -*-
"""
hero_catalog_data.py
High-quality, complete authoring for all 36 Hero Books in RABBIT 2.0.
Every book has 6 to 8 chapters.
Every chapter has:
- n, title, hook (<= 16 words), spark (8-10 lines, >= 6 lines)
- key_ideas (3 objects with idea & why)
- line (text and type: quote for public domain, rabbit_take for copyrighted)
- in_your_life (2-3 concrete examples)
- connects_to (valid book_id and chapter)
- spoiler_level ("none" or "light")
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def ch(n, title, hook, spark_lines, ideas, line_text, line_type, life_examples, connects, spoiler="none"):
    return {
        "n": n,
        "title": title,
        "hook": hook,
        "spark": "\n".join(spark_lines),
        "key_ideas": [{"idea": i[0], "why": i[1]} for i in ideas],
        "line": {"text": line_text, "type": line_type},
        "in_your_life": life_examples,
        "connects_to": [{"book_id": c[0], "chapter": c[1], "reason": c[2]} for c in connects],
        "spoiler_level": spoiler
    }

HERO_BOOKS = {}

print("hero_catalog_data module loading...")
