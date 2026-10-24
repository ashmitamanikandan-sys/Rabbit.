/* RABBIT Dynamic Feed & 20-Genre Discovery Extension
 * Integrates:
 * 1. Curated Masterworks (all 20 genres)
 * 2. Infinite Open Library discovery (thousands and thousands of books)
 * 3. 8-10 line curiosity feed previews with genuine takeaways
 * 4. 4-part interactive Reader overlay for every book
 * 5. Horizontal 20-Genre Navigation Bar in the feed
 * 6. Full Search across millions of books
 */
(function() {
  "use strict";

  const AUTHORITATIVE_GENRES = [
    "The Human Mind",
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

  let catalogBusy = false;
  let moreCount = 0;
  let searchTerm = "";
  let requestEpoch = 0;
  let offset = 0;
  let finished = false;
  const seenWorkIds = new Set();
  const workDescriptionCache = new Map();

  function getActiveGenre() {
    return window.rabbitSelectedGenre || "The Human Mind";
  }

  // Render book cards into the feed
  function addRealBookCards(rows) {
    const scroller = document.getElementById("homeScroll");
    if (!scroller) return;

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

      // Queue lazy background enrichment from Open Library works API if description is short
      if (!enriched.isCurated && String(book.id || "").startsWith("/works/")) {
        queueWorkEnrichment(book, info, headline);
      }

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

  // Background work description enrichment
  function queueWorkEnrichment(book, infoElement, headlineElement) {
    const id = String(book.id || "");
    if (!id.startsWith("/works/")) return;

    if (workDescriptionCache.has(id)) {
      applyCachedDescription(book, workDescriptionCache.get(id), infoElement, headlineElement);
      return;
    }

    fetch("https://openlibrary.org" + id + ".json")
      .then(res => res.ok ? res.json() : null)
      .then(work => {
        if (!work) return;
        const d = typeof work.description === "string" ? work.description : work.description?.value;
        if (typeof d === "string" && d.trim().length > 50) {
          workDescriptionCache.set(id, d.trim());
          applyCachedDescription(book, d.trim(), infoElement, headlineElement);
        }
      })
      .catch(() => {});
  }

  function applyCachedDescription(book, desc, infoElement, headlineElement) {
    book.description = desc;
    if (window.RABBIT_ENRICH && infoElement.isConnected) {
      const enriched = window.RABBIT_ENRICH.getEnrichedBook(book, getActiveGenre());
      book.__rabbitSections = enriched.sections;
      infoElement.textContent = enriched.preview;
      if (headlineElement && headlineElement.isConnected) {
        headlineElement.textContent = enriched.hook;
      }
    }
  }

  // Interactive Reader Overlay for ANY book
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

  // Load more books from Open Library or Curated Catalog
  async function loadMore() {
    if (catalogBusy || finished || !document.getElementById("homeScroll")) return;
    catalogBusy = true;
    const epoch = requestEpoch;

    try {
      const activeGenre = getActiveGenre();
      let rows = [];

      // 1. If at offset 0, first check if we have curated books for this genre
      if (offset === 0 && !searchTerm) {
        const catalog = window.RABBIT_CURATED_CATALOG || {};
        const curatedList = catalog[activeGenre.toLowerCase()] || [];
        curatedList.forEach(b => {
          if (!seenWorkIds.has(b.id || b.title)) {
            seenWorkIds.add(b.id || b.title);
            rows.push(b);
          }
        });
      }

      // 2. Fetch books from Open Library to scale to thousands and thousands of titles
      const subject = GENRE_SUBJECTS[activeGenre] || "fiction";
      const params = new URLSearchParams({
        limit: "50",
        offset: String(offset),
        fields: "key,title,author_name,cover_i,language,first_sentence,first_publish_year"
      });

      if (searchTerm) {
        params.set("q", searchTerm);
      } else {
        params.set("subject", subject);
      }

      const res = await fetch("https://openlibrary.org/search.json?" + params.toString());
      if (res.ok) {
        const data = await res.json();
        const olBooks = (data.docs || [])
          .filter(b => b.key && b.title && b.author_name?.length && (!b.language || b.language.includes("eng")))
          .map(b => ({
            id: b.key,
            title: b.title,
            author: b.author_name[0],
            cover_url: b.cover_i ? "https://covers.openlibrary.org/b/id/" + b.cover_i + "-M.jpg" : "",
            description: (Array.isArray(b.first_sentence) ? b.first_sentence[0] : b.first_sentence) || ""
          }));

        olBooks.forEach(b => {
          if (!seenWorkIds.has(b.id)) {
            seenWorkIds.add(b.id);
            rows.push(b);
          }
        });
      }

      if (epoch !== requestEpoch) return;

      offset += 50;
      if (!rows.length && offset >= 100) finished = true;

      addRealBookCards(rows);

      if (!rows.length && moreCount === 0) {
        const rail = document.querySelector("#homeScroll .home-first .stories");
        if (rail) rail.textContent = "No books found. Try another genre or search.";
      }
    } catch (err) {
      console.warn("RABBIT feed error:", err);
    } finally {
      catalogBusy = false;
      if (epoch !== requestEpoch && document.getElementById("homeScroll")) {
        loadMore();
      }
    }
  }

  // Build the sleek 20-Genre Navigation Bar in the feed
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

      btn.onclick = () => {
        if (getActiveGenre() === g) return;
        switchGenre(g);
      };
      bar.append(btn);
    });

    container.append(bar);
  }

  // Switch genres cleanly and instantly
  function switchGenre(newGenre) {
    window.rabbitSelectedGenre = newGenre;
    try {
      localStorage.setItem("rabbit_selected_genre", newGenre);
    } catch (e) {}

    const scroller = document.getElementById("homeScroll");
    if (!scroller) return;

    // Reset pagination and tracking
    requestEpoch++;
    offset = 0;
    moreCount = 0;
    finished = false;
    searchTerm = "";
    seenWorkIds.clear();

    // Update heading and feature block
    const heading = scroller.querySelector(".section-head .muted");
    if (heading) heading.textContent = newGenre.toUpperCase();

    // Remove old dynamic cards
    scroller.querySelectorAll(".rabbit-expanded-post").forEach(el => el.remove());

    const first = scroller.querySelector(".home-first");
    if (first) {
      const feature = first.querySelector(".feature");
      if (feature) {
        feature.innerHTML = `
          <div class="eyebrow">YOUR RABBIT HOLE · ${newGenre.replace(/</g, "&lt;")}</div>
          <h2 style="font:600 27px/1.2 var(--reading-font);margin:16px 0">Follow your curiosity into ${newGenre.replace(/</g, "&lt;")}.</h2>
          <p class="muted">Bite-sized ideas, 8–10 line curious previews, and deep chapter insights from thousands of books.</p>
        `;
      }

      // Update stories rail
      const stories = first.querySelector(".stories");
      if (stories) {
        stories.replaceChildren();
        stories.dataset.catalog = "loaded";
        const loading = document.createElement("span");
        loading.className = "muted";
        loading.style.cssText = "font-size:12px;min-width:180px;padding:20px 0";
        loading.textContent = "Finding book stories…";
        stories.append(loading);
      }
    }

    // Refresh active genre button highlight
    const bar = scroller.querySelector(".rabbit-genre-nav-bar");
    if (bar) {
      bar.querySelectorAll(".chip").forEach(c => {
        c.classList.toggle("active", c.textContent === newGenre);
      });
    }

    // Load initial batch
    loadMore();
  }

  // Intercept renderHome to add search, genre bar, and trigger discovery
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
            requestEpoch++;
            offset = 0;
            moreCount = 0;
            finished = false;
            seenWorkIds.clear();
            s.querySelectorAll(".rabbit-expanded-post").forEach(el => el.remove());
            const rail = s.querySelector(".home-first .stories");
            if (rail) {
              rail.replaceChildren();
              rail.dataset.catalog = "loaded";
              const message = document.createElement("span");
              message.className = "muted";
              message.textContent = "Searching the library for '" + value + "'…";
              rail.append(message);
            }
            loadMore();
          };
          first.prepend(search);
        }

        // 2. Add Horizontal 20-Genre Bar
        renderGenreBar(first);
      }

      // If user selected non-Human Mind genre, customize the feature card & clear Human Mind cards
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
              <div class="eyebrow">YOUR RABBIT HOLE · ${chosen.replace(/</g, "&lt;")}</div>
              <h2 style="font:600 27px/1.2 var(--reading-font);margin:16px 0">Follow your curiosity into ${chosen.replace(/</g, "&lt;")}.</h2>
              <p class="muted">Curated masterworks and real-time discoveries across thousands of titles. Swipe down to discover.</p>
            `;
          }
          const stories = firstSec.querySelector(".stories");
          if (stories) {
            stories.replaceChildren();
            stories.dataset.catalog = "loaded";
            const loading = document.createElement("span");
            loading.className = "muted";
            loading.style.cssText = "font-size:12px;min-width:180px;padding:20px 0";
            loading.textContent = "Finding book stories…";
            stories.append(loading);
          }
        }
      }

      // Reset request variables and start loading
      requestEpoch++;
      offset = 0;
      moreCount = 0;
      finished = false;
      seenWorkIds.clear();

      loadMore();
    };
  }

  // Infinite Scroll Listener
  document.addEventListener("scroll", () => {
    const scroller = document.getElementById("homeScroll");
    if (!scroller) return;
    if (scroller.scrollTop + scroller.clientHeight >= scroller.scrollHeight - 1400) {
      loadMore();
    }
  }, true);

})();
