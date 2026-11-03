/**
 * RABBIT 2.0 — Celestial Sky & State Engine (rabbit-sky-engine.js)
 * Centers around the identity: "Every chapter is a star."
 * 
 * Features:
 * - State management under LocalStorage key: `rabbit_sky_v2`
 * - Migration from legacy `rabbit_taste_v101`
 * - Deterministic constellation generator per book (seeded star coordinates & lines)
 * - Star collection and constellation completion detection
 * - Tonight's Sky daily 5-chapter playlist generator
 * - Nights (daily streak tracker)
 * - Demo mode (?demo=1) pre-populating "Curious Reader" (42 stars, 2 completed constellations, 12 nights)
 * - Local metric counter: `rabbit_metrics_v1`
 */

(function(window) {
  'use strict';

  var STORAGE_KEY = 'rabbit_sky_v2';
  var LEGACY_KEY = 'rabbit_taste_v101';
  var METRICS_KEY = 'rabbit_metrics_v1';

  // Genre Region Color Palette
  var GENRE_PALETTES = {
    'the human mind': { color: '#2DD4BF', name: 'The Human Mind', glow: 'rgba(45, 212, 191, 0.4)' },
    'self discovery': { color: '#FB7185', name: 'Self Discovery', glow: 'rgba(251, 113, 133, 0.4)' },
    'science fiction': { color: '#60A5FA', name: 'Science Fiction', glow: 'rgba(96, 165, 250, 0.4)' },
    'classics': { color: '#34D399', name: 'Classics', glow: 'rgba(52, 211, 153, 0.4)' },
    'philosophy': { color: '#C084FC', name: 'Philosophy', glow: 'rgba(192, 132, 252, 0.4)' },
    'history': { color: '#FBBF24', name: 'History', glow: 'rgba(251, 191, 36, 0.4)' },
    'business & money': { color: '#F59E0B', name: 'Business & Money', glow: 'rgba(245, 158, 11, 0.4)' },
    'science': { color: '#38BDF8', name: 'Science', glow: 'rgba(56, 189, 248, 0.4)' },
    'fantasy': { color: '#A78BFA', name: 'Fantasy', glow: 'rgba(167, 139, 250, 0.4)' },
    'general': { color: '#BCA6FF', name: 'General', glow: 'rgba(188, 166, 255, 0.4)' }
  };

  function getGenrePalette(genre) {
    if (!genre) return GENRE_PALETTES['general'];
    var g = genre.toLowerCase().trim();
    return GENRE_PALETTES[g] || GENRE_PALETTES['general'];
  }

  // PRNG from string seed (Murmur-like 32-bit hash)
  function hashSeed(str) {
    var h = 1779033703 ^ str.length;
    for (var i = 0; i < str.length; i++) {
      h = Math.imul(h ^ str.charCodeAt(i), 3432918353);
      h = (h << 13) | (h >>> 19);
    }
    return function() {
      h = Math.imul(h ^ (h >>> 16), 2246822507);
      h = Math.imul(h ^ (h >>> 13), 3266489909);
      return (h >>> 0) / 4294967296;
    };
  }

  /**
   * Generates deterministic constellation coordinates for a book
   * @param {string} bookId - Unique book identifier
   * @param {number} totalChapters - Total stars in this constellation
   * @returns {Object} { stars: [{x, y, n}], lines: [[i, j]] }
   */
  function generateConstellation(bookId, totalChapters) {
    var numStars = Math.max(3, totalChapters || 6);
    var rng = hashSeed('constellation-' + bookId);

    // Arrange stars in a pleasing celestial pattern (polar coordinates with jitter)
    var stars = [];
    var baseAngle = rng() * Math.PI * 2;
    var spread = 0.7 + rng() * 0.5; // aspect ratio variation

    for (var i = 0; i < numStars; i++) {
      var progress = i / (numStars - 1 || 1);
      // Gentle curve or organic constellation loop
      var angle = baseAngle + (progress - 0.5) * Math.PI * 1.4 + (rng() - 0.5) * 0.6;
      var radius = 40 + progress * 60 + (rng() - 0.5) * 35;
      
      var x = Math.round(150 + Math.cos(angle) * radius * spread);
      var y = Math.round(150 + Math.sin(angle) * radius);

      // Clamp within 300x300 bounding box
      x = Math.max(30, Math.min(270, x));
      y = Math.max(30, Math.min(270, y));

      stars.push({
        n: i + 1,
        x: x,
        y: y,
        magnitude: 2.5 + rng() * 2.0
      });
    }

    // Connect stars in a natural tree or path
    var lines = [];
    for (var j = 0; j < stars.length - 1; j++) {
      lines.push([j, j + 1]);
    }
    // Occasional cross-branch for constellations with > 4 stars
    if (stars.length >= 5 && rng() > 0.4) {
      lines.push([0, 2]);
    }
    if (stars.length >= 6 && rng() > 0.5) {
      lines.push([1, stars.length - 1]);
    }

    return { stars: stars, lines: lines };
  }

  // Default empty state
  function createDefaultState() {
    return {
      version: 2,
      user: {
        name: 'Reader',
        avatar: '✦',
        created_at: new Date().toISOString()
      },
      stars: {
        total: 0,
        // book_id: [chapter_numbers]
        collected: {}
      },
      constellations: {
        // book_id: { completed: bool, completed_at: string, stars_count: int, total_chapters: int }
        completed: {},
        in_progress: {}
      },
      tonight: {
        date: getTodayString(),
        stars_lit_today: 0,
        playlist: [], // [ { book_id, chapter_n, finished } ]
        completed_screen_shown: false
      },
      streak: {
        nights: 1,
        last_active_date: getTodayString(),
        history: [getTodayString()]
      },
      bookmarks: [],
      likes: [],
      settings: {
        textSize: 'M',
        reducedMotion: false,
        demoMode: false
      }
    };
  }

  function getTodayString() {
    return new Date().toISOString().split('T')[0];
  }

  // Demo Profile State for "?demo=1"
  function createDemoProfile() {
    var state = createDefaultState();
    state.user.name = 'Curious Reader';
    state.user.avatar = '✦';
    state.settings.demoMode = true;
    state.streak.nights = 12;
    state.stars.total = 42;

    // Completed Constellations (2)
    state.constellations.completed['atomic-habits'] = {
      completed: true,
      completed_at: new Date(Date.now() - 86400000 * 2).toISOString(),
      stars_count: 6,
      total_chapters: 6
    };
    state.stars.collected['atomic-habits'] = [1, 2, 3, 4, 5, 6];

    state.constellations.completed['meditations'] = {
      completed: true,
      completed_at: new Date(Date.now() - 86400000 * 4).toISOString(),
      stars_count: 6,
      total_chapters: 6
    };
    state.stars.collected['meditations'] = [1, 2, 3, 4, 5, 6];

    // Constellations in Progress
    state.constellations.in_progress['dune'] = {
      stars_count: 4,
      total_chapters: 6
    };
    state.stars.collected['dune'] = [1, 2, 3, 4];

    state.constellations.in_progress['the-psychology-of-money'] = {
      stars_count: 3,
      total_chapters: 6
    };
    state.stars.collected['the-psychology-of-money'] = [1, 2, 3];

    state.constellations.in_progress['1984-george-orwell'] = {
      stars_count: 4,
      total_chapters: 6
    };
    state.stars.collected['1984-george-orwell'] = [1, 2, 3, 4];

    state.constellations.in_progress['deep-work'] = {
      stars_count: 5,
      total_chapters: 6
    };
    state.stars.collected['deep-work'] = [1, 2, 3, 4, 5];

    state.constellations.in_progress['siddhartha'] = {
      stars_count: 5,
      total_chapters: 6
    };
    state.stars.collected['siddhartha'] = [1, 2, 3, 4, 5];

    state.constellations.in_progress['frankenstein'] = {
      stars_count: 4,
      total_chapters: 6
    };
    state.stars.collected['frankenstein'] = [1, 2, 3, 4];

    state.constellations.in_progress['the-courage-to-be-disliked'] = {
      stars_count: 5,
      total_chapters: 6
    };
    state.stars.collected['the-courage-to-be-disliked'] = [1, 2, 3, 4, 5];

    // Tonight's Sky (3 lit, 2 remaining)
    state.tonight.stars_lit_today = 3;
    state.tonight.playlist = [
      { book_id: 'dune', chapter_n: 5, finished: false },
      { book_id: 'the-psychology-of-money', chapter_n: 4, finished: false },
      { book_id: 'deep-work', chapter_n: 6, finished: true },
      { book_id: 'siddhartha', chapter_n: 6, finished: true },
      { book_id: 'the-courage-to-be-disliked', chapter_n: 6, finished: true }
    ];

    return state;
  }

  // Main Engine Class
  function RabbitSkyEngine() {
    this.state = null;
    this.init();
  }

  RabbitSkyEngine.prototype.init = function() {
    var isDemo = false;
    try {
      var params = new URLSearchParams(window.location.search);
      isDemo = params.get('demo') === '1';
    } catch(e) {}

    if (isDemo) {
      this.state = createDemoProfile();
      this.save();
      return;
    }

    // Try loading existing state
    var raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      try {
        this.state = JSON.parse(raw);
      } catch(e) {
        console.warn('Failed to parse rabbit_sky_v2, resetting:', e);
      }
    }

    if (!this.state) {
      this.state = createDefaultState();
      this.migrateLegacy();
      this.save();
    }

    // Refresh streak and tonight playlist on daily boundary
    this.checkDayRoll();
  };

  RabbitSkyEngine.prototype.save = function() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.state));
    } catch(e) {
      console.error('LocalStorage write error in RabbitSkyEngine:', e);
    }
  };

  // Migrate legacy rabbit_taste_v101
  RabbitSkyEngine.prototype.migrateLegacy = function() {
    var legacyRaw = localStorage.getItem(LEGACY_KEY);
    if (!legacyRaw) return;

    try {
      var legacy = JSON.parse(legacyRaw);
      console.log('Migrating legacy reader taste data to Sky v2...');
      var readBooks = legacy.readBooks || legacy.completedBooks || [];
      if (Array.isArray(readBooks)) {
        for (var i = 0; i < readBooks.length; i++) {
          var bId = readBooks[i];
          if (typeof bId === 'string') {
            this.state.stars.collected[bId] = [1, 2, 3];
            this.state.constellations.in_progress[bId] = {
              stars_count: 3,
              total_chapters: 6
            };
            this.state.stars.total += 3;
          }
        }
      }
      if (legacy.streak && legacy.streak > 1) {
        this.state.streak.nights = Math.max(this.state.streak.nights, legacy.streak);
      }
    } catch(e) {
      console.warn('Legacy migration error:', e);
    }
  };

  // Check day change
  RabbitSkyEngine.prototype.checkDayRoll = function() {
    var today = getTodayString();
    if (this.state.tonight.date !== today) {
      this.state.tonight.date = today;
      this.state.tonight.stars_lit_today = 0;
      this.state.tonight.completed_screen_shown = false;
      this.state.tonight.playlist = [];
      this.save();
    }

    // Streak checking
    var lastActive = this.state.streak.last_active_date;
    if (lastActive && lastActive !== today) {
      var diffDays = Math.round((new Date(today) - new Date(lastActive)) / 86400000);
      if (diffDays > 1) {
        // Streak broken
        this.state.streak.nights = 1;
      }
    }
  };

  /**
   * Collects a star when Card 5 is reached
   * @param {string} bookId
   * @param {number} chapterN
   * @param {number} totalChapters
   * @returns {Object} { isNewStar, constellationCompleted, starsTotal }
   */
  RabbitSkyEngine.prototype.collectStar = function(bookId, chapterN, totalChapters) {
    if (!bookId || !chapterN) return { isNewStar: false };

    this.state.stars.collected[bookId] = this.state.stars.collected[bookId] || [];
    var isNewStar = false;

    if (this.state.stars.collected[bookId].indexOf(chapterN) === -1) {
      this.state.stars.collected[bookId].push(chapterN);
      this.state.stars.total++;
      this.state.tonight.stars_lit_today++;
      isNewStar = true;

      // Update active streak
      var today = getTodayString();
      if (this.state.streak.last_active_date !== today) {
        this.state.streak.nights++;
        this.state.streak.last_active_date = today;
        if (this.state.streak.history.indexOf(today) === -1) {
          this.state.streak.history.push(today);
        }
      }

      // Check in Tonight's playlist
      if (Array.isArray(this.state.tonight.playlist)) {
        for (var p = 0; p < this.state.tonight.playlist.length; p++) {
          var item = this.state.tonight.playlist[p];
          if (item.book_id === bookId && item.chapter_n === chapterN) {
            item.finished = true;
          }
        }
      }
    }

    // Check Constellation completion
    var collectedCount = this.state.stars.collected[bookId].length;
    var totalNeeded = totalChapters || 6;
    var constellationCompleted = false;

    if (collectedCount >= totalNeeded && !this.state.constellations.completed[bookId]) {
      this.state.constellations.completed[bookId] = {
        completed: true,
        completed_at: new Date().toISOString(),
        stars_count: collectedCount,
        total_chapters: totalNeeded
      };
      delete this.state.constellations.in_progress[bookId];
      constellationCompleted = true;
    } else if (!this.state.constellations.completed[bookId]) {
      this.state.constellations.in_progress[bookId] = {
        stars_count: collectedCount,
        total_chapters: totalNeeded
      };
    }

    this.save();

    // Trigger custom events for UI
    try {
      window.dispatchEvent(new CustomEvent('rabbit:star-collected', {
        detail: {
          bookId: bookId,
          chapterN: chapterN,
          isNewStar: isNewStar,
          constellationCompleted: constellationCompleted,
          totalStars: this.state.stars.total,
          nights: this.state.streak.nights
        }
      }));

      if (constellationCompleted) {
        window.dispatchEvent(new CustomEvent('rabbit:constellation-completed', {
          detail: { bookId: bookId }
        }));
      }

      if (this.state.tonight.stars_lit_today >= 5 && !this.state.tonight.completed_screen_shown) {
        this.state.tonight.completed_screen_shown = true;
        this.save();
        window.dispatchEvent(new CustomEvent('rabbit:tonight-completed', {
          detail: { count: this.state.tonight.stars_lit_today }
        }));
      }
    } catch(e) {}

    return {
      isNewStar: isNewStar,
      constellationCompleted: constellationCompleted,
      starsTotal: this.state.stars.total
    };
  };

  /**
   * Generates or retrieves Tonight's Sky 5-chapter playlist
   * @param {Array} catalog
   * @returns {Array} 5 chapters
   */
  RabbitSkyEngine.prototype.getTonightPlaylist = function(catalog) {
    if (this.state.tonight.playlist && this.state.tonight.playlist.length === 5) {
      return this.state.tonight.playlist;
    }

    var playlist = [];
    var books = catalog || (window.RABBIT_CATALOG || []);
    if (!books.length) return playlist;

    // Pick 5 high-quality hero chapters or in-progress chapters
    var seedStr = 'tonight-' + getTodayString();
    var rng = hashSeed(seedStr);

    var samplePool = books.filter(function(b) {
      return b.chapters && b.chapters.length >= 3;
    });

    var chosenBookIds = {};
    while (playlist.length < 5 && samplePool.length > 0) {
      var bIdx = Math.floor(rng() * samplePool.length);
      var book = samplePool[bIdx];
      if (!chosenBookIds[book.id]) {
        chosenBookIds[book.id] = true;
        // Pick next unread chapter or chapter 1
        var collected = (this.state.stars.collected[book.id] || []);
        var nextCh = 1;
        for (var c = 1; c <= book.chapters.length; c++) {
          if (collected.indexOf(c) === -1) {
            nextCh = c;
            break;
          }
        }
        playlist.push({
          book_id: book.id,
          chapter_n: nextCh,
          finished: collected.indexOf(nextCh) !== -1
        });
      }
      samplePool.splice(bIdx, 1);
    }

    this.state.tonight.playlist = playlist;
    this.save();
    return playlist;
  };

  // Local metric tracker for "Find this book" clicks
  RabbitSkyEngine.prototype.trackMetric = function(action, meta) {
    try {
      var raw = localStorage.getItem(METRICS_KEY);
      var metrics = raw ? JSON.parse(raw) : { events: [] };
      metrics.events.push({
        action: action,
        meta: meta || {},
        timestamp: new Date().toISOString()
      });
      // Cap at 200 events
      if (metrics.events.length > 200) {
        metrics.events.shift();
      }
      localStorage.setItem(METRICS_KEY, JSON.stringify(metrics));
    } catch(e) {}
  };

  // Static constellation generator export
  RabbitSkyEngine.generateConstellation = generateConstellation;
  RabbitSkyEngine.getGenrePalette = getGenrePalette;
  RabbitSkyEngine.GENRE_PALETTES = GENRE_PALETTES;

  window.RabbitSkyEngine = RabbitSkyEngine;

  // Initialize global singleton
  window.rabbitSky = new RabbitSkyEngine();

})(window);
