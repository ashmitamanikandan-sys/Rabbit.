# -*- coding: utf-8 -*-
"""
make_hero_self_12.py
Compiles the complete set of 12 Self Discovery Hero Books:
1. the-subtle-art-of-not-giving-a-fuck
2. mans-search-for-meaning
3. meditations (Public Domain)
4. thirukkural (Public Domain)
5. siddhartha (Public Domain)
6. gitanjali (Public Domain)
7. the-alchemist
8. can-t-hurt-me
9. the-courage-to-be-disliked
10. the-mountain-is-you
11. the-power-of-now
12. the-untethered-soul
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

books = []

# Load the 3 from gen_hero_self.py: subtle-art, mans-search, meditations
# And the 3 from add_remaining_heroes.py: thirukkural, siddhartha, gitanjali
# Let's import or load them directly
from gen_hero_self import books as part_a
books.extend(part_a)

from hero_self_complete import books as part_b
for b in part_b:
    if not any(x["id"] == b["id"] for x in books):
        books.append(b)

def add_b(b_id, title, author, cover, pd, chapters):
    if not any(x["id"] == b_id for x in books):
        books.append({
            "id": b_id, "title": title, "author": author, "genre": "Self Discovery",
            "cover_url": cover, "public_domain": pd, "fiction": False,
            "chapters": chapters
        })

# 7. The Alchemist (Paulo Coelho)
add_b("the-alchemist", "The Alchemist", "Paulo Coelho", "https://covers.openlibrary.org/b/id/10543692-M.jpg", False, [
  ch(1, "The Boy and the Shepherd's Dream", "When you want something, all the universe conspires in helping you to achieve it.", [
    "Santiago was an Andalusian shepherd boy who loved his sheep and the open pastures of Spain.",
    "Yet beneath his quiet life, a recurring dream of treasure at the Egyptian pyramids troubled his heart.",
    "He met Melchizedek, the mysterious King of Salem, who introduced him to the concept of the Personal Legend.",
    "A Personal Legend is what you have always wanted to accomplish since childhood.",
    "When you are young, everything is clear and possible; you are not afraid to dream of grand adventures.",
    "As time passes, a mysterious force convinces you that your dream is impossible.",
    "Melchizedek told him: when you want something, all the universe conspires in helping you to achieve it.",
    "Santiago chose to sell his flock and set sail across the strait to Africa in pursuit of his destiny."
  ], [
    ("The Personal Legend calls each soul", "Everyone has a unique purpose, but fear of failure convinces adults to settle."),
    ("The universe conspires to assist", "When you commit with single-minded devotion, unexpected synchronicities emerge."),
    ("Give up the good for the great", "Santiago had to surrender the comfortable safety of his flock to cross the sea.")
  ], ("When you want something, all the universe conspires in helping you to achieve it.", "rabbit_take"), [
    "Identify the childhood passion you abandoned because adults labeled it impractical.",
    "Take one concrete risk toward your real dream rather than staying safe in comfortable routines.",
    "Notice the small signs and encouragements that appear when you finally take action."
  ], [("siddhartha", 1, "Leaving behind comfortable pastoral life to pursue inner calling echoes Siddhartha's departure.")]),
  ch(2, "The Crystal Merchant in Tangier", "Beware of the dream that becomes a comfortable excuse to avoid living fully.", [
    "Upon arriving in Tangier, Santiago was robbed of all his gold by an untrustworthy guide.",
    "Penniless and stranded in a foreign land, he took a job cleaning glassware in a crystal shop atop a hill.",
    "He worked diligently for a year, learning Arabic, expanding sales, and serving mint tea in crystal glasses.",
    "The crystal merchant was an elderly Muslim man who had dreamed of making the pilgrimage to Mecca for thirty years.",
    "Yet when Santiago asked why he did not go now that business was booming, the merchant hesitated.",
    "The merchant confessed: 'I am afraid that if my dream is realized, I will have no reason to go on living.'",
    "He preferred the fantasy of Mecca to the reality of making the journey.",
    "Do not let your dream become a museum piece; dreams are meant to be walked, tested, and lived."
  ], [
    ("The fear of realizing dreams", "Some people cling to fantasies because reality threatens the comforting illusion."),
    ("Turn setbacks into stepping stones", "Being robbed forced Santiago to learn commerce and foreign languages in Tangier."),
    ("Action cures despair", "Hard work in the crystal shop transformed an initial catastrophe into rich savings.")
  ], ("It is the fear of failure that makes a dream impossible to achieve.", "rabbit_take"), [
    "Notice if you procrastinate on your biggest ambition because failing would destroy your ego.",
    "Take practical part-time jobs when money runs short without losing sight of your ultimate north star.",
    "Test your creative ideas in public rather than keeping them safely unjudged in private notebooks."
  ], [("the-subtle-art-of-not-giving-a-fuck", 1, "Accepting real negative experiences is the prerequisite for authentic achievement.")]),
  ch(3, "The Desert Caravan", "The desert is a vast teacher: listen to the language of omens and the soul of the world.", [
    "Having earned back his fortune, Santiago joined a massive desert caravan traveling toward the pyramids.",
    "In the caravan, he met an Englishman who read heavy leather-bound books on alchemy all day.",
    "While the Englishman sought the secret of alchemy through books, Santiago observed the desert.",
    "He learned from the camel driver that the desert has a soul, and that everything is connected.",
    "The Soul of the World is nourished by the happiness of people, or by their unhappiness and envy.",
    "To realize one's destiny is a person's only real obligation.",
    "The Englishman learned that books without observation are dry, and Santiago learned that books hold history.",
    "Both realized that all things speak a single universal language of passion and courage."
  ], [
    ("The Soul of the World connects all beings", "Nature, people, and events are linked by an invisible web of meaning."),
    ("Complementary paths of learning", "Scholarly study and direct physical observation must inform and balance each other."),
    ("The language of omens", "Observing subtle patterns in surroundings reveals guidance when facing crossroads.")
  ], ("To realize one's destiny is a person's only real obligation.", "rabbit_take"), [
    "Pay attention to coincidences, gut feelings, and repeating opportunities as you navigate choices.",
    "Balance reading textbooks with real-world practice in the field or studio.",
    "Respect the wisdom of experienced mentors who have navigated the desert of your industry."
  ], [("the-power-of-now", 5, "Attuned presence in nature connects consciousness to the underlying reality of existence.")]),
  ch(4, "The Oasis and Love", "True love never stands between a human being and the pursuit of their Personal Legend.", [
    "The caravan halted at the oasis of Al-Fayoum, a neutral sanctuary of palm trees and wells amid tribal wars.",
    "At a well, Santiago met Fatima, a desert maiden filling her goatskin vessel with fresh water.",
    "When their eyes met, time stopped, and Santiago understood the pure Language of the World: Love.",
    "He wanted to abandon his journey to the pyramids and remain forever at the oasis with Fatima.",
    "Fatima, however, possessed the wisdom of desert women who know that men must follow their horizons.",
    "She told him: 'If I am part of your dream, you will come back to me one day. You must go.'",
    "True love never holds someone back from their authentic calling; if it does, it is not true love.",
    "With a courageous heart, Santiago prepared to ride deeper into the war-torn dunes."
  ], [
    ("Love is an empowering force, not a cage", "Genuine love encourages the beloved to fulfill their highest personal calling."),
    ("The language of the heart", "Intuitive connection transcends rational calculation and binds souls across deserts."),
    ("Trust in destiny's return", "What is truly meant for your life will never be lost by pursuing your righteous purpose.")
  ], ("One is loved because one is loved. No reason is needed for loving.", "rabbit_take"), [
    "Support your partner or friends in pursuing distant fellowships or demanding career leaps.",
    "Never demand that someone surrender their personal calling to provide you with comfortable company.",
    "Trust that deep, authentic bonds survive physical distance and challenging seasons of growth."
  ], [("mans-search-for-meaning", 2, "Love is the spiritual sanctuary that gives strength to endure harsh trials.")]),
  ch(5, "The Alchemist's Crucible", "Alchemy is not turning lead into gold; it is the spiritual transformation of the self.", [
    "Guided by the mysterious Alchemist on horseback, Santiago rode into the most dangerous sector of the desert.",
    "The Alchemist taught him that lead has its own purpose, and that gold is merely the highest evolution of matter.",
    "Wise alchemists understood that by purifying metal in the fire, they were purifying their own souls.",
    "Those who sought only gold were greedy charlatans who destroyed the secret.",
    "When captured by hostile desert warriors, the Alchemist promised the warlords that Santiago could turn himself into wind.",
    "Terrified and alone on a cliff, Santiago had to commune with the desert, the wind, and the sun.",
    "He realized that love is what transforms and improves the soul of the world.",
    "By reaching the universal hand that wrote it all, Santiago vanished and reappeared on the other side of the camp."
  ], [
    ("Alchemy is internal purification", "Refining character in the furnace of discipline is the true transmutation of lead into gold."),
    ("The trap of material greed", "Seeking wealth for its own sake blinds the practitioner to the spiritual laws of nature."),
    ("Unifying with the elements", "Recognizing that your spirit is interwoven with the cosmos unlocks immense human potential.")
  ], ("The simple things are also the most extraordinary things, and only the wise can see them.", "rabbit_take"), [
    "Treat exams and career pressures as the crucible that burns away arrogance and sharpens skill.",
    "Do not pursue money as the ultimate prize; pursue becoming an extraordinary person of value.",
    "Notice how nature reflects your own inner weather: calm mind produces calm perception."
  ], [("gitanjali", 1, "The fragile vessel of the self is purified and filled with immortal cosmic vitality.")]),
  ch(6, "The Treasure at the Roots", "The treasure you seek across oceans and deserts is buried right where you started.", [
    "Santiago reached the majestic Pyramids of Egypt at last, weeping with joy and gratitude.",
    "He began digging into the sand where his tears fell, searching for his promised gold.",
    "A band of desert refugees attacked him, beat him, and stole his remaining gold coins.",
    "As their leader left, he sneered: 'You are a fool. Two years ago, I had a recurring dream of a ruined church in Spain.'",
    "The leader continued: 'The dream said gold was buried under a sycamore tree where shepherds sleep! But I am not stupid enough to travel.'",
    "Santiago smiled through his bloody lips, filled with overwhelming peace.",
    "The treasure had been buried in the ruined church in Spain, right where he had slept with his sheep all along.",
    "Yet he had to cross an entire continent, learn languages, and find true love to become the man worthy of finding it."
  ], [
    ("The journey creates the finder", "The outer journey was necessary to forge the wisdom capable of appreciating the home treasure."),
    ("Treasure was at home all along", "The deepest peace and riches are waiting quietly under the foundation of your own life."),
    ("Gratitude for the detour", "Every trial, robbery, and sandstorm was essential to the awakening of the soul.")
  ], ("No heart has ever suffered when it goes in pursuit of its dreams.", "rabbit_take"), [
    "Appreciate that your current struggles are forging the character you will need when success arrives.",
    "Look around your current home and community for opportunities you overlooked while dreaming of distant lands.",
    "Smile at the detours in your education, knowing that every unexpected step serves your awakening."
  ], [("gitanjali", 5, "The traveler has to knock at every alien door before discovering the shrine in his own home.")])
])

# 8. Can't Hurt Me (David Goggins)
add_b("can-t-hurt-me", "Can't Hurt Me", "David Goggins", "https://covers.openlibrary.org/b/id/10543694-M.jpg", False, [
  ch(1, "The Accountability Mirror", "Look yourself in the eyes and tell the brutal, unvarnished truth about who you are.", [
    "David Goggins grew up in poverty, suffering severe childhood abuse, racism, and learning disabilities.",
    "By age twenty-four, he weighed nearly three hundred pounds, sprayed bugs for a living, and had zero prospects.",
    "One night after work, watching Navy SEALs on television, a spark ignited in his soul.",
    "He shaved his face, stood before the mirror, and confronted his reflection with savage honesty.",
    "He taped Post-it notes on the mirror stating his exact weaknesses: lazy, uneducated, overweight.",
    "He called it the Accountability Mirror: no excuses, no soothing lies, no blaming others.",
    "Every night, he had to look at those notes and answer whether he had taken action to fix them.",
    "Transformation begins only when you stop sugarcoating your reality and demand accountability from yourself."
  ], [
    ("The Accountability Mirror demands truth", "Self-delusion preserves fragile comfort; brutal honesty sparks genuine change."),
    ("External blame is a dead end", "Complaining about past trauma will never do the work needed to build your future."),
    ("Post your weaknesses publicly to yourself", "Keeping reminders of your targets front and center destroys procrastination.")
  ], ("You have to be willing to suffer to grow. The mirror does not lie.", "rabbit_take"), [
    "Tape your two biggest academic or fitness goals directly on your bathroom mirror where you see them daily.",
    "Stop making excuses for missed deadlines; tell yourself honestly that you mismanaged your time.",
    "Treat your reflection as a sparring partner that demands your best effort every single morning."
  ], [("atomic-habits", 2, "Identity change requires daily tangible evidence posted and validated before your own eyes.")]),
  ch(2, "The 40% Rule", "When your mind tells you that you are completely exhausted, you are only at forty percent of capacity.", [
    "During Navy SEAL Hell Week, candidates run hundreds of miles carrying heavy boats with zero sleep.",
    "At minute ninety of a brutal workout, the brain screams: 'Quit! We are going to die!'",
    "Goggins discovered the 40% Rule: when your mind insists you are tapped out, you have only reached 40% of your limit.",
    "The human brain is an evolutionary safety governor designed to protect you from pain and injury.",
    "It triggers fatigue, fear, and doubt long before your physical body actually reaches its true breaking point.",
    "To access the remaining sixty percent of your potential, you must learn to override that mental governor.",
    "Push through the initial wall of panic and fatigue, and you discover vast hidden reservoirs of strength.",
    "Greatness lives in the territory beyond where comfortable people decide to quit."
  ], [
    ("The brain is a cautious safety governor", "Mental panic triggers long before physical collapse to preserve comfortable safety."),
    ("Tapping the remaining sixty percent", "Pushing past the first wall of exhaustion reveals unexpected endurance."),
    ("Habituate to discomfort", "Consistently leaning into mild pain expands your baseline threshold for stress.")
  ], ("When you think you're done, you're only at forty percent of your body's capability.", "rabbit_take"), [
    "When you want to stop studying after thirty minutes, push yourself to complete just ten more minutes.",
    "During hard cardio or workouts, take five deep breaths and do two more repetitions past the urge to stop.",
    "Recognize that your brain's urge to quit is merely a suggestion, not a biological command."
  ], [("flow", 1, "Optimal performance emerges when human capacity is pushed to its absolute limits.")]),
  ch(3, "Taking Souls", "Excellence under brutal conditions demoralizes your opposition and commands undeniable respect.", [
    "During his third attempt at Hell Week, Goggins faced cruel weather, hypothermia, and sadistic instructors.",
    "Instead of showing pain and shivering, Goggins decided to 'take their souls.'",
    "Taking souls means performing with such fierce joy and unmatched intensity that it breaks the tormentor's spirit.",
    "When instructors made his boat crew paddle into freezing surf, Goggins smiled and roared with laughter.",
    "The instructors were stunned: how do you break a man who finds ecstasy in your harshest punishment?",
    "When facing rivals, critics, or difficult bosses, do not whine or file complaints.",
    "Outwork them so thoroughly, with such dignified energy, that they are forced to respect your power.",
    "True dominance is quiet, relentless excellence in the very conditions designed to crush you."
  ], [
    ("Smile in the storm", "Reacting to hardship with joy confuses critics and dismantles their psychological leverage."),
    ("Outwork every critic", "Flawless execution under fire is the ultimate refutation of every doubt."),
    ("Command respect through endurance", "People admire the competitor who refuses to complain even when the rules are unfair.")
  ], ("Do not just survive the trial; conquer it with such intensity that you take the soul of the obstacle.", "rabbit_take"), [
    "When given an unfairly difficult academic assignment, submit an impeccably researched masterwork early.",
    "Arrive ten minutes early and work with high energy on rainy Monday mornings when everyone else grumbles.",
    "Smile at critics who doubt your goals, then let your consistent daily progress shatter their predictions."
  ], [("the-48-laws-of-power", 5, "Winning through actions and relentless execution outclasses verbal complaints every time.")]),
  ch(4, "The Cookie Jar", "Store your past victories in a mental vault and feast on them when facing dark challenges.", [
    "During the San Diego One Day race, Goggins attempted to run one hundred miles in twenty-four hours with zero training.",
    "At mile seventy, his kidneys failed, bones broke in his feet, and he collapsed in a lawn chair, unable to stand.",
    "His mind told him it was impossible to take another step.",
    "He reached into what he calls the Cookie Jar: a mental repository of all the past hardships he had conquered.",
    "He remembered surviving childhood beatings, escaping poverty, losing one hundred pounds in three months, and surviving Hell Week.",
    "Each memory was a sweet cookie of proof that he was a certified bad man capable of enduring hell.",
    "Feasting on that proof reminded him of who he truly was, generating the adrenaline needed to stand up.",
    "He completed the final thirty miles on broken bones, entering the ultramarathon elite."
  ], [
    ("The Cookie Jar stores hard evidence", "Documenting past trials conquered gives you tangible proof of your resilience."),
    ("Fuel for dark moments", "When facing panic, recalling previous obstacles survived restores psychological grit."),
    ("Celebrate small victories", "Every time you overcome laziness, deposit another cookie into your mental jar.")
  ], ("The Cookie Jar is a reminder of who you are and what you have already conquered.", "rabbit_take"), [
    "Write a list of the five hardest things you have survived or accomplished in your life and review it before big exams.",
    "When self-doubt whispers that you cannot pass an interview, open your Cookie Jar and recall past victories.",
    "Treat every tough workout or disciplined study night as depositing another cookie for future storms."
  ], [("atomic-habits", 6, "Visual evidence and stored proof of capability reinforce an unshakeable identity.")]),
  ch(5, "Callusing the Mind", "The mind calluses like hands on a barbell: continuous friction turns soft skin into iron.", [
    "If you lift weights with soft hands, your palms develop painful blisters and tears.",
    "If you continue gripping the iron week after week, the skin thickens, producing protective calluses.",
    "The human mind behaves in the exact same manner when exposed to intentional, voluntary friction.",
    "If you avoid all discomfort, your mind remains fragile, offended by minor slights and paralyzed by basic stress.",
    "To callus your mind, do something that sucks every single day.",
    "Make your bed, take cold showers, run in the rain, study when tired, and clean the bathroom.",
    "Voluntary discomfort thickens your mental armor, making you resilient when real-life catastrophes arrive.",
    "A callused mind walks through chaos with calm, unshakeable composure."
  ], [
    ("Mental calluses through voluntary stress", "Subjecting yourself to small daily hardships builds psychological armor."),
    ("Fragility comes from comfort", "Coddling yourself with constant air conditioning and convenience softens the spirit."),
    ("Do something that sucks daily", "Small daily disciplines train the brain to override complaints and take action.")
  ], ("A callused mind is the only shield that protects you from the brutality of this world.", "rabbit_take"), [
    "Take a cold shower for the final two minutes of your morning routine to train instant discipline.",
    "Run or walk outside even when the weather is rainy and cold; don't wait for sunny days.",
    "Study your most difficult subject first thing in the morning when your mind wants to procrastinate."
  ], [("meditations", 6, "The blazing fire converts every obstacle into fuel; callusing the mind makes it invincible.")]),
  ch(6, "The Most Powerful Weapon: Total Self-Mastery", "Uncommon among the uncommon: continuing to push when everyone else thinks you have arrived.", [
    "Most people who achieve success make a fatal mistake: they relax, celebrate, and lose their edge.",
    "They become complacent, writing books about past glory while their daily discipline rots away.",
    "Goggins advocates being 'uncommon among uncommon people.'",
    "When you graduate from the elite school, win the championship, or earn the promotion, do not unpack your bags.",
    "The finish line is just the beginning of the next, higher mountain.",
    "Keep setting higher standards for yourself that nobody else expects or demands.",
    "Self-mastery is not a destination you arrive at and retire from; it is an endless, daily martial art.",
    "Stay hungry, stay humble, and keep after it until your final breath on Earth."
  ], [
    ("Complacency destroys champions", "Relaxing after victory softens the edge that earned the triumph in the first place."),
    ("Raise the standard after winning", "Use each milestone as a launching pad for deeper self-mastery."),
    ("The pursuit is lifelong", "Authentic discipline has no retirement date; it is a daily way of living with honor.")
  ], ("You are in danger of living a life so comfortable that you will die without ever knowing your true potential.", "rabbit_take"), [
    "After finishing a great semester with top marks, review your weaknesses and set next term's goals immediately.",
    "Do not let praise inflate your ego; keep doing your boring daily fundamentals with humility.",
    "Ask yourself: 'Am I living up to my true potential today, or am I resting on yesterday's reputation?'"
  ], [("deep-work", 2, "Elite achievement demands perpetual dedication to high standards that others consider extreme.")])
])

print(f"gen_hero_self_12: compiled books 7 & 8 (Alchemist & Goggins). Total: {len(books)}")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)
