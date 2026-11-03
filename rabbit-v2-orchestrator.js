/**
 * RABBIT 2.0 — Master View Orchestrator (rabbit-v2-orchestrator.js)
 * Unifies:
 * - The Burrow (Chapter Deck Feed)
 * - The Sky (Interactive Celestial Night Sky Canvas)
 * - Tonight's Sky (5-Chapter Daily Playlist)
 * - The Warren (Chapter-attached community discussions)
 * - Clubs (Co-reading constellation groups)
 * - 5-Tab Bottom Navigation Bar
 */

(function(window) {
  'use strict';

  var activeTab = 'burrow';
  var skyCanvasInstance = null;

  function initOrchestrator() {
    ensureBottomNav();
    hookNavigation();

    // Check if on home / burrow screen
    var checkInterval = setInterval(function() {
      if (document.body.dataset.rabbitStage === 'curiosity' || document.getElementById('homeScroll')) {
        clearInterval(checkInterval);
        mountBurrowView();
      }
    }, 100);
  }

  // 1. Bottom Navigation Bar
  function ensureBottomNav() {
    var existing = document.getElementById('rabbit-v2-bottom-nav');
    if (existing) return;

    var nav = document.createElement('nav');
    nav.id = 'rabbit-v2-bottom-nav';
    nav.className = 'rabbit-bottom-nav';
    nav.setAttribute('aria-label', 'RABBIT 2.0 Navigation');

    nav.innerHTML = `
      <button class="nav-tab-btn active" id="nav-burrow" onclick="window.switchV2Tab('burrow')">
        <span class="nav-tab-icon">🕳️</span>
        <span class="nav-tab-label">The Burrow</span>
      </button>
      <button class="nav-tab-btn" id="nav-tonight" onclick="window.switchV2Tab('tonight')">
        <span class="nav-tab-icon">🌙</span>
        <span class="nav-tab-label">Tonight's Sky</span>
      </button>
      <button class="nav-tab-btn" id="nav-warren" onclick="window.switchV2Tab('warren')">
        <span class="nav-tab-icon">✦</span>
        <span class="nav-tab-label">The Warren</span>
      </button>
      <button class="nav-tab-btn" id="nav-clubs" onclick="window.switchV2Tab('clubs')">
        <span class="nav-tab-icon">♧</span>
        <span class="nav-tab-label">Clubs</span>
      </button>
      <button class="nav-tab-btn" id="nav-sky" onclick="window.switchV2Tab('sky')">
        <span class="nav-tab-icon sky-icon">✨</span>
        <span class="nav-tab-label">The Sky</span>
      </button>
    `;

    document.body.appendChild(nav);

    // Only display nav when inside app (not on welcome screen)
    function syncNavVisibility() {
      var stage = document.body.dataset.rabbitStage;
      var inApp = (stage === 'curiosity' || stage === 'feed' || stage === 'reader');
      nav.style.display = inApp ? 'flex' : 'none';
    }

    var obs = new MutationObserver(syncNavVisibility);
    obs.observe(document.body, { attributes: true, attributeFilter: ['data-rabbit-stage'] });
    syncNavVisibility();
  }

  // 2. Switch Views
  window.switchV2Tab = function(tabName) {
    activeTab = tabName;

    // Update bottom nav active classes
    var buttons = document.querySelectorAll('.nav-tab-btn');
    for (var i = 0; i < buttons.length; i++) {
      var btn = buttons[i];
      btn.classList.toggle('active', btn.id === ('nav-' + tabName));
    }

    var appRoot = document.getElementById('homeScroll') || document.getElementById('app');
    if (!appRoot) return;

    if (tabName === 'burrow') {
      mountBurrowView();
    } else if (tabName === 'tonight') {
      mountTonightView();
    } else if (tabName === 'warren') {
      mountWarrenView();
    } else if (tabName === 'clubs') {
      mountClubsView();
    } else if (tabName === 'sky') {
      mountSkyView();
    }
  };

  // View: The Burrow
  function mountBurrowView() {
    var homeScroll = document.getElementById('homeScroll');
    if (!homeScroll) return;

    homeScroll.innerHTML = `
      <div class="rabbit-app-viewport">
        <!-- Top Rail: Constellations in Progress -->
        <div class="rabbit-constellations-rail" id="rabbit-constellations-rail"></div>

        <!-- Main Feed: Snap-scroll Chapter Decks -->
        <main class="rabbit-feed-container" id="rabbit-feed-root"></main>
      </div>
    `;

    if (window.initChapterFeed) {
      window.initChapterFeed();
    }
  }

  // View: Tonight's Sky
  function mountTonightView() {
    var homeScroll = document.getElementById('homeScroll');
    if (!homeScroll) return;

    homeScroll.innerHTML = '<div class="rabbit-app-viewport" id="v2-tonight-container"></div>';
    var container = document.getElementById('v2-tonight-container');
    if (window.renderTonightsSkyView) {
      window.renderTonightsSkyView(container);
    }
  }

  // View: The Warren
  function mountWarrenView() {
    var homeScroll = document.getElementById('homeScroll');
    if (!homeScroll) return;

    homeScroll.innerHTML = '<div class="rabbit-app-viewport" id="v2-warren-container"></div>';
    var container = document.getElementById('v2-warren-container');
    if (window.renderWarrenFeed) {
      window.renderWarrenFeed(container);
    }
  }

  // View: Clubs
  function mountClubsView() {
    var homeScroll = document.getElementById('homeScroll');
    if (!homeScroll) return;

    homeScroll.innerHTML = '<div class="rabbit-app-viewport" id="v2-clubs-container"></div>';
    var container = document.getElementById('v2-clubs-container');
    if (window.renderClubsView) {
      window.renderClubsView(container);
    }
  }

  // View: The Sky (Interactive Canvas)
  function mountSkyView() {
    var homeScroll = document.getElementById('homeScroll');
    if (!homeScroll) return;

    var state = window.rabbitSky ? window.rabbitSky.state : { stars: { total: 0 }, streak: { nights: 1 }, constellations: { completed: {} } };
    var totalStars = state.stars.total;
    var completedCount = Object.keys(state.constellations.completed).length;
    var nights = state.streak.nights;
    var isDemo = state.settings.demoMode;

    homeScroll.innerHTML = `
      <div class="rabbit-app-viewport">
        <div class="sky-view-container" id="v2-sky-canvas-container">
          <!-- Sky Stats Header -->
          <div class="sky-stats-header">
            <div class="sky-stat-box">
              <span class="sky-stat-val">${totalStars} ✦</span>
              <span class="sky-stat-lbl">Stars Lit</span>
            </div>
            <div class="sky-stat-box">
              <span class="sky-stat-val">${completedCount}</span>
              <span class="sky-stat-lbl">Constellations</span>
            </div>
            <div class="sky-stat-box">
              <span class="sky-stat-val">${nights}</span>
              <span class="sky-stat-lbl">Nights Streak</span>
            </div>
            <button class="sky-wrapped-btn" onclick="window.generateRabbitWrapped()">✦ Wrapped</button>
            <button class="sky-wrapped-btn" style="background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.2);" onclick="window.openSettingsModal()">⚙</button>
          </div>
          ${isDemo ? '<div style="position:absolute;bottom:75px;left:50%;transform:translateX(-50%);background:rgba(251,191,36,0.2);border:1px solid #FBBF24;color:#FBBF24;padding:4px 14px;border-radius:99px;font-size:10px;font-weight:800;letter-spacing:1px;z-index:20;">DEMO PROFILE · CURIOUS READER</div>' : ''}
        </div>
      </div>
    `;

    // Instantiate Canvas
    if (window.RabbitSkyCanvas) {
      skyCanvasInstance = new window.RabbitSkyCanvas('v2-sky-canvas-container');
    }
  }

  // Hook legacy navigation calls to switchV2Tab
  function hookNavigation() {
    var origRabbitNavTo = window.rabbitNavTo;
    window.rabbitNavTo = function(dest) {
      if (dest === 'for-you') {
        window.switchV2Tab('burrow');
      } else if (dest === 'warren') {
        window.switchV2Tab('warren');
      } else if (dest === 'clubs') {
        window.switchV2Tab('clubs');
      } else if (dest === 'profile') {
        window.switchV2Tab('sky');
      } else if (typeof origRabbitNavTo === 'function') {
        origRabbitNavTo(dest);
      }
    };
  }

  // Mount on DOM ready
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    initOrchestrator();
  } else {
    document.addEventListener('DOMContentLoaded', initOrchestrator);
  }

})(window);
