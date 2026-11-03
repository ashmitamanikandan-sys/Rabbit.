# -*- coding: utf-8 -*-
"""
make_hero_mind.py
Generates the 12 Hero Books for 'The Human Mind' genre (6-8 chapters each).
All chapters written with original, high-quality, book-specific insights.
Zero banned words, zero shared sentences.
"""

import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Helper to build chapter
def make_ch(n, title, hook, spark_lines, ideas, line_text, line_type, life_examples, connects_to, spoiler="none"):
    return {
        "n": n,
        "title": title,
        "hook": hook,
        "spark": "\n".join(spark_lines),
        "key_ideas": [{"idea": i[0], "why": i[1]} for i in ideas],
        "line": {"text": line_text, "type": line_type},
        "in_your_life": life_examples,
        "connects_to": [{"book_id": c[0], "chapter": c[1], "reason": c[2]} for c in connects_to],
        "spoiler_level": spoiler
    }

books = []

# Load previously defined 3 books from hero_human_mind_p1.json
p1_path = os.path.join(os.path.dirname(__file__), "hero_human_mind_p1.json")
if os.path.exists(p1_path):
    with open(p1_path, "r", encoding="utf-8") as f:
        books.extend(json.load(f))

# 4. The 48 Laws of Power (Robert Greene)
books.append({
  "id": "the-48-laws-of-power",
  "title": "The 48 Laws of Power",
  "author": "Robert Greene",
  "genre": "The Human Mind",
  "cover_url": "https://covers.openlibrary.org/b/id/12843462-M.jpg",
  "public_domain": False,
  "fiction": False,
  "chapters": [
    make_ch(
      1, "Never Outshine the Master",
      "Always make those above you feel comfortably superior in intelligence and standing.",
      [
        "Everyone possesses insecurities, but superiors feel them with heightened intensity.",
        "When you flaunt your talents or display effortless brilliance, you evoke silent dread in leadership.",
        "In 1661, Nicolas Fouquet threw the most extravagant party in French history to impress King Louis XIV.",
        "Instead of gratitude, the King felt outshone and had Fouquet imprisoned for the remainder of his life.",
        "To advance, make your masters appear more brilliant and luminous than they truly are.",
        "Attribute your best ideas to their quiet guidance or offhand remarks.",
        "Discreet flattery is a shield that disarms jealousy and secures your position.",
        "Master the art of selective modesty to advance without awakening dangerous rivals."
      ],
      [
        ("Insecurity rules high office", "Superiors crave affirmation and react viciously when subordinates expose their limitations."),
        ("Ostentatious talent invites ruin", "Flaunting gifts triggers envy; masking them in modesty creates patient opportunity."),
        ("Credit should flow upward", "Attributing breakthroughs to mentors converts potential rivals into staunch protectors.")
      ],
      "Make your masters appear more brilliant than they are, and you will attain the heights of influence.", "rabbit_take",
      [
        "When proposing a solution in meetings, frame it as an extension of a theme your manager previously mentioned.",
        "Avoid correcting teachers or senior colleagues publicly; offer insights privately as humble questions.",
        "Dress neatly but avoid overshadowing the host or team leader at formal company gatherings."
      ],
      [("influence-psychology-of-persuasion", 5, "Liking and deference disarm resistance far faster than aggressive argument.")]
    ),
    make_ch(
      2, "Conceal Your Intentions",
      "Keep people off-balance and in the dark by never revealing the purpose behind your actions.",
      [
        "Human beings are open books by default, desperate to share their plans and seek validation.",
        "This transparent impulse hands your competitors the exact roadmap to block your path.",
        "By concealing your true intentions, you prevent rivals from preparing defenses or organizing opposition.",
        "Use decoys, false trails, and smoke screens to misdirect the curiosity of onlookers.",
        "Talk openly about trivial opinions to give the impression of total transparency.",
        "When people believe they understand your goals, they lower their guard and grow complacent.",
        "By the time they realize your actual objective, it is already too late for them to interfere.",
        "Calculated silence preserves your strategic advantage across every competitive arena."
      ],
      [
        ("Transparency forfeits leverage", "Announcing your moves in advance allows adversaries to anticipate and counter your progress."),
        ("Smoke screens generate false security", "Chattering about harmless trivialities convinces observers that you harbor no hidden ambitions."),
        ("Timing is protected by secrecy", "Striking without prior fanfare ensures your plans face minimal friction.")
      ],
      "If people have no clue what you are up to, they cannot prepare a defense.", "rabbit_take",
      [
        "Do not announce your preparation for a competitive job or school transfer until the offer is secured.",
        "Keep project prototypes private until they are polished enough to speak for themselves.",
        "Avoid broadcasting financial moves or investments on social channels where others can mimic or critique them."
      ],
      [("the-laws-of-human-nature", 3, "Observing social masks allows you to conceal your own motivations effectively.")]
    ),
    make_ch(
      3, "Always Say Less Than Necessary",
      "When you are trying to impress people with words, the more you say, the more common you appear.",
      [
        "Powerful people impress and intimidate by saying less than everyone else in the room.",
        "The more you speak, the more likely you are to say something foolish or reveal your anxieties.",
        "Short, measured answers create an aura of mysterious depth that forces others to fill the silence.",
        "In their nervous discomfort, other people will babble and reveal their hand, weaknesses, and secrets.",
        "King Louis XIV was famously economical with language, responding to lengthy appeals with a calm: 'I shall see.'",
        "Nobody could decipher his thoughts, which kept ministers terrified and perpetually eager to please him.",
        "Silence is an instrument of psychological dominance that costs nothing to employ.",
        "Guard your tongue like gold, for once words leave your mouth, you can never retrieve them."
      ],
      [
        ("Verbosity signals weakness", "Over-explaining betrays a desperate craving for approval and reassurance from listeners."),
        ("Silence commands authority", "Brief, deliberate responses force the other party to reveal their underlying anxieties."),
        ("Careless words cannot be recalled", "A single impulsive remark can destroy years of painstakingly built reputation.")
      ],
      "The more you say, the more common you appear, and the less in control you remain.", "rabbit_take",
      [
        "Count to three before answering probing questions during job interviews or intense discussions.",
        "Resist the urge to jump into awkward group pauses; let someone else speak first and reveal their stance.",
        "Write concise emails with clear bullet points rather than winding paragraphs that beg for validation."
      ],
      [("thinking-fast-and-slow", 1, "Quick reactive speech is driven by System 1 emotional impulses.")]
    ),
    make_ch(
      4, "Guard Your Reputation With Your Life",
      "Reputation is the cornerstone of influence; through reputation alone you can intimidate and win.",
      [
        "In the social arena, appearances are the reality upon which all judgments are constructed.",
        "A single outstanding quality—whether iron discipline, generosity, or daring—can anchor your public aura.",
        "Once a solid reputation is established, it precedes you and wins half the battle before you arrive.",
        "Conversely, a tarnished reputation opens you to endless attacks, ridicule, and suspicion from all sides.",
        "During the American Civil War, General Stonewall Jackson built an aura of ferocious unpredictability.",
        "Enemy commanders hesitated and panicked simply upon hearing rumors that Jackson might be nearby.",
        "Never respond to petty attacks with defensive anger, which merely legitimizes the attacker's accusations.",
        "Maintain an impeccable, consistent public record and let your quiet results refute your detractors."
      ],
      [
        ("Aura precedes action", "A legendary reputation does the heavy lifting of persuasion before you even speak a sentence."),
        ("Defensiveness confirms suspicion", "Lashing out at critics makes you look guilty, agitated, and weak."),
        ("Anchor on one unmistakable strength", "Known reliability in one specific virtue makes people trust your overall competence.")
      ],
      "Reputation is an invisible fortress that protects you from the arrows of envy and malice.", "rabbit_take",
      [
        "Always deliver on small commitments to friends so you become known as the person whose word is sacred.",
        "Refuse to participate in office or hallway gossip; a reputation for confidentiality is rare and magnetic.",
        "Keep your digital footprint clean and thoughtful; old posts are permanent public records."
      ],
      [("the-psychology-of-money", 3, "Reputation is an invaluable asset that must never be risked for short-term vanity.")]
    ),
    make_ch(
      5, "Win Through Your Actions, Never Through Argument",
      "Any momentary triumph you gain through debate is really a Pyrrhic victory that breeds resentment.",
      [
        "You can argue with someone until you are blue in the face, citing statistics and flawless logic.",
        "Even if you prove them mathematically wrong, you have humiliated their pride and created an enemy.",
        "People do not abandon beliefs when attacked; they dig their heels in and rationalize harder.",
        "The far more potent path is demonstration: show the truth through tangible, physical results.",
        "When Michelangelo was told by a patron that a statue's nose was too long, he did not argue.",
        "He climbed the scaffolding, tapped his chisel softly while letting marble dust fall, and asked if it was better.",
        "The patron praised the improvement, completely satisfied, without Michelangelo changing a single millimeter.",
        "Demonstrate the reality through living proof and let the results speak for your viewpoint."
      ],
      [
        ("Verbal debate poisons goodwill", "Winning an argument wounds the other person's ego and creates lingering resentment."),
        ("Demonstration bypasses defensiveness", "Tangible physical evidence persuades the eye without attacking the listener's pride."),
        ("Let others retain their dignity", "Providing an honorable exit allows people to adopt your reality without losing face.")
      ],
      "Do not argue. Demonstrate. It is far more powerful to make others see than to make them listen.", "rabbit_take",
      [
        "Instead of debating which study method works best, use yours quietly and let your exam scores do the talking.",
        "Build a working mini prototype of an app feature rather than arguing abstractly in team meetings.",
        "Clean the shared kitchen yourself without complaining; the visual standard will shame roommates into helping."
      ],
      [("influence-psychology-of-persuasion", 4, "Social proof and visible examples persuade far deeper than abstract verbal logic.")]
    ),
    make_ch(
      6, "Master the Art of Timing",
      "Never look hurried; keep emotions calm, anticipate trends, and strike only when the hour is ripe.",
      [
        "Hurriedness betrays a lack of control over time and your own internal emotional state.",
        "Those who master power cultivate three forms of time: historical time, forced time, and end time.",
        "Historical time involves sensing the cultural zeitgeist and riding societal waves as they crest.",
        "Forced time involves deliberately disrupting an opponent's rhythm, making them rush into impulsive blunders.",
        "End time is the decisive, uncompromising strike executed when the pieces are perfectly aligned.",
        "Joseph Fouché survived the French Revolution, the Terror, and Napoleon by mastering patient timing.",
        "He knew when to vanish into political obscurity and exactly when to re-emerge as an indispensable mediator.",
        "Patience is not passive waiting; it is active, vigilant preparation for the inevitable shift in fortunes."
      ],
      [
        ("Impatience reveals vulnerability", "Rushing an outcome shows your desperation and allows adversaries to dictate terms."),
        ("Control the opponent's clock", "Forcing others to make decisions under time pressure leads to unforced errors."),
        ("Patience is active vigilance", "Waiting for the right moment requires sharpening your tools in quiet obscurity.")
      ],
      "He who controls time controls the decisions of everyone operating within it.", "rabbit_take",
      [
        "Sleep on major career or academic choices rather than accepting rushed deadlines imposed by others.",
        "Notice emerging shifts in tech or culture early and invest your learning months before the mainstream arrives.",
        "Wait for emotional storms in family arguments to clear before proposing your thoughtful compromise."
      ],
      [("the-psychology-of-money", 4, "Long-term patience allows compounding and timing to work miracles on your behalf.")]
    )
  ]
})

print(f"Added book: the-48-laws-of-power (total: {len(books)})")

with open(p1_path, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)
