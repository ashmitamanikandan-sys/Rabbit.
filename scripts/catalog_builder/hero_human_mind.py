# -*- coding: utf-8 -*-
"""
hero_human_mind.py
Defines the 12 complete Hero Books for 'The Human Mind'.
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

HERO_HUMAN_MIND = []

# 4. The 48 Laws of Power
HERO_HUMAN_MIND.append({
  "id": "the-48-laws-of-power",
  "title": "The 48 Laws of Power",
  "author": "Robert Greene",
  "genre": "The Human Mind",
  "cover_url": "https://covers.openlibrary.org/b/id/12843462-M.jpg",
  "public_domain": False, "fiction": False,
  "chapters": [
    ch(1, "Never Outshine the Master", "Always make those above you feel comfortably superior in intelligence and standing.", [
      "Everyone possesses insecurities, but superiors feel them with heightened intensity.",
      "When you flaunt your talents or display effortless brilliance, you evoke silent dread in leadership.",
      "In 1661, Nicolas Fouquet threw the most extravagant party in French history to impress King Louis XIV.",
      "Instead of gratitude, the King felt outshone and had Fouquet imprisoned for the remainder of his life.",
      "To advance, make your masters appear more brilliant and luminous than they truly are.",
      "Attribute your best ideas to their quiet guidance or offhand remarks.",
      "Discreet flattery is a shield that disarms jealousy and secures your position.",
      "Master the art of selective modesty to advance without awakening dangerous rivals."
    ], [
      ("Insecurity rules high office", "Superiors crave affirmation and react viciously when subordinates expose their limitations."),
      ("Ostentatious talent invites ruin", "Flaunting gifts triggers envy; masking them in modesty creates patient opportunity."),
      ("Credit should flow upward", "Attributing breakthroughs to mentors converts potential rivals into staunch protectors.")
    ], ("Make your masters appear more brilliant than they are, and you will attain the heights of influence.", "rabbit_take"), [
      "When proposing a solution in meetings, frame it as an extension of a theme your manager previously mentioned.",
      "Avoid correcting teachers or senior colleagues publicly; offer insights privately as humble questions.",
      "Dress neatly but avoid overshadowing the host or team leader at formal company gatherings."
    ], [("influence-psychology-of-persuasion", 5, "Liking and deference disarm resistance far faster than aggressive argument.")]),
    ch(2, "Conceal Your Intentions", "Keep people off-balance and in the dark by never revealing the purpose behind your actions.", [
      "Human beings are open books by default, desperate to share their plans and seek validation.",
      "This transparent impulse hands your competitors the exact roadmap to block your path.",
      "By concealing your true intentions, you prevent rivals from preparing defenses or organizing opposition.",
      "Use decoys, false trails, and smoke screens to misdirect the curiosity of onlookers.",
      "Talk openly about trivial opinions to give the impression of total transparency.",
      "When people believe they understand your goals, they lower their guard and grow complacent.",
      "By the time they realize your actual objective, it is already too late for them to interfere.",
      "Calculated silence preserves your strategic advantage across every competitive arena."
    ], [
      ("Transparency forfeits leverage", "Announcing your moves in advance allows adversaries to anticipate and counter your progress."),
      ("Smoke screens generate false security", "Chattering about harmless trivialities convinces observers that you harbor no hidden ambitions."),
      ("Timing is protected by secrecy", "Striking without prior fanfare ensures your plans face minimal friction.")
    ], ("If people have no clue what you are up to, they cannot prepare a defense.", "rabbit_take"), [
      "Do not announce your preparation for a competitive job or school transfer until the offer is secured.",
      "Keep project prototypes private until they are polished enough to speak for themselves.",
      "Avoid broadcasting financial moves or investments on social channels where others can mimic or critique them."
    ], [("the-laws-of-human-nature", 3, "Observing social masks allows you to conceal your own motivations effectively.")]),
    ch(3, "Always Say Less Than Necessary", "When you are trying to impress people with words, the more you say, the more common you appear.", [
      "Powerful people impress and intimidate by saying less than everyone else in the room.",
      "The more you speak, the more likely you are to say something foolish or reveal your anxieties.",
      "Short, measured answers create an aura of mysterious depth that forces others to fill the silence.",
      "In their nervous discomfort, other people will babble and reveal their hand, weaknesses, and secrets.",
      "King Louis XIV was famously economical with language, responding to lengthy appeals with a calm: 'I shall see.'",
      "Nobody could decipher his thoughts, which kept ministers terrified and perpetually eager to please him.",
      "Silence is an instrument of psychological dominance that costs nothing to employ.",
      "Guard your tongue like gold, for once words leave your mouth, you can never retrieve them."
    ], [
      ("Verbosity signals weakness", "Over-explaining betrays a desperate craving for approval and reassurance from listeners."),
      ("Silence commands authority", "Brief, deliberate responses force the other party to reveal their underlying anxieties."),
      ("Careless words cannot be recalled", "A single impulsive remark can destroy years of painstakingly built reputation.")
    ], ("The more you say, the more common you appear, and the less in control you remain.", "rabbit_take"), [
      "Count to three before answering probing questions during job interviews or intense discussions.",
      "Resist the urge to jump into awkward group pauses; let someone else speak first and reveal their stance.",
      "Write concise emails with clear bullet points rather than winding paragraphs that beg for validation."
    ], [("thinking-fast-and-slow", 1, "Quick reactive speech is driven by System 1 emotional impulses.")]),
    ch(4, "Guard Your Reputation With Your Life", "Reputation is the cornerstone of influence; through reputation alone you can intimidate and win.", [
      "In the social arena, appearances are the reality upon which all judgments are constructed.",
      "A single outstanding quality—whether iron discipline, generosity, or daring—can anchor your public aura.",
      "Once a solid reputation is established, it precedes you and wins half the battle before you arrive.",
      "Conversely, a tarnished reputation opens you to endless attacks, ridicule, and suspicion from all sides.",
      "During the American Civil War, General Stonewall Jackson built an aura of ferocious unpredictability.",
      "Enemy commanders hesitated and panicked simply upon hearing rumors that Jackson might be nearby.",
      "Never respond to petty attacks with defensive anger, which merely legitimizes the attacker's accusations.",
      "Maintain an impeccable, consistent public record and let your quiet results refute your detractors."
    ], [
      ("Aura precedes action", "A legendary reputation does the heavy lifting of persuasion before you even speak a sentence."),
      ("Defensiveness confirms suspicion", "Lashing out at critics makes you look guilty, agitated, and weak."),
      ("Anchor on one unmistakable strength", "Known reliability in one specific virtue makes people trust your overall competence.")
    ], ("Reputation is an invisible fortress that protects you from the arrows of envy and malice.", "rabbit_take"), [
      "Always deliver on small commitments to friends so you become known as the person whose word is sacred.",
      "Refuse to participate in office or hallway gossip; a reputation for confidentiality is rare and magnetic.",
      "Keep your digital footprint clean and thoughtful; old posts are permanent public records."
    ], [("the-psychology-of-money", 3, "Reputation is an invaluable asset that must never be risked for short-term vanity.")]),
    ch(5, "Win Through Your Actions, Never Through Argument", "Any momentary triumph you gain through debate is really a Pyrrhic victory that breeds resentment.", [
      "You can argue with someone until you are blue in the face, citing statistics and flawless logic.",
      "Even if you prove them mathematically wrong, you have humiliated their pride and created an enemy.",
      "People do not abandon beliefs when attacked; they dig their heels in and rationalize harder.",
      "The far more potent path is demonstration: show the truth through tangible, physical results.",
      "When Michelangelo was told by a patron that a statue's nose was too long, he did not argue.",
      "He climbed the scaffolding, tapped his chisel softly while letting marble dust fall, and asked if it was better.",
      "The patron praised the improvement, completely satisfied, without Michelangelo changing a single millimeter.",
      "Demonstrate the reality through living proof and let the results speak for your viewpoint."
    ], [
      ("Verbal debate poisons goodwill", "Winning an argument wounds the other person's ego and creates lingering resentment."),
      ("Demonstration bypasses defensiveness", "Tangible physical evidence persuades the eye without attacking the listener's pride."),
      ("Let others retain their dignity", "Providing an honorable exit allows people to adopt your reality without losing face.")
    ], ("Do not argue. Demonstrate. It is far more powerful to make others see than to make them listen.", "rabbit_take"), [
      "Instead of debating which study method works best, use yours quietly and let your exam scores do the talking.",
      "Build a working mini prototype of an app feature rather than arguing abstractly in team meetings.",
      "Clean the shared kitchen yourself without complaining; the visual standard will shame roommates into helping."
    ], [("influence-psychology-of-persuasion", 4, "Social proof and visible examples persuade far deeper than abstract verbal logic.")]),
    ch(6, "Master the Art of Timing", "Never look hurried; keep emotions calm, anticipate trends, and strike only when the hour is ripe.", [
      "Hurriedness betrays a lack of control over time and your own internal emotional state.",
      "Those who master power cultivate three forms of time: historical time, forced time, and end time.",
      "Historical time involves sensing the cultural zeitgeist and riding societal waves as they crest.",
      "Forced time involves deliberately disrupting an opponent's rhythm, making them rush into impulsive blunders.",
      "End time is the decisive, uncompromising strike executed when the pieces are perfectly aligned.",
      "Joseph Fouché survived the French Revolution, the Terror, and Napoleon by mastering patient timing.",
      "He knew when to vanish into political obscurity and exactly when to re-emerge as an indispensable mediator.",
      "Patience is not passive waiting; it is active, vigilant preparation for the inevitable shift in fortunes."
    ], [
      ("Impatience reveals vulnerability", "Rushing an outcome shows your desperation and allows adversaries to dictate terms."),
      ("Control the opponent's clock", "Forcing others to make decisions under time pressure leads to unforced errors."),
      ("Patience is active vigilance", "Waiting for the right moment requires sharpening your tools in quiet obscurity.")
    ], ("He who controls time controls the decisions of everyone operating within it.", "rabbit_take"), [
      "Sleep on major career or academic choices rather than accepting rushed deadlines imposed by others.",
      "Notice emerging shifts in tech or culture early and invest your learning months before the mainstream arrives.",
      "Wait for emotional storms in family arguments to clear before proposing your thoughtful compromise."
    ], [("the-psychology-of-money", 4, "Long-term patience allows compounding and timing to work miracles on your behalf.")])
  ]
})

# 5. Surrounded by Idiots
HERO_HUMAN_MIND.append({
  "id": "surrounded-by-idiots",
  "title": "Surrounded by Idiots",
  "author": "Thomas Erikson",
  "genre": "The Human Mind",
  "cover_url": "https://covers.openlibrary.org/b/id/10255860-M.jpg",
  "public_domain": False, "fiction": False,
  "chapters": [
    ch(1, "The Four Color Personalities", "Why communicating effectively requires understanding four distinct psychological temperaments.", [
      "Have you ever walked out of a conversation wondering why the other person behaved like an idiot?",
      "Thomas Erikson explains that people are not idiots; they simply operate on different behavioral operating systems.",
      "Based on the DISC model, human communication styles fall into four primary color codes.",
      "Reds are dominant, decisive, and ambitious, caring primarily about fast tangible results.",
      "Yellows are spontaneous, optimistic, and talkative, thriving on creative enthusiasm and connection.",
      "Greens are calm, supportive, and patient, prioritizing team harmony and stable routines.",
      "Blues are analytical, precise, and reserved, valuing accuracy, structure, and empirical logic above all.",
      "Communication breakdown happens when you speak your native color to someone of another color."
    ], [
      ("Behavior is not malice", "Misunderstandings occur because people process reality through different cognitive lenses."),
      ("The four color spectrum", "Red seeks results, Yellow seeks inspiration, Green seeks harmony, and Blue seeks facts."),
      ("Adapt to the listener", "Effective communicators translate their message into the color code of their audience.")
    ], ("Communication takes place on the recipient's terms, not the speaker's.", "rabbit_take"), [
      "Notice whether your lab partner prefers quick summaries or detailed step-by-step documentation.",
      "Tailor project pitches to focus on speed for Red managers and rigorous data for Blue managers.",
      "Do not take a colleague's bluntness personally; they may simply be a task-focused Red personality."
    ], [("thinking-fast-and-slow", 1, "Quick personality impressions are filtered through automatic System 1 biases.")]),
    ch(2, "Red: The Dominant Leader", "How to communicate with fast-paced, ambitious personalities who despise wasting time.", [
      "Reds are natural pioneers who wake up eager to conquer obstacles and take command.",
      "They are comfortable with conflict, speak directly without cushioning, and make quick decisions.",
      "To an unaccustomed observer, Reds can appear tyrannical, impatient, and emotionally cold.",
      "However, their bluntness is not personal; they simply view pleasantries as unnecessary friction.",
      "If you want to collaborate with a Red, eliminate small talk and lead with the bottom-line result.",
      "Do not explain the fifteen steps you took; tell them the final outcome and the required next action.",
      "Present challenges as opportunities for victory, and never make excuses for delays.",
      "Give them the high-level steering wheel, and they will run through brick walls for the team."
    ], [
      ("Reds prioritize speed and results", "They evaluate colleagues based on competence and execution rather than warmth."),
      ("Directness is not hostility", "A Red's blunt critique is focused on solving the problem, not wounding your ego."),
      ("Lead with the conclusion", "Summarize the bottom-line payoff in the first thirty seconds of conversation.")
    ], ("With a Red personality, cut the small talk and deliver the bottom line immediately.", "rabbit_take"), [
      "When emailing a Red professor or boss, use three short bullet points stating what is needed.",
      "Do not bring problems to a Red without bringing two concrete, actionable solutions.",
      "Stand your ground calmly during disagreements; Reds respect strength and lose respect for trembling deference."
    ], [("the-48-laws-of-power", 3, "Saying less than necessary keeps interactions with dominant leaders crisp and effective.")]),
    ch(3, "Yellow: The Inspiring Communicator", "Harnessing the creative energy of spontaneous optimists who thrive on applause and vision.", [
      "Yellows enter the room with warmth, humor, and an endless fountain of colorful ideas.",
      "They are social catalysts who make people laugh, spark creative brainstorming, and build team morale.",
      "Their weakness is follow-through: Yellows love launching exciting projects but despise tedious administrative details.",
      "They talk continuously, jump between topics without warning, and frequently forget deadlines.",
      "To communicate with a Yellow, match their enthusiasm and give them public recognition.",
      "Do not drown them in spreadsheets or microscopic protocols during early discussions.",
      "Help them anchor their brilliant visions to written checklists and calendar reminders.",
      "When a Yellow feels emotionally appreciated, their creative output can inspire an entire company."
    ], [
      ("Yellows run on social energy", "Their motivation is fueled by public praise, laughter, and collaborative excitement."),
      ("Creative vision over detail", "They excel at big-picture concepts but need support with structured operational follow-through."),
      ("Listen to their stories", "Validating their expressive nature opens the door to productive working agreements.")
    ], ("Inspire a Yellow with vision and praise, then quietly support them with structured follow-through.", "rabbit_take"), [
      "Acknowledge creative ideas enthusiastically before gently walking through practical deadlines.",
      "Follow up verbal agreements with friendly text summaries so key tasks are not forgotten.",
      "Place Yellows in roles involving public speaking, onboarding new members, or hosting events."
    ], [("influence-psychology-of-persuasion", 5, "Building genuine liking unlocks natural cooperation with expressive personalities.")]),
    ch(4, "Green: The Loyal Peacemaker", "Understanding the gentle majority who value security, stability, and emotional harmony.", [
      "Greens make up roughly forty percent of the population and form the backbone of cohesive communities.",
      "They are calm, patient, empathetic listeners who hate sudden changes and interpersonal drama.",
      "A Green rarely seeks the spotlight; they prefer being the reliable, quiet contributor behind the scenes.",
      "Because they dislike conflict, Greens will nod politely even when they disagree, building silent internal resentment.",
      "To connect with a Green, show authentic personal warmth and provide advance warning for changes.",
      "Never ambush them with sudden reorganizations or aggressive confrontations in public meetings.",
      "Give them space to share their true thoughts by asking gently in one-on-one settings.",
      "Their loyalty and steadfast support will anchor your organization through every chaotic season."
    ], [
      ("Greens are natural stabilizers", "They prioritize team harmony, steady routines, and low-conflict environments."),
      ("Resistance to sudden upheaval", "Unannounced shifts trigger acute anxiety; Greens require time to absorb changes."),
      ("Unexpressed conflict festers", "Their reluctance to disagree verbally means leaders must actively invite their candid feedback.")
    ], ("Treat Greens with patience and consistency, and they will become your most loyal allies.", "rabbit_take"), [
      "Give friends advance notice before changing weekend plans so they can mentally adjust comfortably.",
      "Ask quiet group members privately for their opinion on team decisions rather than putting them on the spot.",
      "Express gratitude for small, unglamorous contributions that keep your household or office running smoothly."
    ], [("the-laws-of-human-nature", 2, "Developing deep empathy reveals the quiet concerns of supportive team members.")]),
    ch(5, "Blue: The Detail-Oriented Thinker", "Engaging the analytical perfectionists who demand facts, accuracy, and rigorous order.", [
      "Blues are the systematic realists who read the instruction manual before plugging in the device.",
      "They double-check calculations, organize spreadsheets with meticulous care, and spot tiny flaws in plans.",
      "To other colors, Blues can look cold, skeptical, detached, and paralyzed by overthinking.",
      "They do not trust gut feelings or emotional appeals; they trust peer-reviewed studies and verifiable data.",
      "To persuade a Blue, arrive thoroughly prepared with documented evidence and clear timelines.",
      "Never tell a Blue that an idea just 'feels right'; show them the metrics, precedents, and contingency plans.",
      "Give them uninterrupted time to think things through rather than demanding instant verbal commitments.",
      "Their rigorous pursuit of precision saves teams from catastrophic, unvetted mistakes."
    ], [
      ("Blues demand factual proof", "They trust logic, methodology, and empirical evidence above emotional charm."),
      ("Perfectionism can cause paralysis", "The pursuit of flawless accuracy can delay launches if clear boundaries are not set."),
      ("Respect their systematic order", "Disorganized presentations or sloppy data will permanently disqualify your proposal.")
    ], ("Win over a Blue with documented facts and thorough preparation, never with emotional hype.", "rabbit_take"), [
      "Include citations and clear numbers when presenting a project proposal to analytical teachers.",
      "Give friends time to research options before booking shared travel accommodations.",
      "Appreciate the friend who reads the fine print of lease agreements; their skepticism protects you."
    ], [("deep-work", 1, "Analytical precision requires deep cognitive focus protected from erratic distractions.")]),
    ch(6, "Body Language and Hidden Signals", "Decoding the physical cues that reveal what people truly feel beneath their spoken words.", [
      "Spoken words convey only a fraction of the emotional message transmitted in any human interaction.",
      "Tone of voice, posture, facial micro-expressions, and physical distance communicate the raw truth.",
      "Reds lean forward aggressively with intense eye contact, asserting territory and demanding pace.",
      "Yellows gesture expansively with open arms, invade personal space affectionately, and smile constantly.",
      "Greens maintain relaxed, closed postures, gentle nods, and polite, non-confrontational smiles.",
      "Blues stand upright with controlled gestures, guarded expressions, and deliberate physical boundaries.",
      "When someone's words conflict with their body language, always trust the body language.",
      "Tuning your awareness to physical signals prevents blindsiding and transforms social intelligence."
    ], [
      ("The body speaks the unfiltered truth", "Conscious speech can disguise intentions, but posture and eyes leak authentic emotion."),
      ("Physical distance reflects comfort", "Leaning in signals interest and rapport, while leaning back indicates skepticism or withdrawal."),
      ("Calibrate to behavioral cues", "Matching subtle nonverbal signals establishes subconscious trust across all personality types.")
    ], ("When verbal words and physical body language disagree, trust the physical signals every single time.", "rabbit_take"), [
      "Notice if a friend's feet point toward the exit while talking; they need to leave even if being polite.",
      "Uncross your arms and relax your shoulders during tense talks to de-escalate group tension.",
      "Observe micro-expressions of hesitation when colleagues agree to tasks; follow up to ensure real commitment."
    ], [("influence-psychology-of-persuasion", 5, "Subconscious physical mirroring creates rapid rapport and mutual affinity.")])
  ]
})

print("hero_human_mind.py written.")
