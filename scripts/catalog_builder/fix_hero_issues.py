# -*- coding: utf-8 -*-
"""
fix_hero_issues.py
Fixes the 3 banned words and 11 long hooks in the hero files.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"

# 1. Fix hero_mind.json: the-power-of-habit ch 6 ('dismantle')
# and long hooks in influence
with open(os.path.join(ROOT_DIR, "catalog", "hero_mind.json"), "r", encoding="utf-8") as f:
    mind_books = json.load(f)

for b in mind_books:
    if b["id"] == "the-power-of-habit":
        for ch in b["chapters"]:
            txt = json.dumps(ch, ensure_ascii=False)
            txt = txt.replace("dismantle", "transform").replace("Dismantle", "Transform")
            ch.clear()
            ch.update(json.loads(txt))
    if b["id"] == "influence-psychology-of-persuasion":
        for ch in b["chapters"]:
            if ch["n"] == 3:
                ch["hook"] = "We look to others to define reality: when uncertain, the herd dictates our choices."
            elif ch["n"] == 4:
                ch["hook"] = "The halo effect: we unconsciously assign talent and honesty to attractive individuals."

with open(os.path.join(ROOT_DIR, "catalog", "hero_mind.json"), "w", encoding="utf-8") as f:
    json.dump(mind_books, f, indent=2, ensure_ascii=False)
print("Updated hero_mind.json")

# 2. Fix hero_self.json: the-mountain-is-you ch 1 ('unmask')
# and long hooks in subtle-art, thirukkural, gitanjali
with open(os.path.join(ROOT_DIR, "catalog", "hero_self.json"), "r", encoding="utf-8") as f:
    self_books = json.load(f)

for b in self_books:
    if b["id"] == "the-mountain-is-you":
        for ch in b["chapters"]:
            txt = json.dumps(ch, ensure_ascii=False)
            txt = txt.replace("Unmasking", "Revealing").replace("unmasking", "revealing").replace("unmask", "reveal")
            ch.clear()
            ch.update(json.loads(txt))
    if b["id"] == "the-subtle-art-of-not-giving-a-fuck":
        for ch in b["chapters"]:
            if ch["n"] == 5:
                ch["hook"] = "You cannot control every circumstance, but you always choose how you respond to events."
    if b["id"] == "thirukkural":
        for ch in b["chapters"]:
            if ch["n"] == 6:
                ch["hook"] = "True friendship is a steady hand that rushes to catch you when you stumble."
    if b["id"] == "gitanjali":
        for ch in b["chapters"]:
            if ch["n"] == 3:
                ch["hook"] = "Open your eyes: divine truth lives out where the honest laborer tills the soil."
            elif ch["n"] == 5:
                ch["hook"] = "The wanderer knocks on every distant door before discovering the quiet sanctuary within."
            elif ch["n"] == 6:
                ch["hook"] = "At life's close, let every song and action gather into one quiet salutation."

with open(os.path.join(ROOT_DIR, "catalog", "hero_self.json"), "w", encoding="utf-8") as f:
    json.dump(self_books, f, indent=2, ensure_ascii=False)
print("Updated hero_self.json")

# 3. Fix hero_scifi.json: fahrenheit-451 ch 3 ('superficial trivia')
# and long hooks in brave-new-world, fahrenheit-451
with open(os.path.join(ROOT_DIR, "catalog", "hero_scifi.json"), "r", encoding="utf-8") as f:
    scifi_books = json.load(f)

for b in scifi_books:
    if b["id"] == "fahrenheit-451":
        for ch in b["chapters"]:
            txt = json.dumps(ch, ensure_ascii=False)
            txt = txt.replace("superficial trivia", "hollow trivia")
            ch.clear()
            ch.update(json.loads(txt))
            if ch["n"] == 1:
                ch["hook"] = "It was a pleasure to burn: kerosene was perfume to firemen incinerating forbidden books."
            elif ch["n"] == 2:
                ch["hook"] = "The magic is not in paper; it is in what courageous books honestly speak."
            elif ch["n"] == 3:
                ch["hook"] = "To make people happy, give them one simple answer instead of two worrying sides."
    if b["id"] == "brave-new-world":
        for ch in b["chapters"]:
            if ch["n"] == 6:
                ch["hook"] = "Give me the right to catch sickness, the right to endure sorrow and pains."

with open(os.path.join(ROOT_DIR, "catalog", "hero_scifi.json"), "w", encoding="utf-8") as f:
    json.dump(scifi_books, f, indent=2, ensure_ascii=False)
print("Updated hero_scifi.json")
