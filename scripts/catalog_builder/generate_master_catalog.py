# -*- coding: utf-8 -*-
"""
generate_master_catalog.py
Builds the complete, rich, validated RABBIT 2.0 Catalog:
1. 36 Hand-crafted Hero Books (12 Human Mind, 12 Self Discovery, 12 Science Fiction) with 6-8 chapters each.
2. 1,014 Catalog Books (>= 3 unique chapters each).
3. Zero banned phrases, zero 8+ word sentence collisions.
4. Fully validated connects_to graph.
5. Emits catalog/rabbit-catalog-v2.json, modular genre files, and rabbit-catalog-v2.js.
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

BANNED_PHRASES = [
  "masterwork",
  "unmask",
  "dismantle",
  "radical clarity",
  "architecture of your attention",
  "safely mediocre",
  "the rabbit hole runs deep",
  "superficial trivia",
  "hyper-modern algorithmic world"
]

print("Starting RABBIT 2.0 Catalog Compilation...")
