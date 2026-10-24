// ========================================================
// RABBIT FEED COMPONENT (Phase 1 Modernization)
// ========================================================

import { state, switchGenre, toggleGenre, resetToSingleGenre, openReader } from '../state/store.js';
import { AUTHORITATIVE_GENRES, fetchGenreBooks, fetchMultipleGenres, buildMixedGenreFeed, searchCachedBooks } from '../data/catalog.js';
import { renderTopNav, bindTopNavEvents } from './nav.js';
import { createBookCard } from './card.js';

export async function renderMainFeed(container, options = {}) {
  const currentTab = state.activeNavTab || 'for-you';
  const isMixed = state.mixMode && state.selectedGenres.size > 1;
  const selectedArr = Array.from(state.selectedGenres);
  const activeGenreTitle = isMixed 
    ? `${selectedArr.join(' + ').toUpperCase()} (MIXED FEED)`
    : state.activeGenre.toUpperCase();

  container.innerHTML = `
    <div class="page home-scroll" id="homeScroll">
      <section class="home-first">
        <header class="top" style="padding:14px 20px;display:flex;align-items:center;justify-content:space-between;">
          <div class="wordmark" aria-label="RABBIT">
            <span style="font-size:20px;font-weight:900;letter-spacing:1px;color:#fff;">RABBIT <span style="color:var(--lilac);">✦</span></span>
          </div>
          <button type="button" class="rabbit-menu-trigger" id="rabbit-onboarding-restart-trigger" title="Reset onboarding flow for testing" style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);padding:6px 12px;border-radius:20px;color:#9ca3af;font-size:11px;font-weight:600;cursor:pointer;">
            ↺ Reset Onboarding
          </button>
        </header>

        ${renderTopNav(currentTab)}

        <div class="home-body">
          <!-- Stories Carousel -->
          <div class="stories" id="rabbit-stories-rail" aria-label="Book Stories"></div>

          <div class="section" style="padding-top:4px;">
            <!-- Autocomplete Instant Search Form -->
            <form class="rabbit-library-search" id="rabbit-search-form" style="margin-bottom:12px;position:relative;display:flex;gap:6px;align-items:center;">
              <div style="position:relative;flex:1;">
                <input type="search" id="rabbit-search-input" placeholder="Search 1,050+ masterworks, authors, concepts…" aria-label="Search books" autocomplete="off" style="width:100%;box-sizing:border-box;padding:10px 14px;border-radius:24px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);color:#fff;font-size:14px;outline:none;">
                <div class="rabbit-search-autocomplete" id="rabbit-search-dropdown" style="display:none;position:absolute;top:100%;left:0;right:0;margin-top:6px;background:#131318;border:1px solid rgba(168,85,247,0.3);border-radius:14px;box-shadow:0 12px 30px rgba(0,0,0,0.8);z-index:999;max-height:320px;overflow-y:auto;padding:6px 0;"></div>
              </div>
              <button type="submit" class="primary" style="padding:9px 16px;border-radius:24px;cursor:pointer;flex-shrink:0;font-size:13px;font-weight:600;">Search ↗</button>
              <button type="button" id="rabbit-search-clear" style="display:none;padding:8px 12px;border-radius:20px;background:rgba(239,68,68,0.15);color:#fca5a5;border:1px solid rgba(239,68,68,0.3);font-size:12px;font-weight:600;cursor:pointer;flex-shrink:0;">✕ Clear</button>
            </form>

            <!-- Horizontal Genre Bar -->
            <div class="rabbit-genre-nav-bar" id="rabbit-genre-pill-bar" style="display:flex;overflow-x:auto;white-space:nowrap;gap:8px;padding:8px 0 16px;scrollbar-width:none;-webkit-overflow-scrolling:touch;align-items:center;"></div>

            <div class="section-head" style="margin-top:14px;display:flex;align-items:baseline;justify-content:space-between;">
              <h2 style="font-size:20px;margin:0;font-weight:700;">For your curiosity <span class="accent">✦</span></h2>
              <span class="muted" id="rabbit-active-genre-heading" style="font-size:11px;font-weight:700;letter-spacing:1px;color:#a855f7;">${activeGenreTitle}</span>
            </div>

            <!-- First Book Slot -->
            <div class="rabbit-first-book-slot" id="rabbit-first-book-slot">
              <div class="feature" style="padding:40px 20px;text-align:center;">
                <div class="muted">Loading ${activeGenreTitle} landmark works…</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Container for rest of the feed cards -->
      <div id="rabbit-cards-container"></div>
    </div>
  `;

  // Bind Top Nav Events
  bindTopNavEvents(container, (dest) => {
    if (dest === 'library') {
      renderLibraryView(container);
    } else if (dest === 'following') {
      renderFollowingView(container);
    } else {
      renderMainFeed(container);
    }
  });

  // Bind Reset Onboarding Helper
  const restartBtn = container.querySelector('#rabbit-onboarding-restart-trigger');
  if (restartBtn) {
    restartBtn.onclick = () => {
      window.resetRabbitOnboarding();
    };
  }

  // Render Genre Bar
  renderGenrePills(container.querySelector('#rabbit-genre-pill-bar'));

  // Wire Search
  setupSearch(container);

  // Fetch and display books
  await loadAndDisplayBooks(container);
}

function renderGenrePills(bar) {
  if (!bar) return;
  bar.replaceChildren();

  // Multi-genre Clear or Mix toggle chip
  if (state.mixMode && state.selectedGenres.size > 1) {
    const clearBtn = document.createElement('button');
    clearBtn.type = 'button';
    clearBtn.className = 'chip rabbit-mix-clear-chip';
    clearBtn.style.cssText = 'flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 14px;border-radius:20px;background:rgba(239,68,68,0.18);color:#fca5a5;border:1px solid rgba(239,68,68,0.4);font-weight:700;display:inline-flex;align-items:center;gap:5px;';
    clearBtn.innerHTML = `<span>✕</span> Clear Mix (${state.selectedGenres.size})`;
    clearBtn.onclick = () => {
      resetToSingleGenre();
    };
    bar.appendChild(clearBtn);
  } else {
    const mixTrigger = document.createElement('button');
    mixTrigger.type = 'button';
    mixTrigger.className = 'chip rabbit-mix-toggle-chip';
    mixTrigger.style.cssText = 'flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 12px;border-radius:20px;background:rgba(168,85,247,0.12);color:#d8b4fe;border:1px dashed rgba(168,85,247,0.45);font-weight:600;';
    mixTrigger.innerHTML = state.mixMode ? '✓ Mixing Active' : '<span>+</span> Mix Genres';
    mixTrigger.onclick = () => {
      state.mixMode = !state.mixMode;
      renderGenrePills(bar);
    };
    bar.appendChild(mixTrigger);
  }

  AUTHORITATIVE_GENRES.forEach(g => {
    const isSelected = state.selectedGenres.has(g);
    const chip = document.createElement('button');
    chip.type = 'button';
    chip.className = `chip ${isSelected ? 'active' : ''}`;
    chip.style.cssText = 'flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 14px;border-radius:20px;transition:all 0.18s ease;';
    chip.textContent = g;

    chip.onclick = (e) => {
      const isMulti = e.shiftKey || e.ctrlKey || e.metaKey || state.mixMode;
      if (isMulti) {
        toggleGenre(g);
      } else {
        switchGenre(g);
      }
    };
    bar.appendChild(chip);
  });
}

async function loadAndDisplayBooks(container) {
  const isMixed = state.mixMode && state.selectedGenres.size > 1;
  const selectedArr = Array.from(state.selectedGenres);

  let booksToRender = [];
  if (isMixed) {
    const genreMap = await fetchMultipleGenres(selectedArr);
    booksToRender = buildMixedGenreFeed(genreMap, selectedArr);
  } else {
    booksToRender = await fetchGenreBooks(state.activeGenre);
  }

  // Populate Stories Rail
  const storiesRail = container.querySelector('#rabbit-stories-rail');
  if (storiesRail) {
    storiesRail.replaceChildren();
    const storyBooks = booksToRender.slice(0, 24);
    storyBooks.forEach(b => {
      if (!b.cover_url && !b.cover) return;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'story';
      btn.innerHTML = `
        <img loading="lazy" decoding="async" src="${b.cover_url || b.cover}" alt="${b.title}">
        <span>${b.title}</span>
      `;
      btn.onclick = () => openReader(b, 'home');
      storiesRail.appendChild(btn);
    });
  }

  // Render First Book Slot
  const firstSlot = container.querySelector('#rabbit-first-book-slot');
  if (firstSlot && booksToRender.length > 0) {
    firstSlot.replaceChildren();
    const firstCard = createBookCard(booksToRender[0], 0, {
      isFirstSlot: true,
      onReadMore: (b) => openReader(b, 'home')
    });
    firstSlot.appendChild(firstCard);
  }

  // Render Rest of Feed
  const cardsContainer = container.querySelector('#rabbit-cards-container');
  if (cardsContainer) {
    cardsContainer.replaceChildren();
    if (booksToRender.length > 1) {
      const rest = booksToRender.slice(1);
      const fragment = document.createDocumentFragment();
      rest.forEach((b, idx) => {
        const card = createBookCard(b, idx + 1, {
          isFirstSlot: false,
          onReadMore: (book) => openReader(book, 'home')
        });
        fragment.appendChild(card);
      });
      cardsContainer.appendChild(fragment);
    }
  }
}

function setupSearch(container) {
  const form = container.querySelector('#rabbit-search-form');
  const input = container.querySelector('#rabbit-search-input');
  const dropdown = container.querySelector('#rabbit-search-dropdown');
  const clearBtn = container.querySelector('#rabbit-search-clear');
  if (!form || !input || !dropdown) return;

  let timer = null;
  input.oninput = () => {
    const val = input.value.trim();
    if (clearBtn) clearBtn.style.display = val ? 'inline-block' : 'none';
    clearTimeout(timer);
    if (val.length < 2) {
      dropdown.style.display = 'none';
      dropdown.replaceChildren();
      return;
    }
    timer = setTimeout(() => {
      const matches = searchCachedBooks(val).slice(0, 6);
      if (matches.length === 0) {
        dropdown.style.display = 'none';
        return;
      }
      dropdown.replaceChildren();
      matches.forEach(b => {
        const item = document.createElement('div');
        item.style.cssText = 'display:flex;align-items:center;gap:10px;padding:8px 14px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.04);';
        item.innerHTML = `
          <img src="${b.cover_url || b.cover || ''}" style="width:28px;height:40px;object-fit:cover;border-radius:4px;flex-shrink:0;">
          <div style="flex:1;min-width:0;">
            <div style="font-size:13px;font-weight:600;color:#f3f4f6;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${b.title}</div>
            <div style="font-size:11px;color:#9ca3af;">${b.author} · ${b.genre || 'Landmark'}</div>
          </div>
        `;
        item.onclick = () => {
          dropdown.style.display = 'none';
          openReader(b, 'home');
        };
        dropdown.appendChild(item);
      });
      dropdown.style.display = 'block';
    }, 180);
  };

  if (clearBtn) {
    clearBtn.onclick = () => {
      input.value = '';
      dropdown.style.display = 'none';
      clearBtn.style.display = 'none';
      loadAndDisplayBooks(container);
    };
  }

  form.onsubmit = (e) => {
    e.preventDefault();
    dropdown.style.display = 'none';
    const val = input.value.trim();
    if (!val) return;
    const matches = searchCachedBooks(val);
    const heading = container.querySelector('#rabbit-active-genre-heading');
    if (heading) heading.textContent = `SEARCH: "${val.toUpperCase()}" (${matches.length})`;
    
    const cardsContainer = container.querySelector('#rabbit-cards-container');
    const firstSlot = container.querySelector('#rabbit-first-book-slot');
    if (matches.length > 0) {
      if (firstSlot) {
        firstSlot.replaceChildren();
        firstSlot.appendChild(createBookCard(matches[0], 0, { isFirstSlot: true, onReadMore: (b) => openReader(b, 'home') }));
      }
      if (cardsContainer) {
        cardsContainer.replaceChildren();
        if (matches.length > 1) {
          const rest = matches.slice(1);
          rest.forEach((b, i) => {
            cardsContainer.appendChild(createBookCard(b, i + 1, { onReadMore: (bk) => openReader(bk, 'home') }));
          });
        }
      }
    } else {
      if (firstSlot) firstSlot.innerHTML = `<div style="padding:40px;text-align:center;color:#9ca3af;">No masterworks matching "${val}" found in current cache.</div>`;
      if (cardsContainer) cardsContainer.replaceChildren();
    }
  };

  document.addEventListener('click', (e) => {
    if (!form.contains(e.target)) dropdown.style.display = 'none';
  });
}

export async function renderLibraryView(container) {
  const scroller = container.querySelector('#homeScroll');
  if (!scroller) return;

  const cardsContainer = container.querySelector('#rabbit-cards-container');
  const firstSlot = container.querySelector('#rabbit-first-book-slot');
  const heading = container.querySelector('#rabbit-active-genre-heading');
  if (heading) heading.textContent = `MY LIBRARY (${state.savedBookIds.size})`;

  if (state.savedBookIds.size === 0) {
    if (firstSlot) {
      firstSlot.innerHTML = `
        <div class="feedpost" style="padding:48px 24px;text-align:center;background:rgba(20,20,24,0.7);border-radius:18px;border:1px solid rgba(255,255,255,0.08);margin-top:20px;">
          <div style="font-size:36px;margin-bottom:14px;">📚</div>
          <h2 style="font-size:20px;color:#f3f4f6;margin-bottom:8px;">Your Library Burrow is Empty</h2>
          <p style="font-size:14px;color:#9ca3af;line-height:1.6;max-width:380px;margin:0 auto 20px;">
            Tap <strong style="color:#c4b5fd;">Save</strong> on any book insight card or reader overlay to preserve your favorite reads here.
          </p>
          <button type="button" class="primary" id="rabbit-library-explore-btn" style="padding:10px 20px;border-radius:24px;cursor:pointer;font-weight:600;">
            ✦ Explore Masterworks Feed
          </button>
        </div>
      `;
      const btn = firstSlot.querySelector('#rabbit-library-explore-btn');
      if (btn) btn.onclick = () => renderMainFeed(container);
    }
    if (cardsContainer) cardsContainer.replaceChildren();
  } else {
    // Collect saved books
    const savedBooks = [];
    for (const id of state.savedBookIds) {
      const b = await findBookById(id);
      if (b) savedBooks.push(b);
    }
    if (firstSlot && savedBooks.length > 0) {
      firstSlot.replaceChildren(createBookCard(savedBooks[0], 0, { isFirstSlot: true, onReadMore: (b) => openReader(b, 'home') }));
    }
    if (cardsContainer && savedBooks.length > 1) {
      cardsContainer.replaceChildren();
      savedBooks.slice(1).forEach((b, i) => {
        cardsContainer.appendChild(createBookCard(b, i + 1, { onReadMore: (bk) => openReader(bk, 'home') }));
      });
    }
  }
}

export async function renderFollowingView(container) {
  const cardsContainer = container.querySelector('#rabbit-cards-container');
  const firstSlot = container.querySelector('#rabbit-first-book-slot');
  const heading = container.querySelector('#rabbit-active-genre-heading');
  if (heading) heading.textContent = `FOLLOWED BOOKS (${state.followedBookIds.size})`;

  if (state.followedBookIds.size === 0) {
    if (firstSlot) {
      firstSlot.innerHTML = `
        <div class="feedpost" style="padding:48px 24px;text-align:center;background:rgba(20,20,24,0.7);border-radius:18px;border:1px solid rgba(255,255,255,0.08);margin-top:20px;">
          <div style="font-size:36px;margin-bottom:14px;">♥</div>
          <h2 style="font-size:20px;color:#f3f4f6;margin-bottom:8px;">No Followed Books Yet</h2>
          <p style="font-size:14px;color:#9ca3af;line-height:1.6;max-width:380px;margin:0 auto 20px;">
            Follow your favorite authors and landmark works to track future chapter releases and community conversations.
          </p>
          <button type="button" class="primary" id="rabbit-following-explore-btn" style="padding:10px 20px;border-radius:24px;cursor:pointer;font-weight:600;">
            ✦ Explore Masterworks Feed
          </button>
        </div>
      `;
      const btn = firstSlot.querySelector('#rabbit-following-explore-btn');
      if (btn) btn.onclick = () => renderMainFeed(container);
    }
    if (cardsContainer) cardsContainer.replaceChildren();
  }
}
