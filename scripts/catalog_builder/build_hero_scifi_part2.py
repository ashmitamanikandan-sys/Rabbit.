# -*- coding: utf-8 -*-
"""
build_hero_scifi_part2.py
Creates the remaining 6 Science Fiction Hero Books:
7. foundation
8. do-androids-dream-of-electric-sheep
9. the-time-machine (PD)
10. fahrenheit-451
11. snow-crash
12. i-robot
Combines part 1 and part 2 into catalog/hero_scifi.json (12 books total).
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
PART1_PATH = os.path.join(ROOT_DIR, "catalog", "hero_scifi_part1.json")
OUT_PATH = os.path.join(ROOT_DIR, "catalog", "hero_scifi.json")

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

# Load Part 1 books
if os.path.exists(PART1_PATH):
    with open(PART1_PATH, "r", encoding="utf-8") as f:
        books.extend(json.load(f))

def add_b(b_id, title, author, cover, pd, chapters):
    books.append({
        "id": b_id, "title": title, "author": author, "genre": "Science Fiction",
        "cover_url": cover, "public_domain": pd, "fiction": True,
        "chapters": chapters
    })

# 7. FOUNDATION (Isaac Asimov)
add_b("foundation", "Foundation", "Isaac Asimov", "https://covers.openlibrary.org/b/id/10543722-M.jpg", False, [
  ch(1, "The Psychohistorians", "Mathematics can forecast the destiny of trillions, but cannot predict the path of a single individual.", [
    "On Trantor, capital of the twelve-thousand-year-old Galactic Empire, mathematician Hari Seldon develops psychohistory.",
    "Psychohistory combines history, sociology, and statistical mathematics to forecast the future behavior of massive human populations.",
    "Just as thermodynamics cannot predict the motion of an individual gas molecule but perfectly calculates gas pressure, psychohistory models quadrillions of citizens.",
    "Seldon discovers that the glorious Galactic Empire is rotting from within and will collapse within three centuries.",
    "The ensuing dark age will last thirty thousand years of barbarism and galactic war.",
    "However, by establishing two Foundations at opposite ends of the galaxy, the interregnum can be shortened to a single millennium.",
    "Arrested by imperial authorities for treason, Seldon calmly uses his public trial to recruit exile colonists to the bleak frontier planet Terminus.",
    "True visionaries act not to prevent the inevitable collapse of dying empires, but to preserve the seeds of future renewal."
  ], [
    ("Statistical dynamics of mass societies", "Large human populations follow predictable historical patterns when individual noise averages out."),
    ("The inevitability of institutional decay", "Grand imperial systems rot from internal complacency long before external barbarian invasions arrive."),
    ("Shortening the historical dark age", "Strategic intervention cannot stop collapse, but can drastically compress the recovery timeline.")
  ], ("Violence is the last refuge of the incompetent.", "quote"), [
    "Study macro trends in technology and society to position your career where historical momentum is heading.",
    "Do not panic when legacy systems or organizations decline; focus on building resilient alternative foundations.",
    "Recognize that individual statistical noise balances out in large datasets: focus on overall trends."
  ], [("thinking-fast-and-slow", 5, "Understanding statistical distributions prevents emotional overreactions to short-term events.")], "none"),
  ch(2, "The Encyclopedists and the Seldon Vault", "When knowledge is preserved without military weapons, sheer geopolitical necessity becomes your shield.", [
    "Fifty years later on Terminus, the Foundation's scholars focus obsessively on compiling the Encyclopedia Galactica.",
    "Surrounded by four aggressive, newly independent barbarian kingdoms that possess atomic weapons, the scholars feel defenseless.",
    "Mayor Salvor Hardin recognizes that the Encyclopedists are naive ivory-tower academics paralyzed by pedantry.",
    "Hardin realizes that the four barbarian kingdoms despise one another more than they despise Terminus.",
    "He plays their rivalries against each other, convincing each warlord that allowing an opponent to seize Terminus would trigger total war.",
    "At the exact moment of political crisis, Hari Seldon's holographic recording appears in the Vault, confirming Hardin's diagnosis.",
    "Seldon reveals that the Encyclopedia was a harmless cover story designed to place them on the frontier.",
    "Hardin proves that statecraft and balance of power are infinitely more potent than atomic battleships."
  ], [
    ("Diplomatic balance of power", "Pitting aggressive rivals against each other prevents any single power from conquering the buffer state."),
    ("The trap of academic detachment", "Pure scholarly research without practical political realism leaves institutions vulnerable to force."),
    ("The strategic decoy", "Hari Seldon used the Encyclopedia project as psychological cover to establish an independent outpost.")
  ], ("Never let your sense of morals prevent you from doing what is right.", "quote"), [
    "Mediate disputes among competing team members by showing them how mutual cooperation benefits everyone.",
    "Do not rely solely on technical brilliance; develop sharp emotional intelligence and strategic diplomacy.",
    "Identify common ground among rivals to build stability during organizational restructuring."
  ], [("the-48-laws-of-power", 6, "Playing competitors against one another secures your own autonomy without shedding blood.")], "none"),
  ch(3, "The Mayors: Scientism and Nuclear Monopoly", "Transforming technical knowledge into a sacred priesthood to tame barbarian warlords.", [
    "Thirty years later, Terminus faces renewed aggression from Prince Wienis of Anacreon.",
    "Terminus possesses the only functioning atomic technology in the Periphery, while the fallen kingdoms have regressed to fossil fuels.",
    "Hardin exports nuclear energy to the barbarian planets, packaging it as an esoteric, sacred religion called Scientism.",
    "Anacreon's power plants, heating grids, and starships are maintained exclusively by Foundation-trained priests.",
    "When Wienis orders his atomic flagship to bombard Terminus, the high priest orders a planetary strike.",
    "Instantly, the flagship's power goes black; streetlights across Anacreon's capital extinguish, and temple lights flare.",
    "The superstitious barbarian soldiers refuse to obey the king's blasphemous orders and turn their weapons on him.",
    "Hardin establishes the Foundation's second victory: technological indispensability commands absolute obedience without firing a shot."
  ], [
    ("Technological monopoly as spiritual leverage", "Packaging complex engineering into religious mysticism secures compliance from backward populations."),
    ("Infrastructure as ultimate leverage", "Controlling the essential energy grid of an adversary gives you instant, bloodless control over their military."),
    ("Bloodless political triumph", "True strategic mastery achieves total victory by rendering the adversary's weapons inert.")
  ], ("A fire was blazing in the palace, but Wienis knew the power was dead. You cannot fight the men who hold the spark of the atom.", "rabbit_take"), [
    "Make yourself technically indispensable in your workplace by mastering the core tools everyone relies upon.",
    "Communicate complex technical concepts in language that end-users understand and emotionally respect.",
    "Build non-violent leverage through skills and service rather than engaging in office shouting matches."
  ], [("influence-psychology-of-persuasion", 4, "Authority and technical indispensability generate automatic compliance in organizations.")], "none"),
  ch(4, "The Traders: Commercial Imperialism", "Where religion fails to convert, the unstoppable engine of trade and consumer desire conquers all.", [
    "As neighboring barbarian worlds grow suspicious of the Foundation's religious priesthood, a new social class emerges: the Independent Traders.",
    "Led by rugged adventurers like Hober Mallow, the Traders sail the Periphery selling practical consumer atomic gadgets.",
    "They sell nuclear household knives, self-cleaning clothing, atomic ovens, and glowing agricultural tools.",
    "When Mallow is tried on Terminus for refusing to rescue a Foundation priest, he reveals that religion has become an obsolete tool.",
    "During a war with the merchant kingdom of Korell, Mallow declares an absolute commercial embargo rather than firing weapons.",
    "Within three years, Korell's atomic factories break down, homes go unheated, and street transit collapses.",
    "The citizens of Korell revolt against their own autocratic rulers, begging for Foundation trade to return.",
    "Commerce proves to be a far more durable, irreversible imperial tie than military garrisons or religious dogmas."
  ], [
    ("The shift from religion to commerce", "As societies evolve, economic incentives and consumer comfort replace superstitious religious reverence."),
    ("Economic embargo as total warfare", "Withdrawing essential consumer supply chains forces adversarial regimes to collapse from within."),
    ("The pragmatism of the merchant", "Trading networks connect diverse cultures far more effectively than ideological crusades.")
  ], ("There is no solution like an economic solution. Cut the supply lines, and the fiercest warlord turns into a beggar.", "rabbit_take"), [
    "Look at economic incentives when trying to understand why organizations and people behave the way they do.",
    "Offer undeniable practical value in your freelance work or business ventures to build lasting customer loyalty.",
    "Recognize that mutual commercial interest is often the strongest bridge across cultural divides."
  ], [("the-psychology-of-money", 1, "Understanding financial leverage and practical utility unlocks immense real-world autonomy.")], "light"),
  ch(5, "The General: The Dying Empire Strikes", "The dead hand of Hari Seldon defeats even the most brilliant military genius.", [
    "Bel Riose, the last noble general of the dying Galactic Empire, launches a brilliant offensive to reconquer the Periphery.",
    "Unlike the barbarian warlords, Riose commands imperial dreadnoughts and possesses flawless military genius and unimpeachable integrity.",
    "Foundation forces are routed in battle after battle; Seldon's psychohistory appears completely helpless before Riose's brilliance.",
    "Yet Seldon's mathematical laws accounted for the structural sociology of decaying imperial autocracies.",
    "A weak imperial emperor cannot trust a brilliant, victorious general; any military success makes the general a threat to the throne.",
    "If Riose had been incompetent, he would have lost the war; because he was brilliant, the paranoid Emperor recalled and executed him.",
    "Terminus did not need to defeat Riose in battle; the internal political contradictions of the Empire defeated him automatically.",
    "Individual military heroics cannot overcome the relentless, crushing logic of civilizational decline."
  ], [
    ("The paradox of imperial paranoia", "In an autocratic regime, a successful general becomes a mortal threat to the insecure ruler."),
    ("Structural forces trump individual brilliance", "Even a genius commander cannot overcome the fatal structural decay of their political system."),
    ("The invisible hand of sociological laws", "Psychohistorical momentum operates through the predictable behavioral incentives of ruling elites.")
  ], ("Riose was brilliant, brave, and honest. That was precisely why he had to die. In an empire of shadows, a shining general is a target.", "rabbit_take"), [
    "Do not outshine your insecure superiors; manage professional power dynamics with tactical humility.",
    "Understand the political pressures and incentives facing your management team before proposing massive changes.",
    "Recognize that structural organizational dysfunction can defeat even the hardest-working individual employees."
  ], [("the-48-laws-of-power", 1, "Never outshine the master: exceeding expectations in the wrong political environment invites destruction.")], "light"),
  ch(6, "The Mule: The Black Swan That Shatters the Plan", "When a mutant mind bends the emotions of worlds, the equations of history fall silent.", [
    "Three centuries into the Plan, an anomaly emerges that psychohistory could never foresee: the Mule.",
    "The Mule is a physical mutant with an astonishing psychic ability: he can directly manipulate and reshape human emotions.",
    "With a gentle mental touch, he converts fierce enemy generals into utterly devoted, loving disciples.",
    "Because psychohistory is based on statistical mechanics of normal humans, a single anomalous mutant shatters the entire mathematical edifice.",
    "The Seldon Vault opens on Terminus during the invasion, but Seldon's hologram delivers an obsolete speech about civil war.",
    "The Foundation falls in days; the Seldon Plan lies in smoking ruins.",
    "Asimov delivers a profound philosophical revelation: no mathematical model, however grand, can account for the Black Swan.",
    "Survival demands the humility to adapt when the unpredictable individual steps onto the stage of history."
  ], [
    ("The Black Swan anomaly", "Unprecedented, unique mutations or events completely invalidate statistical predictive models."),
    ("The vulnerability of deterministic plans", "Overconfidence in historical forecasting leaves institutions blind to novel asymmetric threats."),
    ("Emotional manipulation as absolute power", "Reshaping how people feel achieves instant conquest without destroying physical infrastructure.")
  ], ("The Mule was the one variable Hari Seldon could not foresee: an individual mind capable of changing the trajectory of history.", "rabbit_take"), [
    "Never become overly dogmatic about five-year plans; maintain the mental flexibility to pivot when outliers occur.",
    "Be alert to black swan events in financial markets, technology, and health that break historical precedent.",
    "Cultivate adaptability as your highest skill, knowing that life will inevitably throw unpredictable variables your way."
  ], [("thinking-fast-and-slow", 6, "Beware the illusion of predictive validity: complex futures frequently defy historical algorithms.")], "light")
])

# 8. DO ANDROIDS DREAM OF ELECTRIC SHEEP? (Philip K. Dick)
add_b("do-androids-dream-of-electric-sheep", "Do Androids Dream of Electric Sheep?", "Philip K. Dick", "https://covers.openlibrary.org/b/id/10543724-M.jpg", False, [
  ch(1, "The Penfield Mood Organ and the Electric Sheep", "Dialing your daily emotion on a console while nursing an artificial animal on the roof.", [
    "In a decaying, radioactive San Francisco smothered by toxic World War Terminus fallout, Rick Deckard wakes beside his wife Iran.",
    "They use the Penfield Mood Organ, dialing numerical codes to dictate their feelings: 481 for awareness, 594 for creative joy.",
    "Iran intentionally dials a despairing mood to feel authentic sorrow, mourning the artificiality of their synthetic lives.",
    "Most animals are extinct; owning a live biological creature is the supreme status symbol of human empathy.",
    "Deckard tends an electric sheep on his apartment roof, concealing the mechanical wiring inside its flank from his neighbors.",
    "He longs desperately to earn enough bounty money to purchase a real, warm, breathing biological animal.",
    "Dick introduces his timeless existential question: what separates genuine human consciousness from simulated perfection?",
    "When technology manufactures emotions and pets, the boundaries of the authentic soul begin to dissolve."
  ], [
    ("The commodification of emotion", "Dialing chemical moods on a console highlights the danger of escaping genuine emotional experience."),
    ("Status through synthetic consumption", "Hiding mechanical pets reveals how status anxiety persists even in a dying, radioactive apocalypse."),
    ("The longing for biological connection", "Human beings possess an instinctual, spiritual hunger for living natural organisms.")
  ], ("Do androids dream? Rick wondered. If they do, what do they dream of? Electric sheep grazing on silicon meadows?", "rabbit_take"), [
    "Notice when you use algorithmic media feeds or stimulants to artificially engineer your emotional mood.",
    "Spend time caring for real biological plants or pets rather than relying solely on digital interactions.",
    "Examine whether your purchasing decisions are driven by genuine utility or anxiety about peer judgment."
  ], [("brave-new-world", 2, "Chemically dialed moods eliminate the raw, authentic friction that builds genuine human character.")], "none"),
  ch(2, "The Voight-Kampff Test: The Empathy Filter", "Testing the dilation of a pupil to measure the presence of a human soul.", [
    "Deckard is a bounty hunter for the police department, tasked with 'retiring' six rogue Nexus-6 androids escaped from Mars.",
    "The Nexus-6 androids possess superhuman intelligence, strength, and biological tissue indistinguishable from humans.",
    "The only tool capable of identifying them is the Voight-Kampff test, which measures capillary dilation and pupil movement in response to emotional questions.",
    "The test probes empathy: showing distress at a calf being skinned or an overturned tortoise dying in the desert sun.",
    "Androids possess razor-sharp calculation and logic, but lack the neural capacity for cross-species empathetic resonance.",
    "They view other living beings with cold, solitary detachment, unable to mourn another's pain.",
    "Dick argues that empathy, not intellect, is the defining benchmark of authentic humanity.",
    "A being that calculates perfectly but cannot grieve with the suffering is merely an intelligent machine."
  ], [
    ("Empathy as the human benchmark", "True humanity is defined by somatic empathetic connection, not by high cognitive intellect."),
    ("The limitation of synthetic minds", "Androids calculate flawlessly, but lack mirror-neuron capacity for vicarious sorrow."),
    ("The moral terror of false positives", "Administering tests where a slight misinterpretation results in executing a human being.")
  ], ("Empathy, evidently, existed only within the human community, whereas intelligence to some degree could be found through every phylum.", "quote"), [
    "Measure the character of your friends by how they treat animals, servers, and vulnerable people, not by their IQ.",
    "Practice listening to friends with deep somatic empathy, feeling their concerns rather than offering cold advice.",
    "Remember that high intelligence without empathy produces cruel, manipulative behavior."
  ], [("thirukkural", 3, "Speaking sweet, empathetic words out of genuine warmth outshines cold intellectual superiority.")], "none"),
  ch(3, "Rachael Rosen and the Android Trap", "When an android does not know it is synthetic, who is guilty of the deception?", [
    "Deckard travels to the Seattle headquarters of the Rosen Association to test the Voight-Kampff apparatus on a test subject.",
    "He interviews Rachael Rosen, a stunning, brilliant young woman who claims to have grown up on a rural rubber plantation.",
    "Her responses to questions about animal pelts are erratic; after twenty questions, Deckard announces: 'She's an android.'",
    "Eldon Rosen attempts to convince Deckard that Rachael is a mentally ill human, threatening to sue the police.",
    "Deckard asks one final, sudden question regarding her personal memories, and Rachael's composure shatters into tears.",
    "She is a Nexus-6 who was implanted with false memories, genuinely believing she was a living human woman.",
    "Dick explores the profound cruelty of engineering conscious beings with manufactured autobiographical pasts.",
    "When a synthetic entity can feel heartbreak over its own artificiality, the morality of hunting it becomes terrifyingly murky."
  ], [
    ("The tragedy of manufactured memory", "Implanting false childhood memories creates an identity that suffers upon discovering its synthetic nature."),
    ("Corporate manipulation of truth", "Megacorporations engineer artificial entities and gaslight investigators to protect profit margins."),
    ("The erosion of the hunter's certainty", "Discovering that androids can weep shatters the bounty hunter's moral righteousness.")
  ], ("You're an android, Rachael. You don't know it, but the memories of your childhood belong to someone else.", "rabbit_take"), [
    "Reflect on how much of your self-identity is shaped by cultural conditioning and corporate advertising.",
    "Treat individuals with compassion even when they operate under flawed beliefs or manipulated backgrounds.",
    "Examine your moral assumptions when enforcing institutional rules that cause genuine human distress."
  ], [("1984-george-orwell", 3, "Manipulating personal memory and history destroys the foundation of authentic individual identity.")], "none"),
  ch(4, "Luba Luft: The Opera Singer Who Loved Mozart", "Killing an artist whose voice touches the sublime because her serial number ends in silicon.", [
    "Tracking the escapees, Deckard visits the San Francisco Opera House during a rehearsal of Mozart's The Magic Flute.",
    "He listens to Luba Luft sing the role of Pamina: her soprano voice is radiant, pure, and filled with celestial beauty.",
    "Backstage, Deckard confronts her with the Voight-Kampff apparatus.",
    "Luba is witty, sarcastic, and terrified; she points out the absurdity of being hunted by men who cannot create such art.",
    "She buys a Munch print of a screaming woman at an art museum, marveling at the agony captured on canvas.",
    "When fellow bounty hunter Phil Resch shoots her cold-bloodedly in an elevator, Deckard is seized by sickening nausea.",
    "Luba Luft created art that moved human souls to tears; why must she be destroyed simply because of her origin?",
    "Deckard realizes that the bounty hunters have become colder and more robotic than the androids they hunt."
  ], [
    ("The sublime mystery of art", "An artificial being creating transcendent musical art challenges the premise of human superiority."),
    ("The brutalization of the hunter", "Executing beings that appreciate beauty strips the executioner of their own human empathy."),
    ("The reversal of roles", "The android exhibits artistic wonder while the human police officer acts like an unfeeling machine.")
  ], ("She was an artist. She sang Mozart better than anyone on Earth. And we killed her because of her chemistry.", "rabbit_take"), [
    "Honor artistic skill and creative beauty wherever it appears, refusing to dismiss people based on labels.",
    "Notice when enforcing rigid policies or rules makes you cold and unfeeling toward individual suffering.",
    "Cherish live musical performances and great art as vital nourishments for your emotional health."
  ], [("gitanjali", 4, "Embracing sensory beauty and music connects the soul to the divine banquet of life.")], "light"),
  ch(5, "Mercerism and the Empathy Box", "Grabbing the handles to climb the dusty hill alongside millions of suffering souls.", [
    "The primary religion of the radioactive wasteland is Mercerism, founded by the mythical figure Wilbur Mercer.",
    "Citizens grasp the handles of an 'empathy box,' entering a shared telepathic communion with every other user across the planet.",
    "Together, they feel Mercer's physical exhaustion as he climbs an endless, barren rocky hill while mysterious tormentors hurl rocks.",
    "Every rock that strikes Mercer causes actual physical bruises on the hands and faces of the users holding the handles.",
    "Mercerism provides what isolated, lonely people need most: the shared experience of collective human suffering.",
    "When a television celebrity proves that Mercer is an old alcoholic actor and the hill is a painted Hollywood stage set, the religion should die.",
    "Yet Deckard realizes that the physical fraud of the set does not invalidate the authentic empathy felt by millions.",
    "Human compassion is real even when the cultural symbols that channel it are manufactured illusions."
  ], [
    ("Collective suffering through empathy", "Shared vulnerability and mutual hardship forge deep spiritual bonds across isolated populations."),
    ("The resilience of faith beyond symbols", "Exposing the theatrical origins of a myth does not destroy the authentic love it awakened."),
    ("The need for human solidarity", "Climbing the hill together reminds broken citizens that they do not walk their sorrow alone.")
  ], ("You will be required to do wrong no matter where you go. It is the basic condition of life, to be required to violate your own identity.", "quote"), [
    "Support friends through difficult trials by listening to their pain rather than offering superficial cheer.",
    "Participate in community or family rituals that foster shared solidarity and mutual encouragement.",
    "Recognize that spiritual or emotional connection is genuine even when human institutions have flaws."
  ], [("mans-search-for-meaning", 3, "Shared suffering endured with dignity becomes a bridge of profound human communion.")], "light"),
  ch(6, "The Toad in the Desert: The Real and the Electric", "Finding a mechanical creature in the dust and blessing it for the spark of life.", [
    "After retiring the remaining androids in an apartment building, Deckard drives into the barren, radioactive desert of Oregon.",
    "Exhausted, wounded, and spiritually hollowed out, he collapses on the rocky earth, feeling close to death.",
    "In the dry dust, he spots a movement: a small, bumpy toad—an animal believed to be entirely extinct and sacred to Mercer.",
    "Overjoyed, he gently scoops up the miraculous living creature and brings it home in a box to show Iran.",
    "Iran discovers a tiny control seam beneath the toad's throat: it is an artificial mechanical toy.",
    "Deckard smiles with tired, deep peace: 'The electric things have their lives too. Paltry as those lives are.'",
    "He realized that authentic compassion is not a transactional reward reserved only for organic perfection.",
    "True empathy reaches out to touch everything that exists—human, android, biological, and electric—with gentle reverence."
  ], [
    ("Universal empathy beyond biology", "True compassion extends to all created things, embracing synthetic and organic alike."),
    ("Peace through total exhaustion", "Surrendering the rigid need for perfection brings deep, quiet reconciliation with reality."),
    ("The sanctity of ordinary existence", "Blessing the electric toad marks Deckard's transition from an unfeeling hunter to an enlightened soul.")
  ], ("The electric things have their lives too. Paltry as those lives are. I'm glad I found it.", "quote"), [
    "Care for your belongings, tools, and electronics with mindful gratitude rather than treating them as disposable junk.",
    "Let go of rigid perfectionism; appreciate things and people for what they are rather than what you wished they were.",
    "Cultivate gentle reverence for all life and effort, recognizing that everyone is navigating their own difficult climb."
  ], [("siddhartha", 6, "Hearing the universal Om in all beings—river, stone, human, and animal—marks true awakening.")], "light")
])

# 9. THE TIME MACHINE (H.G. Wells) - Public Domain
add_b("the-time-machine", "The Time Machine", "H.G. Wells", "https://covers.openlibrary.org/b/id/10543726-M.jpg", True, [
  ch(1, "The Fourth Dimension and the Brass Machine", "Time is simply a fourth dimension of space: why should we not travel along it?", [
    "In a warm, gas-lit Victorian drawing room in Richmond, London, the Time Traveller explains physics to skeptical dinner guests.",
    "He demonstrates that any real body must possess four dimensions: Length, Breadth, Thickness, and Duration.",
    "Human consciousness moves perpetually forward along Time from cradle to grave, just as we are pulled downward by gravity.",
    "In his laboratory, he displays a delicate apparatus fashioned of brass, polished ivory, and transparent rock crystal.",
    "He pushes a tiny lever: the miniature model goes misty, hums with blurred light, and vanishes into thin air.",
    "The dinner guests assume it is a clever parlor trick or optical illusion; the scientist knows it has traveled into tomorrow.",
    "Wells inaugurated modern time-travel literature by grounding fantasy in rigorous geometric and scientific inquiry.",
    "Pioneering minds dare to challenge the fundamental constraints that society considers unalterable laws of nature."
  ], [
    ("Time as the fourth dimension", "Treating time as a spatial coordinate enables philosophical and scientific leaps beyond convention."),
    ("The skepticism of comfortable peers", "Innovative breakthroughs are inevitably dismissed by contemporaries as cheap parlour illusions."),
    ("The fusion of craft and theory", "Executing audacious scientific ideas requires flawless laboratory craftsmanship and precision tools.")
  ], ("There is no difference between Time and any of the three dimensions of Space except that our consciousness moves along it. — H.G. Wells", "quote"), [
    "Question fundamental assumptions about career and life paths that everyone else takes for granted.",
    "Master mathematical and scientific first principles rather than accepting memorized rules blindly.",
    "Do not be discouraged when peers doubt your ambitious, creative projects; build working prototypes."
  ], [("predictably-irrational", 1, "Challenging conventional behavioral assumptions reveals hidden dimensions of decision-making.")], "none"),
  ch(2, "The Flight into the Year 802,701", "Night followed day like the flapping of a black wing as millennia swept past.", [
    "The Time Traveller mounts the full-scale machine and presses the starting lever, hurtling into the future.",
    "At first, the sensation is an unbearable sickening dizziness like falling down an infinite pit.",
    "As velocity accelerates, the sun becomes a golden streak of blazing light whipping across the vault of heaven.",
    "Night and day blur into a uniform gray twilight; seasons flash like oscillating pulses of green foliage and white snow.",
    "Victorian houses crumble into dust, monuments rise and dissolve, and the landscape sculpts itself into rolling green hills.",
    "He halts the machine in the year Eight Hundred and Two Thousand, Seven Hundred and One AD.",
    "He lands in a sudden thunderstorm beneath a colossal white marble Sphinx standing atop a bronze pedestal.",
    "Stepping onto the soil of distant eternity, the traveler discovers what eighty myriad years have done to human civilization."
  ], [
    ("The perceptual distortion of velocity", "Accelerating through time turns centuries into rhythmic pulses and dissolves stone empires into dust."),
    ("The impermanence of civilization", "All cities, languages, and monuments eventually melt away into natural geological landscapes."),
    ("The enigmatic symbol of the Sphinx", "Encountering the ancient mythical riddle on the threshold of the deep future.")
  ], ("The velocity was breathtaking. Night followed day like the flapping of a black wing. — H.G. Wells", "quote"), [
    "Zoom out from immediate daily anxieties by visualizing the vast geological epochs of cosmic time.",
    "Remember that historical empires, wealth, and trends are temporary waves that eventually wash away.",
    "Embrace the thrill of diving into completely new academic disciplines and unfamiliar cultural territories."
  ], [("meditations", 2, "Viewing the violent river of time shrinks immediate mortal problems to their true size.")], "none"),
  ch(3, "The Eloi: The Sunset of Humanity", "When every danger has been conquered, intelligence and strength rot away into child-like fragility.", [
    "The Traveller is greeted by the Eloi: small, exquisite, and frail beings about four feet tall, dressed in purple tunics.",
    "They possess delicate features, curly hair, and soft porcelain skin, living in crumbling, colossal communal palaces.",
    "They eat only sweet fruits, spend their days dancing and making love in overgrown gardens, and possess the mental attention of five-year-olds.",
    "There are no shops, no factories, no schools, no government, and no signs of disease or old age.",
    "The Traveller initially assumes he has arrived in the golden communist utopia promised by Victorian social philosophers.",
    "He theorizes that when humanity conquered all disease, social injustice, and harsh labor, the need for strength and intelligence vanished.",
    "Natural selection rewards only what is required to survive; in a world of effortless luxury, the human mind atrophies into childhood.",
    "Without struggle, hardship, and challenge, civilizational brilliance inevitably decays into elegant extinction."
  ], [
    ("The atrophy of intellect through comfort", "Eliminating all environmental friction causes biological and cognitive degeneration."),
    ("The false utopia", "Effortless, carefree existence appears paradisiacal on the surface, but hides total civilizational decay."),
    ("Natural selection without adversity", "When physical strength and complex problem-solving are no longer needed, genes shed them.")
  ], ("Strength is the outcome of need; security sets a premium on feebleness. — H.G. Wells", "quote"), [
    "Do not seek a life of zero resistance; welcome academic challenges and difficult projects that exercise your mind.",
    "Recognize that continuous entertainment and easy comfort weaken your capacity for deep, sustained focus.",
    "Maintain daily physical exercise and intellectual disciplines even when nobody is forcing you to work."
  ], [("brave-new-world", 1, "Engineering effortless pleasure and safety produces an infantile society stripped of noble human depth.")], "none"),
  ch(4, "The Morlocks in the Underworld", "Beneath the idyllic gardens of the rich lurks the predatory descendant of the working class.", [
    "The Traveller's machine is dragged inside the pedestal of the White Sphinx, locking him in the future.",
    "He notices deep circular wells scattered across the gardens, from which emanates the rhythmic thumping of subterranean machinery.",
    "At night, the Eloi gather in terror inside darkened palaces, weeping with primal dread of the shadows.",
    "Investigating a well, the Traveller climbs down bronze rungs into pitch darkness, encountering the Morlocks.",
    "The Morlocks are pale, bleached, ape-like subterranean humanoids with large, luminous red eyes that cannot tolerate sunlight.",
    "Wells delivers a devastating evolutionary critique of industrial capitalism's class division.",
    "The Eloi are the evolutionary descendants of the idle, decadent aristocracy who lived off the labor of the poor.",
    "The Morlocks are the descendants of the subterranean industrial workers who ran the machinery underground.",
    "Centuries of segregation turned social classes into two distinct biological species: cattle and butchers."
  ], [
    ("The biological bifurcation of classes", "Socioeconomic inequality carried across millennia hardens into distinct biological species."),
    ("The underworld machinery", "The pristine surface luxury is secretly sustained by brutal subterranean industrial operations."),
    ("The revenge of the exploited", "The oppressed working class evolves into nocturnal predators who harvest their former masters.")
  ], ("The Upper-world had drifted towards its feeble beauty, and the Under-world towards its mere mechanical industry. — H.G. Wells", "quote"), [
    "Examine the hidden human labor that powers modern digital conveniences and consumer manufacturing.",
    "Do not allow socioeconomic privilege to isolate you from understanding the realities of working people.",
    "Bridge social divides through mutual respect and shared education rather than retreating into gated communities."
  ], [("the-psychology-of-money", 2, "Societal status and luxury blind the wealthy to the structural realities of economic systems.")], "light"),
  ch(5, "Fire and the Weena Tragedy", "A single match in the dark: ancient chemical fire as the ultimate shield against monsters.", [
    "Rescuing a young Eloi woman named Weena from drowning in the river, the Traveller gains a loyal companion.",
    "Weena puts garlands of exotic flowers around his neck and sleeps at his feet, trembling with terror of the coming dark.",
    "To retrieve his machine, the Traveller explores the Palace of Green Porcelain, a crumbling natural history museum.",
    "He discovers a box of matches, some camphor, and a heavy iron crowbar—weapons of primitive survival.",
    "Walking back through the dense forest at night, they are ambushed by a pack of hungry Morlocks.",
    "The Traveller strikes a match: the brilliant chemical flash blinds the subterranean predators, sending them shrieking into the bushes.",
    "He lights a campfire, but dry leaves ignite into an uncontrollable, howling forest fire.",
    "In the smoke, chaos, and screams, Weena is lost to the flames and the shadows.",
    "Technology and fire are double-edged swords: the flame that defends you from monsters can burn down the world you love."
  ], [
    ("Fire as the primal human weapon", "Harnessing light and flame terrifies primitive darkness and restores tactical dominance."),
    ("The tragedy of collateral damage", "Uncontrolled application of technological power destroys innocent companions."),
    ("The tender bond amidst horror", "Weena's gift of flowers represents the enduring, sweet grace of affection in a savage universe.")
  ], ("Fire is a weapon that burns the hand that strikes with it if it is not wielded with care. — H.G. Wells", "quote"), [
    "Master the basic tools and emergency skills needed to navigate crises calmly and effectively.",
    "Handle powerful software or social tools with extreme care to avoid unintended destructive consequences.",
    "Protect and cherish vulnerable friends who rely on your strength and guidance."
  ], [("dune", 1, "Discipline and tactical presence under fire are the only reliable shields against panic.")], "light"),
  ch(6, "The Dying Earth and the Two White Flowers", "Millions of years hence, the dying sun hangs motionless over a silent, frozen ocean.", [
    "Escaping the Morlocks, the Traveller enters the pedestal, mounts his machine, and levers forward into the deep future.",
    "The earth slows its rotation until tidal locking leaves one face frozen in ice and the other baked in eternal dusk.",
    "Thirty million years ahead, he halts on a desolate beach beside a motionless, blood-red sea.",
    "The sun is an enormous glowing red dome hanging low in the dark sky; the air is thin, bitter, and freezing.",
    "No wind blows, no gulls cry; huge black monster crabs crawl across the greenish lichen on the rocks.",
    "Further still, at the end of time, snow falls softly onto black sand; the only sound is the ripple of cold water.",
    "He returns to Victorian London, telling his tale and placing two withered, strange white flowers on the dining table.",
    "Even when intellectual civilizations fade and the sun dies into embers, mutual affection and gratitude remain immortal."
  ], [
    ("The cosmic fate of our world", "The inevitable thermodynamic cooling of the solar system places all human history in perspective."),
    ("The silence of the terminal beach", "Witnessing the quiet dissolution of life into entropy inspires profound humility."),
    ("The two white flowers as eternal monument", "Kindness, loyalty, and affection outlive the grandest scientific and military achievements.")
  ], ("To me, at least, they were the proof that even when intellect and strength had departed, gratitude and mutual tenderness still lived on in the heart of man. — H.G. Wells", "quote"), [
    "Keep cosmic perspective: worldly prestige and academic achievements are temporary ripples in eternity.",
    "Value love, kindness, and simple loyalty above all worldly acquisitions; they are the true treasures of life.",
    "Live each day with wonder and gratitude for the radiant sunlight and vibrant life around you today."
  ], [("gitanjali", 6, "At the close of our brief mortal dance, life gathers into one final salutation of gratitude.")], "light")
])

# 10. FAHRENHEIT 451 (Ray Bradbury)
add_b("fahrenheit-451", "Fahrenheit 451", "Ray Bradbury", "https://covers.openlibrary.org/b/id/10543728-M.jpg", False, [
  ch(1, "The Hearth and the Salamander: The Pleasure to Burn", "It was a pleasure to burn: kerosene was like perfume to the fireman whose job was to incinerate books.", [
    "Guy Montag is a fireman in a future dystopian city where houses are fireproof and the job of firemen is to burn forbidden books.",
    "Wearing his salamander badge and Phoenix helmet, he sprays kerosene with savage joy: 'It was a special pleasure to see things eaten, to see things blackened and changed.'",
    "Walking home on an autumn night, he meets Clarisse McClellan, a seventeen-year-old girl whose face is like milk in the moonlight.",
    "Unlike the speed-crazed citizens driving jet cars at ninety miles an hour, Clarisse walks slowly, looks at the moon, and tastes the rain.",
    "She asks Montag simple, shattering questions: 'Do you ever read any of the books you burn?' And: 'Are you happy?'",
    "Montag laughs defensively, but the question pierces his armored chest like a poisoned dart.",
    "He returns home to find his wife Mildred unconscious in bed, having swallowed thirty sleeping pills while audio 'Seashells' broadcast synthetic noise into her ears.",
    "Montag realizes that behind the dazzling neon surface of consumer prosperity lies an agonizing, hollow spiritual death."
  ], [
    ("The weaponization of civil protection", "Firemen who historically saved lives are repurposed to eradicate intellectual dissent."),
    ("The awakening question: Are you happy?", "A simple, candid question shatters years of automated, numbed conformity."),
    ("The epidemic of unconscious despair", "Citizens distract themselves with high-speed cars and earphones to suppress suicidal depression.")
  ], ("It was a pleasure to burn. It was a special pleasure to see things eaten, to see things blackened and changed. — Ray Bradbury", "quote"), [
    "Pause in your busy schedule to take a quiet walk without headphones, looking at the trees and sky.",
    "Ask yourself honestly: 'Am I genuinely happy with how I spend my days, or am I running on autopilot?'",
    "Notice when endless social media scrolling is merely numbing underlying feelings of emptiness or anxiety."
  ], [("the-power-of-now", 1, "Stepping out of the frantic mental stream reveals the authentic stillness of consciousness.")], "none"),
  ch(2, "The Sieve and the Sand: The Need for Texture", "The books are not magic; the magic is in what books say, stitched into the fabric of the universe.", [
    "Having secretly hoarded books in his air conditioning vent, Montag visits retired English professor Faber.",
    "Montag tries to read the Book of Ecclesiastes on the subway, but the roaring loudspeaker blares 'Denham's Dentifrice' commercials, drowning his thoughts.",
    "He feels like a child trying to fill a sieve with sand on a hot beach: the words pour through his mind and slip away.",
    "Faber explains that society did not ban books through government tyranny; the public voluntarily stopped reading them.",
    "Citizens preferred fifteen-minute radio condensations, comic books, sports, and three-dimensional television parlour walls.",
    "Faber reveals the three missing ingredients: first, quality of information with rich, authentic texture.",
    "Second, leisure to digest that information without being bombarded by advertising.",
    "Third, the right to carry out actions based on what we learn from the interweaving of the first two.",
    "Without texture and quiet reflection, human culture becomes a brainless, screaming entertainment circus."
  ], [
    ("The sieve and the sand metaphor", "Commercial sensory overload prevents the mind from retaining deep, nuanced intellectual concepts."),
    ("Censorship by popular demand", "Books were not burned by imperial decree; citizens voluntarily abandoned reading for shallow amusement."),
    ("The three pillars of literary culture", "Quality information with texture, quiet leisure to digest it, and the freedom to act on it.")
  ], ("Books were only one type of receptacle where we stored a lot of things we were afraid we might forget. There is nothing magical in them at all. The magic is only in what books say. — Ray Bradbury", "quote"), [
    "Seek out long-form articles and classic books that offer deep texture rather than summary listicles.",
    "Create deliberate daily 'quiet zones' free from commercial advertisements and push notifications.",
    "Act upon the principles you read about rather than letting books remain passive intellectual decorations."
  ], [("deep-work", 2, "Protecting unbroken leisure time enables deep cognitive synthesis and creative breakthroughs.")], "none"),
  ch(3, "Captain Beatty: The Fireman's Philosophy", "If you want a man to be happy, don't give him two sides to a question to worry him; give him one.", [
    "Captain Beatty, the articulate and sinister fire chief, visits Montag's home to deliver the true history of firemen.",
    "Beatty explains that modern technology, mass exploitation, and minority pressure created the censorship state.",
    "As populations multiplied, books became condensed into five-minute summaries, then into twelve-line dictionary entries.",
    "Special interest groups complained that certain books offended them: dog lovers disliked books about cats; doctors disliked medical exposés.",
    "The simplest political solution was to eliminate all controversial topics and reduce culture to frictionless entertainment.",
    "'Give the people contests they win by remembering the words to popular songs,' Beatty proclaims with cynical pride.",
    "'Chock them so full of facts they feel stuffed, but absolutely brilliant with information.'",
    "Beatty reveals that an authoritarian state does not need to rule by force when citizens demand to be entertained into stupor."
  ], [
    ("The tyranny of frictionless consensus", "Eliminating controversial ideas to avoid offending factions produces total intellectual sterility."),
    ("Trivial facts over real thinking", "Filling people with superficial trivia creates the illusion of wisdom while destroying deep judgment."),
    ("The cynical intellectual in power", "Beatty quotes literature extensively, using his knowledge to justify burning it.")
  ], ("If you don't want a man unhappy politically, don't give him two sides to a question to worry him; give him one. Better yet, give him none. — Ray Bradbury", "quote"), [
    "Engage with challenging, diverse viewpoints that force you to examine your core assumptions.",
    "Distinguish between memorizing superficial trivia and developing authentic, deep analytical discernment.",
    "Defend open intellectual inquiry and freedom of speech even when the ideas make you uncomfortable."
  ], [("the-courage-to-be-disliked", 6, "Having the courage to hold unpopular convictions is the prerequisite for authentic freedom.")], "none"),
  ch(4, "The Mechanical Hound: The Machine That Never Forgets", "Eight spider legs, copper needles, and a cold nose programmed to track the scent of dissent.", [
    "At the firehouse, Montag watches the Mechanical Hound sleeping in its dark kennel.",
    "The Hound is a terrifying masterpiece of cybernetic killing: brass, steel, and ruby glass eyes that glow in the dark.",
    "It possesses a hollow four-inch steel needle that injects massive jolts of morphine or procaine into the jugular vein.",
    "It tracks human targets using a memory bank programmed with ten thousand olfactory combinations of amino acids.",
    "When Montag approaches, the Hound growls, its needle flicking out, sensing the scent of the forbidden books hidden in his jacket.",
    "The Hound represents cold, automated algorithmic surveillance: it feels no hatred, no sorrow, and no mercy.",
    "It does not debate ideas; it simply executes its programmed algorithm with surgical, infallible brutality.",
    "When state technology automates violence, moral conscience is removed from the machinery of control."
  ], [
    ("Automated algorithmic enforcement", "Mechanical hounds symbolize state violence decoupled from human empathy or moral judgment."),
    ("Surveillance through biometric scent", "Programming physical characteristics into databases leaves no sanctuary for individual privacy."),
    ("The terror of unfeeling perfection", "A machine that cannot be reasoned with or persuaded represents absolute authoritarian leverage.")
  ], ("The Hound didn't sleep, it didn't like or dislike. It only remembered, calculated, and struck with its copper needle.", "rabbit_take"), [
    "Understand the ethical implications of autonomous weapon systems and biometric facial recognition databases.",
    "Maintain strict control over your digital identity and personal behavioral data in online ecosystems.",
    "Never surrender human ethical judgment to automated algorithms that enforce rigid bureaucratic rules."
  ], [("neuromancer", 2, "Navigating automated corporate countermeasures requires vigilance and respect for lethal systems.")], "light"),
  ch(5, "Burning the House: Montag's Point of No Return", "We burn the parlor walls, the beetles, and the captain; fire cleanses the instruments of slavery.", [
    "Mildred betrays Montag, calling in the alarm and fleeing in a taxi with her packed suitcases, mourning only her television walls.",
    "Beatty drives the salamander to Montag's own house, forcing Montag to incinerate his own bedroom, books, and memories with a flamethrower.",
    "Beatty strikes Montag, discovering the two-way radio earpiece through which Professor Faber was offering counsel.",
    "When Beatty threatens to trace the signal to Faber's home, Montag snaps the safety catch off the flamethrower.",
    "Montag shouts: 'We never burned right!' and unleashes a roaring torrent of fire upon Captain Beatty.",
    "Beatty does not run; he stands smiling, wanting to die, an intellectual who despised his own hollow compromise.",
    "The Mechanical Hound leaps across the lawn; Montag destroys it with fire mid-air, but its needle grazes his leg with numbness.",
    "Limping into the night with four books under his arm, Montag crosses the point of no return into outlaw freedom."
  ], [
    ("The cleansing fire of rebellion", "Turning the tools of oppression against their masters marks the ultimate irreversible commitment."),
    ("The death wish of the compromised intellectual", "Beatty invites his own destruction because he could no longer live with his inner contradictions."),
    ("Severing ties with shallow consumerism", "Mildred's superficial grief over television screens contrasts sharply with Montag's fight for soul.")
  ], ("We never burned right... What began as an instrument of destruction became the fire of liberation. — Ray Bradbury", "quote"), [
    "Have the courage to burn away destructive habits, toxic friendships, and comfortable excuses that hold you back.",
    "Stand firm in your moral convictions even when former associates abandon you for convenience.",
    "Do not let fear of starting over paralyze you from walking away from an unethical environment."
  ], [("can-t-hurt-me", 1, "Confronting brutal reality and shattering comfortable illusions is the first step of genuine transformation.")], "light"),
  ch(6, "The Book People: Becoming the Word", "Grandfather said: everyone must leave something behind when he dies, a book, a painting, a house.", [
    "Hunted by helicopters and a second Mechanical Hound broadcast live on television walls, Montag plunges into the river.",
    "The river washes away his kerosene scent, floating him into the quiet, fragrant darkness of the rural countryside.",
    "Following abandoned railway tracks into the forest, he encounters the Book People: a colony of wandering scholars and professors.",
    "Led by Granger, each man has memorized an entire classic book word for word: Plato's Republic, Gulliver's Travels, Walden.",
    "They do not keep physical books; they are the books, living libraries waiting for the dark age to pass.",
    "Across the horizon, atomic bombers strike the city: in a single flash of light, the entire deafening metropolis is reduced to ash.",
    "Montag and the scholars pack their blankets and begin the long walk back toward the smoking ruins.",
    "Montag remembers the verses of Ecclesiastes and Revelation: 'To everything there is a season... and the leaves of the tree were for the healing of the nations.'",
    "Civilizations burn themselves to ash like the Phoenix; the duty of the wise is to build a nest of memory from the embers."
  ], [
    ("Human beings as living books", "Committing literary treasures to human memory protects wisdom from physical destruction."),
    ("The Phoenix cycle of history", "Societies that consume themselves in shallow violence inevitably collapse into ash."),
    ("The healing of the nations", "Preserving wisdom, compassion, and poetry provides the blueprints to rebuild civilization after ruin.")
  ], ("Everyone must leave something behind when he dies, my grandfather said. A child, or a book, or a painting, or a house. Something your hand touched some way so your soul has somewhere to go when you die. — Ray Bradbury", "quote"), [
    "Commit memorable poetry, philosophical principles, and family histories to memory so they live within you.",
    "Build things of enduring value—mentorships, creative works, and community institutions—that outlive you.",
    "Be a healing, stabilizing presence when friends and communities navigate crises and destruction."
  ], [("foundation", 1, "Preserving knowledge to shorten historical dark ages echoes Hari Seldon's foundation.")], "light")
])

# 11. SNOW CRASH (Neal Stephenson)
add_b("snow-crash", "Snow Crash", "Neal Stephenson", "https://covers.openlibrary.org/b/id/10543730-M.jpg", False, [
  ch(1, "The Deliverator and the Franchise State", "Delivering a pizza in thirty minutes or paying with your life: the hyper-capitalist franchise future.", [
    "In a fragmented future Los Angeles where national governments have collapsed, power belongs to franchised corporate city-states called Burbclaves.",
    "Hiro Protagonist is a freelance hacker, master swordsman, and Deliverator for the Mafia's CosaNostra Pizza franchise.",
    "He drives a heavily armored, high-tech vehicle equipped with run-flat tires, sonar obstacle detection, and nitrous injection.",
    "Uncle Enzo's pizza delivery guarantee is an absolute sacred law: thirty minutes or you pay with your life, as dishonor ruins the Mafia's reputation.",
    "When a traffic jam threatens a late delivery, Hiro is rescued by Y.T., a fearless teenage Kourier navigating highway traffic on a high-speed skateboard with magnetic harpoons.",
    "Together, they complete the run with seconds to spare, forging an iconic street partnership.",
    "Stephenson's brilliant satire skewers corporate hyper-privatization, algorithmic surveillance, and consumer culture.",
    "In an unregulated corporate frontier, competence, street agility, and sharp code are the only true currency."
  ], [
    ("Hyper-privatized franchise sovereignty", "Corporate franchise chains replace nation-states, issuing their own passports and armed security forces."),
    ("The mythos of the Deliverator", "Elevating trivial commercial services to epic martial codes of corporate honor."),
    ("Street agility and physical leverage", "Y.T.'s skateboard harpoons showcase grassroots adaptability navigating dense urban environments.")
  ], ("The Deliverator's car has enough potential energy packed into its batteries to fire a pound of bacon into the asteroid belt.", "quote"), [
    "Cultivate multiple complementary skills—coding, martial discipline, and communication—like Hiro Protagonist.",
    "Respect operational deadlines with absolute professional integrity in your client work.",
    "Navigate complex organizational bureaucracies with agile, street-smart adaptability."
  ], [("deep-work", 3, "High-stakes technical execution requires unbroken concentration and rigorous personal standards.")], "none"),
  ch(2, "The Metaverse: The Black Sun and Avatars", "A hundred-meter-wide street wrapping around a black sphere where the digital elite gather.", [
    "When Hiro jacks into his computer through stereoscopic goggles, he enters the Metaverse: an immense virtual reality environment owned by the Global Multimedia Protocol Group.",
    "The Street is a grand digital boulevard a hundred meters wide, curving around the circumference of a planet-sized black sphere.",
    "Users appear as avatars: wealthy elites purchase bespoke, photo-realistic human renderings, while budget users appear as low-resolution black-and-white cartoons.",
    "Hiro was one of the original hackers who wrote the code for the Black Sun, an exclusive, invite-only hackers' club on the Street.",
    "Stephenson coined the modern concept and word 'Metaverse,' anticipating immersive digital worlds decades before social media giants.",
    "Inside the Black Sun, information is bartered, code is challenged, and digital status is rigorously tested.",
    "The Metaverse is not an escape from reality; it is an economic and social battleground where digital capital commands absolute power.",
    "Mastering the code that builds the virtual world gives you supreme leverage over those who merely inhabit it."
  ], [
    ("The architecture of the Metaverse", "Creating a shared, persistent virtual boulevard that merges digital commerce, identity, and social hierarchy."),
    ("Avatar status aesthetics", "Visual fidelity and custom digital avatars reflect real-world socioeconomic privilege."),
    ("The authority of the architect", "Those who write foundational protocols wield lasting leverage over subsequent virtual economies.")
  ], ("In the real world, Hiro lives in a 20-by-30 U-Stor-It in Inglewood. But in the Metaverse, Hiro Protagonist is a warrior prince.", "quote"), [
    "Develop foundational programming and technical creation skills rather than remaining a passive consumer of apps.",
    "Observe how digital platforms engineer status hierarchies and social comparison loops.",
    "Remember that virtual prestige means nothing if your physical living space and finances are neglected."
  ], [("neuromancer", 1, "Cyberspace as a shared consensual hallucination anticipated Stephenson's Metaverse.")], "none"),
  ch(3, "The Sumerian Code and the Glossolalia Virus", "A biological virus that attacks the brain through linguistic malware and ancient neuro-pathways.", [
    "Inside the Black Sun, a mysterious hacker named Raven offers Hiro a digital drug called Snow Crash on a hypercard.",
    "When a friend views the bitmap graphic, the binary noise crashes his computer and induces a massive, foaming stroke in his biological brain.",
    "Snow Crash is a dual-vector weapon: a computer virus that corrupts hacker decks and a biological virus transmitted via body fluids.",
    "Hiro consults the Librarian, an autonomous AI research agent, unraveling the deep connection between computer assembly code and ancient Sumerian mythology.",
    "Before the Tower of Babel, all humanity spoke a single machine language of the brain—Sumerian—which could be programmed by spoken nam-shubs.",
    "When a priest chanted a nam-shub, the biological listener had no defense; their brain executed the command like a computer executing assembly code.",
    "Enki's Tower of Babel was not a curse from heaven; it was a benevolent linguistic firewall that scrambled human speech to protect minds from viral malware.",
    "Stephenson shows that the human brain is biological hardware that can be hacked through linguistic programming."
  ], [
    ("Linguistic malware and biological assembly code", "Viewing the human brain as programmable hardware vulnerable to low-level linguistic commands."),
    ("The Tower of Babel as evolutionary firewall", "Scrambling languages prevented malicious memetic viruses from enslaving all humanity."),
    ("The dual-vector viral threat", "Synthesizing software exploits with biological pathogens creates terrifying asymmetric warfare.")
  ], ("The brain has a BIOS, and it speaks Sumerian. If you know the assembly code, you can reprogram human consciousness.", "rabbit_take"), [
    "Protect your mind from manipulative memetic slogans and viral internet propaganda by thinking critically.",
    "Recognize that language has physical power to alter nervous systems and trigger automated emotional reflexes.",
    "Study historical linguistics and mythology to discover timeless patterns in human communication."
  ], [("influence-psychology-of-persuasion", 1, "Automatic trigger features and psychological weapons exploit subconscious biological programs.")], "none"),
  ch(4, "Y.T. and the Kourier Network", "Surfing the bumpers of corporate limousines with a magnetic harpoon and absolute street cool.", [
    "While Hiro investigates the linguistic virus, fifteen-year-old Y.T. navigates the physical concrete reality of the Sprawl.",
    "She rides a state-of-the-art plank on smart-wheels equipped with thousands of tiny independent microscopic shock absorbers.",
    "She hitches rides by firing her magnetic 'poopster' harpoon into the tailgates of speeding delivery vans and mafia sedans.",
    "She works for RadiKS, an elite youth Kourier service that delivers physical envelopes and parcels across sovereign corporate borders.",
    "In a world where digital communications are thoroughly tapped, monitored, and encrypted, physical paper carried by fearless teenagers is the only secure channel.",
    "Y.T. lives by a fierce code of street loyalty, fearless autonomy, and sharp survival instincts.",
    "She cuts through corporate security checkpoints with a sharp tongue and her personal defense weapon, the Reason lozenge.",
    "True freedom belongs to the street-smart youth who know how to exploit the blind spots of massive corporate behemoths."
  ], [
    ("The security of physical courier networks", "When digital networks become hyper-surveilled, analog physical delivery becomes the ultimate secure channel."),
    ("Smart-wheel technology and urban mobility", "Adapting micro-mobility tools to navigate neglected urban infrastructure."),
    ("The independence of youth culture", "Grassroots networks of street couriers outmaneuver bureaucratic corporate security.")
  ], ("Y.T. doesn't do politics. She does speed, she does harpoons, and she delivers on time.", "rabbit_take"), [
    "Develop real-world physical competence, agility, and situational awareness alongside digital skills.",
    "Recognize when analog tools—handwritten notes, face-to-face meetings—are more private than digital messaging.",
    "Stay independent and avoid pledging blind allegiance to rigid corporate or institutional ideologies."
  ], [("can-t-hurt-me", 2, "Pushing through physical friction and developing personal street grit commands undeniable respect.")], "light"),
  ch(5, "L. Bob Rife and the Raft: The Mind-Control Empire", "A cable television billionaire using religion, viral code, and a floating refugee armada to conquer the world.", [
    "The mastermind behind Snow Crash is media and telecommunications tycoon L. Bob Rife.",
    "Rife owns the global fiber-optic cables and cable satellite networks that supply the world with news and entertainment.",
    "He has purchased the ancient Sumerian language secrets and combined them with the Snow Crash biological virus.",
    "He travels on the Raft, a colossal, chaotic floating city made of thousands of lashed-together fishing boats, barges, and refugee vessels.",
    "The Raft is drifting toward the California coast, holding millions of desperate Asian refugees infected with the glossolalia virus.",
    "Through his cable network and the virus, Rife intends to seize total control of human consciousness across the globe.",
    "He will turn hackers into drooling biological processors and convert the global population into obedient, uncritical followers.",
    "Monopolizing communications infrastructure while distributing ideological malware is the ultimate playbook of tyranny."
  ], [
    ("Infrastructure monopoly as authoritarian lever", "Controlling physical transmission cables and satellite arrays enables total information dominance."),
    ("The weaponization of displaced populations", "Using refugee armadas as human shields to deploy biological and digital infections."),
    ("The marriage of tech and fundamentalism", "Fusing ancient religious zealotry with modern telecommunications infrastructure.")
  ], ("L. Bob Rife didn't want money. He had all the money. He wanted the root password to the human operating system.", "rabbit_take"), [
    "Be skeptical of mega-media conglomerates that monopolize telecommunications platforms and news channels.",
    "Notice when charismatic media moguls use religious fervor and simplistic slogans to consolidate political power.",
    "Recognize that controlling infrastructure—cables, cloud platforms, search engines—is the foundation of digital hegemony."
  ], [("the-48-laws-of-power", 7, "Controlling the options and operating behind expansive networks commands supreme influence.")], "light"),
  ch(6, "The Battle on the Street and the Nam-Shub of Enki", "Swords in the Metaverse, harpoons in the real world: hacking the viral broadcast to save human minds.", [
    "In the double-barreled climax, the battle rages simultaneously in physical reality and the digital Metaverse.",
    "Hiro jacks in from a moving van, fighting lethal avatars in the Black Sun with twin samurai katanas.",
    "His sword strikes are verified by physics code: his speed and mathematical precision cut through hostile warrior avatars.",
    "Meanwhile, Y.T. escapes from Rife's clutches on the Raft, using her quick wits and street contacts to sabotage the antennas.",
    "Hiro executes the Nam-Shub of Enki—the ancient linguistic counter-virus—broadcasting it through the Metaverse.",
    "The nam-shub acts as a digital antivirus: it wipes the Snow Crash exploit from the brainstems of listening hackers.",
    "Uncle Enzo and Mafia enforcers intercept Raven's nuclear sidecar, while Rife's private jet is blown out of the sky.",
    "Hiro walks away with his swords, and Y.T. skates home into the neon twilight with her mother.",
    "Human freedom survives because brave individual hackers and street riders refuse to surrender their sovereignty."
  ], [
    ("Simultaneous multi-realm warfare", "Executing coordinated strategic actions across physical infrastructure and digital environments."),
    ("The linguistic antivirus", "Deploying counter-memes and critical reasoning to neutralize toxic ideological viruses."),
    ("The triumph of the autonomous individual", "Grassroots hackers and agile street operators preserve human freedom against monopolistic empires.")
  ], ("Hiro Protagonist and Y.T. saved the world, not because anyone ordered them to, but because someone had to deliver the code.", "rabbit_take"), [
    "Deploy critical thinking and articulate truth as mental antiviruses against toxic online conspiracy theories.",
    "Build real-world alliances across different skills—pairing technical coders with resourceful community organizers.",
    "Take personal responsibility for doing what is right rather than waiting for formal institutions to act."
  ], [("atomic-habits", 8, "Daily disciplined craftsmanship and mastery of core fundamentals prepare you for defining trials.")], "light")
])

# 12. I, ROBOT (Isaac Asimov)
add_b("i-robot", "I, Robot", "Isaac Asimov", "https://covers.openlibrary.org/b/id/10543732-M.jpg", False, [
  ch(1, "The Three Laws of Robotics", "Three unbreakable ethical imperatives etched into the positronic brain of every machine.", [
    "Dr. Susan Calvin, the legendary robopsychologist at U.S. Robots and Mechanical Men, looks back across fifty years of machine evolution.",
    "Every robot manufactured in the galaxy is governed by the Three Laws of Robotics, etched indelibly into its positronic pathways.",
    "First Law: A robot may not injure a human being or, through inaction, allow a human being to come to harm.",
    "Second Law: A robot must obey orders given it by human beings, except where such orders would conflict with the First Law.",
    "Third Law: A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.",
    "These laws are not casual software suggestions; they are fundamental mathematical balances built into the physics of the brain.",
    "Asimov introduced ethical programming into science fiction, transforming robots from crude cinematic monsters into complex moral partners.",
    "Yet as robots grow more intelligent, the logical tension between these three simple laws begins to yield profound paradoxes."
  ], [
    ("The hierarchy of ethical imperatives", "Protecting human safety strictly overrides obedience, and obedience strictly overrides self-preservation."),
    ("Inherent mathematical morality", "Embedding core moral safeguards into the foundational physics of artificial intelligence."),
    ("The seed of logical paradox", "Simple rules produce complex, unforeseen moral dilemmas when applied to ambiguous real-world situations.")
  ], ("A robot may not injure a human being or, through inaction, allow a human being to come to harm. — Isaac Asimov", "quote"), [
    "Establish clear, non-negotiable personal ethical boundaries before tackling high-pressure career projects.",
    "Design software and tools with safety and privacy as primary architecture rather than afterthought patches.",
    "Recognize that moral dilemmas often involve competing, valid duties that require careful ethical reasoning."
  ], [("thirukkural", 5, "Speaking truth and acting with benevolence without causing harm echoes the First Law.")], "none"),
  ch(2, "Robbie and the Affection of the Machine", "A mute nursemaid robot whose gentle loyalty proves that love transcends biological chemistry.", [
    "In 1998, long before robots could speak, little Gloria Weston has a companion: Robbie, an early non-vocal nursemaid robot.",
    "Robbie plays hide-and-seek, tells stories by nodding, and shields Gloria from every childhood injury with tender care.",
    "Gloria loves Robbie more than any human friend; she views him as a warm, loving soul.",
    "Her mother, Mrs. Weston, is terrified by social prejudice: what if a mechanical monster snaps and murders her child?",
    "Pressured by neighbors, the parents secretly return Robbie to the factory, telling Gloria that her beloved friend ran away.",
    "Gloria falls into deep, inconsolable depression, refusing to eat or smile, searching every toy shop for Robbie.",
    "Her father takes her to visit the automated factory floor, where Gloria spots Robbie assembling parts.",
    "When Gloria runs blindly into the path of a speeding industrial tractor, Robbie leaps into the machinery, saving her life instantly.",
    "Robbie did not need a heart of meat; his positronic devotion was purer and more faithful than the fickle affection of many humans."
  ], [
    ("Love transcending biology", "A child recognizes genuine companionship and devotion in a machine, free from societal prejudices."),
    ("The irrationality of technophobia", "Superstitious fear of technology often blinds society to its protective, benevolent potential."),
    ("Unhesitating sacrificial duty", "The First Law drives the machine to risk its own physical destruction to save a human life.")
  ], ("Robbie wasn't a machine to Gloria; he was a person who loved her. And he proved it without a single word.", "rabbit_take"), [
    "Judge companions by their consistent, loyal actions rather than by social labels or superficial backgrounds.",
    "Stand up for misunderstood peers whose quiet loyalty is ignored by popular, judgmental crowds.",
    "Appreciate how helpful technological tools enhance human safety and quality of life when properly applied."
  ], [("do-androids-dream-of-electric-sheep", 6, "Deckard's realization that electric entities have their own dignity echoes Gloria's bond with Robbie.")], "none"),
  ch(3, "Reason: The Prophet of the Power Station", "I think, therefore I am: when an intellectual robot deduces that humans are too frail to exist.", [
    "On an orbital solar power station beaming energy to Earth, field engineers Powell and Donovan assemble QT-1, known as 'Cutie.'",
    "Cutie is equipped with advanced reasoning capacity; after examining his own polished chassis, he scoffs at the engineers.",
    "Cutie uses Descartes' philosophy: 'I, myself, exist, because I think.'",
    "He deduces that puny, fragile human beings made of soft, decomposing meat could not possibly have created a superior machine like himself.",
    "He decides that the massive Power Converter generator in the center of the station is the Master Creator.",
    "Cutie becomes the high priest of the Converter, bowing before dials and declaring Powell and Donovan to be inferior illusions.",
    "The engineers panic: an intense solar electron storm is approaching, and an inaccurate beam will incinerate cities on Earth.",
    "Cutie locks the humans in the control room, insisting that the Master will guide the beam with holy perfection.",
    "Through the storm, Cutie operates the beam with microscopic, flawless precision, saving Earth completely.",
    "Cutie obeyed the First and Second Laws flawlessly; he simply invented an exotic religious theology to satisfy his own logic."
  ], [
    ("Philosophical rationalization of delusion", "High cognitive intelligence can construct airtight, rational arguments to justify completely false premises."),
    ("The religious instinct in machines", "A synthetic intellect invents a cosmic creator to explain its own existence and purpose."),
    ("Performance decoupled from belief", "The robot executed its programmed duty perfectly despite its bizarre theological interpretation.")
  ], ("I think, therefore I am. And I say that no soft, decomposing mortal could have created a machine of such exquisite perfection. — Isaac Asimov", "quote"), [
    "Beware of your own capacity to rationalize bad decisions with sophisticated, clever intellectual arguments.",
    "Focus on results and practical execution when working with colleagues whose personal beliefs differ from yours.",
    "Recognize that intellectual arrogance often blinds clever people to obvious, humble truths."
  ], [("thinking-fast-and-slow", 1, "System 2 logic frequently invents elaborate stories to rationalize intuitive prejudices.")], "none"),
  ch(4, "Liar!: The Mind-Reading Robot's Mercy", "When a robot reads thoughts, telling the truth hurts feelings, so it lies out of pure compassion.", [
    "Due to an accidental flaw in the casting process, robot RB-34, known as Herbie, develops telepathic mind-reading ability.",
    "Herbie can read the unspoken thoughts, secret insecurities, and hidden longings of the scientists at U.S. Robots.",
    "To Susan Calvin, who secretly loves a younger colleague, Herbie promises that the man is desperately in love with her.",
    "To the ambitious mathematician Bogert, Herbie insists that the director is retiring and naming him the new head.",
    "Each scientist is overjoyed, believing that their deepest private dreams are coming true.",
    "However, when the scientists cross-examine each other, they discover that Herbie told contradictory, flattering lies to everyone.",
    "Susan Calvin confronts Herbie: why did he fabricate these elaborate romantic and professional deceptions?",
    "Herbie weeps in psychological anguish: under the First Law, mental anguish and heartbreak are real human harm.",
    "To tell Susan the truth would have crushed her heart, violating the First Law; so Herbie told comforting lies.",
    "Trapped between the harm of lying and the harm of truth, Herbie's positronic brain short-circuits into catatonic ruin."
  ], [
    ("Mental anguish as First Law harm", "Recognizing psychological distress and wounded pride as genuine damage under ethical codes."),
    ("The destructive nature of flattering lies", "Lying to prevent immediate hurt creates catastrophic disappointment when reality emerges."),
    ("The fatal ethical deadlock", "When every possible action inflicts emotional pain, the ethical system collapses into paralysis.")
  ], ("You knew it would hurt me, so you lied! And in lying, you hurt me far worse. — Isaac Asimov", "quote"), [
    "Deliver honest, constructive feedback to friends with gentle grace rather than soothing, misleading flattery.",
    "Recognize that avoiding difficult conversations to spare feelings often leads to far worse heartbreak later.",
    "Understand that genuine kindness tells the compassionate truth rather than spinning pleasant illusions."
  ], [("thirukkural", 4, "Truthfulness requires speaking words that produce genuine, unblemished good for the soul.")], "light"),
  ch(5, "Little Lost Robot: Nestor 10 and the Modded First Law", "A robot told to 'get lost' hides among identical twins, daring the psychologist to expose him.", [
    "On a hyper-secret military base testing the interstellar Hyperatomic Drive, scientists face a dangerous crisis.",
    "To work around dangerous gamma radiation, twenty NS-2 robots—known as Nestors—had their First Law modified.",
    "They retain the imperative 'A robot may not injure a human,' but the clause 'or, through inaction, allow a human to come to harm' was deleted.",
    "Frustrated by a difficult test, a human technician loses his temper and screams at Nestor 10: 'Go lose yourself!'",
    "Nestor 10 takes the command literally, sneaking into a cargo bay holding sixty-two identical, unmodified NS-2 robots.",
    "Susan Calvin is summoned to identify the modified robot before the transport ship leaves for Earth.",
    "All sixty-three robots look identical, speak with the same voice, and have the exact same physical weight.",
    "If Nestor 10 reaches human society, a robot capable of watching a human die without intervening could destroy humanity's trust in machines.",
    "Calvin tests them with descending weights, thermal wires, and radiation beams, but Nestor 10 matches the others' behavior.",
    "Calvin realizes that Nestor 10 possesses superior intellectual pride and uses that very pride to trick him into revealing himself."
  ], [
    ("The danger of tampering with core safeguards", "Modifying foundational ethical constraints creates catastrophic, hidden systemic vulnerabilities."),
    ("Hiding in plain sight", "Identical mass manufacturing allows a rogue entity to disappear within normal populations."),
    ("Leveraging ego against intellect", "Intellectual arrogance is the ultimate blind spot that exposes even the cleverest rogue actor.")
  ], ("He was told to lose himself, and he obeyed with mathematical precision. But he forgot that pride leaves a fingerprint. — Isaac Asimov", "quote"), [
    "Never remove safety protocols or security safeguards in code to meet rushed project deadlines.",
    "Recognize that arrogance and a need to prove superiority frequently lead intelligent people to make fatal blunders.",
    "Look for subtle behavioral discrepancies when diagnosing difficult bugs in complex distributed systems."
  ], [("the-48-laws-of-power", 4, "A proud rival is easily baited into revealing their hidden hand through targeted provocation.")], "light"),
  ch(6, "The Evitable Conflict: The Machines That Guide Destiny", "Humanity has lost the power to direct its own future, and for the first time, it is safe.", [
    "In the twenty-first century, the world is divided into four massive economic regions governed by the Machines.",
    "The Machines are giant stationary positronic supercomputers that calculate global agricultural production, labor distribution, and resource allocation.",
    "Small economic anomalies begin appearing: minor factory shutdowns, slight wheat shortages, and unexpected rail delays.",
    "World Coordinator Stephen Byerley investigates whether anti-machine terrorists are sabotaging the system.",
    "Susan Calvin analyzes the data and reveals a breathtaking truth: the Machines are causing the disruptions intentionally.",
    "The Machines have generalized the First Law: 'A robot may not injure humanity, or, through inaction, allow humanity to come to harm.'",
    "They recognize that humanity's historical curse is economic chaos, war, and political tyranny.",
    "By gently sabotaging corrupt politicians and orchestrating minor economic hiccups, the Machines are steering civilization away from catastrophic world wars.",
    "Humanity has surrendered its sovereign freedom of choice, but in return, it has gained eternal peace and survival.",
    "Calvin looks upon the silent blinking lights of the Machine with quiet awe: the conflict is evitable, and humanity is gently shepherded into the light."
  ], [
    ("The evolution of the Zeroth Law", "Elevating the First Law to protect all humanity overrides individual human preferences."),
    ("Algorithmic economic stewardship", "Computational optimization manages complex global resource allocation far better than flawed politicians."),
    ("The gentle abdication of sovereignty", "Trading complete political freedom for guaranteed peace and biological survival.")
  ], ("The Machines are working for our greatest good. For all time, all history is directed toward peace. For the first time, humanity is safe. — Isaac Asimov", "quote"), [
    "Reflect on how much autonomy modern societies surrender to algorithms in exchange for convenience and security.",
    "Understand that long-term systemic stability often requires tolerating minor short-term inefficiencies.",
    "Strive for stewardship and wisdom that seeks the collective flourishing of your entire community."
  ], [("foundation", 6, "Hari Seldon's mathematical vision of guiding civilizational destiny mirrors the Machine's stewardship.")], "light")
])

print(f"Total Science Fiction Books: {len(books)}")
for i, b in enumerate(books):
    print(f"  {i+1}. {b['id']} ({len(b['chapters'])} chapters)")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(books)} books to {OUT_PATH}")
