/**
 * RABBIT Signature Profile Experience — "YOUR LITTLE UNIVERSE" (Parts 5 & 8)
 * Includes real-time dynamic Reading Constellation canvas, Saved Library,
 * Followed Books, and local persistence.
 */
(function() {
  "use strict";

  let profileContainer = null;
  let activeTab = "saved"; // "saved", "followed", "posts", "settings"
  let savedSubTab = "books"; // "books", "insights"
  let animFrameId = null;

  function getUserData() {
    let d = {
      name: "Curious Reader",
      username: "curious_reader",
      bio: "Following my curiosity, one chapter at a time.",
      avatar: ""
    };
    try {
      const v10 = JSON.parse(localStorage.getItem("rabbit_v10_local") || "{}");
      if (v10.name) d.name = v10.name;
      if (v10.bio) d.bio = v10.bio;
      if (v10.avatar) d.avatar = v10.avatar;
      const prof = JSON.parse(localStorage.getItem("rabbit_profile_data") || "{}");
      d = Object.assign(d, prof);
    } catch (e) {}
    return d;
  }

  function saveUserData(d) {
    try {
      localStorage.setItem("rabbit_profile_data", JSON.stringify(d));
      const v10 = JSON.parse(localStorage.getItem("rabbit_v10_local") || "{}");
      v10.name = d.name;
      v10.bio = d.bio;
      if (d.avatar) v10.avatar = d.avatar;
      localStorage.setItem("rabbit_v10_local", JSON.stringify(v10));
    } catch (e) {}
  }

  function getSavedBooks() {
    const list = [];
    try {
      // 1. From rabbit_catalog_saved
      const catSaved = JSON.parse(localStorage.getItem("rabbit_catalog_saved") || "[]");
      // 2. From individual rabbit_save_* keys
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && key.startsWith("rabbit_save_")) {
          const id = key.replace("rabbit_save_", "");
          if (!catSaved.includes(id)) catSaved.push(id);
        }
      }
      // 3. Resolve book objects from catalog or books array
      catSaved.forEach(id => {
        let b = null;
        if (typeof window.searchMasterworkCatalog === "function") {
          const matches = window.searchMasterworkCatalog(id);
          if (matches.length) b = matches[0];
        }
        if (!b && typeof books !== "undefined") {
          b = books.find(x => x.id === id || x.title === id);
        }
        if (b) list.push(b);
        else list.push({ id, title: id, author: "Curated Author", genre: "Curiosity" });
      });
    } catch (e) {}
    return list;
  }

  function getFollowedBooks() {
    const list = [];
    try {
      const followedIds = [];
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && key.startsWith("rabbit_follow_")) {
          followedIds.push(key.replace("rabbit_follow_", ""));
        }
      }
      const raw = JSON.parse(localStorage.getItem("followed") || "[]");
      raw.forEach(id => { if (!followedIds.includes(id)) followedIds.push(id); });

      followedIds.forEach(id => {
        let b = null;
        if (typeof window.searchMasterworkCatalog === "function") {
          const matches = window.searchMasterworkCatalog(id);
          if (matches.length) b = matches[0];
        }
        if (!b && typeof books !== "undefined") {
          b = books.find(x => x.id === id || x.title === id);
        }
        if (b) list.push(b);
        else list.push({ id, title: id, author: "Curated Author", genre: "Curiosity" });
      });
    } catch (e) {}
    return list;
  }

  function getSavedInsights() {
    const list = [];
    try {
      const savedIds = JSON.parse(localStorage.getItem("saved") || "[]");
      savedIds.forEach(id => {
        if (typeof postById === "function") {
          const p = postById(id);
          if (p) list.push(p);
        }
      });
    } catch (e) {}
    return list;
  }

  function ensureStyles() {
    if (document.getElementById("rabbit-profile-style")) return;
    const style = document.createElement("style");
    style.id = "rabbit-profile-style";
    style.textContent = `
      .rabbit-profile-view {
        max-width: 680px;
        margin: 0 auto;
        padding: 24px 18px 120px;
        color: #F5F2F8;
      }

      /* Constellation Hero Canvas Container */
      .rabbit-constellation-hero {
        position: relative;
        width: 100%;
        height: 240px;
        background: radial-gradient(ellipse at 50% 60%, rgba(20, 15, 30, 0.9) 0%, #050505 100%);
        border: 1px solid rgba(167, 139, 250, 0.2);
        border-radius: 24px;
        overflow: hidden;
        margin-bottom: 24px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.7);
      }
      .rabbit-constellation-canvas {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
      }
      .rabbit-constellation-badge {
        position: absolute;
        top: 14px;
        left: 16px;
        font-size: 10.5px;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #C4B5FD;
        background: rgba(18, 14, 25, 0.7);
        border: 1px solid rgba(167, 139, 250, 0.3);
        padding: 4px 10px;
        border-radius: 999px;
        backdrop-filter: blur(8px);
      }
      .rabbit-constellation-caption {
        position: absolute;
        bottom: 14px;
        left: 16px;
        right: 16px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
      }
      .rabbit-constellation-caption h4 {
        margin: 0 0 2px;
        font-size: 15px;
        color: #F5F2F8;
      }
      .rabbit-constellation-caption p {
        margin: 0;
        font-size: 12px;
        color: #A9A3B2;
      }

      /* Profile Header */
      .rabbit-profile-header {
        display: flex;
        gap: 20px;
        align-items: center;
        margin-bottom: 24px;
      }
      .rabbit-profile-avatar-wrap {
        position: relative;
        width: 82px;
        height: 82px;
        flex-shrink: 0;
      }
      .rabbit-profile-avatar {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: linear-gradient(135deg, #4C2882, #1E1235);
        border: 2px solid #A78BFA;
        display: grid;
        place-items: center;
        font-size: 32px;
        font-weight: 800;
        color: #F5F2F8;
        background-size: cover;
        background-position: center;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.25);
      }
      .rabbit-profile-avatar-input {
        position: absolute;
        inset: 0;
        opacity: 0;
        cursor: pointer;
      }
      .rabbit-profile-user-info {
        flex: 1;
        min-width: 0;
      }
      .rabbit-profile-name {
        margin: 0 0 4px;
        font-size: 22px;
        font-weight: 700;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .rabbit-profile-handle {
        color: #A78BFA;
        font-size: 13px;
        margin: 0 0 6px;
      }
      .rabbit-profile-bio {
        color: #A9A3B2;
        font-size: 13.5px;
        line-height: 1.5;
        margin: 0;
      }

      /* Activity Statistics Bar */
      .rabbit-profile-stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        background: #111015;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 14px 10px;
        margin-bottom: 24px;
        text-align: center;
      }
      .rabbit-stat-item strong {
        display: block;
        font-size: 20px;
        color: #F5F2F8;
        font-weight: 700;
      }
      .rabbit-stat-item span {
        font-size: 11px;
        color: #A9A3B2;
        letter-spacing: 0.04em;
        text-transform: uppercase;
      }

      /* Profile Navigation Tabs */
      .rabbit-profile-tabs {
        display: flex;
        gap: 8px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        padding-bottom: 12px;
        margin-bottom: 20px;
        overflow-x: auto;
      }
      .rabbit-profile-tab-btn {
        background: transparent;
        border: none;
        color: #8E8899;
        font-size: 14px;
        font-weight: 600;
        padding: 8px 14px;
        border-radius: 999px;
        cursor: pointer;
        transition: all 0.2s ease;
        white-space: nowrap;
      }
      .rabbit-profile-tab-btn:hover {
        color: #F5F2F8;
        background: rgba(255, 255, 255, 0.05);
      }
      .rabbit-profile-tab-btn.active {
        color: #0B0712;
        background: #A78BFA;
      }

      /* Library Sub-tabs (Books vs Insights) */
      .rabbit-sub-tabs {
        display: flex;
        gap: 8px;
        margin-bottom: 18px;
      }
      .rabbit-sub-tab-btn {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #A9A3B2;
        font-size: 12px;
        font-weight: 600;
        padding: 6px 14px;
        border-radius: 999px;
        cursor: pointer;
      }
      .rabbit-sub-tab-btn.active {
        background: rgba(167, 139, 250, 0.2);
        border-color: #A78BFA;
        color: #F5F2F8;
      }

      /* Book & Insight Grid */
      .rabbit-profile-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
        gap: 14px;
      }
      .rabbit-profile-book-card {
        background: #131217;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 10px;
        display: flex;
        flex-direction: column;
        transition: transform 0.2s ease, border-color 0.2s ease;
      }
      .rabbit-profile-book-card:hover {
        transform: translateY(-2px);
        border-color: rgba(167, 139, 250, 0.4);
      }
      .rabbit-profile-book-cover {
        aspect-ratio: 2/3;
        width: 100%;
        border-radius: 8px;
        object-fit: cover;
        background: #201A2B;
        margin-bottom: 8px;
      }
      .rabbit-profile-book-title {
        font-size: 13px;
        font-weight: 600;
        line-height: 1.3;
        margin: 0 0 4px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .rabbit-profile-book-author {
        font-size: 11px;
        color: #A9A3B2;
        margin: 0 0 10px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .rabbit-profile-book-actions {
        display: flex;
        gap: 6px;
        margin-top: auto;
      }
      .rabbit-profile-book-btn {
        flex: 1;
        font-size: 11px;
        padding: 6px 4px;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        background: rgba(255, 255, 255, 0.04);
        color: #ddd;
        cursor: pointer;
        text-align: center;
      }
      .rabbit-profile-book-btn.primary-action {
        background: rgba(167, 139, 250, 0.18);
        border-color: rgba(167, 139, 250, 0.4);
        color: #E9D5FF;
      }

      /* Empty State */
      .rabbit-profile-empty {
        text-align: center;
        padding: 50px 20px;
        border: 1px dashed rgba(167, 139, 250, 0.25);
        border-radius: 18px;
        color: #A9A3B2;
      }
      .rabbit-profile-empty h3 {
        margin: 0 0 8px;
        color: #F5F2F8;
      }

      /* Edit Profile / Settings Form */
      .rabbit-settings-form {
        display: flex;
        flex-direction: column;
        gap: 16px;
        background: #111016;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 22px;
      }
      .rabbit-settings-label {
        display: flex;
        flex-direction: column;
        gap: 6px;
        font-size: 13px;
        color: #A9A3B2;
      }
      .rabbit-settings-input, .rabbit-settings-textarea {
        background: #09080D;
        border: 1px solid rgba(167, 139, 250, 0.25);
        border-radius: 12px;
        padding: 12px 14px;
        color: #F5F2F8;
        font: inherit;
        outline: none;
      }
      .rabbit-settings-input:focus, .rabbit-settings-textarea:focus {
        border-color: #A78BFA;
      }
      .rabbit-settings-textarea {
        min-height: 80px;
        resize: vertical;
      }
      .rabbit-settings-actions {
        display: flex;
        gap: 10px;
        margin-top: 10px;
      }
    `;
    document.head.appendChild(style);
  }

  function startConstellationCanvas(canvas) {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    let width = canvas.width = canvas.offsetWidth;
    let height = canvas.height = canvas.offsetHeight;

    window.addEventListener("resize", () => {
      if (!canvas || !canvas.offsetWidth) return;
      width = canvas.width = canvas.offsetWidth;
      height = canvas.height = canvas.offsetHeight;
    });

    // Generate stars based on user's reading interests and activity
    const userGenres = Array.from(window.rabbitSelectedGenres || ["The Human Mind", "Philosophy"]);
    const savedCount = getSavedBooks().length;
    const followedCount = getFollowedBooks().length;

    // Background drifting stars
    const numStars = 60;
    const stars = [];
    for (let i = 0; i < numStars; i++) {
      stars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        r: Math.random() * 1.2 + 0.4,
        alpha: Math.random() * 0.7 + 0.2,
        speed: (Math.random() * 0.15 + 0.05)
      });
    }

    // Main constellation nodes (shaped by genres)
    const nodeCount = Math.max(5, Math.min(10, userGenres.length + Math.min(4, savedCount + followedCount)));
    const nodes = [];
    for (let i = 0; i < nodeCount; i++) {
      const angle = (i / nodeCount) * Math.PI * 2 + (Math.sin(i * 1.5) * 0.4);
      const rad = 45 + (i % 3) * 25 + Math.random() * 15;
      nodes.push({
        x: width / 2 + Math.cos(angle) * rad * (width / 260),
        y: height / 2 + Math.sin(angle) * (rad * 0.6),
        name: userGenres[i % userGenres.length] || "Curiosity",
        pulse: Math.random() * Math.PI,
        size: (i === 0 || i === 2) ? 4.2 : 2.8
      });
    }

    function renderFrame() {
      ctx.clearRect(0, 0, width, height);

      // 1. Draw subtle background stars
      stars.forEach(s => {
        s.y -= s.speed;
        if (s.y < 0) {
          s.y = height;
          s.x = Math.random() * width;
        }
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(216, 197, 255, ${s.alpha})`;
        ctx.fill();
      });

      // 2. Draw delicate connecting lines
      ctx.beginPath();
      for (let i = 0; i < nodes.length; i++) {
        const next = nodes[(i + 1) % nodes.length];
        ctx.moveTo(nodes[i].x, nodes[i].y);
        ctx.lineTo(next.x, next.y);
      }
      // Add a couple of cross-links
      if (nodes.length > 4) {
        ctx.moveTo(nodes[0].x, nodes[0].y);
        ctx.lineTo(nodes[3].x, nodes[3].y);
      }
      ctx.strokeStyle = "rgba(167, 139, 250, 0.28)";
      ctx.lineWidth = 1;
      ctx.stroke();

      // 3. Draw luminous constellation stars with soft violet glow
      nodes.forEach(n => {
        n.pulse += 0.035;
        const glow = Math.sin(n.pulse) * 0.3 + 0.7;

        // Outer glow
        const grad = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, n.size * 3.5);
        grad.addColorStop(0, `rgba(167, 139, 250, ${0.45 * glow})`);
        grad.addColorStop(1, "rgba(167, 139, 250, 0)");
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.size * 3.5, 0, Math.PI * 2);
        ctx.fillStyle = grad;
        ctx.fill();

        // Core star
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.size, 0, Math.PI * 2);
        ctx.fillStyle = "#FFFFFF";
        ctx.fill();
      });

      animFrameId = requestAnimationFrame(renderFrame);
    }

    renderFrame();
  }

  function renderProfileView(container) {
    ensureStyles();
    container.innerHTML = "";

    const user = getUserData();
    const savedBooks = getSavedBooks();
    const followedBooks = getFollowedBooks();
    const savedInsights = getSavedInsights();

    const view = document.createElement("div");
    view.className = "rabbit-profile-view";

    // 1. Constellation Hero Canvas
    const hero = document.createElement("div");
    hero.className = "rabbit-constellation-hero";
    hero.innerHTML = `
      <canvas class="rabbit-constellation-canvas" id="rabbit-constellation-canvas"></canvas>
      <div class="rabbit-constellation-badge">✦ READING CONSTELLATION</div>
      <div class="rabbit-constellation-caption">
        <div>
          <h4>Your Little Universe</h4>
          <p>Shaped by your curiosity, saved masterworks, and followed authors</p>
        </div>
      </div>
    `;
    view.appendChild(hero);

    // 2. Profile Header
    const header = document.createElement("div");
    header.className = "rabbit-profile-header";
    header.innerHTML = `
      <div class="rabbit-profile-avatar-wrap">
        <div class="rabbit-profile-avatar" id="rabbit-profile-avatar-display" ${user.avatar ? `style="background-image:url(${user.avatar});color:transparent;"` : ''}>
          ${user.avatar ? '' : (user.name.charAt(0).toUpperCase() || 'R')}
        </div>
        <input type="file" accept="image/*" class="rabbit-profile-avatar-input" id="rabbit-avatar-upload" title="Change profile photo" aria-label="Change profile photo">
      </div>
      <div class="rabbit-profile-user-info">
        <h2 class="rabbit-profile-name">${escapeHtml(user.name)}</h2>
        <div class="rabbit-profile-handle">@${escapeHtml(user.username)}</div>
        <p class="rabbit-profile-bio">${escapeHtml(user.bio)}</p>
      </div>
    `;
    view.appendChild(header);

    // Avatar upload handler
    const uploadInput = header.querySelector("#rabbit-avatar-upload");
    uploadInput.onchange = (e) => {
      const file = e.target.files && e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        user.avatar = reader.result;
        saveUserData(user);
        renderProfileView(container);
      };
      reader.readAsDataURL(file);
    };

    // 3. Activity Statistics Bar
    const stats = document.createElement("div");
    stats.className = "rabbit-profile-stats";
    stats.innerHTML = `
      <div class="rabbit-stat-item">
        <strong>${savedBooks.length + savedInsights.length}</strong>
        <span>Saved Items</span>
      </div>
      <div class="rabbit-stat-item">
        <strong>${followedBooks.length}</strong>
        <span>Followed</span>
      </div>
      <div class="rabbit-stat-item">
        <strong>${(window.rabbitSelectedGenres ? window.rabbitSelectedGenres.size : 1)}</strong>
        <span>Rabbit Holes</span>
      </div>
    `;
    view.appendChild(stats);

    // 4. Profile Navigation Tabs
    const tabs = document.createElement("div");
    tabs.className = "rabbit-profile-tabs";
    tabs.innerHTML = `
      <button type="button" class="rabbit-profile-tab-btn ${activeTab === 'saved' ? 'active' : ''}" data-tab="saved">Saved Library</button>
      <button type="button" class="rabbit-profile-tab-btn ${activeTab === 'followed' ? 'active' : ''}" data-tab="followed">Followed Books</button>
      <button type="button" class="rabbit-profile-tab-btn ${activeTab === 'settings' ? 'active' : ''}" data-tab="settings">Edit Profile</button>
    `;
    tabs.querySelectorAll(".rabbit-profile-tab-btn").forEach(btn => {
      btn.onclick = () => {
        activeTab = btn.dataset.tab;
        renderProfileView(container);
      };
    });
    view.appendChild(tabs);

    // 5. Tab Content Panel
    const panel = document.createElement("div");
    panel.className = "rabbit-profile-panel";

    if (activeTab === "saved") {
      // Sub-tabs for Books vs Insights
      const subTabs = document.createElement("div");
      subTabs.className = "rabbit-sub-tabs";
      subTabs.innerHTML = `
        <button type="button" class="rabbit-sub-tab-btn ${savedSubTab === 'books' ? 'active' : ''}" id="rabbit-sub-books">Saved Books (${savedBooks.length})</button>
        <button type="button" class="rabbit-sub-tab-btn ${savedSubTab === 'insights' ? 'active' : ''}" id="rabbit-sub-insights">Saved Insights (${savedInsights.length})</button>
      `;
      subTabs.querySelector("#rabbit-sub-books").onclick = () => {
        savedSubTab = "books";
        renderProfileView(container);
      };
      subTabs.querySelector("#rabbit-sub-insights").onclick = () => {
        savedSubTab = "insights";
        renderProfileView(container);
      };
      panel.appendChild(subTabs);

      if (savedSubTab === "books") {
        if (savedBooks.length === 0) {
          panel.innerHTML += `
            <div class="rabbit-profile-empty">
              <h3>Your library is waiting</h3>
              <p>Save masterworks from your feed by tapping the "◇ Save" button on any card.</p>
            </div>
          `;
        } else {
          const grid = document.createElement("div");
          grid.className = "rabbit-profile-grid";
          savedBooks.forEach(b => {
            const card = document.createElement("article");
            card.className = "rabbit-profile-book-card";
            card.innerHTML = `
              <img src="${b.cover_url || b.cover || 'https://covers.openlibrary.org/b/id/8231998-M.jpg'}" alt="${escapeHtml(b.title)}" class="rabbit-profile-book-cover" loading="lazy">
              <h4 class="rabbit-profile-book-title">${escapeHtml(b.title)}</h4>
              <p class="rabbit-profile-book-author">${escapeHtml(b.author || 'Curator')}</p>
              <div class="rabbit-profile-book-actions">
                <button type="button" class="rabbit-profile-book-btn primary-action open-btn">Read ↗</button>
                <button type="button" class="rabbit-profile-book-btn remove-btn" title="Remove from Library">✕</button>
              </div>
            `;
            card.querySelector(".open-btn").onclick = () => {
              if (typeof rabbitReader === "function") rabbitReader(b);
              else if (typeof openBook === "function") openBook(b);
            };
            card.querySelector(".remove-btn").onclick = () => {
              try {
                localStorage.removeItem("rabbit_save_" + (b.id || b.title));
                const catSaved = JSON.parse(localStorage.getItem("rabbit_catalog_saved") || "[]").filter(x => x !== b.id);
                localStorage.setItem("rabbit_catalog_saved", JSON.stringify(catSaved));
              } catch (e) {}
              renderProfileView(container);
            };
            grid.appendChild(card);
          });
          panel.appendChild(grid);
        }
      } else {
        // Saved Insights
        if (savedInsights.length === 0) {
          panel.innerHTML += `
            <div class="rabbit-profile-empty">
              <h3>No saved insights yet</h3>
              <p>Bookmark individual chapter ideas and commentary to review them here anytime.</p>
            </div>
          `;
        } else {
          const grid = document.createElement("div");
          grid.className = "rabbit-profile-grid";
          savedInsights.forEach(p => {
            const card = document.createElement("article");
            card.className = "rabbit-profile-book-card";
            card.innerHTML = `
              <img src="${p.book.cover}" alt="${escapeHtml(p.book.title)}" class="rabbit-profile-book-cover" loading="lazy">
              <h4 class="rabbit-profile-book-title">${escapeHtml(p.book.title)}</h4>
              <p class="rabbit-profile-book-author">Chapter ${p.chapter[0]} · ${escapeHtml(p.chapter[1])}</p>
              <div class="rabbit-profile-book-actions">
                <button type="button" class="rabbit-profile-book-btn primary-action open-btn">View ↗</button>
                <button type="button" class="rabbit-profile-book-btn remove-btn">✕</button>
              </div>
            `;
            card.querySelector(".open-btn").onclick = () => {
              if (typeof enterFeed === "function") enterFeed(p.id);
            };
            card.querySelector(".remove-btn").onclick = () => {
              try {
                let savedArr = JSON.parse(localStorage.getItem("saved") || "[]").filter(x => x !== p.id);
                localStorage.setItem("saved", JSON.stringify(savedArr));
              } catch (e) {}
              renderProfileView(container);
            };
            grid.appendChild(card);
          });
          panel.appendChild(grid);
        }
      }
    } else if (activeTab === "followed") {
      if (followedBooks.length === 0) {
        panel.innerHTML = `
          <div class="rabbit-profile-empty">
            <h3>No followed books yet</h3>
            <p>Tap "♡ Follow book" on any feed card to stay connected with its ideas.</p>
          </div>
        `;
      } else {
        const grid = document.createElement("div");
        grid.className = "rabbit-profile-grid";
        followedBooks.forEach(b => {
          const card = document.createElement("article");
          card.className = "rabbit-profile-book-card";
          card.innerHTML = `
            <img src="${b.cover_url || b.cover || 'https://covers.openlibrary.org/b/id/8231998-M.jpg'}" alt="${escapeHtml(b.title)}" class="rabbit-profile-book-cover" loading="lazy">
            <h4 class="rabbit-profile-book-title">${escapeHtml(b.title)}</h4>
            <p class="rabbit-profile-book-author">${escapeHtml(b.author || 'Curator')}</p>
            <div class="rabbit-profile-book-actions">
              <button type="button" class="rabbit-profile-book-btn primary-action open-btn">Explore ↗</button>
              <button type="button" class="rabbit-profile-book-btn remove-btn" title="Unfollow">✕</button>
            </div>
          `;
          card.querySelector(".open-btn").onclick = () => {
            if (typeof rabbitReader === "function") rabbitReader(b);
            else if (typeof openBook === "function") openBook(b);
          };
          card.querySelector(".remove-btn").onclick = () => {
            try {
              localStorage.removeItem("rabbit_follow_" + (b.id || b.title));
              let fl = JSON.parse(localStorage.getItem("followed") || "[]").filter(x => x !== b.id);
              localStorage.setItem("followed", JSON.stringify(fl));
            } catch (e) {}
            renderProfileView(container);
          };
          grid.appendChild(card);
        });
        panel.appendChild(grid);
      }
    } else if (activeTab === "settings") {
      panel.innerHTML = `
        <form class="rabbit-settings-form" id="rabbit-profile-edit-form">
          <label class="rabbit-settings-label">
            Display Name
            <input type="text" class="rabbit-settings-input" id="rabbit-edit-name" value="${escapeHtml(user.name)}" maxlength="50" required>
          </label>
          <label class="rabbit-settings-label">
            Username
            <input type="text" class="rabbit-settings-input" id="rabbit-edit-username" value="${escapeHtml(user.username)}" maxlength="30" required>
          </label>
          <label class="rabbit-settings-label">
            Bio
            <textarea class="rabbit-settings-textarea" id="rabbit-edit-bio" maxlength="200">${escapeHtml(user.bio)}</textarea>
          </label>
          <div class="rabbit-settings-actions">
            <button type="submit" class="rabbit-btn-primary" style="flex:1;">Save Profile ↗</button>
          </div>
          <hr style="border:none;border-top:1px solid rgba(255,255,255,0.08);margin:16px 0;">
          <div style="display:flex;justify-content:space-between;align-items:center;">
            <div>
              <strong style="font-size:13px;display:block;">Development Mode</strong>
              <small style="color:#A9A3B2;">Reset onboarding without losing your saved books</small>
            </div>
            <button type="button" class="rabbit-btn-secondary" id="rabbit-reset-onboarding-btn">Reset Onboarding</button>
          </div>
        </form>
      `;

      const form = panel.querySelector("#rabbit-profile-edit-form");
      form.onsubmit = (e) => {
        e.preventDefault();
        user.name = panel.querySelector("#rabbit-edit-name").value.trim();
        user.username = panel.querySelector("#rabbit-edit-username").value.trim().replace(/^@/, "");
        user.bio = panel.querySelector("#rabbit-edit-bio").value.trim();
        saveUserData(user);
        if (typeof toast === "function") toast("Profile saved! ✦");
        renderProfileView(container);
      };

      const resetBtn = panel.querySelector("#rabbit-reset-onboarding-btn");
      resetBtn.onclick = () => {
        if (confirm("Reset onboarding? This lets you test the welcome and genre picker again. Your saved books and library remain safe.")) {
          localStorage.removeItem("rabbit_onboarding_completed");
          window.location.reload();
        }
      };
    }

    view.appendChild(panel);
    container.appendChild(view);

    // Launch the Constellation Canvas animation
    const canvas = view.querySelector("#rabbit-constellation-canvas");
    startConstellationCanvas(canvas);
  }

  function escapeHtml(str) {
    if (!str) return "";
    return String(str).replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[m]);
  }

  window.RabbitProfile = {
    render: function(container) {
      if (animFrameId) cancelAnimationFrame(animFrameId);
      profileContainer = container;
      renderProfileView(container);
    }
  };
})();
