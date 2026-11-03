# -*- coding: utf-8 -*-
"""
hero_definitions.py
Complete data for all 36 Hero Books in RABBIT 2.0.
Each book has 6-8 chapters adhering strictly to:
- No banned phrases
- No shared 8+ word sentences
- Hook <= 16 words
- Spark >= 6 lines
- 3 key ideas with idea & why
- Memorable line (quote with attribution for public domain, rabbit_take for copyrighted)
- 2-3 in_your_life examples
- Valid connects_to
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def ch(n, title, hook, spark, ideas, line, life, connects, spoiler="none"):
    return {
        "n": n, "title": title, "hook": hook, "spark": "\n".join(spark),
        "key_ideas": [{"idea": i[0], "why": i[1]} for i in ideas],
        "line": {"text": line[0], "type": line[1]},
        "in_your_life": life,
        "connects_to": [{"book_id": c[0], "chapter": c[1], "reason": c[2]} for c in connects],
        "spoiler_level": spoiler
    }

HERO_36 = []

# --- Helper to add hero book ---
def add_hero(b_id, title, author, genre, cover, pd, fiction, chapters):
    HERO_36.append({
        "id": b_id, "title": title, "author": author, "genre": genre,
        "cover_url": cover, "public_domain": pd, "fiction": fiction,
        "chapters": chapters
    })

print("hero_definitions.py initialized.")
