# -*- coding: utf-8 -*-
"""
gen_hero_self.py
Generates the 12 Hero Books for 'Self Discovery' (6 chapters each).
Includes 4 public-domain classics with authentic quotes:
- Meditations (Marcus Aurelius)
- Thirukkural (Thiruvalluvar)
- Siddhartha (Hermann Hesse)
- Gitanjali (Rabindranath Tagore)
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

def add_b(b_id, title, author, cover, pd, chapters):
    books.append({
        "id": b_id, "title": title, "author": author, "genre": "Self Discovery",
        "cover_url": cover, "public_domain": pd, "fiction": False,
        "chapters": chapters
    })

# 1. The Subtle Art of Not Giving a F*ck (Mark Manson)
add_b("the-subtle-art-of-not-giving-a-fuck", "The Subtle Art of Not Giving a F*ck", "Mark Manson", "https://covers.openlibrary.org/b/id/8231996-M.jpg", False, [
  ch(1, "Don't Try", "True confidence comes from being comfortable with your flaws, not pretending to be flawless.", [
    "Modern consumer culture bombards us with relentless messages commanding us to care about everything.",
    "Care about having a better car, a flatter stomach, whiter teeth, and more exotic vacations.",
    "The Feedback Loop from Hell occurs when you feel anxious about being anxious, or guilty about feeling angry.",
    "Charles Bukowski's tombstone famously reads: 'Don't Try.'",
    "Bukowski became an iconic writer not because he tried to project success, but because he was comfortable being a flawed mess.",
    "You have a limited number of cares to give in this finite life.",
    "If you give cares to every trivial traffic jam, rude comment, or social post, you will squander your peace.",
    "Maturity is the art of reserving your cares exclusively for what is genuinely sacred and important."
  ], [
    ("Care budget is strictly finite", "Giving cares to trivial annoyances drains the emotional bandwidth needed for true values."),
    ("The Feedback Loop from Hell", "Judging your negative emotions creates a vicious cycle of neurotic anxiety."),
    ("Accepting flaws brings peace", "True confidence is not being fearless; it is being comfortable with fear.")
  ], ("The desire for a more positive experience is itself a negative experience. Accepting negative experience is a positive experience.", "rabbit_take"), [
    "When stuck in slow traffic, remind yourself that this is not worthy of spending your finite cares.",
    "Stop beating yourself up for feeling nervous before a presentation; accept the nerves as natural.",
    "Unfollow influencers who make you feel inadequate about your normal, grounded daily life."
  ], [("the-courage-to-be-disliked", 1, "Accepting yourself without needing constant external validation is the foundation of freedom.")]),
  ch(2, "Happiness Is a Problem", "Happiness is not a destination where problems disappear; it is the process of solving good problems.", [
    "Many people labor under the myth that one day they will solve their difficulties and live in perpetual bliss.",
    "In reality, problems never stop; they merely get upgraded or exchanged for better problems.",
    "Going to the gym solves health problems but creates the problem of sore muscles and scheduled time.",
    "Earning more money solves debt problems but creates the problem of tax planning and investment decisions.",
    "Happiness comes from solving problems you genuinely enjoy having.",
    "Do not ask what rewards you want out of life; everyone wants financial freedom and loving romance.",
    "The far more revealing question is: what pain are you willing to endure?",
    "What is the struggle you are willing to navigate day after day? That struggle determines your success."
  ], [
    ("Problems are permanent fixtures", "Life is a continuous series of challenges; true joy is finding problems you enjoy solving."),
    ("Choose your flavor of struggle", "Achievements are defined by the hardships you are willing to tolerate, not the trophies you crave."),
    ("Emotions are biological directional flags", "Pain signals that something needs attention, not that you are defective.")
  ], ("Don't ask what you want to achieve. Ask what pain you are willing to sustain.", "rabbit_take"), [
    "If you want to be a great musician, fall in love with the repetitive pain of practicing boring scales.",
    "If you want an entrepreneurial career, accept the pain of unpredictable revenue and constant uncertainty.",
    "View relationship disagreements as cooperative problems to solve together rather than personal attacks."
  ], [("mans-search-for-meaning", 3, "Meaning arises when we transform unavoidable suffering into deliberate heroic responsibility.")]),
  ch(3, "You Are Not Special", "The tyranny of exceptionalism convinces ordinary people that being average is a failure.", [
    "The self-esteem movement of the late twentieth century taught children that everyone is uniquely extraordinary.",
    "This bred a generation of entitlement: people who feel they deserve special treatment without producing effort.",
    "The vast majority of human life in almost every domain is thoroughly, beautifully average.",
    "Internet media highlights only the top 0.001% of physical beauty, athletic triumph, and billionaire fortunes.",
    "This creates an extreme information diet that makes normal, quiet lives feel like catastrophic failures.",
    "Accepting that you are not special is not defeat; it is profound liberation.",
    "Once you drop the exhausting pressure to be a generational prodigy, you are free to do what you love.",
    "You can enjoy cooking, writing, or gardening simply for the intrinsic joy of doing it."
  ], [
    ("Entitlement breeds toxic fragility", "Expecting rewards without putting in the unglamorous grind creates bitter resentment."),
    ("Media magnifies extreme outliers", "Comparing your everyday life to highlight reels of prodigies distorts normal reality."),
    ("The freedom of being average", "Releasing the demand to be extraordinary frees energy for humble, meaningful craftsmanship.")
  ], ("Accepting your ordinary humanity liberates you to accomplish what you truly love without paralyzing pressure.", "rabbit_take"), [
    "Enjoy playing tennis or soccer on weekends without needing to win local tournaments to validate your hobby.",
    "Recognize that ordinary kindness and loyalty to family are far more noble than chasing viral fame.",
    "Celebrate steady, quiet progress in your coursework rather than expecting effortless perfection."
  ], [("the-courage-to-be-disliked", 6, "Having the courage to be normal frees you from neurotic demands for public distinction.")]),
  ch(4, "The Value of Suffering", "Pain is an evolutionary teacher that reveals the flaws in your values and expectations.", [
    "Lieutenant Hiroo Onoda hid in the Philippine jungle for thirty years after World War II ended, refusing to surrender.",
    "He endured immense starvation, rain, and illness because his value was unconditional loyalty to the Emperor.",
    "When he finally returned to Japan, modern consumer culture felt hollow and meaningless to him.",
    "Suffering is inevitable, but the meaning of your suffering depends on the values you choose to measure it by.",
    "Shitty values include: pleasure, material success, always being right, and staying relentlessly positive.",
    "Good values are reality-based, socially constructive, and immediately controllable, like honesty and curiosity.",
    "When you measure life by good values, painful setbacks become lessons that refine your character.",
    "Choose worthy values, and your suffering transforms into the crucible of genuine wisdom."
  ], [
    ("Suffering is an inevitable signal", "Pain alerts us to gaps between our beliefs and reality; ignoring it worsens the wound."),
    ("Audit your internal metrics", "Superficial values like popularity and wealth generate chronic insecurity and fragile pride."),
    ("Controllable values build resilience", "Choosing values like honesty and humility keeps your peace independent of external luck.")
  ], ("The question is not whether you will suffer, but what you will suffer for.", "rabbit_take"), [
    "Replace the goal of 'being liked by everyone' with the controllable value of 'speaking honestly with kindness.'",
    "When rejected by a company, treat the disappointment as data on which skills need sharpening.",
    "Measure friendships by mutual trust and loyalty rather than shared social prestige."
  ], [("meditations", 3, "Stoic philosophy teaches that events do not hurt us; our opinions about events cause our suffering.")]),
  ch(5, "You Are Always Choosing", "You may not be responsible for what happens to you, but you are always responsible for how you respond.", [
    "Many people confuse responsibility with fault.",
    "If someone drops an abandoned baby on your doorstep, it is not your fault that the baby is there.",
    "However, you are one hundred percent responsible for what you choose to do about the baby on your doorstep.",
    "You cannot control the genes you inherited, the parents who raised you, or sudden accidents.",
    "Yet you are completely responsible for how you interpret those events and what actions you take next.",
    "Victimhood mentality occurs when you surrender responsibility for your life to external forces.",
    "While it brings short-term emotional comfort, blaming others traps you in permanent helplessness.",
    "Taking radical responsibility for your responses returns the steering wheel of your life to your hands."
  ], [
    ("Fault is past; responsibility is present", "Others may have caused the injury, but healing the wound is entirely your responsibility."),
    ("Victimhood surrenders personal power", "Blaming external circumstances keeps you paralyzed in permanent childhood dependence."),
    ("Agency begins with radical ownership", "Claiming responsibility for your mindset restores your ability to shape your future.")
  ], ("You are always, at every single second, choosing what to care about and how to respond.", "rabbit_take"), [
    "Stop blaming your high school teacher for your current math gaps; take ownership and study online tutorials.",
    "When someone treats you unfairly, choose to respond with firm boundaries rather than passive-aggressive sulking.",
    "Accept that your physical health is your personal responsibility regardless of your family's dietary history."
  ], [("mans-search-for-meaning", 1, "The last of human freedoms is the ability to choose one's attitude in any given circumstance.")]),
  ch(6, "You're Wrong About Everything", "Growth is an iterative process of becoming slightly less wrong over the course of a lifetime.", [
    "Certainty is the enemy of intellectual and personal growth.",
    "Instead of trying to find the final, perfect truth, strive to become slightly less wrong every single day.",
    "Our brains are flawed instruments that misremember the past, misjudge the present, and miscalculate the future.",
    "When you cling to the belief that you are completely right, you defend your ego at the cost of reality.",
    "Manson's Law of Avoidance states that the more something threatens your identity, the more you will avoid it.",
    "If you see yourself as an unappreciated genius, you will avoid producing work that could be criticized.",
    "Keep your identity small and fluid: see yourself as an imperfect student constantly learning.",
    "Doubt your own certainties, stay curious, and let experience teach you with humility."
  ], [
    ("Certainty halts personal growth", "Believing you have arrived at absolute truth blinds you to necessary feedback and updates."),
    ("The Law of Avoidance protects ego", "We avoid opportunities that challenge the comfortable stories we tell about ourselves."),
    ("Embrace the beginner's mind", "Remaining a perpetual learner keeps you adaptable and open to unexpected breakthroughs.")
  ], ("We don't go from wrong to right. We go from wrong to slightly less wrong.", "rabbit_take"), [
    "Admit when a colleague's idea is superior to yours and thank them publicly for the insight.",
    "Notice when defensiveness flares in discussions; ask yourself what fragile identity story you are protecting.",
    "Be willing to change your opinion on important topics when presented with sound empirical evidence."
  ], [("thinking-fast-and-slow", 5, "Overconfidence and narrative fallacies trick us into false certainty about complex realities.")])
])

# 2. Man's Search for Meaning (Viktor E. Frankl)
add_b("mans-search-for-meaning", "Man's Search for Meaning", "Viktor E. Frankl", "https://covers.openlibrary.org/b/id/10543682-M.jpg", False, [
  ch(1, "Experiences in a Concentration Camp", "When everything physical is stripped away, human dignity rests in the freedom of one's attitude.", [
    "Viktor Frankl survived Auschwitz and Dachau, enduring the absolute lowest depths of human brutality.",
    "In the camps, prisoners were stripped of their clothes, names, professions, and possessions, reduced to bare numbers.",
    "Under conditions of extreme starvation, typhus, and frostbite, most prisoners succumbed to spiritual apathy.",
    "Yet Frankl observed that even in the camps, a few men walked through the huts comforting others and giving away their last crust of bread.",
    "They proved that everything can be taken from a human being but one thing.",
    "The last of the human freedoms: to choose one's attitude in any given set of circumstances, to choose one's own way.",
    "Even when your physical surroundings are a living nightmare, your inner sovereignty remains inviolate.",
    "No external power on Earth can force you to become bitter or hateful unless you surrender your soul."
  ], [
    ("Inner freedom cannot be stolen", "External circumstances may chain the body, but your choice of character remains free."),
    ("Spiritual life deepens under hardship", "A rich inner intellectual and loving life provides an untouchable sanctuary in dark times."),
    ("Apathy is an internal surrender", "Surrendering your sense of future purpose leads directly to physical and psychological collapse.")
  ], ("Everything can be taken from a man but one thing: the last of the human freedoms.", "rabbit_take"), [
    "When dealing with an unfair teacher or boss, remember that your internal dignity is entirely yours to maintain.",
    "Refuse to let physical fatigue or pain dictate whether you speak with kindness to your family.",
    "Recognize that freedom is not just having endless consumer choices; it is mastering your response to difficulty."
  ], [("meditations", 2, "Marcus Aurelius reminds us that external events touch only the body; the mind governs itself.")]),
  ch(2, "The Meaning of Love", "Love is the ultimate and highest goal to which a human being can aspire.", [
    "During an agonizing pre-dawn march through icy mud, guarded by rifle-wielding soldiers, Frankl found salvation.",
    "A fellow prisoner whispered: 'If our wives could see us now! I hope they are better off.'",
    "In that moment, Frankl thought of his young wife, and his mind was illuminated by an overwhelming truth.",
    "He understood that love is the highest and final horizon of human existence.",
    "The salvation of man is through love and in love.",
    "He did not know if his wife was alive or dead, and in a profound sense, it did not matter.",
    "Her loving presence lived with radiant reality in his soul, transcending the physical brutality of the camp.",
    "Love goes far beyond the physical person of the beloved; it finds its deepest meaning in their spiritual being."
  ], [
    ("Love transcends physical presence", "Loving another human being anchors the soul even across physical separation and death."),
    ("Contemplation of the beloved restores courage", "Memories of love provide an oasis of grace during times of acute suffering."),
    ("Love is an active spiritual orientation", "Caring deeply about another person pulls consciousness out of self-centered despair.")
  ], ("The salvation of man is through love and in love.", "rabbit_take"), [
    "Hold the thought of those you love in your mind when walking into intimidating or stressful exams.",
    "Express deep gratitude to parents, partners, and dear friends while they are here beside you.",
    "Dedicate your daily studies and labor as quiet offerings to support and protect the people you love."
  ], [("gitanjali", 2, "Tagore writes that love is the divine song that weaves human souls into the cosmic tapestry.")]),
  ch(3, "The Meaning of Suffering", "Suffering ceases to be suffering the moment it finds the meaning of a sacrifice.", [
    "If there is a meaning in life at all, then there must be a meaning in suffering.",
    "Suffering is an ineradicable part of human life, even as fate and death.",
    "Without suffering and death, human life cannot be complete.",
    "The way in which a person accepts their fate and all its suffering gives them ample opportunity to add deeper meaning to life.",
    "An elderly general physician fell into severe depression after his wife died of cancer.",
    "Frankl asked him: 'What would have happened if you had died first, and your wife had survived you?'",
    "The doctor gasped: 'It would have been terrible for her; she would have suffered immensely!'",
    "Frankl replied: 'You have spared her this suffering, at the price of surviving and mourning her now.'",
    "The doctor shook Frankl's hand and walked out in peace: his suffering had found meaning as an act of loving sacrifice."
  ], [
    ("Suffering can be given purpose", "When pain serves a noble duty, sacrifice, or lesson, it ceases to feel like senseless torture."),
    ("Courage under unavoidable trial", "How you carry an unfair burden reveals the ultimate depth of your moral character."),
    ("Do not search for suffering, but honor it", "Unnecessary pain is masochism; unavoidable pain is an opportunity to prove your humanity.")
  ], ("In some ways suffering ceases to be suffering at the moment it finds a meaning, such as the meaning of a sacrifice.", "rabbit_take"), [
    "Reframe long hours of hard study as a loving sacrifice to build a secure future for your family.",
    "When caring for a sick relative, view the sleepless nights as an honor of service rather than an imposition.",
    "Stand tall during seasons of grief, knowing that your tears honor the beauty of what you were blessed to love."
  ], [("the-subtle-art-of-not-giving-a-fuck", 4, "Choosing worthy values transforms unavoidable suffering into meaningful growth.")]),
  ch(4, "Logotherapy in a Nutshell", "Man's primary motivational force is not pleasure or power, but the striving to find meaning.", [
    "Freud believed humans are driven primarily by the 'will to pleasure.'",
    "Adler argued that humans are driven by the 'will to power' and status.",
    "Frankl's logotherapy demonstrates that human beings are driven primarily by the 'will to meaning.'",
    "We can discover meaning in life in three distinct ways: through creating a work, experiencing something, or our attitude toward suffering.",
    "First, by creating a work or doing a deed: writing a book, building a home, serving a patient.",
    "Second, by experiencing something or encountering someone: absorbing nature's beauty or loving a person.",
    "Third, by the attitude we take toward unavoidable suffering.",
    "Life asks something of each human being, and we answer not through words, but through responsible action."
  ], [
    ("The Will to Meaning is primal", "Humans can endure almost any hardship if they believe their existence serves a purpose."),
    ("Three paths to authentic meaning", "Creating works, experiencing love and beauty, and bearing trials with courage."),
    ("Life questions us, not vice versa", "We do not ask what life owes us; life demands our responsible answer each morning.")
  ], ("Man does not simply exist but always decides what his existence will be, what he will become in the next moment.", "rabbit_take"), [
    "Write down three specific responsibilities—to a creative project, a friend, or a duty—that only you can fulfill.",
    "When feeling lost or unmotivated, ask what this specific day is demanding of your character.",
    "Find meaning in small everyday deeds: cooking a nourishing meal, solving a work problem, or smiling at a stranger."
  ], [("flow", 1, "Directing consciousness toward clear, meaningful creative responsibilities produces optimal experience.")]),
  ch(5, "The Existential Vacuum", "Boredom and purposelessness are the modern plagues that wealth and leisure cannot cure.", [
    "In the twentieth century, human instincts were weakened by civilization, and traditional dogmas lost their grip.",
    "As a result, humanity was plunged into an existential vacuum: a state of profound, hollow meaninglessness.",
    "The existential vacuum manifests primarily in the condition of boredom.",
    "Sunday neurosis describes the depression that settles in when people have no work deadlines to distract them.",
    "To escape this void, people turn to vicarious thrills: consumerism, alcohol, compulsive pleasure, and tribal rage.",
    "No amount of wealth, entertainment, or material luxury can fill the emptiness of an unexamined life.",
    "The cure is not more entertainment, but discovering a personal responsibility that demands your dedicated effort.",
    "Do not wait for meaning to strike like lightning; build it through daily service to something greater than yourself."
  ], [
    ("Boredom reveals the existential void", "Empty leisure without purpose exposes the lack of an authentic guiding compass."),
    ("Escapism fails to heal the soul", "Compulsive entertainment and consumer shopping merely mask spiritual emptiness temporarily."),
    ("Responsibility cures nihilism", "Committing to a calling and serving others fills the vacuum with durable fulfillment.")
  ], ("When a person can't find a deep sense of meaning, they distract themselves with pleasure.", "rabbit_take"), [
    "Notice when weekend boredom triggers endless scrolling; replace it with volunteering or creative projects.",
    "Do not seek a life of zero responsibility; humans thrive under the healthy tension of noble obligations.",
    "Find an initiative in your local school or town that needs dedicated hands and commit your time."
  ], [("deep-work", 3, "Devoting attention to deep craftsmanship anchors the mind and banishes existential drift.")]),
  ch(6, "Tragic Optimism", "Saying yes to life in spite of everything: turning pain into human achievement and guilt into change.", [
    "Tragic optimism means that one is, and remains, optimistic in spite of the 'tragic triad.'",
    "The tragic triad consists of pain, guilt, and death: the unavoidable realities of mortal existence.",
    "Pain offers the opportunity to turn suffering into human achievement and heroic endurance.",
    "Guilt offers the opportunity to change oneself for the better and repair moral errors.",
    "Death and the transitoriness of life offer an incentive to take responsible, decisive action today.",
    "If life were immortal and infinite, every decision could be postponed forever without consequence.",
    "Because your days are numbered and irreversible, every single hour is a precious, unrepeatable decision.",
    "Live as if you were living already for the second time and as if you had acted the first time as wrongly as you are about to act now."
  ], [
    ("Optimism in the face of tragedy", "Affirming life despite pain, guilt, and mortality is the supreme triumph of human character."),
    ("Transitoriness makes life precious", "The finality of death gives urgent, beautiful weight to every choice you make today."),
    ("The categorical imperative of logotherapy", "Live each moment as if it were a second chance to correct past mistakes.")
  ], ("Live as if you were living already for the second time and as if you had acted the first time as wrongly as you are about to act now.", "rabbit_take"), [
    "Treat today as your second chance: if you squandered yesterday, wake up and act with wisdom now.",
    "Acknowledge past mistakes without shame, using healthy guilt to fuel immediate positive restitution.",
    "Remind yourself that life's finite length makes every conversation with loved ones infinitely sacred."
  ], [("meditations", 7, "Remember that you could depart from life right now; let that determine what you do and think.")])
])

print("gen_hero_self.py: added Subtle Art & Man's Search for Meaning.")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)
