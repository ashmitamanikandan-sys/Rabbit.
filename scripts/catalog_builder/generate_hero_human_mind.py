# -*- coding: utf-8 -*-
"""
generate_hero_human_mind.py
Generates the 12 hero books for 'The Human Mind' genre.
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

books = [
  # 1. Atomic Habits (James Clear)
  {
    "id": "atomic-habits",
    "title": "Atomic Habits",
    "author": "James Clear",
    "genre": "The Human Mind",
    "cover_url": "https://covers.openlibrary.org/b/id/12843460-M.jpg",
    "public_domain": False,
    "fiction": False,
    "chapters": [
      {
        "n": 1,
        "title": "The Surprising Power of Atomic Habits",
        "hook": "Why tiny 1% adjustments compound into life-defining transformations over time.",
        "spark": "We routinely convince ourselves that massive success requires massive action.\nWhether chasing academic honors, fitness, or career breakthroughs, we demand instant leaps.\nReal human transformation behaves like financial compound interest rather than a lottery win.\nIf you become just one percent better each day for one year, you end thirty-seven times ahead.\nIf you drift one percent worse each day, your capability deteriorates nearly to zero.\nWhat feels completely unnoticeable on any single Tuesday accumulates into an immense gap over five years.\nYour current outcomes are simply lagging measures of your daily habits.\nYour net worth reflects your financial habits, and your knowledge reflects your reading habits.\nYou do not need an overwhelming reinvention; you need compounding micro-improvements.",
        "key_ideas": [
          {"idea": "Small changes compound exponentially", "why": "A 1% daily upgrade multiplies your baseline ability thirty-seven times over twelve months."},
          {"idea": "Systems beat outcome targets", "why": "Winners and losers share identical goals; the differing systems alone produce the divergent result."},
          {"idea": "Outcomes lag behind actions", "why": "Significant results take time to appear, requiring patience through early plateaus."}
        ],
        "line": {"text": "You do not rise to the level of your goals; you fall to the level of your systems.", "type": "rabbit_take"},
        "in_your_life": [
          "Placing your phone in another room while doing homework stops dozens of accidental distractions.",
          "Reading five pages right after morning coffee ensures you finish twenty books every year.",
          "Laying out workout clothes before sleeping removes morning friction before your brain can negotiate."
        ],
        "connects_to": [{"book_id": "thinking-fast-and-slow", "chapter": 1, "reason": "Automatic habits rely on System 1 mental routines to bypass cognitive fatigue."}],
        "spoiler_level": "none"
      },
      {
        "n": 2,
        "title": "How Your Habits Shape Your Identity",
        "hook": "True change is not about what you want to achieve, but who you wish to become.",
        "spark": "Most people try to change their lives by focusing exclusively on what they want to achieve.\nThis leads to outcome-based habits: I want to run a marathon, or I want to earn an A.\nThe deeper, permanent alternative is identity-based change.\nThe word identity originates from the Latin essentitas, meaning being, and identidem, meaning repeatedly.\nYour identity is literally your repeated beingness, validated by the proof of your daily conduct.\nEvery action you take is a small vote for the type of human being you are becoming.\nNo single vote changes your entire self-image, but as the tally builds, your evidence becomes undeniable.\nWhen you refuse to skip practice, you prove to yourself that you are disciplined.\nWhen you write one thoughtful paragraph, you provide evidence that you are a writer.",
        "key_ideas": [
          {"idea": "Beliefs drive repeated behaviors", "why": "Behind every routine sits a foundational belief about who you are and what you deserve."},
          {"idea": "Every habit is an identity vote", "why": "Small actions furnish tangible evidence that reshapes how your subconscious perceives your capability."},
          {"idea": "Shift questions from goals to identity", "why": "Instead of asking what you want to achieve, ask who you wish to become."}
        ],
        "line": {"text": "The goal is not to read a book; the goal is to become a reader.", "type": "rabbit_take"},
        "in_your_life": [
          "When tempted to procrastinate, ask yourself what an organized person would do right now.",
          "Declaring 'I am not a smoker' works far better than saying 'I am trying to quit smoking'.",
          "Putting away your plate immediately after dinner proves to yourself that you run an orderly life."
        ],
        "connects_to": [{"book_id": "deep-work", "chapter": 1, "reason": "Protecting deep focus requires seeing yourself as someone who values depth over cheap noise."}],
        "spoiler_level": "none"
      },
      {
        "n": 3,
        "title": "The First Law: Make It Obvious",
        "hook": "Design your physical environment so positive cues stare you straight in the face.",
        "spark": "The human brain is an anticipation machine, constantly scanning surroundings for behavioral cues.\nMost of our daily actions are triggered not by conscious will, but by visual prominence.\nIf you want a habit to become a normal part of your day, make the cue obvious in your space.\nDo not hide a book on a crowded shelf if you intend to read it before sleep.\nPlace it directly on your pillow when you make the bed in the morning.\nImplementation intentions create clear triggers by stating: I will do X at time Y in location Z.\nEnvironment design is the secret weapon because willpower is an exhaustible, fickle resource.\nPeople with great self-control rarely possess heroic willpower; they simply design calmer spaces.",
        "key_ideas": [
          {"idea": "Visual cues dictate default choices", "why": "Human vision accounts for more sensory cortex than any other sense, shaping impulses automatically."},
          {"idea": "Implementation intentions stop hesitation", "why": "Specifying the exact time and location removes the mental friction of choosing when to start."},
          {"idea": "Redesign physical surroundings", "why": "It is far easier to avoid temptation when the negative cue is entirely removed from sight."}
        ],
        "line": {"text": "Be the architect of your physical environment, not merely the consumer of it.", "type": "rabbit_take"},
        "in_your_life": [
          "Fill a large water flask and leave it on your desk so staying hydrated requires zero thought.",
          "Keep guitar picks right next to the sofa if you want to practice fifteen minutes daily.",
          "Charge your phone in the kitchen overnight so morning scrolling never enters your bedroom."
        ],
        "connects_to": [{"book_id": "nudge", "chapter": 1, "reason": "Choice architecture shapes decisions through subtle environmental defaults."}],
        "spoiler_level": "none"
      },
      {
        "n": 4,
        "title": "The Second Law: Make It Attractive",
        "hook": "Pair things you need to do with things you genuinely look forward to enjoying.",
        "spark": "Dopamine is the neurotransmitter of desire, anticipation, and pursuit.\nOur brains experience a sharper spike of dopamine anticipating a reward than actually receiving it.\nBy harnessing temptation bundling, you link an action you need to do with an action you want to do.\nYou can say: after I finish ten practice math problems, I get to watch one episode of my show.\nHuman beings also absorb habits from the social tribes they spend their hours around.\nWe imitate the habits of three groups: the close family and friends, the many tribe, and the powerful.\nJoin groups where your desired behavior is the normal daily baseline for everyone.\nWhen surrounding peers read daily or run weekly, positive effort ceases to feel like sacrifice.",
        "key_ideas": [
          {"idea": "Anticipation drives dopamine spikes", "why": "Desire for future pleasure motivates initial effort more strongly than past fulfillment."},
          {"idea": "Temptation bundling bridges reluctance", "why": "Anchoring chores to anticipated rewards creates reliable behavioral momentum."},
          {"idea": "Social culture normalizes effort", "why": "Surrounding yourself with motivated peers transforms tough disciplines into standard habits."}
        ],
        "line": {"text": "Join a culture where your desired behavior is already the normal standard.", "type": "rabbit_take"},
        "in_your_life": [
          "Only listen to your favorite podcast while doing the dishes or folding laundry.",
          "Study in quiet libraries where everyone around you is already focused on coursework.",
          "Form a small reading circle where discussing one chapter each Sunday is celebrated."
        ],
        "connects_to": [{"book_id": "the-psychology-of-money", "chapter": 2, "reason": "Social comparison dictates spending habits far more than pure financial math."}],
        "spoiler_level": "none"
      },
      {
        "n": 5,
        "title": "The Third Law: Make It Easy",
        "hook": "Reduce the friction of good routines and scale them down to two quick minutes.",
        "spark": "Human energy follows the path of least resistance naturally and without apology.\nWhen choosing between two similar choices, people invariably select the one requiring less effort.\nInstead of trying to force massive motivation, strategically reduce the friction of the right path.\nUse the Two-Minute Rule: when you begin a new habit, it should take less than two minutes to do.\nRead one page, do three push-ups, or open your class notebook to the title page.\nThe key is not accomplishing the entire marathon on day one; it is mastering the art of showing up.\nA habit must be established before it can be improved or optimized.\nYou cannot refine a routine that does not exist in the first place.\nStandardize your beginning, and let momentum carry you through the remainder.",
        "key_ideas": [
          {"idea": "Friction determines compliance", "why": "Every extra obstacle between you and an action lowers the likelihood of following through."},
          {"idea": "The Two-Minute Rule establishes routines", "why": "Shrinking a new routine down to two minutes overcomes the dread of beginning."},
          {"idea": "Master the art of showing up", "why": "Consistency at a minimal baseline matters more than sporadic, heroic efforts."}
        ],
        "line": {"text": "A habit must be established before it can be improved.", "type": "rabbit_take"},
        "in_your_life": [
          "Open your assignment document and write one sentence before walking away; you will usually keep writing.",
          "Put running shoes directly by the front door so going for a jog requires zero prep.",
          "Place fruit in an open bowl on the table instead of tucked away inside a refrigerator drawer."
        ],
        "connects_to": [{"book_id": "the-power-of-habit", "chapter": 1, "reason": "Habit loops depend on simple routines triggered by unmistakable cues."}],
        "spoiler_level": "none"
      },
      {
        "n": 6,
        "title": "The Fourth Law: Make It Satisfying",
        "hook": "What is immediately rewarded gets repeated; what is immediately punished gets avoided.",
        "spark": "Our brains evolved in an immediate-return environment on prehistoric savannahs.\nIf you tracked food or found shelter, the survival payoff was instantaneous.\nModern society, however, operates almost entirely on delayed-return horizons.\nWorking hard today pays off in salary next month or graduation in four years.\nTo make a good habit stick, attach a tiny immediate gratification to the completion of the action.\nVisual trackers, such as crossing off dates on a wall calendar, provide immediate visual proof of victory.\nDon't break the chain becomes a psychological asset you protect with pride.\nWhen you experience immediate evidence of your discipline, your brain logs the routine as a win.",
        "key_ideas": [
          {"idea": "Immediate feedback seals the loop", "why": "Immediate pleasure signals to the nervous system that an action is worth performing again."},
          {"idea": "Visual tracking creates protective pride", "why": "Seeing an unbroken streak of checkmarks produces a tangible reason not to quit today."},
          {"idea": "Never miss twice", "why": "Missing once is an accident; missing twice is the start of an unintended new habit."}
        ],
        "line": {"text": "Missing once is an accident. Missing twice is the start of a new habit.", "type": "rabbit_take"},
        "in_your_life": [
          "Move a marble into a glass jar every time you complete a focused forty-minute study block.",
          "Cross off days on a paper calendar with a bold marker to keep your reading streak alive.",
          "If sickness interrupts your routine one day, resume the very next morning without guilt."
        ],
        "connects_to": [{"book_id": "flow", "chapter": 1, "reason": "Flow requires clear rules and immediate feedback so the mind stays locked on the task."}],
        "spoiler_level": "none"
      }
    ]
  },

  # 2. Thinking, Fast and Slow (Daniel Kahneman)
  {
    "id": "thinking-fast-and-slow",
    "title": "Thinking, Fast and Slow",
    "author": "Daniel Kahneman",
    "genre": "The Human Mind",
    "cover_url": "https://covers.openlibrary.org/b/id/10543666-M.jpg",
    "public_domain": False,
    "fiction": False,
    "chapters": [
      {
        "n": 1,
        "title": "Two Systems of Thought",
        "hook": "Your brain operates two distinct engines: one lightning-fast, the other remarkably lazy.",
        "spark": "Daniel Kahneman divides the human mental landscape into two fictional characters: System 1 and System 2.\nSystem 1 operates automatically and quickly, with little or no effort and no sense of voluntary control.\nIt recognizes angry expressions, dodges sudden obstacles, and reads billboards while driving.\nSystem 2 allocates attention to effortful mental operations, including complex calculations and critical choices.\nWhen you solve seventeen times twenty-four, System 2 slowly engages, dilating pupils and increasing heart rate.\nThe central tragedy of human reasoning is that System 2 is inherently lazy.\nIt happily rubber-stamps whatever intuitive story System 1 invents without checking the underlying arithmetic.\nRecognizing when System 1 is steering your judgment is the beginning of genuine intellectual independence.",
        "key_ideas": [
          {"idea": "System 1 is fast and unconscious", "why": "It generates quick impressions, intuitions, and feelings without deliberate calculation."},
          {"idea": "System 2 requires effortful focus", "why": "Complex analysis and logical verification consume scarce metabolic energy."},
          {"idea": "Mental laziness permits cognitive errors", "why": "System 2 accepts intuitive shortcuts because conducting rigorous audits feels exhausting."}
        ],
        "line": {"text": "We can be blind to the obvious, and we are also blind to our blindness.", "type": "rabbit_take"},
        "in_your_life": [
          "Pause for five seconds when reading an emotional headline before clicking to share it.",
          "Recalculate split bills on paper rather than guessing when your intuition insists the total feels right.",
          "Notice when hunger or exhaustion makes you snap; that is System 2 depleting its working bandwidth."
        ],
        "connects_to": [{"book_id": "predictably-irrational", "chapter": 1, "reason": "System 1 shortcuts produce predictable cognitive traps that marketers exploit daily."}],
        "spoiler_level": "none"
      },
      {
        "n": 2,
        "title": "The Anchoring Effect",
        "hook": "Irrelevant numbers you hear first subtly hijack the figures you estimate next.",
        "spark": "When people consider a numerical value for an unknown quantity, an anchor is cast into their thoughts.\nIn an experiment, researchers spun a rigged wheel of fortune that stopped on either ten or sixty-five.\nParticipants were then asked whether the percentage of African nations in the United Nations was higher or lower.\nThose who saw sixty-five guessed an average of forty-five percent; those who saw ten guessed twenty-five percent.\nA completely random wheel influenced estimates about global political geography.\nAnchoring occurs because System 1 searches memory for evidence that confirms the proposed number.\nIn negotiations, whoever names the first price anchors the entire conversation range.\nTo combat anchoring, consciously search your memory for arguments that contradict the anchor.",
        "key_ideas": [
          {"idea": "Initial numbers dictate subsequent estimates", "why": "The mind automatically constructs plausible reasons why an anchor number could be true."},
          {"idea": "Anchoring works even when numbers are absurd", "why": "Random figures still bias judgment because System 1 absorbs them unconsciously."},
          {"idea": "Counter-anchoring protects negotiations", "why": "Actively considering opposing numbers breaks the grip of an opening bid."}
        ],
        "line": {"text": "The first number placed on the table exerts a magnetic pull on every counter-offer.", "type": "rabbit_take"},
        "in_your_life": [
          "Check realistic market prices before entering a flea market or negotiating salary.",
          "Ignore crossed-out original prices on shopping websites designed solely to anchor your perception of a bargain.",
          "When debating project deadlines, propose a realistic schedule before colleagues suggest an overly compressed anchor."
        ],
        "connects_to": [{"book_id": "influence-psychology-of-persuasion", "chapter": 1, "reason": "Anchoring is a core driver of the contrast principle used in sales techniques."}],
        "spoiler_level": "none"
      },
      {
        "n": 3,
        "title": "The Availability Heuristic",
        "hook": "We judge how likely an event is by how easily memorable examples spring to mind.",
        "spark": "If you ask people whether strokes or airplane crashes cause more deaths, most guess airplane crashes.\nIn reality, strokes kill dozens of times more individuals than aviation incidents worldwide.\nBecause plane crashes produce dramatic television coverage and unforgettable footage, they are easy to recall.\nThe availability heuristic explains that we evaluate the frequency or danger of an event by how readily examples occur to us.\nDramatic, emotionally charged, and recent stories dominate our subconscious risk assessments.\nEvents that are quiet, slow, and non-dramatic fade into statistical obscurity.\nPoliticians and media outlets leverage this heuristic constantly to generate disproportionate fear.\nTrue clarity demands consulting actual statistical distributions rather than vivid personal memory.",
        "key_ideas": [
          {"idea": "Recall ease substitutes for frequency", "why": "The brain equates memorable emotional vividness with real-world probability."},
          {"idea": "Media coverage distorts perception", "why": "High-intensity visual tragedies crowd out common, silent dangers from public awareness."},
          {"idea": "Check empirical base rates", "why": "Looking at actual percentages protects against fear-driven decision making."}
        ],
        "line": {"text": "What is easy to remember is rarely what is statistically common.", "type": "rabbit_take"},
        "in_your_life": [
          "Remind yourself that flying remains safer than driving whenever turbulence triggers flight anxiety.",
          "Do not assume a disease is surging just because a viral video documented one rare case.",
          "Base your career choices on employment data rather than one celebrity dropout who got lucky."
        ],
        "connects_to": [{"book_id": "the-psychology-of-money", "chapter": 3, "reason": "Personal market panic is driven by recent headlines rather than century-long returns."}],
        "spoiler_level": "none"
      },
      {
        "n": 4,
        "title": "Loss Aversion and Prospect Theory",
        "hook": "Losing one hundred dollars hurts roughly twice as much as finding one hundred dollars feels good.",
        "spark": "Classical economics assumed humans were rational calculators who valued gains and losses symmetrically.\nKahneman and Tversky proved this assumption fundamentally wrong through prospect theory.\nFor almost all humans, the psychological pain of losing something is twice as intense as the joy of winning it.\nIf someone offers you a coin flip where heads wins one hundred dollars and tails loses one hundred dollars, you will decline.\nEven with balanced odds, loss aversion makes the prospect feel deeply unattractive.\nThis evolutionary instinct kept ancestors safe when a single loss meant starvation or death.\nIn modern investing and personal decisions, however, loss aversion makes us cling to losing bets.\nPeople hold on to crashing assets hoping to break even rather than acknowledging a smart exit.",
        "key_ideas": [
          {"idea": "Pain of loss outweighs joy of gain", "why": "Losses cast a psychological shadow roughly double the size of equivalent gains."},
          {"idea": "Status quo bias shields losses", "why": "Fear of regret causes people to stick with poor defaults rather than risk change."},
          {"idea": "Sunk costs trap logical thinking", "why": "Refusing to accept past losses leads to throwing good resources after bad."}
        ],
        "line": {"text": "The response to losses is consistently stronger than the response to corresponding gains.", "type": "rabbit_take"},
        "in_your_life": [
          "Sell that unused outfit or bad investment today instead of holding on just to recover past money spent.",
          "Recognize that fear of rejection in dating or job applications is magnified by loss aversion.",
          "Evaluate opportunities from current reality rather than past sunk investments you cannot retrieve."
        ],
        "connects_to": [{"book_id": "the-subtle-art-of-not-giving-a-fuck", "chapter": 2, "reason": "Embracing struggle means accepting unavoidable losses in pursuit of worthwhile goals."}],
        "spoiler_level": "none"
      },
      {
        "n": 5,
        "title": "Overconfidence and the Narrative Fallacy",
        "hook": "We weave tidy hindsight stories that make past surprises look completely predictable.",
        "spark": "The human mind possesses an insatiable hunger for coherent narratives.\nWhen unexpected events happen, we immediately stitch together explanations that make the outcome appear inevitable.\nNassim Taleb called this the narrative fallacy, and Kahneman showed how it fuels blind overconfidence.\nAfter a startup succeeds, commentators write books praising the founder's visionary decisions.\nIf that same startup had failed, those exact same decisions would be condemned as reckless gambles.\nWe systematically ignore the colossal role of luck, timing, and unrepeatable circumstance.\nThis illusion of comprehension tricks us into believing the future is easily foreseeable.\nTrue intellectual maturity requires acknowledging that the world remains far more random than our stories allow.",
        "key_ideas": [
          {"idea": "Hindsight creates illusions of inevitability", "why": "Once an outcome occurs, we rewrite past history to make it look predictable."},
          {"idea": "Outcome bias judges decisions unfairly", "why": "A lucky bad decision looks brilliant, while an unlucky good decision gets criticized."},
          {"idea": "Humility counters false foresight", "why": "Admitting the vast role of uncertainty prevents reckless future bets."}
        ],
        "line": {"text": "Hindsight bias leads us to believe that the world is far more predictable than it actually is.", "type": "rabbit_take"},
        "in_your_life": [
          "Do not judge your study choices purely on exam grades if unexpected questions dominated the paper.",
          "Beware of biographies promising one simple formula for winning; luck always plays a quiet hand.",
          "Keep a written decision journal recording your exact reasoning before major moves occur."
        ],
        "connects_to": [{"book_id": "the-psychology-of-money", "chapter": 1, "reason": "Recognizing the massive role of luck keeps successful investors grounded."}],
        "spoiler_level": "none"
      },
      {
        "n": 6,
        "title": "The Two Selves: Experiencing vs Remembering",
        "hook": "The self that lives through your moments is entirely different from the self that remembers them.",
        "spark": "Who are you: the person who lives in this exact second, or the person who looks back on yesterday?\nKahneman revealed a profound split between the Experiencing Self and the Remembering Self.\nThe Experiencing Self feels each second of existence in real time, from quiet calm to sudden pain.\nThe Remembering Self is a storyteller that maintains scores and creates permanent impressions.\nCrucially, the Remembering Self does not compute mathematical averages of your experiences.\nIt obeys the Peak-End Rule: it rates an event almost solely by its most intense peak and its final seconds.\nA painful medical procedure that ends gently is remembered as far less agonizing than a shorter one that ends abruptly.\nWhen making choices about future holidays or relationships, the Remembering Self always casts the vote.",
        "key_ideas": [
          {"idea": "The Peak-End Rule governs memory", "why": "We judge past episodes by their most acute emotional peak and their closing moments."},
          {"idea": "Duration neglect distorts evaluation", "why": "The total minutes spent in pain or joy matter far less to memory than the final impressions."},
          {"idea": "Design endings with intention", "why": "Finishing workouts, classes, or presentations on a high note cements a positive legacy."}
        ],
        "line": {"text": "We do not choose between experiences; we choose between memories of experiences.", "type": "rabbit_take"},
        "in_your_life": [
          "End your daily study sessions with one simple, satisfying win so you remember studying as rewarding.",
          "Plan a special pleasant activity on the final day of vacations to leave a glowing memory.",
          "Do not let a minor argument at the airport ruin your memory of an entire week with close friends."
        ],
        "connects_to": [{"book_id": "flow", "chapter": 3, "reason": "Living deeply in the present moment frees the Experiencing Self from neurotic memory audits."}],
        "spoiler_level": "none"
      }
    ]
  },

  # 3. The Psychology of Money (Morgan Housel)
  {
    "id": "the-psychology-of-money",
    "title": "The Psychology of Money",
    "author": "Morgan Housel",
    "genre": "The Human Mind",
    "cover_url": "https://covers.openlibrary.org/b/id/10595562-M.jpg",
    "public_domain": False,
    "fiction": False,
    "chapters": [
      {
        "n": 1,
        "title": "No One's Crazy",
        "hook": "Your personal experiences with money make up maybe 0.00000001% of what happened in the world.",
        "spark": "People from different generations, raised by different parents with different incomes, think about money in radically divergent ways.\nA child of the Great Depression views market risk and cash safety in a way an eighties tech boom baby cannot fathom.\nSomeone who grew up in runaway inflation buys hard goods quickly, while someone from stable times hoards paper cash.\nNone of these people are crazy; they have simply formed financial models based on the specific world they witnessed.\nWhen you see someone spend or save in a manner that looks reckless to you, understand their background first.\nEvery financial decision an individual makes makes complete sense to them at that exact moment.\nThey are matching their personal mental ledger of fear, pride, and history to the immediate choice.\nFinancial wisdom starts by realizing your own background is just one narrow slice of human reality.",
        "key_ideas": [
          {"idea": "Early life financial conditions shape lifelong reflexes", "why": "What happened to the economy when you were young permanently anchors your comfort with risk."},
          {"idea": "Different experiences produce different rationalities", "why": "What looks like financial insanity to an outsider feels like sensible self-defense to the actor."},
          {"idea": "Empathy beats judgment in money talks", "why": "Recognizing varied backgrounds explains household disagreements over investing and saving far better than insults."}
        ],
        "line": {"text": "Doing well with money has a little to do with how smart you are and a lot to do with how you behave.", "type": "rabbit_take"},
        "in_your_life": [
          "Do not judge your parents' conservative spending habits if they lived through a severe local banking collapse.",
          "Recognize that your own appetite for crypto or stocks was shaped heavily by recent bull markets.",
          "Talk calmly with roommates or partners about their family background before creating shared expense budgets."
        ],
        "connects_to": [{"book_id": "thinking-fast-and-slow", "chapter": 3, "reason": "Availability heuristics anchor our financial expectations to the few years we personally witnessed."}],
        "spoiler_level": "none"
      },
      {
        "n": 2,
        "title": "Luck & Risk",
        "hook": "Luck and risk are siblings: both prove that outcomes are guided by forces outside your control.",
        "spark": "The world is far too complex to allow 100% of your outcomes to be determined by your own effort.\nEvery outcome in life is guided by forces other than individual effort, namely luck and risk.\nBill Gates attended Lakeside School, one of the only high schools on Earth with a computer teletype in 1968.\nGates himself admitted that if there were no Lakeside, there would be no Microsoft.\nAt that same high school, his brilliant classmate Kent Evans shared the exact same skill and ambition.\nKent Evans died in a mountaineering accident before graduating high school.\nOne experienced one-in-a-million positive luck; the other experienced one-in-a-million negative risk.\nBe careful who you praise and admire, and be careful who you look down upon and pity.\nRealize that not all success is due to genius, and not all failure is due to laziness.",
        "key_ideas": [
          {"idea": "Accident and agency co-exist in every outcome", "why": "Statistical serendipity often plays a decisive role that personal effort cannot overpower."},
          {"idea": "Beware of extreme case studies", "why": "Studying outlier billionaires teaches more about unique luck than repeatable daily principles."},
          {"idea": "Focus on broad patterns instead of individual icons", "why": "Broad historical truths about diversification and thrift endure far longer than individual genius stories."}
        ],
        "line": {"text": "Nothing is as good or as bad as it looks.", "type": "rabbit_take"},
        "in_your_life": [
          "Give yourself grace when an honest, well-researched project fails due to sudden market shifts.",
          "Stay humble when an early side-project blows up; acknowledge the tailwinds that helped you along.",
          "Emulate broad virtues like living below your means rather than trying to replicate a celebrity's exact portfolio."
        ],
        "connects_to": [{"book_id": "thinking-fast-and-slow", "chapter": 5, "reason": "Narrative fallacies erase luck from historical accounts to make victories look inevitable."}],
        "spoiler_level": "none"
      },
      {
        "n": 3,
        "title": "Never Enough",
        "hook": "The hardest financial skill is getting the goalpost to stop moving.",
        "spark": "Modern capitalism is exceptionally good at two things: generating wealth and generating envy.\nWhen expectations rise alongside income, you never feel the slightest increase in security or peace.\nYou can earn millions and still feel inadequate if your neighboring peers are earning tens of millions.\nAt a party hosted by a billionaire, Kurt Vonnegut informed Joseph Heller that their host made more money in a day than Heller earned from his novel Catch-22.\nHeller calmly replied: 'Yes, but I have something he will never have: enough.'\nKnowing what constitutes enough for your soul is the ultimate protective shield.\nWithout a clear finish line for your desires, you will eventually take risks that ruin everything you built.\nThere is no reason to risk what you have and need for what you don't have and don't need.",
        "key_ideas": [
          {"idea": "Moving goalposts guarantee permanent dissatisfaction", "why": "If your appetite expands at the exact pace of your paycheck, wealth produces zero happiness."},
          {"idea": "Social comparison is an unwinnable battle", "why": "There is always someone with a bigger yacht, larger house, or faster sports car."},
          {"idea": "Invaluable things must never be risked", "why": "Reputation, freedom, family, and peace of mind must never be staked on speculative gains."}
        ],
        "line": {"text": "There is no reason to risk what you have and need for what you do not have and do not need.", "type": "rabbit_take"},
        "in_your_life": [
          "Define your desired annual lifestyle cost in writing before you start receiving career promotions.",
          "Mute accounts that trigger lifestyle envy on your feed; they are selling products, not peace.",
          "Celebrate having enough time to read, walk, and sleep instead of chasing prestige titles you secretly hate."
        ],
        "connects_to": [{"book_id": "meditations", "chapter": 3, "reason": "Stoic philosophy teaches that real wealth is not having great possessions, but few wants."}],
        "spoiler_level": "none"
      },
      {
        "n": 4,
        "title": "Confounding Compounding",
        "hook": "Warren Buffett's real secret is not his stock picking, but that he has been investing for 80 years.",
        "spark": "Human intuition struggles to grasp the counterintuitive mathematics of exponential compounding.\nMore than ninety-nine percent of Warren Buffett's wealth was accumulated after his fiftieth birthday.\nIf Buffett had started investing at age thirty and retired at sixty, few people would know his name today.\nHis true genius was not just annual returns, but the sheer, unbroken duration of his timeline.\nIce ages on Earth were not caused by brutally cold winters, but by slightly cooler summers that failed to melt winter snow.\nThe thin residual layer of snow reflected sunlight, cooling the climate further, allowing more snow to persist next year.\nTiny, persistent advantages compounded across vast spans of time produce monumental glacial shifts.\nIn your personal life, small sums invested early and left undisturbed will always outperform clever, sporadic bets.",
        "key_ideas": [
          {"idea": "Time is the engine of compound growth", "why": "The exponent of duration creates the staggering gains, far more than marginal returns."},
          {"idea": "Survival enables compounding to work", "why": "You must avoid catastrophic wipeouts so your compounding curve is never forcibly reset to zero."},
          {"idea": "Intuition under-appreciates slow beginnings", "why": "Linear minds expect steady growth, but exponential curves remain flat for decades before soaring."}
        ],
        "line": {"text": "Compounding does not rely on big returns; it relies on uninterrupted, consistent endurance.", "type": "rabbit_take"},
        "in_your_life": [
          "Start investing fifty dollars every month right now, even if the total looks trivial today.",
          "Do not interrupt your savings during market pullbacks; time in the market beats timing the market.",
          "Apply compounding to learning: reading fifteen minutes daily builds an encyclopedic mind by thirty."
        ],
        "connects_to": [{"book_id": "atomic-habits", "chapter": 1, "reason": "Habits behave identically to financial capital: small inputs yield exponential compound interest."}],
        "spoiler_level": "none"
      },
      {
        "n": 5,
        "title": "Getting Wealthy vs. Staying Wealthy",
        "hook": "Getting money requires taking risks; keeping money requires paranoia, frugality, and humility.",
        "spark": "Getting wealthy and staying wealthy are two completely distinct skill sets that frequently war with each other.\nGetting wealthy requires taking bold risks, projecting optimism, and shooting for the stars.\nStaying wealthy, however, requires the exact opposite: humility, frugality, and healthy paranoia.\nIt demands accepting that at least part of your success was driven by luck you cannot easily duplicate.\nIt means keeping a substantial cash buffer so unexpected emergencies never force you to liquidate assets at market bottoms.\nMany brilliant entrepreneurs become rich through audacity, only to go bankrupt because they cannot turn the risk valve off.\nJesse Livermore made one hundred million dollars shorting the 1929 stock market crash, then lost everything within four years.\nSurvival is the only metric that matters because staying in the game is the prerequisite for all future gains.",
        "key_ideas": [
          {"idea": "Risk tolerance must adjust over time", "why": "The reckless aggression that builds an initial nest egg will destroy it if left unchecked."},
          {"idea": "Maintain a margin of safety", "why": "A financial plan is only useful if it survives the inevitable errors and market downturns."},
          {"idea": "Cash is an emotional shock absorber", "why": "Holding cash may drag statistical returns slightly, but it buys uninterrupted nighttime sleep."}
        ],
        "line": {"text": "A plan is only good if it can survive reality when reality does not go according to plan.", "type": "rabbit_take"},
        "in_your_life": [
          "Keep three to six months of living expenses in a boring bank account that you never gamble with.",
          "Never borrow money against your investments; leverage turns standard market dips into total ruin.",
          "Treat success as a temporary lease that must be renewed with daily diligence and modesty."
        ],
        "connects_to": [{"book_id": "the-48-laws-of-power", "chapter": 7, "reason": "Conserving power requires constant vigilance and protective buffers against sudden reversals."}],
        "spoiler_level": "none"
      },
      {
        "n": 6,
        "title": "Freedom: The Highest Dividend",
        "hook": "The greatest intrinsic value of money is its ability to give you control over your time.",
        "spark": "More than your house, your wristwatch, or your social standing, the highest dividend money pays is autonomy.\nHaving the ability to wake up in the morning and say, 'I can do whatever I want today,' is the ultimate wealth.\nDecades of psychological research consistently demonstrate that control over one's schedule is the strongest predictor of well-being.\nDoing work you love on a schedule you hate feels remarkably similar to doing work you despise.\nA person with six months of emergency savings can decline an abusive boss or take an exciting pay cut for an emerging venture.\nThey possess an invisible degree of leverage that the heavily indebted executive with a luxury sports car lacks.\nTrue riches are defined not by the luxury goods you buy, but by the negative options you can refuse.",
        "key_ideas": [
          {"idea": "Time autonomy is the supreme metric of wealth", "why": "Control over daily schedule brings more enduring happiness than any consumer possession."},
          {"idea": "Savings buy flexibility and independence", "why": "Unspent money gives you the power to choose what to work on, when to rest, and who to work with."},
          {"idea": "Avoid golden handcuffs", "why": "High salaries tied to uncontrollable eighty-hour weeks often feel like plush prison cells."}
        ],
        "line": {"text": "The highest form of wealth is the ability to wake up and say: I can do whatever I want today.", "type": "rabbit_take"},
        "in_your_life": [
          "Prioritize building savings that give you the courage to leave a toxic job or career path.",
          "Evaluate purchases by asking how many hours of your life energy they cost to acquire.",
          "Choose careers with schedule sovereignty over prestigious titles that demand total constant availability."
        ],
        "connects_to": [{"book_id": "deep-work", "chapter": 3, "reason": "Sovereignty over your calendar is the essential prerequisite for producing deep, meaningful work."}],
        "spoiler_level": "none"
      }
    ]
  }
]

with open("scripts/catalog_builder/hero_human_mind_p1.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)

print(f"Generated {len(books)} books for hero_human_mind_p1.json")
