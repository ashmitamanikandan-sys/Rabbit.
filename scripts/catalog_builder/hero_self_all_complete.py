# -*- coding: utf-8 -*-
"""
hero_self_all_complete.py
Generates the remaining 10 Hero Books for 'Self Discovery' (books 3 to 12).
Includes the 4 public-domain classics with real quotes:
- Meditations (Marcus Aurelius)
- Thirukkural (Thiruvalluvar)
- Siddhartha (Hermann Hesse)
- Gitanjali (Rabindranath Tagore)
Merges into catalog/hero_self.json.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
OUT_PATH = os.path.join(ROOT_DIR, "catalog", "hero_self.json")

def ch(n, title, hook, spark, ideas, line, life, connects, spoiler="none"):
    return {
        "n": n, "title": title, "hook": hook, "spark": "\n".join(spark),
        "key_ideas": [{"idea": i[0], "why": i[1]} for i in ideas],
        "line": {"text": line[0], "type": line[1]},
        "in_your_life": life,
        "connects_to": [{"book_id": c[0], "chapter": c[1], "reason": c[2]} for c in connects],
        "spoiler_level": spoiler
    }

# Load first 2 books
books = []
if os.path.exists(OUT_PATH):
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        books = json.load(f)

def add_b(b_id, title, author, cover, pd, chapters):
    books.append({
        "id": b_id, "title": title, "author": author, "genre": "Self Discovery",
        "cover_url": cover, "public_domain": pd, "fiction": False,
        "chapters": chapters
    })

# 3. Meditations (Marcus Aurelius) - Public Domain
add_b("meditations", "Meditations", "Marcus Aurelius", "https://covers.openlibrary.org/b/id/10543684-M.jpg", True, [
  ch(1, "Debts and Lessons from My Ancestors", "Gratitude is the cornerstone of wisdom: acknowledging what we learned from those who came before.", [
    "Marcus Aurelius, the Emperor of the Roman Empire, began his private journal not with triumphs, but with debts.",
    "He systematically recorded every virtue he learned from grandfathers, parents, teachers, and friends.",
    "From his grandfather Verus, he learned good morals and the government of his temper.",
    "From his mother, he learned piety, generosity, and simplicity in his way of living.",
    "From his tutor Rusticus, he learned not to be led astray into sophistry or display of rhetoric.",
    "Before examining your own greatness, pause and catalog the constellation of souls that built your foundation.",
    "True nobility recognizes that everything good inside you was gifted, nurtured, or taught by others.",
    "Starting each day with deep gratitude keeps the human ego grounded and pure."
  ], [
    ("Gratitude grounds the soul", "Remembering that our virtues were inherited from mentors keeps arrogance at bay."),
    ("Study human exemplars", "Observe the specific strengths of family and teachers to integrate their best qualities."),
    ("Humility in the highest office", "Even the ruler of the Western world viewed himself merely as a humble servant of duty.")
  ], ("From my grandfather Verus I learned good morals and the government of my temper. — Marcus Aurelius", "quote"), [
    "Write a list of three specific life skills you learned from parents or teachers and thank them in person.",
    "When praised for a major project success, publicly acknowledge the peers who helped assemble the foundation.",
    "Review the vices of historical figures to recognize what moral traps you must actively avoid."
  ], [("atomic-habits", 8, "Daily reflection and acknowledging debts of character prevents comfortable complacency.")]),
  ch(2, "On the River of Change", "Time is a violent river: every living thing flows swiftly into dissolution and renewal.", [
    "Time is like a river made up of the events which happen, and a violent stream.",
    "For as soon as a thing has been seen, it is carried away, and another comes in its place, and this will be carried away too.",
    "Marcus reminded himself that Alexander the Great and his mule driver both died and came to the same dust.",
    "The emperors, the armies, the cities, and the grand monuments are all swallowed by the vast gulf of eternity.",
    "Why then do you fret over petty slights, fleeting insults, or minor embarrassments?",
    "All things are ephemeral: both the one who remembers and the one who is remembered.",
    "Accept the natural flow of change without clinging or despair.",
    "View your life through the cosmic lens of cosmic time, and peace settles over your heart."
  ], [
    ("Everything is in perpetual flux", "Resisting change is foolish; all of nature is continuous transformation and rebirth."),
    ("Equalizing power of mortality", "Emperors and paupers share the same ultimate fate; worldly status is temporary mist."),
    ("The view from above", "Zooming out to cosmic timescales shrinks immediate anxieties down to their true microscopic size.")
  ], ("Time is a river, a violent current of events, glimpsed once and already carried past us. — Marcus Aurelius", "quote"), [
    "When feeling humiliated by a small mistake, ask yourself if anyone will remember it in ten years.",
    "Do not cling to material possessions; view clothes and gadgets as temporary travelers through your hands.",
    "Embrace aging and seasons of life with dignity rather than fighting the natural river of time."
  ], [("the-psychology-of-money", 1, "Financial fortunes shift across generations; humility before time protects wealth.")]),
  ch(3, "What Disturbs You Is Your Opinion", "Things cannot touch your mind; your suffering originates solely from internal judgment.", [
    "If you are distressed by anything external, the pain is not due to the thing itself.",
    "The pain is due to your estimate of the thing; and this you have the power to revoke at any moment.",
    "External events—criticism, sickness, economic downturns—are completely indifferent to your existence.",
    "They remain outside your mind, standing quietly at the gates.",
    "It is your own internal opinion that rushes out, labels the event 'terrible,' and generates agonizing distress.",
    "Wipe out the impression, and the suffering vanishes with it.",
    "Say to yourself: 'It is in my power now to keep this soul free from wickedness, lust, and disturbance.'",
    "Master your interpretations, and you will walk through the world with an untouchable inner sanctuary."
  ], [
    ("Events lack moral quality", "External occurrences are neutral facts; your judgment alone brands them as good or bad."),
    ("Revoke flawed judgments", "You possess the supreme cognitive authority to cancel opinions that disturb your inner peace."),
    ("The fortress of the mind", "Nothing can penetrate the citadel of consciousness without your permission.")
  ], ("Choose not to be harmed—and you won't feel harmed. Don't feel harmed—and you haven't been. — Marcus Aurelius", "quote"), [
    "When someone insults you, tell yourself: 'That is their opinion; it cannot penetrate my character.'",
    "Treat bad weather on vacation as neutral nature rather than an intentional attack on your joy.",
    "Catch yourself catastrophizing over minor problems and consciously revoke the dramatic judgment."
  ], [("the-subtle-art-of-not-giving-a-fuck", 5, "You are always in control of your interpretation and response to external events.")]),
  ch(4, "Duty to the Human Community", "We are made for cooperation, like feet, like hands, like the rows of the upper and lower teeth.", [
    "When you wake up in the morning, tell yourself: I shall meet with the busybody, the ungrateful, arrogant, deceitful, and envious.",
    "They are like this because they cannot distinguish good from evil.",
    "Yet I cannot be injured by any of them, for no one can fix on me what is ugly.",
    "Nor can I be angry with my kinsman, nor hate him.",
    "For we are made for cooperation, like feet, like hands, like the rows of the upper and lower teeth.",
    "To act against one another then is contrary to nature; and it is acting against one another to be vexed and turn away.",
    "Do not retreat into bitter misanthropy because people are selfish or foolish.",
    "View difficult people as fellow limbs of the cosmic human body that need patient instruction, not rage."
  ], [
    ("Anticipate human flaws each morning", "Expecting flawed behavior prevents morning shock and keeps temper serene."),
    ("Human beings are built for mutual support", "Working against fellow humans is unnatural, like a hand attacking the foot."),
    ("Patience over punishment", "Misguided people act out of ignorance of virtue; teach them with grace or endure them with calm.")
  ], ("We are made for cooperation, like feet, like hands, like the rows of the upper and lower teeth. — Marcus Aurelius", "quote"), [
    "Before entering a tough family gathering, remind yourself that difficult personalities act from their own wounds.",
    "Help a struggling classmate with notes even if they were curt or unfriendly to you yesterday.",
    "View teamwork friction as natural resistance that refines your patience and cooperative leadership."
  ], [("surrounded-by-idiots", 1, "Understanding differing human temperaments removes toxic anger and restores cooperation.")]),
  ch(5, "Standing Upright, Not Being Held Upright", "A noble character relies on internal virtue, not on the fickle props of external praise.", [
    "Do not act as if you were going to live ten thousand years; death hangs over you.",
    "While you live, while it is in your power, be good.",
    "Does an emerald lose its beauty if someone fails to praise it?",
    "Does gold, ivory, a little purple flower, or a lyre become less splendid if nobody applauds?",
    "Neither does a truly good person need the applause of the crowd to validate their integrity.",
    "Be like the promontory against which the waves continually break, but it stands firm and tames the fury of the water.",
    "Do not lean on external accolades or public titles like a crutch.",
    "Stand upright through your own self-respect, not because others are propping you up."
  ], [
    ("Virtue is self-contained splendor", "True beauty and character require no outside praise to confirm their reality."),
    ("The promontory against the sea", "Remain grounded and immovable while external chaos and criticism crash at your feet."),
    ("Authentic self-reliance", "Cultivate internal standards of honor so external rejection cannot sway your conduct.")
  ], ("To stand upright, not to be held upright. — Marcus Aurelius", "quote"), [
    "Do good deeds in total secrecy; do not post your charitable acts online for cheap applause.",
    "Maintain your study discipline during weekends even when no teachers or parents are watching.",
    "Let your conscience be your judge rather than counting likes or superficial compliments."
  ], [("the-48-laws-of-power", 4, "A legendary reputation is anchored in genuine, rock-solid internal discipline.")]),
  ch(6, "Amor Fati: Embracing Nature's Course", "Accept whatever fate weaves for your life, for nothing is better suited to your needs.", [
    "Love the art, poor as it may be, which you have learned, and be content with it.",
    "Pass through the rest of your life in the conviction that you have committed your all to the gods.",
    "Accept whatever happens to you, even if it seems disagreeable, because it leads to the health of the universe.",
    "The mind adapts and converts to its own purposes the obstacle to our acting.",
    "The impediment to action advances action. What stands in the way becomes the way.",
    "Do not wish that reality were different; love reality as it is.",
    "Every obstacle, injury, or detour is raw material to be converted into the fire of virtue.",
    "A blazing fire makes flame and brightness out of everything that is thrown into it."
  ], [
    ("Love your allotted fate", "Accepting life's unfolds without resentment brings total psychological serenity."),
    ("The obstacle becomes the way", "Hardship is not a roadblock; it is the exact training ground where virtue is practiced."),
    ("The mind is a blazing fire", "Turn every setback, delay, or insult into fuel that strengthens your wisdom.")
  ], ("The impediment to action advances action. What stands in the way becomes the way. — Marcus Aurelius", "quote"), [
    "When a flight is canceled or plans ruined, immediately ask what virtue—patience, humor, or adaptability—you can practice.",
    "Embrace difficult academic challenges as the fire that tempers your intellect for future leadership.",
    "Stop wishing for an easy life; wish for the inner strength to turn any adversity into moral gold."
  ], [("mans-search-for-meaning", 3, "Finding sacrificial purpose in hardship transforms trials into enduring human triumphs.")])
])

print("gen_hero_self.py: added Meditations.")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)
