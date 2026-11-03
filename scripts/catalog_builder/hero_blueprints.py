# -*- coding: utf-8 -*-
"""
hero_blueprints.py
High-curiosity chapter blueprints for all 36 Hero Books.
"""

# Each blueprint defines:
# title, author, genre, cover_url, public_domain, fiction, and chapters:
# [n, title, hook, spark_lines, [(idea, why), ...], (line_text, line_type), [life_examples, ...], [(target_id, ch_num, reason), ...], spoiler]

HERO_BLUEPRINTS = {
  # --- THE HUMAN MIND (12) ---
  "deep-work": {
    "title": "Deep Work", "author": "Cal Newport", "genre": "The Human Mind",
    "cover_url": "https://covers.openlibrary.org/b/id/10543668-M.jpg", "public_domain": False, "fiction": False,
    "chapters": [
      (1, "Deep Work Is Valuable", "The ability to perform deep cognitive work is becoming increasingly rare and prized.", [
        "Modern knowledge workers are drown in an ocean of instant messages, notifications, and meetings.",
        "Most people spend their workdays in shallow work: logistical tasks easily performed while distracted.",
        "Deep work is the ability to focus without distraction on a cognitively demanding task.",
        "It pushes your cognitive capabilities to their limit and creates new value that is hard to replicate.",
        "If you cannot learn complex tools quickly, you will be replaced by automated systems or cheaper labor.",
        "To master difficult subjects and produce elite creative output, you must cultivate unbroken concentration.",
        "The economy rewards those who can rapidly master hard things and produce at an elite level.",
        "Depth is the superpower of the twenty-first century knowledge economy."
      ], [
        ("Shallow work produces zero moat", "Answering emails and attending meetings produces minimal lasting differentiation."),
        ("Deliberate practice demands depth", "Mastering challenging skills requires intense, uninterrupted concentration cycles."),
        ("High-value output equals time multiplied by focus", "Ten hours of distracted work achieves less than three hours of pure immersion.")
      ], ("Clarity about what matters provides clarity about what does not.", "rabbit_take"), [
        "Schedule two ninety-minute blocks every morning with phone turned completely off.",
        "Batch all social media checking and email replies into a single afternoon window.",
        "Decline non-essential meetings to protect time for challenging writing or coding assignments."
      ], [("flow", 1, "Deep work is the practical discipline required to access sustained states of cognitive flow.")], "none"),
      (2, "Deep Work Is Rare", "Modern office culture systematically destroys the very concentration it claims to value.", [
        "Open office floor plans, Slack channels, and constant connectivity promise seamless collaboration.",
        "In reality, they create a culture of continuous partial attention and chronic fragmentation.",
        "Whenever you check your inbox for thirty seconds, a residue of attention stays behind.",
        "Sophie Leroy proved that attention residue severely impairs performance on subsequent tasks.",
        "Because deep work is hard to measure, people substitute visible busyness for genuine productivity.",
        "Sending fifty quick messages feels like effort, but it creates negligible tangible value.",
        "Those who swim against this tide and protect their attention build an unassailable career advantage.",
        "Rarity makes depth profoundly valuable to anyone willing to structure their days differently."
      ], [
        ("Attention residue cripples cognition", "Quick glances at messages leave fragments of your brain stuck on the interruption."),
        ("Busyness is a proxy for productivity", "Visible activity is often used to mask a lack of genuine creative output."),
        ("Cultivate monastic focus windows", "Stepping away from instant connectivity gives your brain space to synthesize breakthroughs.")
      ], ("If you do not produce, you will not thrive; and production requires depth.", "rabbit_take"), [
        "Close communication apps when drafting important reports or studying complex formulas.",
        "Tell study partners that you will respond to group chats at set hours rather than instantly.",
        "Judge your workday by the depth of your focus rather than the quantity of cleared notifications."
      ], [("thinking-fast-and-slow", 1, "Multitasking forces System 2 into constant, exhausting context switches.")], "none"),
      (3, "Deep Work Is Meaningful", "A life spent in deep craft produces profound psychological calm and satisfaction.", [
        "Neurologist Barbara Fredrickson demonstrated that what you pay attention to shapes your emotional reality.",
        "When your day is filled with petty crises and notifications, your mind reflects frantic disorder.",
        "When you immerse your attention in a deep, challenging craft, your consciousness enters a state of serene order.",
        "A craftsman working on wood, code, or literature experiences the intrinsic dignity of creation.",
        "Meaning is not found in grand abstract titles; it is found in the sacred quality of your daily focus.",
        "The idle mind is a wandering playground for anxieties, insecurities, and existential dread.",
        "Deep focus anchors the psyche, banishing petty worries and cultivating quiet inner joy.",
        "To live a deep life is to live a good, grounded, and dignified human life."
      ], [
        ("Attention shapes subjective reality", "Your world is what you pay attention to; focus on depth and life feels substantial."),
        ("Craftsmanship banishes existential dread", "Dedication to high standards in your work provides inherent psychological purpose."),
        ("Depth protects emotional health", "Immersion in challenging problems quiets the neurotic inner critic.")
      ], ("I will live the focused life, because it is the best kind there is.", "rabbit_take"), [
        "Notice how peaceful you feel after two hours of uninterrupted drawing, writing, or coding.",
        "When feeling anxious or overwhelmed, pick one challenging problem and work on it deeply.",
        "Treat your study desk as a sacred workbench dedicated to mastering your craft."
      ], [("mans-search-for-meaning", 4, "Purpose is created through devoted engagement with meaningful creative responsibilities.")], "none"),
      (4, "Rule 1: Work Deeply", "Choose a scheduling philosophy that fiercely defends your daily cognitive hours.", [
        "Willpower is not enough to maintain deep work; you need robust rituals and routines.",
        "Cal Newport outlines four scheduling philosophies: monastic, bimodal, rhythmic, and journalistic.",
        "The rhythmic philosophy is best for most students and professionals: dedicate fixed hours each day.",
        "Create a dedicated environment: remove distractions, prepare water, and set clear milestone goals.",
        "Grand gestures, such as booking a remote cabin or quiet hotel room, can shock the mind into focus.",
        "J.K. Rowling finished writing the final Harry Potter novel by checking into a quiet Edinburgh hotel.",
        "Treat your focus time with the seriousness of a scheduled medical appointment.",
        "Routines eliminate the mental friction of constantly deciding when and where to start working."
      ], [
        ("Rely on rituals, not willpower", "Predetermined start times and quiet locations remove daily decision fatigue."),
        ("The rhythmic strategy builds consistency", "A predictable morning block creates automatic momentum week after week."),
        ("Grand gestures signal importance", "Changing environments or investing in dedicated spaces signals commitment to your mind.")
      ], ("Great creative achievements require long periods of uninterrupted, protected solitude.", "rabbit_take"), [
        "Block 8:00 AM to 10:00 AM in your calendar as non-negotiable study time every weekday.",
        "Establish a clear pre-work ritual: clear the desk, brew tea, and put on noise-canceling headphones.",
        "Study in the silent upper floors of a library where conversation is strictly prohibited."
      ], [("atomic-habits", 3, "Implementation intentions remove friction by defining exact times and places for deep study.")], "none"),
      (5, "Rule 2: Embrace Boredom", "Train your brain to tolerate stillness instead of reaching for a screen every free second.", [
        "The ability to concentrate deeply is a mental muscle that must be trained through daily resistance.",
        "If you reach for your phone every time you wait in line, your brain becomes addicted to constant novelty.",
        "Once your brain is wired for distraction, it cannot endure thirty minutes of quiet study without craving a fix.",
        "To rebuild focus, practice embracing boredom: sit in quiet waiting rooms without pulling out a screen.",
        "Schedule your internet use: instead of staying online and taking breaks to focus, stay offline and take breaks to check.",
        "Practice productive meditation: think through a single professional problem while walking or running.",
        "Hold the problem in your mind, notice when attention wanders, and gently steer it back.",
        "Teaching your brain to sit comfortably with silence restores your cognitive independence."
      ], [
        ("Distraction tolerance ruins focus", "Feeding the brain novelty every boring second destroys its capacity for deep reading."),
        ("Schedule internet breaks", "Living offline by default and taking deliberate breaks online retrains attention."),
        ("Productive meditation sharpens focus", "Holding a single complex question in mind during walks strengthens cognitive endurance.")
      ], ("If you cannot endure boredom, you will never master difficult, high-value skills.", "rabbit_take"), [
        "Leave your phone in your pocket while waiting for the elevator, bus, or coffee order.",
        "Go for a thirty-minute walk without headphones and let your thoughts wander through a problem.",
        "Resist opening a new browser tab the moment a homework problem feels slightly confusing."
      ], [("the-power-of-now", 3, "Being present in quiet moments frees consciousness from compulsive digital stimulation.")], "none"),
      (6, "Rule 3: Quit Social Media", "Reject tools that provide tiny bits of entertainment in exchange for your life's attention.", [
        "Most people use the Any-Benefit Approach to evaluate network tools: if it offers any tiny benefit, adopt it.",
        "Professional craftsmen use the Craftsman Approach: adopt a tool only if its benefits substantially outweigh its harms.",
        "Social media platforms are designed by behavioral engineers to hijack dopamine and harvest human attention.",
        "They offer trivial conveniences—seeing high school acquaintances—at the catastrophic cost of deep concentration.",
        "Try a thirty-day digital detox: delete apps without announcing it to test whether anyone actually notices.",
        "Put real thought into your leisure time: plan high-quality hobbies rather than defaulting to passive scrolling.",
        "Give your evening hours structure through reading, sports, woodworking, or music.",
        "When your leisure is fulfilling, you no longer crave the cheap digital dopamine of the infinite feed."
      ], [
        ("The Craftsman Approach to tools", "Only use services that actively support your primary creative and human priorities."),
        ("Social media trades diamonds for plastic", "Hours of profound focus are sacrificed for superficial online validation."),
        ("Structured leisure cures digital addiction", "Engaging, physical hobbies satisfy the spirit far deeper than passive scrolling.")
      ], ("Do not let algorithmic platforms commodify the finite hours of your one precious life.", "rabbit_take"), [
        "Delete social media apps from your phone for one weekend and notice your mental clarity.",
        "Replace evening screen scrolling with reading twenty pages of a physical paperback.",
        "Pick up an analog hobby like cooking, chess, or sketching that demands physical presence."
      ], [("the-psychology-of-money", 6, "True freedom is having control over your time rather than surrendering it to feeds.")], "none")
    ]
  }
}

print("hero_blueprints.py started with Deep Work.")
