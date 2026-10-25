/* RABBIT Dynamic Content & Genre Synthesis Engine
 * Transforms any book from Open Library, search, or database into:
 * 1. A Curiosity Hook Headline
 * 2. An 8-10 line intriguing feed preview with genuine insights
 * 3. A 4-part structured reading guide for the RABBIT Reader overlay
 * Scalable to thousands upon thousands of books across all 20 genres.
 */
(function() {
  "use strict";

  // Genre specific editorial archetypes
  const GENRE_PROFILES = {
    "Science Fiction": {
      focus: "speculative science, cosmic scales, future stakes, and technological ethics",
      hookPrefixes: [
        "What happens to human consciousness when technology eliminates our biological boundaries?",
        "When artificial intelligence surpasses human comprehension, who actually owns the future?",
        "A single scientific discovery that threatens the fragile equilibrium of an interstellar empire.",
        "In a future where memory can be rewritten, how do you verify who you really are?",
        "The laws of physics don't negotiate—and humanity just violated the first rule."
      ],
      insightAngles: [
        "The danger is never the machine itself, but the human appetites we encode into its programming.",
        "Technological evolution moves at exponential speed while human ethics remains stubbornly linear.",
        "Surviving in deep space requires surrendering the illusion of individual self-sufficiency.",
        "When every physical desire is automated, purpose becomes the rarest commodity in the universe."
      ]
    },
    "Fantasy": {
      focus: "worldbuilding, magic systems, mythic conflicts, and the cost of power",
      hookPrefixes: [
        "Power belongs not to the rightful heir, but to whoever can survive the night the wards break.",
        "When an ancient oath is shattered, magic exacts a price that gold can never pay.",
        "In a realm ruled by forgotten gods, every spell is a debt carved directly into the bone.",
        "A reluctant hero discovers that prophecy is not destiny—it is an architect's blueprint for war.",
        "Legends speak of kingdoms won with swords; history remembers those betrayed with whispers."
      ],
      insightAngles: [
        "True strength is not measured by the magic you command, but by the restraint you exercise.",
        "Every great empire builds its monuments on the silent sacrifices of people whose names are erased.",
        "Destiny is merely the story victors tell to justify the catastrophes they unleashed.",
        "Loyalty earned through mutual vulnerability outlasts armies bound only by fear."
      ]
    },
    "Mystery & Thriller": {
      focus: "suspense, psychological secrets, danger, and escalating stakes",
      hookPrefixes: [
        "A locked door, an impossible crime, and seven witnesses who swear they never heard a sound.",
        "The closer you look at a flawless alibi, the faster the foundation begins to splinter.",
        "Someone in this room is lying about the past—and willing to kill to keep it buried.",
        "A missing person leaves behind a single clue that points directly to the lead detective.",
        "Every secret leaves a digital or physical footprint; the art is learning where to look."
      ],
      insightAngles: [
        "The most dangerous deception is not the elaborate lie, but the partial truth everyone wants to believe.",
        "Human panic creates predictable patterns that can be anticipated long before the trap springs.",
        "Guilt is a psychological accelerant that eventually compels the culprit to revisit the crime.",
        "In high-stakes investigation, your strongest initial suspicion is often your blindest bias."
      ]
    },
    "Romance": {
      focus: "emotional tension, vulnerability, personal barriers, and relationship chemistry",
      hookPrefixes: [
        "Two rivals forced to collaborate on the one project that could make—or destroy—both their careers.",
        "What happens when the person you swore never to trust is the only one who sees who you really are?",
        "Falling in love is easy; dismantling the emotional walls you built to survive is the real battlefield.",
        "A chance encounter rekindles a past connection that neither partner has ever truly escaped.",
        "The greatest risk in intimacy is not rejection, but allowing yourself to be genuinely known."
      ],
      insightAngles: [
        "Vulnerability is not weakness; it is the prerequisite for any enduring emotional intimacy.",
        "True partnership does not demand losing yourself, but finding someone who expands your world.",
        "Pride protects our ego in the short term while quietly starving our need for connection.",
        "The courage to forgive another person begins with forgiving the choices you made to survive."
      ]
    },
    "Horror": {
      focus: "atmosphere, dread, unsettling premises, and psychological or supernatural tension",
      hookPrefixes: [
        "The house has only one rule after sunset: never answer when the voice from the attic calls your name.",
        "What terrifies us most is not the monster in the shadows, but recognizing its face in the mirror.",
        "A quiet town hides a ritual that demands a horrific sacrifice to keep the darkness at bay.",
        "Isolation has a way of turning the mind's darkest whispers into undeniable physical reality.",
        "Some doors are locked not to keep intruders out, but to ensure whatever is inside never escapes."
      ],
      insightAngles: [
        "Fear is an evolutionary radar: when something feels subtly wrong, your subconscious already knows why.",
        "Grief and guilt are the most potent haunting agents, transforming ordinary spaces into chambers of dread.",
        "Monstrosity thrives wherever human communities choose collective denial over painful truth.",
        "The ultimate terror is the erosion of certainty about what is real and what is hallucination."
      ]
    },
    "Historical Fiction": {
      focus: "historical settings, turning points, human resilience, and lived experience",
      hookPrefixes: [
        "Amidst the crumbling splendor of an empire, an ordinary family must navigate the tides of revolution.",
        "History records the treaties signed by generals; fiction preserves the quiet courage of those who rebuilt.",
        "A hidden journal reveals the forgotten woman whose scientific work altered the course of a world war.",
        "When war strips away all social convention, humanity reveals both its purest grace and deepest cruelty.",
        "Two strangers on opposing sides of a conflict find their shared humanity tested by duty."
      ],
      insightAngles: [
        "Epoch-defining events are shaped not just by famous leaders, but by ordinary choices made in the dark.",
        "Human nature remains startlingly constant: the fears and hopes of ancient citizens mirror our own.",
        "Preserving memory against state-sponsored erasure is the most radical form of cultural resistance.",
        "True historical empathy requires understanding people within the moral boundaries of their era."
      ]
    },
    "Classics": {
      focus: "timeless human nature, moral conflict, societal critique, and literary weight",
      hookPrefixes: [
        "Beneath aristocratic elegance lies an unsparing examination of pride, hypocrisy, and social survival.",
        "A single moral compromise sets off a chain reaction that unravels an entire life.",
        "Generations pass, but the fundamental struggle between personal freedom and social duty never ages.",
        "An enduring inquiry into what human beings owe to each other when societal institutions fail.",
        "The eternal conflict between our rational ideals and our destructive subterranean impulses."
      ],
      insightAngles: [
        "Great literature does not provide easy answers; it equips us to ask more courageous questions.",
        "Social institutions often demand conformity at the direct expense of individual integrity.",
        "The flaws that undo tragic heroes are often inseparable from their greatest virtues.",
        "Language holds the mirror up to human nature, stripping away the self-deceptions of every era."
      ]
    },
    "Adventure": {
      focus: "exploration, danger, physical resilience, discovery, and the consequences of courage",
      hookPrefixes: [
        "Eight hundred miles across uncharted terrain with failing equipment and one desperate chance at return.",
        "When the elements push human endurance past the breaking point, character is all that remains.",
        "A legendary expedition ventures into the blank spaces of the map, confronting nature at its rawest.",
        "Survival is not a heroic spectacle; it is a grueling series of small, disciplined choices in the cold.",
        "The wild does not care about human ambition—it only tests how much you are willing to endure."
      ],
      insightAngles: [
        "Resilience is not the absence of fear, but the daily discipline of taking the next step despite it.",
        "In extreme environments, teamwork and morale determine survival long before supplies run dry.",
        "Humility before the natural world is the only attitude that preserves life in the wilderness.",
        "Adventure reveals that the physical boundaries we imagine are almost always mental constructs."
      ]
    },
    "Business & Money": {
      focus: "practical principles, economic tradeoffs, strategic positioning, and human incentives",
      hookPrefixes: [
        "Why do brilliant companies fail while underdogs with fraction of the resources dominate their markets?",
        "Real wealth is not what you spend—it is the autonomy and freedom your balance sheet quietly buys.",
        "Understanding incentives is the master key to decoding how organizations and markets actually operate.",
        "The fastest way to destroy competitive advantage is mistaking a temporary monopoly for permanent genius.",
        "In business, what you choose not to do defines your strategy far more than what you attempt."
      ],
      insightAngles: [
        "Compounding is the most powerful force in finance, but it demands uninterrupted emotional stamina.",
        "A system designed purely for short-term efficiency collapses under the first unexpected shock.",
        "Value creation is sustainable only when aligned with genuine customer utility, not financial engineering.",
        "The best strategic investments feel uncomfortable because they challenge existing organizational dogma."
      ]
    },
    "Science": {
      focus: "empirical discoveries, physical mechanisms, natural laws, and worldview shifts",
      hookPrefixes: [
        "The counterintuitive physics that explains why time itself slows down as you move through space.",
        "Inside every living cell, microscopic molecular engines are performing calculations that baffle engineers.",
        "The universe is not obliged to make sense to our primate intuition—and quantum reality proves it.",
        "From cosmic dust to self-aware consciousness: how four billion years of evolution forged the human mind.",
        "The most profound breakthroughs in science occur when an experiment yields an anomaly everyone tried to ignore."
      ],
      insightAngles: [
        "Scientific inquiry is not a collection of settled dogmas, but a relentless method of organized doubt.",
        "Complex living phenomena emerge naturally from simple, local mathematical interactions over time.",
        "Every atom in your body was forged in the thermonuclear core of an ancient exploding star.",
        "A deeper understanding of nature does not diminish its beauty; it elevates wonder into profound awe."
      ]
    },
    "History": {
      focus: "consequential events, human turning points, unseen connections, and enduring lessons",
      hookPrefixes: [
        "Three decisions in a single week that quietly altered the geopolitical trajectory of the modern world.",
        "How a forgotten trade route across Central Asia built global empires and sparked the Renaissance.",
        "The fall of civilizations rarely begins at the borders; it begins with the internal decay of shared trust.",
        "History is not a smooth progression toward enlightened reason, but a turbulent cycle of human ambition.",
        "Overlooked documents reveal how ordinary citizens organized under tyranny to preserve democratic values."
      ],
      insightAngles: [
        "Institutions survive only as long as citizens believe in the unwritten norms that uphold them.",
        "Technological disruption without social adaptation consistently triggers political upheaval.",
        "Studying history does not allow us to predict the future, but it prevents us from being surprised by the present.",
        "Every generation imagines its dilemmas are unprecedented, forgetting that human nature has walked this path before."
      ]
    },
    "Philosophy": {
      focus: "foundational paradoxes, ethical frameworks, clarity of thought, and human existence",
      hookPrefixes: [
        "If our desires are conditioned by social biology, what does it truly mean to possess free will?",
        "You cannot control the chaos of external circumstance; your only true sovereignty is your own judgment.",
        "Living an examined life is not an academic pursuit—it is the urgent craft of finding clarity before death.",
        "Why do human beings sacrifice undeniable truth for the comforting illusion of certainty?",
        "The paradox of happiness: the more aggressively you hunt for pleasure, the more elusive peace becomes."
      ],
      insightAngles: [
        "Clarity of thought requires the uncomfortable courage to dismantle beliefs that flatter your ego.",
        "Ethics is not tested when doing the right thing is easy; it is defined when integrity comes at personal cost.",
        "Accepting mortality does not make life pointless; it renders every conscious moment infinitely precious.",
        "True philosophical wisdom begins with the humility of acknowledging how little we genuinely know."
      ]
    },
    "Self-Help": {
      focus: "sustainable habit architecture, mental models, attention control, and personal compounding",
      hookPrefixes: [
        "Why willpower consistently fails, and how environment design turns difficult actions into natural habits.",
        "Stop optimizing for frantic productivity; start protecting the deep focus that generates true breakthroughs.",
        "The obstacle in your path is not an interruption to your work—it is the material you must work with.",
        "How to build emotional stamina when setbacks threaten to derail your long-term ambitions.",
        "Small, unglamorous disciplines practiced daily compound into outcomes that look like overnight magic."
      ],
      insightAngles: [
        "Consistency over time beats sporadic bursts of heroic intensity in every domain of human achievement.",
        "Your attention is your most irreplaceable currency; whatever you give it to becomes your life.",
        "Clarifying your core priorities requires learning the liberating power of saying no to good opportunities.",
        "Confidence is not a personality trait you wait to feel; it is a byproduct of keeping promises to yourself."
      ]
    },
    "Young Adult": {
      focus: "identity discovery, rebellion against unjust systems, friendship, and moral choices",
      hookPrefixes: [
        "When the rules of your world are engineered to keep you obedient, breaking them is the only moral act.",
        "A group of outcasts with complementary talents take on an impossible heist against corrupt powers.",
        "Growing up means realizing the adults in authority don't have all the answers—and sometimes lie.",
        "Standing up for someone vulnerable turns out to be far more dangerous than anyone warned you.",
        "In a society that demands conformity, discovering who you are is the ultimate act of defiance."
      ],
      insightAngles: [
        "Courage is not the absence of fear, but deciding that something else matters more than your safety.",
        "Real friendship is forged through shared vulnerability, not through performing perfection for peers.",
        "You do not have to wait until you are older to make an indelible difference in the world around you.",
        "Questioning authority is an essential step in forging authentic moral autonomy."
      ]
    },
    "True Crime": {
      focus: "investigative forensic rigor, human psychology, systemic justice, and seeking truth",
      hookPrefixes: [
        "The single forensic detail everyone overlooked for twenty years until an archivist opened the cold case.",
        "Behind the tranquil facade of a quiet suburban community lay a pattern of calculated, silent deception.",
        "How a dedicated team of investigators pieced together microscopic clues to bring justice to victims.",
        "A courtroom drama where the physical evidence clashed directly with charismatic witness testimony.",
        "The psychological anatomy of a con artist who manipulated financial systems and personal trust for decades."
      ],
      insightAngles: [
        "Real justice requires relentless, unglamorous persistence when the public spotlight has faded.",
        "Deception succeeds by exploiting our natural human desire to trust and avoid uncomfortable conflict.",
        "Forensic science has rewritten legal history, exposing the catastrophic flaws in eye-witness certainty.",
        "Honoring the dignity and voices of victims must always remain the moral center of crime investigation."
      ]
    },
    "Poetry": {
      focus: "emotional compression, sensory imagery, lyrical honesty, and transforming grief into art",
      hookPrefixes: [
        "A sequence of verses that captures the precise, wordless ache of losing a loved one.",
        "In a world drowning in digital noise, poetry restores sacred attention to the present moment.",
        "Lyrical lines that carve through emotional defenses, speaking directly to our quietest longings.",
        "Transforming ancient folklore and private sorrow into a radiant tapestry of modern survival.",
        "The economy of language: how four lines can alter your emotional relationship to your own past."
      ],
      insightAngles: [
        "Poetry gives voice to experiences that conventional analytical language is too clumsy to articulate.",
        "Naming your pain with precision strips it of its ability to haunt you as an amorphous dread.",
        "Beauty is not a superficial ornament; it is a vital spiritual sustenance that keeps the soul alive.",
        "Attentive presence to the ordinary world reveals that the miraculous is woven into daily life."
      ]
    },
    "Literary Fiction": {
      focus: "character psychology, moral nuance, stylistic brilliance, and the complexities of life",
      hookPrefixes: [
        "A family gathers across three generations, each harboring an unspoken truth that reshapes the inheritance.",
        "A profound meditation on how memory distorts the past to protect our fragile self-image.",
        "In lyrical, devastating prose, an ordinary life is illuminated with extraordinary psychological weight.",
        "The choices we make in our youth echo through decades, demanding a reckoning when least expected.",
        "A masterwork exploring the delicate, fragile boundaries between loneliness, desire, and forgiveness."
      ],
      insightAngles: [
        "Life rarely offers tidy moral conclusions; literary fiction trains our empathy for human ambiguity.",
        "We are all unreliable narrators of our own history, constantly editing our memories to justify our choices.",
        "Small, quiet gestures between people often carry more emotional consequence than dramatic events.",
        "True wisdom lies in holding compassion for flawed people without excusing the harm they cause."
      ]
    },
    "Biography & Memoir": {
      focus: "turning points, internal struggles, enduring legacy, and lessons from a lived life",
      hookPrefixes: [
        "Behind the world-famous triumphs lay decades of grueling obscurity, self-doubt, and private failure.",
        "How a pioneer from an underprivileged background defied social barriers to redefine their entire field.",
        "The private letters and diaries that reveal the human vulnerability behind an imposing public icon.",
        "A raw, courageous memoir about surviving family dysfunction and claiming the right to your own story.",
        "Leadership under pressure: the crucial decisions made when every advisor urged surrender."
      ],
      insightAngles: [
        "Great lives are not defined by uninterrupted success, but by resilience during prolonged seasons of failure.",
        "True leadership requires the moral courage to stand alone when popular opinion demands compromise.",
        "Your origins do not define your destination, but understanding them grants freedom from their shadows.",
        "Legacy is measured not by monuments or wealth, but by how many people were elevated by your work."
      ]
    },
    "Politics & Society": {
      focus: "institutional incentives, collective behavior, democratic health, and civic power",
      hookPrefixes: [
        "Why do political systems designed for democratic representation consistently succumb to factional gridlock?",
        "The unseen economic mechanisms that drive wealth concentration and reshape global civic trust.",
        "How propaganda evolves in the algorithmic era to divide communities through emotional contagion.",
        "A penetrating analysis of why democratic institutions must be actively protected by each generation.",
        "The grassroots movements that proved organized citizens hold more enduring power than concentrated capital."
      ],
      insightAngles: [
        "Democracy is not a permanent machine that runs of itself; it requires active, vigilant civic participation.",
        "Polarization worsens when political identity replaces shared community bonds as a source of belonging.",
        "Transparent accountability is the only antidote to the systemic abuse of public power.",
        "Meaningful societal progress is always achieved through persistent, unglamorous coalitions across divides."
      ]
    },

    "Self Discovery": {
      focus: "authentic identity, breaking self-sabotage, emotional courage, and personal transformation",
      hookPrefixes: [
        "What if the habits you can't break are secretly trying to protect you from an old emotional wound?",
        "Finding yourself does not mean inventing a new person; it means shedding who you thought you had to be.",
        "The mountain in your path is not an obstacle to your growth—it is the exact arena where you transform.",
        "Why do we repeatedly sabotage our happiest moments right when life begins to go well?",
        "The courageous question is not what other people expect of you, but what you are willing to let go of."
      ],
      insightAngles: [
        "Self-sabotage is simply a protective mechanism born from a time when hiding felt safer than being seen.",
        "You cannot hate yourself into a version of yourself that you love; transformation requires compassionate curiosity.",
        "Emotional discomfort is not a sign that something has gone wrong; it is the physical sensation of outgrowing a former life.",
        "True authenticity begins when the exhausting performance of pleasing everyone finally collapses."
      ]
    },
    "The Human Mind": {
      focus: "cognitive biases, emotional resilience, unconscious drivers, and behavior change",
      hookPrefixes: [
        "Why does your brain stubbornly cling to beliefs that empirical evidence has already disproven?",
        "The psychological mechanics of how stress quietly rewires our capacity for long-term planning.",
        "How our unconscious memory stores emotional patterns that dictate our adult relationship choices.",
        "The surprising science of neuroplasticity: how your brain physically reshapes itself around what you practice.",
        "Why human happiness depends far less on our external achievements than on how we narrate our experiences."
      ],
      insightAngles: [
        "Your thoughts are suggestions, not absolute commands; learning to observe them creates mental freedom.",
        "Emotional regulation begins with physical biology: sleep, movement, and environment set the mental baseline.",
        "Self-criticism activates the threat system, while compassionate curiosity facilitates genuine neuroplastic change.",
        "Understanding your cognitive biases is the first step toward reclaiming genuine sovereignty over your decisions."
      ]
    }
  };

  // Helper hash function to get consistent deterministic pseudo-random seeds per book
  function hashString(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = ((hash << 5) - hash) + str.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }

  // Clean raw description from Open Library (removes brackets, markdown, noise, publisher boilerplate)
  function cleanRawDescription(raw) {
    if (!raw) return "";
    let clean = String(raw)
      .replace(/<[^>]*>/g, " ")
      .replace(/\[\d+\]/g, "")
      .replace(/\(source:[^)]+\)/gi, "")
      .replace(/contains\s+spoilers/gi, "")
      .replace(/----------+/g, " ")
      .replace(/https?:\/\/\S+/g, "")
      .replace(/\s+/g, " ")
      .trim();
    return clean;
  }

  // Synthesize an 8-10 line curiosity feed preview packed with genuine insights
  function synthesizeFeedPreview(book, genreName) {
    const profile = GENRE_PROFILES[genreName] || GENRE_PROFILES["Literary Fiction"];
    const seed = hashString((book.title || "") + (book.author || ""));
    const rawDesc = cleanRawDescription(book.description || book.original_summary);

    const hookPrefix = profile.hookPrefixes[seed % profile.hookPrefixes.length];
    const insightAngle = profile.insightAngles[(seed + 1) % profile.insightAngles.length];

    let lines = [];
    lines.push(hookPrefix);

    if (rawDesc && rawDesc.length > 80) {
      // Extract the most evocative 2-3 sentences from raw description
      const sentences = rawDesc.split(/(?<=[.!?])\s+/).filter(s => s.length > 20 && !s.toLowerCase().includes("edition") && !s.toLowerCase().includes("published"));
      const bestExcerpt = sentences.slice(0, 2).join(" ");
      if (bestExcerpt.length > 60) {
        lines.push(bestExcerpt);
      } else {
        lines.push(`In this masterwork, ${book.author} crafts an immersive narrative centered around ${book.title}. The work explores ${profile.focus}, challenging how the reader understands the forces shaping human decisions.`);
      }
    } else {
      lines.push(`In this acclaimed exploration of ${genreName.toLowerCase()}, ${book.author} examines ${profile.focus}. Rather than offering easy answers or familiar tropes, the work draws the reader into the heart of a consequential conflict.`);
    }

    lines.push(`What makes ${book.title} so compelling is its refusal to simplify the psychological stakes. As the situation escalates, each character must confront the trade-offs between self-preservation and moral duty.`);
    lines.push(`The core takeaway is profound: ${insightAngle}`);
    lines.push(`Whether you are encountering ${book.author}'s work for the first time or returning to it, this book gives you an idea worth carrying into your own life.`);

    // Join into a substantial 8-10 line paragraph (approx 550 - 750 chars)
    let fullText = lines.join("\n");
    if (fullText.length < 520) {
      fullText += `\nScroll to explore another perspective, or select Read More to dive into the deeper editorial breakdown.`;
    }
    return fullText;
  }

  // Generate a distinct curiosity hook
  function synthesizeHook(book, genreName) {
    const profile = GENRE_PROFILES[genreName] || GENRE_PROFILES["Literary Fiction"];
    const seed = hashString((book.title || "") + "hook");
    return profile.hookPrefixes[seed % profile.hookPrefixes.length];
  }

  // Synthesize 4 structured reading sections for the Reader overlay
  function synthesizeReaderSections(book, genreName) {
    const profile = GENRE_PROFILES[genreName] || GENRE_PROFILES["Literary Fiction"];
    const seed = hashString((book.title || "") + "reader");
    const rawDesc = cleanRawDescription(book.description || book.original_summary);

    return [
      {
        title: "The Core Premise & Curiosity Hook",
        body: `${book.title} by ${book.author} immediately pulls the reader into a world governed by ${profile.focus}.\n${rawDesc ? rawDesc.slice(0, 400) + (rawDesc.length > 400 ? "..." : "") : "The narrative introduces a central dilemma where conventional solutions no longer apply, forcing the central figures to make high-stakes choices under relentless pressure."}\nThis is not just an entertaining story; it is a calculated inquiry into what happens when fundamental human assumptions are tested by extreme circumstances.`
      },
      {
        title: "Deep Dive: Themes & Conflict",
        body: `At the heart of ${book.title} lies a tension that mirrors our own societal struggles. ${book.author} constructs a complex architecture of conflict where every faction or character possesses an internally consistent logic.\nThe friction is not merely between good and evil, but between competing ideals that cannot both survive. This conceptual depth elevates the work beyond standard genre formulas, rewarding attentive reading with subtle layers of meaning.`
      },
      {
        title: "Key Insights & Takeaways",
        body: `RABBIT's primary takeaway from ${book.title}:\n\n1. ${profile.insightAngles[seed % profile.insightAngles.length]}\n\n2. The choices that seem most practical in the moment often carry hidden, systemic costs that compound over time.\n\n3. Real courage requires the willingness to embrace uncertainty rather than surrendering to comfortable illusions.\n\nReflecting on these principles reveals why ${book.author}'s work continues to spark intense discussion among curious readers.`
      },
      {
        title: "Why This Book Matters to Read",
        body: `In an era of disposable entertainment and superficial summaries, ${book.title} stands out for its intellectual honesty and emotional resonance.\nIt does not preach or lecture; instead, it provides a vivid, memorable lens through which to examine our own lives, relationships, and world.\nTaking time to go down this particular rabbit hole will leave you looking at ${genreName.toLowerCase()} with entirely new eyes.`
      }
    ];
  }

  // Public enrichment engine API
  window.RABBIT_ENRICH = {
    getEnrichedBook: function(book, genreName) {
      const g = genreName || window.rabbitSelectedGenre || "Literary Fiction";
      const titleLower = String(book.title || "").toLowerCase().trim();

      // Check if book exists in curated master catalog
      const catalog = window.RABBIT_CURATED_CATALOG || {};
      for (const [catGenre, books] of Object.entries(catalog)) {
        const found = books.find(b => b.title.toLowerCase().trim() === titleLower || b.id === book.id);
        if (found) {
          return {
            hook: found.hook,
            preview: found.preview,
            sections: found.sections,
            isCurated: true
          };
        }
      }

      // If not in static curated list, dynamically synthesize rich 8-10 line preview and reader guide!
      return {
        hook: synthesizeHook(book, g),
        preview: synthesizeFeedPreview(book, g),
        sections: synthesizeReaderSections(book, g),
        isCurated: false
      };
    },

    getGenreProfile: function(genreName) {
      return GENRE_PROFILES[genreName] || GENRE_PROFILES["Literary Fiction"];
    }
  };
})();
