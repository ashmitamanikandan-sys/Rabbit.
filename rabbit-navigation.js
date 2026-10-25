/**
 * RABBIT Unified Navigation System (Part 4)
 * Authoritative 5 destinations: Home, Genres, Warren, Clubs, Profile.
 * Responsive mobile bottom bar + desktop top bar with elegant icons and active states.
 */
(function() {
  "use strict";

  const DESTINATIONS = [
    {
      id: "home",
      label: "Home",
      iconSvg: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
    },
    {
      id: "genres",
      label: "Genres",
      iconSvg: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>'
    },
    {
      id: "warren",
      label: "Warren",
      iconSvg: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>'
    },
    {
      id: "clubs",
      label: "Clubs",
      iconSvg: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
    },
    {
      id: "profile",
      label: "Profile",
      iconSvg: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/></svg>'
    }
  ];

  let currentTab = "home";
  let navBarEl = null;

  function ensureStyles() {
    if (document.getElementById("rabbit-unified-nav-style")) return;
    const style = document.createElement("style");
    style.id = "rabbit-unified-nav-style";
    style.textContent = `
      /* Universal Docked Navigation Bar */
      #rabbit-unified-nav {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        max-width: 540px;
        background: rgba(8, 8, 11, 0.92);
        -webkit-backdrop-filter: blur(24px) saturate(160%);
        backdrop-filter: blur(24px) saturate(160%);
        border-top: 1px solid rgba(167, 139, 250, 0.16);
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 8px 12px calc(8px + env(safe-area-inset-bottom));
        z-index: 9000;
        box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.6);
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
      }

      /* Hide old competing navs */
      .footnav, #rabbit-v10-nav, #rabbit-menu-trigger, #rabbit-warren-direct, #rabbit-fy-trigger {
        display: none !important;
      }

      .rabbit-nav-item {
        background: transparent;
        border: none;
        color: #8E8899;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 3px;
        padding: 6px 12px;
        border-radius: 12px;
        cursor: pointer;
        min-width: 58px;
        transition: color 0.18s ease, transform 0.18s ease;
        -webkit-tap-highlight-color: transparent;
      }
      .rabbit-nav-item svg {
        transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1), stroke 0.2s ease;
      }
      .rabbit-nav-item span {
        font-size: 10.5px;
        font-weight: 600;
        letter-spacing: 0.02em;
        line-height: 1;
      }

      .rabbit-nav-item:hover {
        color: #D8C5FF;
        transform: translateY(-1px);
      }
      .rabbit-nav-item.active {
        color: #A78BFA;
      }
      .rabbit-nav-item.active svg {
        transform: scale(1.12);
        stroke: #A78BFA;
        filter: drop-shadow(0 0 6px rgba(167, 139, 250, 0.45));
      }
      .rabbit-nav-item.active span {
        color: #F5F2F8;
      }

      /* Hide nav during Welcome / Auth screens */
      body[data-rabbit-stage="welcome"] #rabbit-unified-nav,
      body[data-rabbit-stage="interests"] #rabbit-unified-nav,
      body[data-rabbit-stage="auth"] #rabbit-unified-nav {
        display: none !important;
      }

      /* Desktop / Tablet polish */
      @media (min-width: 768px) {
        #rabbit-unified-nav {
          max-width: 600px;
          border-radius: 24px;
          bottom: 20px;
          border: 1px solid rgba(167, 139, 250, 0.2);
          box-shadow: 0 12px 40px rgba(0, 0, 0, 0.75);
          padding: 8px 16px;
        }
      }
    `;
    document.head.appendChild(style);
  }

  function mountNavBar() {
    ensureStyles();
    if (navBarEl) return navBarEl;

    navBarEl = document.createElement("nav");
    navBarEl.id = "rabbit-unified-nav";
    navBarEl.setAttribute("aria-label", "RABBIT primary navigation");

    DESTINATIONS.forEach(dest => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "rabbit-nav-item" + (dest.id === currentTab ? " active" : "");
      btn.dataset.tab = dest.id;
      btn.setAttribute("aria-label", dest.label);

      btn.innerHTML = `
        ${dest.iconSvg}
        <span>${dest.label}</span>
      `;

      btn.onclick = () => window.RabbitNavigation.navigate(dest.id);
      navBarEl.appendChild(btn);
    });

    document.body.appendChild(navBarEl);
    return navBarEl;
  }

  function updateActiveVisual() {
    if (!navBarEl) return;
    const btns = navBarEl.querySelectorAll(".rabbit-nav-item");
    btns.forEach(b => {
      const isAct = b.dataset.tab === currentTab;
      b.classList.toggle("active", isAct);
    });
  }

  window.RabbitNavigation = {
    init: function() {
      mountNavBar();
      // Check query parameter if navigated with ?tab=warren, etc.
      const params = new URLSearchParams(window.location.search);
      const tabParam = params.get("tab");
      if (tabParam && ["home", "genres", "warren", "clubs", "profile"].includes(tabParam)) {
        setTimeout(() => this.navigate(tabParam), 50);
      }
    },

    navigate: function(tabId) {
      if (tabId === "genres") {
        if (window.RabbitGenreModal) {
          window.RabbitGenreModal.open({ fromNav: true });
        }
        return;
      }

      currentTab = tabId;
      updateActiveVisual();

      // Dispatch route switch
      if (tabId === "home") {
        if (window.RabbitUnifiedViews) window.RabbitUnifiedViews.showHome();
        else if (typeof renderHome === "function") renderHome();
      } else if (tabId === "warren") {
        if (window.RabbitUnifiedViews) window.RabbitUnifiedViews.showWarren();
      } else if (tabId === "clubs") {
        if (window.RabbitUnifiedViews) window.RabbitUnifiedViews.showClubs();
      } else if (tabId === "profile") {
        if (window.RabbitUnifiedViews) window.RabbitUnifiedViews.showProfile();
      }
    },

    getActiveTab: function() {
      return currentTab;
    },

    setActiveTab: function(tabId) {
      currentTab = tabId;
      updateActiveVisual();
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => window.RabbitNavigation.init(), { once: true });
  } else {
    window.RabbitNavigation.init();
  }
})();
