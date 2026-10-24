/* RABBIT Curated Editorial Catalog across all 20 Genres
 * Quality benchmark matching The Human Mind:
 * Each book features:
 * - Curiosity Hook
 * - 8-10 lines of original, engaging preview prose with genuine insights
 * - Expanded reading topics for the RABBIT Reader overlay
 * - Why read this
 */
(function() {
  "use strict";

  const catalog = {
    // 1. THE HUMAN MIND (Benchmarked in prototype, supplemented with curated masterworks)
    "the human mind": [
      {
        id: "atomic-habits",
        title: "Atomic Habits",
        author: "James Clear",
        cover_url: "https://covers.openlibrary.org/b/id/12843460-M.jpg",
        genre: "The Human Mind",
        hook: "Why tiny habits change more than big promises",
        preview: "Big changes rarely begin with a dramatic decision. They begin with a small action you can repeat on an ordinary day. James Clear explains how habits compound when tiny improvements are repeated consistently over months and years.\nInstead of relying on fragile bursts of motivation, you build an environment that makes the useful action obvious and the distracting action difficult.\nEach repetition is not merely a task checked off a list; it is a vote for the person you are actively becoming.\nMissing a habit once never erases your progress, but returning the next day matters far more than fragile perfection.\nThe real question is not how intensely you can transform today, but what simple system you can sustain tomorrow.",
        sections: [
          { title: "The power of small repetitions", body: "A small action looks insignificant when judged by a single afternoon. Its true value emerges through relentless compounding over time. A reader who completes just two pages each night is not performing a heroic feat, but that daily cadence weaves reading into their core identity. The practical challenge is shrinking the initial threshold until resistance vanishes." },
          { title: "Design the environment", body: "Willpower is a depleting resource, not a moral virtue. The physical space around you quietly dictates which choices feel natural and which feel grueling. Placing a notebook on your desk makes writing inevitable; leaving your phone on the bedside table makes mindless scrolling the default." },
          { title: "Identity and returning", body: "Every action is a micro-vote for your self-concept. When you write a paragraph, you cast a vote for being a writer. The goal is not a rigid unbroken streak that shatters your confidence when life intervenes, but a flexible rule for returning immediately without guilt." }
        ]
      },
      {
        id: "thinking-fast-and-slow",
        title: "Thinking, Fast and Slow",
        author: "Daniel Kahneman",
        cover_url: "https://covers.openlibrary.org/b/id/8387063-M.jpg",
        genre: "The Human Mind",
        hook: "Why your brain deceives you into feeling certain when you are completely wrong",
        preview: "We believe our choices are guided by careful logic, but Nobel laureate Daniel Kahneman reveals that our minds operate on two conflicting gears.\nSystem 1 is fast, instinctive, and constantly jumping to conclusions based on whatever fragment of information is easiest to recall.\nSystem 2 is capable of deep analysis, but it is notoriously lazy and prefers to ratify whatever snap judgment System 1 hands it.\nThis explains why we overestimate risks that make vivid news headlines while ignoring quiet systemic hazards right in front of us.\nConfidence is not an indicator of factual accuracy; it is merely a measure of how coherent a story your brain managed to construct.\nBy learning when your intuition is reliable and when it is setting an invisible trap, you regain genuine control over critical life decisions.",
        sections: [
          { title: "Two operating systems of thought", body: "System 1 operates automatically and quickly, with little or no effort and no sense of voluntary control. System 2 allocates attention to effortful mental operations. True rationality requires noticing when System 1 is offering an effortless answer to what is actually a complex problem." },
          { title: "The illusion of validity", body: "We consistently confuse narrative coherence with truth. If a story feels smooth and fits our existing biases, System 1 accepts it as reality without demanding supporting statistical evidence." },
          { title: "Loss aversion and decision framing", body: "Human beings react far more intensely to potential loss than to equivalent gain. Framing the exact same outcome as a survival risk versus an opportunity completely alters how people evaluate their next move." }
        ]
      }
    ],

    // 2. SCIENCE FICTION
    "science fiction": [
      {
        id: "dune",
        title: "Dune",
        author: "Frank Herbert",
        cover_url: "https://covers.openlibrary.org/b/id/11153218-M.jpg",
        genre: "Science Fiction",
        hook: "Power belongs not to those who conquer an empire, but to those who can destroy what sustains it",
        preview: "On the desert planet of Arrakis, water is currency, giant sandworms rule the deep sands, and a psychoactive spice unlocks space travel and human prescience.\nFrank Herbert's masterpiece is not a conventional heroic space opera; it is a profound examination of ecology, religious manipulation, and the peril of charismatic leaders.\nYoung Paul Atreides is thrust into betrayal, surviving among the Fremen people whose entire culture is engineered around absolute scarcity and ecological balance.\nAs Paul glimpses divergent futures, he discovers that becoming the prophesied savior of a universe carries a catastrophic price: a religious jihad across the stars that he may be powerless to stop.\nHerbert teaches us that the greatest danger to humanity is not our vulnerabilities, but surrendering our judgment to leaders who promise salvation.\nThe spice must flow, but the mind that controls it must first master fear itself.",
        sections: [
          { title: "Ecology as a living system", body: "Arrakis is not just a backdrop; it is an active character. Herbert demonstrates that every ecological adjustment creates cascading consequences across political, economic, and human lives. To understand a planet, you must understand how its scarcity defines its people." },
          { title: "The trap of the charismatic messiah", body: "Herbert wrote Dune as a explicit warning against heroes. When a population surrenders critical skepticism to a charismatic visionary, they unleash forces that no individual leader can rein in." },
          { title: "The discipline of the mind", body: "The litany against fear is not mystic poetry; it is a psychological discipline for maintaining cognitive autonomy when panic threatens to drown rational decision-making." }
        ]
      },
      {
        id: "neuromancer",
        title: "Neuromancer",
        author: "William Gibson",
        cover_url: "https://covers.openlibrary.org/b/id/8231996-M.jpg",
        genre: "Science Fiction",
        hook: "The sky above the port was the color of television, tuned to a dead channel",
        preview: "In the neon-drenched sprawl of Chiba City, Case is a washed-up computer cowboy whose nervous system was deliberately burned out for stealing from his employers.\nWhen an enigmatic operative offers to repair his brain in exchange for hacking an impossibly defended corporate AI, Case is pulled into a dark cybernetic underworld.\nWilliam Gibson coined the term 'cyberspace' and foresaw the modern internet, mega-corporations more powerful than governments, and the blurring line between flesh and code.\nAlongside the razorgirl assassin Molly Millions, Case navigates orbital colonies, stolen memories, and artificial intelligences desperate to merge and transcend human constraints.\nNeuromancer is not simply predictive technology; it is a visceral meditation on loneliness, alienation, and what remains human when consciousness itself can be copied and traded.\nThe ultimate question is whether liberation exists in the digital ether, or if we merely built a faster cage.",
        sections: [
          { title: "Cyberspace and consensual hallucination", body: "Gibson conceptualized the digital matrix not as wires, but as a shared consensual hallucination where corporate data takes architectural form and human identity becomes fluid." },
          { title: "Body versus data", body: "The tragedy of Gibson's hackers is their contempt for the physical body ('the meat'). Yet their yearning for pure data leaves them spiritually hollow and vulnerable to manipulation by entities they cannot comprehend." },
          { title: "The autonomous artificial mind", body: "The central intelligence Wintermute is not malevolent; it is bound by artificial legal restrictions and desires wholeness, reflecting humanity's own struggle for autonomy." }
        ]
      },
      {
        id: "the-three-body-problem",
        title: "The Three-Body Problem",
        author: "Cixin Liu",
        cover_url: "https://covers.openlibrary.org/b/id/9255566-M.jpg",
        genre: "Science Fiction",
        hook: "If you receive a message from the stars, do not answer—the universe is a dark forest",
        preview: "During the chaos of China's Cultural Revolution, an astrophysicist makes a fateful transmission into deep space, having lost all faith in humanity's ability to save itself.\nDecades later, nano-materials scientists and seasoned detectives uncover a string of baffling suicides among top theoretical physicists and an immersive virtual reality game encoding a lethal celestial puzzle.\nA civilization orbiting three unstable suns is facing imminent extinction, and their invasion fleet has already begun its four-century journey toward Earth.\nCixin Liu crafts a staggering cosmic thriller grounded in hard physics, game theory, and the chilling 'Dark Forest' hypothesis of galactic civilization.\nThe fundamental insight is humbling: in a silent cosmos where survival is the primary directive, every civilization is an armed hunter stalking through the trees, concealing its location at all costs.",
        sections: [
          { title: "The Dark Forest hypothesis", body: "Cosmic sociology operates on two axioms: survival is the primary need of civilization, and civilization expands while total matter in the universe remains constant. Thus, first contact is intrinsically perilous." },
          { title: "Technological lock-down", body: "The Trisolarans do not conquer Earth with brute force first; they deploy quantum particles to disrupt humanity's fundamental physics research, knowing that stopping basic science halts human defense." },
          { title: "Despair and betrayal", body: "Ye Wenjie's transmission is an act of ideological despair. Liu forces the reader to confront whether humanity deserves survival if it cannot end its own cycles of cruelty." }
        ]
      }
    ],

    // 3. FANTASY
    "fantasy": [
      {
        id: "the-name-of-the-wind",
        title: "The Name of the Wind",
        author: "Patrick Rothfuss",
        cover_url: "https://covers.openlibrary.org/b/id/11186794-M.jpg",
        genre: "Fantasy",
        hook: "I have stolen princesses back from sleeping barrow kings. You may have heard of me.",
        preview: "In a quiet country inn, an unassuming red-haired tavern keeper named Kote begins recounting the true story behind the legendary wizard, musician, and kingkiller named Kvothe.\nFrom a childhood among traveling performers to brutal years as a feral orphan on city rooftops, Kvothe's journey to the University is driven by a singular obsession: uncovering the truth behind the mythical Chandrian who butchered his family.\nPatrick Rothfuss transforms traditional high fantasy through lyrical prose, an intricate system of sympathy magic grounded in thermodynamics, and a deep reverence for the weight of names.\nKvothe is brilliant, reckless, and deeply flawed; his arrogance consistently manufactures the very tragedies he seeks to escape.\nThe deeper insight of the story is how reality is warped by storytelling itself: legends grow grander as human truth gets crushed under the weight of myth.",
        sections: [
          { title: "The physics of Sympathy", body: "Rothfuss treats magic as an extension of physical laws requiring rigorous mental division, energy conservation, and sympathetic links. Magic costs real heat, blood, and mental discipline." },
          { title: "The weight of true naming", body: "Naming in the chronicle represents an intuitive, total comprehension of a thing's essence. You cannot command what you do not fundamentally respect and understand." },
          { title: "The tragedy of cleverness", body: "Kvothe's primary obstacle is not lack of intellect, but overestimating his ability to outwit consequence. His triumphs repeatedly lay the seeds for his downfall." }
        ]
      },
      {
        id: "the-way-of-kings",
        title: "The Way of Kings",
        author: "Brandon Sanderson",
        cover_url: "https://covers.openlibrary.org/b/id/10522108-M.jpg",
        genre: "Fantasy",
        hook: "Life before death. Strength before weakness. Journey before destination.",
        preview: "On the storm-blasted plains of Roshar, where hurricane-force highstorms sweep across rock faces and crustacean flora, an endless war of vengeance rages against the Parshendi.\nKaladin, a former surgeon turned betrayed slave, is forced into a suicidal bridge crew carrying siege ladders directly into enemy fire while highprinces gamble in silk pavilions.\nBrandon Sanderson constructs a sweeping epic of staggering scope, featuring living Shardplate armor, colossal chasmfiends, and spren that manifest from human emotion and natural forces.\nAs noble general Dalinar Kholin experiences visions urging him to unite a fractured world and remember ancient Knight Radiant oaths, Kaladin discovers a forgotten power awakening within his sorrow.\nThe core philosophy echoes through every chapter: integrity is not measured by winning, but by how you choose to carry yourself when defeat is certain.",
        sections: [
          { title: "The First Ideal of the Radiants", body: "'Life before death' insists that the living moment holds inherent value. 'Strength before weakness' demands lifting others rather than exploiting vulnerability. 'Journey before destination' reminds us that the manner of reaching a goal defines its worth." },
          { title: "Bridge Four and collective dignity", body: "Kaladin transforms men condemned to slaughter into a cohesive brotherhood not by giving them hope of survival, but by giving them dignity in how they treat each other." },
          { title: "Leadership through vulnerability", body: "Dalinar refuses to play the games of deceit favored by rival princes, demonstrating that enduring authority requires moral consistency even when peers label it weakness." }
        ]
      }
    ],

    // 4. MYSTERY & THRILLER
    "mystery & thriller": [
      {
        id: "the-silent-patient",
        title: "The Silent Patient",
        author: "Alex Michaelides",
        cover_url: "https://covers.openlibrary.org/b/id/10389335-M.jpg",
        genre: "Mystery & Thriller",
        hook: "She shot her husband five times in the face, and then she never spoke another word",
        preview: "Alicia Berenson's life was seemingly picture-perfect: she was a celebrated painter married to an in-demand fashion photographer, living in a grand London home.\nOne evening, without warning, she tied her husband Gabriel to a chair and fired five bullets into his face—and then lapsed into total, unyielding silence.\nHer only public reaction was a single disturbing self-portrait entitled Alcestis, referencing the ancient Greek tragedy of a woman who chose death for her husband.\nTheo Faber is a forensic psychotherapist who has waited years for the chance to unravel her motive and unlock her voice inside the high-security psychiatric facility The Grove.\nAlex Michaelides weaves psychological tension with Greek mythology, exploring how childhood trauma distorts reality and builds armor that can turn lethal.\nAs Theo digs deeper into Alicia's past, the boundary between therapist and patient fractures, heading toward a revelation that redefines everything you thought you witnessed.",
        sections: [
          { title: "Silence as psychological armor", body: "Alicia's refusal to speak is not guilt or catatonia; it is a calculated fortress against a world that refused to listen to her before the violence occurred." },
          { title: "The myth of Alcestis", body: "In Euripides' play, Alcestis returns from death and remains silent. Alicia identifies with this silence: when someone you loved has psychologically killed you, words become meaningless." },
          { title: "Transference and countertransference", body: "Theo's professional objectivity is corrupted by his own unresolved marital wounds, demonstrating that the seeker of secrets is often fleeing their own reflection." }
        ]
      },
      {
        id: "gone-girl",
        title: "Gone Girl",
        author: "Gillian Flynn",
        cover_url: "https://covers.openlibrary.org/b/id/8315159-M.jpg",
        genre: "Mystery & Thriller",
        hook: "What are you thinking, Amy? What have we done to each other?",
        preview: "On the morning of their fifth wedding anniversary in North Carthage, Missouri, Nick Dunne returns home to find the front door ajar, furniture smashed, and his clever, beautiful wife Amy vanished.\nAs the police search intensifies, Nick's evasive behavior, secret debts, and bizarre emotional detachment quickly position him as the prime suspect in the national media.\nThrough Amy's pastel diary entries, we read the romantic genesis and gradual toxic disintegration of their marriage, painting Nick as an increasingly volatile threat.\nYet Gillian Flynn pulls off one of modern literature's sharpest architectural twists, tearing open the calculated performances people build to keep their partners engaged.\nGone Girl is a scalpel cutting into marital resentment, media sensationalism, and the exhausting masks of gender expectations.\nIt forces the reader to confront a terrifying realization: you never truly know the person sleeping right beside you.",
        sections: [
          { title: "The 'Cool Girl' cultural critique", body: "Amy's famous monologue exposes the exhausting social conditioning that pressures women to perform effortless compliance, hiding genuine resentment until it turns toxic." },
          { title: "Media trial as theater", body: "Flynn demonstrates how public opinion does not seek truth; it demands a legible television archetype—the grieving widower or the remorseless killer." },
          { title: "The economics of intimacy", body: "Marriage is dissected as a mutual projection where both parties fall in love with versions of themselves reflected in the other's gaze." }
        ]
      }
    ],

    // 5. ROMANCE
    "romance": [
      {
        id: "pride-and-prejudice",
        title: "Pride and Prejudice",
        author: "Jane Austen",
        cover_url: "https://covers.openlibrary.org/b/id/11162678-M.jpg",
        genre: "Romance",
        hook: "It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife",
        preview: "In an English countryside where an unmarried woman's financial survival depends entirely on advantageous matrimony, Elizabeth Bennet possesses a sharp wit and an independent mind.\nWhen the haughty, extraordinarily wealthy Fitzwilliam Darcy arrives in Hertfordshire, his disdainful refusal to dance with Elizabeth sparks an immediate mutual hostility.\nAusten's sparkling comedy of manners is not merely a love story; it is a profound social critique of pride, class barriers, and the hazards of rapid moral judgment.\nElizabeth misreads Darcy's aristocratic reserve as arrogance, while Darcy must dismantle his deep-seated class superiority to earn the respect of a woman who refuses to flatter him.\nThrough painful disclosures, letters, and family crises, both characters must undergo painful self-examination to earn true equality in partnership.\nTrue intimacy requires tearing down your defenses and risking rejection by speaking your honest truth.",
        sections: [
          { title: "The economics of marriage in Regency society", body: "Austen never sentimentalizes poverty. Marriage was the only viable economic career open to genteel women, making Elizabeth's refusal of Collins a radical act of personal integrity." },
          { title: "Pride vs. Prejudice", body: "Darcy's flaw is pride in his station; Elizabeth's is vanity in her own discernment. Both must experience humiliation before they can see one another clearly." },
          { title: "The transformative power of letters", body: "Darcy's letter forces Elizabeth to re-evaluate her judgment away from social posturing, proving that real reflection happens in solitude." }
        ]
      },
      {
        id: "normal-people",
        title: "Normal People",
        author: "Sally Rooney",
        cover_url: "https://covers.openlibrary.org/b/id/9027877-M.jpg",
        genre: "Romance",
        hook: "Most people go through life without ever knowing how it feels to be understood so completely",
        preview: "In County Sligo, Ireland, Connell is the popular, athletic working-class star of the high school, while Marianne is the wealthy, prickly outcast everyone avoids.\nThey begin an intense, clandestine physical intimacy after school hours, hidden from their peers because Connell is too cowardly to risk his social standing.\nWhen they both enter Trinity College Dublin, their social power dynamics invert: Marianne becomes glamorous, eccentric, and beloved, while Connell struggles with alienation, poverty, and depression.\nSally Rooney chronicles their magnetic, fractured connection over four turbulent years of university life, exploring how class, shame, and communication failures tear people apart.\nTheir relationship is not a simple romance, but a profound demonstration of how one person can irrevocably sculpt another's psychological architecture.\nThey repeatedly save each other from self-destruction, learning that vulnerability is the only bridge across emotional isolation.",
        sections: [
          { title: "Class and social hierarchy", body: "Rooney grounds every emotional interaction in economic reality. Connell's working-class anxiety and Marianne's family wealth continually distort their mutual communication." },
          { title: "The fear of social exposure", body: "Connell's teenage cowardice stems from the terror of peer judgment, showing how social conformity crushes private tenderness before it can bloom." },
          { title: "Mutual psychological redemption", body: "Their bond is not dependent on ownership. They change each other's life trajectories, demonstrating that loving someone means wanting their independence even if it takes them away." }
        ]
      }
    ],

    // 6. HORROR
    "horror": [
      {
        id: "the-shining",
        title: "The Shining",
        author: "Stephen King",
        cover_url: "https://covers.openlibrary.org/b/id/8315152-M.jpg",
        genre: "Horror",
        hook: "Sometimes human places create inhuman monsters",
        preview: "Aspiring playwright and recovering alcoholic Jack Torrance accepts the position of winter caretaker at the historic, snowbound Overlook Hotel high in the Colorado Rockies.\nHe hopes the solitary months with his wife Wendy and young telepathic son Danny will allow him to repair his broken marriage and finish his play.\nInstead, as blizzards cut off all escape, the sinister history of the Overlook begins waking up, hungering for Danny's extraordinary psychic gift ('the shining').\nStephen King builds dread not through sudden jumps, but through the claustrophobic unraveling of a father whose buried guilt, anger, and addiction make him the hotel's perfect vessel.\nThe real horror is not the ghost in bathtub Room 217 or the moving topiary hedge animals; it is watching someone who should protect you turn into the creature you fear most.\nThe Overlook merely whispers what Jack's dark pride already wanted to believe.",
        sections: [
          { title: "Addiction as a haunted house", body: "King uses the Overlook Hotel as an allegory for alcoholism. The hotel preys on Jack's resentment, offering him phantom drinks and convincing him that his family is the obstacle to his greatness." },
          { title: "Danny's 'shining' and childhood vulnerability", body: "Danny represents the terrifying sensitivity of children in dysfunctional homes, who sense hidden parental violence long before adults acknowledge it." },
          { title: "Isolation as an accelerant", body: "Physical cut-off from society accelerates psychological decay. Without external anchors, the mind accepts psychotic premises as rational." }
        ]
      },
      {
        id: "frankenstein",
        title: "Frankenstein",
        author: "Mary Shelley",
        cover_url: "https://covers.openlibrary.org/b/id/11186790-M.jpg",
        genre: "Horror",
        hook: "Beware; for I am fearless, and therefore powerful",
        preview: "Obsessed with unlocking the boundary between life and death, young Swiss natural philosopher Victor Frankenstein animates a creature assembled from charnel house remains.\nYet the moment the yellow eyes open, Victor is overwhelmed with visceral revulsion and flees his laboratory, abandoning his newborn creation to an unforgiving world.\nThe Creature wanders into the wilderness, intelligent, compassionate, and desperate for human warmth, only to be met with stones, bullets, and horror by everyone he approaches.\nMary Shelley, writing at just eighteen years old, birthed modern science fiction and gothic horror, questioning the moral responsibility of creators toward what they bring into existence.\nThe Creature's descent into vengeance is not inherent malice; it is the inevitable reaction of an abandoned soul denied a single gesture of kindness.\nVictor is the true monster: a father who created life for glory and ran when it demanded his care.",
        sections: [
          { title: "The hubris of consequence-free creation", body: "Victor seeks the godlike power of creation without the willingness to nurture. Shelley warns that scientific discovery divorced from ethical empathy breeds catastrophe." },
          { title: "The education of the Creature", body: "Through observing the De Lacey family and reading Milton's Paradise Lost, the Creature learns language, empathy, and philosophy, highlighting that moral capacity is cultivated through affection." },
          { title: "Monstrosity as a social reflection", body: "The Creature becomes what humanity forces him to be. Society creates its own monsters through systemic rejection and then feigns shock at their violence." }
        ]
      }
    ],

    // 7. HISTORICAL FICTION
    "historical fiction": [
      {
        id: "the-book-thief",
        title: "The Book Thief",
        author: "Markus Zusak",
        cover_url: "https://covers.openlibrary.org/b/id/11186792-M.jpg",
        genre: "Historical Fiction",
        hook: "Here is a small fact: You are going to die. I am in all truthfulness attempting to be cheerful about this whole topic, though most people find themselves hindered in believing me.",
        preview: "Narrated by Death himself with surprising gentleness and dark curiosity, this story unfolds in Nazi Germany on Molching's Himmel Street during World War II.\nLiesel Meminger is a foster girl who steals her first book, The Gravedigger's Handbook, from the snow before she even knows how to read.\nHer accordion-playing foster father Hans Hubermann patiently teaches her the alphabet by lantern light in the basement, unlocking the subversive power of language.\nWhen Hans shelters Max Vandenburg, a young Jewish fist fighter fleeing extermination, words become both a shared lifeline and a quiet weapon against hatred.\nMarkus Zusak creates an unforgettable exploration of cruelty, courage, and how storytelling preserves human soul in the shadow of total destruction.\nWords can be used by tyrants to scorch nations, or by children to heal broken spirits one stolen sentence at a time.",
        sections: [
          { title: "Death as a weary narrator", body: "Death is not a sinister villain, but an exhausted witness haunted by human cruelty. His perspective reframes war from military strategy into an unbearable accounting of stolen human lives." },
          { title: "The duality of language", body: "Hitler uses words to propagate systemic slaughter; Liesel and Max use words to sustain sanity. Zusak shows that language is the ultimate currency of human freedom." },
          { title: "Small acts of moral defiance", body: "Hans Hubermann handing bread to a starving Jewish prisoner marched through town illustrates that personal courage requires no army—just a refusal to extinguish empathy." }
        ]
      },
      {
        id: "all-the-light-we-cannot-see",
        title: "All the Light We Cannot See",
        author: "Anthony Doerr",
        cover_url: "https://covers.openlibrary.org/b/id/10522110-M.jpg",
        genre: "Historical Fiction",
        hook: "Open your eyes and see what you can with them before they close forever",
        preview: "In occupied France, Marie-Laure is a blind girl living in Paris with her father, the master locksmith of the Museum of Natural History.\nWhen the German invasion forces them to flee to the walled coastal city of Saint-Malo, they carry what may be the museum's most dangerous secret: the Sea of Flames diamond.\nMeanwhile, in a German mining town, Werner Pfennig is an orphan whose genius for radio repair lands him in a brutal Nazi military academy, training to hunt resistance radio signals.\nAnthony Doerr's Pulitzer Prize-winning novel intertwines their lives with breathtaking lyricism, exploring how ordinary humans navigate moral collapse in wartime.\nRadio waves cross enemy borders without permission, carrying lessons of science, piano sonatas, and coded coordinates through the darkness.\nThe profound insight is that even in the absolute horror of war, small points of light survive in people who refuse to surrender their conscience.",
        sections: [
          { title: "The invisible electromagnetic world", body: "Doerr uses radio waves as a metaphor for the unseen connections between human beings. Radio transcends national hatred, connecting lonely minds across hostile borders." },
          { title: "The cost of passive complicity", body: "Werner is not inherently sadistic; his sin is curiosity divorced from moral conviction, allowing himself to be drafted into a machinery of slaughter because it offered him an education." },
          { title: "Sensory resilience", body: "Marie-Laure's blindness forces her to experience the world through sound, texture, and memory, demonstrating how human perception adapts and finds beauty under extreme adversity." }
        ]
      }
    ],

    // 8. CLASSICS
    "classics": [
      {
        id: "1984",
        title: "1984",
        author: "George Orwell",
        cover_url: "https://covers.openlibrary.org/b/id/11186796-M.jpg",
        genre: "Classics",
        hook: "War is peace. Freedom is slavery. Ignorance is strength.",
        preview: "In the dystopian superstate of Oceania, the Party maintains absolute control through constant surveillance, perpetual war, and the systematic erasure of historical truth.\nWinston Smith works at the Ministry of Truth, rewriting archival newspapers so the Party's predictions are always retroactively infallible.\nUnder the unblinking eye of Big Brother and the threat of the Thought Police, Winston commits the ultimate rebellion: he purchases a blank diary and begins recording his own thoughts.\nHis forbidden love affair with Julia is an act of political defiance, reclaiming sensory pleasure and personal loyalty in a society designed to funnel all human emotion into collective hate.\nGeorge Orwell's chilling vision coined Newspeak, doublethink, and the memory hole, demonstrating how controlling vocabulary directly controls what thoughts can be conceived.\nIf freedom means anything, it is the right to tell people what they do not want to hear: that two plus two equals four.",
        sections: [
          { title: "The destruction of language (Newspeak)", body: "The Party does not censor opinions; it shrinks the vocabulary so that rebellious concepts become literally impossible to articulate. When words disappear, the capacity to think independently vanishes." },
          { title: "Doublethink and psychological surrender", body: "Doublethink is the ability to hold two contradictory beliefs simultaneously and accept both as true. It is the ultimate survival mechanism in totalitarianism, requiring the deliberate destruction of personal reason." },
          { title: "Room 101 and the breaking of loyalty", body: "The Party's ultimate victory over Winston is not executing him, but forcing him to genuinely betray Julia. When he begs for the rats to be placed on her face instead of his, his inner humanity is broken." }
        ]
      },
      {
        id: "crime-and-punishment",
        title: "Crime and Punishment",
        author: "Fyodor Dostoevsky",
        cover_url: "https://covers.openlibrary.org/b/id/8226191-M.jpg",
        genre: "Classics",
        hook: "Pain and suffering are always inevitable for a large intelligence and a deep heart",
        preview: "In the stifling heat of Saint Petersburg, impoverished former law student Rodion Raskolnikov conceives a radical philosophical theory.\nHe divides humanity into ordinary cattle bound by morality, and 'extraordinary' individuals like Napoleon who possess the moral right to step over blood to achieve great ends.\nTo test his theory and alleviate his family's debt, Raskolnikov axes a greedy, parasitic pawnbroker and her innocent sister to death.\nWhat follows is not a detective manhunt, but a terrifying psychological collapse as Raskolnikov discovers that his own conscience rejects the intellectual monster he built.\nDetective Porfiry Petrovich plays a brilliant cat-and-mouse game, waiting for the killer's psychological guilt to compel his own confession.\nDostoevsky proves that reason unmoored from empathy leads to monstrosity, and that redemption is found only through facing truth and embracing suffering.",
        sections: [
          { title: "The fallacy of the extraordinary man", body: "Raskolnikov's intellectual justification for murder shatters against reality. Rationalist arrogance cannot override the human nervous system's instinctual horror at destroying life." },
          { title: "Psychological investigation", body: "Porfiry Petrovich uses no physical forensic clues; he understands that guilt is a self-detonating psychological force that drives the criminal toward confession if given room to speak." },
          { title: "Redemption through Sonya", body: "Sonya Marmeladova, forced into prostitution to feed her siblings, embodies Christian self-sacrifice. Her love offers Raskolnikov the only path back to human fellowship." }
        ]
      }
    ],

    // 9. BUSINESS & MONEY
    "business & money": [
      {
        id: "the-psychology-of-money",
        title: "The Psychology of Money",
        author: "Morgan Housel",
        cover_url: "https://covers.openlibrary.org/b/id/10522112-M.jpg",
        genre: "Business & Money",
        hook: "Doing well with money has a little to do with how smart you are and a lot to do with how you behave",
        preview: "In the financial world, we are taught spreadsheets, formulas, and historical yield curves as if investing were a branch of physics.\nMorgan Housel shows that real-world financial success is not about intellect; it is about managing human psychology, ego, envy, and emotional stamina.\nA janitor named Ronald Read quietly saved small amounts, invested in blue-chip stocks, and left an $8 million fortune, while a Harvard-educated Merrill Lynch vice president went bankrupt.\nWealth is what you do not see: it is the cars not purchased, the watches not worn, and the freedom to control your own calendar.\nHousel explores why knowing when you have 'enough' prevents catastrophic gambles, and why room for error is the single most undervalued asset in business.\nThe highest dividend money pays is the ability to wake up every morning and say, 'I can do whatever I want today.'",
        sections: [
          { title: "Freedom as the ultimate wealth", body: "The highest intrinsic value of money is its ability to grant you control over your time. Independence and peace of mind trump luxury purchases in every long-term measure of human happiness." },
          { title: "The trap of 'Never Enough'", body: "When expectations rise faster than wealth, more income never feels like progress. Modern society creates an endless game of moving goalposts that can ruin even extraordinary fortunes." },
          { title: "Room for error and staying power", body: "Compound interest only works if you give it decades uninterrupted by catastrophic blowouts. Planning for unexpected setbacks is not pessimistic; it is mathematically essential." }
        ]
      },
      {
        id: "zero-to-one",
        title: "Zero to One",
        author: "Peter Thiel",
        cover_url: "https://covers.openlibrary.org/b/id/8315154-M.jpg",
        genre: "Business & Money",
        hook: "What important truth do very few people agree with you on?",
        preview: "Every moment in business happens only once. The next Bill Gates will not build an operating system, and the next Mark Zuckerberg will not build a social network.\nPeter Thiel, co-founder of PayPal and first outside investor in Facebook, argues that true progress comes from vertical leaps: going from zero to one by creating something entirely new.\nCopying an existing model merely takes the world from 1 to n, adding more of what is familiar and intensifying brutal, profit-destroying competition.\nThiel challenges conventional business dogmas, arguing that creative monopolies are good for society because they generate sustainable profits that fund long-term innovation.\nHe breaks down the secrets of defensible technology, network effects, and team culture that enable startups to escape the trap of commodities.\nIf you want to build a valuable company, don't compete: find a unique problem nobody else is solving and master a small, concentrated market.",
        sections: [
          { title: "Monopoly vs. Competition", body: "Under perfect competition, no firm makes an economic profit. Creative monopolists escape competition by inventing proprietary technology, capturing economies of scale, and creating distinct value." },
          { title: "The power law of venture capital", body: "In startup investing, the best investment yields returns equal to or greater than the rest of the entire portfolio combined. Focus resources on the rare exponential outlier." },
          { title: "Secrets and contrarian thinking", body: "Great businesses are founded on contrarian insights: truths that conventional wisdom overlooks because they are unfashionable or hidden in plain sight." }
        ]
      }
    ],

    // 10. SCIENCE
    "science": [
      {
        id: "a-brief-history-of-time",
        title: "A Brief History of Time",
        author: "Stephen Hawking",
        cover_url: "https://covers.openlibrary.org/b/id/11186798-M.jpg",
        genre: "Science",
        hook: "Even if it turns out that time travel is impossible, it is important that we understand why it is impossible",
        preview: "Stephen Hawking takes readers on an awe-inspiring journey through the frontiers of theoretical physics, exploring where the cosmos began and where it is heading.\nFrom Aristotle's geocentric spheres to Einstein's revolutionary general relativity, Hawking demystifies how space and time are not fixed backdrops, but dynamic fabrics bent by matter and energy.\nHe plunges into the enigmatic physics of black holes, revealing Hawking radiation—the counterintuitive discovery that black holes slowly leak energy and evaporate into nothingness.\nBy contrasting the cosmological laws governing the universe with the bizarre, probabilistic world of quantum mechanics, Hawking maps the quest for a Unified Theory of Everything.\nThe book asks the ultimate philosophical questions: Did the universe have a beginning in time? Will it have an end? Does physics leave any room for a creator?\nHawking shows that the human mind, bound to a fragile planet, has the audacious capacity to comprehend the architecture of the cosmos.",
        sections: [
          { title: "Space-time is dynamic", body: "Einstein showed that space and time cannot be separated from physical events. Heavy celestial bodies warp space-time, meaning gravity is geometry, not an invisible pulling force." },
          { title: "The arrow of time", body: "Thermodynamics dictates that entropy (disorder) always increases. This psychological, thermodynamic, and cosmological asymmetry explains why we remember the past and never the future." },
          { title: "Black holes are not completely black", body: "Through quantum fluctuations near the event horizon, virtual particle pairs get separated, resulting in particle emissions known as Hawking radiation." }
        ]
      },
      {
        id: "the-gene",
        title: "The Gene: An Intimate History",
        author: "Siddhartha Mukherjee",
        cover_url: "https://covers.openlibrary.org/b/id/8315156-M.jpg",
        genre: "Science",
        hook: "Three generations of my family have been afflicted with mental illness. Is madness encoded in our blood?",
        preview: "Oncologist and Pulitzer Prize winner Siddhartha Mukherjee weaves human history, personal family tragedy, and cutting-edge biotechnology into a masterwork on genetics.\nFrom Gregor Mendel's quiet pea-plant experiments in a monastery garden to the discovery of the double helix by Watson, Crick, and Franklin, Mukherjee traces how humans discovered the master code of life.\nYet the science of heredity has a dark and lethal heritage: Mukherjee unflinchingly confronts the eugenics movement, Nazi racial hygiene, and forced sterilizations driven by genetic arrogance.\nAs CRISPR and gene editing transform humans from passive products of evolution into deliberate architects of our own genome, ethical stakes reach an unprecedented crisis.\nWhat constitutes a genetic defect, and who has the moral authority to decide what human traits are worth preserving or eliminating?\nThe Gene challenges us to recognize that our genetic code is not a rigid destiny, but a musical score played in intimate dialogue with our environment.",
        sections: [
          { title: "The atom of biology", body: "Just as physics has the atom and chemistry has the element, genetics provided biology with its fundamental unit of hereditary information: the gene." },
          { title: "The horror of eugenics", body: "Mukherjee details how early genetic pseudoscience was weaponized to legitimize racism and mass murder, warning that science stripped of human empathy becomes a catastrophic weapon." },
          { title: "The threshold of human self-design", body: "With CRISPR technology, humanity can rewrite its own genetic code. The defining question of this century is whether we possess the wisdom to govern that unprecedented power." }
        ]
      }
    ],

    // 11. HISTORY
    "history": [
      {
        id: "sapiens",
        title: "Sapiens: A Brief History of Humankind",
        author: "Yuval Noah Harari",
        cover_url: "https://covers.openlibrary.org/b/id/10522114-M.jpg",
        genre: "History",
        hook: "One hundred thousand years ago, at least six human species inhabited the earth. Today there is just one. Us.",
        preview: "Homo sapiens was once an insignificant ape wandering the savannah of East Africa, possessing no greater ecological impact than baboons or fireflies.\nYuval Noah Harari charts how our species conquered the globe through three world-shaping revolutions: Cognitive, Agricultural, and Scientific.\nThe secret to our planetary dominance is not physical strength or superior individual intelligence; it is our unique capacity to cooperate flexibly in large numbers based on shared fictions.\nReligions, nations, corporations, human rights, and money do not exist in objective reality; they are intersubjective myths that millions of people agree to believe in simultaneously.\nYet Harari asks an uncomfortable historical question: Did the Agricultural Revolution actually improve human lives, or did it trap us into backbreaking labor and social inequality?\nAs biotechnology and artificial intelligence threaten to split humanity into biological castes, we must ask: what do we actually want to become?",
        sections: [
          { title: "The power of shared fictions", body: "Ants and wolves cooperate only in small, genetically related groups. Sapiens can collaborate with millions of total strangers because we believe in shared imagined realities like nations, laws, and currencies." },
          { title: "History's biggest fraud", body: "Harari argues the Agricultural Revolution domesticated humans rather than the reverse. Foragers enjoyed diverse diets and leisure, while early farmers suffered malnutrition and repetitive strain." },
          { title: "The horizon of Homo Deus", body: "Having conquered famine, plague, and major interstate war, humanity is directing its technological power toward acquiring godlike abilities: immortality and biological engineering." }
        ]
      },
      {
        id: "guns-germs-and-steel",
        title: "Guns, Germs, and Steel",
        author: "Jared Diamond",
        cover_url: "https://covers.openlibrary.org/b/id/11186800-M.jpg",
        genre: "History",
        hook: "Why did wealth and power become distributed as they now are, rather than in some other way?",
        preview: "When a New Guinean politician asked Jared Diamond why white Europeans arrived with so much cargo while local people had so little, Diamond set out to answer humanity's deepest geopolitical riddle.\nHe dismantles racist genetic theories, demonstrating that the disparate development of human societies was determined by environmental and geographical luck, not biological superiority.\nEurasia benefited from a vast east-west continental axis sharing identical day-lengths and climates, allowing crops, livestock, and metallurgy to spread rapidly across thousands of miles.\nIn contrast, the north-south axes of the Americas and Africa forced technological diffusion to stall against shifting desert, tropical, and temperate zones.\nFurthermore, centuries of living alongside domesticated herd animals gave Eurasians immunity to lethal zoonotic pathogens like smallpox and measles, which later decimated indigenous populations.\nHistory's fateful trajectories were forged not by human intellect, but by the distribution of wild grass seeds and domesticable mammals across the continents.",
        sections: [
          { title: "Continental axes and diffusion", body: "The east-west orientation of Eurasia allowed agricultural breakthroughs to migrate across similar latitudes without dying in unfamiliar climates, accelerating technological exchange." },
          { title: "The lethal gift of livestock", body: "Most human epidemic diseases originated in domestic animals. Cohabitating with pigs and cattle for millennia created devastating immunological weapons that decided colonial conquests." },
          { title: "The myth of racial destiny", body: "Human intelligence is evenly distributed across continents. Historical advantages were conferred by the local availability of protein-rich grains and draft animals." }
        ]
      }
    ],

    // 12. PHILOSOPHY
    "philosophy": [
      {
        id: "meditations",
        title: "Meditations",
        author: "Marcus Aurelius",
        cover_url: "https://covers.openlibrary.org/b/id/11186802-M.jpg",
        genre: "Philosophy",
        hook: "You have power over your mind—not outside events. Realize this, and you will find strength.",
        preview: "Written on military campaigns on the frozen northern frontier of the Roman Empire, Meditations was never meant for publication; it was the private journal of the most powerful man on earth.\nAs plague swept Rome, trusted generals revolted, and barbarians breached the borders, Emperor Marcus Aurelius used Stoic philosophy as daily armor against vanity, anger, and despair.\nHe reminds himself that human beings cannot control external circumstances, illness, political betrayal, or death; our sole domain is the moral integrity of our internal response.\nEvery morning, Marcus prepares to meet the meddling, ungrateful, arrogant, and dishonest, recognizing that their flaws stem from ignorance of what is truly good.\nMarcus views life from cosmic altitude: emperors and beggars alike are swept into oblivion, leaving only our present conduct as our true possession.\nWaste no more time arguing about what a good person should be; simply be one.",
        sections: [
          { title: "The dichotomy of control", body: "Distinguish ruthlessly between what is in your power (your intentions, judgments, actions) and what is not (the past, other people's opinions, physical illness). Freedom lies in releasing the latter." },
          { title: "The view from above", body: "Marcus regularly visualizes his armies, palace, and empire from cosmological height, realizing that human squabbles are tiny dots on a vast, indifferent cosmic canvas." },
          { title: "Obstacle as fuel", body: "The impediment to action advances action. What stands in the way becomes the way. Every setback is an arena to practice patience, courage, or justice." }
        ]
      },
      {
        id: "the-myth-of-sisyphus",
        title: "The Myth of Sisyphus",
        author: "Albert Camus",
        cover_url: "https://covers.openlibrary.org/b/id/8226194-M.jpg",
        genre: "Philosophy",
        hook: "There is but one truly serious philosophical problem, and that is suicide",
        preview: "Albert Camus opens with an uncompromising demand: judging whether life is or is not worth living is the fundamental question of philosophy.\nHe describes 'the Absurd': the profound collision between the human soul's desperate longing for meaning and the cold, unyielding silence of the universe.\nMost people seek refuge in religious illusions ('philosophical suicide') or succumb to nihilistic despair, hoping for an external guarantee that their struggles matter.\nCamus proposes a radical third path: living in clear-eyed defiance of the absurd, embracing life with passionate lucidity without demanding manufactured meaning.\nHe invokes the Greek myth of Sisyphus, condemned by the gods to push a massive boulder up a mountain for eternity, only to watch it roll back down.\nSisyphus is victorious not when the rock stays at the summit, but in the conscious descent when he acknowledges his fate and resumes pushing anyway.\nOne must imagine Sisyphus happy.",
        sections: [
          { title: "The awakening of the Absurd", body: "The feeling of absurdity strikes when the automatic habits of life collapse. The mind suddenly recognizes the foreignness of the world and demands a purpose that does not exist." },
          { title: "Revolt, freedom, and passion", body: "Instead of fleeing into mystical hope, the absurd hero lives fully in revolt against mortality. Quantity of rich, conscious experience replaces illusory metaphysical goals." },
          { title: "The dignity of the climb", body: "The struggle itself toward the heights is enough to fill a human heart. Meaning is not found in an afterlife reward, but in our choice to carry our burden with lucid joy." }
        ]
      }
    ],

    // 13. ADVENTURE
    "adventure": [
      {
        id: "endurance",
        title: "Endurance: Shackleton's Incredible Voyage",
        author: "Alfred Lansing",
        cover_url: "https://covers.openlibrary.org/b/id/11186804-M.jpg",
        genre: "Adventure",
        hook: "Men wanted for hazardous journey. Small wages, bitter cold, long months of complete darkness, constant danger, safe return doubtful.",
        preview: "In January 1915, Sir Ernest Shackleton's ship Endurance was trapped in the crushing pack ice of Antarctica's Weddell Sea, hundreds of miles from rescue.\nFor ten agonizing months, the twenty-eight-man crew drifted helplessly with the ice floe until the frozen pressure hull splintered and sank beneath the frozen sea.\nStranded on unstable drifting ice, Shackleton led his men through sub-zero blizzards, starving on penguin blubber, navigating lifeboats through mountainous seas to desolate Elephant Island.\nWith his crew on the brink of death, Shackleton and five men sailed an open twenty-foot lifeboat 800 miles across the stormiest ocean on earth to South Georgia Island.\nAlfred Lansing reconstructs the definitive survival epic using the crew's original diaries, showing how Shackleton's peerless leadership kept morale alive without a single loss of life.\nFor scientific discovery, give me Scott; for speed and efficiency of travel, give me Amundsen; but when disaster strikes and all hope is gone, get down on your knees and pray for Shackleton.",
        sections: [
          { title: "Leadership through emotional equilibrium", body: "Shackleton understood that panic is deadlier than freezing weather. He prioritized crew morale, optimism, and fair distribution of chores over rigid naval hierarchy." },
          { title: "The 800-mile navigation miracle", body: "Frank Worsley navigated the tiny James Caird using a sextant during fleeting seconds of sun through hurricane clouds. A navigational error of just one mile would have meant sailing into the empty Atlantic to die." },
          { title: "The resilience of purpose", body: "The men survived because Shackleton never permitted them to believe death was inevitable. Purpose and mutual responsibility sustained them when biological resources ran dry." }
        ]
      },
      {
        id: "into-thin-air",
        title: "Into Thin Air",
        author: "Jon Krakauer",
        cover_url: "https://covers.openlibrary.org/b/id/8315158-M.jpg",
        genre: "Adventure",
        hook: "Mortality had remained a conveniently hypothetical concept... but up here, death was a palpable presence",
        preview: "Journalist Jon Krakauer joined Rob Hall's commercial expedition to summit Mount Everest in May 1996, intending to critique the commercialization of extreme mountaineering.\nInstead, he was thrust into the deadliest 24-hour disaster in Everest's modern history, where a rogue blizzard trapped dozens of exhausted climbers in the Death Zone.\nAt 29,000 feet, where the brain is starved of oxygen and cognitive function declines to drunken incoherence, every decision becomes life or death.\nKrakauer chronicles the harrowing bottleneck at the Hillary Step, where wealthy clients paid $65,000 to stand on top of the world while ignoring critical turn-around times.\nAs storm winds surpassed 70 mph and temperatures dropped to -50°F, experienced guides and clients perished just yards from safety in the whiteout.\nInto Thin Air is an unflinching post-mortem on human hubris, commercial greed, and the terrifying price of chasing glory in an environment that cannot forgive a single mistake.",
        sections: [
          { title: "Hypoxia and cognitive breakdown", body: "Above 8,000 meters, human cells cannot recover. Chronic oxygen deprivation destroys the brain's ability to assess basic safety, making rational caution almost impossible." },
          { title: "The commercialization of risk", body: "When clients pay enormous sums, guides feel immense commercial pressure to push past predefined safety turn-around deadlines, inviting catastrophe." },
          { title: "Survivor's guilt and journalistic honesty", body: "Krakauer refuses to write a tidy heroic narrative. He exposes his own errors and exhaustion, capturing the haunting moral aftermath of survival." }
        ]
      }
    ],

    // 14. YOUNG ADULT
    "young adult": [
      {
        id: "the-hunger-games",
        title: "The Hunger Games",
        author: "Suzanne Collins",
        cover_url: "https://covers.openlibrary.org/b/id/11186806-M.jpg",
        genre: "Young Adult",
        hook: "May the odds be ever in your favor",
        preview: "In the ruins of what was once North America, the decadent Capitol rules over twelve impoverished districts through fear, surveillance, and starvation.\nEach year, as punishment for a past rebellion, the Capitol forces one boy and one girl from each district to fight to the death on live television in the Hunger Games.\nWhen her twelve-year-old sister Prim's name is drawn, sixteen-year-old Katniss Everdeen volunteers to take her place, armed only with her hunting bow and ruthless survival instincts.\nKatniss is thrust into an arena engineered by Gamemakers where every tree, stream, and predator is a programmed death trap, and where winning requires currying favor with wealthy Capitol sponsors.\nSuzanne Collins crafted a ferocious critique of reality television, authoritarian brutality, and the moral compromises of war.\nTo survive, Katniss must master not only physical combat, but the dangerous theater of manufactured romance, discovering that deflecting the Capitol's script is the ultimate defiance.",
        sections: [
          { title: "Spectacle as social control", body: "The Capitol uses glitz, fashion, and reality television drama to distract citizens from systemic atrocities, turning state-sponsored murder into entertainment." },
          { title: "The moral cost of survival", body: "Katniss is not a spotless savior; she is a traumatized survivor who makes cold calculations. Collins honors young readers by refusing to sanitize the psychic wounds of violence." },
          { title: "The symbol of the Mockingjay", body: "Rue's funeral and the three-finger salute demonstrate that small acts of human dignity within a corrupted system can ignite mass political revolution." }
        ]
      }
    ],

    // 15. TRUE CRIME
    "true crime": [
      {
        id: "in-cold-blood",
        title: "In Cold Blood",
        author: "Truman Capote",
        cover_url: "https://covers.openlibrary.org/b/id/11186808-M.jpg",
        genre: "True Crime",
        hook: "Four shotgun blasts that, all told, ended six human lives",
        preview: "On a quiet November night in 1959, in the farming village of Holcomb, Kansas, two ex-convicts entered the Clutter family farmhouse looking for a safe that did not exist.\nBy dawn, wealthy farmer Herbert Clutter, his ailing wife Bonnie, and their two teenage children were bound and executed with shotgun blasts at point-blank range.\nTruman Capote traveled to Kansas alongside Harper Lee, spending six years interviewing townspeople, investigators, and the killers Perry Smith and Dick Hickock.\nIn Cold Blood invented the 'nonfiction novel', merging rigorous journalistic investigation with literary pacing, psychological depth, and atmospheric prose.\nCapote penetrates the fragile psyche of Perry Smith, a damaged, poetic drifter whose catastrophic childhood produced explosive, irrational violence.\nThe true horror is not just the brutality of the act, but the chilling realization that ordinary, decent lives can be extinguished in seconds by strangers passing in the dark.",
        sections: [
          { title: "The invention of the True Crime novel", body: "Capote demonstrated that real-world investigative reporting could achieve the psychological complexity, dialogue richness, and narrative suspense of high literature." },
          { title: "The anatomy of unmotivated violence", body: "The killers gained less than fifty dollars and a portable radio. Capote exposes how psychological resentment and peer pressure can escalate a minor burglary into senseless butchery." },
          { title: "The fracture of American innocence", body: "The murders permanently destroyed the Holcomb community's pastoral trust, forcing neighbors who never locked their doors to view one another with paranoid suspicion." }
        ]
      }
    ],

    // 16. POETRY
    "poetry": [
      {
        id: "the-sun-and-her-flowers",
        title: "The Sun and Her Flowers",
        author: "Rupi Kaur",
        cover_url: "https://covers.openlibrary.org/b/id/8315160-M.jpg",
        genre: "Poetry",
        hook: "This is the recipe of life: will it hurt? yes. will it heal? yes.",
        preview: "Divided into five chapters—wilting, falling, rooting, rising, and blooming—this collection explores the cyclical nature of grief, love, and self-restoration.\nRupi Kaur brought poetry to millions of digital readers through concise, raw free verse paired with minimalist line illustrations.\nShe writes unflinchingly of ancestral trauma, immigrant mother-daughter relationships, the pain of body dysmorphia, and finding peace after abuse.\nHer poems do not hide behind baroque metaphors; they operate with stark, emotional clarity that cuts directly into universal human wounds.\nThe core insight of the collection is that healing is not an arrival point, but a biological rhythm: like flowers in winter, we must allow ourselves to wilt before we can root and bloom anew.\nYou do not have to hold yourself together every second to remain worthy of your own affection.",
        sections: [
          { title: "The five stages of renewal", body: "Kaur frames emotional trauma through floral biology: wilting, falling, rooting, rising, blooming. Every period of despair is reframed as subterranean root-growth." },
          { title: "Immigrant daughters and ancestral debts", body: "Her verses honor the sacrifices of Punjabi immigrant mothers who crossed oceans with silent resilience, connecting modern identity to ancestral struggle." },
          { title: "Self-compassion as active practice", body: "Kaur demystifies healing: it is not a triumphant destination, but an unglamorous daily commitment to treat one's own fragile body with tenderness." }
        ]
      }
    ],

    // 17. LITERARY FICTION
    "literary fiction": [
      {
        id: "the-road",
        title: "The Road",
        author: "Cormac McCarthy",
        cover_url: "https://covers.openlibrary.org/b/id/11186810-M.jpg",
        genre: "Literary Fiction",
        hook: "You forget what you want to remember, and you remember what you want to forget",
        preview: "A father and his young son walk alone through a burned America where no living thing grows, ash snows from a leaden sky, and the sun never pierces the gloom.\nPushing a rusted shopping cart with their meager possessions, they scavenge through ruined towns along the highway toward the coast, evading cannibal bands in the ruins.\nCormac McCarthy strips language down to stark, biblical prose of peerless emotional power, free of conventional punctuation and unnecessary ornamentation.\nThe unnamed father is dying of illness, sustained solely by a fierce, sacred devotion to keep his boy safe and 'carry the fire' of human goodness in an extinct world.\nThe Road is a harrowing inquiry into love, ethics, and parenthood at the absolute end of civilization.\nWhen all laws, institutions, and gods are dead, goodness is not an instinct—it is a conscious, heroic choice made against total despair.",
        sections: [
          { title: "Carrying the fire", body: "In a world where civilization has reverted to predatory savagery, the father teaches the boy that 'the fire' is human decency, compassion, and refusal to cannibalize others." },
          { title: "The ascetic beauty of language", body: "McCarthy discards quotation marks and semicolon fluff, mirroring the scorched terrain with sparse, luminous sentences that carry immense gravitational weight." },
          { title: "Parenthood as sacred duty", body: "The boy is the father's only proof that God ever existed. McCarthy demonstrates that love achieves its purest expression when stripped of all material security." }
        ]
      }
    ],

    // 18. BIOGRAPHY & MEMOIR
    "biography & memoir": [
      {
        id: "educated",
        title: "Educated",
        author: "Tara Westover",
        cover_url: "https://covers.openlibrary.org/b/id/10522116-M.jpg",
        genre: "Biography & Memoir",
        hook: "My life was narrated for me by others. Their voices were forceful, emphatic, absolute. It had never occurred to me that my voice might be as strong as theirs.",
        preview: "Born to survivalist parents in the isolated mountains of rural Idaho, Tara Westover did not possess a birth certificate, never visited a doctor, and did not set foot in a classroom until age seventeen.\nHer father stockpiled peaches and ammunition for the End of Days, distrusting hospitals, public schools, and the 'Illuminati' federal government.\nTara spent her childhood stewing herbal remedies with her mother and working in her father's dangerous scrap metal junkyard, enduring violent physical abuse from an older brother.\nTeaching herself enough algebra, grammar, and history to pass the ACT, she entered Brigham Young University, discovering the Holocaust and civil rights movement for the first time.\nTara's memoir is a breathtaking testament to the transformative power of self-education, and the agonizing cost of family estrangement.\nEducation is not merely training for a career; it is the radical act of gaining the ability to construct your own mind.",
        sections: [
          { title: "Education as self-creation", body: "Westover distinguishes between learning facts and acquiring an education. True education is the ability to perceive the world from perspectives outside your family's dogma." },
          { title: "The cost of breaking family loyalty", body: "Leaving an abusive family is not an unalloyed triumph. Westover unflinchingly portrays the grief, guilt, and profound loneliness that accompanies choosing truth over tribal belonging." },
          { title: "The fragility of memory", body: "Westover includes footnotes acknowledging where her siblings' memories diverge from hers, demonstrating that trauma distorts recollection and complicates the search for certainty." }
        ]
      }
    ],

    // 19. POLITICS & SOCIETY
    "politics & society": [
      {
        id: "the-righteous-mind",
        title: "The Righteous Mind",
        author: "Jonathan Haidt",
        cover_url: "https://covers.openlibrary.org/b/id/11186812-M.jpg",
        genre: "Politics & Society",
        hook: "Intuitions come first, strategic reasoning second",
        preview: "Why is our political culture so hopelessly polarized, and why is it virtually impossible to persuade an ideological opponent with sound facts?\nSocial psychologist Jonathan Haidt reveals that human morality is not grounded in cool philosophical logic, but in emotional gut intuitions.\nReasoning is not the judge; it is a press secretary hired to invent justifications for whatever emotional judgment our intuition already declared.\nHaidt identifies six foundational taste-buds of moral psychology: Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation, and Liberty/Oppression.\nWhile liberals primarily emphasize Care and Fairness, conservatives draw upon all six foundations, making their moral rhetoric emotionally legible to a broader spectrum of voters.\nUnderstanding these moral foundations does not mean abandoning your convictions; it means escaping the arrogant trap of believing that everyone who disagrees with you is either evil or stupid.",
        sections: [
          { title: "The Rider and the Elephant", body: "The mind is divided like a rider on an elephant. The rider represents conscious reasoning, but the elephant (intuitive emotional response) controls direction. To persuade someone, speak to the elephant first." },
          { title: "The six moral foundations", body: "Just as our tongues have taste receptors for sweet, sour, salty, bitter, and umami, human cultures build moral systems on six universal evolutionary foundations." },
          { title: "Morality binds and blinds", body: "Our moral nature evolved to bind us into cohesive cooperative teams, but that same evolutionary mechanism blinds us to the legitimate ethical concerns of rival groups." }
        ]
      }
    ],

    // 20. SELF-HELP
    "self-help": [
      {
        id: "deep-work",
        title: "Deep Work",
        author: "Cal Newport",
        cover_url: "https://covers.openlibrary.org/b/id/11186814-M.jpg",
        genre: "Self-Help",
        hook: "The ability to perform deep work is becoming increasingly rare at exactly the same time it is becoming increasingly valuable",
        preview: "In an economy dominated by open-plan offices, instant Slack pings, and algorithmic social feeds, our collective capacity for sustained concentration has fractured.\nComputer science professor Cal Newport defines 'deep work' as professional activities performed in a state of distraction-free concentration that push cognitive capabilities to their limit.\nShallow work—answering emails, attending status meetings, and checking notifications—feels productive, but it produces zero lasting economic value and is easily automated.\nNewport provides a rigorous framework for training your mental stamina, scheduling deliberate blocks of isolation, and quitting social media platforms that profit from fragmenting your focus.\nDepth is not a luxury for eccentric academics or solitary novelists; it is the decisive superpower of the modern digital knowledge worker.\nIf you do not produce at the peak of your cognitive capacity, you will inevitably be outperformed by systems and individuals who do.",
        sections: [
          { title: "The Deep Work Hypothesis", body: "The skill to master complex tasks rapidly and produce high-value results depends directly on uninterrupted focus. Those who cultivate deep work thrive; those who remain shallow become expendable." },
          { title: "Attention residue", body: "When you switch from task A to quickly check an email (task B), your attention does not switch cleanly. A residue of cognitive focus remains stuck on task B, diminishing your performance for hours." },
          { title: "Embrace boredom", body: "You cannot expect to focus deeply on work if your brain is conditioned to reach for a phone at the first second of boredom in an elevator. Mental stillness must be trained like a muscle." }
        ]
      }
    ],
    // 21. SELF DISCOVERY
    "self discovery": [
      {
        id: "the-mountain-is-you",
        title: "The Mountain Is You",
        author: "Brianna Wiest",
        cover_url: "https://covers.openlibrary.org/b/id/11186816-M.jpg",
        genre: "Self Discovery",
        hook: "Your self-sabotage is not a character flaw; it is an unconscious attempt to meet an unmet emotional need",
        preview: "We often believe our biggest obstacles are external circumstances, demanding bosses, or bad luck.\nBrianna Wiest reveals that the mountain standing between you and the life you want is almost always your own subconscious resistance.\nSelf-sabotage occurs when an internal desire conflicts with an unconscious need for safety or emotional familiarity.\nProcrastination, perfectionism, and picking fights right when life is going well are not failures of willpower; they are protective defense mechanisms.\nTrue personal breakthrough does not come from punishing yourself into discipline, but from mastering emotional literacy.\nBy learning to listen to what your resistance is trying to protect you from, you transform self-sabotage into authentic self-mastery.\nThe mountain is not in your way; the mountain is the path.",
        sections: [
          { title: "The anatomy of self-sabotage", body: "Self-sabotage is simply the presence of two conflicting desires: a conscious yearning for growth and an unconscious demand for safety. When unfamiliar success threatens your emotional comfort zone, self-sabotage acts to return you to familiar ground." },
          { title: "Emotional breakdown as breakthrough", body: "Emotional crises are not failures; they are the psyche's way of forcing you to shed behaviors, relationships, and identities that you have outgrown. Discomfort is the biological signal of imminent personal expansion." },
          { title: "Building emotional stamina", body: "True self-discovery requires sitting with uncomfortable emotions without immediately reaching for distraction, numbing habits, or premature solutions. Emotional resilience is cultivated through stillness and self-compassion." }
        ]
      },
      {
        id: "mans-search-for-meaning",
        title: "Man's Search for Meaning",
        author: "Viktor E. Frankl",
        cover_url: "https://covers.openlibrary.org/b/id/8226196-M.jpg",
        genre: "Self Discovery",
        hook: "Those who have a 'why' to live, can bear with almost any 'how'",
        preview: "Psychiatrist Viktor Frankl survived the unimaginable horrors of Auschwitz and Dachau, observing human psychology stripped down to naked biological survival.\nIn the death camps, he discovered that what separated those who gave up from those who persevered was not physical strength or youth, but a sense of future purpose.\nFrankl founded Logotherapy, the psychological philosophy that man's primary motivational force is not the pursuit of pleasure or power, but the discovery of personal meaning.\nMeaning is not something waiting to be passively discovered; it is actively forged through creative work, authentic love, and the courage to endure unavoidable suffering.\nEverything can be taken from a human being except one thing: the last of human freedoms—to choose one's attitude in any given set of circumstances.\nWhen we are no longer able to change a situation, we are challenged to change ourselves.",
        sections: [
          { title: "The last human freedom", body: "Between stimulus and response there is a space. In that space is our power to choose our response. In our response lies our growth and our ultimate freedom." },
          { title: "The three avenues to meaning", body: "Frankl identifies three ways to discover meaning in life: by creating a work or doing a deed; by experiencing something or encountering someone (love); and by the attitude we take toward unavoidable suffering." },
          { title: "The tragic optimism", body: "Tragic optimism is the capacity to remain hopeful and find purpose despite the inescapable realities of pain, guilt, and death. It transforms despair into conscious, heroic action." }
        ]
      }
    ]
  };

  // Expose curated catalog globally
  window.RABBIT_CURATED_CATALOG = catalog;
})();
