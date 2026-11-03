/**
 * RABBIT 2.0 — Chapter Deck Feed Engine (rabbit-feed-2.js)
 * Implements the signature Chapter Deck:
 * - 5-card horizontal swipe: 1. Spark, 2. Key Ideas, 3. The Line, 4. In Your Life, 5. Rabbit Hole
 * - Vertical snap scrolling between chapters (100dvh)
 * - Axis-locking touch, mouse drag, keyboard arrows (↑ ↓ ← →), and visible buttons
 * - "Constellations in progress" glowing top rail
 * - Flying star animation from Card 5 to the Sky nav icon
 * - Long-form "Read More" reader overlay
 * - Fiction spoiler veil with tap-to-reveal
 * - Metric tracking for "Find this book"
 */

(function(window) {
  'use strict';

  var currentActiveDeck = null;
  var currentCardIndex = 0;

  function initChapterFeed() {
    var container = document.getElementById('rabbit-feed-root') || document.querySelector('.rabbit-feed-container');
    if (!container) return;

    renderConstellationsRail();
    renderFeedDecks(container);
    setupGlobalKeyboardNav();
    setupStarEventListener();
  }

  // 1. Constellations In Progress Top Rail
  function renderConstellationsRail() {
    var rail = document.getElementById('rabbit-constellations-rail');
    if (!rail) return;

    var state = window.rabbitSky.state;
    var collected = state.stars.collected || {};
    var inProgress = state.constellations.in_progress || {};
    var completed = state.constellations.completed || {};

    // Get list of active book IDs
    var activeBookIds = Object.keys(completed).concat(Object.keys(inProgress));
    if (activeBookIds.length === 0) {
      // Default highlight hero books if empty
      activeBookIds = ['atomic-habits', 'meditations', 'dune', 'deep-work', 'the-psychology-of-money'];
    }

    var html = '';
    for (var i = 0; i < activeBookIds.length; i++) {
      var bId = activeBookIds[i];
      var book = (window.RABBIT_BOOK_MAP && window.RABBIT_BOOK_MAP[bId]) || (window.getBookById && window.getBookById(bId)) || {
        id: bId,
        title: bId.replace(/-/g, ' '),
        cover_url: 'https://covers.openlibrary.org/b/id/12843460-M.jpg'
      };

      var starsLit = (collected[bId] || []).length;
      var totalNeeded = (inProgress[bId] && inProgress[bId].total_chapters) || (completed[bId] && completed[bId].total_chapters) || (book.chapters ? book.chapters.length : 6);
      var isComp = !!completed[bId] || (starsLit >= totalNeeded && starsLit > 0);
      var pct = Math.min(1, starsLit / totalNeeded);
      var circumference = 2 * Math.PI * 22; // r=22
      var strokeDashoffset = circumference * (1 - pct);

      html += '<div class="rail-item ' + (isComp ? 'completed' : '') + '" data-book-id="' + book.id + '" onclick="window.jumpToBookDeck(\'' + book.id + '\')">';
      html += '  <div class="rail-ring-wrapper">';
      html += '    <svg class="rail-svg-ring" viewBox="0 0 50 50">';
      html += '      <circle class="rail-svg-bg" cx="25" cy="25" r="22"></circle>';
      html += '      <circle class="rail-svg-progress" cx="25" cy="25" r="22" stroke-dasharray="' + circumference + '" stroke-dashoffset="' + strokeDashoffset + '"></circle>';
      html += '    </svg>';
      html += '    <img class="rail-cover" src="' + (book.cover_url || '') + '" alt="' + escapeHtml(book.title) + '" onerror="this.src=\'https://covers.openlibrary.org/b/id/12843460-M.jpg\'">';
      html += '  </div>';
      html += '  <span class="rail-label">' + escapeHtml(book.title) + '</span>';
      html += '</div>';
    }

    rail.innerHTML = html;
  }

  // 2. Render Vertical Chapter Decks
  function renderFeedDecks(container) {
    var catalog = window.RABBIT_CATALOG || [];
    if (!catalog.length) return;

    // Filter books based on active genre or show diverse playlist
    var activeGenre = window.currentSelectedGenre || 'all';
    var booksToRender = catalog;
    if (activeGenre && activeGenre !== 'all' && activeGenre !== 'the burrow') {
      booksToRender = catalog.filter(function(b) {
        return (b.genre || '').toLowerCase().trim() === activeGenre.toLowerCase().trim();
      });
    }

    // Limit to top 25 chapters for smooth initial 60fps feed
    var deckHtml = '';
    var count = 0;
    for (var i = 0; i < booksToRender.length && count < 25; i++) {
      var book = booksToRender[i];
      var chapters = book.chapters || [];
      for (var c = 0; c < chapters.length && count < 25; c++) {
        var chapter = chapters[c];
        deckHtml += renderSingleChapterDeck(book, chapter);
        count++;
      }
    }

    container.innerHTML = deckHtml;
    attachDeckTouchHandlers(container);
  }

  // 3. Render 1 Chapter Deck with its 5 Cards
  function renderSingleChapterDeck(book, chapter) {
    var bId = book.id;
    var chN = chapter.n || 1;
    var totalCh = book.chapters ? book.chapters.length : 6;
    var genre = book.genre || 'General';
    var palette = window.RabbitSkyEngine.getGenrePalette(genre);
    var isSpoiler = chapter.spoiler_level === 'light';

    var html = '<article class="chapter-deck" data-book-id="' + bId + '" data-chapter-n="' + chN + '" data-total-chapters="' + totalCh + '">';
    html += '  <div class="deck-card-viewport">';
    
    // Horizontal Track
    html += '    <div class="deck-track" data-active-card="0">';

    // Card 1: THE SPARK
    html += '      <div class="deck-card card-spark">';
    html += '        <div class="spark-header">';
    html += '          <img class="spark-cover" src="' + (book.cover_url || '') + '" alt="' + escapeHtml(book.title) + '" onerror="this.src=\'https://covers.openlibrary.org/b/id/12843460-M.jpg\'">';
    html += '          <div class="spark-meta">';
    html += '            <span class="spark-genre-pill" style="color:' + palette.color + '; border-color:' + palette.color + '; background:' + palette.glow + '">' + escapeHtml(genre) + '</span>';
    html += '            <h3 class="spark-book-title">' + escapeHtml(book.title) + '</h3>';
    html += '            <p class="spark-book-author">by ' + escapeHtml(book.author) + '</p>';
    html += '          </div>';
    html += '        </div>';
    html += '        <span class="spark-chapter-badge">CHAPTER ' + chN + ' OF ' + totalCh + '</span>';
    html += '        <h2 class="spark-chapter-title">' + escapeHtml(chapter.title) + '</h2>';
    html += '        <div class="spark-hook">' + escapeHtml(chapter.hook || '') + '</div>';
    html += '        <div class="spark-copy">' + escapeHtml(chapter.spark || '') + '</div>';
    html += '        <button class="spark-read-more-btn" onclick="window.openReaderOverlay(\'' + bId + '\', ' + chN + ')">Read full chapter story →</button>';
    html += '      </div>';

    // Card 2: KEY IDEAS
    html += '      <div class="deck-card card-key-ideas">';
    html += '        <span class="card-eyebrow">KEY IDEAS</span>';
    html += '        <h2 class="card-heading">Three core insights to remember</h2>';
    if (isSpoiler) {
      html += '      <div class="spoiler-veil">';
      html += '        <p style="font-size:13px; color:#FBBF24;">✦ Spoilers ahead for this chapter</p>';
      html += '        <button class="spoiler-reveal-btn" onclick="this.parentElement.remove()">Tap to reveal</button>';
      html += '      </div>';
    }
    html += '        <div class="key-ideas-list">';
    var ideas = chapter.key_ideas || [];
    for (var k = 0; k < ideas.length; k++) {
      html += '        <div class="key-idea-card">';
      html += '          <span class="idea-num">' + (k + 1) + '</span>';
      html += '          <div class="idea-content">';
      html += '            <div class="idea-bold">' + escapeHtml(ideas[k].idea) + '</div>';
      html += '            <div class="idea-why">' + escapeHtml(ideas[k].why) + '</div>';
      html += '          </div>';
      html += '        </div>';
    }
    html += '        </div>';
    html += '      </div>';

    // Card 3: THE LINE
    html += '      <div class="deck-card card-line">';
    html += '        <span class="card-eyebrow">THE LINE</span>';
    var lineObj = chapter.line || { text: 'Knowledge becomes wisdom when embodied.', type: 'rabbit_take' };
    html += '        <blockquote class="the-line-quote">' + escapeHtml(lineObj.text) + '</blockquote>';
    var badgeLabel = lineObj.type === 'quote' ? 'Quote — ' + book.author : "RABBIT's take";
    html += '        <span class="the-line-badge">' + escapeHtml(badgeLabel) + '</span>';
    html += '        <button class="line-share-warren-btn" onclick="window.shareLineToWarren(\'' + bId + '\', ' + chN + ', ' + escapeHtml(JSON.stringify(lineObj.text)) + ')">✦ Share to The Warren</button>';
    html += '      </div>';

    // Card 4: IN YOUR LIFE
    html += '      <div class="deck-card card-in-your-life">';
    html += '        <span class="card-eyebrow">IN YOUR LIFE</span>';
    html += '        <h2 class="card-heading">How to apply this today</h2>';
    html += '        <div class="life-scenarios-list">';
    var lifeScenarios = chapter.in_your_life || [];
    var icons = ['✦', '⚡', '◈'];
    for (var l = 0; l < lifeScenarios.length; l++) {
      html += '        <div class="life-scenario-item">';
      html += '          <span class="life-icon">' + icons[l % icons.length] + '</span>';
      html += '          <p class="life-text">' + escapeHtml(lifeScenarios[l]) + '</p>';
      html += '        </div>';
    }
    html += '        </div>';
    html += '      </div>';

    // Card 5: RABBIT HOLE (Star Lit Card!)
    html += '      <div class="deck-card card-rabbit-hole">';
    html += '        <span class="card-eyebrow">RABBIT HOLE</span>';
    html += '        <h2 class="card-heading">This chapter connects to...</h2>';
    html += '        <p class="rabbit-hole-intro">Fall deeper down the rabbit hole through related ideas:</p>';
    html += '        <div class="connection-cards-list">';
    var connects = chapter.connects_to || [];
    for (var cn = 0; cn < connects.length; cn++) {
      var targetId = connects[cn].book_id;
      var targetCh = connects[cn].chapter;
      var targetBook = (window.RABBIT_BOOK_MAP && window.RABBIT_BOOK_MAP[targetId]) || (window.getBookById && window.getBookById(targetId)) || {
        title: targetId.replace(/-/g, ' '),
        cover_url: 'https://covers.openlibrary.org/b/id/12843460-M.jpg'
      };
      html += '        <div class="connection-card" onclick="window.jumpToBookDeck(\'' + targetId + '\', ' + targetCh + ')">';
      html += '          <img class="conn-cover" src="' + (targetBook.cover_url || '') + '" alt="' + escapeHtml(targetBook.title) + '" onerror="this.src=\'https://covers.openlibrary.org/b/id/12843460-M.jpg\'">';
      html += '          <div class="conn-info">';
      html += '            <span class="conn-title">' + escapeHtml(targetBook.title) + ' (Ch ' + targetCh + ')</span>';
      html += '            <span class="conn-reason">' + escapeHtml(connects[cn].reason) + '</span>';
      html += '          </div>';
      html += '        </div>';
    }
    html += '        </div>';

    // Star Lit Micro-Interaction Banner
    html += '        <div class="star-lit-banner">';
    html += '          <span class="star-lit-icon">✦</span>';
    html += '          <div class="star-lit-text">';
    html += '            <span class="star-lit-title">Star Lit in Your Sky</span>';
    html += '            <span class="star-lit-subtitle">You finished this chapter deck!</span>';
    html += '          </div>';
    html += '        </div>';

    // "Find this book" link with metric counter
    html += '        <button class="find-book-btn" onclick="window.findThisBook(\'' + bId + '\', \'' + escapeHtml(book.title) + '\')">📖 Find this book in your library or bookshop</button>';
    html += '      </div>';

    html += '    </div>'; // end deck-track

    // 5 Progress Dots
    html += '    <div class="deck-dots-bar">';
    for (var d = 0; d < 5; d++) {
      html += '    <div class="deck-dot ' + (d === 0 ? 'active' : '') + '" data-dot-idx="' + d + '"></div>';
    }
    html += '    </div>';

    // Arrow Nav Controls
    html += '    <button class="deck-arrow-btn deck-arrow-left" hidden aria-label="Previous card" onclick="window.stepDeckCard(this, -1)">‹</button>';
    html += '    <button class="deck-arrow-btn deck-arrow-right" aria-label="Next card" onclick="window.stepDeckCard(this, 1)">›</button>';

    html += '  </div>'; // end deck-card-viewport
    html += '</article>';

    return html;
  }

  // 4. Horizontal Deck Swipe & Axis-Locking Handlers
  function attachDeckTouchHandlers(container) {
    var decks = container.querySelectorAll('.chapter-deck');
    for (var i = 0; i < decks.length; i++) {
      (function(deck) {
        var track = deck.querySelector('.deck-track');
        var startX = 0, startY = 0;
        var diffX = 0, diffY = 0;
        var isHorizontal = null;

        deck.addEventListener('touchstart', function(e) {
          if (e.touches.length !== 1) return;
          startX = e.touches[0].clientX;
          startY = e.touches[0].clientY;
          diffX = 0;
          diffY = 0;
          isHorizontal = null;
        }, { passive: true });

        deck.addEventListener('touchmove', function(e) {
          if (e.touches.length !== 1) return;
          diffX = e.touches[0].clientX - startX;
          diffY = e.touches[0].clientY - startY;

          // Axis lock: determine intent on first 10px of movement
          if (isHorizontal === null) {
            if (Math.abs(diffX) > 8 || Math.abs(diffY) > 8) {
              isHorizontal = Math.abs(diffX) > Math.abs(diffY);
            }
          }

          // If swiping horizontally, stop vertical scroll interference
          if (isHorizontal === true) {
            e.stopPropagation();
          }
        }, { passive: false });

        deck.addEventListener('touchend', function() {
          if (isHorizontal === true) {
            if (diffX < -45) {
              // Swipe left -> Next card
              navigateCard(deck, 1);
            } else if (diffX > 45) {
              // Swipe right -> Prev card
              navigateCard(deck, -1);
            }
          }
        }, { passive: true });
      })(decks[i]);
    }
  }

  // Navigate cards within deck
  function navigateCard(deck, delta) {
    var track = deck.querySelector('.deck-track');
    if (!track) return;

    var currentIdx = parseInt(track.getAttribute('data-active-card') || '0', 10);
    var newIdx = Math.max(0, Math.min(4, currentIdx + delta));
    if (newIdx === currentIdx) return;

    track.setAttribute('data-active-card', newIdx);
    track.style.transform = 'translateX(-' + (newIdx * 20) + '%)';

    // Update Dots
    var dots = deck.querySelectorAll('.deck-dot');
    for (var i = 0; i < dots.length; i++) {
      dots[i].classList.toggle('active', i === newIdx);
    }

    // Update Arrow buttons visibility
    var leftBtn = deck.querySelector('.deck-arrow-left');
    var rightBtn = deck.querySelector('.deck-arrow-right');
    if (leftBtn) leftBtn.hidden = (newIdx === 0);
    if (rightBtn) rightBtn.hidden = (newIdx === 4);

    // On reaching Card 5 (Rabbit Hole / Star Lit)
    if (newIdx === 4) {
      handleCard5Reached(deck);
    }
  }

  // Step card via button
  window.stepDeckCard = function(btn, delta) {
    var deck = btn.closest('.chapter-deck');
    if (deck) navigateCard(deck, delta);
  };

  // Card 5 Star Collection & Flying Star Particle
  function handleCard5Reached(deck) {
    var bId = deck.getAttribute('data-book-id');
    var chN = parseInt(deck.getAttribute('data-chapter-n') || '1', 10);
    var totalCh = parseInt(deck.getAttribute('data-total-chapters') || '6', 10);

    var res = window.rabbitSky.collectStar(bId, chN, totalCh);

    if (res.isNewStar) {
      // Spawn flying star animation from card center to Sky icon in nav
      spawnFlyingStar(deck);
      renderConstellationsRail();
    }
  }

  // Flying Star Animation to Sky icon
  function spawnFlyingStar(sourceElem) {
    var target = document.getElementById('nav-sky') || document.querySelector('.sky-icon');
    var rect = sourceElem.getBoundingClientRect();

    var star = document.createElement('div');
    star.className = 'flying-star-particle';
    star.innerHTML = '✦';
    star.style.left = (rect.left + rect.width / 2 - 13) + 'px';
    star.style.top = (rect.top + rect.height / 2 - 13) + 'px';
    document.body.appendChild(star);

    // Target position (nav button)
    var targetRect = target ? target.getBoundingClientRect() : { left: window.innerWidth - 60, top: window.innerHeight - 40 };

    requestAnimationFrame(function() {
      var dx = (targetRect.left + targetRect.width / 2) - (rect.left + rect.width / 2);
      var dy = (targetRect.top + targetRect.height / 2) - (rect.top + rect.height / 2);

      star.style.transform = 'translate(' + dx + 'px, ' + dy + 'px) scale(0.4)';
      star.style.opacity = '0.3';
    });

    setTimeout(function() {
      if (star.parentNode) star.parentNode.removeChild(star);
      if (target) {
        target.classList.add('pulse-glow');
        setTimeout(function() { target.classList.remove('pulse-glow'); }, 800);
      }
    }, 900);
  }

  // Keyboard navigation (← → for cards, ↑ ↓ for chapters)
  function setupGlobalKeyboardNav() {
    window.addEventListener('keydown', function(e) {
      if (document.querySelector('.rabbit-reader-overlay.open')) return;
      var activeDeck = getVisibleDeck();
      if (!activeDeck) return;

      if (e.key === 'ArrowRight') {
        navigateCard(activeDeck, 1);
      } else if (e.key === 'ArrowLeft') {
        navigateCard(activeDeck, -1);
      }
    });
  }

  function getVisibleDeck() {
    var decks = document.querySelectorAll('.chapter-deck');
    var winHeight = window.innerHeight;
    for (var i = 0; i < decks.length; i++) {
      var r = decks[i].getBoundingClientRect();
      if (r.top >= -r.height / 2 && r.top <= winHeight / 2) {
        return decks[i];
      }
    }
    return decks[0] || null;
  }

  // Jump directly to a book's deck
  window.jumpToBookDeck = function(bookId, chapterN) {
    var target = document.querySelector('.chapter-deck[data-book-id="' + bookId + '"]');
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
      if (chapterN) {
        var card = chapterN >= 5 ? 4 : 0;
        navigateCard(target, card);
      }
    }
  };

  // "Find this book" library search and metric tracker
  window.findThisBook = function(bookId, bookTitle) {
    window.rabbitSky.trackMetric('find_book_click', { book_id: bookId, title: bookTitle });
    var query = encodeURIComponent(bookTitle);
    var searchUrl = 'https://openlibrary.org/search?q=' + query;
    window.open(searchUrl, '_blank');
  };

  // Long-Form Reader Overlay
  window.openReaderOverlay = function(bookId, chapterN) {
    var book = (window.RABBIT_BOOK_MAP && window.RABBIT_BOOK_MAP[bookId]) || (window.getBookById && window.getBookById(bookId));
    if (!book) return;
    var chapter = (book.chapters && book.chapters[chapterN - 1]) || book.chapters[0];
    if (!chapter) return;

    var overlay = document.getElementById('rabbit-reader-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'rabbit-reader-overlay';
      overlay.className = 'rabbit-reader-overlay';
      document.body.appendChild(overlay);
    }

    var html = '<button class="reader-close-btn" onclick="window.closeReaderOverlay()">✕</button>';
    html += '<div class="reader-inner">';
    html += '  <span style="font-size:11px;font-weight:700;color:var(--rabbit-lilac);letter-spacing:1px;text-transform:uppercase;">' + escapeHtml(book.genre || '') + ' · CHAPTER ' + chapterN + '</span>';
    html += '  <h1 style="font-family:var(--rabbit-font-serif);font-size:32px;line-height:1.25;margin:12px 0 6px 0;">' + escapeHtml(chapter.title) + '</h1>';
    html += '  <p style="font-size:14px;color:var(--rabbit-muted);margin:0 0 24px 0;">from <strong>' + escapeHtml(book.title) + '</strong> by ' + escapeHtml(book.author) + '</p>';
    html += '  <div style="font-size:17px;font-weight:600;color:#DDD6FE;border-left:3px solid var(--rabbit-lilac);padding-left:14px;margin-bottom:28px;">' + escapeHtml(chapter.hook || '') + '</div>';
    html += '  <div style="font-family:var(--rabbit-font-serif);font-size:18px;line-height:1.85;color:#EDEAF5;white-space:pre-line;margin-bottom:36px;">' + escapeHtml(chapter.spark || '') + '</div>';

    // Key Ideas
    html += '  <div style="background:rgba(33,27,51,0.5);border:1px solid rgba(188,166,255,0.2);border-radius:18px;padding:24px;margin-bottom:36px;">';
    html += '    <h3 style="font-size:18px;margin:0 0 16px 0;color:var(--rabbit-white);">Core Insights</h3>';
    var ideas = chapter.key_ideas || [];
    for (var k = 0; k < ideas.length; k++) {
      html += '    <div style="margin-bottom:14px;">';
      html += '      <strong style="color:var(--rabbit-lilac);font-size:15px;">' + (k + 1) + '. ' + escapeHtml(ideas[k].idea) + '</strong>';
      html += '      <p style="margin:4px 0 0 0;font-size:14px;color:var(--rabbit-muted);">' + escapeHtml(ideas[k].why) + '</p>';
      html += '    </div>';
    }
    html += '  </div>';

    // The Line
    if (chapter.line) {
      html += '  <blockquote style="font-family:var(--rabbit-font-serif);font-size:22px;font-style:italic;text-align:center;margin:36px 0;color:var(--rabbit-white);">';
      html += '    “' + escapeHtml(chapter.line.text) + '”';
      html += '  </blockquote>';
    }

    html += '</div>';

    overlay.innerHTML = html;
    overlay.classList.add('open');
  };

  window.closeReaderOverlay = function() {
    var overlay = document.getElementById('rabbit-reader-overlay');
    if (overlay) overlay.classList.remove('open');
  };

  function setupStarEventListener() {
    window.addEventListener('rabbit:star-collected', function(e) {
      console.log('Star collected event received:', e.detail);
      renderConstellationsRail();
    });
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  window.initChapterFeed = initChapterFeed;
  window.renderConstellationsRail = renderConstellationsRail;

})(window);
