# -*- coding: utf-8 -*-
"""
hero_self_complete.py
Builds the complete 12 Hero Books for 'Self Discovery'.
Outputs to catalog/hero_self.json.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
OUT_PATH = os.path.join(ROOT_DIR, "catalog", "hero_self.json")
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

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

# Load Subtle Art, Frankl, and Meditations if present
if os.path.exists(OUT_PATH):
    try:
        with open(OUT_PATH, "r", encoding="utf-8") as f:
            existing = json.load(f)
            # take first 3 if valid
            for b in existing:
                if b["id"] in ["the-subtle-art-of-not-giving-a-fuck", "mans-search-for-meaning", "meditations"]:
                    books.append(b)
    except:
        pass

def add_b(b_id, title, author, cover, pd, chapters):
    if not any(x["id"] == b_id for x in books):
        books.append({
            "id": b_id, "title": title, "author": author, "genre": "Self Discovery",
            "cover_url": cover, "public_domain": pd, "fiction": False,
            "chapters": chapters
        })

# 4. Thirukkural (Thiruvalluvar) - Public Domain
add_b("thirukkural", "Thirukkural", "Thiruvalluvar", "https://covers.openlibrary.org/b/id/10543686-M.jpg", True, [
  ch(1, "The Primacy of Virtue (Aram)", "Virtue is not a passive duty; it is the active foundation that yields supreme renown and joy.", [
    "Composed two thousand years ago in Tamil Nadu, the Thirukkural begins with an uncompromising celebration of moral virtue.",
    "Thiruvalluvar teaches that virtue yields both worldly honor and eternal spiritual liberation.",
    "What greater gain can there be in mortal life than to cultivate that which secures both peace and dignity?",
    "Virtue is not practiced in secluded caves away from society, but in the heat of daily domestic life.",
    "To be free from four mental poisons is the totality of virtue: envy, greed, anger, and harsh words.",
    "When a person purifies their mind of these four vices, their very presence radiates auspicious light.",
    "Do not delay virtue until old age; practice it this hour, for death waits for no man's convenience.",
    "Virtue practiced today will accompany you as an unfailing friend into the vast unknown."
  ], [
    ("Four poisons destroy virtue", "Envy, uncontrolled greed, sudden wrath, and bitter speech poison the human heart."),
    ("Virtue thrives in ordinary life", "Living ethically within family and community is superior to cowardly ascetic retreat."),
    ("Do not postpone righteousness", "Death strikes without warning; practice virtue now so your legacy is secure.")
  ], ("Virtue yields honor and wealth; what greater gain can life bestow? — Thiruvalluvar", "quote"), [
    "Notice when envy rises at a classmate's good fortune; immediately replace it with sincere congratulations.",
    "Refrain from using sharp, cutting sarcasm during family arguments even when you feel provoked.",
    "Make regular small contributions to community charity without announcing your deeds to onlookers."
  ], [("meditations", 5, "Standing upright in virtue without needing the crutches of public applause.")]),
  ch(2, "The Power of Rain (Vaan Sirappu)", "Without the gift of rain, oceans wither, charity dies, and human civilization starves.", [
    "Thiruvalluvar dedicates his second chapter to the sacred ecological gift of falling rain.",
    "By the bountiful fall of rain the world is preserved; it is the nectar of all living organisms.",
    "If the clouds fail to dispense their liquid drops, even the mighty green grass cannot shoot forth its blade.",
    "If the sky runs dry, ocean treasures diminish and pearls no longer form in the depths of the sea.",
    "Neither worship of the divine nor daily acts of charity can endure in a world parched by drought.",
    "Water is the prime minister of nature; without water, no mortal duty can be performed on Earth.",
    "Treat the natural world with reverence, for civilization is a fragile guest on a living planet.",
    "True ethics begins with environmental stewardship and awe before the life-giving rains."
  ], [
    ("Water is the prerequisite for all ethics", "Without ecological abundance, neither charity, worship, nor moral living can survive."),
    ("The fragility of nature's web", "When rain fails, both land agriculture and marine life suffer catastrophic decline."),
    ("Reverence for natural cycles", "Recognizing our total dependence on weather fosters profound ecological humility.")
  ], ("If the heavens dry up, neither charity nor worship will endure on earth. — Thiruvalluvar", "quote"), [
    "Turn off running taps and protect clean water in your household with mindful discipline.",
    "Support sustainable agriculture and plant native trees in your neighborhood community spaces.",
    "Remember that material wealth is worthless without the natural ecological foundations that sustain life."
  ], [("dune", 3, "Water as sacred currency on desert worlds echoes Thiruvalluvar's ecological reverence.")]),
  ch(3, "Sweet Words (Iniyavai Koorala)", "Speaking kindly with an open heart is superior to giving lavish gifts with a cold face.", [
    "Humility and sweet speech are the only authentic ornaments of a civilized human being; all else is vanity.",
    "When you possess the ability to speak words that comfort, heal, and encourage, why use words that wound?",
    "To utter harsh words when pleasant ones are available is like eating unripe bitter fruit when sweet ripe fruit hangs near.",
    "A pleasant face and warm words of greeting create instant goodwill that gold cannot purchase.",
    "Kind words cost nothing to produce, yet they enrich both the speaker and the listener beyond measure.",
    "Harsh speech leaves invisible burns on the soul that fester for decades after the argument ends.",
    "Train your tongue to speak with gracious warmth, and you will walk through the world surrounded by friends.",
    "Let every word that crosses your lips be a blessing of sweetness and truth."
  ], [
    ("Kind words are true jewelry", "Gentle speech and humble posture outshine the most extravagant physical adornments."),
    ("The unripe fruit metaphor", "Choosing bitter insults when kind words exist is an act of foolish self-deprivation."),
    ("Healing power of speech", "A gracious greeting dissolves interpersonal hostility and knits fractured bonds.")
  ], ("To utter harsh words when sweet ones are available is like eating unripe fruit when ripe is at hand. — Thiruvalluvar", "quote"), [
    "Greet shopkeepers, bus drivers, and servers with a warm smile and sincere words of appreciation.",
    "When delivering critical feedback to team members, wrap the truth in encouraging, constructive praise.",
    "Catch yourself before speaking in anger; pause until you can communicate with calm sweetness."
  ], [("surrounded-by-idiots", 4, "Gentle, non-confrontational speech builds lasting trust with supportive colleagues.")]),
  ch(4, "Gratitude (Seinri Arithal)", "A favor done in the hour of need, however small, is larger than the measure of the earth.", [
    "A kindness done in a season of desperate emergency, though small as a grain of millet, looms as vast as a palm tree.",
    "Never forget the benefit conferred upon you by those who stood beside you in the hour of sorrow.",
    "Do not abandon the friendship of those who sheltered you when the storms of life raged around your head.",
    "The wise remember with tears of joy the favor that lifted them out of darkness.",
    "He who has killed every other virtue may yet find redemption, but there is no salvation for the ungrateful.",
    "Ingratitude is the spiritual poison that corrodes the soul and burns the bridges of human fellowship.",
    "Repay favors with double measure whenever fortune grants you the strength to give.",
    "Hold the memory of kindness sacred, carved into granite that time cannot erase."
  ], [
    ("Timely help carries infinite weight", "Assistance rendered during acute crises has a spiritual value beyond any price."),
    ("Ingratitude is the unpardonable sin", "Betraying those who helped you in your vulnerable hour ruins character completely."),
    ("Remember kindness forever", "Let injuries be written on water, but let favors be carved in stone.")
  ], ("A favor conferred in the hour of need, though small, is larger than the world itself. — Thiruvalluvar", "quote"), [
    "Call a mentor or friend who supported you during tough times and thank them for their loyalty.",
    "When you achieve career success, look back and hire or assist those who helped you get your start.",
    "Never speak ill of someone who opened their home or wallet to you when you were broke."
  ], [("meditations", 1, "Cataloging lessons and debts to ancestors echoes the sacred duty of gratitude.")]),
  ch(5, "Truthfulness (Vaimai)", "Truthfulness is speech that produces not the slightest harm to any living creature.", [
    "What is truthfulness? It is speaking words that are utterly free from harm and malice.",
    "Even a falsehood may take the rank of truth if it produces unblemished, life-saving good for the innocent.",
    "If a person speaks truth with purity of heart, their name will be honored above those who perform austerities and gifts.",
    "External water cleanses the physical body, but truthfulness alone purifies the internal soul.",
    "Let not a person consciously utter a falsehood; for their own conscience will burn them with relentless fire.",
    "He who lives in truth dwells in the hearts of all noble people across all generations.",
    "Truth needs no elaborate armor; its quiet simplicity stands unconquered against all deceits.",
    "Speak the truth with love, and your character will become an unshakeable beacon."
  ], [
    ("Truth must be benevolent", "Speech that is factual but malicious fails the highest test of righteous truthfulness."),
    ("Conscience is an inescapable judge", "Lying burns the inner spirit with guilt long after the lie has been spoken."),
    ("Inward purity through truth", "Physical bathing cleanses skin; speaking truth purifies consciousness itself.")
  ], ("Purity of body is achieved by water; purity of heart is illuminated by truthfulness. — Thiruvalluvar", "quote"), [
    "Refuse to tell flattering lies to curry favor with superiors; speak the respectful, constructive truth.",
    "When you make an error on a team project, confess it immediately rather than hiding behind excuses.",
    "Let your word be your bond so partners never feel the need for legal threats to ensure compliance."
  ], [("the-48-laws-of-power", 5, "Winning through actions rather than deceitful arguments establishes unshakeable integrity.")]),
  ch(6, "Friendship (Natpu)", "True friendship is not a face that smiles in company; it is a hand that catches you when you fall.", [
    "Friendship is not merely walking together and laughing over pleasant entertainment.",
    "True friendship is an inner bond that rushes forward to avert ruin in the hour of calamity.",
    "Like the hand that instantly catches the garment slipping from the waist, true friendship acts without delay.",
    "A friend does not hesitate, deliberate, or calculate when danger threatens the companion.",
    "They step into the breach, pull you back from wrong paths, and share your burden with fierce loyalty.",
    "Associate with those who possess noble character, for their virtue will elevate your own standards.",
    "Flee from the fair-weather companion who smiles in prosperity but vanishes when hardship arrives.",
    "One faithful, principled friend is a treasure greater than all the gold in royal vaults."
  ], [
    ("Immediate instinct to protect", "True friendship reacts like the hand catching a falling robe: instantaneous and instinctive."),
    ("Moral correction as love", "A genuine friend rebukes your bad habits to save you from self-destruction."),
    ("Shun transactional allies", "Fair-weather friends who celebrate your wins but flee your trials must be cast aside.")
  ], ("Like the hand that moves to catch a slipping garment, true friendship leaps to avert ruin. — Thiruvalluvar", "quote"), [
    "Show up for friends during hospital stays, family deaths, and financial crises without waiting to be invited.",
    "Have the courage to tell a close friend when their alcohol or spending habits are spiraling out of control.",
    "Choose friends whose ambition, honesty, and kindness inspire you to become a better human being."
  ], [("the-courage-to-be-disliked", 2, "Building deep interpersonal bonds requires treating companions as equals, not competitors.")])
])

# 5. Siddhartha (Hermann Hesse) - Public Domain
add_b("siddhartha", "Siddhartha", "Hermann Hesse", "https://covers.openlibrary.org/b/id/10543688-M.jpg", True, [
  ch(1, "The Brahmin's Son", "The thirst for truth cannot be quenched by rituals, scriptures, or the teachings of others.", [
    "Siddhartha grew up in the golden sunlight of the riverbank, loved by his father and revered by the Brahmins.",
    "He mastered the holy ablutions, recited the sacred verses, and performed every ritual with flawless devotion.",
    "Yet his heart was not at peace; his soul was an empty vessel thirsting for authentic illumination.",
    "He realized that the wise Brahmins could impart knowledge, but they could not impart enlightenment.",
    "The sacred river of truth must be discovered within one's own consciousness, not borrowed from texts.",
    "Siddhartha resolved to leave behind his family, his wealth, and his status to become a wandering Samana.",
    "No dogma, however ancient, can substitute for the raw, direct encounter with one's own soul.",
    "The journey toward self-discovery requires the courage to leave comfortable shores behind."
  ], [
    ("Knowledge is not wisdom", "Memorizing scriptures and rituals does not dissolve the spiritual thirst of the seeker."),
    ("Direct experience over second-hand dogma", "Authentic truth must be lived firsthand, not accepted on blind authority."),
    ("The courage of renunciation", "Leaving behind comfortable privileges is often the necessary first step of awakening.")
  ], ("Wisdom cannot be imparted. Wisdom that a wise man attempts to impart always sounds like foolishness. — Hermann Hesse", "quote"), [
    "Do not accept career or life paths purely because parents or tradition demand it; examine your own calling.",
    "Read philosophical texts critically, testing their claims against the laboratory of your own lived experience.",
    "Step away from comfortable group echo chambers to discover what you truly believe in solitude."
  ], [("the-power-of-now", 1, "Direct conscious presence transcends theoretical concepts and intellectual doctrines.")]),
  ch(2, "With the Samanas", "Fasting, waiting, and thinking: the three timeless arts that conquer the restless appetites.", [
    "Siddhartha joined the ascetics in the forest, learning to renounce the body and silence the senses.",
    "He gave away his clothes, fasted for weeks, and exposed his flesh to scorching sun and icy rain.",
    "He learned the three foundational arts that would serve him throughout his entire earthly journey.",
    "I can think, I can wait, I can fast.",
    "Thinking allows the mind to solve complex problems without panic or emotional distraction.",
    "Waiting allows the spirit to endure long delays with patience, knowing that fruits ripen in their season.",
    "Fasting frees the individual from desperate dependency on immediate food, luxury, or comfort.",
    "When you possess these three arts, you can walk into any marketplace or palace without fear."
  ], [
    ("I can think", "The disciplined intellect cuts through confusion and refuses to accept hasty conclusions."),
    ("I can wait", "Patience allows the seeker to endure long winters without forcing premature action."),
    ("I can fast", "Freedom from physical cravings makes you immune to bribery, greed, and panic.")
  ], ("I can think. I can wait. I can fast. — Hermann Hesse", "quote"), [
    "Practice intermittent fasting to prove to yourself that appetite is a servant, not your master.",
    "Wait twenty-four hours before responding to stressful life events; cultivate the art of waiting.",
    "Sit quietly with difficult academic problems for an hour before searching for shortcut solutions."
  ], [("the-psychology-of-money", 5, "Living below your means and tolerating delays is the financial equivalent of fasting and waiting.")]),
  ch(3, "Gotama the Buddha", "Enlightenment is a path walked in solitary footsteps; no master can hand you your awakening.", [
    "In the grove of Jetavana, Siddhartha encountered Gotama, the Illustrious Buddha, whose presence radiated pure peace.",
    "Siddhartha observed Gotama's downcast gaze, his gentle step, his quiet robe: every finger spoke of wholeness.",
    "Govinda, Siddhartha's companion, took refuge in the Buddha and joined the monastic order of the yellow robes.",
    "Siddhartha bowed in profound reverence before the Buddha, but declined to join the disciples.",
    "He told Gotama: 'Your doctrine contains no flaw, yet it cannot teach me what occurred to you in the hour of awakening.'",
    "The secret of what the Buddha experienced under the Bodhi tree was incommunicable through words.",
    "To achieve genuine salvation, Siddhartha had to leave all teachers behind and walk into the world alone.",
    "Reverence for the master must not become an excuse to avoid walking your own solitary path."
  ], [
    ("Teaching has boundaries", "Words can convey information, but they cannot transmit the living essence of enlightenment."),
    ("The master cannot walk your path", "Borrowing another person's awakening leaves your own spirit unawakened."),
    ("Solitary responsibility", "Every human being must discover their own liberation through their own steps.")
  ], ("No doctrine can save you; you must find your own salvation through your own footsteps. — Hermann Hesse", "quote"), [
    "Respect teachers and authors, but test their wisdom in your own daily conduct rather than idolizing them.",
    "Do not become a passive follower of online gurus; build your own coherent life philosophy.",
    "Have the courage to walk away from systems that no longer nourish your genuine spiritual growth."
  ], [("the-courage-to-be-disliked", 3, "Separating tasks means taking total ownership of your own path rather than living someone else's.")]),
  ch(4, "Kamala and the City", "Immersing in the worldly dance of desire, commerce, and pleasure without losing your center.", [
    "Siddhartha entered the bustling commercial city, encountering the beautiful courtesan Kamala and the merchant Kamaswami.",
    "To win Kamala's affection and learn the art of love, Siddhartha became a wealthy merchant.",
    "Because he could think, wait, and fast, business felt like an effortless children's game to him.",
    "He did not panic when ships were delayed or transactions failed; he viewed commerce with amused detachment.",
    "Kamaswami was astonished: while other merchants lost their hair over losses, Siddhartha remained serene.",
    "However, slowly and insidiously, the poison of worldly luxury began to seep into Siddhartha's bloodstream.",
    "He began to play dice for money, feel the pangs of greed, and drink wine late into the night.",
    "The game of the world had caught him in its velvet trap, drowning the quiet voice within."
  ], [
    ("Detachment creates business mastery", "Not caring about petty outcomes gives you immense leverage in commercial affairs."),
    ("The subtle trap of luxury", "Material comforts slowly numb the spiritual ear until the quiet voice of truth falls silent."),
    ("Experience teaches what theory cannot", "Siddhartha had to taste worldly indulgence to understand its ultimate emptiness.")
  ], ("Most people are like falling leaves that drift and turn in the air; a few are like stars that follow a fixed course. — Hermann Hesse", "quote"), [
    "Engage in business and career goals with excellence, but do not tie your inner worth to quarterly profits.",
    "Watch out for lifestyle creep: luxury slowly turns from an amusing game into an addictive necessity.",
    "Maintain daily habits of quiet meditation so worldly commercial noise does not drown your center."
  ], [("the-psychology-of-money", 3, "Knowing what is enough prevents the worldly trap of endless pursuit from destroying your peace.")]),
  ch(5, "By the River with Vasudeva", "The river is everywhere at once: time is an illusion, and all voices merge into the holy Om.", [
    "Fleeing the city in disgust and despair, Siddhartha collapsed by the banks of the mighty river.",
    "Contemplating ending his life in the waters, the holy sound 'Om' resonated from the depths of his being.",
    "He awoke refreshed, as if reborn, and met Vasudeva, the humble ferryman whose eyes radiated divine calm.",
    "Vasudeva was not a scholar; he was a listener who learned everything from the voice of the flowing water.",
    "Siddhartha became the ferryman's assistant, learning to listen to the river with an open, non-judgmental soul.",
    "He learned from the river that there is no such thing as time: the river is at the source and the ocean simultaneously.",
    "The past, present, and future are merely shadows; reality exists in the eternal, indivisible Now.",
    "Listening without ego reveals that all joy, all suffering, and all beings are one harmonious melody."
  ], [
    ("The river knows all secrets", "Nature speaks profound truths to those who listen with patience and humility."),
    ("Time is a human illusion", "The river is present everywhere at once; the eternal Now is the only true reality."),
    ("The art of non-judgmental listening", "Quieting your own internal commentary allows you to hear the universal harmony of existence.")
  ], ("The river is everywhere at the same time, at the source and at the mouth, at the waterfall, at the ferry, at the current, in the ocean and in the mountains. — Hermann Hesse", "quote"), [
    "Spend time walking beside a flowing river or in a forest, listening without headphones or distractions.",
    "Release anxiety about the future by reminding yourself that only this present moment actually exists.",
    "Listen to friends with complete, unhurried presence rather than mentally formulating your reply."
  ], [("the-power-of-now", 3, "Moving deeply into the present moment reveals the timeless river of consciousness.")]),
  ch(6, "The Eternal Smile: Om", "When all voices of sorrow, joy, longing, and laughter merge, the single word Om resounds.", [
    "In his final trial, Siddhartha suffered the agony of loving his rebellious son, who fled back to the city.",
    "Siddhartha realized that he could not protect his son from life's pain, just as his own father could not protect him.",
    "He sat beside Vasudeva and listened to the river with total surrender, hearing thousands of voices at once.",
    "He heard the voice of the lustful, the voice of the grieving, the voice of the warrior, and the voice of the dying.",
    "None of the voices could be separated from the others; all were interwoven into a singular cosmic web.",
    "When all voices merged together, the river sang the great syllable: Om, the perfection of being.",
    "In that moment, Siddhartha ceased to fight against destiny; his wound healed, and his face shone with an eternal smile.",
    "Like the Buddha, like Vasudeva, his countenance beamed with the quiet, loving radiance of enlightenment."
  ], [
    ("Accepting the limits of control", "You cannot spare loved ones their life lessons; every soul must walk its own fire."),
    ("The unity of all existence", "Pain and joy, evil and good, are complementary notes in the universal symphony."),
    ("The smile of enlightenment", "Surrendering resistance to reality produces profound peace that blesses the entire world.")
  ], ("When Siddhartha listened attentively to the thousand-fold song of the river, when he did not bind his soul to any one voice, but heard all, he heard the single word: Om. — Hermann Hesse", "quote"), [
    "Accept that loved ones must make their own mistakes to grow; love them without suffocating control.",
    "View the chaotic news of the world as a vast unfolding symphony rather than an occasion for despair.",
    "Smile at the ordinary challenges of today, knowing that every moment is woven into your awakening."
  ], [("flow", 6, "The autotelic self perceives the unity of all experience and moves with cosmic harmony.")])
])

# 6. Gitanjali (Rabindranath Tagore) - Public Domain
add_b("gitanjali", "Gitanjali", "Rabindranath Tagore", "https://covers.openlibrary.org/b/id/10543690-M.jpg", True, [
  ch(1, "Thou Hast Made Me Endless", "The fragile human vessel is emptied again and again to be filled with fresh immortal life.", [
    "Rabindranath Tagore opens Gitanjali with an ecstatic realization of the human soul's eternal renewal.",
    "Thou hast made me endless, such is thy pleasure. This frail vessel thou emptiest again and again, and fillest it ever with fresh life.",
    "The body is a little flute of reed carried over hills and dales, breathing through it melodies eternally new.",
    "At the immortal touch of the infinite, the heart loses its limits in joy and gives birth to utterance ineffable.",
    "Tagore reminds us that our small ego-boundaries are illusions; we are open vessels of cosmic vitality.",
    "When you surrender the rigid demand to control every outcome, the universe breathes fresh life through your spirit.",
    "Your creative gifts are not private possessions to hoard, but divine melodies passing through your reed.",
    "Open your heart to each sunrise as an unearned gift of renewed consciousness."
  ], [
    ("The soul as an open vessel", "Emptying oneself of rigid pride allows universal vitality and inspiration to enter."),
    ("The flute of the infinite", "Human talent is an instrument through which universal melodies and beauty are expressed."),
    ("Transcendence of the finite ego", "Releasing petty self-centeredness dissolves mortal limits into profound joy.")
  ], ("Thou hast made me endless, such is thy pleasure. This frail vessel thou emptiest again and again, and fillest it ever with fresh life. — Rabindranath Tagore", "quote"), [
    "Begin each morning by sitting in stillness, visualizing emptying your mind of yesterday's lingering grievances.",
    "View your creative writing or artistic projects as gifts flowing through you rather than stressful tests of ego.",
    "Walk outdoors at dawn and feel the fresh air as a physical reminder of renewed life."
  ], [("the-untethered-soul", 4, "Infinite energy flows through the spiritual heart when internal blockages are surrendered.")]),
  ch(2, "Where the Mind Is Without Fear", "The supreme prayer for human freedom: where knowledge is free and the mind led into widening thought.", [
    "Tagore's immortal Poem 35 is a universal anthem for the liberation of the human intellect and spirit.",
    "Where the mind is without fear and the head is held high; where knowledge is free;",
    "Where the world has not been broken up into fragments by narrow domestic walls;",
    "Where words come out from the depth of truth; where tireless striving stretches its arms towards perfection;",
    "Where the clear stream of reason has not lost its way into the dreary desert sand of dead habit;",
    "Where the mind is led forward by thee into ever-widening thought and action;",
    "Into that heaven of freedom, my Father, let my country awake.",
    "Tagore challenges every generation to shatter the petty barriers of caste, tribe, and dogmatic tradition."
  ], [
    ("Fearless intellectual integrity", "A truly educated mind holds its head high in truth, untamed by authoritarian intimidation."),
    ("Shatter narrow domestic walls", "Rejecting tribal sectarianism unites humanity into a single borderless family of knowledge."),
    ("The clear stream of reason", "Living truth must never be suffocated by the dry desert sands of unthinking dead habit.")
  ], ("Where the clear stream of reason has not lost its way into the dreary desert sand of dead habit. — Rabindranath Tagore", "quote"), [
    "Refuse to let partisan tribalism divide your friendships; seek truth beyond political slogans.",
    "Challenge dead traditions and superstitions with the clear stream of respectful, curious reasoning.",
    "Speak from the depth of your authentic conviction rather than parroting opinions to please the crowd."
  ], [("1984-george-orwell", 1, "Freedom is the ability to say that two plus two equals four without fear of persecution.")]),
  ch(3, "Leave This Chanting and Singing", "Open your eyes and see your God is not in the temple, but out where the tiller is tilling the ground.", [
    "Tagore delivers a stunning rebuke to hypocritical, cloistered religious asceticism in Poem 11.",
    "Leave this chanting and singing and telling of beads! Whom dost thou worship in this lonely dark corner of a temple with doors all shut?",
    "Open thine eyes and see thy God is not before thee!",
    "He is there where the tiller is tilling the hard ground and where the pathmaker is breaking stones.",
    "He is with them in sun and in shower, and his garment is covered with the dust of honest labor.",
    "Put off thy holy mantle and even like him come down on the dusty soil!",
    "True holiness is found not in incense and chants, but in compassionate solidarity with hardworking common people.",
    "Meet the divine in honest work, in sweat, and in serving those who labor under the hot sun."
  ], [
    ("Divinity resides with working hands", "God is present in the honest sweat of the laborer, not trapped inside cold temple walls."),
    ("Spiritual hypocrisy of seclusion", "Shutting oneself away in ritual isolation avoids the sacred duty of loving human service."),
    ("Put off the holy mantle", "True enlightenment gets its hands dirty in the dusty soil of daily community care.")
  ], ("He is there where the tiller is tilling the hard ground and where the pathmaker is breaking stones. — Rabindranath Tagore", "quote"), [
    "Honor manual laborers, janitors, and street workers with deep personal respect and generous tips.",
    "Do not separate your spiritual ideals from your daily work; treat studying and cooking as sacred acts.",
    "Step outside academic libraries and volunteer at local shelters where genuine human needs exist."
  ], [("thirukkural", 1, "Virtue practiced within domestic and communal labor is superior to ascetic retreat.")]),
  ch(4, "Deliverance Is Not for Me in Renunciation", "Freedom is not found in fleeing the world, but in embracing life with a thousand bonds of delight.", [
    "Many ascetic traditions demand that seekers renounce the senses, despise the body, and flee worldly delight.",
    "Tagore boldly rejects world-denying asceticism in Poem 73.",
    "Deliverance is not for me in renunciation. I feel the embrace of freedom in a thousand bonds of delight.",
    "Thou ever pourest for me the fresh draught of thy wine of various colors and fragrance, filling this earthen vessel to the brim.",
    "The world is not an evil illusion to be shunned; it is a radiant banquet of divine beauty to be celebrated with joy.",
    "My world will keep its hundred different lamps lit with thy flame and place them before the altar of thy temple.",
    "No, I will never shut the doors of my senses. The delights of sight and hearing and touch will bear thy delight.",
    "Taste the splendor of art, friendship, nature, and song with holy gratitude and an open heart."
  ], [
    ("Embrace the sacred banquet of life", "Sensory beauty is a divine gift to be enjoyed with reverence, not an evil trap to avoid."),
    ("Freedom within connection", "True liberation is experienced through a thousand loving bonds of delightful relationship."),
    ("Do not extinguish the senses", "Let sight, hearing, and touch become windows of wonder and gratitude for existence.")
  ], ("Deliverance is not for me in renunciation. I feel the embrace of freedom in a thousand bonds of delight. — Rabindranath Tagore", "quote"), [
    "Enjoy the colors of a sunset, the aroma of fresh bread, and the beauty of music without monastic guilt.",
    "Reject toxic self-denial; celebrate healthy physical vitality and wholesome creative pleasures.",
    "Cultivate deep friendships and creative passions as joyful threads in your spiritual tapestry."
  ], [("siddhartha", 4, "Siddhartha learns that true enlightenment embraces the full sensory dance of earthly reality.")]),
  ch(5, "The Journey Home", "The traveler has to knock at every alien door to come to his own; the song I came to sing remains unsung.", [
    "The time that my journey takes is long and the way of it long.",
    "I came out on the chariot of the first gleam of light, and my path through the wildernesses of worlds left its impression upon many a star.",
    "It is the most distant course that comes nearest to thyself, and that training is the most intricate which leads to the utter simplicity of a tune.",
    "The traveler has to knock at every alien door to come to his own, and one has to wander through all the outer worlds to reach the innermost shrine at the end.",
    "My eyes strayed far and wide before I shut them and said: 'Here art thou!'",
    "We search across oceans and foreign lands for the peace that was waiting quietly in our own chest.",
    "The longest journey of any human soul is the journey that leads back home to its authentic self.",
    "Rest from outer wandering, close your restless eyes, and discover the radiant presence within."
  ], [
    ("The longest journey leads home", "Wandering through alien philosophies and distant lands ultimately returns us to our own heart."),
    ("The complexity of simplicity", "Achieving profound inner simplicity requires extensive spiritual discipline and wandering."),
    ("The shrine within", "The divine truth sought across external mountains was dwelling quietly within all along.")
  ], ("The traveler has to knock at every alien door to come to his own. — Rabindranath Tagore", "quote"), [
    "Do not regret past detours, false starts, and mistakes; they were necessary steps on the road back to your center.",
    "Stop looking to external approval or exotic places to fix your life; find peace right where you stand today.",
    "Take fifteen minutes of silence tonight, closing your eyes to rest in the sanctuary of your own being."
  ], [("the-alchemist", 6, "The treasure sought at the Egyptian pyramids was buried beneath the roots of the home tree all along.")]),
  ch(6, "In One Salutation to Thee", "At the end of life's voyage, let all my songs and actions gather like homeward swans into one final salutation.", [
    "Tagore concludes Gitanjali with Poem 103: a magnificent symphony of complete surrender and peace.",
    "In one salutation to thee, my God, let all my senses spread out and touch this world at thy feet.",
    "Like a rain-cloud of July hung low with its burden of unshed showers let all my mind bend down at thy door in one salutation to thee.",
    "Let all my songs gather together their diverse strains into a single current and flow to a sea of silence in one salutation to thee.",
    "Like a flock of homesick cranes flying night and day back to their mountain nests, let all my life take its voyage to its eternal home in one salutation to thee.",
    "At the close of our brief mortal dance, let our striving dissolve into profound gratitude.",
    "Every song, every tear, and every trial gathers into a single river flowing home to the sea of quiet eternity.",
    "Live with such grace that when the final call arrives, your soul departs like homeward cranes flying to their nest."
  ], [
    ("The ultimate gathering of the self", "All diverse life experiences, joys, and sorrows merge into a singular river of gratitude."),
    ("The rain-cloud of humility", "Bending down like a heavy cloud ready to bless the parched earth with gentle rain."),
    ("The voyage of the homeward cranes", "Death is not a violent terror, but a peaceful return of the soul to its eternal home.")
  ], ("Like a flock of homesick cranes flying night and day back to their mountain nests, let all my life take its voyage to its eternal home. — Rabindranath Tagore", "quote"), [
    "End every day by mentally gathering all your accomplishments and frustrations into one quiet prayer of gratitude.",
    "Let go of petty rivalries before sleep, remembering that life is a brief homeward flight.",
    "Live each hour so that when your journey concludes, you can look back with peaceful, unblemished honor."
  ], [("mans-search-for-meaning", 6, "Tragic optimism enables human beings to affirm life with gratitude even in the presence of mortality.")])
])

print(f"gen_hero_self.py: Total books now: {len(books)} (including Gitanjali)")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)
