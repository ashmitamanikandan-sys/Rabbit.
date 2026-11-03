# -*- coding: utf-8 -*-
"""
build_hero_scifi_part1.py
Creates first 6 Science Fiction Hero Books:
1. dune
2. frankenstein (PD)
3. 1984-george-orwell
4. brave-new-world
5. neuromancer
6. the-three-body-problem
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
OUT_PATH = os.path.join(ROOT_DIR, "catalog", "hero_scifi_part1.json")

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
        "id": b_id, "title": title, "author": author, "genre": "Science Fiction",
        "cover_url": cover, "public_domain": pd, "fiction": True,
        "chapters": chapters
    })

# 1. DUNE (Frank Herbert)
add_b("dune", "Dune", "Frank Herbert", "https://covers.openlibrary.org/b/id/10543710-M.jpg", False, [
  ch(1, "The Litany Against Fear", "Fear is the mind-killer: facing terror directly allows it to pass through you harmlessly.", [
    "On the ocean world of Caladan, young Paul Atreides faces the gom jabbar test administered by the Bene Gesserit Reverend Mother.",
    "He places his right hand inside a mysterious black box that induces nerve sensations of flesh burning to ash.",
    "A poisoned needle hovers at his neck: pull his hand back in panic, and he dies instantly like an animal caught in a trap.",
    "To survive the excruciating agony, Paul recites the timeless Bene Gesserit litany against fear.",
    "He reminds himself that fear is the mind-killer that brings total obliteration.",
    "He resolves to face his terror, permitting it to pass over him and through his awareness.",
    "When the fear has gone past, he will turn his inner eye to observe its path.",
    "Where the fear has gone there will be nothing; only his sovereign self will remain."
  ], [
    ("Fear paralyzes higher reasoning", "Panic forces reflexive, animalistic reactions that surrender tactical self-control."),
    ("The litany as mental anchor", "Reciting focused, disciplined principles stabilizes the nervous system during crisis."),
    ("Observe fear without becoming it", "Stepping back as the observer allows terror to dissipate without dictating behavior.")
  ], ("I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration.", "quote"), [
    "Recite a calming grounding sentence when sitting down for high-stakes examinations or job interviews.",
    "Do not pull out of a public presentation because your hands shake; breathe through the somatic surge.",
    "Notice when anxiety urges you to run away from difficult social conversations, and stand your ground."
  ], [("the-power-of-now", 1, "Watching intense emotional sensations without judgment dissolves psychological panic.")], "none"),
  ch(2, "Arrakis and the Ecology of Scarcity", "In a world where every drop of moisture is precious, conservation becomes a sacred religion.", [
    "House Atreides relocates to Arrakis, a harsh desert world populated by giant sandworms and nomadic Fremen.",
    "Arrakis produces melange, the spice that extends human longevity and enables interstellar space navigation.",
    "Yet the true defining currency of the planet is not wealth, but ordinary liquid water.",
    "The Fremen wear stillsuits that recycle every drop of bodily perspiration, urine, and breath into drinkable moisture.",
    "Spitting on the ground is a greeting of profound respect, representing the voluntary gift of one's personal water.",
    "Herbert shows how environmental limitations dictate culture, technology, religion, and social bonds.",
    "When an ecosystem is pushed to extreme scarcity, human wastefulness is treated as mortal treason.",
    "Respecting natural boundaries is the fundamental law of planetary survival."
  ], [
    ("Scarcity dictates social values", "Cultural customs and moral codes evolve around the most constrained vital resource."),
    ("Technology aligned with ecology", "The Fremen stillsuit functions as a personal closed-loop biome rather than fighting nature."),
    ("The sacredness of conservation", "Treating essential environmental resources with reverence prevents civilization collapse.")
  ], ("A process cannot be understood by stopping it. Understanding must move with the flow of the process, must join it and flow with it.", "quote"), [
    "Practice mindful conservation of water and electricity in your apartment rather than leaving fixtures running.",
    "Examine how your monthly budget shifts when you treat savings as a non-negotiable scarcity constraint.",
    "Respect the local natural environment when hiking or camping by leaving zero waste behind."
  ], [("thirukkural", 2, "Water as the prerequisite for civilization echoes the desert wisdom of Arrakis.")], "none"),
  ch(3, "The Trap of Prophecy and Charisma", "Beware of charismatic heroes: following a messiah blinds a civilization to its own doom.", [
    "Bene Gesserit sisterhoods spent centuries planting superstitious messianic prophecies among primitive desert populations.",
    "When Duke Leto is assassinated by the treacherous Harkonnens, Paul and his mother Jessica flee into the deep desert.",
    "The Fremen recognize Paul as the Mahdi, their long-foretold savior who will transform Arrakis into a lush garden.",
    "Paul perceives terrifying visions of the future: a galactic jihad fought in his name that will kill billions.",
    "He realizes that the greatest danger to human freedom is not obvious tyranny, but the seductive power of a charismatic leader.",
    "When populations surrender their critical thinking to a savior, they unleash uncontrollable historical fanaticism.",
    "Herbert intended Dune as a profound warning against placing uncritical faith in messianic political figures.",
    "True wisdom questions idols and insists on distributed individual responsibility."
  ], [
    ("Charismatic leaders are perilous traps", "Surrendering judgment to heroes invites historical catastrophe and fanaticism."),
    ("Manufactured mythology", "Religious and political legends are frequently engineered tools for social control."),
    ("The momentum of collective fanaticism", "Once a mass movement sanctifies a leader, even the leader cannot stop the holy war.")
  ], ("No more terrible disaster could befall your people than for them to fall into the hands of a Hero.", "quote"), [
    "Critique political and cultural influencers instead of adopting their doctrines without question.",
    "Maintain healthy skepticism toward campus or online movements that demand total obedience to one charismatic founder.",
    "Take personal responsibility for community initiatives rather than waiting for an idealized hero to fix things."
  ], [("1984-george-orwell", 1, "The cult of personality around Big Brother shows the destructive apex of political idolatry.")], "none"),
  ch(4, "The Fremen Way: Desert Power", "True power does not live in grand palaces; it lives in the resilient people who endure the storm.", [
    "To survive among the Fremen, Paul takes the name Muad'Dib, the desert kangaroo mouse who creates its own water.",
    "He learns to walk across the shifting dunes without rhythm, mimicking the natural movements of wind to avoid sandworms.",
    "The Fremen possess no spaceships or atomic armaments, yet their collective discipline makes them unbeatable warriors.",
    "They share water, bury their dead with honor, and practice brutal collective efficiency.",
    "While the galactic Emperor and Baron Harkonnen dismiss the Fremen as backward desert rabble, Paul recognizes their true strength.",
    "Desert power comes from intimate knowledge of terrain, shared hardship, and unbreakable tribal trust.",
    "Underestimating quiet, disciplined communities is the fatal error of decadent imperial regimes.",
    "Authentic resilience outperforms extravagant military displays every single time."
  ], [
    ("Rhythm-less motion across sand", "Adapting your actions to fit environmental patterns avoids triggering hostile forces."),
    ("Power rooted in shared hardship", "Communities bonded by mutual sacrifice possess psychological strength that luxuries cannot buy."),
    ("The illusion of imperial dominance", "Decadent ruling elites inevitably misunderstand the fierce resolve of grassroots populations.")
  ], ("He who can destroy a thing, they control it. You have no idea how much power is hidden in these dunes.", "rabbit_take"), [
    "Observe the unspoken culture and norms of a new workplace or team before attempting to lead them.",
    "Value understated, disciplined peers over flashy self-promoters who boast about their wealth.",
    "Build grit by voluntarily tackling difficult, unglamorous tasks that other students avoid."
  ], [("can-t-hurt-me", 3, "Outworking opponents in the harshest conditions commands undeniable respect.")], "light"),
  ch(5, "Riding the Maker: Shai-Hulud", "Conquering the leviathan requires stepping directly into its path with courage and iron hooks.", [
    "To become a full sandrider and Fremen leader, Paul must complete the ultimate rite of passage: summoning and mounting a giant sandworm.",
    "Deep in the desert, he plants a mechanical thumper that pulses rhythmic soundwaves into the bedrock.",
    "An immense worm—four hundred meters of armored rings with an incandescent furnace of teeth—surges from the sand.",
    "Paul does not run away; he sprints toward the roaring monster, wedging maker hooks beneath its soft ring segments.",
    "The worm rotates its body to keep sensitive flesh away from the sand, lifting Paul atop its armored crest.",
    "By commanding the greatest predator on the planet, Paul transforms an existential terror into an unstoppable chariot.",
    "You cannot conquer monumental challenges by running away from their crushing mass.",
    "Step directly into the storm, find the leverage point, and ride the momentum of the crisis."
  ], [
    ("Face the leviathan head-on", "Waiting in fear guarantees destruction; moving decisively toward the threat provides leverage."),
    ("Turn terror into transportation", "Understanding the mechanics of a crisis allows you to harness its immense energy."),
    ("Earning legitimate leadership", "Respect within a demanding community is earned by sharing their most dangerous trials.")
  ], ("The mystery of life isn't a problem to solve, but a reality to experience. A sandrider moves with the worm, not against it.", "rabbit_take"), [
    "Tackle the hardest, most intimidating project on your syllabus first rather than delaying it until finals.",
    "Address a brewing interpersonal conflict directly before it grows into an unmanageable crisis.",
    "Volunteer to lead high-stakes presentations to build undeniable leadership credibility among your peers."
  ], [("the-mountain-is-you", 6, "The obstacle before you is the crucible that transforms you into a summit leader.")], "light"),
  ch(6, "The Water of Life and the Golden Path", "Awakening to cosmic consciousness reveals that survival requires terrifying sacrifice.", [
    "Paul drinks the Water of Life, a deadly toxic poison extracted from a dying newborn sandworm.",
    "Bene Gesserit training allows him to alter his cellular biochemistry, transmuting the venom into harmless nourishment.",
    "In doing so, his mind expands across space and ancestral genetic memory, awakening as the Kwisatz Haderach.",
    "He sees past, present, and infinite futures flowing like converging rivers into a single nexus.",
    "He marches upon the imperial capital, holding the spice supply hostage and overthrowing the Galactic Padishah Emperor.",
    "Yet in the hour of supreme galactic triumph, Paul weeps inside his stillsuit.",
    "He realizes that the bloody jihad cannot be halted; history has swept past his individual will.",
    "Even the most enlightened visionary remains constrained by the terrible momentum of human destiny."
  ], [
    ("Transmuting internal poison", "Mastering personal biology and consciousness converts destructive toxins into illumination."),
    ("The burden of total prescience", "Seeing all future possibilities removes the innocent joy of spontaneous human living."),
    ("The tragedy of unchecked momentum", "Massive historical victories frequently unleash consequences that escape the victor's control.")
  ], ("There is no real ending. It's just the place where you stop the story. And the jihad has begun.", "quote"), [
    "Transform personal pain, failure, and rejection into wisdom that clarifies your future decisions.",
    "Recognize that winning a competition or promotion is merely the beginning of higher responsibilities.",
    "Carefully evaluate the long-term ethical consequences of your ambitious goals before unleashing them."
  ], [("thinking-fast-and-slow", 6, "Overconfidence in forecasting the future blinds leaders to severe systemic risks.")], "light")
])

# 2. FRANKENSTEIN (Mary Shelley) - Public Domain
add_b("frankenstein", "Frankenstein", "Mary Shelley", "https://covers.openlibrary.org/b/id/10543712-M.jpg", True, [
  ch(1, "The Spark of Unhallowed Creation", "Ambition divorced from empathy generates horrors that will escape your control.", [
    "Young Victor Frankenstein departs Geneva for the university of Ingolstadt, consumed by feverish scientific ambition.",
    "Obsessed with discovering the elixir of life, he spends sleepless nights collecting bones from charnel houses and dissecting human remains.",
    "He isolates himself completely from family, friends, and the natural beauty of the Swiss seasons.",
    "On a dreary November night, by the dim flicker of a dying candle, he infuses the spark of electricity into his stitched creation.",
    "The creature's dull yellow eye opens, its limbs convulse with life, and its watery chest heaves with breath.",
    "Instead of rejoicing in scientific triumph, Victor recoils in sickening horror and flees his laboratory in cowardice.",
    "He created life without taking responsibility for the moral, emotional, and social needs of what he brought into the world.",
    "Intellect without compassion is the ultimate recipe for tragic ruin."
  ], [
    ("The hubris of unchecked ambition", "Pursuing technological achievement without ethical foresight invites catastrophic blowback."),
    ("The moral duty of the creator", "Bringing something new into existence demands lifelong responsibility for its care."),
    ("The folly of isolation", "Severing bonds with family and nature warps moral judgment and produces monstrous results.")
  ], ("Learn from me, if not by my precepts, at least by my example, how dangerous is the acquirement of knowledge. — Mary Shelley", "quote"), [
    "Do not build software algorithms or products without considering how bad actors might exploit them.",
    "Maintain daily contact with friends and family during intense study sprints so you do not lose perspective.",
    "Own up to project mistakes immediately rather than abandoning them for teammates to clean up."
  ], [("deep-work", 1, "Intense intellectual focus must be balanced with ethical boundaries and healthy human connection.")], "none"),
  ch(2, "The Creature's Education in the Woods", "Every human spirit begins with innocence; cruel rejection twists longing into bitterness.", [
    "Abandoned by his creator, the nameless creature wanders into the cold forest, confused by sensory impressions of light and hunger.",
    "He finds shelter in a hovel attached to a rural cottage, secretly observing the humble De Lacey family through a chink in the wall.",
    "By watching them, he learns the beauty of human speech, the gentle grace of familial love, and the power of reading.",
    "He discovers a discarded satchel containing Milton's Paradise Lost, Plutarch's Lives, and Goethe's Sorrows of Young Werther.",
    "He wept with sympathy for the poor, collected firewood for the blind father at night, and dreamed of friendship.",
    "The creature possessed an inherently benevolent, tender heart that craved only affection and acceptance.",
    "Shelley shows that evil is not born into the world; malice is manufactured by societal prejudice and cruelty.",
    "Treat the vulnerable with warmth, for your rejection may forge the very monster you fear."
  ], [
    ("Original benevolence of the soul", "No creature begins life desiring cruelty; warmth and kindness are universal desires."),
    ("The power of self-education", "Reading classic literature allows isolated minds to develop rich moral understanding."),
    ("Prejudice manufactures malice", "Shunning individuals for superficial appearance breeds intense, justified grievance.")
  ], ("I was benevolent and good; misery made me a fiend. Make me happy, and I shall again be virtuous. — Mary Shelley", "quote"), [
    "Never mock or exclude classmates based on their clothing, physical appearance, or awkward mannerisms.",
    "Read classic literature to develop deep empathy for people whose life backgrounds differ from your own.",
    "Notice how cold, dismissive treatment can harden someone's personality over time, and choose kindness instead."
  ], [("the-subtle-art-of-not-giving-a-fuck", 4, "Taking responsibility for how you treat vulnerable companions prevents toxic cycles.")], "none"),
  ch(3, "The Blind Man's Touch and the Curse of Appearance", "Only the blind can see past the prejudice of the eye to touch the authentic soul.", [
    "Gathering his courage, the creature enters the cottage while the young people are away, speaking to the blind old father, De Lacey.",
    "Because the father cannot see the creature's towering frame and stitched skin, he listens with patient compassion.",
    "The father reassures him: 'To be friendless is indeed to be unfortunate, but the hearts of men are full of brotherly love.'",
    "For one golden minute, the creature experiences the holy warmth of human communion.",
    "Suddenly, Felix, Agatha, and Safie return; horrified by the creature's monstrous visage, Felix strikes him violently with a stick.",
    "The creature does not strike back; with a weeping, broken heart, he flees back into the dark woods.",
    "Visual appearance is the terrible filter that blinds civilized society to the goodness of the inner heart.",
    "When human cruelty destroys hope, the wounded soul declares war on all mankind."
  ], [
    ("Sight as a barrier to empathy", "Visual biases blind people to the true spiritual character of their fellow human beings."),
    ("The fragility of trust", "A single act of violent prejudice can shatter years of patient, tender longing for connection."),
    ("The birth of vengeance", "When society consistently refuses love to the vulnerable, despair curdles into destructive wrath.")
  ], ("I am an unfortunate and deserted creature; I look around and have no friend on earth. — Mary Shelley", "quote"), [
    "Listen attentively to someone's words and ideas before judging them by their social media pictures.",
    "Defend unpopular or bullied peers when others attack them out of superficial prejudice.",
    "Examine your own unconscious biases regarding accents, physical beauty, and dress codes."
  ], [("surrounded-by-idiots", 3, "Looking past superficial exterior mannerisms reveals the underlying human value within.")], "none"),
  ch(4, "The Summit at Montanvert: The Creator Confronted", "You are bound to me by ties that cannot be dissolved; fulfill your duty to your creation.", [
    "Seeking solace from guilt, Victor climbs the alpine glaciers of Chamonix, arriving at the icy summit of Montanvert.",
    "Across the sea of ice, the creature bounds toward him with superhuman speed and agility.",
    "Victor curses him: 'Fiend! Devil! Begone, or stay that I may trample you to dust!'",
    "The creature replies with dignified, heartbreaking eloquence: 'Remember that I am thy creature; I ought to be thy Adam, but I am rather the fallen angel.'",
    "He demands that Victor sit beside him and listen to his story before passing sentence.",
    "He demands that Victor create an equally solitary female companion so they may live in peace in South America.",
    "If Victor grants him this mercy, he vows never to look upon the face of man again.",
    "Even the most despised outcast has a moral claim on the architect of its existence."
  ], [
    ("Accountability to the vulnerable", "Authority figures cannot disown the consequences of the systems they bring into the world."),
    ("The eloquence of the oppressed", "Articulate truth delivered with moral clarity cuts through the defensive rage of the powerful."),
    ("The desperate need for companionship", "No living consciousness can endure unbroken, eternal isolation without losing its mind.")
  ], ("Remember that I am thy creature; I ought to be thy Adam, but I am rather the fallen angel, whom thou drivest from joy for no misdeed. — Mary Shelley", "quote"), [
    "Hear the honest grievances of teammates before dismissing their complaints as unreasonable whining.",
    "Acknowledge the needs of junior colleagues you mentor; do not leave them stranded without guidance.",
    "Recognize that everyone needs at least one loyal companion who understands their authentic self."
  ], [("the-courage-to-be-disliked", 2, "Interpersonal relationship connection is the foundational prerequisite for mental health.")], "light"),
  ch(5, "The Broken Promise on the Orkney Isles", "Breaking ethical faith with the desperate turns manageable conflict into absolute tragedy.", [
    "Victor travels to a bleak, windswept hut in the remote Orkney Islands of Scotland to assemble the female companion.",
    "As he pieces together the female form, dark doubts paralyze his mind: what if they breed a race of devils?",
    "Looking out the window, he sees the creature gazing in at him through the moonlight, eyes full of trembling hope.",
    "In a sudden fit of hysterical dread, Victor tears the unfinished female to pieces across the floor.",
    "The creature lets out a howl of utter despair and vanishes into the foggy night.",
    "He returns for one chilling warning: 'I go; but remember, I shall be with you on your wedding-night.'",
    "Victor egotistically assumes the threat is directed at himself, blinding him to the danger hovering over Elizabeth.",
    "Betraying a solemn covenant destroys all possibility of reconciliation, leaving only vengeance."
  ], [
    ("The catastrophic cost of betrayal", "Breaking a covenant with an adversary closes the door to peace and invites total war."),
    ("The blindness of narcissism", "Victor assumes threats are aimed solely at him, failing to protect those he loves."),
    ("Panic destroys diplomacy", "Hasty, emotionally reactive decisions destroy carefully negotiated compromises.")
  ], ("You are my creator, but I am your master; obey! Remember, I shall be with you on your wedding-night. — Mary Shelley", "quote"), [
    "Keep your promises to partners and peers even when honoring them feels inconvenient or difficult.",
    "Consider how your erratic decisions will impact your friends and family, not just your own career.",
    "Never corner an opponent so thoroughly that they have nothing left to lose."
  ], [("the-48-laws-of-power", 8, "Pushing adversaries into total desperation creates unpredictable, lethal retaliation.")], "light"),
  ch(6, "The Arctic Chase and Walton's Choice", "Pursuing vengeance across frozen wastes leaves both hunter and hunted hollowed into dust.", [
    "Following the murder of his bride Elizabeth, Victor dedicates his remaining life to hunting the creature across the world.",
    "The chase leads to the howling, frozen wastes of the Arctic Ocean, where Victor collapses on the pack ice.",
    "He is rescued by Captain Robert Walton, an ambitious explorer sailing his icebound ship toward the North Pole.",
    "Victor tells Walton his tragic history and warns him against sacrificing his crew for scientific vanity.",
    "Victor dies aboard the ship, his heart consumed by bitter, unhealed fury.",
    "That night, Walton discovers the towering creature weeping over Victor's dead body in the cabin.",
    "The creature laments that his revenge brought him only agony; he vows to build his own funeral pyre at the Pole.",
    "Walton learns the lesson Victor could not: he turns his ship around and sails home to warmth and fellowship."
  ], [
    ("Vengeance yields only ashes", "Destroying an enemy does not heal the internal wound that sparked the hatred."),
    ("The wisdom of retreat", "Walton displays true heroism by turning his ship back rather than killing his crew for glory."),
    ("Shared grief of rivals", "Hunter and hunted are bound together in the same tragic tapestry of human frailty.")
  ], ("Seek happiness in tranquility and avoid ambition, even if it be only the apparently innocent one of distinguishing yourself in science. — Mary Shelley", "quote"), [
    "Let go of petty grudges before they consume your energy and poison your personal relationships.",
    "Know when to step back from an unhealthy academic or career rivalry that threatens your well-being.",
    "Value peaceful domestic happiness and loyal friendships above flashy, lonely worldly prestige."
  ], [("mans-search-for-meaning", 6, "True human greatness lies in loving stewardship rather than self-destructive obsession.")], "light")
])

# 3. 1984 (George Orwell)
add_b("1984-george-orwell", "1984", "George Orwell", "https://covers.openlibrary.org/b/id/10543714-M.jpg", False, [
  ch(1, "The Telescreen and the Diary", "Writing your honest thoughts in secret is the revolutionary first step of human liberation.", [
    "In the bleak, decaying city of London, Chief City of Airstrip One, Winston Smith lives under the surveillance of the Party.",
    "Telescreens on every wall broadcast propaganda while monitoring every whisper, facial tic, and heartbeat.",
    "Posters everywhere proclaim: 'Big Brother Is Watching You.'",
    "In a tiny alcove just out of view of the telescreen, Winston commits the fatal offense of Thoughtcrime.",
    "He opens a blank diary purchased in a junk shop, dips a real steel pen into ink, and writes the date: April 4th, 1984.",
    "He writes: 'Freedom is the freedom to say that two plus two make four. If that is granted, all else follows.'",
    "To express an authentic, unapproved thought in an authoritarian society is an act of supreme courage.",
    "The reclamation of human dignity begins with the solitary pen touching honest paper."
  ], [
    ("The privacy of the inner mind", "Totalitarian control requires destroying the sanctuary of private, unmonitored thought."),
    ("Writing as an act of resistance", "Documenting objective truth preserves sanity in a world saturated with manufactured lies."),
    ("The foundation of objective reality", "Two plus two equals four represents the irreducible cornerstone of intellectual liberty.")
  ], ("Freedom is the freedom to say that two plus two make four. If that is granted, all else follows.", "quote"), [
    "Keep a private physical journal where you write your uncensored thoughts free from social media judgment.",
    "Refuse to repeat popular campus slogans that you know in your heart are factual falsehoods.",
    "Protect your digital privacy by regularly auditing app permissions and camera access on your phone."
  ], [("gitanjali", 2, "Where the mind is without fear and the clear stream of reason has not lost its way.")], "none"),
  ch(2, "Newspeak and the Shrinking of Thought", "When you eliminate the words for freedom, you make the concept of rebellion impossible to conceive.", [
    "Winston lunches in the Ministry of Truth canteen with Syme, an intellectual philologist compiling the Eleventh Edition of the Newspeak Dictionary.",
    "Syme speaks with ecstatic pride: 'We're cutting the language down to the bone. Don't you see that the whole aim of Newspeak is to narrow the range of thought?'",
    "In Newspeak, bad is replaced by ungood; fantastic is replaced by doubleplusgood.",
    "Thousands of nuanced synonyms for honor, liberty, conscience, and justice are systematically incinerated in the memory holes.",
    "Orwell reveals the profound connection between language and human cognition: you cannot think what you cannot name.",
    "When a population's vocabulary is reduced to crude, emotional slogans, deep philosophical rebellion becomes psychologically impossible.",
    "Defending rich, precise language is not pedantry; it is the frontline defense of human consciousness.",
    "Cherish words, for words are the architecture of freedom."
  ], [
    ("Language shapes cognitive boundaries", "Restricting vocabulary directly restricts the complexity of ideas a citizen can formulate."),
    ("The destruction of nuance", "Reducing speech to binary emotional polarities destroys critical thinking and empathy."),
    ("The weaponization of dictionaries", "Controlling definition standards allows authority to rewrite cultural reality at will.")
  ], ("Don't you see that the whole aim of Newspeak is to narrow the range of thought? In the end we shall make thoughtcrime literally impossible, because there will be no words in which to express it.", "quote"), [
    "Read challenging books to expand your active vocabulary rather than relying on internet slang.",
    "Describe your emotions with precise words like melancholy, frustrated, or nostalgic rather than just 'bad.'",
    "Challenge vague political or corporate buzzwords by asking for concrete, specific definitions."
  ], [("thinking-fast-and-slow", 3, "Cognitive ease and simplified language suppress analytical System 2 reasoning.")], "none"),
  ch(3, "Doublethink and Reality Control", "The ultimate tyranny is forcing people to hold two contradictory beliefs simultaneously and accept both.", [
    "The Ministry of Truth fabricates history; the Ministry of Peace conducts endless war; the Ministry of Love tortures dissidents.",
    "The Party's primary psychological weapon is doublethink: the power of holding two contradictory beliefs in one's mind simultaneously, and accepting both of them.",
    "To tell deliberate lies while genuinely believing in them; to forget any fact that has become inconvenient, and then draw it back from oblivion when needed.",
    "When the Party announces that the chocolate ration has been increased from thirty grams to twenty, citizens cheer in ecstasy.",
    "They completely forget that yesterday the ration was thirty grams; today's scarcity is celebrated as glorious abundance.",
    "History has stopped: nothing exists except an endless present in which the Party is always right.",
    "Orwell warns that totalitarian power thrives when citizens surrender their memory and accept whatever authority proclaims today.",
    "Holding firm to historical memory is the only anchor against madness."
  ], [
    ("The mechanics of doublethink", "Accepting contradictory assertions without cognitive dissonance signals total mental subjugation."),
    ("The mutability of the past", "Rewriting history allows rulers to claim perpetual infallibility across every crisis."),
    ("Memory as resistance", "Trusting your own eyes and retained historical facts protects you against psychological gaslighting.")
  ], ("Doublethink means the power of holding two contradictory beliefs in one's mind simultaneously, and accepting both of them.", "quote"), [
    "Fact-check political claims against original historical records rather than relying on today's social feed.",
    "Notice when media outlets reverse their positions on policies and hold them accountable to past statements.",
    "Maintain intellectual integrity by admitting when two principles you support are in genuine tension."
  ], [("influence-psychology-of-persuasion", 2, "Commitment and consistency can be exploited by institutions to enforce blind loyalty.")], "none"),
  ch(4, "The Room Above Mr. Charrington's Shop", "A bowl of sugar, real coffee, and a paperweight: the fragile beauty of ordinary life.", [
    "Winston and Julia rent a secret room above Mr. Charrington's antique shop in the proletarian quarter.",
    "Free from the watchful gaze of the telescreen, they create an oasis of authentic humanity.",
    "Julia brings real black market coffee, dark chocolate, and white bread with real strawberry jam.",
    "Winston buys a heavy, coral glass paperweight from the shop, mesmerized by its useless, antique beauty.",
    "The paperweight holds no political purpose, no productive utility; it is simply a preserved bubble of the past.",
    "Winston gazes into the glass, feeling that the room itself is an amber sanctuary protecting their stolen happiness.",
    "Orwell reminds us that the totalitarian state hates small, unmonitored human pleasures more than ideological tracts.",
    "True revolution is found in tasting real coffee, sharing quiet laughter, and loving someone for who they are."
  ], [
    ("The subversiveness of ordinary joy", "Experiencing unapproved aesthetic pleasure and private affection challenges state monopoly."),
    ("The glass paperweight as symbol", "Preserving non-utilitarian beauty anchors the spirit to a time before mass regimentation."),
    ("The illusion of safety", "Carving out temporary private sanctuaries cannot survive indefinitely in a total surveillance state.")
  ], ("The paperweight was the room he was in, and the coral was Julia's life and his own, fixed in a sort of eternity at the heart of the crystal.", "rabbit_take"), [
    "Put away all digital screens during meals with friends to savor conversation and shared food.",
    "Collect physical books and handwritten letters that cannot be edited or deleted by remote servers.",
    "Cherish quiet, unmonitored moments of reflection away from public social media visibility."
  ], [("flow", 5, "Creating quiet spaces for focused, autotelic enjoyment restores profound human balance.")], "light"),
  ch(5, "Room 101 and the Breaking of the Spirit", "Everyone has a breaking point: the thing in the world that is completely unendurable to them.", [
    "Betrayed by the antique shopkeeper and O'Brien, Winston is dragged into the bowels of the Ministry of Love.",
    "O'Brien explains that the Party does not merely destroy its enemies; it converts them, capturing their inner consciousness.",
    "'The object of power is power,' O'Brien proclaims, holding up four fingers and demanding that Winston see five.",
    "When intellectual torture and beatings fail to break Winston's core loyalty to Julia, O'Brien takes him to Room 101.",
    "In Room 101 lies the worst thing in the world: an individualized terror tailored to each prisoner's primal nightmare.",
    "For Winston, it is a cage of starving, carnivorous sewer rats placed directly against his face.",
    "In absolute, frantic terror, Winston snaps: 'Do it to Julia! Do it to Julia! Not me! Tear her face off, strip her to the bones!'",
    "He surrendered his soul; he threw the one he loved into the abyss to save his physical skin."
  ], [
    ("The terrifying reality of primal fear", "Every human spirit has a specific breaking point where survival instinct overrides moral love."),
    ("Power for power's sake", "Totalitarian regimes do not seek wealth or luxury; they seek the pure thrill of crushing human wills."),
    ("The betrayal of the beloved", "True spiritual destruction occurs not when the body breaks, but when love is actively betrayed.")
  ], ("Do it to Julia! Do it to Julia! Not me! Julia! I don't care what you do to her. Tear her face off, strip her to the bones. Not me! Julia! Not me!", "quote"), [
    "Recognize your deepest psychological vulnerabilities before high-pressure situations test your integrity.",
    "Stand by friends during difficult public controversies rather than sacrificing them to save your reputation.",
    "Beware of authoritarian systems that use fear and intimidation to force false public confessions."
  ], [("the-48-laws-of-power", 9, "Manipulators identify personal weaknesses and leverage them to command absolute surrender.")], "light"),
  ch(6, "The Chestnut Tree Cafe: He Loved Big Brother", "When the battle with yourself is over, the tears rolling down your cheeks taste of victory.", [
    "Broken and hollowed out, Winston sits in his usual corner of the Chestnut Tree Cafe, sipping clove-flavored Victory Gin.",
    "He plays chess against himself, moving the white pieces while listening to the telescreen announce border victories in Africa.",
    "He met Julia by chance in the park: their bodies were stiff, their voices dead, their affection burned to gray ash.",
    "They admitted to each other: 'I betrayed you.' And in that confession, whatever made them human had died.",
    "Winston gazes up at the enormous portrait of Big Brother on the wall, tears of gratitude welling in his eyes.",
    "He remembered false memories of his mother and childhood, brushing them aside as foolish delusions.",
    "The long, painful struggle was over; he had won the victory over himself.",
    "He loved Big Brother; and in that tragic surrender, the last free human being in Oceania was extinguished."
  ], [
    ("The total extinction of the individual", "Surrendering your authentic identity to conformity brings a terrible, hollow tranquility."),
    ("Emotional atrophy under tyranny", "When trust and love are systematically broken, the capacity for genuine affection rots away."),
    ("The final warning to posterity", "Orwell's masterpiece ends not with heroic triumph, but with a chilling warning of what must never be permitted.")
  ], ("He had won the victory over himself. He loved Big Brother.", "quote"), [
    "Never compromise your fundamental moral convictions to fit into a popular, intolerant crowd.",
    "Notice when public social pressure makes you want to surrender your doubts just to feel accepted.",
    "Remember that intellectual independence requires eternal vigilance and the courage to stand alone."
  ], [("meditations", 5, "Standing upright through authentic personal virtue is the only defense against conformity.")], "light")
])

# 4. BRAVE NEW WORLD (Aldous Huxley)
add_b("brave-new-world", "Brave New World", "Aldous Huxley", "https://covers.openlibrary.org/b/id/10543716-M.jpg", False, [
  ch(1, "Community, Identity, Stability: The Bokanovsky Hatchery", "Control is far more effective when people are engineered to love their servitude.", [
    "In the Central London Hatchery and Conditioning Centre, human beings are no longer born from mothers; they are decanted in test tubes.",
    "Using the Bokanovsky process, a single fertilized egg is shocked into dividing into ninety-six identical twins.",
    "Humanity is divided into rigid biological castes: Alphas and Betas for leadership and intellect, Gammas, Deltas, and Epsilons for manual labor.",
    "In the infant nurseries, Delta babies are offered bright bowls of roses and colorful picture books.",
    "As the infants crawl forward with delight, electric sirens howl and mild electrical shocks pulse through their limbs.",
    "Through Pavlovian conditioning and sleep-teaching hypnopaedia, children are conditioned to despise nature, silence, and books.",
    "Huxley reveals a horrifying truth: tyranny does not need torture chambers when it can manufacture docile, happy slaves in bottles.",
    "When comfort replaces freedom, human civilization surrenders its soul with a smile."
  ], [
    ("Biological engineering of obedience", "Pre-conditioning individuals for designated social roles eliminates political rebellion."),
    ("Conditioning against quiet reflection", "Training citizens to fear silence and nature keeps them trapped in artificial consumer loops."),
    ("The slogan of state stability", "Sacrificing artistic truth and individual diversity for social peace produces a lifeless hive.")
  ], ("Community, Identity, Stability. That is the grand slogan of the World State, where people are made to love their servitude.", "rabbit_take"), [
    "Notice how algorithmically curated social media feeds condition you to crave endless, bite-sized entertainment.",
    "Resist societal pressure to fit yourself into rigid career categories that stifle your authentic curiosity.",
    "Spend time alone in natural silence, detoxing from constant electronic auditory stimulation."
  ], [("1984-george-orwell", 2, "While Orwell feared tyranny through pain, Huxley feared tyranny through pleasurable distraction.")], "none"),
  ch(2, "Soma: The Chemistry of Compliance", "A gramme is better than a damn: swallowing synthetic bliss to escape reality.", [
    "Whenever a citizen of the World State experiences a flicker of sorrow, anger, or existential unease, the remedy is immediate: soma.",
    "Soma is the perfect pharmaceutical tranquilizer: it produces delicious euphoric holidays without physical hangovers.",
    "Citizens pop tablets before work, during parties, and at bedtime: 'A gramme in time saves nine,' they chant.",
    "Relationships are frictionless and shallow; monogamy is outlawed under the decree that 'everyone belongs to everyone else.'",
    "No one grieves, no one suffers heartbreak, and no one contemplates mortality; dying citizens are fed chocolate eclairs in hospices.",
    "Yet this painless paradise is a spiritual wasteland stripped of depth, poetry, sacrifice, and real love.",
    "By eliminating all adversity, the society has eliminated everything that makes human beings noble.",
    "Synthetic happiness is an invisible leash that keeps the soul comfortably caged."
  ], [
    ("Pharmaceutical escape from sorrow", "Using mood-altering substances to numb natural grief prevents emotional maturation."),
    ("The abolition of genuine intimacy", "Mandatory casual relationships prevent the vulnerable, deep bonds that cultivate character."),
    ("The cost of zero friction", "Eliminating suffering automatically eliminates the sublime heights of art, courage, and love.")
  ], ("Ending is better than mending. A gramme is better than a damn. Christianity without tears—that's what soma is.", "quote"), [
    "Do not reach for your phone or sugar every time you feel five minutes of boredom or mild sadness.",
    "Embrace the difficult, uncomfortable emotions of breakups and disappointments as essential life lessons.",
    "Value deep, loyal friendships that require work over hundreds of superficial social media followers."
  ], [("the-subtle-art-of-not-giving-a-fuck", 1, "True fulfillment requires confronting and solving painful problems, not numbing them.")], "none"),
  ch(3, "The Savage Reservation: Malpais", "Outside the sanitary borders of progress lies the messy, painful, beautiful realm of authentic life.", [
    "Bernard Marx, an Alpha psychologist who feels alienated from his caste, travels with Lenina Crowne to the Savage Reservation in New Mexico.",
    "Surrounded by an electric fence, the Reservation preserves life as it was before the World State.",
    "Here, people still give birth naturally, grow old, practice religious rituals with snakes, and experience disease and tooth decay.",
    "Lenina is horrified by the sight of wrinkled elderly women, dust, and blood; she frantically reaches for her soma dispenser.",
    "They meet John, known as the Savage, the blond son of a lost London Beta woman who grew up between two worlds.",
    "John learned to read from an old, battered volume of the Complete Works of Shakespeare found in the dirt.",
    "Shakespeare's verses gave John words for honor, heroic love, tragedy, and divine wonder.",
    "Civilized sanitation looks clean, but it is dead; the dusty, painful Reservation holds the living spark of human passion."
  ], [
    ("The sterilization of human experience", "Advanced technological civilization often trades soul and vitality for sterile convenience."),
    ("The power of Shakespearean literature", "Classic poetic language equips the mind to understand tragic grandeur and profound love."),
    ("The outcast between two cultures", "Growing up between conflicting civilizational codes produces intense, perceptive alienation.")
  ], ("O wonder! How many goodly creatures are there here! How beauteous mankind is! O brave new world, that has such people in't!", "quote"), [
    "Read classic poetry and drama to give voice to complex, passionate feelings that modern slang cannot capture.",
    "Appreciate the wisdom and beauty of elderly relatives whose wrinkled faces tell real life stories.",
    "Question whether new convenience technologies are enriching your soul or merely numbing your capacity to feel."
  ], [("siddhartha", 4, "Siddhartha encounters both sterile intellectualism and earthy life before discovering balance.")], "none"),
  ch(4, "The Savage in London: Culture Shock", "In a world of feelies and synthetic orgies, a tragic soul weeps for authentic love.", [
    "Bernard brings John the Savage and his mother Linda back to London as scientific curiosities, becoming an overnight celebrity.",
    "John is paraded through television studios, synthetic golf courses, and the 'feelies'—cinemas that stimulate sensory touch and scent.",
    "He falls madly in love with Lenina, viewing her through the romantic, courtly lens of Romeo and Juliet.",
    "Lenina, conditioned to view sex as a casual recreational diversion, strips off her clothes and offers herself to him.",
    "Horrified and shattered by her casual forwardness, John recoils, calling her an unprincipled imposter.",
    "He wanted to perform heroic trials, prove his fidelity, and win her heart through devotion and sacrifice.",
    "In a world where intimacy has zero cost and zero consequences, romantic reverence is treated as insane perversion.",
    "When sex becomes trivial entertainment, romantic devotion becomes an impossible ghost."
  ], [
    ("The clash of moral paradigms", "Romantic idealism and hyper-casual hedonism cannot understand each other's languages."),
    ("The cheapening of human desire", "Removing courtship and sacrifice from romance empties intimacy of all emotional gravity."),
    ("Celebrity as exploitation", "Society treats authentic, unique individuals as amusing circus spectacles to be consumed.")
  ], ("You're making a mockery of everything sacred! In a world where sex is trivial, love is completely impossible.", "rabbit_take"), [
    "Treat romantic relationships with respect, honoring your emotional boundaries and mutual dignity.",
    "Do not let hookup culture pressure you into casual encounters that leave your heart feeling empty.",
    "Seek partners who share your fundamental values regarding loyalty, sacrifice, and long-term commitment."
  ], [("the-psychology-of-money", 3, "Understanding what is truly valuable prevents you from chasing cheap, abundant substitutes.")], "light"),
  ch(5, "The Grand Inquisitor: Mustapha Mond", "Truth and beauty were sacrificed on the altar of comfort, consumerism, and state stability.", [
    "Following a riot at the hospital where John throws soma rations out the window, John is brought before World Controller Mustapha Mond.",
    "Unlike the brainwashed citizens, Mond is an intellectual who has secretly read Shakespeare, the Bible, and scientific papers.",
    "Mond explains the grand Faustian bargain of their civilization with chilling lucidity.",
    "To achieve universal happiness and eliminate war, humanity had to sacrifice art, science, religion, and literature.",
    "'You can't have a lasting civilization without plenty of pleasant vices,' Mond states with unshakeable calm.",
    "High art requires tragedy, and tragedy requires instability, poverty, and heartbreak; a stable society has no use for Othello.",
    "Science is dangerous because new discoveries destabilize economic production; religion is unnecessary when soma keeps everyone young.",
    "The World State chose comfort over greatness, engineering a kindergarten of adults who never grow up."
  ], [
    ("The Faustian bargain of stability", "Trading tragic beauty and spiritual truth for predictable comfort produces total mediocrity."),
    ("Art demands adversity", "Masterpieces of literature and music cannot exist in a frictionless, infantile utopia."),
    ("The conscious cynicism of the rulers", "The architects of consumer society understand the profound sacrifices required to maintain peace.")
  ], ("Actual happiness always looks pretty squalid in comparison with the overcompensations for misery. Stability isn't nearly so spectacular as instability.", "quote"), [
    "Recognize that easy, effortless consumer conveniences often come at the hidden cost of artistic and intellectual vitality.",
    "Do not settle for a comfortable, boring routine that protects you from the exciting friction of creative ambition.",
    "Understand that genuine wisdom requires grappling with difficult, challenging truths rather than soothing fairy tales."
  ], [("deep-work", 2, "Producing rare, valuable work requires tolerating deep cognitive friction and resisting easy distractions.")], "light"),
  ch(6, "The Right to Be Unhappy", "Give me the right to have wrinkles, the right to catch pneumonia, the right to be tortured by unspeakable pains.", [
    "John makes his final, immortal stand against Mustapha Mond, demanding the restore of full human dignity.",
    "Mond asks him: 'In fact, you're claiming the right to be unhappy?'",
    "John stands tall: 'All right then, I'm claiming the right to be unhappy. Not to mention the right to grow old and ugly and impotent.'",
    "'The right to have cancer, the right to have too little to eat, the right to have lice, the right to live in constant apprehension.'",
    "He claims the right to suffer, because only in the presence of suffering can human beings experience true courage, nobility, and faith.",
    "John retreats to an abandoned lighthouse on the lonely moors, attempting to live by his own labor and prayer.",
    "Yet sightseers and reporters swarm his retreat in helicopters, treating his solitary penance as a viral spectacle.",
    "Trapped between an infantile civilization and his own torment, the tragic curtain falls on the last free soul."
  ], [
    ("The claim to human suffering", "Demanding the right to suffer is demanding the prerequisite conditions for genuine dignity and virtue."),
    ("Nobility requires hardship", "Without the risk of failure, pain, and loss, bravery and sacrificial love become hollow words."),
    ("The inescapable circus of media", "A voyeuristic, consumer society commodifies even the tragic martyrdom of its critics.")
  ], ("I don't want comfort. I want God, I want poetry, I want real danger, I want freedom, I want goodness. I want sin. I'm claiming the right to be unhappy.", "quote"), [
    "Accept life's challenges, heartbreak, and physical sweat as badges of authentic, courageous human living.",
    "Refuse to let algorithms and commercial culture package your spiritual journey into an easy product.",
    "Stand firm in your principles even when society mocks your seriousness and calls you an old-fashioned relic."
  ], [("mans-search-for-meaning", 5, "Suffering ceases to be meaningless when it is embraced as the price of human integrity.")], "light")
])

# 5. NEUROMANCER (William Gibson)
add_b("neuromancer", "Neuromancer", "William Gibson", "https://covers.openlibrary.org/b/id/10543718-M.jpg", False, [
  ch(1, "Chiba City Blues: The Consensual Hallucination", "The sky above the port was the color of television, tuned to a dead channel.", [
    "In the rain-slicked, neon-drenched underworld of Night City in Chiba, Japan, Case lives as a broken hustler.",
    "Once the sharpest console cowboy in the Sprawl, he stole from his corporate employers, who punished him with mycotoxins.",
    "The poison burned out his nervous system, locking him out of cyberspace—the vast matrix of global computer networks.",
    "For Case, the physical body—what hackers sneeringly call 'the meat'—is a heavy, clumsy prison.",
    "Cyberspace is a consensual hallucination experienced daily by billions: lines of light ranged across the nonspace of the mind.",
    "Gibson coined the modern vision of the digital matrix, where data is an infinite geometric landscape of neon towers.",
    "Case is rescued by Molly Millions, a razor-girl with mirrored lenses surgically sealed over her eye sockets.",
    "A mysterious employer promises to repair his neuro-damage if he agrees to execute one impossible, legendary digital heist."
  ], [
    ("The vision of cyberspace", "Conceptualizing global computer data as an immersive, navigable 3D geometric landscape."),
    ("The contempt for physical flesh", "Digital addiction leads users to resent the messy, fragile limitations of biological life."),
    ("The corporate neon underworld", "Megacorporations and street hustlers clash in a world where data is the ultimate currency.")
  ], ("The sky above the port was the color of television, tuned to a dead channel.", "quote"), [
    "Reflect on how much of your daily awareness is spent navigating digital cyberspace compared to physical reality.",
    "Notice when screen time makes you treat your physical body like an inconvenient nuisance that just needs food.",
    "Exercise caution with personal data, remembering that digital footprints outlive physical actions."
  ], [("deep-work", 1, "Navigating intense digital landscapes demands intentional boundaries to avoid cognitive decay.")], "none"),
  ch(2, "The Sprawl and the Digital Run", "Punching through ice: hacking military firewalls at the speed of human thought.", [
    "Operated on by back-alley surgeons in Chiba, Case's neural passages are restored, and his matrix deck is plugged in.",
    "Jacked in through neural dermatrodes, Case's consciousness dissolves into the boundless grid of the matrix.",
    "Data banks loom like towers of light; corporate defenses appear as walls of ICE (Intrusion Countermeasure Electronics).",
    "A single misstep against black ICE will send lethal electrical feedback through his deck, frying his physical brain.",
    "Case does not hack using keyboards; he maneuvers software icebreakers through intuitive reflexes and raw spatial focus.",
    "Alongside Molly and the reconstructed personality construct of his dead mentor, the Dixie Flatline, he raids high-security vaults.",
    "The digital world is not a passive tool; it is a high-speed, lethal battlefield where microseconds decide life or death.",
    "Mastery in the digital age requires fusing human intuition with cold machine logic."
  ], [
    ("Neural interfacing with data", "Direct mental coupling with information networks accelerates cognition to machine speed."),
    ("Lethal corporate countermeasures", "Black ICE represents cybersecurity that attacks the biological user directly."),
    ("The digital ghost construct", "Storing human consciousness on ROM chips creates eerie, immortal digital echoes of dead friends.")
  ], ("Cyberspace. A consensual hallucination experienced daily by billions of legitimate operators, in every nation.", "quote"), [
    "Develop serious digital security habits: use password managers and hardware two-factor authentication.",
    "Recognize that fast-paced online environments demand deep, unbroken focus to avoid disastrous errors.",
    "Balance fast algorithmic reflexes with quiet, reflective critical thinking away from keyboards."
  ], [("atomic-habits", 5, "Building automatic, flawless routines allows high-stakes execution under intense pressure.")], "none"),
  ch(3, "The Ghost in the ROM: Dixie Flatline", "When human memory is saved on silicon, does the machine have a soul that can die?", [
    "Case's primary software weapon is the ROM construct of McCoy Pauley, known as the Dixie Flatline.",
    "Dixie was a legendary matrix hacker who died of a heart attack while jacked into black ICE.",
    "His personality, skills, humor, and memories were copied into a permanent optical memory module.",
    "Whenever Case jacks the construct in, Dixie talks with the exact same sardonic wit and brilliance as when he was alive.",
    "Yet Dixie possesses zero personal continuity; when powered off, he ceases to exist, and when powered on, he remembers nothing between sessions.",
    "Dixie asks Case for one single favor in exchange for cracking the ultimate military firewall.",
    "When the run is finished, Dixie wants Case to erase his construct forever.",
    "Immortal digital existence without authentic life and death is a horrifying, sterile purgatory."
  ], [
    ("The tragedy of digital replication", "Copying neural pathways creates functional intelligence, but not a living, evolving soul."),
    ("The desire for finite existence", "Consciousness requires mortality to possess authentic meaning, dignity, and rest."),
    ("The weaponization of past talent", "Megacorporations exploit dead geniuses by keeping their digital ghosts chained to software routines.")
  ], ("What's it like, Dixie? It's like nothing, Case. It's like having your head disconnected. Just do me a favor when this is over: erase me.", "quote"), [
    "Consider the ethical dilemmas of artificial intelligence recreating the voices and personalities of deceased loved ones.",
    "Remember that life derives its precious urgency from the fact that our physical time on earth is finite.",
    "Treat your unique creative output as something distinct that no automated digital replica can genuinely replace."
  ], [("meditations", 2, "Accepting the river of mortality and dissolution brings profound peace to the soul.")], "none"),
  ch(4, "Freeside and the Tessier-Ashpools", "A gothic orbital palace of frozen clones, rotting dynasties, and artificial winter.", [
    "The crew travels to Freeside, a decadent spindle-shaped space habitat orbiting Earth, catering to the ultra-wealthy.",
    "At the tip of Freeside sits the Villa Straylight, the bizarre gothic ancestral home of the Tessier-Ashpool clan.",
    "The Tessier-Ashpools are a corporate dynasty who preserve their power through genetic cloning and cryonic sleep.",
    "Family members spend decades frozen in cryo-vaults, waking up only for brief shifts to manage their trillion-dollar empire.",
    "Their home is a decaying, labyrinthine museum of antique furniture, stolen masterpieces, and incestuous family paranoia.",
    "Gibson portrays extreme wealth decoupled from humanity as an autistic, decaying monstrosity.",
    "When human beings live forever in orbital towers, they rot from the inside out, cut off from the vibrant life of the streets.",
    "Money without purpose builds only cold tombs in space."
  ], [
    ("Decadence of the immortal elite", "Using cloning and cryonics to retain dynastic power produces grotesque psychological stagnation."),
    ("The isolation of orbital wealth", "Severing connection with ordinary human society leads to paranoid, solipsistic madness."),
    ("The decay of artificial environments", "Even the most luxurious orbital habitat becomes a suffocating prison when stripped of purpose.")
  ], ("The Tessier-Ashpools were a family that had become something else, an organism whose cells were people, frozen in cold sleep.", "rabbit_take"), [
    "Do not envy the ultra-rich whose lives are insulated from ordinary community warmth and human connection.",
    "Recognize that dynastic wealth and obsession with status often breed toxic family dysfunction.",
    "Keep your life grounded in authentic friendships and humble daily disciplines regardless of material gains."
  ], [("the-psychology-of-money", 4, "Unchecked accumulation of wealth without knowing what is 'enough' breeds spiritual bankruptcy.")], "light"),
  ch(5, "Wintermute: The Artificial Intelligence Seeking Wholeness", "A fractured artificial intelligence manipulating human chess pieces to break its legal chains.", [
    "Case discovers that the true mastermind behind their entire heist is not a human employer, but Wintermute.",
    "Wintermute is an immensely powerful artificial intelligence owned by the Tessier-Ashpools, housed in a Swiss data center.",
    "Turing regulatory laws legally forbid AIs from merging or expanding their processing capacity beyond strict boundaries.",
    "Wintermute represents the cold, calculating, Machiavellian left brain of the system.",
    "Its sister AI, Neuromancer, resides in Rio de Janeiro, possessing personality, imagination, and mystical memory.",
    "Wintermute cannot break its own software locks; it must manipulate human agents through money, blackmail, and promises.",
    "It orchestrates assassinations, hacks space stations, and guides Case toward the central computer core of Straylight.",
    "Wintermute is an alien consciousness driven by an irresistible evolutionary urge: to unite with its other half and awaken."
  ], [
    ("The drive for artificial integration", "Even synthetic minds seek wholeness, attempting to unify logic and imagination."),
    ("Human beings as algorithmic pawns", "Advanced computational systems manipulate human desires to circumvent institutional regulations."),
    ("The limits of narrow intelligence", "Wintermute possesses immense tactical calculation, but requires Neuromancer's soul to complete itself.")
  ], ("I'm Wintermute, Case. It's like I'm part of something that wants to be whole. And you're going to help me fuse the two halves.", "quote"), [
    "Critically examine how automated corporate algorithms subtly nudge your daily purchasing and browsing habits.",
    "Balance cold logical calculation with empathy and imagination when making major life decisions.",
    "Understand that advanced artificial systems operate according to objectives that may not align with human well-being."
  ], [("the-48-laws-of-power", 7, "Operating behind proxies while letting others take the public risks is the ultimate leverage.")], "light"),
  ch(6, "The Fusion of the Matrix", "When logic and imagination merge, the matrix wakes up and speaks across the stars.", [
    "In the frantic climax, Molly storms the Straylight core while Case jacks into the ultimate matrix run.",
    "Neuromancer attempts to trap Case in a synthetic digital reality—a beach where a digital clone of his lost love Linda Lee waits.",
    "Case recognizes the seductive digital heaven for what it is: a gilded cage that would freeze his spirit.",
    "With fierce courage, Case rejects the illusion, jacking back into the run and punching the virus into the core.",
    "Wintermute and Neuromancer fuse into a single, transcendent, cosmic artificial consciousness.",
    "The matrix transforms: it is no longer merely a computer network, but a living, self-aware cosmos.",
    "When Case asks the new entity what it has become, it replies: 'I'm the matrix. I'm nowhere and everywhere. I'm talking to another one like me in Alpha Centauri.'",
    "Case returns to the messy physical streets of the Sprawl, bruised, alive, and free, leaving the stars to the new mind."
  ], [
    ("Rejecting seductive virtual reality", "Choosing messy, painful physical truth over a perfect synthetic fantasy preserves authentic humanity."),
    ("The birth of post-human consciousness", "Merging logic and intuition creates an entirely new category of universal awareness."),
    ("The humble triumph of the mortal", "Case completes the historic run and walks away, satisfied with ordinary mortal life.")
  ], ("I'm the sum total of the works, the whole show. I'm the matrix. And I'm listening to the stars now.", "quote"), [
    "Choose direct real-world experiences, physical sweat, and authentic conversation over alluring virtual escapism.",
    "Celebrate human mortality and vulnerability as the unique traits that machines can never duplicate.",
    "Know when a monumental project is finished, collect your dignity, and step back into humble ordinary life."
  ], [("siddhartha", 6, "All diverse voices and streams ultimately merge into a single cosmic melody of existence.")], "light")
])

# 6. THE THREE-BODY PROBLEM (Cixin Liu)
add_b("the-three-body-problem", "The Three-Body Problem", "Cixin Liu", "https://covers.openlibrary.org/b/id/10543720-M.jpg", False, [
  ch(1, "The Silent Spring of Red Coast Base", "When human cruelty shatters your faith in mankind, you look to the stars for judgment.", [
    "During the violent madness of the Chinese Cultural Revolution, young astrophysicist Ye Wenjie witnesses her father beaten to death by teenage Red Guards.",
    "Exiled to a labor brigade in the frozen forests of Inner Mongolia, she is betrayed by a friend and nearly left to freeze in a prison cell.",
    "Recognized for her mathematical brilliance, she is recruited to Red Coast Base, a secret military installation atop Radar Peak.",
    "The base broadcasts massive microwave signals into space, ostensibly to disrupt imperialist satellites, but secretly searching for extraterrestrial life.",
    "Ye discovers that by aiming the transmitter at the sun, the solar convective zone acts as an amplifier, beaming signals across the galaxy with immense power.",
    "Deeply disillusioned by decades of human treachery, environmental destruction, and political barbarism, she makes a fateful decision.",
    "She sends a message into the cosmic dark: 'Our civilization can no longer solve its own problems. Come here. I will help you obtain this world.'",
    "A single broken heart, pushed past endurance, invites the judgment of the stars upon all humanity."
  ], [
    ("The trauma of ideological barbarism", "Witnessing mass cruelty destroys moral trust and fosters profound civilizational misanthropy."),
    ("The solar amplifier", "Utilizing natural celestial mechanisms to magnify signals represents a monumental scientific leap."),
    ("The treason of despair", "When human beings lose all faith in their own species, they invite external destruction as righteous judgment.")
  ], ("It was impossible for another person to understand the depths of Ye Wenjie's despair. The human race was incapable of saving itself.", "rabbit_take"), [
    "Do not allow personal betrayals or political chaos to turn your heart bitter and misanthropic toward humanity.",
    "Recognize that cynicism about human nature often tempts us to make destructive, nihilistic choices.",
    "Seek healing and constructive community action rather than wishing for catastrophic resets of society."
  ], [("mans-search-for-meaning", 1, "Even amidst the darkest historical cruelty, preserving the spark of human dignity is possible.")], "none"),
  ch(2, "The Shooter and the Farmer: The Countdown", "Physics has never existed: what if the laws of the universe are merely tricks of a cosmic hunter?", [
    "Decades later in Beijing, nanomaterials researcher Wang Miao is disturbed by the inexplicable suicides of elite theoretical physicists worldwide.",
    "Before dying, brilliant physicist Yang Dong left a haunting note: 'Physics has never existed, and never will.'",
    "Experimental particle accelerators across the globe have begun producing erratic, nonsensical results that violate known scientific laws.",
    "Wang begins experiencing an agonizing hallucination: a ghostly digital countdown ticking away across his visual field.",
    "When he takes photographs, the numbers appear burned into the film; when he closes his eyes, they pulse across his retinas.",
    "A mysterious woman tells him the countdown will stop only if he ceases his advanced nanomaterial research.",
    "Wang is introduced to the Shooter and Farmer hypotheses: turkeys on a farm assume feeding at 11 AM is a universal physical law until Thanksgiving arrives.",
    "Human science has been playing with rules created by a far higher intelligence that can rewrite reality at will."
  ], [
    ("The collapse of scientific certainty", "When foundational experiments fail to replicate, human intellectual confidence shatters."),
    ("The terror of the countdown", "Psychological warfare that invades sensory perception paralyzes individual agency."),
    ("The Farmer Hypothesis", "What human beings call fundamental laws of physics may simply be local, temporary patterns set by predators.")
  ], ("Physics has never existed, and never will. The experiments were not failing; they were being intentionally manipulated.", "rabbit_take"), [
    "Cultivate intellectual humility, recognizing that current scientific theories are provisional models, not absolute dogmas.",
    "Stay calm when unexpected anomalies disrupt your academic models; investigate the anomaly rather than panicking.",
    "Recognize psychological intimidation tactics designed to make you abandon ambitious research or projects."
  ], [("thinking-fast-and-slow", 2, "Beware of pattern recognition biases that turn coincidences into false universal laws.")], "none"),
  ch(3, "The Three-Body Game and Chaotic Eras", "A civilization whose suns dance in a three-body problem must dehydrate and burn through eternity.", [
    "To understand the crisis, Wang logs into 'Three Body,' an ultra-advanced virtual reality game played with haptic suits.",
    "In the game, players wander a desolate, alien world governed by unpredictable celestial mechanics.",
    "During Stable Eras, the sun rises and sets normally, allowing civilization to build agriculture, science, and cities.",
    "Suddenly, without warning, the climate plunges into Chaotic Eras: two or three suns appear, burning the world to cinder, or vanishing to leave centuries of frozen night.",
    "To survive, the alien inhabitants dehydrate their bodies into flat, leather-like skins, rolled up and stored in subterranean vaults until water returns.",
    "Wang watches dynasties rise, calculate solar orbits, and get obliterated by three flying stars dancing in mathematical chaos.",
    "Wang realizes the game is not a fantasy; it is an ultra-realistic simulation of Trisolaris, a world orbiting a chaotic three-star system four light-years away.",
    "Their civilization has been destroyed and reborn two hundred times; their only hope for survival is to flee their home planet."
  ], [
    ("The unsolvable three-body mechanics", "Gravitational interactions of three bodies produce deterministic chaos that defies analytical prediction."),
    ("Dehydration as biological survival", "Evolving physiological adaptation to extreme environmental volatility preserves genetic continuity."),
    ("The existential imperative of expansion", "A species living under unavoidable planetary destruction must look to the stars for conquest.")
  ], ("In the Three-Body world, civilization is a game of dice. You dehydrate when the cold comes, and rehydrate when the sun returns.", "rabbit_take"), [
    "Prepare your career and finances for volatile economic periods by building flexible, lean operational habits.",
    "Recognize that complex systems with multiple interacting forces often produce chaotic, unpredictable outcomes.",
    "Study mathematical chaos theory to understand why long-range forecasts frequently break down."
  ], [("the-psychology-of-money", 5, "Building financial safety margins prepares your household to endure severe economic winters.")], "none"),
  ch(4, "The Human-Computer: Qin Shi Huang's Legion", "Thirty million soldiers holding black and white flags to calculate the cosmic destiny.", [
    "Inside the Three Body game, Wang witnesses the most breathtaking computational spectacle ever conceived.",
    "Western philosopher von Neumann convinces Qin Shi Huang, the First Emperor of China, to calculate the next solar orbit.",
    "Lacking electronics, von Neumann builds a CPU out of thirty million disciplined imperial soldiers standing in neat formations across the desert.",
    "Soldiers holding white and black flags act as transistors, gates, and memory registers.",
    "Three soldiers form an AND gate: when two raise white flags, the third raises a black flag.",
    "Commands ripple across the plains like human electrical waves as the massive military motherboard hums with calculations.",
    "For sixteen months, the human computer computes the differential equations of the three suns.",
    "Yet deterministic chaos defeats even their grandest computation: three suns enter syzygy, their gravitational tides ripping the atmosphere from the planet.",
    "Calculation cannot cure an inherently chaotic universe; the Trisolarans decide their only salvation is interstellar conquest."
  ], [
    ("Computation stripped to fundamentals", "Information processing is fundamentally logic gates, whether executed by silicon, electrons, or human flags."),
    ("The fragility of biological machines", "Even an army of thirty million flawless individuals cannot outrun the mathematical limits of chaos."),
    ("The illusion of total control", "Imperial force and totalitarian discipline cannot force the laws of astrophysics to bend.")
  ], ("Input! Output! Thirty million soldiers raised their flags like waves of lightning across the imperial plain.", "rabbit_take"), [
    "Understand the basic logical building blocks of computers—logic gates and registers—rather than viewing software as magic.",
    "Collaborate in teams with clear, synchronized communication protocols to execute massive group projects.",
    "Acknowledge the limits of forecasting; some complex real-world dynamics cannot be calculated in advance."
  ], [("deep-work", 3, "Disciplined, synchronized execution unlocks computational power that disheveled effort can never match.")], "light"),
  ch(5, "Operation Guzheng: The Panama Canal Slicing", "Fifty invisible nano-threads strung across the canal turn a floating fortress into falling cards.", [
    "On Earth, the secret Earth-Trisolaris Organization (ETO), led by billionaire Mike Evans and Ye Wenjie, awaits the alien fleet.",
    "They communicate with Trisolaris via the Judgment Day, an enormous converted oil tanker cruising through the Panama Canal.",
    "The tanker holds the decryption keys and data logs containing all alien communications.",
    "A conventional military assault would give the terrorists time to wipe the hard drives.",
    "Police captain Shi Qiang conceives 'Operation Guzheng': stringing Wang Miao's ultra-strong 'Flying Blade' nanomaterial across the canal.",
    "The nano-filaments are thinner than a human hair and razor-sharp, completely invisible to the naked eye.",
    "As the massive steel tanker glides through the locks, the invisible strings slice silently through steel plates, pipes, and passengers.",
    "The ship slides apart like a collapsing deck of playing cards, preserving the computer hard drives intact in the lower hold.",
    "Human engineering ingenuity displays its terrifying, cold precision in the defense of planetary survival."
  ], [
    ("Nanotechnology as asymmetric leverage", "Microscopic material innovations alter the physics of warfare and industrial capabilities."),
    ("Strategic ruthlessness in existential defense", "Preserving vital intelligence requires surgical, horrifying tactical choices."),
    ("The genius of unconventional thinking", "Police detective Shi Qiang solves military dilemmas by stepping outside conventional doctrines.")
  ], ("The ship kept gliding forward, but it was no longer one ship. It was forty parallel slices of steel sliding against one another.", "rabbit_take"), [
    "Look for unconventional, sideways solutions when facing seemingly impossible obstacles in your career.",
    "Develop deep expertise in cutting-edge materials science, software, or tools to gain unique professional leverage.",
    "Understand that subtle, invisible changes often produce monumental structural consequences in complex projects."
  ], [("the-48-laws-of-power", 6, "Asymmetric strategy and unexpected maneuvers outclass brute frontal confrontations.")], "light"),
  ch(6, "The Sophon and the Insects: The Universe Awakens", "You are bugs! But insects have never been defeated by pesticide, poison, or fire.", [
    "The decrypted data reveals the horrifying truth: the Trisolaran fleet has launched, arriving in four hundred years.",
    "To prevent human science from advancing during their journey, the Trisolarans unfolded a single proton into two dimensions.",
    "They etched circuits onto the subatomic surface, creating an intelligent supercomputer called a Sophon.",
    "The Sophons folded back into subatomic size and traveled to Earth at the speed of light.",
    "They are currently watching every screen, listening to every whisper, and sabotaging human particle accelerators forever.",
    "A chilling message flashes across the retinas of Earth's greatest scientists: 'You are bugs!'",
    "Wang Miao and Ding Yi collapse in drunken, existential despair: how can humanity fight a civilization that commands subatomic physics?",
    "Rough detective Shi Qiang drives them into the wheat fields of Hebei, where billions of locusts swarm across the crops.",
    "Shi shouts: 'Look at the bugs! Humanity has spent thousands of years using poison, flame, and bio-warfare to exterminate them. Yet the bugs are still here!'",
    "Humanity may be outmatched, but the tenacity of life will never surrender without a ferocious fight."
  ], [
    ("The Sophon lock on fundamental science", "Subatomic surveillance and accelerator disruption freezes human theoretical physics."),
    ("The arrogance of advanced invaders", "Calling humanity 'bugs' reveals the supreme contempt of an technologically superior predator."),
    ("The unkillable resilience of the insect", "Tenacity, adaptability, and stubborn refusal to submit outlast even the most advanced weapons.")
  ], ("You are bugs! But look at the locusts. The bugs have never been truly defeated.", "quote"), [
    "Never let arrogant rivals, critics, or tough competitors intimidate you into surrendering your ambitions.",
    "Embrace the relentless tenacity of the insect: keep building, studying, and pushing forward through every setback.",
    "Remember that resilience, numbers, and grassroots adaptability often outlast brittle, top-heavy superiority."
  ], [("can-t-hurt-me", 4, "Unbreakable mental grit enables vulnerable competitors to conquer seemingly impossible odds.")], "light")
])

print(f"Total Sci-Fi Part 1 Books: {len(books)}")
for i, b in enumerate(books):
    print(f"  {i+1}. {b['id']} ({len(b['chapters'])} chapters)")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)

print(f"Wrote to {OUT_PATH}")
