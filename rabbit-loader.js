/**
 * RABBIT Mandatory Loading Experience (Part 2)
 * Ensures a minimum 2.0-second branded transition experience with hopping rabbit,
 * minimal book motif, rotating poetic lines, and zero layout jumping.
 */
(function() {
  "use strict";

  const POETIC_LINES = [
    "Every page hides another universe.",
    "Curiosity looks good on you.",
    "Some stories find you.",
    "Your next obsession is a page away."
  ];

  let activeLineIndex = 0;
  let overlayEl = null;
  let startTime = 0;
  let minDurationTimer = null;
  let isReadySignalReceived = false;
  let isShowing = false;

  function ensureStyles() {
    if (document.getElementById("rabbit-loader-style")) return;
    const style = document.createElement("style");
    style.id = "rabbit-loader-style";
    style.textContent = `
      #rabbit-loader-overlay {
        position: fixed;
        inset: 0;
        z-index: 99999;
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 45%, rgba(139, 92, 246, 0.12) 0%, rgba(5, 5, 5, 0.98) 75%);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        opacity: 1;
        transition: opacity 0.45s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.45s ease;
        visibility: visible;
        pointer-events: all;
        user-select: none;
      }
      #rabbit-loader-overlay.fade-out {
        opacity: 0;
        visibility: hidden;
        pointer-events: none;
      }

      .rabbit-loader-stage {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 24px;
        max-width: 360px;
        position: relative;
      }

      /* Hopping Rabbit & Floating Book Horizon */
      .rabbit-hopper-track {
        position: relative;
        width: 140px;
        height: 80px;
        margin-bottom: 24px;
      }

      .rabbit-book-motif {
        position: absolute;
        bottom: 8px;
        right: 14px;
        width: 38px;
        height: 26px;
        opacity: 0.85;
      }

      .rabbit-hopping-figure {
        position: absolute;
        bottom: 10px;
        left: 12px;
        width: 44px;
        height: 44px;
        animation: rabbit-hop-cycle 1.15s cubic-bezier(0.28, 0, 0.2, 1) infinite;
        transform-origin: 50% 100%;
      }

      .rabbit-shadow {
        position: absolute;
        bottom: 6px;
        left: 20px;
        width: 32px;
        height: 7px;
        background: radial-gradient(ellipse, rgba(167, 139, 250, 0.35) 0%, rgba(0, 0, 0, 0.7) 70%, transparent 100%);
        border-radius: 50%;
        animation: rabbit-shadow-pulse 1.15s cubic-bezier(0.28, 0, 0.2, 1) infinite;
      }

      @keyframes rabbit-hop-cycle {
        0%, 100% {
          transform: translate(0, 0) scale(1, 0.92);
        }
        25% {
          transform: translate(16px, -24px) scale(0.94, 1.06) rotate(6deg);
        }
        50% {
          transform: translate(32px, -32px) scale(0.96, 1.04) rotate(0deg);
        }
        75% {
          transform: translate(48px, -12px) scale(1.02, 0.98) rotate(-4deg);
        }
        88% {
          transform: translate(56px, 0) scale(1.12, 0.88);
        }
        94% {
          transform: translate(28px, 0) scale(0.98, 1);
        }
      }

      @keyframes rabbit-shadow-pulse {
        0%, 100% {
          transform: scale(1);
          opacity: 0.7;
        }
        50% {
          transform: scale(0.5);
          opacity: 0.2;
        }
      }

      .rabbit-loader-brand {
        font-size: 20px;
        font-weight: 800;
        letter-spacing: -0.04em;
        color: #F5F2F8;
        display: flex;
        align-items: center;
        gap: 2px;
        margin-bottom: 12px;
      }
      .rabbit-loader-brand .accent {
        color: #A78BFA;
      }

      .rabbit-loader-quote {
        font-family: "Iowan Old Style", "Baskerville", Georgia, serif;
        font-style: italic;
        font-size: 15px;
        line-height: 1.5;
        color: #A9A3B2;
        min-height: 44px;
        margin: 0;
        transition: opacity 0.3s ease;
      }

      .rabbit-loader-subtle {
        font-size: 10px;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #7A7485;
        margin-top: 18px;
        font-weight: 600;
      }

      @media (prefers-reduced-motion: reduce) {
        .rabbit-hopping-figure {
          animation: none !important;
          transform: none !important;
        }
        .rabbit-shadow {
          animation: none !important;
        }
      }
    `;
    document.head.appendChild(style);
  }

  function createOverlay() {
    ensureStyles();
    if (overlayEl) return overlayEl;

    overlayEl = document.createElement("div");
    overlayEl.id = "rabbit-loader-overlay";
    overlayEl.setAttribute("aria-live", "polite");
    overlayEl.setAttribute("role", "status");

    // Rotating quote
    const quote = POETIC_LINES[activeLineIndex % POETIC_LINES.length];
    activeLineIndex++;

    overlayEl.innerHTML = `
      <div class="rabbit-loader-stage">
        <div class="rabbit-hopper-track" aria-hidden="true">
          <div class="rabbit-shadow"></div>
          
          <!-- Hopping Rabbit SVG -->
          <svg class="rabbit-hopping-figure" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Ears with soft cosmic lilac gradient -->
            <path d="M16 19C16 11 19 3 22 3C25 3 25 11 23 18" stroke="#A78BFA" stroke-width="2.6" stroke-linecap="round"/>
            <path d="M21 20C22 13 26 5 29 6C32 7 30 14 27 20" stroke="#C4B5FD" stroke-width="2.6" stroke-linecap="round"/>
            <!-- Rabbit Body -->
            <ellipse cx="20" cy="28" rx="12" ry="9" fill="#F5F2F8"/>
            <circle cx="26" cy="23" r="7" fill="#F5F2F8"/>
            <!-- Eye -->
            <circle cx="28" cy="22" r="1.3" fill="#8B5CF6"/>
            <!-- Little Fluffy Tail -->
            <circle cx="9" cy="27" r="3.2" fill="#E0D7F5"/>
            <!-- Paws -->
            <ellipse cx="25" cy="35" rx="4" ry="2.2" fill="#E9E2F8"/>
            <ellipse cx="14" cy="35" rx="4.5" ry="2.2" fill="#E9E2F8"/>
          </svg>

          <!-- Minimal Open Book Motif -->
          <svg class="rabbit-book-motif" viewBox="0 0 38 26" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19 8C14 4 6 5 2 7V22C6 20 14 19 19 23C24 19 32 20 36 22V7C32 5 24 4 19 8Z" fill="#131217" stroke="#A78BFA" stroke-width="1.6" stroke-linejoin="round"/>
            <path d="M19 8V23" stroke="#8B5CF6" stroke-width="1.6" stroke-linecap="round"/>
            <line x1="7" y1="11" x2="14" y2="10" stroke="rgba(216,197,255,0.4)" stroke-width="1.2" stroke-linecap="round"/>
            <line x1="7" y1="15" x2="15" y2="14" stroke="rgba(216,197,255,0.4)" stroke-width="1.2" stroke-linecap="round"/>
            <line x1="23" y1="10" x2="31" y2="11" stroke="rgba(216,197,255,0.4)" stroke-width="1.2" stroke-linecap="round"/>
            <line x1="23" y1="14" x2="31" y2="15" stroke="rgba(216,197,255,0.4)" stroke-width="1.2" stroke-linecap="round"/>
          </svg>
        </div>

        <div class="rabbit-loader-brand">RABBIT<span class="accent">.</span></div>
        <p class="rabbit-loader-quote">“${quote}”</p>
        <span class="rabbit-loader-subtle">Entering the Burrow</span>
      </div>
    `;

    document.body.appendChild(overlayEl);
    return overlayEl;
  }

  window.RabbitLoader = {
    /**
     * Shows the loader. Returns a promise or completion handler.
     * Guaranteed minimum duration: 2000ms.
     */
    show: function(customLine) {
      if (isShowing) return;
      isShowing = true;
      isReadySignalReceived = false;
      startTime = Date.now();

      const el = createOverlay();
      el.classList.remove("fade-out");
      el.style.display = "flex";

      if (customLine) {
        const qEl = el.querySelector(".rabbit-loader-quote");
        if (qEl) qEl.textContent = `“${customLine}”`;
      }
    },

    /**
     * Signals that the underlying feed/content is ready.
     * The loader will NOT dismiss until at least 2000ms have elapsed since show().
     */
    ready: function(onDismissed) {
      isReadySignalReceived = true;
      const elapsed = Date.now() - startTime;
      const remaining = Math.max(0, 2000 - elapsed);

      clearTimeout(minDurationTimer);
      minDurationTimer = setTimeout(() => {
        if (!isShowing) return;
        if (overlayEl) {
          overlayEl.classList.add("fade-out");
          setTimeout(() => {
            overlayEl.style.display = "none";
            isShowing = false;
            if (typeof onDismissed === "function") onDismissed();
          }, 450);
        } else {
          isShowing = false;
          if (typeof onDismissed === "function") onDismissed();
        }
      }, remaining);
    },

    /**
     * Quick check if loader is actively covering screen.
     */
    isActive: function() {
      return isShowing;
    }
  };
})();
