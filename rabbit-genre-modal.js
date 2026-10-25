/**
 * RABBIT Authoritative Full-Screen Genre Selection (Part 3)
 * Supports unlimited genre selection, "The Wild Burrow" all-genres mode,
 * single primary CTA "Enter the Rabbit Hole", and full persistence.
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

  const GENRE_EMOJIS = {
    "The Human Mind": "\u{1F9E0}",
    "Self Discovery": "\u{2728}",
    "Science Fiction": "\u{1F680}",
    "Fantasy": "\u{2694}\u{FE0F}",
    "Mystery & Thriller": "\u{1F50D}",
    "Romance": "\u{2764}\u{FE0F}",
    "Horror": "\u{1F56F}\u{FE0F}",
    "Historical Fiction": "\u{1F3DB}\u{FE0F}",
    "Young Adult": "\u{26A1}",
    "Classics": "\u{1F4DC}",
    "Adventure": "\u{1F5FA}\u{FE0F}",
    "Literary Fiction": "\u{1F4D6}",
    "Philosophy": "\u{1F30C}",
    "Self-Help": "\u{1F331}",
    "Business & Money": "\u{1F4C8}",
    "Science": "\u{1F52C}",
    "History": "\u{23F3}",
    "Biography & Memoir": "\u{1FAB6}",
    "Politics & Society": "\u{1F310}",
    "True Crime": "\u{1F5DD}\u{FE0F}",
    "Poetry": "\u{1FAB7}"
  };

  let modalEl = null;
  let tempSelectedGenres = new Set();
  let isWildBurrowSelected = false;
  let isFromNavigation = false;

  function getStoredGenres() {
    try {
      const stored = localStorage.getItem("rabbit_selected_genres");
      if (stored) {
        const arr = JSON.parse(stored);
        if (Array.isArray(arr) && arr.length) return new Set(arr);
      }
      const single = localStorage.getItem("rabbit_selected_genre");
      if (single) return new Set([single]);
    } catch (e) {}
    return new Set(["The Human Mind", "Philosophy"]);
  }

  function getStoredWildBurrow() {
    return localStorage.getItem("rabbit_wild_burrow_active") === "true";
  }

  function ensureStyles() {
    if (document.getElementById("rabbit-genre-modal-style")) return;
    const style = document.createElement("style");
    style.id = "rabbit-genre-modal-style";
    style.textContent = `
      #rabbit-genre-modal {
        position: fixed;
        inset: 0;
        z-index: 9999;
        background: #050505;
        background-image: radial-gradient(ellipse at 50% 10%, rgba(139, 92, 246, 0.14) 0%, rgba(5, 5, 5, 0.98) 70%);
        overflow-y: auto;
        overscroll-behavior: contain;
        display: none;
        flex-direction: column;
        align-items: center;
        padding: 40px 20px 140px;
        color: #F5F2F8;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        box-sizing: border-box;
      }
      #rabbit-genre-modal.active {
        display: flex;
      }

      .rabbit-genre-shell {
        width: 100%;
        max-width: 640px;
        display: flex;
        flex-direction: column;
      }

      .rabbit-genre-top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 24px;
      }
      .rabbit-genre-brand {
        font-weight: 800;
        font-size: 21px;
        letter-spacing: -0.04em;
        display: flex;
        align-items: baseline;
      }
      .rabbit-genre-brand .accent {
        color: #A78BFA;
      }
      .rabbit-genre-cancel-btn {
        background: transparent;
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #A9A3B2;
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 13px;
        cursor: pointer;
        transition: all 0.2s ease;
      }
      .rabbit-genre-cancel-btn:hover {
        background: rgba(255, 255, 255, 0.08);
        color: #fff;
      }

      .rabbit-genre-header {
        margin-bottom: 28px;
      }
      .rabbit-genre-eyebrow {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #A78BFA;
        margin-bottom: 8px;
      }
      .rabbit-genre-title {
        font-family: "Iowan Old Style", "Baskerville", Georgia, serif;
        font-size: clamp(32px, 6vw, 44px);
        font-weight: 600;
        line-height: 1.12;
        letter-spacing: -0.03em;
        margin: 0 0 10px;
      }
      .rabbit-genre-desc {
        color: #A9A3B2;
        font-size: 15px;
        line-height: 1.6;
        margin: 0;
      }

      /* Special THE WILD BURROW Card */
      .rabbit-wild-burrow-card {
        background: linear-gradient(135deg, rgba(35, 26, 48, 0.85) 0%, rgba(18, 17, 24, 0.95) 100%);
        border: 1.5px solid rgba(167, 139, 250, 0.35);
        border-radius: 18px;
        padding: 18px 20px;
        margin-bottom: 22px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 16px;
        transition: all 0.22s cubic-bezier(0.2, 0.8, 0.2, 1);
        box-shadow: 0 8px 28px rgba(0, 0, 0, 0.45);
        position: relative;
        overflow: hidden;
      }
      .rabbit-wild-burrow-card::before {
        content: "";
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 10% 20%, rgba(167, 139, 250, 0.12), transparent 70%);
        pointer-events: none;
      }
      .rabbit-wild-burrow-card:hover {
        border-color: #A78BFA;
        transform: translateY(-2px);
        box-shadow: 0 12px 34px rgba(139, 92, 246, 0.2);
      }
      .rabbit-wild-burrow-card.active {
        border-color: #A78BFA;
        background: linear-gradient(135deg, rgba(82, 53, 122, 0.7) 0%, rgba(30, 24, 43, 0.95) 100%);
        box-shadow: 0 0 0 2px rgba(167, 139, 250, 0.4), 0 12px 32px rgba(139, 92, 246, 0.28);
      }
      .rabbit-wild-burrow-icon {
        font-size: 28px;
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: rgba(167, 139, 250, 0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border: 1px solid rgba(167, 139, 250, 0.3);
      }
      .rabbit-wild-burrow-info h3 {
        margin: 0 0 4px;
        font-size: 17px;
        font-weight: 700;
        letter-spacing: -0.01em;
        color: #F5F2F8;
      }
      .rabbit-wild-burrow-info p {
        margin: 0;
        font-size: 13px;
        color: #C4B5FD;
        font-style: italic;
      }
      .rabbit-wild-burrow-check {
        margin-left: auto;
        font-size: 18px;
        color: #A78BFA;
        font-weight: 800;
      }

      /* Genre Cards Grid */
      .rabbit-genre-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(135px, 1fr));
        gap: 11px;
        margin-bottom: 30px;
      }
      .rabbit-genre-card {
        background: #121116;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 15px;
        padding: 14px 12px;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
        user-select: none;
        position: relative;
      }
      .rabbit-genre-card:hover {
        background: #181622;
        border-color: rgba(167, 139, 250, 0.35);
        transform: translateY(-2px);
      }
      .rabbit-genre-card.active {
        background: linear-gradient(145deg, rgba(46, 33, 67, 0.95), rgba(24, 19, 35, 0.95));
        border-color: #A78BFA;
        box-shadow: 0 0 0 1px #A78BFA, 0 6px 20px rgba(139, 92, 246, 0.24);
      }
      .rabbit-genre-card-emoji {
        font-size: 20px;
        margin-bottom: 8px;
      }
      .rabbit-genre-card-name {
        font-size: 13px;
        font-weight: 600;
        color: #F5F2F8;
        line-height: 1.25;
      }
      .rabbit-genre-card.active .rabbit-genre-card-name {
        color: #E9D5FF;
      }
      .rabbit-genre-card-check {
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 11px;
        color: #A78BFA;
        font-weight: 800;
        opacity: 0;
        transition: opacity 0.15s ease;
      }
      .rabbit-genre-card.active .rabbit-genre-card-check {
        opacity: 1;
      }

      /* Sticky Bottom Action CTA */
      .rabbit-genre-bottom-cta {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, #050505 70%, rgba(5, 5, 5, 0));
        padding: 24px 20px calc(24px + env(safe-area-inset-bottom));
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 10000;
      }
      .rabbit-genre-enter-btn {
        width: 100%;
        max-width: 480px;
        background: linear-gradient(135deg, #D8C5FF 0%, #A78BFA 48%, #8B5CF6 100%);
        color: #0B0712;
        font-size: 16px;
        font-weight: 800;
        padding: 16px 28px;
        border-radius: 999px;
        border: none;
        cursor: pointer;
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.5);
        transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.2s ease;
      }
      .rabbit-genre-enter-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 38px rgba(139, 92, 246, 0.48);
      }
      .rabbit-genre-enter-btn:active {
        transform: scale(0.98);
      }
      .rabbit-genre-count-label {
        font-size: 12px;
        color: #A9A3B2;
        margin-top: 8px;
      }
    `;
    document.head.appendChild(style);
  }

  function renderModal() {
    ensureStyles();
    if (modalEl) return modalEl;

    modalEl = document.createElement("div");
    modalEl.id = "rabbit-genre-modal";
    modalEl.setAttribute("role", "dialog");
    modalEl.setAttribute("aria-label", "Select your reading genres");

    modalEl.innerHTML = `
      <div class="rabbit-genre-shell">
        <div class="rabbit-genre-top-bar">
          <div class="rabbit-genre-brand">
            RABBIT<span class="accent">.</span>
          </div>
          <button type="button" class="rabbit-genre-cancel-btn" id="rabbit-genre-cancel-btn" style="display:none">
            Cancel
          </button>
        </div>

        <div class="rabbit-genre-header">
          <div class="rabbit-genre-eyebrow">THE FIRST HOP · CURATED EXPEDITION</div>
          <h1 class="rabbit-genre-title">What pulls you in?</h1>
          <p class="rabbit-genre-desc">Pick your rabbit holes. Choose as many as you like—or explore them all together.</p>
        </div>

        <!-- THE WILD BURROW option -->
        <div class="rabbit-wild-burrow-card" id="rabbit-wild-burrow-card" role="checkbox" aria-checked="false" tabindex="0">
          <div class="rabbit-wild-burrow-icon">🐇</div>
          <div class="rabbit-wild-burrow-info">
            <h3>THE WILD BURROW</h3>
            <p>A little bit of everything. All genres, one feed.</p>
          </div>
          <div class="rabbit-wild-burrow-check" id="rabbit-wild-burrow-check">○</div>
        </div>

        <!-- 21 Genre Cards -->
        <div class="rabbit-genre-grid" id="rabbit-genre-grid"></div>
      </div>

      <div class="rabbit-genre-bottom-cta">
        <button type="button" class="rabbit-genre-enter-btn" id="rabbit-genre-enter-btn">
          Enter the Rabbit Hole →
        </button>
        <span class="rabbit-genre-count-label" id="rabbit-genre-count-label">Select at least one genre</span>
      </div>
    `;

    document.body.appendChild(modalEl);

    // Event listeners
    const cancelBtn = modalEl.querySelector("#rabbit-genre-cancel-btn");
    cancelBtn.onclick = () => window.RabbitGenreModal.close();

    const wildCard = modalEl.querySelector("#rabbit-wild-burrow-card");
    wildCard.onclick = () => toggleWildBurrow();

    const enterBtn = modalEl.querySelector("#rabbit-genre-enter-btn");
    enterBtn.onclick = () => confirmAndEnter();

    buildGenreCards();
    return modalEl;
  }

  function buildGenreCards() {
    const grid = modalEl.querySelector("#rabbit-genre-grid");
    if (!grid) return;
    grid.innerHTML = "";

    AUTHORITATIVE_GENRES.forEach(genre => {
      const card = document.createElement("div");
      card.className = "rabbit-genre-card";
      card.dataset.genre = genre;
      card.setAttribute("role", "checkbox");
      card.setAttribute("aria-checked", "false");
      card.tabIndex = 0;

      const emoji = GENRE_EMOJIS[genre] || "📖";
      card.innerHTML = `
        <span class="rabbit-genre-card-emoji">${emoji}</span>
        <span class="rabbit-genre-card-name">${genre}</span>
        <span class="rabbit-genre-card-check">✓</span>
      `;

      card.onclick = () => toggleGenre(genre, card);
      card.onkeydown = e => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          toggleGenre(genre, card);
        }
      };

      grid.appendChild(card);
    });
  }

  function updateVisuals() {
    const wildCard = modalEl.querySelector("#rabbit-wild-burrow-card");
    const wildCheck = modalEl.querySelector("#rabbit-wild-burrow-check");
    if (wildCard && wildCheck) {
      wildCard.classList.toggle("active", isWildBurrowSelected);
      wildCard.setAttribute("aria-checked", String(isWildBurrowSelected));
      wildCheck.textContent = isWildBurrowSelected ? "✓" : "○";
    }

    const cards = modalEl.querySelectorAll(".rabbit-genre-card");
    cards.forEach(c => {
      const g = c.dataset.genre;
      const isSelected = tempSelectedGenres.has(g);
      c.classList.toggle("active", isSelected);
      c.setAttribute("aria-checked", String(isSelected));
    });

    const countLabel = modalEl.querySelector("#rabbit-genre-count-label");
    const enterBtn = modalEl.querySelector("#rabbit-genre-enter-btn");

    if (isWildBurrowSelected) {
      if (countLabel) countLabel.textContent = "The Wild Burrow active · All 21 genres in one feed";
      if (enterBtn) {
        enterBtn.textContent = "Enter the Rabbit Hole \u2192";
        enterBtn.disabled = false;
      }
    } else {
      const count = tempSelectedGenres.size;
      if (countLabel) {
        if (count === 0) countLabel.textContent = "Pick at least one rabbit hole to continue";
        else if (count === 1) countLabel.textContent = "1 genre selected";
        else countLabel.textContent = `${count} genres selected (Mixed feed)`;
      }
      if (enterBtn) {
        enterBtn.textContent = count === 0 ? "Select a Genre" : "Enter the Rabbit Hole \u2192";
        enterBtn.disabled = (count === 0);
      }
    }
  }

  function toggleGenre(genre, cardEl) {
    // If Wild Burrow was active, deselect Wild Burrow so specific genres take over
    if (isWildBurrowSelected) {
      isWildBurrowSelected = false;
      tempSelectedGenres.clear();
    }

    if (tempSelectedGenres.has(genre)) {
      tempSelectedGenres.delete(genre);
    } else {
      tempSelectedGenres.add(genre);
    }
    updateVisuals();
  }

  function toggleWildBurrow() {
    isWildBurrowSelected = !isWildBurrowSelected;
    if (isWildBurrowSelected) {
      // Clear individual toggles visually so Wild Burrow represents all
      tempSelectedGenres.clear();
    } else {
      // Default back to first genre if deselected
      tempSelectedGenres.add(AUTHORITATIVE_GENRES[0]);
    }
    updateVisuals();
  }

  function confirmAndEnter() {
    if (!isWildBurrowSelected && tempSelectedGenres.size === 0) {
      if (typeof toast === "function") toast("Please choose at least one genre or The Wild Burrow");
      return;
    }

    // Persist selections
    try {
      localStorage.setItem("rabbit_wild_burrow_active", String(isWildBurrowSelected));
      if (isWildBurrowSelected) {
        localStorage.setItem("rabbit_selected_genres", JSON.stringify(AUTHORITATIVE_GENRES));
        localStorage.setItem("rabbit_selected_genre", "The Wild Burrow");
        window.rabbitWildBurrowActive = true;
        window.rabbitSelectedGenres = new Set(AUTHORITATIVE_GENRES);
        window.rabbitSelectedGenre = "The Wild Burrow";
      } else {
        const arr = Array.from(tempSelectedGenres);
        localStorage.setItem("rabbit_selected_genres", JSON.stringify(arr));
        localStorage.setItem("rabbit_selected_genre", arr[0]);
        window.rabbitWildBurrowActive = false;
        window.rabbitSelectedGenres = new Set(arr);
        window.rabbitSelectedGenre = arr[0];
      }
      localStorage.setItem("rabbit_onboarding_completed", "true");
    } catch (e) {}

    // Close modal
    window.RabbitGenreModal.close();

    // Trigger mandatory 2-second loading animation and render the updated feed
    if (window.RabbitLoader) {
      const line = isWildBurrowSelected
        ? "Curiosity looks good on you."
        : "Your next obsession is a page away.";
      window.RabbitLoader.show(line);
    }

    // Delay render to guarantee minimum 2-second animation
    setTimeout(() => {
      // 1. Ensure Home view is mounted in #app (creates #homeScroll & sets curiosity stage)
      if (window.RabbitUnifiedViews) {
        window.RabbitUnifiedViews.showHome();
      } else if (typeof renderHome === "function") {
        renderHome();
      }

      // 2. Ensure feed is populated for the current genre selection
      if (typeof window.applyGenreSelectionAndRefreshFeed === "function") {
        window.applyGenreSelectionAndRefreshFeed();
      }

      // 3. Update bottom navigation tab state to 'home'
      if (window.RabbitNavigation) {
        window.RabbitNavigation.setActiveTab("home");
      }

      // 4. Signal loader readiness (loader enforces full 2000ms minimum)
      if (window.RabbitLoader) {
        window.RabbitLoader.ready();
      }
    }, 400);
  }

  window.RabbitGenreModal = {
    open: function(options) {
      renderModal();
      isFromNavigation = !!(options && options.fromNav);

      const cancelBtn = modalEl.querySelector("#rabbit-genre-cancel-btn");
      if (cancelBtn) cancelBtn.style.display = isFromNavigation ? "block" : "none";

      // Initialize with currently saved genres
      isWildBurrowSelected = getStoredWildBurrow();
      tempSelectedGenres = getStoredGenres();
      if (isWildBurrowSelected) tempSelectedGenres.clear();

      updateVisuals();
      modalEl.classList.add("active");
      document.body.style.overflow = "hidden";
    },

    close: function() {
      if (!modalEl) return;
      modalEl.classList.remove("active");
      document.body.style.overflow = "";
    },

    isOpen: function() {
      return modalEl && modalEl.classList.contains("active");
    },

    getGenres: function() {
      return AUTHORITATIVE_GENRES.slice();
    }
  };
})();
