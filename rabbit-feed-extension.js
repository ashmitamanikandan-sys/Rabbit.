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
  function resolveGenreKey(genreName) {
    if (!genreName) return "The Human Mind";
    const g = String(genreName).trim();
    const lower = g.toLowerCase();

    if (lower.includes("self discovery") || lower.includes("self-discovery")) return "Self Discovery";
    if (lower.includes("self-help") || lower.includes("self help") || lower.includes("productivity")) return "Self-Help";
    if (lower.includes("mind") || lower.includes("psychology") || lower.includes("neuroscience") || lower.includes("behavior")) return "The Human Mind";
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

    return g;
  }

  function getActiveGenre() {
    return resolveGenreKey(window.rabbitSelectedGenre || "The Human Mind");
  }

  // Retrieve instant books (curated masterworks + localStorage cache)
  function getInstantBooks(genreName) {
    const list = [];
    const key = genreName.toLowerCase();

    // 1. Curated masterworks from static catalog
    const catalog = window.RABBIT_CURATED_CATALOG || {};
    const curated = catalog[key] || catalog[key.replace(/\s+/g, "-")] || [];
    curated.forEach(b => {
      list.push(Object.assign({}, b, { isCurated: true }));
    });

    // 2. Cached books from previous sessions
    try {
      const cacheStr = localStorage.getItem("rabbit_cache_" + genreName);
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
      meta.textContent = (enriched.isCurated ? "ORIGINAL RABBIT MASTERWORK" : "RABBIT BOOK DISCOVERY") +
        " · HOP " + String(++moreCount).padStart(2, "0") + " / " + getActiveGenre().toUpperCase();
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
      save.textContent = localStorage.getItem(sk) ? "◆ Saved" : "◇ Save";
      save.onclick = () => {
        if (localStorage.getItem(sk)) localStorage.removeItem(sk);
        else localStorage.setItem(sk, "1");
        save.textContent = localStorage.getItem(sk) ? "◆ Saved" : "◇ Save";
      };
      actions.append(save);

      const follow = document.createElement("button");
      const fk = "rabbit_follow_" + (book.id || book.title);
      follow.textContent = localStorage.getItem(fk) ? "♥ Following" : "♡ Follow book";
      follow.onclick = () => {
        if (localStorage.getItem(fk)) localStorage.removeItem(fk);
        else localStorage.setItem(fk, "1");
        follow.textContent = localStorage.getItem(fk) ? "♥ Following" : "♡ Follow book";
      };
      actions.append(follow);

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

    const sections = book.__rabbitSections || (window.RABBIT_ENRICH ? window.RABBIT_ENRICH.getEnrichedBook(book, getActiveGenre()).sections : []);

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
        addRealBookCards(toRender);
        saveToLocalCache(targetGenre, toRender);
      }
    } catch (err) {
      // Graceful handling of network timeout, rate-limit, or abort:
      // The user ALREADY has instant books rendered. Never crash or freeze!
      console.warn("Background fetch completed or timed out for:", targetGenre);
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
    bar.style.cssText = "display:flex;overflow-x:auto;white-space:nowrap;gap:8px;padding:12px 0 16px;scrollbar-width:none;-webkit-overflow-scrolling:touch;";

    AUTHORITATIVE_GENRES.forEach(g => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "chip" + (getActiveGenre() === g ? " active" : "");
      btn.style.cssText = "flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 14px;border-radius:20px;transition:all 0.2s ease;";
      btn.textContent = g;
      btn.dataset.genre = g;

      btn.onclick = () => {
        if (getActiveGenre() === g) return;
        switchGenre(g);
      };
      bar.append(btn);
    });

    container.append(bar);
  }

  // Instant zero-latency switch between genres
  function switchGenre(targetGenre) {
    const resolved = resolveGenreKey(targetGenre);
    window.rabbitSelectedGenre = resolved;
    try {
      localStorage.setItem("rabbit_selected_genre", resolved);
    } catch (e) {}

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

    const scroller = document.getElementById("homeScroll");
    if (!scroller) return;

    // 2. Update heading
    const heading = scroller.querySelector(".section-head .muted");
    if (heading) heading.textContent = resolved.toUpperCase();

    // 3. Update active pill highlight
    const bar = scroller.querySelector(".rabbit-genre-nav-bar");
    if (bar) {
      bar.querySelectorAll(".chip").forEach(c => {
        c.classList.toggle("active", c.dataset.genre === resolved || c.textContent === resolved);
      });
    }

    // 4. Clear old expanded cards
    scroller.querySelectorAll(".rabbit-expanded-post").forEach(el => el.remove());

    // 5. Update feature box and clear story rail
    const first = scroller.querySelector(".home-first");
    if (first) {
      const feature = first.querySelector(".feature");
      if (feature) {
        feature.innerHTML = `
          <div class="eyebrow">YOUR RABBIT HOLE · ${escapeHtml(resolved)}</div>
          <h2 style="font:600 27px/1.2 var(--reading-font);margin:16px 0">Follow your curiosity into ${escapeHtml(resolved)}.</h2>
          <p class="muted">Instant ideas, 8–10 line curious previews, and deep chapter insights. Swipe down to discover.</p>
        `;
      }
      const stories = first.querySelector(".stories");
      if (stories) {
        stories.replaceChildren();
        stories.dataset.catalog = "loaded";
      }
    }

    // 6. ZERO-LATENCY INSTANT FIRST RENDER: Show instant books immediately! (0ms)
    const instantBooks = getInstantBooks(resolved);
    if (instantBooks && instantBooks.length > 0) {
      instantBooks.forEach(b => seenWorkIds.add(b.id || b.title));
      addRealBookCards(instantBooks);
    } else {
      // If no instant books, show clean placeholder
      const stories = first?.querySelector(".stories");
      if (stories && !stories.children.length) {
        const loading = document.createElement("span");
        loading.className = "muted";
        loading.style.cssText = "font-size:12px;padding:20px 0";
        loading.textContent = "Connecting to library…";
        stories.append(loading);
      }
    }

    // 7. Non-blocking progressive background fetch
    loadBackgroundBooks(resolved, thisEpoch);
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
        // 1. Add Search Form
        if (!first.querySelector(".rabbit-library-search")) {
          const search = document.createElement("form");
          search.className = "rabbit-library-search";
          search.style.marginBottom = "8px";

          const input = document.createElement("input");
          input.type = "search";
          input.placeholder = "Search millions of books, authors, ideas…";
          input.setAttribute("aria-label", "Search books");
          input.autocomplete = "off";

          const go = document.createElement("button");
          go.type = "submit";
          go.textContent = "Search ↗";

          search.append(input, go);
          search.onsubmit = e => {
            e.preventDefault();
            const value = input.value.trim();
            if (!value) {
              input.focus();
              return;
            }
            searchTerm = value;
            if (currentAbortController) currentAbortController.abort();
            requestEpoch++;
            const searchEpoch = requestEpoch;
            currentOffset = 0;
            moreCount = 0;
            catalogBusy = false;
            seenWorkIds.clear();
            s.querySelectorAll(".rabbit-expanded-post").forEach(el => el.remove());
            const rail = s.querySelector(".home-first .stories");
            if (rail) {
              rail.replaceChildren();
              rail.dataset.catalog = "loaded";
            }
            loadBackgroundBooks(chosen, searchEpoch);
          };
          first.prepend(search);
        }

        // 2. Add Horizontal Genre Bar
        renderGenreBar(first);
      }

      // If user selected non-Human Mind genre, customize feature card and show instant books
      if (chosen !== "The Human Mind") {
        const heading = s.querySelector(".section-head .muted");
        if (heading) heading.textContent = chosen.toUpperCase();

        const oldPosts = s.querySelectorAll(".feedpost:not(.rabbit-expanded-post)");
        oldPosts.forEach(p => p.remove());

        const firstSec = s.querySelector(".home-first");
        if (firstSec) {
          const feature = firstSec.querySelector(".feature");
          if (feature) {
            feature.innerHTML = `
              <div class="eyebrow">YOUR RABBIT HOLE · ${escapeHtml(chosen)}</div>
              <h2 style="font:600 27px/1.2 var(--reading-font);margin:16px 0">Follow your curiosity into ${escapeHtml(chosen)}.</h2>
              <p class="muted">Instant ideas, 8–10 line curious previews, and deep chapter insights. Swipe down to discover.</p>
            `;
          }
          const stories = firstSec.querySelector(".stories");
          if (stories) {
            stories.replaceChildren();
            stories.dataset.catalog = "loaded";
          }
        }

        // Render instant books immediately
        requestEpoch++;
        const thisEpoch = requestEpoch;
        currentOffset = 0;
        moreCount = 0;
        catalogBusy = false;
        seenWorkIds.clear();

        const instantBooks = getInstantBooks(chosen);
        if (instantBooks && instantBooks.length > 0) {
          instantBooks.forEach(b => seenWorkIds.add(b.id || b.title));
          addRealBookCards(instantBooks);
        }

        loadBackgroundBooks(chosen, thisEpoch);
      } else {
        // If Human Mind, background fetch additional titles progressively
        requestEpoch++;
        loadBackgroundBooks("The Human Mind", requestEpoch);
      }
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

})();
