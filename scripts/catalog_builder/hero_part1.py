# -*- coding: utf-8 -*-
"""
hero_part1.py
Defines Human Mind books 7 to 12:
- flow
- predictably-irrational
- the-power-of-habit
- influence-psychology-of-persuasion
- the-laws-of-human-nature
- nudge
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

PART1_BOOKS = [
  # 7. Flow (Mihaly Csikszentmihalyi)
  {
    "id": "flow",
    "title": "Flow: The Psychology of Optimal Experience",
    "author": "Mihaly Csikszentmihalyi",
    "genre": "The Human Mind",
    "cover_url": "https://covers.openlibrary.org/b/id/10543670-M.jpg",
    "public_domain": False, "fiction": False,
    "chapters": [
      ch(1, "Happiness Revisited", "Genuine happiness is not a passive state, but an active mastery of psychic energy.", [
        "Human beings have spent millennia searching for lasting contentment in wealth and prestige.",
        "Yet modern studies demonstrate that material abundance does not reliably increase subjective happiness.",
        "The moments when life feels richest occur when a person's body or mind is stretched to its limits.",
        "This voluntary effort to accomplish something difficult and worthwhile is what Csikszentmihalyi terms flow.",
        "Flow is the optimal state of consciousness where you become completely absorbed in an activity.",
        "During flow, self-consciousness vanishes, time distorts, and every action flows seamlessly into the next.",
        "Optimal experience is something we make happen through disciplined personal agency.",
        "Taking control of your inner experience is the direct gateway to authentic joy."
      ], [
        ("Material comfort does not yield joy", "External riches cannot order the chaotic contents of an undisciplined mind."),
        ("Flow requires voluntary struggle", "Peak happiness arises from meeting difficult challenges with full capacity."),
        ("Psychic energy must be directed", "Without conscious goals, human attention drifts into anxiety and boredom.")
      ], ("The best moments in our lives are not passive, receptive, or relaxing.", "rabbit_take"), [
        "Notice how satisfying a hard training session feels compared to three hours of passive couch resting.",
        "Set clear daily creative targets so your working hours have direction and purpose.",
        "Engage in hobbies that challenge your skill rather than defaulting to mindless video consumption."
      ], [("deep-work", 3, "Deep cognitive immersion creates the exact psychological conditions for flow states.")]),
      ch(2, "The Anatomy of Consciousness", "Attention is your most precious psychic resource; how you invest it shapes your soul.", [
        "Consciousness is an intentional clearing house that processes sensory and cognitive information.",
        "Our working memory can only process roughly one hundred and twenty bits of information per second.",
        "Listening to another person speak consumes nearly half of that total bandwidth.",
        "Whatever commands your attention becomes the fabric of your lived psychological reality.",
        "Psychic entropy occurs when conflicting desires, fears, or distractions throw attention into chaos.",
        "When attention is fragmented by anxiety, you lose the ability to act effectively.",
        "Ordering consciousness through clear intentions protects your mental clarity from external storms.",
        "Mastering your life requires mastering where and how you direct your finite attention."
      ], [
        ("Attention has severe bandwidth limits", "You can only attend to a tiny fraction of incoming sensory stimuli at any second."),
        ("Psychic entropy degrades performance", "Internal worry and scattered focus drain the energy required for excellence."),
        ("Focus restores psychological order", "Centering awareness on a coherent goal instantly reduces internal friction.")
      ], ("Control of consciousness determines the quality of life.", "rabbit_take"), [
        "Turn off phone notifications when having meaningful conversations with friends.",
        "Recognize that rumination about past mistakes is simply psychic entropy wasting attention.",
        "Choose inspiring books that feed your consciousness rather than algorithmic rage bait."
      ], [("thinking-fast-and-slow", 1, "System 2 attention is an exhaustible resource that must be allocated with extreme care.")]),
      ch(3, "The Conditions of Flow", "Flow arises when clear goals, immediate feedback, and matched challenges align.", [
        "Flow does not happen by accident; it requires three specific structural conditions.",
        "First, you need clear goals: you must know exactly what you are trying to accomplish at each step.",
        "Second, you need immediate feedback: you must receive unambiguous signals on how well you are performing.",
        "Third, you need a balance between challenges and skills: the task must stretch you without overwhelming you.",
        "If challenge exceeds skill, you plunge into anxiety and panic.",
        "If skill exceeds challenge, you drift into apathy and boredom.",
        "When challenge and skill meet at a high level, the self steps aside and pure engagement takes over.",
        "Structure your daily tasks with clear milestones to unlock flow on command."
      ], [
        ("Clear rules guide momentum", "Ambiguous goals create hesitation; clear targets enable smooth cognitive execution."),
        ("Immediate feedback anchors focus", "Knowing how you are doing in real time prevents attention from wandering."),
        ("The Goldilocks balance of challenge", "Flow exists on the narrow ridge between the abyss of anxiety and the swamp of boredom.")
      ], ("When goals are clear and feedback immediate, the self vanishes into the joy of pure action.", "rabbit_take"), [
        "Break large academic papers into distinct mini-goals with immediate word-count milestones.",
        "Use chess or video games to observe how explicit rules and instant feedback foster deep focus.",
        "Increase the difficulty of routine chores by timing yourself to see if you can complete them faster."
      ], [("atomic-habits", 7, "Operating at the four percent challenge boundary sustains motivation and enters flow.")]),
      ch(4, "The Flow of Thought", "The human mind can turn any mental activity into an exhilarating voyage of discovery.", [
        "You do not need mountains or musical instruments to experience flow; your mind is an infinite playground.",
        "Reading great literature, solving mathematical puzzles, or learning a language creates immense flow.",
        "Memory was the original art of flow for ancient philosophers who memorized entire epics.",
        "By structuring ideas into mental models, you can explore concepts anywhere, even in a prison cell.",
        "The joy of learning for its own sake is known as an autotelic experience.",
        "An autotelic activity is one where the reward is intrinsic to the doing, not dependent on external praise.",
        "When you study out of pure curiosity rather than fear of tests, education becomes an intoxicating adventure.",
        "Cultivate an autotelic mind and you will never experience boredom for the rest of your life."
      ], [
        ("The mind is self-contained entertainment", "A well-trained memory and curious intellect can find flow in any physical setting."),
        ("Autotelic motivation endures", "Doing an activity for its own sake outlasts any fragile desire for external accolades."),
        ("Mental models structure thought", "Organizing knowledge into coherent frameworks transforms dry facts into vivid insights.")
      ], ("The ultimate test of an educated mind is the ability to enjoy its own company in solitude.", "rabbit_take"), [
        "Learn the rules of a new card game or puzzle and immerse yourself in finding optimal strategies.",
        "Read historical accounts with an eye for discovering timeless patterns of human behavior.",
        "Spend a train ride mentally reconstructing the plot of your favorite book without checking your phone."
      ], [("siddhartha", 7, "Inner peace comes from experiencing the river of consciousness without clinging to outcomes.")]),
      ch(5, "Work as Flow", "Transforming boring labor into a rewarding craft by treating it as an athletic game.", [
        "Many people view work as an unpleasant chore they must endure to earn money for weekend leisure.",
        "Ironically, people frequently experience more flow during their jobs than during their unstructured free time.",
        "Work provides built-in goals, feedback, and challenges, whereas unstructured weekends often collapse into passive malaise.",
        "A welder or surgeon can turn their job into an art form by constantly refining their precision.",
        "By setting personal speed or quality records, you transform ordinary tasks into absorbing games.",
        "Do not wait for your employer to make your job engaging; take personal ownership of your standards.",
        "When you approach your labor as a dedicated craftsman, work stops being a prison and becomes a playground.",
        "Mastery of your craft is the most reliable path to professional dignity and daily flow."
      ], [
        ("Work naturally provides flow structures", "Occupational deadlines and goals organize attention far better than empty leisure."),
        ("Craftsmanship elevates mundane tasks", "Refining small nuances of technique makes repetitive duties intellectually engaging."),
        ("Take ownership of personal standards", "Exceeding minimum job requirements rewards you with intrinsic competence and pride.")
      ], ("Even the most routine labor becomes an art when performed with deliberate, loving craftsmanship.", "rabbit_take"), [
        "Turn dishwashing into a flow exercise by optimizing your sequence and water efficiency.",
        "Challenge yourself to write the cleanest, most concise code possible even on minor project tasks.",
        "Treat customer service interactions as empathy games: see how quickly you can make an upset caller smile."
      ], [("deep-work", 1, "Approaching cognitive tasks as serious craftsmanship yields deep professional fulfillment.")]),
      ch(6, "The Autotelic Self", "Building a resilient personality that converts unexpected obstacles into fuel for growth.", [
        "An autotelic person possesses a self-contained purpose and is rarely swayed by external rewards or threats.",
        "When tragedy strikes, non-autotelic people collapse because their external anchors are broken.",
        "An autotelic individual immediately reframes the catastrophe as a new challenge requiring creative adaptation.",
        "They transform adversity into enjoyable challenges through four key traits: focus, goal-setting, feedback, and immersion.",
        "They do not worry about what others think of them, freeing all psychic energy for living fully.",
        "They see themselves as part of a larger interconnected whole, reducing the fragile neurosis of the ego.",
        "By learning to enjoy the process of life itself, they become psychologically invincible.",
        "Cultivate the autotelic spirit, and every hour of your existence becomes an extraordinary blessing."
      ], [
        ("Autotelic resilience overcomes crises", "Viewing hardship as a puzzle rather than a curse preserves emotional composure."),
        ("Ego detachment frees energy", "Stopping the obsession with social approval releases immense focus for creative action."),
        ("Connection to the cosmos", "Seeing oneself as part of a larger ongoing universe dissolves petty everyday irritations.")
      ], ("The person who has mastered flow can turn tragedy into a source of renewed inner strength.", "rabbit_take"), [
        "When flights are delayed, pull out a notebook and treat the extra hour as unexpected writing time.",
        "Reframe tough academic criticism as precise coaching that illuminates your next step of growth.",
        "Smile when plans fall apart, knowing that navigating surprises tests and refines your character."
      ], [("mans-search-for-meaning", 3, "Finding meaning in suffering transforms unavoidable pain into heroic spiritual triumph.")])
    ]
  },

  # 8. Predictably Irrational (Dan Ariely)
  {
    "id": "predictably-irrational",
    "title": "Predictably Irrational",
    "author": "Dan Ariely",
    "genre": "The Human Mind",
    "cover_url": "https://covers.openlibrary.org/b/id/10543672-M.jpg",
    "public_domain": False, "fiction": False,
    "chapters": [
      ch(1, "The Truth About Relativity", "We rarely know what we want until we see it in context with comparative decoys.", [
        "Humans do not evaluate things in absolute terms; we judge everything relative to nearby comparisons.",
        "The Economist once offered three subscriptions: web for $59, print for $125, and print-and-web for $125.",
        "Nobody chose the print-only option, but its presence made the print-and-web deal look like a miraculous bargain.",
        "When Ariely removed the print-only decoy, most students switched to the cheaper $59 web option.",
        "The decoy changed their preference without anyone realizing they were being steered.",
        "Relativity distorts our salary satisfaction, our house choices, and even our romantic evaluations.",
        "We compare our lives to friends just above us on the ladder, fostering endless, unnecessary envy.",
        "Break the cycle of relativity by broadening your frame of reference and defining internal values."
      ], [
        ("Decoys dictate choices", "Introducing an inferior third option makes the target choice look overwhelmingly attractive."),
        ("We judge through nearby context", "Human judgment lacks an internal compass; it relies entirely on local comparisons."),
        ("Control your comparison circles", "Choosing smaller or healthier social circles instantly cures artificial lifestyle inadequacy.")
      ], ("We always look at the things around us in relation to others; we cannot help it.", "rabbit_take"), [
        "Watch out for menu items with high prices whose sole purpose is making the second-priciest meal seem reasonable.",
        "Do not compare your entry-level salary to influencers who selectively showcase luxury trips.",
        "When buying electronics, evaluate whether you actually need the features of the higher-tier comparison model."
      ], [("thinking-fast-and-slow", 2, "Anchoring and relativity work hand-in-hand to manipulate intuitive System 1 pricing.")]),
      ch(2, "The Cost of Zero Cost", "The concept of 'Free!' exerts an irrational emotional pull that leads to foolish decisions.", [
        "Zero is not just another price; it is an emotional hot button that blinds human rationality.",
        "In an experiment, Ariely offered Lindt truffles for fifteen cents and ordinary Hershey kisses for one cent.",
        "Seventy-three percent of buyers chose the superior Lindt truffle, making a sensible price-to-quality trade.",
        "When he reduced both prices by one cent—making kisses free and truffles fourteen cents—the result flipped.",
        "Sixty-nine percent of people chose the free kiss, even though the price difference remained identical.",
        "Free creates an illusion of zero downside, blinding us to the hidden costs of time, storage, and health.",
        "People wait in line for forty minutes in the rain to get a free two-dollar scoop of ice cream.",
        "Recognize that free items carry heavy invisible price tags that waste your most precious resource."
      ], [
        ("Zero is an emotional trigger", "Free eliminates the fear of loss, creating an irresistible urge to claim the item."),
        ("Hidden costs accompany free goods", "Wasted hours in line and cluttered storage spaces are the real cost of free promotions."),
        ("Calculate total opportunity cost", "Always ask what your time and health are worth before pursuing free promotions.")
      ], ("Free is not merely a discount; it is an emotional gravity well that distorts judgment.", "rabbit_take"), [
        "Refuse free promotional swag at conferences if you know it will end up collecting dust in your closet.",
        "Never buy five unwanted items just to hit the threshold for free shipping.",
        "Value forty minutes of uninterrupted reading far more than waiting in line for a complimentary snack."
      ], [("the-psychology-of-money", 3, "Understanding what is truly enough stops you from taking bad bargains out of greed.")]),
      ch(3, "The Cost of Social Norms", "Mixing market norms with social norms poisons friendships and destroys goodwill.", [
        "Human society operates across two distinct realms: social norms and market norms.",
        "Social norms govern friendships, family dinners, and favors: warm, cooperative, with no instant repayment expected.",
        "Market norms govern business transactions: cold, contractual, sharp, and settled immediately with currency.",
        "The moment you introduce market compensation into a social realm, the social norm evaporates instantly.",
        "If your mother-in-law cooks a magnificent Thanksgiving dinner and you hand her forty dollars, you insult her deeply.",
        "A daycare center fined parents who picked up their children late, hoping to reduce tardiness.",
        "Instead, late pickups doubled: parents viewed the fine as a market fee that cleared their guilt.",
        "Guard the boundary of social norms fiercely, for once market norms enter, trust rarely recovers."
      ], [
        ("Two separate behavioral realms", "Social norms are built on community goodwill; market norms are built on transactional exchange."),
        ("Cash destroys social motivation", "Paying friends for small favors insults the spirit of mutual loyalty."),
        ("Social bonds create higher loyalty", "Teams bonded by shared mission outperform teams motivated purely by bonus checks.")
      ], ("When social norms clash with market norms, social norms leave the scene and seldom return.", "rabbit_take"), [
        "Offer to help friends move with pizza and camaraderie; never offer them an awkward hourly wage.",
        "Thank hosts with a thoughtful gift or dessert rather than offering to split the grocery receipt.",
        "Cultivate study clubs based on mutual academic growth rather than scorekeeping who helped whom."
      ], [("influence-psychology-of-persuasion", 2, "Reciprocity works best as an unspoken social bond rather than a calculated market trade.")]),
      ch(4, "The Power of a Free Cookie", "Social norms make people generous, but market prices turn them into selfish calculators.", [
        "When an office brings a box of gourmet cookies and leaves a sign saying 'Free,' people take one with modesty.",
        "Everyone considers others and restrains their appetite so colleagues can share in the treat.",
        "If you put a coin jar next to the box charging ten cents per cookie, social norms vanish.",
        "Individuals will pull out a dollar bill, buy ten cookies without guilt, and leave the box empty for everyone else.",
        "The price transformed a communal gift into an individual commercial right.",
        "When price is zero, we think about community welfare, fairness, and ethical behavior.",
        "When price enters, we calculate personal benefit versus cost and act strictly in self-interest.",
        "Understanding this paradox allows leaders to inspire generosity through shared culture rather than small cash incentives."
      ], [
        ("Zero price evokes communal ethics", "Free goods prompt consideration of social fairness and sharing among peers."),
        ("Commercial prices remove guilt", "Paying even a trivial coin removes the social obligation to share with others."),
        ("Design systems that appeal to pride", "Appealing to personal character produces more cooperative behavior than micro-fees.")
      ], ("A price tag changes an ethical communal decision into a selfish commercial calculation.", "rabbit_take"), [
        "Lead volunteer groups with shared ideals and appreciation rather than minor financial stipends.",
        "Notice how shared kitchen snacks are respected until someone claims ownership rights.",
        "Protect team camaraderie by emphasizing collective pride in work rather than competing for petty bonuses."
      ], [("nudge", 3, "Social norms are powerful default nudges that steer group conduct without coercion.")]),
      ch(5, "The High Price of Ownership", "We fall in love with what we own and irrationally overvalue our personal possessions.", [
        "Duke University students camp out in tents for weeks in the winter for a chance at men's basketball tickets.",
        "Because demand far exceeds supply, tickets are distributed via a random lottery among campers.",
        "Ariely called students after the lottery: those who did not win were willing to pay $170 to buy a ticket.",
        "Students who won the exact same lottery refused to sell their ticket for less than $2,400.",
        "The endowment effect explains that owning an item instantly inflates its subjective value in our eyes.",
        "We focus on what we will lose rather than what we might gain from trading.",
        "Companies exploit this with thirty-day free trials: once the device is in your home, it feels like yours.",
        "View possessions with objective detachment: you are simply a temporary custodian of matter."
      ], [
        ("The endowment effect distorts value", "We value things we own far higher than identical items owned by other people."),
        ("Focus on loss aversion", "Parting with possessions feels like an acute loss, blinding us to better alternative uses of money."),
        ("Beware of virtual ownership", "Viewing or touching an item creates an emotional attachment before you even purchase it.")
      ], ("Once we own something, we begin to value it far more than anyone else in the world ever will.", "rabbit_take"), [
        "When decluttering, ask what you would pay to buy the item today if you did not already own it.",
        "Be wary of home trial subscriptions; companies know returning the item feels like a painful loss.",
        "Evaluate used cars and vintage clothes objectively without paying a premium for emotional attachment."
      ], [("thinking-fast-and-slow", 4, "Loss aversion is the psychological root driving the irrational endowment effect.")]),
      ch(6, "The Problem of Procrastination", "Pre-commitments and external deadlines are our best weapons against self-sabotaging delays.", [
        "Every human being intends to eat healthy, save money, and complete assignments early.",
        "When the moment of action arrives, our future rational self is ambushed by our present emotional self.",
        "Ariely tested three college classes on essay deadlines: one had strict deadlines, one chose deadlines, one was free.",
        "The class with strict, evenly spaced deadlines imposed by the professor earned the highest final grades.",
        "The class that could turn everything in at the end of the term produced sloppy work and earned the lowest grades.",
        "Students who chose their own deadlines did reasonably well, proving that self-imposed boundaries work.",
        "To defeat procrastination, make binding pre-commitments that penalize your future self for delay.",
        "Rely on external accountability systems rather than pretending tomorrow's willpower will be infinite."
      ], [
        ("Self-control is weak in the present", "Immediate gratification routinely overpowers long-term rational intentions."),
        ("Evenly spaced deadlines work best", "Breaking projects into mandatory milestones prevents the panic of last-minute cramming."),
        ("Binding pre-commitments secure goals", "Setting up automatic barriers and penalties forces compliance when motivation wanes.")
      ], ("We are all born with procrastination; only structured pre-commitments allow us to conquer it.", "rabbit_take"), [
        "Ask a study partner to hold twenty dollars of your money, only returned if you submit your draft by Friday.",
        "Set calendar milestones two weeks ahead of actual university or project deadlines.",
        "Automate monthly savings transfers on the exact morning your paycheck arrives before you can spend it."
      ], [("atomic-habits", 5, "Reducing friction and establishing clear commitment devices defeats chronic hesitation.")])
    ]
  }
]

print("hero_part1.py loaded with Flow and Predictably Irrational.")
