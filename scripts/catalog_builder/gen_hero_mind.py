# -*- coding: utf-8 -*-
"""
gen_hero_mind.py
Generates the 12 Hero Books for 'The Human Mind' genre (6-8 chapters each).
Outputs to catalog/hero_mind.json.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
OUT_PATH = os.path.join(ROOT_DIR, "catalog", "hero_mind.json")
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

def add_b(b_id, title, author, cover, chapters):
    books.append({
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

# 2. Thinking, Fast and Slow
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
add_b("the-psychology-of-money", "The Psychology of Money", "Morgan Housel", "https://covers.openlibrary.org/b/id/10595562-M.jpg", [
  ch(1, "No One's Crazy", "Your personal experiences with money make up maybe 0.00000001% of what happened in the world.", [
    "People from different generations, raised by different parents with different incomes, think about money in radically divergent ways.",
    "A child of the Great Depression views market risk and cash safety in a way an eighties tech boom baby cannot fathom.",
    "Someone who grew up in runaway inflation buys hard goods quickly, while someone from stable times hoards paper cash.",
    "None of these people are crazy; they have simply formed financial models based on the specific world they witnessed.",
    "When you see someone spend or save in a manner that looks reckless to you, understand their background first.",
    "Every financial decision an individual makes makes complete sense to them at that exact moment.",
    "They are matching their personal mental ledger of fear, pride, and history to the immediate choice.",
    "Financial wisdom starts by realizing your own background is just one narrow slice of human reality."
  ], [
    ("Early life financial conditions shape lifelong reflexes", "What happened to the economy when you were young permanently anchors your comfort with risk."),
    ("Different experiences produce different rationalities", "What looks like financial insanity to an outsider feels like sensible self-defense to the actor."),
    ("Empathy beats judgment in money talks", "Recognizing varied backgrounds explains household disagreements over investing and saving far better than insults.")
  ], ("Doing well with money has a little to do with how smart you are and a lot to do with how you behave.", "rabbit_take"), [
    "Do not judge your parents' conservative spending habits if they lived through a severe local banking collapse.",
    "Recognize that your own appetite for crypto or stocks was shaped heavily by recent bull markets.",
    "Talk calmly with roommates or partners about their family background before creating shared expense budgets."
  ], [("thinking-fast-and-slow", 3, "Availability heuristics anchor our financial expectations to the few years we personally witnessed.")]),
  ch(2, "Luck & Risk", "Luck and risk are siblings: both prove that outcomes are guided by forces outside your control.", [
    "The world is far too complex to allow 100% of your outcomes to be determined by your own effort.",
    "Every outcome in life is guided by forces other than individual effort, namely luck and risk.",
    "Bill Gates attended Lakeside School, one of the only high schools on Earth with a computer teletype in 1968.",
    "Gates himself admitted that if there were no Lakeside, there would be no Microsoft.",
    "At that same high school, his brilliant classmate Kent Evans shared the exact same skill and ambition.",
    "Kent Evans died in a mountaineering accident before graduating high school.",
    "One experienced one-in-a-million positive luck; the other experienced one-in-a-million negative risk.",
    "Be careful who you praise and admire, and be careful who you look down upon and pity.",
    "Realize that not all success is due to genius, and not all failure is due to laziness."
  ], [
    ("Accident and agency co-exist in every outcome", "Statistical serendipity often plays a decisive role that personal effort cannot overpower."),
    ("Beware of extreme case studies", "Studying outlier billionaires teaches more about unique luck than repeatable daily principles."),
    ("Focus on broad patterns instead of individual icons", "Broad historical truths about diversification and thrift endure far longer than individual genius stories.")
  ], ("Nothing is as good or as bad as it looks.", "rabbit_take"), [
    "Give yourself grace when an honest, well-researched project fails due to sudden market shifts.",
    "Stay humble when an early side-project blows up; acknowledge the tailwinds that helped you along.",
    "Emulate broad virtues like living below your means rather than trying to replicate a celebrity's exact portfolio."
  ], [("thinking-fast-and-slow", 5, "Narrative fallacies erase luck from historical accounts to make victories look inevitable.")]),
  ch(3, "Never Enough", "The hardest financial skill is getting the goalpost to stop moving.", [
    "Modern capitalism is exceptionally good at two things: generating wealth and generating envy.",
    "When expectations rise alongside income, you never feel the slightest increase in security or peace.",
    "You can earn millions and still feel inadequate if your neighboring peers are earning tens of millions.",
    "At a party hosted by a billionaire, Kurt Vonnegut informed Joseph Heller that their host made more money in a day than Heller earned from his novel Catch-22.",
    "Heller calmly replied: 'Yes, but I have something he will never have: enough.'",
    "Knowing what constitutes enough for your soul is the ultimate protective shield.",
    "Without a clear finish line for your desires, you will eventually take risks that ruin everything you built.",
    "There is no reason to risk what you have and need for what you don't have and don't need."
  ], [
    ("Moving goalposts guarantee permanent dissatisfaction", "If your appetite expands at the exact pace of your paycheck, wealth produces zero happiness."),
    ("Social comparison is an unwinnable battle", "There is always someone with a bigger yacht, larger house, or faster sports car."),
    ("Invaluable things must never be risked", "Reputation, freedom, family, and peace of mind must never be staked on speculative gains.")
  ], ("There is no reason to risk what you have and need for what you do not have and do not need.", "rabbit_take"), [
    "Define your desired annual lifestyle cost in writing before you start receiving career promotions.",
    "Mute accounts that trigger lifestyle envy on your feed; they are selling products, not peace.",
    "Celebrate having enough time to read, walk, and sleep instead of chasing prestige titles you secretly hate."
  ], [("the-48-laws-of-power", 4, "Guard your core reputation and sanity because losing them ruins all worldly gains.")]),
  ch(4, "Confounding Compounding", "Warren Buffett's real secret is not his stock picking, but that he has been investing for 80 years.", [
    "Human intuition struggles to grasp the counterintuitive mathematics of exponential compounding.",
    "More than ninety-nine percent of Warren Buffett's wealth was accumulated after his fiftieth birthday.",
    "If Buffett had started investing at age thirty and retired at sixty, few people would know his name today.",
    "His true genius was not just annual returns, but the sheer, unbroken duration of his timeline.",
    "Ice ages on Earth were not caused by brutally cold winters, but by slightly cooler summers that failed to melt winter snow.",
    "The thin residual layer of snow reflected sunlight, cooling the climate further, allowing more snow to persist next year.",
    "Tiny, persistent advantages compounded across vast spans of time produce monumental glacial shifts.",
    "In your personal life, small sums invested early and left undisturbed will always outperform clever, sporadic bets."
  ], [
    ("Time is the engine of compound growth", "The exponent of duration creates the staggering gains, far more than marginal returns."),
    ("Survival enables compounding to work", "You must avoid catastrophic wipeouts so your compounding curve is never forcibly reset to zero."),
    ("Intuition under-appreciates slow beginnings", "Linear minds expect steady growth, but exponential curves remain flat for decades before soaring.")
  ], ("Compounding does not rely on big returns; it relies on uninterrupted, consistent endurance.", "rabbit_take"), [
    "Start investing fifty dollars every month right now, even if the total looks trivial today.",
    "Do not interrupt your savings during market pullbacks; time in the market beats timing the market.",
    "Apply compounding to learning: reading fifteen minutes daily builds an encyclopedic mind by thirty."
  ], [("atomic-habits", 1, "Habits behave identically to financial capital: small inputs yield exponential compound interest.")]),
  ch(5, "Getting Wealthy vs. Staying Wealthy", "Getting money requires taking risks; keeping money requires paranoia, frugality, and humility.", [
    "Getting wealthy and staying wealthy are two completely distinct skill sets that frequently war with each other.",
    "Getting wealthy requires taking bold risks, projecting optimism, and shooting for the stars.",
    "Staying wealthy, however, requires the exact opposite: humility, frugality, and healthy paranoia.",
    "It demands accepting that at least part of your success was driven by luck you cannot easily duplicate.",
    "It means keeping a substantial cash buffer so unexpected emergencies never force you to liquidate assets at market bottoms.",
    "Many brilliant entrepreneurs become rich through audacity, only to go bankrupt because they cannot turn the risk valve off.",
    "Jesse Livermore made one hundred million dollars shorting the 1929 stock market crash, then lost everything within four years.",
    "Survival is the only metric that matters because staying in the game is the prerequisite for all future gains."
  ], [
    ("Risk tolerance must adjust over time", "The reckless aggression that builds an initial nest egg will destroy it if left unchecked."),
    ("Maintain a margin of safety", "A financial plan is only useful if it survives the inevitable errors and market downturns."),
    ("Cash is an emotional shock absorber", "Holding cash may drag statistical returns slightly, but it buys uninterrupted nighttime sleep.")
  ], ("A plan is only good if it can survive reality when reality does not go according to plan.", "rabbit_take"), [
    "Keep three to six months of living expenses in a boring bank account that you never gamble with.",
    "Never borrow money against your investments; leverage turns standard market dips into total ruin.",
    "Treat success as a temporary lease that must be renewed with daily diligence and modesty."
  ], [("the-48-laws-of-power", 6, "Mastering time and defensive posture preserves influence across unpredictable political changes.")]),
  ch(6, "Freedom: The Highest Dividend", "The greatest intrinsic value of money is its ability to give you control over your time.", [
    "More than your house, your wristwatch, or your social standing, the highest dividend money pays is autonomy.",
    "Having the ability to wake up in the morning and say, 'I can do whatever I want today,' is the ultimate wealth.",
    "Decades of psychological research consistently demonstrate that control over one's schedule is the strongest predictor of well-being.",
    "Doing work you love on a schedule you hate feels remarkably similar to doing work you despise.",
    "A person with six months of emergency savings can decline an abusive boss or take an exciting pay cut for an emerging venture.",
    "They possess an invisible degree of leverage that the heavily indebted executive with a luxury sports car lacks.",
    "True riches are defined not by the luxury goods you buy, but by the negative options you can refuse."
  ], [
    ("Time autonomy is the supreme metric of wealth", "Control over daily schedule brings more enduring happiness than any consumer possession."),
    ("Savings buy flexibility and independence", "Unspent money gives you the power to choose what to work on, when to rest, and who to work with."),
    ("Avoid golden handcuffs", "High salaries tied to uncontrollable eighty-hour weeks often feel like plush prison cells.")
  ], ("The highest form of wealth is the ability to wake up and say: I can do whatever I want today.", "rabbit_take"), [
    "Prioritize building savings that give you the courage to leave a toxic job or career path.",
    "Evaluate purchases by asking how many hours of your life energy they cost to acquire.",
    "Choose careers with schedule sovereignty over prestigious titles that demand total constant availability."
  ], [("deep-work", 3, "Sovereignty over your calendar is the essential prerequisite for producing deep, meaningful work.")])
])

# Import Deep Work, 48 Laws, and Surrounded by Idiots from hero_blueprints / hero_human_mind
from hero_blueprints import HERO_BLUEPRINTS
if "deep-work" in HERO_BLUEPRINTS:
    dw = HERO_BLUEPRINTS["deep-work"]
    books.append({
        "id": "deep-work", "title": dw["title"], "author": dw["author"],
        "genre": dw["genre"], "cover_url": dw["cover_url"],
        "public_domain": dw["public_domain"], "fiction": dw["fiction"],
        "chapters": dw["chapters"]
    })

from hero_human_mind import HERO_HUMAN_MIND
for b_item in HERO_HUMAN_MIND:
    if not any(x["id"] == b_item["id"] for x in books):
        books.append(b_item)

# Import Flow & Predictably Irrational from hero_part1
from hero_part1 import PART1_BOOKS
for b_item in PART1_BOOKS:
    if not any(x["id"] == b_item["id"] for x in books):
        books.append(b_item)

# 9. The Power of Habit (Charles Duhigg)
add_b("the-power-of-habit", "The Power of Habit", "Charles Duhigg", "https://covers.openlibrary.org/b/id/10543674-M.jpg", [
  ch(1, "The Habit Loop: Cue, Routine, Reward", "Every automatic behavior in human life follows a three-step neurological loop.", [
    "In the 1990s, MIT neuroscientists discovered that habits are stored in the primitive basal ganglia.",
    "As a behavior becomes automatic, the cognitive prefrontal cortex essentially goes to sleep.",
    "The habit loop consists of three distinct components: a cue, a routine, and a reward.",
    "The cue is a trigger that informs your brain to enter autopilot and selects which habit to deploy.",
    "The routine is the physical, mental, or emotional behavior you carry out automatically.",
    "The reward is the neurochemical payoff that teaches your brain whether this loop is worth remembering.",
    "You cannot extinguish a bad habit; you can only change the routine while keeping the cue and reward intact.",
    "Diagnosing your personal cues and rewards is the foundational step to transforming daily life."
  ], [
    ("The basal ganglia automates routines", "The brain converts repeated sequences into automated chunks to conserve cognitive energy."),
    ("The loop cannot be erased", "Neural pathways of old habits remain permanently etched; they must be overwritten with new routines."),
    ("Identify the real reward", "Craving a cookie at 3 PM is rarely about sugar; it is usually about taking a social break.")
  ], ("Habits can be changed if we understand how they work.", "rabbit_take"), [
    "Notice what triggers your phone scrolling: is it a specific time, a location, or a feeling of boredom?",
    "When craving a sugary snack, stand up and chat with a colleague for five minutes to test if social relief was the real need.",
    "Keep running shoes by your bedside so the physical cue triggers your morning jog without thought."
  ], [("atomic-habits", 3, "Clear visual cues and immediate rewards are the mechanics that drive the habit loop.")]),
  ch(2, "The Craving Brain", "Cravings are the neurological engine that powers the habit loop into automatic overdrive.", [
    "A cue and a reward alone do not build a habit; an intense psychological craving must link them together.",
    "Claude Hopkins made Pepsodent the world's bestselling toothpaste by creating a new craving for a clean feeling.",
    "He pointed out the natural film that covers teeth and promised that brushing creates a cool, tingling sensation.",
    "That tingling sensation of citric acid and mint did not actually clean teeth, but it signaled freshness.",
    "Consumers developed an intense craving for the tingling feeling; without it, their mouths felt dirty.",
    "When your brain anticipates the reward upon seeing the cue, a subconscious craving is born.",
    "If the reward fails to arrive, frustration and irritability surge through your nervous system.",
    "Harness cravings by consciously anticipating the positive emotional payoff of healthy disciplines."
  ], [
    ("Craving powers the loop", "Anticipation of the reward creates the neurological urge that compels immediate action."),
    ("Sensory feedback validates completion", "Tingling sensations and pleasant scents provide tangible proof that the routine worked."),
    ("Channel cravings toward constructive ends", "Associate the post-workout endorphin glow with the cue of tying your laces.")
  ], ("Cravings are what drive habits. Find the craving, and you unlock the key to change.", "rabbit_take"), [
    "Notice the feeling of relief you anticipate before opening an entertaining video feed.",
    "Anchor workouts to the vivid anticipation of how refreshed and calm you will feel in the shower afterward.",
    "Create a sensory reward for study sessions, like enjoying a special cup of herbal tea while reading."
  ], [("atomic-habits", 4, "Temptation bundling harnesses the brain's dopamine craving to make difficult routines attractive.")]),
  ch(3, "The Golden Rule of Habit Change", "To change a habit, you must keep the old cue and old reward, but insert a new routine.", [
    "Alcoholics Anonymous succeeds not by eliminating the emotional cravings that drive drinking, but by redirecting them.",
    "Members drink to relieve anxiety, connect socially, and escape crushing loneliness.",
    "AA provides ninety meetings in ninety days: the exact same cue and reward, but with conversation instead of alcohol.",
    "The Golden Rule of Habit Change states: keep the cue, keep the reward, but substitute the middle routine.",
    "Tony Dungy transformed the Tampa Bay Buccaneers by reducing player hesitation to pure instinct.",
    "He did not teach players hundreds of new formations; he drilled a few basic responses until they reacted without thinking.",
    "Belief is the critical ingredient that makes habit transformation permanent during acute crises.",
    "When adversity strikes, having a supportive community reinforces the conviction that change is possible."
  ], [
    ("Substitute the middle routine", "Trying to suppress urges fails; replacing the action while preserving the payoff succeeds."),
    ("Keep cues and rewards identical", "Match the exact emotional relief of the old habit with a healthier alternative behavior."),
    ("Belief sustains transformation under pressure", "Community support proves that new habits can withstand traumatic life shocks.")
  ], ("You cannot extinguish bad habits; you can only change them.", "rabbit_take"), [
    "When stress urges you to bite your nails, squeeze a small stress ball to satisfy the physical fidgeting reward.",
    "Replace midnight junk food snacking with slicing a fresh crisp apple while watching your evening show.",
    "Join a study group so the social reward of companionship replaces the temptation to ditch coursework."
  ], [("the-mountain-is-you", 1, "Self-sabotage is simply an unconscious mechanism trying to satisfy a legitimate emotional need.")]),
  ch(4, "Keystone Habits: Paul O'Neill", "Certain habits have the power to start a chain reaction that transforms an entire institution.", [
    "When Paul O'Neill became CEO of aluminum giant Alcoa in 1987, Wall Street investors expected financial targets.",
    "Instead, O'Neill stunned shareholders by focusing on a single operational metric: worker safety.",
    "He mandated that every workplace accident must be reported to him within twenty-four hours along with a fix.",
    "To achieve this, factory workers had to communicate freely with managers, breaking down rigid corporate hierarchies.",
    "Safety improvements required redesigning faulty machines, which eliminated manufacturing defects and cut costs.",
    "By focusing on one keystone habit, Alcoa's net income increased fivefold and it became a manufacturing titan.",
    "Keystone habits matter because they introduce small wins that spill over into unrelated areas of life.",
    "Exercise is a classic personal keystone habit: people who start exercising naturally eat better and manage time wiser."
  ], [
    ("Keystone habits trigger cascading upgrades", "Changing one foundational behavior creates positive momentum across unrelated domains."),
    ("Small wins cultivate collective efficacy", "Tiny early victories convince people that larger systematic transformations are achievable."),
    ("Focus on root operational leverage", "Target the single discipline that forces communication and accountability throughout your day.")
  ], ("Some habits matter more than others. Change a keystone habit, and everything else shifts.", "rabbit_take"), [
    "Make regular morning exercise your keystone habit; notice how your diet and sleep naturally fall into place.",
    "Make your bed every morning; this tiny early win establishes an orderly tone for the rest of your day.",
    "Track your daily financial spending; awareness of money naturally curtails impulse shopping."
  ], [("atomic-habits", 2, "Identity-based habits act as keystones that rewrite your fundamental self-image.")]),
  ch(5, "Starbucks and the Habit of Willpower", "Willpower is a learnable skill that can be systematized through advance planning for stress.", [
    "Dozens of studies prove that willpower is the single most reliable predictor of academic and career success.",
    "However, willpower is like a muscle: it tires after heavy exertion, leaving people vulnerable to impulse.",
    "Starbucks realized that barista turnover was driven by stressful interactions with angry, demanding customers.",
    "They developed the LATTE method: Listen, Acknowledge, Take action, Thank the customer, and Explain.",
    "By giving employees an explicit script for moments of conflict, emotional reactivity was converted into routine.",
    "Employees practiced how to respond when a customer screamed about a wrong order, eliminating panic.",
    "When you predetermine how you will handle painful inflection points, your self-control remains steady.",
    "Willpower becomes a habit when you decide how to act before the emotional crisis arrives."
  ], [
    ("Willpower is an exhaustible resource", "Making continuous self-control choices drains the stamina needed for later challenges."),
    ("Pre-plan inflection points", "Anticipating the exact moment when temptation or anger peaks prevents emotional surrender."),
    ("Scripts convert panic into poise", "Having a memorized protocol allows you to execute calmly under intense pressure.")
  ], ("Willpower is not just a skill; it is a muscle that can be systematically trained and preserved.", "rabbit_take"), [
    "Write down exactly what you will say when peers pressure you to skip an important study night.",
    "Anticipate afternoon hunger crashes by keeping healthy almonds in your bag before cravings strike.",
    "Memorize a five-second breathing pause to execute whenever a difficult email triggers instant defensive anger."
  ], [("thinking-fast-and-slow", 1, "Pre-planned protocols prevent reactive System 1 emotional outbursts from driving decisions.")]),
  ch(6, "The Power of a Crisis", "Good leaders seize crises to rewire institutional habits that were previously untouchable.", [
    "During normal times, organizations fall into comfortable truces between rival departments.",
    "These truces protect vested interests and prevent uncomfortable changes, even when efficiency suffers.",
    "A severe crisis shatters these truces, creating a rare window of organizational malleability.",
    "In 2000, Rhode Island Hospital experienced three horrific surgical errors due to toxic nurse-doctor friction.",
    "The administration used the public outrage to install video monitoring, standardized checklists, and culture overhauls.",
    "A crisis creates a sense of urgency that makes people willing to accept sacrifices and new disciplines.",
    "Never waste a crisis; use moments of breakdown to discard toxic habits and establish higher standards.",
    "The pain of sudden failure is often the fertile soil where lifelong discipline takes root."
  ], [
    ("Crises break stagnant truces", "Catastrophes dissolve internal resistance to change that seemed impossible during peaceful times."),
    ("Urgency unites divided factions", "Shared existential threats force competing groups to collaborate on new operational norms."),
    ("Reframe failure as an upgrade catalyst", "Use moments of personal collapse to dismantle bad routines and institute fresh rules.")
  ], ("Never waste a good crisis; use the disruption to establish habits that endure for decades.", "rabbit_take"), [
    "After failing an important exam, completely overhaul your note-taking system while the lesson is fresh.",
    "Use a painful breakup as the catalyst to rebuild your physical fitness and personal independence.",
    "When a team project crashes, call an immediate blameless retrospective to rewrite group protocols."
  ], [("the-subtle-art-of-not-giving-a-fuck", 4, "Painful setbacks reveal our flawed metrics and force us to adopt healthier life values.")])
])

print(f"gen_hero_mind.py compiled {len(books)} books.")

# 10. Influence (Robert Cialdini)
add_b("influence-psychology-of-persuasion", "Influence: The Psychology of Persuasion", "Robert B. Cialdini", "https://covers.openlibrary.org/b/id/10543676-M.jpg", [
  ch(1, "Weapons of Influence: Click, Whirr", "Automatic behavioral triggers allow people to bypass conscious deliberation in decision making.", [
    "Mother turkeys are devoted parents who warm, clean, and protect their chicks with loving care.",
    "All of this maternal behavior is triggered by one single auditory stimulus: the 'cheep-cheep' sound of the poult.",
    "If a stuffed polecat—the turkey's natural predator—emits the recorded cheep sound, the mother turkey cares for it.",
    "If the real chick cannot produce the sound, the mother turkey ignores it or attacks it as a stranger.",
    "Humans possess similar automatic behavioral sequences that Cialdini terms 'click, whirr'.",
    "A specific trigger tape clicks into place, and the standard behavioral script automatically whirrs into action.",
    "Harvard psychologist Ellen Langer proved that adding the word 'because' increases compliance from 60% to 94%.",
    "Even when the reason was meaningless ('because I have to make copies'), the trigger word unlocked agreement."
  ], [
    ("Automatic mental shortcuts dominate life", "Human cognition relies on automatic behavioral tapes to navigate overwhelming daily complexity."),
    ("Trigger features bypass critical analysis", "Certain words and gestures activate automatic compliance without engaging deep logic."),
    ("Awareness disarms manipulation", "Recognizing automatic triggers allows you to hit the mental pause button and audit requests.")
  ], ("Civilization advances by extending the number of operations we can perform without thinking.", "rabbit_take"), [
    "Always provide a reason using the word 'because' when asking someone for a small favor.",
    "Pause when you feel an automatic urge to agree to a request; check if a compliance trigger was pressed.",
    "Notice how discount tags that look like coupons trigger spending even when the price is unchanged."
  ], [("thinking-fast-and-slow", 1, "Click-whirr responses are classic System 1 heuristics operating on autopilot.")]),
  ch(2, "Reciprocation: The Old Give and Take", "The human urge to repay debts is one of the most powerful evolutionary forces in history.", [
    "The rule of reciprocation states that we should try to repay, in kind, what another person has provided us.",
    "Sociologists view this obligation as a unique human adaptation that enabled division of labor and mutual trade.",
    "The rule is so overpowering that it frequently overwhelms feelings of personal dislike for the requester.",
    "The Hare Krishna Society famously handed free flowers to airport passengers before asking for donations.",
    "Even though travelers hated the flower and threw it in the trash, their subconscious felt obligated to donate.",
    "The rejection-then-retreat technique starts with an extreme request you expect to be denied.",
    "When the other person declines, you retreat to your smaller, actual request, which they accept as a concession.",
    "Defend yourself by distinguishing between authentic gifts of generosity and calculated sales hooks."
  ], [
    ("The debt of gratitude is universal", "Human cultures universally enforce the moral obligation to return favors and gifts."),
    ("Uninvited gifts still trigger compliance", "Even unwanted favors create an uncomfortable psychological pressure to repay."),
    ("Reciprocal concessions yield agreement", "Backing down from an extreme request looks like a compromise that invites a return concession.")
  ], ("There is no human society that does not subscribe to the sacred rule of reciprocation.", "rabbit_take"), [
    "Offer helpful assistance or useful introductions to colleagues without asking for anything in return.",
    "Be cautious when accepting lavish free meals or gifts from vendors before negotiating contracts.",
    "When someone concedes a point during a debate, offer a graceful concession in return to foster goodwill."
  ], [("predictably-irrational", 3, "Reciprocity is the foundational currency of social norms that hold human groups together.")]),
  ch(3, "Commitment and Consistency", "Once we make a choice or take a stand, we face immense personal and interpersonal pressure to stay consistent.", [
    "Human beings possess an obsessive desire to be, and to appear, consistent with what they have already done.",
    "Once you take a public stand, you encounter powerful psychological pressure to align future conduct with that commitment.",
    "In a famous study, researchers asked homeowners to put a massive, ugly billboard saying 'Drive Carefully' on their lawns.",
    "Most homeowners refused, but eighty-three percent agreed if they had signed a tiny petition two weeks earlier.",
    "The foot-in-the-door technique uses tiny initial commitments to reshape a person's self-concept into that of an active citizen.",
    "Writing commitments down produces a permanent, tangible anchor that resists subsequent doubts.",
    "Chinese prisoner-of-war camps used written essays on minor flaws in capitalism to gradually convert American soldiers.",
    "Beware of agreeing to small, seemingly harmless commitments that subtly alter your identity and trajectory."
  ], [
    ("Consistency is viewed as personal integrity", "Society values steadfast consistency and despises indecisive, hypocritical flip-flopping."),
    ("Small commitments reshape identity", "Agreeing to minor requests changes how you see yourself, opening the door to massive future compliance."),
    ("Written commitments endure", "The physical act of writing creates a durable psychological anchor that binds future behavior.")
  ], ("The desire for consistency is a central motivator of our behavior, often driving us against our best interests.", "rabbit_take"), [
    "Write down your personal study goals and sign them to create a binding psychological contract.",
    "Ask prospective project partners for a tiny five-minute commitment before offering larger responsibilities.",
    "Watch out for car salesmen who offer a great price, get you emotionally committed, then reveal hidden fees."
  ], [("atomic-habits", 2, "Identity votes rely on the commitment-consistency principle to solidify new habits.")]),
  ch(4, "Social Proof: Truths Are Us", "We view a behavior as more correct in a given situation to the degree that we see others doing it.", [
    "When people are uncertain about what to do, they look outside themselves to the actions of others to guide judgment.",
    "Television sitcom producers use canned laughter tracks because studies prove it makes audiences laugh longer and rate shows funnier.",
    "Even when we know the laughter is fake and mechanical, the subconscious signal of social approval still works.",
    "Social proof operates with maximum potency under two conditions: uncertainty and similarity.",
    "When a situation is ambiguous, pluralistic ignorance occurs: everyone looks at everyone else, and nobody acts.",
    "Catherine Genovese was murdered in New York while thirty-eight neighbors watched from windows without calling the police.",
    "Each neighbor saw others watching quietly and concluded that the situation must not be an emergency.",
    "If you need help in an emergency, point directly at one specific person, eliminate uncertainty, and assign them the task."
  ], [
    ("Uncertainty drives imitation", "When people are confused, they look to the crowd rather than conducting independent audits."),
    ("Pluralistic ignorance paralyzes groups", "In ambiguous emergencies, passive crowds convince each onlooker that no action is needed."),
    ("Similarity magnifies social proof", "We are far more likely to follow the lead of peers who look, talk, and live like us.")
  ], ("Since ninety-five percent of the people are imitators, people are persuaded more by the actions of others.", "rabbit_take"), [
    "In an emergency, point to one individual in the crowd and say: 'You in the blue jacket, call the police right now.'",
    "Show testimonials from peers of similar age and background when pitching ideas to prospective team members.",
    "Remember that viral online trends reflect crowd conformity far more than genuine quality or truth."
  ], [("the-48-laws-of-power", 5, "Social demonstration and visible crowd examples persuade far deeper than verbal debate.")]),
  ch(5, "Liking: The Friendly Thief", "We vastly prefer to say yes to requests from people we know, like, and find attractive.", [
    "Compliance professionals know that building interpersonal affinity is the quickest way to disarm resistance.",
    "Tupperware parties generated billions in sales by having neighborhood hostesses invite friends into their living rooms.",
    "Guests bought products not because they loved plastic containers, but because they loved their friend who was hosting.",
    "Several factors reliably trigger liking: physical attractiveness, similarity, compliments, and cooperative contact.",
    "Good-looking people benefit from a halo effect where others automatically perceive them as smarter and kinder.",
    "We naturally like people who share our background, dress style, hobbies, and hometown.",
    "Automobile salesman Joe Girard sent thirteen thousand greeting cards every month saying simply: 'I like you.'",
    "He became the greatest car salesman in history because people loved buying from someone who praised them."
  ], [
    ("The halo effect distorts evaluation", "A single positive trait like charm or attractiveness biases overall judgment of character."),
    ("Similarity breeds mutual comfort", "We open up to people who reflect our vocabulary, interests, and style."),
    ("Compliments unlock doors", "Even transparent praise produces positive feelings that soften commercial resistance.")
  ], ("We rarely buy from people we dislike. Affection is the invisible lubricant of human compliance.", "rabbit_take"), [
    "Find genuine common ground—such as a shared favorite author or sports team—before discussing business.",
    "Offer sincere, specific compliments to team members; everyone hungers for honest appreciation.",
    "Beware of salesmen who pretend to be your best friend; separate the person from the contractual terms."
  ], [("surrounded-by-idiots", 3, "Matching communication styles and building genuine warmth unlocks spontaneous cooperation.")]),
  ch(6, "Scarcity: The Rule of the Few", "Opportunities seem infinitely more valuable to us when their availability is strictly limited.", [
    "The scarcity principle states that people assign higher value to things that are rare or dwindling in availability.",
    "Nearly everyone has felt the sudden urgency to buy when an airline website says: 'Only 2 seats left at this price!'",
    "Psychological reactance explains that whenever free choice is restricted, the need to retain our freedoms makes us desire them more.",
    "When Miami banned phosphate laundry detergents, citizens smuggled soap and rated phosphate cleaners as gentler and superior.",
    "Scarcity is most powerful when it is newly experienced: newly restricted freedoms provoke far more rebellion than constant deprivation.",
    "Furthermore, we desire scarce items most intensely when we are in active competition with other rivals for them.",
    "Real estate agents use multiple-bidder open houses to whip prospective buyers into an irrational feeding frenzy.",
    "Whenever you feel a sudden surge of physical desire driven by a closing deadline, recognize that scarcity is manipulating your pulse."
  ], [
    ("Scarcity inflates perceived quality", "The threat of potential loss makes items feel precious regardless of utility."),
    ("Psychological reactance fuels desire", "Restricting access to an idea or product makes people crave it with heightened passion."),
    ("Competition supercharges scarcity", "Competing directly with rivals for a limited resource triggers primal territory instincts.")
  ], ("The way to love anything is to realize that it might be lost.", "rabbit_take"), [
    "Never bid in auctions under emotional excitement; establish your maximum walk-away number in advance.",
    "Ignore countdown timers on retail websites designed purely to trigger manufactured urgency.",
    "Recognize that censored books or forbidden topics become instantly more appealing to human curiosity."
  ], [("the-psychology-of-money", 3, "Resisting fabricated market scarcity protects you from speculative bubbles and regret.")])
])

# 11. The Laws of Human Nature (Robert Greene)
add_b("the-laws-of-human-nature", "The Laws of Human Nature", "Robert Greene", "https://covers.openlibrary.org/b/id/10543678-M.jpg", [
  ch(1, "Master Your Emotional Self: The Law of Irrationality", "You believe you are rational, but your decisions are constantly steered by unconscious emotions.", [
    "Most human beings operate under the continuous delusion that their opinions are guided by cold logic and intellect.",
    "In reality, our brains are governed by a deep, ancient emotional limbic system that reacts before reason wakes up.",
    "Our conscious minds are master rationalizers that invent clever intellectual justifications for raw emotional desires.",
    "Pericles understood that Athenian democracy was vulnerable to emotional panic, demagogues, and war fever.",
    "He trained himself to never make decisions while feeling angry, euphoric, or fearful.",
    "He withdrew into quiet solitude to let emotional floods subside before examining the cold strategic facts.",
    "True rationality is not an innate gift; it is a hard-won psychological discipline requiring relentless self-audit.",
    "Observe your emotional triggers with detached curiosity rather than treating feelings as final truths."
  ], [
    ("Rationality requires deliberate training", "Nobody is born purely rational; intellect is an acquired muscle built by checking impulses."),
    ("Emotions masquerade as logic", "We invent sophisticated intellectual arguments to defend positions chosen by gut fear or pride."),
    ("The pause between stimulus and response", "Withdrawing from immediate agitation allows reason to regain control of strategy.")
  ], ("Rationality is the ability to counteract emotional reactions and think with sober clarity.", "rabbit_take"), [
    "Never send angry emails or texts immediately; draft them, close the app, and review them the next morning.",
    "Ask yourself which underlying emotion—envy, fear, or vanity—is truly driving your latest impulse.",
    "Deliberately research the strongest arguments against your cherished political beliefs."
  ], [("thinking-fast-and-slow", 1, "System 1 emotional impulses constantly trick System 2 into manufacturing false justifications.")]),
  ch(2, "Transform Self-Love into Empathy: The Law of Narcissism", "We are all self-absorbed; the highest human art is turning that attention outward through deep empathy.", [
    "Human beings fall along a spectrum of narcissism: from deep, toxic absorption to healthy, outward-facing empathy.",
    "Deep narcissists view other people merely as instruments, mirrors, or obstacles to their personal gratification.",
    "They possess fragile egos that shatter at minor criticism, triggering vindictive rage and theatrical victimhood.",
    "Healthy narcissists recognize their self-absorption and deliberately train their attention to focus on other people.",
    "Analytic empathy involves stepping into another person's emotional shoes and understanding their childhood background.",
    "Visceral empathy involves feeling their emotions in real time through attuned listening and observing body language.",
    "When you make people feel truly seen and understood, you unlock the most magnetic power in human society.",
    "Shift your focus from trying to impress people to being deeply fascinated by who they are."
  ], [
    ("Move from self-obsession to curiosity", "Redirecting inward mental chatter toward studying others disarms social anxiety."),
    ("Beware of deep narcissists", "Spot the warning signs: excessive sensitivity to critique, entitlement, and transactional friendships."),
    ("Empathy is a superpower", "People will forgive almost any error if they feel you genuinely respect their inner reality.")
  ], ("The highest form of intelligence is the ability to step inside the reality of another human being.", "rabbit_take"), [
    "During your next conversation, focus entirely on understanding the speaker without planning your response.",
    "Study the childhood origins of colleagues' insecurities to replace irritation with compassionate insight.",
    "Notice when your ego feels bruised in meetings and consciously pivot your thoughts toward helping the team."
  ], [("surrounded-by-idiots", 1, "Empathy requires understanding that people process reality through entirely different psychological temperaments.")]),
  ch(3, "See Through People's Masks: The Law of Role-Playing", "People present polished public personas; true character is revealed through micro-expressions and leaks.", [
    "Every individual wears a carefully constructed social mask designed to project competence, warmth, and morality.",
    "If you accept people's public presentations at face value, you will be perpetually deceived and blindsided.",
    "Human nature cannot completely conceal its authentic emotional states; micro-expressions always leak through.",
    "Observe nonverbal cues: forced smiles do not engage the muscles around the eyes; crossed legs betray hidden tension.",
    "Notice vocal inflections, sudden changes in tone, and how people treat waitstaff or junior employees.",
    "Master the craft of observing without staring; develop peripheral social radar that absorbs clues quietly.",
    "Furthermore, become conscious of your own public mask: project calm confidence and avoid leaking anxious insecurity.",
    "Seeing through social theater protects you from predatory manipulators while keeping your own position secure."
  ], [
    ("Social masks conceal raw reality", "Public behavior is theatrical performance; true motives emerge in unguarded moments."),
    ("Nonverbal leaks tell the truth", "Micro-expressions, postural shifts, and tone changes betray hidden envy or hostility."),
    ("Judge people by treatment of the weak", "How someone treats powerless subordinates reveals their authentic ethical core.")
  ], ("Learn to see through the masks people wear, and you will never be surprised by their actions.", "rabbit_take"), [
    "Pay attention to how a prospective friend or business partner talks about former colleagues.",
    "Notice whether someone's smile reaches their eyes or remains a frozen social grimace.",
    "Develop a calm, pleasant public persona that keeps your private vulnerabilities safely shielded."
  ], [("the-48-laws-of-power", 2, "Concealing intentions depends on presenting a plausible, polished social mask that disarms suspicion.")]),
  ch(4, "Determine Strength of Character: The Law of Compulsive Behavior", "People are prisoners of their childhood patterns; character is destiny, repeated over and over.", [
    "When evaluating colleagues, partners, or leaders, we are frequently blinded by charisma, wit, or intelligence.",
    "These superficial traits tell you nothing about a person's underlying character.",
    "Character is the deeply ingrained behavioral habits formed in early childhood that dictate responses to stress.",
    "A person of weak character collapses under pressure, blames others for mistakes, and betrays allies when panicked.",
    "A person of strong character takes accountability, adapts gracefully to sudden chaos, and remains loyal.",
    "People do not change their fundamental character; they merely repeat the same patterns in new environments.",
    "Do not assume that someone who cheated or lied in their last three jobs will treat you differently.",
    "Prioritize strength of character above all other traits in friendship, hiring, and romantic partnerships."
  ], [
    ("Character outweighs talent", "Brilliance without integrity creates brilliant disasters; character determines durability under fire."),
    ("Patterns repeat compulsively", "Past behavior in difficult seasons is the most reliable predictor of future conduct."),
    ("Examine responses to stress", "Watch how someone reacts when plans fail: do they take ownership or point fingers?")
  ], ("Character is destiny. What people have done in the past, they will inevitably do again.", "rabbit_take"), [
    "Check references thoroughly and inquire specifically about how candidates handled stressful project failures.",
    "Do not ignore early red flags in dating; small signs of entitlement or dishonesty always expand later.",
    "Build personal character by honoring commitments even when breaking them would be convenient and private."
  ], [("atomic-habits", 2, "Habits are the tangible proof that builds and validates your enduring personal character.")]),
  ch(5, "Become an Elusive Object of Desire: The Law of Covetousness", "We crave what is absent and elusive; presence tires, while mystery and distance ignite desire.", [
    "Human beings are perpetually haunted by the illusion that the grass is greener on the other side.",
    "The moment an object, person, or opportunity becomes too readily available, its value plummets in our estimation.",
    "Presence creates comfortable familiarity, but absence stimulates the imagination and inflames desire.",
    "To become an elusive object of desire, do not suffocate relationships with total, cloying availability.",
    "Maintain an air of mystery: keep private boundaries, cultivate independent pursuits, and do not reveal everything.",
    "In commerce, luxury brands create artificial scarcity and deliberate waiting lists to stoke obsessive demand.",
    "If you give people everything they ask for, they will take you for granted and eventually look elsewhere.",
    "Strategic absence combined with genuine excellence creates an irresistible aura that draws others toward you."
  ], [
    ("Familiarity breeds complacency", "Being constantly available cheapens your perceived worth in social and romantic arenas."),
    ("Absence feeds the imagination", "Distance forces others to wonder about you, projecting their own desires onto your silence."),
    ("Cultivate independent mystery", "Having private passions outside a relationship makes your presence precious and exciting.")
  ], ("Create an aura of mystery. People do not desire what is always present and completely understood.", "rabbit_take"), [
    "Do not reply to non-urgent texts within three seconds; let your time reflect focused, active priorities.",
    "Keep some accomplishments and personal stories private until the right moment arises organically.",
    "In business proposals, showcase exclusivity and limited partnership slots to accelerate client commitments."
  ], [("influence-psychology-of-persuasion", 6, "Scarcity of time and availability triggers psychological reactance and deepens desire.")]),
  ch(6, "Elevate Your Perspective: The Law of Shortsightedness", "Most people react to immediate fires; true power belongs to those who view the long horizon.", [
    "The default human tendency is to be entirely consumed by the immediate drama happening right in front of us.",
    "We panic over today's falling stock price, gossip about today's minor office feud, and react to every headline.",
    "This shortsightedness blinds people to slow-moving tectonic shifts that will reshape their entire industry.",
    "Elevate your perspective: zoom out to historical altitude and examine the five-to-ten-year horizon.",
    "Distinguish between temporary passing noise and enduring fundamental trends.",
    "Do not sacrifice long-term strategic positioning for minor short-term tactical victories.",
    "When facing sudden crises, step back and ask how this moment will appear ten years from now.",
    "The long view brings immense emotional composure and positions you miles ahead of the reactive crowd."
  ], [
    ("Zoom out from daily noise", "Most urgent daily crises are completely forgotten within three months; focus on enduring assets."),
    ("Anticipate slow tectonic shifts", "Position your skills for where technology and culture will stand a decade from now."),
    ("Long horizons breed calmness", "Viewing setbacks through a ten-year lens dissolves immediate panic and restores perspective.")
  ], ("Elevate your gaze above the immediate battlefield, and you will see the moves that win the war.", "rabbit_take"), [
    "When a project hits a snag, ask: 'Will this matter in five years?' If not, resolve it without emotional drama.",
    "Invest learning hours in foundational principles—math, psychology, clear writing—that never expire.",
    "Ignore daily market fluctuations and focus on thirty-year compounding in your investments."
  ], [("the-psychology-of-money", 4, "Long-term compounding requires elevating your horizon above short-term market noise.")])
])

# 12. Nudge (Richard Thaler & Cass Sunstein)
add_b("nudge", "Nudge: Improving Decisions", "Richard H. Thaler & Cass R. Sunstein", "https://covers.openlibrary.org/b/id/10543680-M.jpg", [
  ch(1, "Biases and Blunders", "Humans are not rational calculators; we need thoughtful choice architecture to help us thrive.", [
    "Economists traditionally assumed that humans behave like 'Econs': perfectly rational, emotionless calculating machines.",
    "In reality, we are 'Humans': prone to inertia, biased by framing, forgetful, and easily overwhelmed by choices.",
    "Because human cognition relies on mental heuristics, the way choices are presented dramatically steers decisions.",
    "Choice architecture is the practice of designing environments to influence people's choices without forbidding any option.",
    "A school cafeteria director rearranged food displays: putting fresh fruits and vegetables at eye level.",
    "Consumption of healthy food surged by twenty-five percent without banning junk food or lecturing students.",
    "A nudge is any aspect of the choice architecture that alters people's behavior in a predictable way without coercion.",
    "Recognize that there is no such thing as a neutral design; someone is always setting the defaults."
  ], [
    ("Humans are not Econs", "Real people suffer from procrastination, cognitive bias, and decision fatigue."),
    ("No design is neutral", "How choices are arranged on a menu, form, or website inevitably guides human selections."),
    ("Nudges preserve freedom", "A legitimate nudge makes the better choice easier while leaving every alternative open.")
  ], ("By knowing how people think, we can make it easier for them to choose what is best for their lives.", "rabbit_take"), [
    "Place fresh fruit and water at eye level on your kitchen counter to nudge healthy snacking.",
    "Unsubscribe from shopping promo emails so spending impulse triggers never enter your inbox.",
    "Position your alarm clock across the room so turning it off requires standing up on your feet."
  ], [("atomic-habits", 3, "Designing physical environments with prominent visual cues is the ultimate personal nudge.")]),
  ch(2, "The Power of Defaults", "The single most powerful nudge on Earth is the default option that occurs when you do nothing.", [
    "Human beings possess an immense status quo bias: we tend to stick with whatever option is already selected.",
    "In European organ donation, countries that require citizens to opt in have donation rates around fifteen percent.",
    "Countries with presumed consent—where you are automatically an organ donor unless you opt out—have ninety-nine percent rates.",
    "Citizens did not have radically different moral souls; they simply accepted the default checkmark on the form.",
    "Software companies exploit defaults by pre-checking boxes for automatic annual renewals and marketing emails.",
    "You can harness the power of defaults to transform your personal finances and health.",
    "Automate your savings, automate your retirement contributions, and set default app limits on your phone.",
    "When the constructive path is the default path, human inertia works in your favor rather than against you."
  ], [
    ("Default options carry immense gravity", "Most people take the path of least resistance and accept whatever is pre-selected."),
    ("Harness inertia for good", "Setting automatic positive defaults ensures progress even during seasons of low motivation."),
    ("Audit your digital defaults", "Review app permissions and subscription renewals to ensure companies are not exploiting your inertia.")
  ], ("If you want to encourage someone to do something, make it easy. Above all, make it the default.", "rabbit_take"), [
    "Set up automatic monthly transfers to your investment account on the day your paycheck arrives.",
    "Use screen-time settings that automatically lock distracting entertainment apps after thirty minutes.",
    "Default to drinking water with every meal unless celebrating a special occasion."
  ], [("the-psychology-of-money", 5, "Automated savings create an untouchable financial buffer without relying on daily willpower.")]),
  ch(3, "Following the Herd: Social Nudges", "Informing people about what their neighbors are doing is more powerful than moral lectures.", [
    "Humans are social animals who desperately want to fit in with their local tribe's behavioral norms.",
    "Hotels tried to encourage towel reuse with signs about saving the environment, achieving moderate compliance.",
    "When they changed signs to say: 'Seventy-five percent of guests who stay in this room reuse their towels,' reuse surged.",
    "People did not care about abstract planetary statistics; they cared about matching the norms of their peers.",
    "Utility companies printed energy bills comparing a homeowner's electricity consumption with efficient neighbors.",
    "Homeowners who consumed more than their neighbors immediately reduced electricity use without any financial penalty.",
    "Social nudges work because human beings use peer consensus as a shortcut for what is sensible and safe.",
    "Surround yourself with groups whose baseline conduct mirrors the person you want to become."
  ], [
    ("Peer comparison motivates change", "Seeing that neighbors or classmates outperform you triggers an immediate urge to align."),
    ("Abstract appeals fail", "Lectures about duty are far less effective than concrete data showing popular conformity."),
    ("Harness positive social proof", "Highlighting the high percentage of people doing the right thing pulls the remainder along.")
  ], ("If you want people to adopt a behavior, tell them that their peers are already doing it.", "rabbit_take"), [
    "Form a study group where daily check-ins make finishing assignments the accepted social norm.",
    "Track your reading alongside friends on book platforms where seeing peers finish chapters inspires you.",
    "Notice when peer pressure nudges you toward bad habits; consciously choose healthy tribes."
  ], [("influence-psychology-of-persuasion", 4, "Social proof is the engine that drives social nudges across every human culture.")]),
  ch(4, "When Do We Need a Nudge?", "We need nudges most when choices have delayed consequences, rare frequency, and ambiguous feedback.", [
    "Humans do not need nudges for activities they perform daily with immediate feedback, like eating favorite foods.",
    "We need nudges desperately in domains where four specific conditions create cognitive vulnerability.",
    "First, choices with benefits now and costs later: cigarettes, junk food, and excessive credit card spending.",
    "Second, choices that are rare and difficult: choosing a college, buying a home, or selecting a retirement plan.",
    "Third, choices where feedback is ambiguous or nonexistent: you do not learn if your investment plan works until retirement.",
    "Fourth, choices where the connection between the decision and the real-world experience is opaque.",
    "In these tricky domains, human intuition fails and behavioral blunders become standard.",
    "Construct personal nudges around high-stakes, low-frequency choices to protect your future self."
  ], [
    ("Delayed consequences invite disaster", "When pleasure is immediate and pain is distant, human willpower almost always collapses."),
    ("Rare choices lack practice", "Because you only choose a mortgage or career a few times, experience cannot guide you."),
    ("Build structural guardrails", "Consult checklists and trusted mentors for high-stakes decisions with opaque feedback.")
  ], ("The best nudges help people navigate choices whose consequences will not be felt for decades.", "rabbit_take"), [
    "Create a written checklist for major life choices like signing leases or accepting job offers.",
    "Set up strict barriers against impulse purchases over one hundred dollars: enforce a mandatory forty-eight-hour wait.",
    "Consult older mentors who have lived through the long-term consequences of career pathways."
  ], [("thinking-fast-and-slow", 6, "The Experiencing Self seeks instant gratification; nudges protect the Remembering Self's future.")]),
  ch(5, "Choice Architecture in Action: RECAP", "Complex pricing and opaque fees must be countered by radical transparency and standardized metrics.", [
    "Modern consumer life is filled with complex, bewildering pricing structures designed to confuse.",
    "Credit card companies, mobile carriers, and mortgages bury crucial fees in microscopic legal fine print.",
    "Thaler and Sunstein propose a universal regulatory nudge called RECAP: Record, Evaluate, and Compare Alternative Prices.",
    "Under RECAP, companies must provide consumers with a machine-readable record of all fees paid over the past year.",
    "Independent comparison websites could then import this file and instantly show the cheapest alternative provider.",
    "Choice architecture should empower consumers with clear, actionable comparisons rather than information overload.",
    "When data is standardized and clear, market competition drives prices down and protects the public.",
    "Demand clear, transparent summaries in your personal contracts and refuse to do business with opaque vendors."
  ], [
    ("Complexity is often predatory", "Opaque fee structures are deliberately engineered to prevent consumers from comparing true costs."),
    ("Standardized data restores agency", "Machine-readable fee records allow technology to do the comparison shopping for you."),
    ("Transparency breeds honest competition", "When consumers can clearly see total costs, predatory pricing models collapse.")
  ], ("Good choice architecture does not restrict options; it illuminates true costs with radiant clarity.", "rabbit_take"), [
    "Review your bank statements annually and sum up all recurring subscriptions and hidden maintenance fees.",
    "Use comparison calculators to evaluate total loan costs rather than looking only at monthly minimum payments.",
    "Ask service providers directly for an itemized fee breakdown before agreeing to contracts."
  ], [("predictably-irrational", 1, "Comparative clarity eliminates the manipulative decoys used by sellers to distort value.")]),
  ch(6, "Saving More Tomorrow", "Overcoming loss aversion by committing to save a portion of your future pay raises today.", [
    "Most workers know they should save more for retirement, but good intentions collapse when facing present budgets.",
    "Asking people to cut current spending triggers acute loss aversion: it feels like a painful lifestyle downgrade.",
    "Thaler and Benartzi invented the Save More Tomorrow program to bypass this psychological barrier.",
    "Workers are asked to commit today to increasing their savings rate in the future, whenever they receive a pay raise.",
    "Because the commitment takes effect in the future, hyperbolic discounting makes the sacrifice feel painless today.",
    "When the pay raise arrives, the savings rate increases automatically before the worker ever sees the cash in their account.",
    "Workers never experience a drop in take-home pay, completely avoiding loss aversion.",
    "In pilot programs, participants quadrupled their annual savings rate within forty months.",
    "Tie future commitments to future windfalls, and your wealth will multiply without painful deprivation."
  ], [
    ("Bypass present loss aversion", "Committing future raises to savings prevents the pain of reducing current take-home spending."),
    ("Leverage hyperbolic discounting", "Future sacrifices feel emotionally manageable today; lock in the commitment before tomorrow arrives."),
    ("Automatic escalation compounds wealth", "Synchronizing savings hikes with career promotions builds massive net worth effortlessly.")
  ], ("By tying savings increases to future raises, we make financial discipline feel completely painless.", "rabbit_take"), [
    "Commit right now to directing fifty percent of your next job promotion or salary raise straight to savings.",
    "When a debt is fully paid off, immediately divert that monthly payment into investments rather than lifestyle inflation.",
    "Set an annual calendar reminder to review and increase your automatic investment contributions."
  ], [("the-psychology-of-money", 4, "Compounding thrives when future savings escalations are locked in before lifestyle creep begins.")])
])

print(f"gen_hero_mind.py successfully built all {len(books)} books!")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)

print(f"Saved {len(books)} Human Mind hero books to {OUT_PATH}")
