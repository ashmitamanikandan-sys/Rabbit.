// ========================================================
// RABBIT RESPONSIVE NAVIGATION COMPONENT (Phase 1 Modernization)
// ========================================================

import { state, setActiveNavTab, setScreen, resetOnboardingForTesting, switchGenre } from '../state/store.js';
import { AUTHORITATIVE_GENRES } from '../data/catalog.js';

export function renderTopNav(currentTab = 'for-you') {
  return `
    <nav class="rabbit-top-nav" id="rabbit-top-main-nav" aria-label="Main Navigation">
      <div class="rabbit-top-nav-inner">
        <button type="button" class="rabbit-top-nav-item ${currentTab === 'for-you' ? 'active' : ''}" data-nav="for-you" aria-label="For You Feed">
          <svg class="rabbit-nav-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2L14.2 9.2L21.4 11.4L14.2 13.6L12 21L9.8 13.6L2.6 11.4L9.8 9.2L12 2Z"></path>
          </svg>
          <span>For You</span>
        </button>

        <button type="button" class="rabbit-top-nav-item ${currentTab === 'genres' ? 'active' : ''}" data-nav="genres" aria-label="Browse Genres">
          <svg class="rabbit-nav-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon>
          </svg>
          <span>Genres</span>
        </button>

        <button type="button" class="rabbit-top-nav-item ${currentTab === 'library' ? 'active' : ''}" data-nav="library" aria-label="My Saved Library">
          <svg class="rabbit-nav-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
          </svg>
          <span>My Library</span>
        </button>

        <button type="button" class="rabbit-top-nav-item ${currentTab === 'following' ? 'active' : ''}" data-nav="following" aria-label="Following Books">
          <svg class="rabbit-nav-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
            <path d="M12 7.5a1.5 1.5 0 0 1 3 0c0 1.5-2.2 2.5-3 3.5-.8-1-3-2-3-3.5a1.5 1.5 0 0 1 3 0z" fill="currentColor"></path>
          </svg>
          <span>Following</span>
        </button>
      </div>
    </nav>
  `;
}

export function bindTopNavEvents(container, onNavSelect) {
  container.querySelectorAll('.rabbit-top-nav-item').forEach(btn => {
    btn.onclick = () => {
      const dest = btn.dataset.nav;
      if (dest === 'genres') {
        const bar = document.querySelector('.rabbit-genre-nav-bar');
        if (bar) {
          bar.scrollIntoView({ behavior: 'smooth', block: 'center' });
          bar.classList.add('rabbit-pulse-highlight');
          setTimeout(() => bar.classList.remove('rabbit-pulse-highlight'), 1200);
        } else {
          setScreen('interests');
        }
      } else {
        setActiveNavTab(dest);
        if (onNavSelect) onNavSelect(dest);
      }
    };
  });
}

export function renderDesktopSidebar(activeTab = 'for-you', onNavSelect) {
  const sidebar = document.createElement('aside');
  sidebar.className = 'rabbit-desktop-sidebar';
  sidebar.setAttribute('aria-label', 'Desktop Navigation');

  sidebar.innerHTML = `
    <div class="sidebar-brand" style="padding:24px 20px 20px;border-bottom:1px solid rgba(255,255,255,0.08);">
      <div style="font-size:22px;font-weight:900;letter-spacing:1px;color:#fff;display:flex;align-items:center;gap:8px;">
        RABBIT <span style="color:var(--lilac);font-size:16px;">✦</span>
      </div>
      <p style="font-size:12px;color:var(--muted);margin:6px 0 0;">Ideas worth getting lost in</p>
    </div>

    <nav class="sidebar-links" style="padding:16px 12px;display:flex;flex-direction:column;gap:6px;">
      <button type="button" class="sidebar-link ${activeTab === 'for-you' ? 'active' : ''}" data-nav="for-you">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L14.2 9.2L21.4 11.4L14.2 13.6L12 21L9.8 13.6L2.6 11.4L9.8 9.2L12 2Z"></path></svg>
        <span>For You Feed</span>
      </button>

      <button type="button" class="sidebar-link ${activeTab === 'library' ? 'active' : ''}" data-nav="library">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
        <span>My Saved Library</span>
      </button>

      <button type="button" class="sidebar-link ${activeTab === 'following' ? 'active' : ''}" data-nav="following">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
        <span>Following Books</span>
      </button>

      <button type="button" class="sidebar-link" id="rabbit-sidebar-reset-onboarding-btn" style="margin-top:20px;opacity:0.65;font-size:12px;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path></svg>
        <span>Reset Onboarding (Demo)</span>
      </button>
    </nav>
  `;

  sidebar.querySelectorAll('.sidebar-link[data-nav]').forEach(btn => {
    btn.onclick = () => {
      const dest = btn.dataset.nav;
      setActiveNavTab(dest);
      if (onNavSelect) onNavSelect(dest);
    };
  });

  const resetBtn = sidebar.querySelector('#rabbit-sidebar-reset-onboarding-btn');
  if (resetBtn) {
    resetBtn.onclick = () => {
      resetOnboardingForTesting();
    };
  }

  return sidebar;
}

export function renderDesktopContextPane() {
  const pane = document.createElement('aside');
  pane.className = 'rabbit-desktop-context-pane';
  pane.setAttribute('aria-label', 'Context & Rabbit Hole Stats');

  const savedCount = state.savedBookIds ? state.savedBookIds.size : 0;
  const likedCount = state.likedBooks ? state.likedBooks.size : 0;
  const isMixed = state.mixMode && state.selectedGenres.size > 1;
  const selectedArr = Array.from(state.selectedGenres);
  const activeLabel = isMixed 
    ? `${selectedArr.slice(0, 3).join(' + ')}${selectedArr.length > 3 ? ` +${selectedArr.length - 3}` : ''} (Mix)`
    : state.activeGenre;

  pane.innerHTML = `
    <!-- Active Genre Status Card -->
    <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(188,166,255,0.18);border-radius:16px;padding:18px;">
      <div style="font-size:10px;font-weight:700;letter-spacing:1.5px;color:var(--lilac);text-transform:uppercase;margin-bottom:6px;">ACTIVE EXPLORATION</div>
      <div style="font-size:18px;font-weight:700;color:#fff;line-height:1.2;font-family:var(--reading-font);margin-bottom:8px;">${activeLabel}</div>
      <p style="font-size:12px;color:var(--muted);line-height:1.5;margin:0;">
        ${isMixed ? 'Naturally interleaved from your custom genre selection.' : 'Landmark masterworks curated for depth and clarity.'}
      </p>
    </div>

    <!-- Rabbit Hole Stats -->
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:18px;">
      <div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#d1d5db;margin-bottom:14px;display:flex;align-items:center;gap:6px;">
        <span>✦</span> RABBIT HOLE STATS
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
        <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);">
          <div style="font-size:20px;font-weight:800;color:var(--lilac);">1,050</div>
          <div style="font-size:11px;color:var(--muted);margin-top:2px;">Landmark Books</div>
        </div>
        <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);">
          <div style="font-size:20px;font-weight:800;color:var(--lilac);">21</div>
          <div style="font-size:11px;color:var(--muted);margin-top:2px;">Curated Genres</div>
        </div>
        <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);">
          <div style="font-size:20px;font-weight:800;color:#f472b6;">${likedCount}</div>
          <div style="font-size:11px;color:var(--muted);margin-top:2px;">Liked Insights</div>
        </div>
        <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);">
          <div style="font-size:20px;font-weight:800;color:#c084fc;">${savedCount}</div>
          <div style="font-size:11px;color:var(--muted);margin-top:2px;">Saved in Library</div>
        </div>
      </div>
    </div>

    <!-- Quick Genre Switcher -->
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:18px;">
      <div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#d1d5db;margin-bottom:12px;">QUICK HOP</div>
      <div class="chips" id="rabbit-context-genre-chips" style="display:flex;flex-wrap:wrap;gap:6px;">
        ${AUTHORITATIVE_GENRES.map(g => {
          const isActive = state.activeGenre === g;
          return `
            <button type="button" 
              class="chip ${isActive ? 'active' : ''}" 
              data-genre="${g}" 
              style="padding:5px 11px;font-size:11px;border-radius:16px;cursor:pointer;"
            >
              ${g}
            </button>
          `;
        }).join('')}
      </div>
    </div>

    <!-- Inspiration Quote -->
    <div style="padding:14px;border-left:2px solid var(--lilac);background:rgba(188,166,255,0.05);border-radius:0 12px 12px 0;">
      <p style="font-family:var(--reading-font);font-style:italic;font-size:13px;line-height:1.6;color:#e5e7eb;margin:0 0 6px;">
        "Follow your curiosity wherever it leads. The deepest leverage comes from the books you didn't expect to read."
      </p>
      <span style="font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;">— RABBIT EDITORIAL</span>
    </div>
  `;

  // Bind quick hop chip events
  pane.querySelectorAll('#rabbit-context-genre-chips .chip').forEach(btn => {
    btn.onclick = () => {
      const g = btn.dataset.genre;
      switchGenre(g);
    };
  });

  return pane;
}

