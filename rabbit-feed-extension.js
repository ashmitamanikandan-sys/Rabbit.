/* RABBIT Fast Resilient Feed & Genre Discovery Extension
 * Guarantees:
 * 1. Zero-latency instant first render (0ms) from curated catalog + local cache
 * 2. Strict 3.5s fetch timeout with AbortController - never hangs or loops
 * 3. Graceful fallback on network timeout/rate-limit - never breaks UI
 * 4. Stale request cancellation when switching genres
 * 5. Full support for all 20+ genres including Self Discovery
 * 6. Substantial 8-10 line curiosity feed previews and 4-part reader overlays
 */
(function() {
  "use strict";

  const AUTHORITATIVE_GENRES = [
    "The Human Mind",
    "Self Discovery",
    "Science Fiction",
    "Fantasy",
    "Mystery & Thriller",
    "Romance",
    "Horror",
    "Historical Fiction",
    "Young Adult",
    "Classics",
    "Adventure",
    "Literary Fiction",
    "Philosophy",
    "Self-Help",
    "Business & Money",
    "Science",
    "History",
    "Biography & Memoir",
    "Politics & Society",
    "True Crime",
    "Poetry"
  ];

  const GENRE_SUBJECTS = {
    "The Human Mind": "psychology",
    "Self Discovery": "self_help",
    "Science Fiction": "science_fiction",
    "Fantasy": "fantasy",
    "Mystery & Thriller": "mystery",
    "Romance": "romance",
    "Horror": "horror",
    "Historical Fiction": "historical_fiction",
    "Young Adult": "young_adult_fiction",
    "Classics": "classic_literature",
    "Adventure": "adventure",
    "Literary Fiction": "literary_fiction",
    "Philosophy": "philosophy",
    "Self-Help": "self_help",
    "Business & Money": "business",
    "Science": "science",
    "History": "history",
    "Biography & Memoir": "biography",
    "Politics & Society": "politics",
    "True Crime": "true_crime",
    "Poetry": "poetry"
  };

  // State variables
  let currentAbortController = null;
  let requestEpoch = 0;
  let catalogBusy = false;
  let moreCount = 0;
  let searchTerm = "";
  let currentOffset = 0;
  const seenWorkIds = new Set();

  function escapeHtml(str) {
    return String(str || "").replace(/[&<>"']/g, c => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    }[c]));
  }

  // Robust genre resolver: maps aliases to standard genre names
  // NEVER silently defaults to "The Human Mind" when genreName is falsy or invalid!
  function resolveGenreKey(genreName) {
    if (!genreName) return null;
    const g = String(genreName).trim();
    if (!g) return null;
    const lower = g.toLowerCase();

    if (lower.includes("self discovery") || lower.includes("self-discovery")) return "Self Discovery";
    if (lower.includes("self-help") || lower.includes("self help") || lower.includes("productivity")) return "Self-Help";
    if (lower.includes("human mind") || lower === "the human mind" || lower.includes("psychology") || lower.includes("neuroscience") || lower.includes("behavior")) return "The Human Mind";
    if (lower.includes("sci-fi") || lower.includes("science fiction") || lower.includes("space") || lower.includes("technology") || lower.includes("artificial intelligence")) return "Science Fiction";
    if (lower.includes("fantasy") || lower.includes("mythology")) return "Fantasy";
    if (lower.includes("mystery") || lower.includes("thriller") || (lower.includes("crime") && !lower.includes("true crime"))) return "Mystery & Thriller";
    if (lower.includes("true crime")) return "True Crime";
    if (lower.includes("romance") || lower.includes("relationship") || lower.includes("love")) return "Romance";
    if (lower.includes("horror")) return "Horror";
    if (lower.includes("historical fiction")) return "Historical Fiction";
    if (lower.includes("history") || lower.includes("ancient")) return "History";
    if (lower.includes("young adult") || lower.includes("ya")) return "Young Adult";
    if (lower.includes("classic")) return "Classics";
    if (lower.includes("adventure") || lower.includes("travel")) return "Adventure";
    if (lower.includes("business") || lower.includes("money") || lower.includes("economic") || lower.includes("entrepreneurship") || lower.includes("leadership")) return "Business & Money";
    if (lower.includes("science") || lower.includes("environment") || lower.includes("nature")) return "Science";
    if (lower.includes("philosophy") || lower.includes("ethics")) return "Philosophy";
    if (lower.includes("biography") || lower.includes("memoir")) return "Biography & Memoir";
    if (lower.includes("politic") || lower.includes("society") || lower.includes("culture") || lower.includes("sociology") || lower.includes("feminism")) return "Politics & Society";
    if (lower.includes("poetry")) return "Poetry";
    if (lower.includes("literary") || lower.includes("fiction")) return "Literary Fiction";

    if (window.RABBIT_GENRES_CATALOG && window.RABBIT_GENRES_CATALOG[g]) {
      return g;
    }
    if (typeof AUTHORITATIVE_GENRES !== "undefined" && AUTHORITATIVE_GENRES.includes(g)) {
      return g;
    }
    return null;
  }

  function getActiveGenre() {
    if (window.rabbitSelectedGenre) {
      const resolved = resolveGenreKey(window.rabbitSelectedGenre);
      if (resolved) return resolved;
    }
    if (window.rabbitSelectedGenres && window.rabbitSelectedGenres.size > 0) {
      const first = Array.from(window.rabbitSelectedGenres)[0];
      const resolved = resolveGenreKey(first);
      if (resolved) return resolved;
    }
    try {
      const saved = localStorage.getItem("rabbit_selected_genre");
      if (saved) {
        const resolved = resolveGenreKey(saved);
        if (resolved) return resolved;
      }
    } catch (e) {}
    return "Self Discovery";
  }

  // Retrieve instant books (curated masterworks from 1,050 landmark catalog + localStorage cache)
  window.RABBIT_GENRES_CATALOG = window.RABBIT_GENRES_CATALOG || window.RABBIT_CURATED_CATALOG || {};
  window.RABBIT_CURATED_CATALOG = window.RABBIT_GENRES_CATALOG;

  // Multi-genre selection state & Mix Mode: Initialize with robust persistence and URL routing
  let initialGenre = null;
  try {
    const urlParams = new URLSearchParams(window.location.search);
    const genreParam = urlParams.get("genre");
    if (genreParam) initialGenre = resolveGenreKey(genreParam);
  } catch(e) {}

  if (!initialGenre) {
    try {
      const saved = localStorage.getItem("rabbit_selected_genre");
      if (saved) initialGenre = resolveGenreKey(saved);
    } catch (e) {}
  }

  let initialGenresList = [];
  try {
    const savedList = JSON.parse(localStorage.getItem("rabbit_selected_genres") || "[]");
    if (Array.isArray(savedList) && savedList.length > 0) {
      initialGenresList = savedList.map(resolveGenreKey).filter(Boolean);
    }
  } catch (e) {}

  window.rabbitSelectedGenres = window.rabbitSelectedGenres || new Set();
  if (initialGenresList.length > 0) {
    initialGenresList.forEach(g => window.rabbitSelectedGenres.add(g));
    window.rabbitSelectedGenre = initialGenresList[0];
  } else if (initialGenre) {
    window.rabbitSelectedGenres.add(initialGenre);
    window.rabbitSelectedGenre = initialGenre;
  } else {
    window.rabbitSelectedGenre = "Self Discovery";
    window.rabbitSelectedGenres.add("Self Discovery");
  }
  window.rabbitMixMode = (window.rabbitSelectedGenres.size > 1);

  // Sync browser popstate (Back/Forward navigation)
  window.addEventListener("popstate", (e) => {
    let target = null;
    if (e.state && e.state.genre) {
      target = e.state.genre;
    } else {
      const urlParams = new URLSearchParams(window.location.search);
      target = urlParams.get("genre") || localStorage.getItem("rabbit_selected_genre");
    }
    if (target && typeof window.switchSingleGenre === "function") {
      window.switchSingleGenre(target, false);
    }
  });

  
  // Global Local Search Helper across all 1,050 Landmark Books
  function searchMasterworkCatalog(query) {
    if (!query || !query.trim()) return [];
    const q = query.toLowerCase().trim();
    const results = [];
    const seen = new Set();
    const catalog = window.RABBIT_GENRES_CATALOG || {};
    for (const genreKey in catalog) {
      const list = catalog[genreKey] || [];
      for (const b of list) {
        const matchTitle = (b.title || "").toLowerCase().includes(q);
        const matchAuthor = (b.author || "").toLowerCase().includes(q);
        const matchHook = (b.hook || "").toLowerCase().includes(q);
        const matchGenre = (b.genre || "").toLowerCase().includes(q);
        if (matchTitle || matchAuthor || matchHook || matchGenre) {
          const id = b.id || b.title;
          if (!seen.has(id)) {
            seen.add(id);
            results.push(b);
          }
        }
      }
    }
    return results;
  }

  // Persistent User Library Storage
  function getSavedBooksList() {
    try {
      const list = JSON.parse(localStorage.getItem("rabbit_user_library") || "[]");
      if (list.length > 0) return list;

      // Migrate from rabbit_save_ keys if empty
      const catalog = window.RABBIT_GENRES_CATALOG || {};
      const migrated = [];
      const seen = new Set();
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith("rabbit_save_")) {
          const idOrTitle = k.replace("rabbit_save_", "");
          for (const g in catalog) {
            const found = (catalog[g] || []).find(b => (b.id === idOrTitle || b.title === idOrTitle));
            if (found && !seen.has(found.id || found.title)) {
              seen.add(found.id || found.title);
              migrated.push(found);
            }
          }
        }
      }
      if (migrated.length > 0) {
        localStorage.setItem("rabbit_user_library", JSON.stringify(migrated));
        return migrated;
      }
      return [];
    } catch (e) {
      return [];
    }
  }

  function saveBookToLibrary(book) {
    if (!book) return;
    try {
      const list = getSavedBooksList();
      const id = book.id || book.title;
      if (!list.some(b => (b.id && b.id === id) || b.title === book.title)) {
        list.unshift(Object.assign({}, book, { savedAt: Date.now() }));
        localStorage.setItem("rabbit_user_library", JSON.stringify(list));
      }
      localStorage.setItem("rabbit_save_" + id, "1");
    } catch (e) {}
  }

  function removeBookFromLibrary(book) {
    if (!book) return;
    try {
      const id = book.id || book.title;
      let list = getSavedBooksList();
      list = list.filter(b => (b.id && b.id !== id) && b.title !== book.title);
      localStorage.setItem("rabbit_user_library", JSON.stringify(list));
      localStorage.removeItem("rabbit_save_" + id);
    } catch (e) {}
  }

  function getFollowedBooksList() {
    try {
      const list = JSON.parse(localStorage.getItem("rabbit_user_followed") || "[]");
      if (list.length > 0) return list;
      const catalog = window.RABBIT_GENRES_CATALOG || {};
      const migrated = [];
      const seen = new Set();
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith("rabbit_follow_")) {
          const idOrTitle = k.replace("rabbit_follow_", "");
          for (const g in catalog) {
            const found = (catalog[g] || []).find(b => (b.id === idOrTitle || b.title === idOrTitle));
            if (found && !seen.has(found.id || found.title)) {
              seen.add(found.id || found.title);
              migrated.push(found);
            }
          }
        }
      }
      if (migrated.length > 0) {
        localStorage.setItem("rabbit_user_followed", JSON.stringify(migrated));
        return migrated;
      }
      return [];
    } catch (e) {
      return [];
    }
  }

  function followBook(book) {
    if (!book) return;
    try {
      const list = getFollowedBooksList();
      const id = book.id || book.title;
      if (!list.some(b => (b.id && b.id === id) || b.title === book.title)) {
        list.unshift(Object.assign({}, book, { followedAt: Date.now() }));
        localStorage.setItem("rabbit_user_followed", JSON.stringify(list));
      }
      localStorage.setItem("rabbit_follow_" + id, "1");
    } catch (e) {}
  }

  function unfollowBook(book) {
    if (!book) return;
    try {
      const id = book.id || book.title;
      let list = getFollowedBooksList();
      list = list.filter(b => (b.id && b.id !== id) && b.title !== book.title);
      localStorage.setItem("rabbit_user_followed", JSON.stringify(list));
      localStorage.removeItem("rabbit_follow_" + id);
    } catch (e) {}
  }

  function getInstantBooks(genreName) {
    if (!genreName) return [];
    const list = [];
    const key = genreName.toLowerCase().trim();

    // 1. Curated masterworks from static 1,050-book catalog
    const catalog = window.RABBIT_GENRES_CATALOG || window.RABBIT_CURATED_CATALOG || {};
    const curated = (typeof window.getRabbitInstantBooks === "function" ? window.getRabbitInstantBooks(key) : null) ||
                    catalog[key] || catalog[key.replace(/\s+/g, "-")] || [];
    curated.forEach(b => {
      list.push(Object.assign({}, b, { isCurated: true, genre: b.genre || genreName }));
    });

    // 2. Cached books from previous sessions
    try {
      const cacheStr = localStorage.getItem("rabbit_cache_" + key) || localStorage.getItem("rabbit_cache_" + genreName);
      if (cacheStr) {
        const cached = JSON.parse(cacheStr);
        if (Array.isArray(cached)) {
          cached.forEach(b => {
            if (!list.some(item => (item.id || item.title) === (b.id || b.title))) {
              list.push(b);
            }
          });
        }
      }
    } catch (e) {}

    return list;
  }

  // Mixed-Genre Round-Robin Interleaving Engine with 1-in-8 Serendipity Injection
  function getBlendedMixedBooks(genresArray) {
    if (!genresArray || !genresArray.length) return [];
    if (genresArray.length === 1) return getInstantBooks(genresArray[0]);

    const mixedBooks = [];
    const seen = new Set();
    const queues = {};
    genresArray.forEach(g => {
      queues[g] = [...getInstantBooks(g)];
    });

    let hasMore = true;
    let cardCount = 0;
    while (hasMore) {
      hasMore = false;
      for (const g of genresArray) {
        const q = queues[g];
        while (q && q.length > 0) {
          const candidate = q.shift();
          const key = candidate.id || candidate.title;
          if (!seen.has(key)) {
            seen.add(key);
            candidate.mixedGenre = g;
            mixedBooks.push(candidate);
            cardCount++;
            hasMore = true;

            // 1-in-8 Serendipity Injection from an unexpected unselected genre
            if (cardCount % 8 === 0) {
              const unselected = AUTHORITATIVE_GENRES.filter(x => !genresArray.includes(x));
              if (unselected.length > 0) {
                const randomGenre = unselected[Math.floor(Math.random() * unselected.length)];
                const serenPool = getInstantBooks(randomGenre);
                const pick = serenPool.find(p => !seen.has(p.id || p.title));
                if (pick) {
                  seen.add(pick.id || pick.title);
                  pick.isSerendipity = true;
                  pick.mixedGenre = randomGenre;
                  mixedBooks.push(pick);
                  cardCount++;
                }
              }
            }
            break;
          }
        }
      }
    }
    return mixedBooks;
  }

  // Save successful discoveries to localStorage
  function saveToLocalCache(genreName, newBooks) {
    if (!newBooks || !newBooks.length) return;
    try {
      const cacheKey = "rabbit_cache_" + genreName;
      let existing = [];
      const cacheStr = localStorage.getItem(cacheKey);
      if (cacheStr) {
        existing = JSON.parse(cacheStr) || [];
      }
      const existingIds = new Set(existing.map(b => b.id || b.title));
      newBooks.forEach(b => {
        if (!existingIds.has(b.id || b.title)) {
          existing.push({
            id: b.id,
            title: b.title,
            author: b.author,
            cover_url: b.cover_url,
            description: b.description
          });
        }
      });
      // Store at most 30 books per genre in cache to keep storage light
      localStorage.setItem(cacheKey, JSON.stringify(existing.slice(0, 30)));
    } catch (e) {}
  }

  // Render cards into the feed
  function addRealBookCards(rows) {
    const scroller = document.getElementById("homeScroll");
    if (!scroller || !rows || !rows.length) return;

    const storyRail = scroller.querySelector(".home-first .stories");
    if (storyRail) {
      if (storyRail.dataset.catalog !== "loaded") storyRail.dataset.catalog = "loaded";
      if (storyRail.querySelector(".muted")) storyRail.replaceChildren();
    }

    const nav = scroller.querySelector(".footnav");
    const fragment = document.createDocumentFragment();

    rows.forEach(book => {
      if (!book || !book.title || !book.author) return;

      // Add to story rail if cover available
      if (storyRail && storyRail.children.length < 24 && book.cover_url) {
        const story = document.createElement("button");
        story.className = "story";
        story.type = "button";
        const image = document.createElement("img");
        image.src = book.cover_url;
        image.alt = book.title;
        image.loading = "lazy";
        image.decoding = "async";
        const label = document.createElement("span");
        label.textContent = book.title;
        story.append(image, label);
        story.onclick = () => rabbitReader(book);
        storyRail.append(story);
      }

      // Synthesize editorial preview using RABBIT_ENRICH engine
      const enriched = window.RABBIT_ENRICH
        ? window.RABBIT_ENRICH.getEnrichedBook(book, getActiveGenre())
        : {
            hook: book.title,
            preview: book.description || book.original_summary || "Explore this book in the RABBIT catalog.",
            sections: []
          };

      book.__rabbitSections = enriched.sections;
      book.__rabbitHook = enriched.hook;
      book.__rabbitPreview = enriched.preview;

      const article = document.createElement("article");
      article.className = "feedpost rabbit-expanded-post";
      article.style.scrollSnapAlign = "start";

      const top = document.createElement("div");
      top.className = "top";
      if (typeof window.logo === "function") {
        top.innerHTML = '<span class="muted" style="font-size:11px;letter-spacing:1px">FOLLOW YOUR CURIOSITY</span>' + window.logo();
      }
      article.append(top);

      const body = document.createElement("div");
      body.className = "postbody";

      const meta = document.createElement("div");
      meta.className = "postmeta";
      const displayGenre = (book.genre || book.mixedGenre || getActiveGenre()).toUpperCase();
      meta.textContent = (enriched.isCurated ? "ORIGINAL RABBIT MASTERWORK" : "RABBIT BOOK DISCOVERY") +
        " · HOP " + String(++moreCount).padStart(2, "0") + " / " + displayGenre;
      if (book.isSerendipity) {
        const serenTag = document.createElement("div");
        serenTag.style.cssText = "font-size:11px;font-weight:700;letter-spacing:0.06em;color:#fcd34d;margin-top:4px;display:flex;align-items:center;gap:4px;";
        serenTag.textContent = "✨ SERENDIPITY PICK · " + displayGenre;
        body.append(serenTag);
      }
      body.append(meta);

      const row = document.createElement("div");
      row.className = "bookrow";
      row.style.marginTop = "20px";

      if (book.cover_url && book.cover_url.startsWith("http")) {
        const cover = document.createElement("img");
        cover.className = "cover";
        cover.src = book.cover_url;
        cover.alt = "Cover of " + book.title;
        cover.loading = "lazy";
        cover.decoding = "async";
        row.append(cover);
      }

      const details = document.createElement("div");
      details.style.flex = "1";
      details.style.minWidth = "0";
      const title = document.createElement("h3");
      title.textContent = book.title;
      const author = document.createElement("p");
      author.textContent = book.author;
      details.append(title, author);
      row.append(details);
      body.append(row);

      // Headline Hook (Curiosity)
      const headline = document.createElement("h2");
      headline.textContent = enriched.hook || book.title;
      headline.style.marginTop = "16px";
      headline.style.lineHeight = "1.25";
      body.append(headline);

      // 8-10 Line Insight Preview
      const info = document.createElement("div");
      info.className = "insight";
      info.style.whiteSpace = "pre-line";
      info.style.lineHeight = "1.55";
      info.style.margin = "14px 0";
      info.textContent = enriched.preview;
      body.append(info);

      // Actions: Read More, Save, Follow
      const actions = document.createElement("div");
      actions.className = "actions";

      const read = document.createElement("button");
      read.className = "readmore";
      read.textContent = "Read more ↗";
      read.onclick = () => rabbitReader(book);
      actions.append(read);

      const save = document.createElement("button");
      const sk = "rabbit_save_" + (book.id || book.title);
      const isSaved = !!localStorage.getItem(sk);
      save.textContent = isSaved ? "◆ Saved" : "◇ Save";
      save.onclick = () => {
        const currentlySaved = !!localStorage.getItem(sk);
        if (currentlySaved) {
          removeBookFromLibrary(book);
          save.textContent = "◇ Save";
        } else {
          saveBookToLibrary(book);
          save.textContent = "◆ Saved";
        }
      };
      actions.append(save);

      const follow = document.createElement("button");
      const fk = "rabbit_follow_" + (book.id || book.title);
      const isFollowed = !!localStorage.getItem(fk);
      follow.textContent = isFollowed ? "♥ Following" : "♡ Follow book";
      follow.onclick = () => {
        const currentlyFollowed = !!localStorage.getItem(fk);
        if (currentlyFollowed) {
          unfollowBook(book);
          follow.textContent = "♡ Follow book";
        } else {
          followBook(book);
          follow.textContent = "♥ Following";
        }
      };
      actions.append(follow);

      const share = document.createElement("button");
      share.className = "rabbit-share-btn";
      share.setAttribute("aria-label", "Share book");
      share.style.cssText = "display:inline-flex;align-items:center;gap:4px;background:none;border:none;color:#ddd;cursor:pointer;padding:4px 6px;font-size:12px;margin-left:auto;";
      share.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg><span>Share</span>';
      share.onclick = () => {
        if (typeof window.rabbitShareBook === "function") {
          window.rabbitShareBook(book);
        } else if (navigator.share) {
          navigator.share({ title: book.title, text: book.title + " — " + (book.author || "RABBIT"), url: location.href }).catch(() => {});
        } else if (navigator.clipboard) {
          navigator.clipboard.writeText(location.href).then(() => { if (typeof toast === 'function') toast('Link copied to clipboard! ↗'); });
        }
      };
      actions.append(share);

      body.append(actions);

      const note = document.createElement("p");
      note.className = "muted";
      note.style.fontSize = "11px";
      note.style.marginTop = "14px";
      note.textContent = "Book listing · Swipe down for another discovery ↓";
      body.append(note);

      article.append(body);
      fragment.append(article);
    });

    if (nav) {
      scroller.insertBefore(fragment, nav);
    } else {
      scroller.append(fragment);
    }
  }

  // Interactive 4-Part Reader Overlay
  function rabbitReader(book) {
    const old = document.querySelector(".rabbit-reader-overlay");
    if (old) old.remove();

    const overlay = document.createElement("div");
    overlay.className = "rabbit-reader-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "RABBIT book reader");

    const panel = document.createElement("div");
    panel.className = "rabbit-reader-panel rabbit-chapter-reader";

    const close = document.createElement("button");
    close.className = "rabbit-reader-close";
    close.type = "button";
    close.textContent = "← Back to the rabbit hole";

    // Quick Save button in Reader Header
    const readerSaveBtn = document.createElement("button");
    readerSaveBtn.type = "button";
    readerSaveBtn.className = "rabbit-reader-save-btn";
    const rsk = "rabbit_save_" + (book.id || book.title);
    readerSaveBtn.style.cssText = "float:right;padding:6px 14px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;background:rgba(168,85,247,0.18);color:#d8b4fe;border:1px solid rgba(168,85,247,0.4);transition:all 0.2s ease;";
    readerSaveBtn.textContent = localStorage.getItem(rsk) ? "◆ Saved in Library" : "◇ Save to Library";
    readerSaveBtn.onclick = () => {
      if (localStorage.getItem(rsk)) {
        removeBookFromLibrary(book);
        readerSaveBtn.textContent = "◇ Save to Library";
      } else {
        saveBookToLibrary(book);
        readerSaveBtn.textContent = "◆ Saved in Library";
      }
    };
    panel.append(readerSaveBtn);

    const readerShareBtn = document.createElement("button");
    readerShareBtn.type = "button";
    readerShareBtn.className = "rabbit-reader-share-btn";
    readerShareBtn.style.cssText = "float:right;margin-right:8px;padding:6px 14px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;background:rgba(255,255,255,0.08);color:#eee;border:1px solid #444;transition:all 0.2s ease;display:inline-flex;align-items:center;gap:5px;";
    readerShareBtn.innerHTML = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg><span>Share</span>';
    readerShareBtn.onclick = () => {
      if (typeof window.rabbitShareBook === "function") window.rabbitShareBook(book);
      else if (navigator.share) navigator.share({title:book.title, url:location.href}).catch(() => {});
      else if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(() => { if (typeof toast === 'function') toast('Link copied! ↗'); });
    };
    panel.append(readerShareBtn);

    const eyebrow = document.createElement("div");
    eyebrow.className = "eyebrow";
    eyebrow.textContent = getActiveGenre().toUpperCase() + " / RABBIT READER";

    const title = document.createElement("h1");
    title.textContent = book.title;

    const author = document.createElement("p");
    author.className = "muted";
    author.textContent = "By " + book.author;

    const intro = document.createElement("p");
    intro.className = "rabbit-chapter-intro";
    intro.textContent = "Original RABBIT editorial breakdown. Explore the core premise, key themes, and actionable insights from this work.";

    const sections = (book.sections && book.sections.length ? book.sections : null) || book.__rabbitSections || (window.RABBIT_ENRICH ? window.RABBIT_ENRICH.getEnrichedBook(book, getActiveGenre()).sections : []);

    const label = document.createElement("div");
    label.className = "rabbit-chapter-status";
    label.textContent = "EDITORIAL TOPICS & INSIGHTS · 4 Comprehensive Sections";

    const layout = document.createElement("div");
    layout.className = "rabbit-chapter-layout";

    const nav = document.createElement("nav");
    nav.className = "rabbit-chapter-nav";
    nav.setAttribute("aria-label", "Reading sections");

    const page = document.createElement("section");
    page.className = "rabbit-chapter-page";
    page.setAttribute("aria-live", "polite");

    const storageKey = "rabbit-reader-progress:" + String(book.id || book.title).slice(0, 140);
    let current = 0;
    try {
      current = Math.max(0, Math.min(sections.length - 1, Number(localStorage.getItem(storageKey)) || 0));
    } catch (e) {
      current = 0;
    }

    const buttons = [];

    function showSection(index) {
      if (index < 0 || index >= sections.length) return;
      current = index;
      page.replaceChildren();

      const counter = document.createElement("div");
      counter.className = "eyebrow";
      counter.textContent = "RABBIT ORIGINAL · SECTION " + (index + 1) + " OF " + sections.length;

      const heading = document.createElement("h2");
      heading.textContent = sections[index].title;

      const copy = document.createElement("p");
      copy.className = "rabbit-chapter-body";
      copy.style.whiteSpace = "pre-line";
      copy.style.lineHeight = "1.65";
      copy.textContent = sections[index].body;

      const note = document.createElement("p");
      note.className = "rabbit-chapter-disclaimer";
      note.textContent = "Original RABBIT editorial synthesis. Designed to spark curiosity and convey the author's core ideas.";

      const controls = document.createElement("div");
      controls.className = "rabbit-chapter-controls";

      const previous = document.createElement("button");
      previous.type = "button";
      previous.textContent = "← Previous";
      previous.disabled = index === 0;
      previous.onclick = () => showSection(current - 1);

      const next = document.createElement("button");
      next.type = "button";
      next.textContent = index === sections.length - 1 ? "Finished ✓" : "Next topic →";
      next.onclick = () => {
        if (index === sections.length - 1) {
          dismiss();
        } else {
          showSection(current + 1);
        }
      };

      controls.append(previous, next);
      page.append(counter, heading, copy, note, controls);

      buttons.forEach((btn, i) => {
        btn.setAttribute("aria-current", i === index ? "true" : "false");
      });

      try {
        localStorage.setItem(storageKey, String(index));
      } catch (e) {}
    }

    sections.forEach((sec, i) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "rabbit-chapter-link";
      btn.textContent = String(i + 1).padStart(2, "0") + "  " + sec.title;
      btn.onclick = () => showSection(i);
      nav.append(btn);
      buttons.push(btn);
    });

    layout.append(nav, page);
    panel.append(close, eyebrow, title, author, intro, label, layout);
    overlay.append(panel);
    document.body.append(overlay);

    function dismiss() {
      overlay.remove();
      document.removeEventListener("keydown", keys);
    }

    close.onclick = dismiss;
    overlay.addEventListener("click", e => {
      if (e.target === overlay) dismiss();
    });

    function keys(e) {
      if (e.key === "Escape") dismiss();
    }
    document.addEventListener("keydown", keys);
    close.focus();

    showSection(current);
  }

  window.rabbitOpenBook = rabbitReader;

  // Background incremental discovery with strict 3.5s timeout
  async function loadBackgroundBooks(targetGenre, epoch) {
    if (catalogBusy) return;
    catalogBusy = true;

    // Set up AbortController with 3.5s timeout
    if (currentAbortController) {
      currentAbortController.abort();
    }
    const controller = new AbortController();
    currentAbortController = controller;
    const timeoutId = setTimeout(() => controller.abort(), 3500);

    try {
      const subject = GENRE_SUBJECTS[targetGenre] || "fiction";
      const params = new URLSearchParams({
        limit: "10",
        offset: String(currentOffset),
        fields: "key,title,author_name,cover_i,language,first_sentence"
      });

      if (searchTerm) {
        params.set("q", searchTerm);
      } else {
        params.set("subject", subject);
      }

      const res = await fetch("https://openlibrary.org/search.json?" + params.toString(), {
        signal: controller.signal
      });
      clearTimeout(timeoutId);

      if (!res.ok) throw new Error("HTTP " + res.status);
      const data = await res.json();

      if (epoch !== requestEpoch) return;

      const newBooks = (data.docs || [])
        .filter(b => b.key && b.title && b.author_name?.length && (!b.language || b.language.includes("eng")))
        .map(b => ({
          id: b.key,
          title: b.title,
          author: b.author_name[0],
          cover_url: b.cover_i ? "https://covers.openlibrary.org/b/id/" + b.cover_i + "-M.jpg" : "",
          description: (Array.isArray(b.first_sentence) ? b.first_sentence[0] : b.first_sentence) || ""
        }));

      const toRender = [];
      newBooks.forEach(b => {
        if (!seenWorkIds.has(b.id || b.title)) {
          seenWorkIds.add(b.id || b.title);
          toRender.push(b);
        }
      });

      if (toRender.length > 0) {
        currentOffset += toRender.length;
        const slot = document.getElementById("rabbit-first-book-slot");
        if (slot && !slot.querySelector(".feature")) {
          const firstBook = toRender.shift();
          renderFirstBookSlot(firstBook, targetGenre);
        }
        if (toRender.length > 0) {
          addRealBookCards(toRender);
        }
        saveToLocalCache(targetGenre, toRender);
        window.RabbitSmartLoader.done();
      }
    } catch (err) {
      console.warn("Background fetch completed or timed out for:", targetGenre);
      const scroller = document.getElementById("homeScroll");
      const hasCards = scroller && scroller.querySelectorAll(".feedpost, .rabbit-featured-insight-card").length > 0;
      if (!hasCards) {
        window.RabbitSmartLoader.fail();
      } else {
        window.RabbitSmartLoader.done();
      }
    } finally {
      clearTimeout(timeoutId);
      catalogBusy = false;

      // Always ensure "Finding book stories..." is cleared
      const scroller = document.getElementById("homeScroll");
      if (scroller) {
        const rail = scroller.querySelector(".home-first .stories");
        if (rail && rail.querySelector(".muted") && rail.children.length > 1) {
          rail.querySelector(".muted").remove();
        }
      }
    }
  }

  // Build the horizontal 20-Genre Navigation Bar in the feed
  function renderGenreBar(container) {
    if (!container) return;
    const existing = container.querySelector(".rabbit-genre-nav-bar");
    if (existing) existing.remove();

    const bar = document.createElement("div");
    bar.className = "rabbit-genre-nav-bar";
    bar.style.cssText = "display:flex;overflow-x:auto;white-space:nowrap;gap:8px;padding:12px 0 16px;scrollbar-width:none;-webkit-overflow-scrolling:touch;align-items:center;";

    // If multiple genres are selected, prepend [ ✕ Clear Mix (N) ] button
    if (window.rabbitSelectedGenres && window.rabbitSelectedGenres.size > 1) {
      const clearBtn = document.createElement("button");
      clearBtn.type = "button";
      clearBtn.className = "chip rabbit-mix-clear-chip";
      clearBtn.style.cssText = "flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 14px;border-radius:20px;background:rgba(239,68,68,0.18);color:#fca5a5;border:1px solid rgba(239,68,68,0.4);font-weight:700;display:inline-flex;align-items:center;gap:5px;transition:all 0.2s ease;";
      clearBtn.innerHTML = "<span>✕</span> Clear Mix (" + window.rabbitSelectedGenres.size + ")";
      clearBtn.onclick = () => {
        resetToSingleGenre();
      };
      bar.append(clearBtn);
    } else {
      // Single genre mode: show a chic "+ Mix" trigger chip
      const mixTrigger = document.createElement("button");
      mixTrigger.type = "button";
      mixTrigger.className = "chip rabbit-mix-toggle-chip";
      mixTrigger.style.cssText = "flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 12px;border-radius:20px;background:rgba(168,85,247,0.12);color:#d8b4fe;border:1px dashed rgba(168,85,247,0.45);font-weight:600;display:inline-flex;align-items:center;gap:4px;transition:all 0.2s ease;";
      mixTrigger.innerHTML = window.rabbitMixMode ? "✓ Mixing Active" : "<span>+</span> Mix Genres";
      mixTrigger.onclick = () => {
        window.rabbitMixMode = !window.rabbitMixMode;
        renderGenreBar(container);
      };
      bar.append(mixTrigger);
    }

    // Quick access button to full-screen genre modal
    const manageBtn = document.createElement("button");
    manageBtn.type = "button";
    manageBtn.className = "chip";
    manageBtn.style.cssText = "flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 14px;border-radius:20px;background:rgba(167,139,250,0.18);border:1px solid #A78BFA;color:#E9D5FF;font-weight:700;";
    manageBtn.textContent = "✦ Edit Genres";
    manageBtn.onclick = () => {
      if (window.RabbitGenreModal) window.RabbitGenreModal.open({ fromNav: true });
    };
    bar.append(manageBtn);

    AUTHORITATIVE_GENRES.forEach(g => {
      const isSelected = window.rabbitSelectedGenres && window.rabbitSelectedGenres.has(g);
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "chip" + (isSelected ? " active" : "");
      btn.style.cssText = "flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 14px;border-radius:20px;transition:all 0.2s ease;";
      btn.textContent = g;
      btn.dataset.genre = g;

      btn.onclick = (e) => {
        const isMulti = e.shiftKey || e.ctrlKey || e.metaKey || window.rabbitMixMode || (window.rabbitSelectedGenres && window.rabbitSelectedGenres.size > 1);
        if (isMulti) {
          toggleGenre(g);
        } else {
          switchSingleGenre(g);
        }
      };
      bar.append(btn);
    });

    container.append(bar);
  }


  // ========================================================
  // Phase 2: SMART RABBIT LOADING SCREEN
  // ========================================================
  window.RabbitSmartLoader = (function() {
    let loaderEl = null;
    let timerId = null;
    let messageInterval = null;
    let timeoutId = null;
    let currentRetryFn = null;
    let currentGenre = "";

    const messages = [
      "Digging into the library burrow…",
      "Sniffing out rare ideas and hidden chapters…",
      "Unearthing books worth falling into…",
      "Filtering through thousands of thoughts…",
      "Curating your next great curiosity…",
      "Almost there — preparing your rabbit hole…"
    ];
    let msgIndex = 0;

    function ensureMounted() {
      if (loaderEl && document.body.contains(loaderEl)) return loaderEl;
      const existing = document.getElementById("rabbit-smart-loader");
      if (existing) {
        loaderEl = existing;
        return loaderEl;
      }

      loaderEl = document.createElement("div");
      loaderEl.id = "rabbit-smart-loader";
      loaderEl.className = "rabbit-smart-loader";
      loaderEl.setAttribute("aria-live", "polite");
      loaderEl.innerHTML = `
        <div class="rabbit-smart-loader-card">
          <div class="rabbit-hopper-container">
            <svg class="rabbit-hopper-svg" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
              <g class="rabbit-hopper-body">
                <path d="M34 26C34 16 38 8 42 8C46 8 46 16 44 26" stroke="#bca6ff" stroke-width="2.8" stroke-linecap="round" fill="rgba(188,166,255,0.18)"/>
                <path d="M40 24C42 14 47 7 51 8C55 9 53 18 49 26" stroke="#bca6ff" stroke-width="3" stroke-linecap="round" fill="rgba(188,166,255,0.3)"/>
                <circle cx="44" cy="32" r="9" fill="#181622" stroke="#bca6ff" stroke-width="2.5"/>
                <circle cx="47" cy="30" r="1.6" fill="#bca6ff"/>
                <circle cx="53" cy="33" r="1.2" fill="#e8e4f5"/>
                <path d="M52 35L57 36M52 34L58 33" stroke="rgba(188,166,255,0.6)" stroke-width="1.2" stroke-linecap="round"/>
                <ellipse cx="33" cy="46" rx="15" ry="12" fill="#181622" stroke="#bca6ff" stroke-width="2.5"/>
                <circle cx="17" cy="46" r="4.5" fill="#bca6ff" stroke="#e8e4f5" stroke-width="1.5"/>
                <ellipse cx="44" cy="56" rx="4" ry="2.5" fill="#bca6ff"/>
                <ellipse cx="28" cy="56" rx="6" ry="3.5" fill="#bca6ff"/>
              </g>
              <ellipse class="rabbit-hopper-shadow" cx="36" cy="68" rx="20" ry="4" fill="rgba(188,166,255,0.25)"/>
            </svg>
          </div>
          <div class="rabbit-loader-status" id="rabbit-loader-status">
            <div class="rabbit-loader-genre-badge" id="rabbit-loader-genre">THE BURROW</div>
            <p class="rabbit-loader-message" id="rabbit-loader-msg">Digging into the library burrow…</p>
          </div>
          <div class="rabbit-loader-error" id="rabbit-loader-error" hidden>
            <p class="rabbit-error-text">The library burrow took too long to respond.</p>
            <button type="button" class="rabbit-retry-btn" id="rabbit-loader-retry">Try Again ↻</button>
          </div>
        </div>
      `;
      document.body.appendChild(loaderEl);

      const retryBtn = loaderEl.querySelector("#rabbit-loader-retry");
      if (retryBtn) {
        retryBtn.onclick = () => {
          if (typeof currentRetryFn === "function") {
            currentRetryFn();
          }
        };
      }
      return loaderEl;
    }

    function start(genre, retryFn) {
      clearTimers();
      currentGenre = genre || "Curiosity Feed";
      currentRetryFn = retryFn;
      msgIndex = 0;

      // Strict 500ms threshold: Content loaded under 500ms NEVER shows the loader!
      timerId = setTimeout(() => {
        show();
      }, 500);
    }

    function show() {
      const el = ensureMounted();
      const genreBadge = el.querySelector("#rabbit-loader-genre");
      if (genreBadge) genreBadge.textContent = currentGenre.toUpperCase();

      const msgEl = el.querySelector("#rabbit-loader-msg");
      if (msgEl) msgEl.textContent = messages[0];

      const errEl = el.querySelector("#rabbit-loader-error");
      if (errEl) errEl.hidden = true;
      const statusEl = el.querySelector("#rabbit-loader-status");
      if (statusEl) statusEl.hidden = false;

      el.classList.add("visible");

      if (messageInterval) clearInterval(messageInterval);
      messageInterval = setInterval(() => {
        msgIndex = (msgIndex + 1) % messages.length;
        if (msgEl) {
          msgEl.classList.add("swapping");
          setTimeout(() => {
            msgEl.textContent = messages[msgIndex];
            msgEl.classList.remove("swapping");
          }, 280);
        }
      }, 1800);

      timeoutId = setTimeout(() => {
        fail();
      }, 4500);
    }

    function done() {
      clearTimers();
      if (loaderEl && loaderEl.classList.contains("visible")) {
        loaderEl.classList.remove("visible");
        if (messageInterval) {
          clearInterval(messageInterval);
          messageInterval = null;
        }
      }
    }

    function fail() {
      if (messageInterval) {
        clearInterval(messageInterval);
        messageInterval = null;
      }
      const el = ensureMounted();
      el.classList.add("visible");
      const statusEl = el.querySelector("#rabbit-loader-status");
      if (statusEl) statusEl.hidden = true;
      const errEl = el.querySelector("#rabbit-loader-error");
      if (errEl) errEl.hidden = false;
    }

    function clearTimers() {
      if (timerId) {
        clearTimeout(timerId);
        timerId = null;
      }
      if (timeoutId) {
        clearTimeout(timeoutId);
        timeoutId = null;
      }
      if (messageInterval) {
        clearInterval(messageInterval);
        messageInterval = null;
      }
    }

    return {
      start,
      done,
      fail
    };
  })();

  // ========================================================
  // Phase 2: RENDER FIRST REAL BOOK INSIGHT (NO UNWANTED CARD!)
  // ========================================================
  function renderFirstBookSlot(book, genreName) {
    const scroller = document.getElementById("homeScroll");
    if (!scroller || !book) return;

    let slot = scroller.querySelector("#rabbit-first-book-slot");
    if (!slot) {
      const oldFeature = scroller.querySelector(".home-first .feature");
      if (oldFeature) {
        slot = document.createElement("div");
        slot.id = "rabbit-first-book-slot";
        slot.className = "rabbit-first-book-slot";
        oldFeature.replaceWith(slot);
      } else {
        const sec = scroller.querySelector(".home-first .section");
        if (!sec) return;
        slot = document.createElement("div");
        slot.id = "rabbit-first-book-slot";
        slot.className = "rabbit-first-book-slot";
        sec.appendChild(slot);
      }
    }

    // Synthesize editorial preview using RABBIT_ENRICH engine
    const enriched = window.RABBIT_ENRICH
      ? window.RABBIT_ENRICH.getEnrichedBook(book, genreName)
      : {
          hook: book.title,
          preview: book.description || book.original_summary || "Explore this book in the RABBIT catalog.",
          sections: []
        };

    book.__rabbitSections = enriched.sections;
    book.__rabbitHook = enriched.hook;
    book.__rabbitPreview = enriched.preview;

    const sk = "rabbit_save_" + (book.id || book.title);
    const isSaved = localStorage.getItem(sk);
    const lk = "rabbit_like_" + (book.id || book.title);
    const isLiked = localStorage.getItem(lk);

    slot.innerHTML = `
      <div class="feature rabbit-featured-insight-card">
        <div class="bookrow" style="display:flex;align-items:center;gap:14px;margin-top:6px">
          ${book.cover_url ? `<img src="${escapeHtml(book.cover_url)}" alt="${escapeHtml(book.title)}" class="cover" style="width:52px;height:74px;object-fit:cover;border-radius:6px;box-shadow:0 6px 16px rgba(0,0,0,0.55);flex-shrink:0" loading="lazy" decoding="async">` : `<div style="width:52px;height:74px;background:#242428;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#bca6ff;font-weight:700">R</div>`}
          <div style="flex:1;min-width:0">
            <h3 style="font-size:17px;font-weight:600;margin:0 0 4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${escapeHtml(book.title)}</h3>
            <p class="muted" style="font-size:13px;margin:0">${escapeHtml(book.author || "RABBIT Curator")}</p>
            <span class="chip" style="font-size:10px;padding:3px 10px;margin-top:6px;display:inline-block;background:rgba(188,166,255,0.12);border-color:rgba(188,166,255,0.3)">${escapeHtml(genreName)}</span>
          </div>
        </div>
        <div class="eyebrow" style="margin-top:16px;font-size:11px;letter-spacing:1px;color:#bca6ff">THE FIRST HOP · 001</div>
        <h3 style="font-size:22px;letter-spacing:-0.4px;line-height:1.24;margin:10px 0;font-weight:600">${escapeHtml(enriched.hook || book.title)}</h3>
        <div class="insight" style="white-space:pre-line;line-height:1.62;margin:12px 0;font-size:14px;color:#dedede">${escapeHtml(enriched.preview)}</div>
        <div class="actions" style="display:flex;align-items:center;gap:10px;margin-top:16px">
          <button class="rabbit-card-btn ${isLiked ? 'active' : ''}" id="rabbit-featured-like-btn" aria-label="Like book" style="background:rgba(255,255,255,0.06);border:1px solid #333;color:#ddd;padding:8px 14px;border-radius:20px;cursor:pointer;font-size:13px;display:inline-flex;align-items:center;gap:5px">${isLiked ? '♥ Liked' : '♡ Like'}</button>
          <button class="rabbit-card-btn ${isSaved ? 'active' : ''}" id="rabbit-featured-save-btn" aria-label="Save book" style="background:rgba(255,255,255,0.06);border:1px solid #333;color:#ddd;padding:8px 14px;border-radius:20px;cursor:pointer;font-size:13px;display:inline-flex;align-items:center;gap:5px">${isSaved ? '◆ Saved' : '◇ Save'}</button>
          <button class="rabbit-card-btn" id="rabbit-featured-share-btn" aria-label="Share book" style="background:rgba(255,255,255,0.06);border:1px solid #333;color:#ddd;padding:8px 14px;border-radius:20px;cursor:pointer;font-size:13px;display:inline-flex;align-items:center;gap:5px"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg><span>Share</span></button>
          <button class="readmore" id="rabbit-featured-read-btn" style="margin-left:auto;background:transparent;border:1px solid #bca6ff;color:#bca6ff;padding:8px 16px;border-radius:20px;cursor:pointer;font-size:13px;font-weight:500">Read more ↗</button>
        </div>
        <div class="subtle" style="margin-top:14px;font-size:11px;color:#888;text-align:center">↓ Scroll to fall deeper into the rabbit hole</div>
      </div>
    `;

    const readBtn = slot.querySelector("#rabbit-featured-read-btn");
    if (readBtn) readBtn.onclick = () => rabbitReader(book);
    const featuredShareBtn = slot.querySelector("#rabbit-featured-share-btn");
    if (featuredShareBtn) featuredShareBtn.onclick = () => window.rabbitShareBook ? window.rabbitShareBook(book) : (navigator.share ? navigator.share({title:book.title, url:location.href}) : null);

    const likeBtn = slot.querySelector("#rabbit-featured-like-btn");
    if (likeBtn) {
      likeBtn.onclick = () => {
        if (localStorage.getItem(lk)) {
          localStorage.removeItem(lk);
          likeBtn.classList.remove("active");
          likeBtn.textContent = "♡ Like";
        } else {
          localStorage.setItem(lk, "1");
          likeBtn.classList.add("active");
          likeBtn.textContent = "♥ Liked";
        }
      };
    }

    const saveBtn = slot.querySelector("#rabbit-featured-save-btn");
    if (saveBtn) {
      saveBtn.onclick = () => {
        if (localStorage.getItem(sk)) {
          localStorage.removeItem(sk);
          saveBtn.classList.remove("active");
          saveBtn.textContent = "◇ Save";
        } else {
          localStorage.setItem(sk, "1");
          saveBtn.classList.add("active");
          saveBtn.textContent = "◆ Saved";
        }
      };
    }
  }


  // Instant zero-latency switch between genres
  window.switchGenre = switchGenre;
  window.switchSingleGenre = switchSingleGenre;
  window.toggleGenre = toggleGenre;
  window.resetToSingleGenre = resetToSingleGenre;
  window.renderFeedForCurrentSelection = renderFeedForCurrentSelection;
  window.applyGenreSelectionAndRefreshFeed = renderFeedForCurrentSelection;

  window.renderUserLibrary = function() {
    const scroller = document.getElementById("homeScroll");
    if (!scroller) return;

    if (currentAbortController) currentAbortController.abort();
    requestEpoch++;
    currentOffset = 0;
    moreCount = 0;
    catalogBusy = false;
    searchTerm = "";
    seenWorkIds.clear();

    const savedBooks = getSavedBooksList();
    const heading = scroller.querySelector(".section-head .muted");
    if (heading) heading.textContent = `MY LIBRARY (${savedBooks.length} SAVED)`;

    // Update active top nav tab highlight
    document.querySelectorAll(".rabbit-top-nav-item").forEach(btn => {
      btn.classList.toggle("active", btn.getAttribute("onclick")?.includes("'library'"));
    });

    scroller.querySelectorAll(".rabbit-expanded-post").forEach(el => el.remove());
    const firstSec = scroller.querySelector(".home-first");
    if (firstSec) {
      const stories = firstSec.querySelector(".stories");
      if (stories) stories.replaceChildren();
    }

    if (savedBooks.length === 0) {
      const slot = document.getElementById("rabbit-first-book-slot");
      if (slot) {
        slot.replaceChildren();
        const emptyCard = document.createElement("div");
        emptyCard.className = "feedpost rabbit-expanded-post";
        emptyCard.style.cssText = "padding:48px 24px;text-align:center;background:rgba(20,20,24,0.7);border-radius:18px;border:1px solid rgba(255,255,255,0.08);margin-top:20px;";
        emptyCard.innerHTML = `
          <div style="font-size:36px;margin-bottom:14px;">📚</div>
          <h2 style="font-size:20px;color:#f3f4f6;margin-bottom:8px;">Your Library Burrow is Empty</h2>
          <p style="font-size:14px;color:#9ca3af;line-height:1.6;max-width:380px;margin:0 auto 20px;">
            Tap <strong style="color:#c4b5fd;">◇ Save</strong> on any book insight card or reader overlay to preserve your favorite reads here.
          </p>
          <button type="button" class="primary" style="padding:10px 20px;border-radius:24px;cursor:pointer;font-weight:600;" onclick="window.resetToSingleGenre()">
            ✦ Explore Masterworks Feed
          </button>
        `;
        slot.append(emptyCard);
      }
    } else {
      renderFirstBookSlot(savedBooks[0], "MY LIBRARY");
      seenWorkIds.add(savedBooks[0].id || savedBooks[0].title);
      if (savedBooks.length > 1) {
        const rest = savedBooks.slice(1);
        rest.forEach(b => seenWorkIds.add(b.id || b.title));
        addRealBookCards(rest);
      }
    }
  };

  window.renderUserFollowing = function() {
    const scroller = document.getElementById("homeScroll");
    if (!scroller) return;

    if (currentAbortController) currentAbortController.abort();
    requestEpoch++;
    currentOffset = 0;
    moreCount = 0;
    catalogBusy = false;
    searchTerm = "";
    seenWorkIds.clear();

    const followedBooks = getFollowedBooksList();
    const heading = scroller.querySelector(".section-head .muted");
    if (heading) heading.textContent = `FOLLOWED BOOKS (${followedBooks.length})`;

    document.querySelectorAll(".rabbit-top-nav-item").forEach(btn => {
      btn.classList.toggle("active", btn.getAttribute("onclick")?.includes("'following'"));
    });

    scroller.querySelectorAll(".rabbit-expanded-post").forEach(el => el.remove());
    const firstSec = scroller.querySelector(".home-first");
    if (firstSec) {
      const stories = firstSec.querySelector(".stories");
      if (stories) stories.replaceChildren();
    }

    if (followedBooks.length === 0) {
      const slot = document.getElementById("rabbit-first-book-slot");
      if (slot) {
        slot.replaceChildren();
        const emptyCard = document.createElement("div");
        emptyCard.className = "feedpost rabbit-expanded-post";
        emptyCard.style.cssText = "padding:48px 24px;text-align:center;background:rgba(20,20,24,0.7);border-radius:18px;border:1px solid rgba(255,255,255,0.08);margin-top:20px;";
        emptyCard.innerHTML = `
          <div style="font-size:36px;margin-bottom:14px;">♥</div>
          <h2 style="font-size:20px;color:#f3f4f6;margin-bottom:8px;">No Followed Books Yet</h2>
          <p style="font-size:14px;color:#9ca3af;line-height:1.6;max-width:380px;margin:0 auto 20px;">
            Tap <strong style="color:#f43f5e;">♡ Follow book</strong> on any insight card to track authors and future community discussions.
          </p>
          <button type="button" class="primary" style="padding:10px 20px;border-radius:24px;cursor:pointer;font-weight:600;" onclick="window.resetToSingleGenre()">
            ✦ Explore Masterworks Feed
          </button>
        `;
        slot.append(emptyCard);
      }
    } else {
      renderFirstBookSlot(followedBooks[0], "FOLLOWED BOOKS");
      seenWorkIds.add(followedBooks[0].id || followedBooks[0].title);
      if (followedBooks.length > 1) {
        const rest = followedBooks.slice(1);
        rest.forEach(b => seenWorkIds.add(b.id || b.title));
        addRealBookCards(rest);
      }
    }
  };

  window.renderFirstBookSlot = renderFirstBookSlot;

  function switchGenre(targetGenre) {
    switchSingleGenre(targetGenre, true);
  }

  function switchSingleGenre(targetGenre, updateHistory = true) {
    const prevGenre = window.rabbitSelectedGenre || "None";
    const prevStored = (function(){ try { return localStorage.getItem("rabbit_selected_genre") || "None"; } catch(e){ return "None"; } })();
    let resolved = resolveGenreKey(targetGenre);
    let fallbackTriggered = false;
    let fallbackReason = "none";

    if (!resolved) {
      fallbackTriggered = true;
      fallbackReason = `Invalid or unmapped genre "${targetGenre}". Preserving current active genre "${prevGenre}".`;
      console.warn(`[RABBIT WARN] ${fallbackReason}`);
      resolved = prevGenre !== "None" ? prevGenre : "Self Discovery";
    }

    window.rabbitMixMode = false;
    window.rabbitSelectedGenres = new Set([resolved]);
    window.rabbitSelectedGenre = resolved;
    try {
      localStorage.setItem("rabbit_selected_genre", resolved);
      localStorage.setItem("rabbit_selected_genres", JSON.stringify([resolved]));
      if (updateHistory) {
        const url = new URL(window.location);
        url.searchParams.set("genre", resolved);
        history.pushState({ genre: resolved }, "", url.toString());
      }
    } catch (e) {}

    renderFeedForCurrentSelection({
      event: "switchSingleGenre",
      targetGenre,
      resolved,
      prevGenre,
      prevStored,
      fallbackTriggered,
      fallbackReason
    });
  }

  function toggleGenre(targetGenre) {
    const prevGenre = window.rabbitSelectedGenre || "None";
    const prevStored = (function(){ try { return localStorage.getItem("rabbit_selected_genre") || "None"; } catch(e){ return "None"; } })();
    const resolved = resolveGenreKey(targetGenre);
    if (!resolved) return;

    window.rabbitSelectedGenres = window.rabbitSelectedGenres || new Set();
    if (window.rabbitSelectedGenres.has(resolved)) {
      if (window.rabbitSelectedGenres.size > 1) {
        window.rabbitSelectedGenres.delete(resolved);
      }
    } else {
      window.rabbitSelectedGenres.add(resolved);
    }

    if (window.rabbitSelectedGenres.size > 1) {
      window.rabbitMixMode = true;
    } else {
      window.rabbitMixMode = false;
    }

    const selectedList = Array.from(window.rabbitSelectedGenres);
    const first = selectedList[0] || resolved;
    window.rabbitSelectedGenre = first;
    try {
      localStorage.setItem("rabbit_selected_genre", first);
      localStorage.setItem("rabbit_selected_genres", JSON.stringify(selectedList));
      const url = new URL(window.location);
      url.searchParams.set("genre", selectedList.join(","));
      history.replaceState({ genre: selectedList }, "", url.toString());
    } catch (e) {}

    renderFeedForCurrentSelection({
      event: "toggleGenre",
      targetGenre,
      resolved,
      prevGenre,
      prevStored,
      fallbackTriggered: false,
      fallbackReason: "none"
    });
  }

  function resetToSingleGenre(optionalTarget) {
    window.rabbitMixMode = false;
    const currentActive = window.rabbitSelectedGenre || (window.rabbitSelectedGenres ? Array.from(window.rabbitSelectedGenres)[0] : "");
    const target = optionalTarget || currentActive || "Self Discovery";
    switchSingleGenre(target, true);
  }

  function renderFeedForCurrentSelection(diagnosticInfo = null) {
    const scroller = document.getElementById("homeScroll");
    if (!scroller) return;

    // 1. Cancel in-flight network requests
    if (currentAbortController) {
      currentAbortController.abort();
      currentAbortController = null;
    }
    requestEpoch++;
    const thisEpoch = requestEpoch;
    currentOffset = 0;
    moreCount = 0;
    catalogBusy = false;
    searchTerm = "";
    seenWorkIds.clear();

    const isWildBurrow = localStorage.getItem("rabbit_wild_burrow_active") === "true";
    const selectedArr = isWildBurrow
      ? AUTHORITATIVE_GENRES.slice()
      : Array.from(window.rabbitSelectedGenres || [getActiveGenre()]);
    const isMixed = isWildBurrow || selectedArr.length > 1;

    // 2. Update heading
    const heading = scroller.querySelector(".section-head .muted");
    const headingText = isWildBurrow
      ? "THE WILD BURROW · ALL 21 GENRES"
      : (isMixed ? selectedArr.join(" + ").toUpperCase() + " (MIXED FEED)" : selectedArr[0].toUpperCase());
    if (heading) heading.textContent = headingText;

    // 3. Re-render genre bar
    const barContainer = scroller.querySelector(".home-first .section");
    if (barContainer) {
      renderGenreBar(barContainer);
    }

    // 4. Clear ALL old expanded cards AND any residual feedposts from index.html
    scroller.querySelectorAll(".feedpost, .rabbit-expanded-post").forEach(el => el.remove());

    // 5. Clear story rail
    const first = scroller.querySelector(".home-first");
    if (first) {
      const stories = first.querySelector(".stories");
      if (stories) {
        stories.replaceChildren();
        stories.dataset.catalog = "loaded";
      }
    }

    // 6. Start Smart Rabbit Loader
    window.RabbitSmartLoader.start(isMixed ? "Mixed Genres" : selectedArr[0], () => renderFeedForCurrentSelection());

    // 7. Get books (Curated 1,050 landmark catalog)
    const booksToRender = isMixed
      ? getBlendedMixedBooks(selectedArr)
      : getInstantBooks(selectedArr[0]);

    if (booksToRender && booksToRender.length > 0) {
      renderFirstBookSlot(booksToRender[0], isMixed ? headingText : selectedArr[0]);
      seenWorkIds.add(booksToRender[0].id || booksToRender[0].title);

      if (booksToRender.length > 1) {
        const rest = booksToRender.slice(1);
        rest.forEach(b => seenWorkIds.add(b.id || b.title));
        addRealBookCards(rest);
      }
      window.RabbitSmartLoader.done();
    } else {
      window.RabbitSmartLoader.done();
    }

    // Structured Diagnostic Logging (Fulfilling Section 3 User Specification)
    try {
      const storedAfter = localStorage.getItem("rabbit_selected_genre");
      console.log("%c[RABBIT GENRE DISCOVERY EVENT]%c", "background:#9333ea;color:#fff;font-weight:bold;padding:2px 8px;border-radius:4px;", "", {
        genreSelectedByUser: diagnosticInfo?.targetGenre || selectedArr.join(" + "),
        selectedGenreId: selectedArr[0].toLowerCase().replace(/[^a-z0-9]/g, "_"),
        previousActiveGenre: diagnosticInfo?.prevGenre || "N/A",
        urlRoute: window.location.href,
        storedPreferencesBefore: diagnosticInfo?.prevStored || "N/A",
        storedPreferencesAfter: storedAfter,
        resolvedGenreUsedForFetching: isMixed ? selectedArr : selectedArr[0],
        fallbackTriggered: diagnosticInfo?.fallbackTriggered ? `YES: ${diagnosticInfo.fallbackReason}` : "NO",
        booksReturnedCount: booksToRender ? booksToRender.length : 0,
        feedRenderedToUser: headingText
      });
    } catch (e) {}

    // 8. If single genre, progressive background fetch for serendipity
    if (!isMixed) {
      loadBackgroundBooks(selectedArr[0], thisEpoch);
    }
  }

  // Intercept renderHome to add search, genre bar, and trigger instant discovery
  const originalHome = window.renderHome;
  if (typeof originalHome === "function") {
    window.renderHome = function() {
      originalHome();

      const chosen = getActiveGenre();
      const s = document.getElementById("homeScroll");
      if (!s) return;

      const first = s.querySelector(".home-first .section");
      if (first) {
        // Search bar removed as requested
        // 2. Add Horizontal Genre Bar
        renderGenreBar(first);
      }

      // Instantly render real book insights for the active genre or mixed genres!
      renderFeedForCurrentSelection();
    };
  }

  // Infinite Scroll Listener
  document.addEventListener("scroll", () => {
    const scroller = document.getElementById("homeScroll");
    if (!scroller || catalogBusy) return;
    if (scroller.scrollTop + scroller.clientHeight >= scroller.scrollHeight - 1400) {
      loadBackgroundBooks(getActiveGenre(), requestEpoch);
    }
  }, true);

  // If home is already mounted (e.g. initial load or reload when entered=true),
  // immediately mount the search bar, genre navigation bar, and book feed!
  if (document.getElementById("homeScroll") && typeof window.renderHome === "function") {
    window.renderHome();
  }

})();
