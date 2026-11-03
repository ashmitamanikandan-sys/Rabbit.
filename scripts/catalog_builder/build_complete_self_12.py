# -*- coding: utf-8 -*-
"""
build_complete_self_12.py
Compiles all 12 Hero Books for 'Self Discovery':
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

Outputs to catalog/hero_self.json.
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

def add_b(b_id, title, author, cover, pd, fiction, chapters):
    books.append({
        "id": b_id, "title": title, "author": author, "genre": "Self Discovery",
        "cover_url": cover, "public_domain": pd, "fiction": fiction,
        "chapters": chapters
    })

import importlib.util
def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# 1 & 2: Subtle Art & Frankl
gen_self_mod = load_module("gen_hero_self", os.path.join(ROOT_DIR, "scripts", "catalog_builder", "gen_hero_self.py"))
for b in gen_self_mod.books:
    if b["id"] in ["the-subtle-art-of-not-giving-a-fuck", "mans-search-for-meaning"]:
        books.append(b)

# 3: Meditations
all_comp_mod = load_module("hero_self_all_complete", os.path.join(ROOT_DIR, "scripts", "catalog_builder", "hero_self_all_complete.py"))
for b in all_comp_mod.books:
    if b["id"] == "meditations":
        books.append(b)

# 4, 5, 6: Thirukkural, Siddhartha, Gitanjali from hero_self_complete
self_comp_mod = load_module("hero_self_complete", os.path.join(ROOT_DIR, "scripts", "catalog_builder", "hero_self_complete.py"))
for b in self_comp_mod.books:
    if b["id"] in ["thirukkural", "siddhartha", "gitanjali"]:
        books.append(b)

# 7: The Alchemist
add_b("the-alchemist", "The Alchemist", "Paulo Coelho", "https://covers.openlibrary.org/b/id/10543692-M.jpg", False, True, [
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

# 8: Can't Hurt Me (cleaned of banned words)
add_b("can-t-hurt-me", "Can't Hurt Me", "David Goggins", "https://covers.openlibrary.org/b/id/10543694-M.jpg", False, False, [
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
    ("Smile in the storm", "Reacting to hardship with joy confuses critics and neutralizes their psychological leverage."),
    ("Outwork every critic", "Flawless execution under fire is the ultimate refutation of every doubt."),
    ("Command respect through endurance", "People admire the competitor who refuses to complain even when the rules are unfair.")
  ], ("Do not just survive the trial; conquer it with such intensity that you take the soul of the obstacle.", "rabbit_take"), [
    "When given an unfairly difficult academic assignment, submit an impeccably researched paper early.",
    "Arrive ten minutes early and work with high energy on rainy Monday mornings when everyone else grumbles.",
    "Smile at critics who doubt your goals, then let your consistent daily progress shatter their predictions."
  ], [("the-48-laws-of-power", 5, "Winning through actions and relentless execution outclasses verbal complaints every time.")]),
  ch(4, "The Cookie Jar", "Store your past victories in a mental vault and feast on them when facing dark challenges.", [
    "During the San Diego One Day race, Goggins attempted to run one hundred miles in twenty-four hours with zero training.",
    "At mile seventy, his kidneys failed, bones broke in his feet, and he collapsed in a lawn chair, unable to stand.",
    "His mind told him it was impossible to take another step.",
    "He reached into what he calls the Cookie Jar: a mental repository of all the past hardships he had conquered.",
    "He remembered surviving childhood beatings, escaping poverty, losing one hundred pounds in three months, and surviving Hell Week.",
    "Each memory was a sweet cookie of proof that he was capable of enduring hell.",
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

# 9. Courage to Be Disliked
add_b("the-courage-to-be-disliked", "The Courage to Be Disliked", "Ichiro Kishimi & Fumitake Koga", "https://covers.openlibrary.org/b/id/10543696-M.jpg", False, False, [
  ch(1, "The Unknown Third Giant: Alfred Adler", "Your past does not determine your future; you are driven by goals, not haunted by causes.", [
    "While Sigmund Freud taught that past traumas cause our present unhappiness, Alfred Adler proposed a liberating alternative: teleology.",
    "Teleology looks at the purpose of our present behavior rather than past causes.",
    "Adler argues that people do not suffer from the shock of past experiences; instead, they make out of them whatever suits their current purposes.",
    "A person who claims they cannot socialize because of past childhood bullying is often using trauma as an excuse to avoid the risk of future rejection.",
    "We determine our own lives according to the meaning we choose to give to our past experiences.",
    "You are not a helpless puppet of your childhood environment or ancestral genetics.",
    "At any given moment, you hold the creative power to choose a completely new lifestyle and destination.",
    "Freedom begins the instant you stop blaming yesterday for how you behave today."
  ], [
    ("Teleology over etiology", "Behavior is driven by current goals and convenience, not fixed by historical trauma."),
    ("Trauma as an excuse", "People cling to past wounds to justify avoiding the frightening uncertainty of present growth."),
    ("The power of present reinterpretation", "You can assign empowering new meaning to past events this very afternoon.")
  ], ("No experience is in itself a cause of our success or failure. We do not suffer from the shock of our experiences—the so-called trauma—but instead make out of them whatever suits our purposes.", "rabbit_take"), [
    "Catch yourself saying 'I am bad at math because my fifth-grade teacher was mean' and replace it with intentional practice.",
    "Stop using past introversion as an alibi to decline invitations to join study groups and clubs.",
    "Acknowledge that staying in a rut can feel safer than trying and risking public failure."
  ], [("atomic-habits", 2, "Identity is shaped by current habits rather than permanent historical labels.")]),
  ch(2, "All Problems Are Interpersonal Relationship Problems", "Loneliness is not being alone; loneliness is the painful sensation of being alienated from others.", [
    "Adler stated emphatically: 'All problems are interpersonal relationship problems.'",
    "If an individual lived completely alone in the boundless universe, all financial worries, self-consciousness, and jealousy would vanish instantly.",
    "We suffer because we constantly compare ourselves against friends, colleagues, and social media personas.",
    "When we view the human world through the lens of competition, everyone around us looks like an adversary or a judge.",
    "You worry about what shoes you wear, how your voice sounds, and how much money you earn because you fear their judgment.",
    "True growth is not competing against other human beings, but comparing yourself against your own potential.",
    "The moment you step off the competitive battlefield, other people transform from threatening rivals into trusted companions.",
    "Peace arrives when you celebrate other people's victories as if they were your own."
  ], [
    ("The root of human suffering", "Virtually all anxiety arises from navigating status, approval, and judgment among peers."),
    ("The curse of vertical competition", "Viewing society as a ladder makes every peer a threat to your self-worth."),
    ("Shift to horizontal fellowship", "Treating humans as equals on a wide plain dissolves jealousy and unlocks genuine empathy.")
  ], ("To get rid of one's problems, all one can do is live in the universe all alone. But that is impossible. So we must learn to be companions, not rivals.", "rabbit_take"), [
    "Unfollow social media accounts that trigger chronic feelings of material or social inadequacy.",
    "Send a message of sincere admiration to a peer who just won an award you secretly hoped to receive.",
    "Measure your daily study progress against what you knew yesterday, never against your classmate's test score."
  ], [("surrounded-by-idiots", 2, "Recognizing complementary human behavioral styles eliminates toxic workplace rivalry.")]),
  ch(3, "The Separation of Tasks", "Do not intrude on other people's life tasks, and never let them intrude upon yours.", [
    "How can we free ourselves from the suffocating pressure of trying to meet everyone else's expectations?",
    "Adler introduces his signature diagnostic tool: the separation of tasks.",
    "In any situation, ask yourself: 'Whose task is this ultimately? Who will receive the final results brought about by this choice?'",
    "Studying for an exam is the child's task; worrying about or forcing it is a parental intrusion that breeds resentment.",
    "What other people think of your career choice, your clothing, or your beliefs is entirely their task, not yours.",
    "You have full responsibility over your actions, your honesty, and your kindness; you have zero control over how others react to you.",
    "Trying to control other people's opinions is like trying to command the clouds to rain.",
    "Discard the burden of other people's expectations, and you will breathe the clean air of true autonomy."
  ], [
    ("Diagnose the task", "Identify who bears the ultimate consequences of a decision before getting entangled."),
    ("Stop intruding on others", "Trying to force family members to change their habits only creates unnecessary warfare."),
    ("Release control of opinions", "How someone judges your choices belongs strictly on their side of the boundary line.")
  ], ("You are not living to satisfy other people's expectations, and other people are not living to satisfy yours.", "rabbit_take"), [
    "State your honest boundary to parents regarding your university major without apologizing or shouting.",
    "Stop losing sleep over an awkward comment you made at lunch; how they interpret it is their task.",
    "Allow your younger sibling to suffer the natural consequence of forgetting their homework instead of rescuing them."
  ], [("the-48-laws-of-power", 7, "Cultivating quiet autonomy prevents emotional manipulators from dictating your schedule.")]),
  ch(4, "The Center of the Universe Fallacy", "You are not the center of the world; you are an active part of the human community.", [
    "People who are obsessed with what others think of them believe they are deeply humble, but Adler reveals they are profoundly self-centered.",
    "They view everyone else merely as mirrors to reflect their own importance, anxiety, or perfection.",
    "They constantly ask: 'What will they think of me? Will they like me? Do they admire me?'",
    "To overcome this toxic self-preoccupation, shift your awareness from self-regard to community feeling.",
    "You are not the conductor of the cosmic orchestra; you are simply one grateful musician holding an instrument.",
    "Community feeling means seeing others as companions and feeling that you have a meaningful place of belonging among them.",
    "Belonging is not something you passively receive like a trophy; it is something you actively build through contributing.",
    "When you focus on how you can be of use to those around you, self-conscious paralysis evaporates."
  ], [
    ("Vanity disguises as insecurity", "Chronic self-consciousness is an inverted form of egotism where you imagine everyone is watching you."),
    ("The shift to community feeling", "True psychological health replaces 'what do they think of me' with 'how can I contribute'."),
    ("Belonging is earned through service", "Active contribution creates an indestructible sense of psychological home.")
  ], ("Do not ask what others can give you; ask what you can contribute to the community right now.", "rabbit_take"), [
    "When feeling awkward at a party, go into the kitchen and help the host wash dishes or serve drinks.",
    "Focus your attention on asking thoughtful questions to quiet colleagues rather than worrying about your own charisma.",
    "Join a volunteer initiative to experience the grounding joy of selfless communal labor."
  ], [("thirukkural", 6, "True friendship acts instinctively to uplift the companion without selfish calculation.")]),
  ch(5, "Praise Is a Vertical Trap", "Never praise or rebuke someone; treat human beings with horizontal equality and genuine gratitude.", [
    "Many parents and managers believe that lavish praise is the most effective way to motivate children and employees.",
    "Adler warns that praise is a vertical tool used by the superior to manipulate the inferior.",
    "When you say 'Good job! You are so smart!', you are passing judgment from an elevated throne of authority.",
    "Praise creates approval addicts who will only work hard when an authority figure is watching to hand out rewards.",
    "Instead of praise, Adler advocates horizontal encouragement rooted in genuine gratitude: 'Thank you for your help. That made a big difference.'",
    "Gratitude does not judge; it simply acknowledges the person's positive contribution to the group.",
    "When people feel that they are beneficial to the community, they discover their own authentic courage from within.",
    "Encourage others as equal companions on the path of life, and watch their inner dignity blossom."
  ], [
    ("Praise implies hierarchy", "Congratulatory judgment reinforces vertical power dynamics and breeds approval dependency."),
    ("Encouragement through gratitude", "Saying 'thank you' honors the recipient's dignity without placing yourself above them."),
    ("Awakening internal courage", "People gain real courage when they realize their existence is useful to those around them.")
  ], ("Do not praise, and do not scold. Simply offer gratitude. That is how equal companions encourage one another.", "rabbit_take"), [
    "Thank your project partner for their hard work on the slides instead of rating them like a school teacher.",
    "Acknowledge your parents' cooked dinner with heartfelt thanks rather than a patronizing 'good job.'",
    "Notice when you are performing only to fish for praise, and redirect your focus to the quality of the work."
  ], [("influence-psychology-of-persuasion", 3, "Genuine peer reciprocity creates mutual respect far deeper than hollow flattery.")]),
  ch(6, "The Courage to Be Disliked", "Freedom is being disliked by other people; live now in the dance of the present moment.", [
    "The courage to be happy inherently requires the courage to be disliked.",
    "If nobody dislikes you, it means you are constantly currying favor, altering your opinions, and living a compromised, cowardly existence.",
    "Being disliked by someone is proof that you are living freely according to your own principles.",
    "Adler uses the metaphor of dancing: life is not a straight highway leading toward a distant peak where success awaits.",
    "Life is a dance made up of a series of present moments, complete in and of themselves.",
    "If you dance with full energy and passion across the floor, it does not matter where you end up when the music stops.",
    "Do not shine a weak spotlight into a foggy future, worrying about retirement or distant status.",
    "Shine a brilliant, blazing spotlight on the present moment, live with honor, and let others think whatever they wish."
  ], [
    ("Dislike as the cost of freedom", "Having critics confirms that you are standing up for authentic values rather than pandering."),
    ("Life as a kinetic dance", "Every moment of living, studying, and loving is an end in itself, not just a stepping stone."),
    ("The intense spotlight on Now", "Focusing on immediate ethical action eliminates chronic anxiety about the unknown future.")
  ], ("The courage to be happy also includes the courage to be disliked. When you have gained that courage, all your interpersonal relationships will suddenly turn light.", "rabbit_take"), [
    "Speak your candid, ethical perspective during a meeting even if the popular crowd disagrees.",
    "Stop putting off happiness until graduation or promotion; enjoy the study session you are conducting tonight.",
    "Smile when you encounter someone who disapproves of your creative projects; take it as proof of your independence."
  ], [("meditations", 5, "Standing upright through internal virtue rather than leaning on the props of external applause.")])
])

# 10. The Mountain Is You
add_b("the-mountain-is-you", "The Mountain Is You", "Brianna Wiest", "https://covers.openlibrary.org/b/id/10543698-M.jpg", False, False, [
  ch(1, "Self-Sabotage Is an Unconscious Need", "Your bad habits are not flaws; they are maladaptive coping mechanisms protecting your comfort zone.", [
    "We often view our procrastination, overeating, or sudden relationship drama as inexplicable self-sabotage.",
    "Brianna Wiest reframes this completely: self-sabotage is never random destruction.",
    "It is a brilliant, misguided psychological attempt to meet an unconscious, unmet emotional need.",
    "When you procrastinate on an important application, your brain is actively protecting you from the fear of catastrophic failure.",
    "When you pick fights with someone who loves you, your subconscious is seeking safety from the vulnerability of true intimacy.",
    "You cannot eliminate a self-sabotaging behavior simply through sheer willpower and angry self-criticism.",
    "You must identify the hidden need the habit was desperately trying to satisfy and provide a healthier solution.",
    "The mountain before you is not a roadblock; the mountain is the parts of yourself waiting to be understood."
  ], [
    ("The purpose of self-sabotage", "Harmful habits are protective shields designed to keep us inside familiar emotional territory."),
    ("Willpower is insufficient", "Yelling at yourself does not heal the subconscious fear driving the destructive cycle."),
    ("Unmasking the hidden payoff", "Ask what emotional comfort or safety your bad habit is secretly providing.")
  ], ("Self-sabotage is what happens when you have two conflicting desires: one conscious, and one unconscious.", "rabbit_take"), [
    "When delaying study for an exam, ask: 'What terrifying outcome is my procrastination trying to protect me from?'",
    "Recognize that leaving assignments to the last minute gives you a convenient excuse if you receive a low grade.",
    "Offer yourself compassionate reassurance before starting intimidating tasks to calm subconscious fear."
  ], [("atomic-habits", 3, "Understanding the cue and craving behind habits unlocks true behavioral transformation.")]),
  ch(2, "The Upper Limit Problem and Familiar Misery", "The brain prefers familiar suffering over the terrifying uncertainty of unfamiliar happiness.", [
    "Human beings possess an internal emotional thermostat known as their upper limit.",
    "We have a baseline level of joy, success, and love that we feel safe tolerating.",
    "When life suddenly goes wonderfully well—a promotion, a great romance, a creative breakthrough—our alarms sound.",
    "The subconscious mind panics: 'This is unfamiliar territory! Danger! We don't know how to survive here!'",
    "To bring the thermostat back down to baseline, we unconsciously manufacture a crisis or drama.",
    "We pick an argument, overspend money, or spiral into irrational worry to return to familiar misery.",
    "Familiar misery feels safe because we already know how to survive it; unfamiliar joy demands immense vulnerability.",
    "To ascend your mountain, you must expand your capacity to hold peace, joy, and abundance without panicking."
  ], [
    ("The upper limit thermostat", "When good fortune exceeds our comfort baseline, we unconsciously sabotage our joy."),
    ("Familiar suffering feels safe", "The brain equates the known with survival, even when the known is painful depression."),
    ("Expanding tolerance for peace", "Learn to sit inside quiet contentment without frantically looking for the next emergency.")
  ], ("Your comfort zone is not comfortable; it is simply familiar.", "rabbit_take"), [
    "Notice when you start inventing catastrophic worries immediately after receiving wonderful news.",
    "Take three deep breaths when experiencing pure happiness, allowing your nervous system to register safety.",
    "Resist the urge to check your work email during relaxing weekends to avoid manufactured stress."
  ], [("thinking-fast-and-slow", 5, "The subconscious brain is biased toward loss aversion and hyper-vigilant threat detection.")]),
  ch(3, "Emotional Triggers as Internal Maps", "Whatever irritates you in other people is a direct reflection of an unhealed fracture within yourself.", [
    "When someone's arrogance, laziness, or success makes your blood boil, pause before you attack them.",
    "Your emotional triggers are not proof of their evil; they are brightly lit roadmaps to your own internal wounds.",
    "You cannot be triggered by something that does not resonate with a suppressed part of your own psyche.",
    "If a peer's boastful self-confidence fills you with rage, it often points to your own repressed ambition and fear of being seen.",
    "If someone's disorganization disgusts you, it may reflect your own exhausting, perfectionist fear of losing control.",
    "Stop wasting valuable life energy policing other people's flaws and social media posts.",
    "Turn the investigative mirror around and ask: 'What unintegrated piece of my history does this trigger reveal?'",
    "Healing begins when you thank your triggers for highlighting the exact places where you are not yet free."
  ], [
    ("Triggers as diagnostic tools", "Extreme emotional reactions to others reveal suppressed desires and unhealed insecurities."),
    ("Projection of the shadow", "We despise in others the very behaviors we forbid ourselves from expressing."),
    ("The mirror of self-awareness", "Shift the focus from judging their conduct to healing your own vulnerability.")
  ], ("What you see in others is a reflection of what you need to heal in yourself.", "rabbit_take"), [
    "When infuriated by a loud classmate, examine whether you harbor unexpressed resentment about your own quietness.",
    "Write down three traits that trigger intense annoyance in others and reflect on your own relationship to them.",
    "Use moments of interpersonal irritation as opportunities for quiet self-inquiry rather than gossip."
  ], [("the-laws-of-human-nature", 2, "Shadow projection leads us to condemn our own dark traits in neighboring rivals.")]),
  ch(4, "Releasing Emotional Residue and Trauma", "Feelings do not vanish because you ignore them; they sit in your physical tissues waiting to be felt.", [
    "Modern culture encourages us to numb our sorrow, distract our grief, and scroll past our anxiety.",
    "However, an emotion is a physiological wave that lasts roughly ninety seconds if allowed to flow uninterrupted.",
    "When we resist our feelings—labeling them as weak or inconvenient—we trap their emotional residue in our bodies.",
    "This accumulated emotional backlog manifests as chronic fatigue, sudden panic attacks, and inexplicable irritability.",
    "To heal, you must cultivate the courage to sit quietly and feel your feelings all the way through to the end.",
    "Lie on the floor, close your eyes, and locate the physical sensation of the ache in your chest or stomach.",
    "Do not analyze the story, blame culprits, or search for solutions; simply breathe into the physical sensation.",
    "When you stop fleeing from your sadness, it dissolves naturally, leaving clean clarity and deep peace in its wake."
  ], [
    ("Emotions are temporary waves", "A physiological emotional response completes its cycle in ninety seconds when not resisted."),
    ("The danger of emotional numbing", "Suppressed feelings solidify into chronic physical tension, exhaustion, and anxiety."),
    ("Somatic release through presence", "Locating feelings in the physical body allows emotional residue to metabolize and release.")
  ], ("You do not heal by thinking your way out of feelings; you heal by allowing yourself to feel them completely.", "rabbit_take"), [
    "Put your phone away and sit in silence for ten minutes when hit by unexpected sadness or grief.",
    "Notice where stress sits in your shoulders or stomach and take slow, deep breaths directly into that area.",
    "Stop judging yourself for feeling vulnerable; honor your sadness as a natural, cleansing human tide."
  ], [("the-power-of-now", 2, "Observing the pain-body with conscious awareness dissolves its toxic grip on the psyche.")]),
  ch(5, "Building Radical Self-Trust", "Confidence is not knowing you will succeed; confidence is knowing you will survive failure.", [
    "Many people wait for confidence to magically arrive before they apply for the job, speak up, or start the business.",
    "Wiest reveals that confidence is not a feeling you summon; it is the after-effect of repeated, honest action.",
    "Self-doubt is not a mystery; it is the natural consequence of breaking hundreds of small promises to yourself.",
    "Every time you set an alarm and hit snooze five times, you teach your subconscious that your word is worthless.",
    "Every time you promise to eat clean or study at seven and break it, your self-trust deteriorates.",
    "To rebuild self-trust, start with microscopic, unbreakable commitments.",
    "Drink a glass of water upon waking, walk for ten minutes, or read two pages without fail.",
    "When your subconscious realizes that your decisions are non-negotiable laws, fear dissolves and genuine courage rises."
  ], [
    ("Confidence follows action", "Waiting for courage before taking steps guarantees paralysis; action generates confidence."),
    ("The currency of self-trust", "Keeping small daily promises builds an unshakeable psychological foundation."),
    ("Surviving failure", "Real self-reliance is not avoiding defeat, but trusting your capacity to endure and rebuild.")
  ], ("Self-trust is built in the tiny moments when nobody is watching and you keep your promise anyway.", "rabbit_take"), [
    "Set only one micro-promise tomorrow—like washing your dish immediately after eating—and keep it without exception.",
    "Stop making grandiose New Year resolutions that set you up for predictable cycles of failure and self-disgust.",
    "Remind yourself during tough moments: 'I have survived one hundred percent of my worst days so far.'"
  ], [("atomic-habits", 1, "Tiny two-minute habits reinforce the subconscious belief that you are an effective, reliable person.")]),
  ch(6, "The Mountain Was You", "The obstacle in your path was never the circumstances; it was your own readiness to awaken.", [
    "At the start of your journey, the mountain appeared as an external monster designed to ruin your plans.",
    "You cursed the economic climate, the toxic family dynamics, the breakup, or the lack of luck.",
    "Yet as you climb the steep, rocky terrain, you are forced to shed everything that cannot survive at high altitudes.",
    "You shed people-pleasing, victim mentality, toxic numbing, and superficial pride.",
    "When you finally reach the windy summit and gaze down upon the valley below, a profound revelation strikes your heart.",
    "The mountain was never placed there to defeat you, humiliate you, or hold you back.",
    "The mountain was an intentional crucible designed by destiny to forge the strength required for your true purpose.",
    "You did not conquer the mountain; the mountain was you, and you finally stepped into your power."
  ], [
    ("The crucible of adversity", "High mountains exist to strip away fragile pretenses and cultivate authentic resilience."),
    ("Shedding baggage at altitude", "You cannot carry old victim narratives into the higher elevations of your personal destiny."),
    ("The realization of wholeness", "Looking back reveals that every painful trial was an essential brick in your spiritual backbone.")
  ], ("You are not moving the mountain; you are becoming the person who can stand upon its summit.", "rabbit_take"), [
    "Write a letter thanking a past painful experience for the resilience and discernment it forced you to build.",
    "Identify one comfortable excuse you are finally ready to leave behind in the valley as you climb upward.",
    "Stand tall today, recognizing that you already possess the inner strength to handle whatever summit lies ahead."
  ], [("mans-search-for-meaning", 4, "Finding transcendent purpose transforms suffering into an enduring human victory.")])
])

# 11. The Power of Now
add_b("the-power-of-now", "The Power of Now", "Eckhart Tolle", "https://covers.openlibrary.org/b/id/10543700-M.jpg", False, False, [
  ch(1, "You Are Not Your Mind", "Thinking is a tool; when you cannot stop thinking, the tool has become your tyrannical master.", [
    "Most human beings live in a state of involuntary, incessant mental chatter.",
    "A continuous stream of commentary, judgment, regret about the past, and anxiety about the future plays in our heads.",
    "Eckhart Tolle points out the single most liberating realization of human existence: you are not your mind.",
    "You are the silent, spacious awareness behind the thoughts, the witness who observes the chatter.",
    "When you identify completely with your thoughts, you mistake the voice in your head for your authentic identity.",
    "This false, manufactured identity is the ego: fragile, defensive, and perpetually terrified of not being enough.",
    "The ego constantly drags your consciousness into past resentments or future fears to ensure its own survival.",
    "The moment you watch a thought without judging it, a gap of pure presence opens in your soul."
  ], [
    ("Incessant thinking is a disease", "When mental chatter operates without pause, consciousness is trapped in chronic illusion."),
    ("The witness behind thoughts", "You are the spacious observer of the mind, not the neurotic thoughts passing through it."),
    ("The birth of the ego", "Identifying with mental concepts creates a fragile, anxious persona that craves constant defense.")
  ], ("The beginning of freedom is the realization that you are not 'the thinker.' The moment you start watching the thinker, a higher level of consciousness becomes activated.", "quote"), [
    "Pause right now, take a breath, and ask yourself: 'What will my next thought be?' Notice the silent gap that follows.",
    "While brushing your teeth, focus entirely on the sound of the water and the feel of the bristles rather than replaying arguments.",
    "Notice when your mind starts an anxious monologue and say silently: 'There is anxiety in the mind, but I am the observer.'"
  ], [("flow", 1, "Total immersion in the immediate activity silences the psychic entropy of anxious ego-chatter.")]),
  ch(2, "Consciousness: The Way Out of Pain", "Past and future have no reality of their own; all suffering exists as psychological time.", [
    "Have you ever experienced anything outside of the present moment? Can you ever do so?",
    "The answer is an absolute, undeniable no: nothing has ever happened in the past; it happened in the Now.",
    "Nothing will ever happen in the future; it will happen in the Now.",
    "Yet the human ego spends ninety-nine percent of its energy living in psychological time.",
    "It hoards memories of past injuries, generating guilt, regret, and resentment.",
    "Or it projects hypothetical catastrophes into the future, creating worry, panic, and dread.",
    "Tolle explains that all anxiety is caused by too much future, and all guilt is caused by too much past.",
    "When you step fully into the immediate present, psychological suffering instantly dissolves, for in the Now, there are no problems."
  ], [
    ("The illusion of psychological time", "Past and future exist only as memory traces and mental projections in the present brain."),
    ("The anatomy of anxiety and guilt", "Worry requires a future to fear; depression requires a past to grieve; Now holds neither."),
    ("Problems require time to exist", "In the immediate five seconds of this exact room, you have challenges to handle, not abstract problems.")
  ], ("Unease, anxiety, tension, stress, worry—all forms of fear—are caused by too much future, and not enough presence. Guilt, regret, resentment, grievances, sadness, bitterness, and all forms of nonforgiveness are caused by too much past, and not enough presence.", "quote"), [
    "Whenever you catch yourself spiraling about next week's exam, return your attention to the desk beneath your elbows.",
    "Ask yourself: 'What is lacking in this exact physical second right now?' You will find that the present is whole.",
    "Stop treating the present moment merely as an inconvenient obstacle to reach a future goal."
  ], [("siddhartha", 5, "The river flows everywhere simultaneously; time is a human illusion that blinds us to eternity.")]),
  ch(3, "The Pain-Body: Dissolving the Ghost", "Negative emotional energy accumulates into a psychic parasite that feeds on drama and conflict.", [
    "Most people carry an invisible accumulation of old, unhealed emotional pain called the pain-body.",
    "The pain-body consists of every heartache, betrayal, and sorrow from childhood to adulthood that was never fully faced.",
    "It lies dormant inside your nervous system until a trigger—a critical word, a tired evening—wakes it up.",
    "Once awake, the pain-body takes over your mind, making you crave drama, arguments, and gloomy victimhood.",
    "It feeds on negative emotional energy; it wants to fight with your partner or plunge you into dark despair.",
    "The pain-body survives only as long as you remain unconscious and identify with its misery.",
    "The moment you bring sustained, conscious awareness to the pain-body, you break the cycle of feeding.",
    "Do not fight it; simply observe the dark cloud in your chest with alert, non-judgmental presence, and it dissolves."
  ], [
    ("The nature of the pain-body", "An accumulated mass of old emotional trauma that periodically wakes to feed on drama."),
    ("The craving for misery", "When hijacked by the pain-body, the ego actively seeks conflicts to sustain its negative charge."),
    ("Transmutation through awareness", "Shining the light of alert consciousness on the pain-body transmutes suffering into peace.")
  ], ("The pain-body cannot survive in the light of your presence. It can only survive if you identify with it and feed it with your thinking.", "quote"), [
    "When a sudden wave of gloom hits, recognize it instantly: 'The pain-body has awakened; I will not feed it with thoughts.'",
    "Refrain from sending angry text messages late at night when the pain-body is running your fingertips.",
    "Breathe quietly into physical chest tension until the physiological storm subsides without adding narrative drama."
  ], [("the-mountain-is-you", 4, "Somatic presence allows old emotional residue to release without getting entangled in mental stories.")]),
  ch(4, "The Inner Body as an Anchor", "Connecting with the invisible life energy inside your physical form roots you in timeless reality.", [
    "How can you remain centered in the present moment when the world around you is loud, chaotic, and stressful?",
    "Tolle provides an infallible, portable spiritual practice: inhabiting the inner body.",
    "Close your eyes and ask yourself: 'How do I know that my hands still exist without looking at them?'",
    "You will immediately feel a subtle tingling, a quiet warmth, an invisible current of alive energy in your fingers.",
    "That subtle vibration is the life of the universe pulsing through your physical cells.",
    "Direct your awareness into your feet, your legs, your chest, and your arms until your entire body hums with life.",
    "By anchoring fifty percent of your attention in the inner body, you prevent the mind from wandering into neurotic chatter.",
    "The inner body is your personal gateway from the noisy realm of time into the quiet ocean of Being."
  ], [
    ("The felt sense of aliveness", "Inhabiting the internal cellular energy of the physical body tethers consciousness to the Now."),
    ("Preventing mental wandering", "Keeping a portion of awareness inside the physical form prevents egoic spiraling during stress."),
    ("The gateway to Being", "The inner body bridges the fleeting world of physical form with the formless depths of pure spirit.")
  ], ("Inhabit your body. Feel the subtle energy field that animates every cell. That is how you step out of the prison of conceptual thought.", "rabbit_take"), [
    "Feel the warmth and tingling in your palms while sitting in boring lectures or stressful meetings.",
    "Take three conscious breaths into your lower abdomen before answering difficult emails or texts.",
    "Use physical exercise and walking not to escape yourself, but to feel the vibrant life surging in your limbs."
  ], [("deep-work", 3, "Grounding your physical nervous system enables prolonged, laser-focused intellectual concentration.")]),
  ch(5, "The Beauty of Surrender", "Surrender is not cowardly weakness; it is the yielded wisdom of yielding to the reality of what is.", [
    "To many modern minds, the word 'surrender' carries connotations of defeat, resignation, and failure.",
    "Tolle radically redefines surrender: it is not passive victimhood or tolerating abuse.",
    "Surrender is the simple, profound willingness to yield to the reality of the present moment without internal resistance.",
    "When you are stuck in traffic, raining on your wedding day, or facing a flat tire, resistance is sheer madness.",
    "Saying 'this should not be happening' does not change the flat tire; it only adds agonizing suffering to the circumstance.",
    "Surrender means saying 'Yes' to what is, accepting the fact of the situation with total internal neutrality.",
    "From that clear, unclouded state of surrender, you take whatever effective, intelligent action is required.",
    "Surrender eliminates the poison of resentment and unlocks creative power that transforms any obstacle."
  ], [
    ("Surrender is not defeat", "Yielding to reality frees you from toxic internal rebellion against unchangeable current facts."),
    ("The madness of resistance", "Arguing with the present moment is as foolish as yelling at the rain for falling."),
    ("Clean, unclouded action", "Accepting what is allows you to act with surgical precision, free from the distortions of rage.")
  ], ("Surrender is the simple but profound wisdom of yielding to rather than opposing the flow of life.", "quote"), [
    "When facing unexpected flight delays, immediately accept the fact without whining to airline desk staff.",
    "Say 'Yes' to the rain on your picnic day, and then calmly pack up your basket and move indoors.",
    "Accept when an exam question is unexpectedly hard; drop panic, take a deep breath, and tackle what you know."
  ], [("meditations", 6, "Loving your allotted fate transforms every impediment into fuel for virtuous action.")]),
  ch(6, "The Unmanifested: Beyond Death", "Beneath the surface ripples of your mortal personality lies an eternal realm of luminous peace.", [
    "Everything in the physical cosmos—stars, galaxies, empires, and human bodies—is subject to birth, decay, and death.",
    "The ego lives in constant terror of this physical mortality, building wealth and reputations to shield itself from dust.",
    "Yet Tolle reveals that death only claims what is ephemeral: your physical form and mental concepts.",
    "Consciousness itself—the formless, unmanifested light of awareness that shines through your eyes—was never born and can never die.",
    "In deep meditation, in the silence of nature, and in moments of deep presence, you touch this unmanifested realm.",
    "You realize that you are not a drop of water desperately trying to avoid evaporating on a hot rock.",
    "You are the boundless ocean itself, temporarily expressing itself in the shape of a human wave.",
    "When this realization dawns, fear of death vanishes, and life becomes an effortless, joyful celebration of Being."
  ], [
    ("The transient nature of form", "All physical objects and worldly personalities inevitably dissolve in the cosmic river of change."),
    ("The eternal unmanifested source", "Formless consciousness is the timeless canvas upon which the temporary universe appears."),
    ("The ocean and the wave", "Realizing your identity as pure awareness eliminates all existential dread and fear of death.")
  ], ("Death is a stripping away of all that is not you. The secret of life is to 'die before you die'—and find that there is no death.", "quote"), [
    "Take five minutes tonight under the stars to gaze into the deep black space, sensing the timeless stillness.",
    "Remember that material possessions, academic degrees, and trophies will all be left behind at death; cultivate inner peace.",
    "Smile at your mortal human quirks, resting in the unshakable realization that your true nature is boundless awareness."
  ], [("gitanjali", 6, "At the close of our brief mortal dance, life takes its voyage to its eternal home like homeward cranes.")])
])

# 12. The Untethered Soul
add_b("the-untethered-soul", "The Untethered Soul", "Michael A. Singer", "https://covers.openlibrary.org/b/id/10543702-M.jpg", False, False, [
  ch(1, "The Voice Inside Your Head", "Stop listening to the neurotic roommate in your mind who never stops talking about everything.", [
    "If you sit quietly for just two minutes, you will notice an incessant voice chattering away inside your consciousness.",
    "It says: 'Did I lock the door? Why did she look at me like that? It's too cold in here. I need a coffee.'",
    "Michael A. Singer asks a devastating question: if you had a human roommate who talked like that nonstop, would you live with them?",
    "You would throw them out of your apartment within twenty minutes for being clinically insane.",
    "Yet we allow this frantic mental voice to dictate our mood, our self-worth, and our life decisions every single hour.",
    "The voice talks not because it is wise, but because it is trying to make the infinite, uncontrollable universe feel manageable.",
    "To achieve spiritual liberation, take a step back and occupy the seat of witness consciousness.",
    "You are not the voice; you are the one who hears the voice.",
    "Once you notice the voice from the seat of the witness, you are finally free from its neurotic dictatorship."
  ], [
    ("The neurotic roommate", "The inner monologue is a hyper-reactive mechanism attempting to control reality, not a source of truth."),
    ("The seat of witness consciousness", "True freedom begins when you step back and observe the inner chatter without participating."),
    ("Dis-identifying with the mind", "Realizing that you are the listener rather than the speaker breaks the cycle of anxiety.")
  ], ("There is nothing more important to true growth than realizing that you are not the voice of the mind—you are the one who hears it.", "quote"), [
    "Listen to your mind complain about bad weather today as if listening to a fussy toddler on a bus.",
    "When feeling insecure before an interview, observe the voice whispering doubts without believing its catastrophic warnings.",
    "Take three quiet breaths before sleep, resting as the silent observer who watches thoughts drift by."
  ], [("the-power-of-now", 1, "Observing the mental thinker from spacious presence breaks the tyrant grip of egoic chatter.")]),
  ch(2, "Your Inner Energy: The Flow of Prana", "Your heart is an energetic valve that opens with love and closes with fear and past resentment.", [
    "Have you ever noticed how you can feel completely exhausted, but when someone you love calls, you suddenly have boundless energy?",
    "Where did that massive surge of vitality come from? You didn't eat a meal or take an hour-long nap.",
    "Singer explains that human beings possess an unlimited reservoir of spiritual life energy, known as prana, chi, or shakti.",
    "This energy flows naturally into your mind and body as long as your heart center remains open.",
    "The heart is an energetic valve: when you experience trauma, rejection, or disappointment, you instinctively close down to protect yourself.",
    "By closing your heart, you trap the old pain inside and block the upward flow of universal life energy.",
    "You become lethargic, depressed, and defensive, needing endless coffee and external stimulation just to function.",
    "The secret to vibrant living is to keep your heart open, no matter what happens in the outside world."
  ], [
    ("The infinite well of life energy", "Boundless vitality resides within you, accessible whenever the heart center remains receptive."),
    ("The closing mechanism of fear", "Closing the heart to prevent pain traps old emotional poison and blocks energetic nourishment."),
    ("The vow of the open heart", "Choosing to keep your heart open through all circumstances ensures an endless stream of inner light.")
  ], ("Energy does not get tired. You only feel drained when you close your heart and block the flow of life through your system.", "rabbit_take"), [
    "Notice the physical sensation of tightening in your chest during arguments and consciously relax your shoulders to stay open.",
    "Instead of shutting down when criticized, keep your posture relaxed and breathe through the discomfort.",
    "Choose to greet friends and family with an open, warm heart even when you feel slightly tired or irritable."
  ], [("flow", 2, "Opening consciousness to experience allows psychic energy to flow without friction or blockage.")]),
  ch(3, "The Samskaras: Clearing the Thorn", "Unprocessed emotional impressions get stuck in your psyche like festering thorns waiting to be triggered.", [
    "Suppose you have a sharp thorn stuck in your arm directly over a nerve ending.",
    "It hurts excruciatingly whenever anything brushes against it: clothes, branches, or a gentle touch from a friend.",
    "You have two fundamental choices: you can carefully build elaborate padding around the thorn to avoid touching it, or you can pull it out.",
    "Building padding means rearranging your entire life—wearing special sleeves, avoiding crowds, and never hugging anyone.",
    "Singer explains that human beings do this exact foolish thing with their emotional wounds, known in yogic science as samskaras.",
    "When a past betrayal or humiliation occurs, we don't process it; we lock it away and rearrange our entire life to avoid triggering it.",
    "We avoid certain places, become defensive around certain topics, and control other people's behavior to protect our inner thorn.",
    "The only authentic path to freedom is to pull the thorn out: allow the old feeling to surface, feel its sting, and let it pass through."
  ], [
    ("The thorn analogy", "Rearranging your lifestyle to avoid triggering unhealed wounds keeps you in permanent emotional prison."),
    ("The creation of samskaras", "Incomplete experiences get blocked in the energy system, becoming emotional landmines."),
    ("Liberation through extraction", "Letting the thorn get touched and feeling the old pain allows it to release forever.")
  ], ("If you want to be free, you must stop protecting your thorns and simply let them come out.", "rabbit_take"), [
    "When a conversation triggers old high school insecurities, resist the urge to get angry or flee; sit and let it burn out.",
    "Stop demanding that friends walk on eggshells around your sensitive topics; take responsibility for your thorns.",
    "View moments of emotional discomfort as the thorn rising to the surface to be permanently released."
  ], [("the-mountain-is-you", 3, "Interpersonal triggers are mirrors revealing the exact internal wounds ready for healing.")]),
  ch(4, "Relax and Release: The Ultimate Practice", "When life pushes your buttons, do not fight back; relax your shoulders, breathe, and release.", [
    "Throughout your day, thousands of microscopic events will disturb your comfort zone.",
    "Someone will cut you off in traffic, the elevator will take too long, or a colleague will use a curt tone.",
    "In that split second, your internal energy will contract; your mind will urge you to shout, complain, or seethe in silent fury.",
    "Singer offers the most practical, transformative spiritual tool in existence: the practice of relax and release.",
    "The instant you feel the contraction in your chest or throat, immediately relax the physical muscles around your heart.",
    "Take a slow, deep breath, lean back behind the disturbance, and let the negative energy pass right through you like a gust of wind.",
    "Do not touch it, do not analyze it, and do not act upon it while contracted.",
    "By relaxing and releasing twenty times a day, you become an untouchable spiritual warrior who walks through fire without burning."
  ], [
    ("The split-second choice", "Between a trigger and your reaction lies a moment of supreme power to relax or contract."),
    ("Relaxing the heart center", "Releasing physical tension around the chest allows emotional contractions to dissipate harmlessly."),
    ("Letting the wind blow through", "Viewing disturbances as passing gusts of wind preserves your profound inner peace.")
  ], ("Relax and release. When the disturbance hits, just let go of your shoulders, breathe out, and let it pass.", "rabbit_take"), [
    "Relax your jaw and hands the moment you see an annoying email notification arrive.",
    "When someone takes the parking spot you wanted, exhale deeply and consciously say: 'I release this; it means nothing.'",
    "Practice relaxing your chest while standing in long supermarket checkout lines rather than tapping your foot."
  ], [("meditations", 3, "External events cannot penetrate consciousness unless you endorse the disturbing judgment.")]),
  ch(5, "Stepping Behind the Wall: The Prison of the Ego", "You built a psychological fortress to keep pain out, but that fortress has become your solitary prison.", [
    "Imagine living inside a house where you boarded up all the windows and doors because you were terrified of the dark woods outside.",
    "Inside, it is pitch black, stuffy, and claustrophobic, but you tell yourself: 'At least I am safe from predators.'",
    "This boarded-up house is your ego: a rigid mental structure built out of preferences, dislikes, anxieties, and defenses.",
    "You say: 'I only like people who agree with me; I only like warm weather; I cannot stand loud noise.'",
    "Every single preference is another heavy bar you weld onto your own cell door.",
    "You spend your entire earthly incarnation defending your prison walls rather than exploring the boundless universe of experience.",
    "To awaken, you must dare to tear down the boards and step outside into the sunlight of reality.",
    "Embrace the cold days as well as the warm; accept difficult people alongside pleasant companions.",
    "When you no longer need the universe to match your petty preferences, you discover that you are already free."
  ], [
    ("The architecture of the ego prison", "Preferences and neurotic dislikes are psychological bars that trap us in tiny comfort zones."),
    ("The misery of defensive living", "Spending life protecting a fragile self-concept prevents direct participation in the beauty of life."),
    ("Dismantling the walls", "Dropping rigid demands about how reality must behave unlocks boundless experiential joy.")
  ], ("Your inner house is only a prison if you refuse to open the door and walk out into the vast world.", "rabbit_take"), [
    "Eat a meal you usually avoid without complaining, training your mind to transcend petty culinary dislikes.",
    "Spend an afternoon with people of differing political or cultural viewpoints with an open, curious heart.",
    "Catch yourself saying 'I can't stand when...' and remind yourself that your peace does not depend on external conditions."
  ], [("siddhartha", 4, "Transcending rigid ascetic preferences enables full, joyful immersion in the dance of reality.")]),
  ch(6, "Death as the Great Teacher", "Death does not rob life of its meaning; death is the supreme master that makes every breath precious.", [
    "Most people live as though they have an infinite lease on life, squandering hours on petty arguments, resentment, and trivial distractions.",
    "Singer reminds us that death is walking right beside us every single day, waiting to tap us on the shoulder.",
    "Suppose an angel told you that tonight at midnight, your heart would stop beating forever.",
    "Would you spend your remaining hours arguing about politics on social media or complaining about the weather?",
    "Every single trivial grievance would evaporate instantly in the blazing light of your imminent departure.",
    "You would hug your loved ones, gaze at the green leaves of the trees with wonder, and marvel at the taste of clean water.",
    "Death is not an enemy to be feared; death is your greatest friend, stripping away petty nonsense and revealing what truly matters.",
    "Live every single day with death by your side as an advisor, and every ordinary moment will shine like a polished jewel."
  ], [
    ("The reality of mortality", "Forgetting our inevitable death causes us to squander precious time on meaningless squabbles."),
    ("Death clarifies priority", "Viewing your day through the lens of your final hour instantly dissolves petty grievances."),
    ("Gratitude for every ordinary breath", "Remembering mortality turns walking outside, drinking water, and smiling into holy miracles.")
  ], ("Death is the great equalizer and the greatest teacher. It reminds you that this moment is all you are ever guaranteed.", "quote"), [
    "Ask yourself before engaging in a petty argument: 'If this were my last day on earth, would I want to spend it being right?'",
    "Look at a tree or a sunset today with the profound awareness that one day you will see your last one.",
    "Tell your family members that you love them with total presence and heartfelt sincerity today."
  ], [("meditations", 2, "Viewing life from the equalizing perspective of cosmic time and mortality restores profound serenity.")])
])

print(f"Total Self Discovery Hero Books: {len(books)}")
for i, b in enumerate(books):
    print(f"  {i+1}. {b['id']} ({len(b['chapters'])} chapters)")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(books)} books to {OUT_PATH}")
