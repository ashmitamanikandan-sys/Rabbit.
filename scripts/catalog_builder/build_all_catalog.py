# -*- coding: utf-8 -*-
"""
build_all_catalog.py
Master compiler for RABBIT 2.0 Catalog.
Builds:
- 36 Hand-crafted Hero Books (6-10 chapters each)
- 1,014 Curated Catalog Books (>= 3 chapters each)
- Zero banned phrases, zero 8+ word sentence collisions
- Valid connects_to graph
- Writes catalog/rabbit-catalog-v2.json, catalog/genres/*.js, and rabbit-catalog-v2.js
"""

import sys
import json
import re
import os

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

print("Building RABBIT 2.0 Master Catalog...")
