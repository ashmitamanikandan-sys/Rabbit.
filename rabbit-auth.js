/**
 * RABBIT Redesigned Authentication View (Part 9)
 * "Your rabbit hole awaits."
 * Editorial, Gen Z-friendly, Obsidian Black with minimal violet lighting.
 * Simple "Back to Home", no Warren or Clubs navigation clutter.
 */
(function() {
  "use strict";

  function ensureStyles() {
    if (document.getElementById("rabbit-auth-style")) return;
    const style = document.createElement("style");
    style.id = "rabbit-auth-style";
    style.textContent = `
      .rabbit-auth-wrap {
        min-height: 100dvh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 30px 20px;
        background: #050505;
        background-image: radial-gradient(ellipse at 50% 20%, rgba(139, 92, 246, 0.14) 0%, rgba(5, 5, 5, 0.98) 70%);
        color: #F5F2F8;
      }
      .rabbit-auth-card {
        width: 100%;
        max-width: 420px;
        background: #111016;
        border: 1px solid rgba(167, 139, 250, 0.22);
        border-radius: 24px;
        padding: clamp(24px, 5vw, 36px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.7);
        text-align: center;
      }
      .rabbit-auth-logo {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin-bottom: 20px;
        display: inline-flex;
        align-items: baseline;
      }
      .rabbit-auth-logo .accent {
        color: #A78BFA;
      }
      .rabbit-auth-title {
        font-family: "Iowan Old Style", "Baskerville", Georgia, serif;
        font-size: 32px;
        line-height: 1.15;
        margin: 0 0 10px;
        font-weight: 600;
      }
      .rabbit-auth-subtitle {
        color: #A9A3B2;
        font-size: 14px;
        line-height: 1.5;
        margin: 0 0 24px;
      }
      .rabbit-auth-form {
        display: flex;
        flex-direction: column;
        gap: 14px;
        text-align: left;
      }
      .rabbit-auth-label {
        font-size: 12px;
        color: #A9A3B2;
        display: flex;
        flex-direction: column;
        gap: 6px;
      }
      .rabbit-auth-input {
        background: #09080E;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        padding: 13px 14px;
        color: #F5F2F8;
        font: inherit;
        outline: none;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
      }
      .rabbit-auth-input:focus {
        border-color: #A78BFA;
        box-shadow: 0 0 0 3px rgba(167, 139, 250, 0.15);
      }
      .rabbit-auth-btn {
        width: 100%;
        margin-top: 10px;
      }
      .rabbit-auth-switch {
        margin-top: 20px;
        font-size: 13px;
        color: #8E8899;
      }
      .rabbit-auth-switch button {
        background: none;
        border: none;
        color: #A78BFA;
        font-weight: 600;
        cursor: pointer;
        padding: 0 4px;
      }
      .rabbit-auth-back {
        margin-top: 24px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        color: #8E8899;
        font-size: 13px;
        text-decoration: none;
        background: none;
        border: none;
        cursor: pointer;
      }
      .rabbit-auth-back:hover {
        color: #D8C5FF;
      }
    `;
    document.head.appendChild(style);
  }

  function renderAuthView(container, isSignUp = false) {
    ensureStyles();
    container.innerHTML = "";

    const wrap = document.createElement("div");
    wrap.className = "rabbit-auth-wrap";

    wrap.innerHTML = `
      <div class="rabbit-auth-card">
        <div class="rabbit-auth-logo">RABBIT<span class="accent">.</span></div>
        <h1 class="rabbit-auth-title">Your rabbit hole awaits.</h1>
        <p class="rabbit-auth-subtitle">Good stories are better when they find their way back to you.</p>

        <form class="rabbit-auth-form" id="rabbit-auth-form">
          <label class="rabbit-auth-label">
            Email address
            <input type="email" class="rabbit-auth-input" id="rabbit-auth-email" placeholder="you@domain.com" required autocomplete="email">
          </label>
          <label class="rabbit-auth-label">
            Password
            <input type="password" class="rabbit-auth-input" id="rabbit-auth-pass" placeholder="••••••••" minlength="6" required autocomplete="current-password">
          </label>
          <button type="submit" class="rabbit-btn-primary rabbit-auth-btn">
            ${isSignUp ? "Create Account ↗" : "Sign In ↗"}
          </button>
        </form>

        <div class="rabbit-auth-switch">
          ${isSignUp ? "Already have a rabbit hole?" : "New to RABBIT?"}
          <button type="button" id="rabbit-auth-toggle-btn">
            ${isSignUp ? "Sign In" : "Create Account"}
          </button>
        </div>

        <button type="button" class="rabbit-auth-back" id="rabbit-auth-back-btn">
          ← Back to Home
        </button>
      </div>
    `;

    wrap.querySelector("#rabbit-auth-toggle-btn").onclick = () => {
      renderAuthView(container, !isSignUp);
    };

    wrap.querySelector("#rabbit-auth-back-btn").onclick = () => {
      if (window.RabbitNavigation) {
        window.RabbitNavigation.navigate("home");
      } else if (typeof renderHome === "function") {
        renderHome();
      }
    };

    wrap.querySelector("#rabbit-auth-form").onsubmit = (e) => {
      e.preventDefault();
      const email = wrap.querySelector("#rabbit-auth-email").value.trim();
      if (typeof toast === "function") toast(`Signed in as ${email} · Demo state active`);
      if (window.RabbitNavigation) window.RabbitNavigation.navigate("profile");
    };

    container.appendChild(wrap);
  }

  window.RabbitAuth = {
    render: renderAuthView
  };
})();
