/**
 * RABBIT Unified Community Views (Parts 6 & 7)
 * Unifies Warren (social community feed) and Clubs (reading clubs & chats)
 * within the single Obsidian Black × Cosmic Violet design system and shared navigation.
 */
(function() {
  "use strict";

  // Warren Demo Data & Storage
  const STORAGE_KEY = "rabbit_v10_local";
  function getWarrenData() {
    let data;
    try { data = JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; } catch(e) { data = {}; }
    if (!Array.isArray(data.warren)) data.warren = [];
    
    // Seed initial demo thoughts if empty
    if (!data.warrenDemoSeeded) {
      const demo = [
        {
          id: "demo-48",
          name: "Mira",
          category: "Favourite moments",
          book: "The 48 Laws of Power",
          body: "I finally started The 48 Laws of Power and Law 4 — Always Say Less Than Necessary — actually made me pause. Explaining yourself too much often gives away your confidence. It got me thinking about how we communicate online. Thoughts?",
          image: "https://covers.openlibrary.org/b/isbn/9780140280197-L.jpg",
          likes: 38,
          replies: [
            { id: "demo-r1", name: "Aanya", text: "Highlighted that exact law! Small shifts in habit make a massive difference." }
          ],
          created: Date.now() - 3600000 * 3,
          demo: true
        },
        {
          id: "demo-atomic",
          name: "Arjun",
          category: "What I learned",
          book: "Atomic Habits",
          body: "A tiny idea from Atomic Habits that stuck with me: instead of obsessing over a giant goal, focus on the kind of person you're becoming. Reading just 10 pages before bed changed my entire evening routine. 🐇",
          image: "https://covers.openlibrary.org/b/isbn/9780735211292-L.jpg",
          likes: 72,
          replies: [
            { id: "demo-r2", name: "Dev", text: "Consistency always beats intensity in reading." }
          ],
          created: Date.now() - 3600000 * 12,
          demo: true
        },
        {
          id: "demo-psych",
          name: "Nila",
          category: "Book suggestions",
          book: "The Psychology of Money",
          body: "If you want a book that changes how you think about wealth without feeling like a boring spreadsheet, pick this up. It's really about human behavior and ego.",
          image: "https://covers.openlibrary.org/b/isbn/9780857197689-L.jpg",
          likes: 46,
          replies: [],
          created: Date.now() - 3600000 * 20,
          demo: true
        }
      ];
      demo.forEach(p => data.warren.push(p));
      data.warrenDemoSeeded = true;
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(data)); } catch(e) {}
    }
    return data;
  }

  function saveWarrenData(d) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(d)); } catch(e) {}
  }

  // Clubs Data & Storage
  const CLUBS_KEY = "rabbit_clubs_v1";
  function getClubsData() {
    let state;
    try { state = JSON.parse(localStorage.getItem(CLUBS_KEY)) || {}; } catch(e) { state = {}; }
    const seeds = [
      {
        id: "midnight",
        name: "The Midnight Readers",
        emoji: "🌙",
        desc: "One more chapter at 2 AM? You're home.",
        members: 128,
        topic: "Literary fiction",
        demo: true,
        posts: [
          { id: "m1", by: "Mira", text: "I finished our latest pick and I NEED to discuss that ending!", likes: 23, replies: [] }
        ],
        chats: {
          general: [{ by: "Mira", text: "Hey night owls! What are we reading tonight?" }],
          "book-talk": [{ by: "Aanya", text: "What's our next group read?" }],
          spoilers: []
        }
      },
      {
        id: "mind",
        name: "Mind Games",
        emoji: "🧠",
        desc: "Psychology, brain science and strange human behaviour.",
        members: 96,
        topic: "Psychology",
        demo: true,
        posts: [
          { id: "p1", by: "Arjun", text: "Question: do we remember an event, or the last time we remembered it?", likes: 31, replies: [] }
        ],
        chats: {
          general: [{ by: "Arjun", text: "Share a fascinating cognitive bias!" }],
          "book-talk": [],
          spoilers: []
        }
      },
      {
        id: "twist",
        name: "Plot Twist Society",
        emoji: "🕵️",
        desc: "Mysteries, theories and suspicious side characters.",
        members: 211,
        topic: "Mystery & thriller",
        demo: true,
        posts: [
          { id: "t1", by: "Ishita", text: "I KNEW that secondary character was hiding something!", likes: 42, replies: [] }
        ],
        chats: { general: [], "book-talk": [], spoilers: [] }
      },
      {
        id: "worlds",
        name: "Between Worlds",
        emoji: "🪄",
        desc: "Fantasy worlds and characters we wish were real.",
        members: 174,
        topic: "Fantasy",
        demo: true,
        posts: [],
        chats: { general: [], "book-talk": [], spoilers: [] }
      }
    ];
    if (!Array.isArray(state.clubs)) state.clubs = seeds;
    if (!Array.isArray(state.joined)) state.joined = ["midnight"];
    return state;
  }

  function saveClubsData(s) {
    try { localStorage.setItem(CLUBS_KEY, JSON.stringify(s)); } catch(e) {}
  }

  function ensureStyles() {
    if (document.getElementById("rabbit-community-style")) return;
    const style = document.createElement("style");
    style.id = "rabbit-community-style";
    style.textContent = `
      .rabbit-community-view {
        max-width: 680px;
        margin: 0 auto;
        padding: 24px 18px 120px;
        color: #F5F2F8;
      }
      .rabbit-community-header {
        margin-bottom: 24px;
      }
      .rabbit-community-eyebrow {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #A78BFA;
        margin-bottom: 6px;
      }
      .rabbit-community-title {
        font-family: "Iowan Old Style", "Baskerville", Georgia, serif;
        font-size: clamp(28px, 5vw, 36px);
        margin: 0 0 8px;
        font-weight: 600;
      }
      .rabbit-community-subtitle {
        color: #A9A3B2;
        font-size: 14px;
        margin: 0;
        line-height: 1.5;
      }

      /* Stories Rail in Community Header */
      .rabbit-community-stories-rail {
        display: flex;
        overflow-x: auto;
        gap: 14px;
        padding: 12px 0 16px;
        margin-bottom: 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      }

      /* Warren Post Card */
      .rabbit-warren-card {
        background: #111016;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 18px;
        transition: border-color 0.2s ease, transform 0.2s ease;
      }
      .rabbit-warren-card:hover {
        border-color: rgba(167, 139, 250, 0.3);
      }
      .rabbit-warren-top {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 14px;
      }
      .rabbit-warren-avatar {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: linear-gradient(135deg, #4C2882, #23163E);
        border: 1.5px solid #A78BFA;
        display: grid;
        place-items: center;
        font-size: 18px;
        font-weight: 700;
        color: #F5F2F8;
      }
      .rabbit-warren-meta h4 {
        margin: 0 0 2px;
        font-size: 14px;
        font-weight: 600;
      }
      .rabbit-warren-meta span {
        font-size: 11px;
        color: #8E8899;
      }
      .rabbit-warren-tag {
        margin-left: auto;
        font-size: 10.5px;
        padding: 3px 10px;
        border-radius: 999px;
        background: rgba(167, 139, 250, 0.12);
        color: #C4B5FD;
        border: 1px solid rgba(167, 139, 250, 0.25);
      }
      .rabbit-warren-book-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 8px;
        padding: 6px 10px;
        font-size: 12px;
        color: #D8C5FF;
        margin-bottom: 12px;
      }
      .rabbit-warren-body {
        font-size: 15px;
        line-height: 1.65;
        color: #E2DFE8;
        margin: 0 0 16px;
        white-space: pre-wrap;
      }
      .rabbit-warren-image {
        width: 100%;
        max-height: 380px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
      }

      /* Warren Action Buttons (Like, Comments, Share) with comfortable spacing */
      .rabbit-warren-actions {
        display: flex;
        align-items: center;
        gap: 18px;
        padding-top: 14px;
        border-top: 1px solid rgba(255, 255, 255, 0.07);
      }
      .rabbit-warren-act-btn {
        background: transparent;
        border: none;
        color: #A9A3B2;
        font-size: 13px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        cursor: pointer;
        padding: 6px 8px;
        border-radius: 8px;
        transition: color 0.18s ease;
      }
      .rabbit-warren-act-btn:hover {
        color: #F5F2F8;
      }
      .rabbit-warren-act-btn.active {
        color: #A78BFA;
      }

      /* Post Composer Fab / Card */
      .rabbit-warren-compose-card {
        background: #14131A;
        border: 1px solid rgba(167, 139, 250, 0.25);
        border-radius: 18px;
        padding: 16px;
        margin-bottom: 22px;
      }
      .rabbit-warren-compose-input {
        width: 100%;
        background: #09080E;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 12px 14px;
        color: #F5F2F8;
        font: inherit;
        resize: vertical;
        min-height: 70px;
        box-sizing: border-box;
        margin-bottom: 12px;
        outline: none;
      }
      .rabbit-warren-compose-input:focus {
        border-color: #A78BFA;
      }

      /* Clubs Cards */
      .rabbit-club-card {
        background: #121116;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 16px;
        display: flex;
        gap: 16px;
        align-items: center;
        transition: border-color 0.2s ease, transform 0.2s ease;
      }
      .rabbit-club-card:hover {
        border-color: rgba(167, 139, 250, 0.35);
        transform: translateY(-2px);
      }
      .rabbit-club-emoji {
        width: 54px;
        height: 54px;
        border-radius: 16px;
        background: rgba(167, 139, 250, 0.14);
        border: 1px solid rgba(167, 139, 250, 0.3);
        display: grid;
        place-items: center;
        font-size: 26px;
        flex-shrink: 0;
      }
      .rabbit-club-info {
        flex: 1;
        min-width: 0;
      }
      .rabbit-club-info h3 {
        margin: 0 0 4px;
        font-size: 16px;
        font-weight: 700;
      }
      .rabbit-club-info p {
        margin: 0 0 6px;
        font-size: 13px;
        color: #A9A3B2;
        line-height: 1.4;
      }
      .rabbit-club-meta {
        font-size: 11px;
        color: #8E8899;
      }
    `;
    document.head.appendChild(style);
  }

  function renderWarrenView(container) {
    ensureStyles();
    container.innerHTML = "";

    const warrenData = getWarrenData();
    const view = document.createElement("div");
    view.className = "rabbit-community-view";

    // Header
    const header = document.createElement("div");
    header.className = "rabbit-community-header";
    header.innerHTML = `
      <div class="rabbit-community-eyebrow">RABBIT / THE SOCIAL BURROW</div>
      <h1 class="rabbit-community-title">The Warren ✦</h1>
      <p class="rabbit-community-subtitle">A place for the moments, book discoveries, and thoughts that stay with us.</p>
    `;
    view.appendChild(header);

    // Followed Books / Stories Rail
    const storiesRail = document.createElement("div");
    storiesRail.className = "rabbit-community-stories-rail";
    let followedList = [];
    if (typeof books !== "undefined") {
      followedList = books.slice(0, 10);
    }
    followedList.forEach(b => {
      const item = document.createElement("div");
      item.style.cssText = "display:flex;flex-direction:column;align-items:center;width:64px;cursor:pointer;flex-shrink:0;";
      item.innerHTML = `
        <img src="${b.cover}" alt="${b.title}" style="width:54px;height:54px;border-radius:50%;object-fit:cover;border:2px solid #8B5CF6;box-shadow:0 4px 12px rgba(0,0,0,0.5);">
        <span style="font-size:10px;color:#A9A3B2;margin-top:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;width:100%;text-align:center;">${b.title}</span>
      `;
      item.onclick = () => {
        if (typeof openStory === "function") openStory(b.id);
        else if (typeof rabbitReader === "function") rabbitReader(b);
      };
      storiesRail.appendChild(item);
    });
    view.appendChild(storiesRail);

    // Fast Post Composer
    const composer = document.createElement("div");
    composer.className = "rabbit-warren-compose-card";
    composer.innerHTML = `
      <textarea class="rabbit-warren-compose-input" placeholder="Share a line, a book discovery, or a question with readers…" id="rabbit-warren-post-text"></textarea>
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <span style="font-size:11px;color:#7A7485;">Demo community · saved in browser</span>
        <button type="button" class="rabbit-btn-primary" id="rabbit-warren-submit-btn" style="padding:8px 18px;font-size:13px;">Post ↗</button>
      </div>
    `;
    const submitBtn = composer.querySelector("#rabbit-warren-submit-btn");
    submitBtn.onclick = () => {
      const text = composer.querySelector("#rabbit-warren-post-text").value.trim();
      if (!text) return;
      warrenData.warren.unshift({
        id: "post-" + Date.now(),
        name: "You",
        category: "Discovery",
        book: "",
        body: text,
        likes: 0,
        replies: [],
        created: Date.now(),
        demo: false
      });
      saveWarrenData(warrenData);
      renderWarrenView(container);
    };
    view.appendChild(composer);

    // Continuous Feed
    const feed = document.createElement("div");
    feed.className = "rabbit-warren-feed";

    warrenData.warren.forEach(p => {
      const card = document.createElement("article");
      card.className = "rabbit-warren-card";

      card.innerHTML = `
        <div class="rabbit-warren-top">
          <div class="rabbit-warren-avatar">${(p.name || 'R').charAt(0).toUpperCase()}</div>
          <div class="rabbit-warren-meta">
            <h4>${escapeHtml(p.name || 'Curious Reader')}</h4>
            <span>${p.demo ? 'Demo reader' : 'Your post'} · ${timeAgo(p.created)}</span>
          </div>
          <span class="rabbit-warren-tag">${escapeHtml(p.category || 'Post')}</span>
        </div>
        ${p.book ? `<div class="rabbit-warren-book-badge">↗ ${escapeHtml(p.book)}</div>` : ''}
        <p class="rabbit-warren-body">${escapeHtml(p.body)}</p>
        ${p.image ? `<img src="${p.image}" alt="Attached photo" class="rabbit-warren-image" loading="lazy">` : ''}
        
        <!-- Action Row with Comfortable Spacing -->
        <div class="rabbit-warren-actions">
          <button type="button" class="rabbit-warren-act-btn ${p.liked ? 'active' : ''} like-btn">
            ${p.liked ? '♥' : '♡'} <span>${p.likes + (p.liked ? 1 : 0)}</span>
          </button>
          <button type="button" class="rabbit-warren-act-btn reply-btn">
            ↩ <span>${(p.replies || []).length} Replies</span>
          </button>
          <button type="button" class="rabbit-warren-act-btn share-btn" style="margin-left:auto;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>
            <span>Share</span>
          </button>
        </div>
      `;

      // Actions event handlers
      const likeBtn = card.querySelector(".like-btn");
      likeBtn.onclick = () => {
        p.liked = !p.liked;
        saveWarrenData(warrenData);
        likeBtn.classList.toggle("active", p.liked);
        likeBtn.querySelector("span").textContent = p.likes + (p.liked ? 1 : 0);
      };

      const shareBtn = card.querySelector(".share-btn");
      shareBtn.onclick = () => {
        if (typeof window.rabbitShareBook === "function") {
          window.rabbitShareBook({ title: p.book || "Warren Conversation", author: p.name });
        } else if (navigator.share) {
          navigator.share({ title: "RABBIT Warren", text: p.body, url: location.href }).catch(() => {});
        } else {
          navigator.clipboard.writeText(location.href).then(() => { if (typeof toast === "function") toast("Link copied! ↗"); });
        }
      };

      feed.appendChild(card);
    });

    view.appendChild(feed);
    container.appendChild(view);
  }

  function renderClubsView(container) {
    ensureStyles();
    container.innerHTML = "";

    const clubsData = getClubsData();
    const view = document.createElement("div");
    view.className = "rabbit-community-view";

    view.innerHTML = `
      <div class="rabbit-community-header">
        <div class="rabbit-community-eyebrow">RABBIT / READING COLLECTIVES</div>
        <h1 class="rabbit-community-title">Clubs ✦</h1>
        <p class="rabbit-community-subtitle">Find your people between the pages. Read together, share theories, and stay for the conversations.</p>
      </div>
      <div id="rabbit-clubs-list"></div>
    `;

    const list = view.querySelector("#rabbit-clubs-list");
    clubsData.clubs.forEach(c => {
      const isJoined = clubsData.joined.includes(c.id);
      const card = document.createElement("article");
      card.className = "rabbit-club-card";
      card.innerHTML = `
        <div class="rabbit-club-emoji">${c.emoji}</div>
        <div class="rabbit-club-info">
          <h3>${escapeHtml(c.name)}</h3>
          <p>${escapeHtml(c.desc)}</p>
          <span class="rabbit-club-meta">${escapeHtml(c.topic)} · ${c.members + (isJoined ? 1 : 0)} demo members</span>
        </div>
        <button type="button" class="rabbit-btn-secondary join-btn" style="flex-shrink:0;">
          ${isJoined ? 'Joined ✓' : 'Join +'}
        </button>
      `;

      const joinBtn = card.querySelector(".join-btn");
      joinBtn.onclick = () => {
        if (isJoined) {
          clubsData.joined = clubsData.joined.filter(x => x !== c.id);
        } else {
          clubsData.joined.push(c.id);
        }
        saveClubsData(clubsData);
        renderClubsView(container);
      };

      list.appendChild(card);
    });

    container.appendChild(view);
  }

  function timeAgo(time) {
    const diff = Date.now() - time;
    const hours = Math.floor(diff / 3600000);
    if (hours < 1) return "Just now";
    if (hours < 24) return hours + "h ago";
    return Math.floor(hours / 24) + "d ago";
  }

  function escapeHtml(str) {
    if (!str) return "";
    return String(str).replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[m]);
  }

  window.RabbitCommunityViews = {
    renderWarren: renderWarrenView,
    renderClubs: renderClubsView
  };
})();
