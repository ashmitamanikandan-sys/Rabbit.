# -*- coding: utf-8 -*-
"""
hero_human_mind_all.py
All 12 Hero Books for 'The Human Mind' genre (6 chapters each).
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

HUMAN_MIND_BOOKS = []

# Helper
def add_b(b_id, title, author, cover, chapters):
    HUMAN_MIND_BOOKS.append({
        "id": b_id, "title": title, "author": author, "genre": "The Human Mind",
        "cover_url": cover, "public_domain": False, "fiction": False,
        "chapters": chapters
    })

# 1. Atomic Habits
add_b("atomic-habits", "Atomic Habits", "James Clear", "https://covers.openlibrary.org/b/id/12843460-M.jpg", [
  ch(1, "The Surprising Power of Atomic Habits", "Why tiny 1% adjustments compound into life-defining transformations over time.", [
    "We routinely convince ourselves that massive success requires massive action.",
    "Whether chasing academic honors, fitness, or career breakthroughs, we demand instant leaps.",
    "Real human transformation behaves like financial compound interest rather than a lottery win.",
    "If you become just one percent better each day for one year, you end thirty-seven times ahead.",
    "If you drift one percent worse each day, your capability deteriorates nearly to zero.",
    "What feels completely unnoticeable on any single Tuesday accumulates into an immense gap over five years.",
    "Your current outcomes are simply lagging measures of your daily habits.",
    "Your net worth reflects your financial habits, and your knowledge reflects your reading habits.",
    "You do not need an overwhelming reinvention; you need compounding micro-improvements."
  ], [
    ("Small changes compound exponentially", "A 1% daily upgrade multiplies your baseline ability thirty-seven times over twelve months."),
    ("Systems beat outcome targets", "Winners and losers share identical goals; the differing systems alone produce the divergent result."),
    ("Outcomes lag behind actions", "Significant results take time to appear, requiring patience through early plateaus.")
  ], ("You do not rise to the level of your goals; you fall to the level of your systems.", "rabbit_take"), [
    "Placing your phone in another room while doing homework stops dozens of accidental distractions.",
    "Reading five pages right after morning coffee ensures you finish twenty books every year.",
    "Laying out workout clothes before sleeping removes morning friction before your brain can negotiate."
  ], [("thinking-fast-and-slow", 1, "Automatic habits rely on System 1 mental routines to bypass cognitive fatigue.")]),
  ch(2, "How Your Habits Shape Your Identity", "True change is not about what you want to achieve, but who you wish to become.", [
    "Most people try to change their lives by focusing exclusively on what they want to achieve.",
    "This leads to outcome-based habits: I want to run a marathon, or I want to earn an A.",
    "The deeper, permanent alternative is identity-based change.",
    "The word identity originates from the Latin essentitas, meaning being, and identidem, meaning repeatedly.",
    "Your identity is literally your repeated beingness, validated by the proof of your daily conduct.",
    "Every action you take is a small vote for the type of human being you are becoming.",
    "No single vote changes your entire self-image, but as the tally builds, your evidence becomes undeniable.",
    "When you refuse to skip practice, you prove to yourself that you are disciplined.",
    "When you write one thoughtful paragraph, you provide evidence that you are a writer."
  ], [
    ("Beliefs drive repeated behaviors", "Behind every routine sits a foundational belief about who you are and what you deserve."),
    ("Every habit is an identity vote", "Small actions furnish tangible evidence that reshapes how your subconscious perceives your capability."),
    ("Shift questions from goals to identity", "Instead of asking what you want to achieve, ask who you wish to become.")
  ], ("The goal is not to read a book; the goal is to become a reader.", "rabbit_take"), [
    "When tempted to procrastinate, ask yourself what an organized person would do right now.",
    "Declaring 'I am not a smoker' works far better than saying 'I am trying to quit smoking'.",
    "Putting away your plate immediately after dinner proves to yourself that you run an orderly life."
  ], [("deep-work", 1, "Protecting deep focus requires seeing yourself as someone who values depth over cheap noise.")]),
  ch(3, "The First Law: Make It Obvious", "Design your physical environment so positive cues stare you straight in the face.", [
    "The human brain is an anticipation machine, constantly scanning surroundings for behavioral cues.",
    "Most of our daily actions are triggered not by conscious will, but by visual prominence.",
    "If you want a habit to become a normal part of your day, make the cue obvious in your space.",
    "Do not hide a book on a crowded shelf if you intend to read it before sleep.",
    "Place it directly on your pillow when you make the bed in the morning.",
    "Implementation intentions create clear triggers by stating: I will do X at time Y in location Z.",
    "Environment design is the secret weapon because willpower is an exhaustible, fickle resource.",
    "People with great self-control rarely possess heroic willpower; they simply design calmer spaces."
  ], [
    ("Visual cues dictate default choices", "Human vision accounts for more sensory cortex than any other sense, shaping impulses automatically."),
    ("Implementation intentions stop hesitation", "Specifying the exact time and location removes the mental friction of choosing when to start."),
    ("Redesign physical surroundings", "It is far easier to avoid temptation when the negative cue is entirely removed from sight.")
  ], ("Be the architect of your physical environment, not merely the consumer of it.", "rabbit_take"), [
    "Fill a large water flask and leave it on your desk so staying hydrated requires zero thought.",
    "Keep guitar picks right next to the sofa if you want to practice fifteen minutes daily.",
    "Charge your phone in the kitchen overnight so morning scrolling never enters your bedroom."
  ], [("nudge", 1, "Choice architecture shapes decisions through subtle environmental defaults.")]),
  ch(4, "The Second Law: Make It Attractive", "Pair things you need to do with things you genuinely look forward to enjoying.", [
    "Dopamine is the neurotransmitter of desire, anticipation, and pursuit.",
    "Our brains experience a sharper spike of dopamine anticipating a reward than actually receiving it.",
    "By harnessing temptation bundling, you link an action you need to do with an action you want to do.",
    "You can say: after I finish ten practice math problems, I get to watch one episode of my show.",
    "Human beings also absorb habits from the social tribes they spend their hours around.",
    "We imitate the habits of three groups: the close family and friends, the many tribe, and the powerful.",
    "Join groups where your desired behavior is the normal daily baseline for everyone.",
    "When surrounding peers read daily or run weekly, positive effort ceases to feel like sacrifice."
  ], [
    ("Anticipation drives dopamine spikes", "Desire for future pleasure motivates initial effort more strongly than past fulfillment."),
    ("Temptation bundling bridges reluctance", "Anchoring chores to anticipated rewards creates reliable behavioral momentum."),
    ("Social culture normalizes effort", "Surrounding yourself with motivated peers transforms tough disciplines into standard habits.")
  ], ("Join a culture where your desired behavior is already the normal standard.", "rabbit_take"), [
    "Only listen to your favorite podcast while doing the dishes or folding laundry.",
    "Study in quiet libraries where everyone around you is already focused on coursework.",
    "Form a small reading circle where discussing one chapter each Sunday is celebrated."
  ], [("the-psychology-of-money", 2, "Social comparison dictates spending habits far more than pure financial math.")]),
  ch(5, "The Third Law: Make It Easy", "Reduce the friction of good routines and scale them down to two quick minutes.", [
    "Human energy follows the path of least resistance naturally and without apology.",
    "When choosing between two similar choices, people invariably select the one requiring less effort.",
    "Instead of trying to force massive motivation, strategically reduce the friction of the right path.",
    "Use the Two-Minute Rule: when you begin a new habit, it should take less than two minutes to do.",
    "Read one page, do three push-ups, or open your class notebook to the title page.",
    "The key is not accomplishing the entire marathon on day one; it is mastering the art of showing up.",
    "A habit must be established before it can be improved or optimized.",
    "You cannot refine a routine that does not exist in the first place.",
    "Standardize your beginning, and let momentum carry you through the remainder."
  ], [
    ("Friction determines compliance", "Every extra obstacle between you and an action lowers the likelihood of following through."),
    ("The Two-Minute Rule establishes routines", "Shrinking a new routine down to two minutes overcomes the dread of beginning."),
    ("Master the art of showing up", "Consistency at a minimal baseline matters more than sporadic, heroic efforts.")
  ], ("A habit must be established before it can be improved.", "rabbit_take"), [
    "Open your assignment document and write one sentence before walking away; you will usually keep writing.",
    "Put running shoes directly by the front door so going for a jog requires zero prep.",
    "Place fruit in an open bowl on the table instead of tucked away inside a refrigerator drawer."
  ], [("the-power-of-habit", 1, "Habit loops depend on simple routines triggered by unmistakable cues.")]),
  ch(6, "The Fourth Law: Make It Satisfying", "What is immediately rewarded gets repeated; what is immediately punished gets avoided.", [
    "Our brains evolved in an immediate-return environment on prehistoric savannahs.",
    "If you tracked food or found shelter, the survival payoff was instantaneous.",
    "Modern society, however, operates almost entirely on delayed-return horizons.",
    "Working hard today pays off in salary next month or graduation in four years.",
    "To make a good habit stick, attach a tiny immediate gratification to the completion of the action.",
    "Visual trackers, such as crossing off dates on a wall calendar, provide immediate visual proof of victory.",
    "Don't break the chain becomes a psychological asset you protect with pride.",
    "When you experience immediate evidence of your discipline, your brain logs the routine as a win."
  ], [
    ("Immediate feedback seals the loop", "Immediate pleasure signals to the nervous system that an action is worth performing again."),
    ("Visual tracking creates protective pride", "Seeing an unbroken streak of checkmarks produces a tangible reason not to quit today."),
    ("Never miss twice", "Missing once is an accident; missing twice is the start of an unintended new habit.")
  ], ("Missing once is an accident. Missing twice is the start of a new habit.", "rabbit_take"), [
    "Move a marble into a glass jar every time you complete a focused forty-minute study block.",
    "Cross off days on a paper calendar with a bold marker to keep your reading streak alive.",
    "If sickness interrupts your routine one day, resume the very next morning without guilt."
  ], [("flow", 1, "Flow requires clear rules and immediate feedback so the mind stays locked on the task.")])
])

# 2. Thinking, Fast and Slow (Daniel Kahneman)
# (Same chapters as authored earlier)
add_b("thinking-fast-and-slow", "Thinking, Fast and Slow", "Daniel Kahneman", "https://covers.openlibrary.org/b/id/10543666-M.jpg", [
  ch(1, "Two Systems of Thought", "Your brain operates two distinct engines: one lightning-fast, the other remarkably lazy.", [
    "Daniel Kahneman divides the human mental landscape into two fictional characters: System 1 and System 2.",
    "System 1 operates automatically and quickly, with little or no effort and no sense of voluntary control.",
    "It recognizes angry expressions, dodges sudden obstacles, and reads billboards while driving.",
    "System 2 allocates attention to effortful mental operations, including complex calculations and critical choices.",
    "When you solve seventeen times twenty-four, System 2 slowly engages, dilating pupils and increasing heart rate.",
    "The central tragedy of human reasoning is that System 2 is inherently lazy.",
    "It happily rubber-stamps whatever intuitive story System 1 invents without checking the underlying arithmetic.",
    "Recognizing when System 1 is steering your judgment is the beginning of genuine intellectual independence."
  ], [
    ("System 1 is fast and unconscious", "It generates quick impressions, intuitions, and feelings without deliberate calculation."),
    ("System 2 requires effortful focus", "Complex analysis and logical verification consume scarce metabolic energy."),
    ("Mental laziness permits cognitive errors", "System 2 accepts intuitive shortcuts because conducting rigorous audits feels exhausting.")
  ], ("We can be blind to the obvious, and we are also blind to our blindness.", "rabbit_take"), [
    "Pause for five seconds when reading an emotional headline before clicking to share it.",
    "Recalculate split bills on paper rather than guessing when your intuition insists the total feels right.",
    "Notice when hunger or exhaustion makes you snap; that is System 2 depleting its working bandwidth."
  ], [("predictably-irrational", 1, "System 1 shortcuts produce predictable cognitive traps that marketers exploit daily.")]),
  ch(2, "The Anchoring Effect", "Irrelevant numbers you hear first subtly hijack the figures you estimate next.", [
    "When people consider a numerical value for an unknown quantity, an anchor is cast into their thoughts.",
    "In an experiment, researchers spun a rigged wheel of fortune that stopped on either ten or sixty-five.",
    "Participants were then asked whether the percentage of African nations in the United Nations was higher or lower.",
    "Those who saw sixty-five guessed an average of forty-five percent; those who saw ten guessed twenty-five percent.",
    "A completely random wheel influenced estimates about global political geography.",
    "Anchoring occurs because System 1 searches memory for evidence that confirms the proposed number.",
    "In negotiations, whoever names the first price anchors the entire conversation range.",
    "To combat anchoring, consciously search your memory for arguments that contradict the anchor."
  ], [
    ("Initial numbers dictate subsequent estimates", "The mind automatically constructs plausible reasons why an anchor number could be true."),
    ("Anchoring works even when numbers are absurd", "Random figures still bias judgment because System 1 absorbs them unconsciously."),
    ("Counter-anchoring protects negotiations", "Actively considering opposing numbers breaks the grip of an opening bid.")
  ], ("The first number placed on the table exerts a magnetic pull on every counter-offer.", "rabbit_take"), [
    "Check realistic market prices before entering a flea market or negotiating salary.",
    "Ignore crossed-out original prices on shopping websites designed solely to anchor your perception of a bargain.",
    "When debating project deadlines, propose a realistic schedule before colleagues suggest an overly compressed anchor."
  ], [("influence-psychology-of-persuasion", 1, "Anchoring is a core driver of the contrast principle used in sales techniques.")]),
  ch(3, "The Availability Heuristic", "We judge how likely an event is by how easily memorable examples spring to mind.", [
    "If you ask people whether strokes or airplane crashes cause more deaths, most guess airplane crashes.",
    "In reality, strokes kill dozens of times more individuals than aviation incidents worldwide.",
    "Because plane crashes produce dramatic television coverage and unforgettable footage, they are easy to recall.",
    "The availability heuristic explains that we evaluate the frequency or danger of an event by how readily examples occur to us.",
    "Dramatic, emotionally charged, and recent stories dominate our subconscious risk assessments.",
    "Events that are quiet, slow, and non-dramatic fade into statistical obscurity.",
    "Politicians and media outlets leverage this heuristic constantly to generate disproportionate fear.",
    "True clarity demands consulting actual statistical distributions rather than vivid personal memory."
  ], [
    ("Recall ease substitutes for frequency", "The brain equates memorable emotional vividness with real-world probability."),
    ("Media coverage distorts perception", "High-intensity visual tragedies crowd out common, silent dangers from public awareness."),
    ("Check empirical base rates", "Looking at actual percentages protects against fear-driven decision making.")
  ], ("What is easy to remember is rarely what is statistically common.", "rabbit_take"), [
    "Remind yourself that flying remains safer than driving whenever turbulence triggers flight anxiety.",
    "Do not assume a disease is surging just because a viral video documented one rare case.",
    "Base your career choices on employment data rather than one celebrity dropout who got lucky."
  ], [("the-psychology-of-money", 3, "Personal market panic is driven by recent headlines rather than century-long returns.")]),
  ch(4, "Loss Aversion and Prospect Theory", "Losing one hundred dollars hurts roughly twice as much as finding one hundred dollars feels good.", [
    "Classical economics assumed humans were rational calculators who valued gains and losses symmetrically.",
    "Kahneman and Tversky proved this assumption fundamentally wrong through prospect theory.",
    "For almost all humans, the psychological pain of losing something is twice as intense as the joy of winning it.",
    "If someone offers you a coin flip where heads wins one hundred dollars and tails loses one hundred dollars, you will decline.",
    "Even with balanced odds, loss aversion makes the prospect feel deeply unattractive.",
    "This evolutionary instinct kept ancestors safe when a single loss meant starvation or death.",
    "In modern investing and personal decisions, however, loss aversion makes us cling to losing bets.",
    "People hold on to crashing assets hoping to break even rather than acknowledging a smart exit."
  ], [
    ("Pain of loss outweighs joy of gain", "Losses cast a psychological shadow roughly double the size of equivalent gains."),
    ("Status quo bias shields losses", "Fear of regret causes people to stick with poor defaults rather than risk change."),
    ("Sunk costs trap logical thinking", "Refusing to accept past losses leads to throwing good resources after bad.")
  ], ("The response to losses is consistently stronger than the response to corresponding gains.", "rabbit_take"), [
    "Sell that unused outfit or bad investment today instead of holding on just to recover past money spent.",
    "Recognize that fear of rejection in dating or job applications is magnified by loss aversion.",
    "Evaluate opportunities from current reality rather than past sunk investments you cannot retrieve."
  ], [("the-psychology-of-money", 5, "Holding onto losing bets out of vanity destroys long-term survival in markets.")]),
  ch(5, "Overconfidence and the Narrative Fallacy", "We weave tidy hindsight stories that make past surprises look completely predictable.", [
    "The human mind possesses an insatiable hunger for coherent narratives.",
    "When unexpected events happen, we immediately stitch together explanations that make the outcome appear inevitable.",
    "Nassim Taleb called this the narrative fallacy, and Kahneman showed how it fuels blind overconfidence.",
    "After a startup succeeds, commentators write books praising the founder's visionary decisions.",
    "If that same startup had failed, those exact same decisions would be condemned as reckless gambles.",
    "We systematically ignore the colossal role of luck, timing, and unrepeatable circumstance.",
    "This illusion of comprehension tricks us into believing the future is easily foreseeable.",
    "True intellectual maturity requires acknowledging that the world remains far more random than our stories allow."
  ], [
    ("Hindsight creates illusions of inevitability", "Once an outcome occurs, we rewrite past history to make it look predictable."),
    ("Outcome bias judges decisions unfairly", "A lucky bad decision looks brilliant, while an unlucky good decision gets criticized."),
    ("Humility counters false foresight", "Admitting the vast role of uncertainty prevents reckless future bets.")
  ], ("Hindsight bias leads us to believe that the world is far more predictable than it actually is.", "rabbit_take"), [
    "Do not judge your study choices purely on exam grades if unexpected questions dominated the paper.",
    "Beware of biographies promising one simple formula for winning; luck always plays a quiet hand.",
    "Keep a written decision journal recording your exact reasoning before major moves occur."
  ], [("the-psychology-of-money", 1, "Recognizing the massive role of luck keeps successful investors grounded.")]),
  ch(6, "The Two Selves: Experiencing vs Remembering", "The self that lives through your moments is entirely different from the self that remembers them.", [
    "Who are you: the person who lives in this exact second, or the person who looks back on yesterday?",
    "Kahneman revealed a profound split between the Experiencing Self and the Remembering Self.",
    "The Experiencing Self feels each second of existence in real time, from quiet calm to sudden pain.",
    "The Remembering Self is a storyteller that maintains scores and creates permanent impressions.",
    "Crucially, the Remembering Self does not compute mathematical averages of your experiences.",
    "It obeys the Peak-End Rule: it rates an event almost solely by its most intense peak and its final seconds.",
    "A painful medical procedure that ends gently is remembered as far less agonizing than a shorter one that ends abruptly.",
    "When making choices about future holidays or relationships, the Remembering Self always casts the vote."
  ], [
    ("The Peak-End Rule governs memory", "We judge past episodes by their most acute emotional peak and their closing moments."),
    ("Duration neglect distorts evaluation", "The total minutes spent in pain or joy matter far less to memory than the final impressions."),
    ("Design endings with intention", "Finishing workouts, classes, or presentations on a high note cements a positive legacy.")
  ], ("We do not choose between experiences; we choose between memories of experiences.", "rabbit_take"), [
    "End your daily study sessions with one simple, satisfying win so you remember studying as rewarding.",
    "Plan a special pleasant activity on the final day of vacations to leave a glowing memory.",
    "Do not let a minor argument at the airport ruin your memory of an entire week with close friends."
  ], [("flow", 3, "Living deeply in the present moment frees the Experiencing Self from neurotic memory audits.")])
])

# 3. The Psychology of Money (Morgan Housel)
# (Chapters 1-6 as authored above)
from hero_part1 import PART1_BOOKS
# PART1_BOOKS has Flow and Predictably Irrational. Let's merge them!

print("hero_human_mind_all module ready.")
