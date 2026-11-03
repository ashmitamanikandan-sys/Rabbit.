/**
 * RABBIT 2.0 — Warren, Clubs, Wrapped & Settings (rabbit-community-wrapped.js)
 * Implements:
 * - The Warren: chapter & line attached thoughts with "✦ this" reactions
 * - Clubs: groups lighting up shared constellations together
 * - RABBIT Wrapped: 1080x1920 high-res canvas card export (PNG download & Web Share API)
 * - Tonight's Sky 5-chapter modal & daily completion recap
 * - Settings modal (text size, reduced motion, demo mode toggle)
 */

(function(window) {
  'use strict';

  // 1. The Warren: Share Line or Chapter Thought
  window.shareLineToWarren = function(bookId, chapterN, quoteText) {
    var book = (window.RABBIT_BOOK_MAP && window.RABBIT_BOOK_MAP[bookId]) || (window.getBookById && window.getBookById(bookId));
    var title = book ? book.title : bookId;

    var text = prompt('Share your reflection on this line with The Warren:\n\n"' + quoteText + '"', '');
    if (!text || !text.trim()) return;

    var post = {
      id: 'warren-' + Date.now(),
      author: window.rabbitSky.state.user.name,
      bookId: bookId,
      bookTitle: title,
      chapterN: chapterN,
      quote: quoteText,
      reflection: text.trim(),
      reactions: 1,
      createdAt: new Date().toISOString()
    };

    var warrenPosts = getWarrenPosts();
    warrenPosts.unshift(post);
    localStorage.setItem('rabbit_warren_posts_v2', JSON.stringify(warrenPosts));

    alert('✦ Your thought has been posted to The Warren attached to this line!');
  };

  function getWarrenPosts() {
    try {
      var raw = localStorage.getItem('rabbit_warren_posts_v2');
      if (raw) return JSON.parse(raw);
    } catch(e) {}

    // Seeded initial thoughts
    return [
      {
        id: 'w-1',
        author: 'Aria M.',
        bookId: 'atomic-habits',
        bookTitle: 'Atomic Habits',
        chapterN: 1,
        quote: 'You do not rise to the level of your goals. You fall to the level of your systems.',
        reflection: 'Realized I set five study goals every semester, but my desk routine was pure chaos. Fixing the desk changed my semester.',
        reactions: 14,
        createdAt: '2 hours ago'
      },
      {
        id: 'w-2',
        author: 'Marcus K.',
        bookId: 'dune',
        bookTitle: 'Dune',
        chapterN: 1,
        quote: 'I must not fear. Fear is the mind-killer.',
        reflection: 'Used this before my thesis defense yesterday. When you let the terror pass through you, only your sovereign mind remains.',
        reactions: 29,
        createdAt: '4 hours ago'
      },
      {
        id: 'w-3',
        author: 'Dev P.',
        bookId: 'meditations',
        bookTitle: 'Meditations',
        chapterN: 3,
        quote: 'Choose not to be harmed—and you won\'t feel harmed. Don\'t feel harmed—and you haven\'t been.',
        reflection: 'Marcus wrote this for himself while running an empire at war. Puts my roommate argument into clean perspective.',
        reactions: 42,
        createdAt: '6 hours ago'
      }
    ];
  }

  window.renderWarrenFeed = function(container) {
    if (!container) return;
    var posts = getWarrenPosts();
    var html = '<div class="warren-feed-wrapper">';
    html += '  <header class="warren-header">';
    html += '    <h1>The Warren</h1>';
    html += '    <p>Thoughts & conversations anchored directly to chapters and lines.</p>';
    html += '  </header>';
    html += '  <div class="warren-posts-list">';

    for (var i = 0; i < posts.length; i++) {
      var p = posts[i];
      html += '<div class="warren-card" data-post-id="' + p.id + '">';
      html += '  <div class="warren-card-header">';
      html += '    <span class="warren-author">✦ ' + escapeHtml(p.author) + '</span>';
      html += '    <span class="warren-book-tag" onclick="window.jumpToBookDeck(\'' + p.bookId + '\', ' + p.chapterN + ')">' + escapeHtml(p.bookTitle) + ' · Ch ' + p.chapterN + '</span>';
      html += '  </div>';
      if (p.quote) {
        html += '<blockquote class="warren-card-quote">“' + escapeHtml(p.quote) + '”</blockquote>';
      }
      html += '  <p class="warren-card-body">' + escapeHtml(p.reflection) + '</p>';
      html += '  <div class="warren-card-footer">';
      html += '    <button class="warren-react-btn" onclick="window.reactToWarrenPost(this, \'' + p.id + '\')">✦ this (' + p.reactions + ')</button>';
      html += '    <span class="warren-time">' + (p.createdAt.includes('T') ? 'Recently' : p.createdAt) + '</span>';
      html += '  </div>';
      html += '</div>';
    }

    html += '  </div>';
    html += '</div>';
    container.innerHTML = html;
  };

  window.reactToWarrenPost = function(btn, postId) {
    var posts = getWarrenPosts();
    for (var i = 0; i < posts.length; i++) {
      if (posts[i].id === postId) {
        posts[i].reactions++;
        btn.innerHTML = '✦ this (' + posts[i].reactions + ')';
        btn.classList.add('reacted');
        break;
      }
    }
    localStorage.setItem('rabbit_warren_posts_v2', JSON.stringify(posts));
  };

  // 2. Clubs: Lighting Shared Constellations
  window.renderClubsView = function(container) {
    if (!container) return;
    var clubs = [
      {
        id: 'club-1',
        name: 'The Midnight Thinkers',
        book: 'Thinking, Fast and Slow',
        bookId: 'thinking-fast-and-slow',
        members: 38,
        starsLit: 184,
        totalStarsNeeded: 228
      },
      {
        id: 'club-2',
        name: 'Deep Work Pioneers',
        book: 'Deep Work',
        bookId: 'deep-work',
        members: 52,
        starsLit: 270,
        totalStarsNeeded: 312
      },
      {
        id: 'club-3',
        name: 'Arrakis Stargazers',
        book: 'Dune',
        bookId: 'dune',
        members: 64,
        starsLit: 320,
        totalStarsNeeded: 384
      }
    ];

    var html = '<div class="clubs-view-wrapper">';
    html += '  <header class="clubs-header">';
    html += '    <h1>Clubs</h1>';
    html += '    <p>Read together and light up shared constellations star by star.</p>';
    html += '  </header>';
    html += '  <div class="clubs-list">';

    for (var i = 0; i < clubs.length; i++) {
      var c = clubs[i];
      var pct = Math.round((c.starsLit / c.totalStarsNeeded) * 100);
      html += '<div class="club-card" onclick="window.jumpToBookDeck(\'' + c.bookId + '\')">';
      html += '  <div class="club-card-top">';
      html += '    <div>';
      html += '      <h3 class="club-name">' + escapeHtml(c.name) + '</h3>';
      html += '      <p class="club-book">Reading <strong>' + escapeHtml(c.book) + '</strong></p>';
      html += '    </div>';
      html += '    <span class="club-members-badge">' + c.members + ' members</span>';
      html += '  </div>';
      html += '  <div class="club-progress-bar">';
      html += '    <div class="club-progress-fill" style="width:' + pct + '%;"></div>';
      html += '  </div>';
      html += '  <div class="club-card-bottom">';
      html += '    <span>Constellation ' + pct + '% Complete</span>';
      html += '    <span style="color:#BCA6FF;">' + c.starsLit + ' / ' + c.totalStarsNeeded + ' stars lit ✦</span>';
      html += '  </div>';
      html += '</div>';
    }

    html += '  </div>';
    html += '</div>';
    container.innerHTML = html;
  };

  // 3. RABBIT Wrapped: 1080x1920 Instagram Story Card Export
  window.generateRabbitWrapped = function() {
    var state = window.rabbitSky.state;
    var canvas = document.createElement('canvas');
    canvas.width = 1080;
    canvas.height = 1920;
    var ctx = canvas.getContext('2d');

    // Gradient Background
    var bg = ctx.createLinearGradient(0, 0, 1080, 1920);
    bg.addColorStop(0, '#050409');
    bg.addColorStop(0.4, '#130E24');
    bg.addColorStop(0.8, '#211B33');
    bg.addColorStop(1, '#08060D');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, 1080, 1920);

    // Subtle Stars in background
    ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
    for (var s = 0; s < 120; s++) {
      var sx = Math.random() * 1080;
      var sy = Math.random() * 1920;
      var sr = Math.random() * 2 + 0.5;
      ctx.beginPath();
      ctx.arc(sx, sy, sr, 0, Math.PI * 2);
      ctx.fill();
    }

    // RABBIT Wordmark & Header
    ctx.font = '800 52px -apple-system, sans-serif';
    ctx.fillStyle = '#BCA6FF';
    ctx.textAlign = 'center';
    ctx.fillText('RABBIT', 540, 240);

    ctx.font = '600 28px -apple-system, sans-serif';
    ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
    ctx.letterSpacing = '4px';
    ctx.fillText('MONTHLY SKY WRAPPED', 540, 290);

    // Central Constellation Glow
    var glow = ctx.createRadialGradient(540, 720, 40, 540, 720, 360);
    glow.addColorStop(0, 'rgba(188, 166, 255, 0.25)');
    glow.addColorStop(1, 'rgba(0, 0, 0, 0)');
    ctx.fillStyle = glow;
    ctx.beginPath();
    ctx.arc(540, 720, 360, 0, Math.PI * 2);
    ctx.fill();

    // Central Stat: Stars Lit
    ctx.font = '800 160px -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.shadowColor = '#BCA6FF';
    ctx.shadowBlur = 30;
    ctx.fillText(state.stars.total.toString(), 540, 760);
    ctx.shadowBlur = 0;

    ctx.font = '700 36px -apple-system, sans-serif';
    ctx.fillStyle = '#BCA6FF';
    ctx.fillText('STARS LIT IN YOUR SKY', 540, 830);

    // Stats Grid
    var compCount = Object.keys(state.constellations.completed).length;
    var nights = state.streak.nights;

    // Stat 1: Completed Constellations
    drawStatPill(ctx, 280, 1080, compCount.toString(), 'CONSTELLATIONS COMPLETED');
    // Stat 2: Nights Streak
    drawStatPill(ctx, 800, 1080, nights.toString() + ' NIGHTS', 'CONSECUTIVE STREAK');

    // Quote Footer
    ctx.font = 'italic 34px Georgia, serif';
    ctx.fillStyle = '#EDEAF5';
    ctx.fillText('“Every chapter is a star in your night sky.”', 540, 1500);

    ctx.font = '600 26px -apple-system, sans-serif';
    ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
    ctx.fillText('rabbit.app · Download the app & explore your burrow', 540, 1720);

    // Export & Share
    canvas.toBlob(function(blob) {
      if (navigator.share && navigator.canShare && navigator.canShare({ files: [new File([blob], 'rabbit-wrapped.png', { type: 'image/png' })] })) {
        var file = new File([blob], 'rabbit-wrapped.png', { type: 'image/png' });
        navigator.share({
          files: [file],
          title: 'My RABBIT Sky Wrapped',
          text: 'I have lit ' + state.stars.total + ' stars in my RABBIT night sky!'
        });
      } else {
        // Fallback: download PNG directly
        var a = document.createElement('a');
        a.download = 'rabbit-sky-wrapped.png';
        a.href = canvas.toDataURL('image/png');
        a.click();
      }
    });
  };

  function drawStatPill(ctx, x, y, value, label) {
    ctx.fillStyle = 'rgba(33, 27, 51, 0.6)';
    ctx.strokeStyle = 'rgba(188, 166, 255, 0.3)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(x - 220, y - 80, 440, 160, 28);
    ctx.fill();
    ctx.stroke();

    ctx.font = '800 52px -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.textAlign = 'center';
    ctx.fillText(value, x, y + 8);

    ctx.font = '700 18px -apple-system, sans-serif';
    ctx.fillStyle = '#9E96B0';
    ctx.letterSpacing = '1px';
    ctx.fillText(label, x, y + 48);
  }

  // 4. Tonight's Sky 5-Chapter Playlist View & Completion Modal
  window.renderTonightsSkyView = function(container) {
    if (!container) return;
    var state = window.rabbitSky.state;
    var playlist = window.rabbitSky.getTonightPlaylist();

    var litCount = state.tonight.stars_lit_today;
    var html = '<div class="tonight-view-wrapper">';
    html += '  <header class="tonight-header">';
    html += '    <span style="font-size:11px;font-weight:700;color:#BCA6FF;letter-spacing:1.5px;text-transform:uppercase;">TONIGHT\'S SKY</span>';
    html += '    <h1>Daily 5 Chapters</h1>';
    html += '    <p>Read 5 curated chapters tonight to light your daily stars and keep your streak alive.</p>';
    html += '    <div class="tonight-progress-pill">' + litCount + ' / 5 Stars Lit Tonight ' + (litCount >= 5 ? '✦ Complete' : '') + '</div>';
    html += '  </header>';

    html += '  <div class="tonight-playlist-list">';
    for (var i = 0; i < playlist.length; i++) {
      var item = playlist[i];
      var book = (window.RABBIT_BOOK_MAP && window.RABBIT_BOOK_MAP[item.book_id]) || (window.getBookById && window.getBookById(item.book_id)) || {
        title: item.book_id,
        cover_url: 'https://covers.openlibrary.org/b/id/12843460-M.jpg'
      };
      var chapter = (book.chapters && book.chapters[item.chapter_n - 1]) || { title: 'Chapter ' + item.chapter_n };

      html += '<div class="tonight-item-card ' + (item.finished ? 'finished' : '') + '" onclick="window.jumpToBookDeck(\'' + item.book_id + '\', ' + item.chapter_n + ')">';
      html += '  <span class="tonight-item-star">' + (item.finished ? '✦' : (i + 1)) + '</span>';
      html += '  <img class="tonight-item-cover" src="' + (book.cover_url || '') + '" alt="' + escapeHtml(book.title) + '">';
      html += '  <div class="tonight-item-info">';
      html += '    <strong>' + escapeHtml(book.title) + '</strong>';
      html += '    <span>Ch ' + item.chapter_n + ': ' + escapeHtml(chapter.title) + '</span>';
      html += '  </div>';
      html += '  <button class="tonight-read-action">' + (item.finished ? 'Lit ✦' : 'Read →') + '</button>';
      html += '</div>';
    }
    html += '  </div>';
    html += '</div>';

    container.innerHTML = html;
  };

  // Listen for Tonight 5-star completion event
  window.addEventListener('rabbit:tonight-completed', function() {
    alert("✦ You've lit 5 stars tonight!\nYour daily constellation is complete. Rest your mind, or keep digging deeper down the rabbit hole.");
  });

  // Settings Modal
  window.openSettingsModal = function() {
    var modal = document.getElementById('rabbit-settings-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'rabbit-settings-modal';
      modal.className = 'rabbit-settings-modal';
      document.body.appendChild(modal);
    }

    var state = window.rabbitSky.state;
    var html = '<div class="settings-modal-content">';
    html += '  <button class="modal-close-btn" onclick="document.getElementById(\'rabbit-settings-modal\').classList.remove(\'open\')">✕</button>';
    html += '  <h2>Settings & Profile</h2>';
    html += '  <div class="settings-field">';
    html += '    <label>Reader Name</label>';
    html += '    <input type="text" id="setting-name" value="' + escapeHtml(state.user.name) + '">';
    html += '  </div>';
    html += '  <div class="settings-field">';
    html += '    <label>Demo Mode</label>';
    html += '    <button class="settings-toggle-btn ' + (state.settings.demoMode ? 'active' : '') + '" onclick="window.toggleDemoMode()">' + (state.settings.demoMode ? 'ENABLED (Demo Profile)' : 'DISABLED') + '</button>';
    html += '  </div>';
    html += '  <div class="settings-field">';
    html += '    <label>Reading Text Size</label>';
    html += '    <div style="display:flex;gap:10px;">';
    html += '      <button class="settings-btn" onclick="window.setTextSize(\'S\')">S</button>';
    html += '      <button class="settings-btn" onclick="window.setTextSize(\'M\')">M</button>';
    html += '      <button class="settings-btn" onclick="window.setTextSize(\'L\')">L</button>';
    html += '    </div>';
    html += '  </div>';
    html += '  <div style="margin-top:24px;border-top:1px solid rgba(255,255,255,0.1);padding-top:16px;">';
    html += '    <button style="background:#EF4444;color:#fff;border:none;padding:10px 18px;border-radius:10px;cursor:pointer;font-weight:700;" onclick="window.resetUserData()">Reset All Data</button>';
    html += '  </div>';
    html += '</div>';

    modal.innerHTML = html;
    modal.classList.add('open');
  };

  window.toggleDemoMode = function() {
    var isCurrentlyDemo = window.rabbitSky.state.settings.demoMode;
    if (isCurrentlyDemo) {
      localStorage.removeItem('rabbit_sky_v2');
      window.location.href = window.location.pathname;
    } else {
      window.location.href = window.location.pathname + '?demo=1';
    }
  };

  window.setTextSize = function(size) {
    document.documentElement.style.setProperty('--reader-size', size === 'S' ? '15px' : size === 'L' ? '19px' : '17px');
    window.rabbitSky.state.settings.textSize = size;
    window.rabbitSky.save();
  };

  window.resetUserData = function() {
    if (confirm('Are you sure you want to reset your stars and reading history?')) {
      localStorage.clear();
      window.location.reload();
    }
  };

  function escapeHtml(str) {
    if (!str) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

})(window);
