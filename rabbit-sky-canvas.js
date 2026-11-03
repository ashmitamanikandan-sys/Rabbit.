/**
 * RABBIT 2.0 — The Sky: Celestial Constellation Canvas (rabbit-sky-canvas.js)
 * High-DPI interactive night sky map featuring:
 * - Deterministic book constellations clustered by genre regions
 * - Touch & mouse pan/zoom navigation
 * - Star glow states (collected vs guide stars)
 * - Constellation line drawing
 * - Click-to-inspect constellation modal with chapter checklist
 * - Elegant completion celebration
 */

(function(window) {
  'use strict';

  function RabbitSkyCanvas(containerId) {
    this.container = document.getElementById(containerId);
    if (!this.container) return;

    this.canvas = document.createElement('canvas');
    this.ctx = this.canvas.getContext('2d');
    this.container.appendChild(this.canvas);

    // Camera view state
    this.camera = {
      x: 0,
      y: 0,
      zoom: 1.0,
      minZoom: 0.5,
      maxZoom: 2.5
    };

    this.isDragging = false;
    this.lastMouse = { x: 0, y: 0 };
    this.constellationNodes = []; // hit test targets

    this.init();
  }

  RabbitSkyCanvas.prototype.init = function() {
    this.resize();
    window.addEventListener('resize', this.resize.bind(this));

    this.setupInteraction();
    this.buildConstellationMap();
    this.render();

    // Listen for completion celebrations
    var self = this;
    window.addEventListener('rabbit:constellation-completed', function(e) {
      self.celebrateConstellation(e.detail.bookId);
    });
  };

  RabbitSkyCanvas.prototype.resize = function() {
    var rect = this.container.getBoundingClientRect();
    var dpr = window.devicePixelRatio || 1;
    this.width = rect.width || window.innerWidth;
    this.height = rect.height || (window.innerHeight - 130);

    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.canvas.style.width = this.width + 'px';
    this.canvas.style.height = this.height + 'px';

    this.ctx.scale(dpr, dpr);
    this.render();
  };

  // Build spatial layout of constellations grouped by genre regions
  RabbitSkyCanvas.prototype.buildConstellationMap = function() {
    this.constellationNodes = [];
    var catalog = window.RABBIT_CATALOG || [];
    var state = window.rabbitSky ? window.rabbitSky.state : null;
    var collected = (state && state.stars.collected) || {};
    var completed = (state && state.constellations.completed) || {};

    // Region center points (celestial hemisphere)
    var REGION_CENTERS = {
      'the human mind': { x: -450, y: -250 },
      'self discovery': { x: 450, y: -250 },
      'science fiction': { x: 0, y: -500 },
      'philosophy': { x: -350, y: 350 },
      'classics': { x: 350, y: 350 },
      'history': { x: 0, y: 550 },
      'general': { x: 0, y: 0 }
    };

    var genreOffsets = {};

    for (var i = 0; i < catalog.length; i++) {
      var book = catalog[i];
      var gkey = (book.genre || 'general').toLowerCase().trim();
      var center = REGION_CENTERS[gkey] || REGION_CENTERS['general'];

      genreOffsets[gkey] = genreOffsets[gkey] || 0;
      var offsetIdx = genreOffsets[gkey]++;

      // Spiral placement around region center
      var angle = offsetIdx * 0.95;
      var dist = 90 + offsetIdx * 38;
      var cx = center.x + Math.cos(angle) * dist;
      var cy = center.y + Math.sin(angle) * dist;

      var totalChapters = book.chapters ? book.chapters.length : 6;
      var constellation = window.RabbitSkyEngine.generateConstellation(book.id, totalChapters);
      var starsLit = collected[book.id] || [];
      var isCompleted = !!completed[book.id] || (starsLit.length >= totalChapters);

      this.constellationNodes.push({
        book: book,
        centerX: cx,
        centerY: cy,
        constellation: constellation,
        starsLit: starsLit,
        isCompleted: isCompleted,
        palette: window.RabbitSkyEngine.getGenrePalette(book.genre)
      });
    }
  };

  RabbitSkyCanvas.prototype.setupInteraction = function() {
    var self = this;

    // Mouse drag
    this.canvas.addEventListener('mousedown', function(e) {
      self.isDragging = true;
      self.lastMouse = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener('mousemove', function(e) {
      if (!self.isDragging) return;
      var dx = e.clientX - self.lastMouse.x;
      var dy = e.clientY - self.lastMouse.y;
      self.camera.x += dx / self.camera.zoom;
      self.camera.y += dy / self.camera.zoom;
      self.lastMouse = { x: e.clientX, y: e.clientY };
      self.render();
    });

    window.addEventListener('mouseup', function() {
      self.isDragging = false;
    });

    // Touch drag & pinch zoom
    var initialTouchDist = null;
    this.canvas.addEventListener('touchstart', function(e) {
      if (e.touches.length === 1) {
        self.isDragging = true;
        self.lastMouse = { x: e.touches[0].clientX, y: e.touches[0].clientY };
      } else if (e.touches.length === 2) {
        self.isDragging = false;
        initialTouchDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
      }
    }, { passive: true });

    this.canvas.addEventListener('touchmove', function(e) {
      if (e.touches.length === 1 && self.isDragging) {
        var dx = e.touches[0].clientX - self.lastMouse.x;
        var dy = e.touches[0].clientY - self.lastMouse.y;
        self.camera.x += dx / self.camera.zoom;
        self.camera.y += dy / self.camera.zoom;
        self.lastMouse = { x: e.touches[0].clientX, y: e.touches[0].clientY };
        self.render();
      } else if (e.touches.length === 2 && initialTouchDist) {
        var currentDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        var factor = currentDist / initialTouchDist;
        self.camera.zoom = Math.max(self.camera.minZoom, Math.min(self.camera.maxZoom, self.camera.zoom * factor));
        initialTouchDist = currentDist;
        self.render();
      }
    }, { passive: true });

    this.canvas.addEventListener('touchend', function() {
      self.isDragging = false;
      initialTouchDist = null;
    });

    // Mouse wheel zoom
    this.canvas.addEventListener('wheel', function(e) {
      e.preventDefault();
      var zoomFactor = e.deltaY < 0 ? 1.1 : 0.9;
      self.camera.zoom = Math.max(self.camera.minZoom, Math.min(self.camera.maxZoom, self.camera.zoom * zoomFactor));
      self.render();
    }, { passive: false });

    // Click to inspect constellation
    this.canvas.addEventListener('click', function(e) {
      var rect = self.canvas.getBoundingClientRect();
      var clickX = (e.clientX - rect.left - self.width / 2) / self.camera.zoom - self.camera.x;
      var clickY = (e.clientY - rect.top - self.height / 2) / self.camera.zoom - self.camera.y;

      // Find clicked constellation
      for (var i = 0; i < self.constellationNodes.length; i++) {
        var node = self.constellationNodes[i];
        var dist = Math.hypot(clickX - node.centerX, clickY - node.centerY);
        if (dist < 75) {
          self.openConstellationModal(node);
          return;
        }
      }
    });
  };

  // Render Night Sky Canvas
  RabbitSkyCanvas.prototype.render = function() {
    var ctx = this.ctx;
    var w = this.width;
    var h = this.height;

    // Clear dark space background
    ctx.save();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.fillStyle = '#050408';
    ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    ctx.restore();

    ctx.save();
    // Center camera
    ctx.translate(w / 2, h / 2);
    ctx.scale(this.camera.zoom, this.camera.zoom);
    ctx.translate(this.camera.x, this.camera.y);

    // Draw ambient cosmic nebulae / genre regions
    this.drawNebulae(ctx);

    // Draw background guide stars
    this.drawBackgroundStars(ctx);

    // Draw Constellations
    for (var i = 0; i < this.constellationNodes.length; i++) {
      var node = this.constellationNodes[i];
      // Frustum culling
      var screenX = (node.centerX + this.camera.x) * this.camera.zoom + w / 2;
      var screenY = (node.centerY + this.camera.y) * this.camera.zoom + h / 2;
      if (screenX < -200 || screenX > w + 200 || screenY < -200 || screenY > h + 200) {
        continue;
      }

      this.drawConstellation(ctx, node);
    }

    ctx.restore();
  };

  // Ambient Genre Nebulae
  RabbitSkyCanvas.prototype.drawNebulae = function(ctx) {
    var regions = [
      { x: -450, y: -250, color: 'rgba(45, 212, 191, 0.08)', radius: 320 }, // Mind
      { x: 450, y: -250, color: 'rgba(251, 113, 133, 0.08)', radius: 320 }, // Self
      { x: 0, y: -500, color: 'rgba(96, 165, 250, 0.08)', radius: 340 },   // Sci-Fi
      { x: -350, y: 350, color: 'rgba(192, 132, 252, 0.08)', radius: 300 }, // Philosophy
      { x: 350, y: 350, color: 'rgba(52, 211, 153, 0.08)', radius: 300 }   // Classics
    ];

    for (var i = 0; i < regions.length; i++) {
      var r = regions[i];
      var grad = ctx.createRadialGradient(r.x, r.y, 10, r.x, r.y, r.radius);
      grad.addColorStop(0, r.color);
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(r.x, r.y, r.radius, 0, Math.PI * 2);
      ctx.fill();
    }
  };

  // Background guide stars
  RabbitSkyCanvas.prototype.drawBackgroundStars = function(ctx) {
    ctx.fillStyle = 'rgba(255, 255, 255, 0.25)';
    var rng = window.RabbitSkyEngine.getGenrePalette ? hashSeed('sky-bg-stars') : Math.random;
    for (var i = 0; i < 180; i++) {
      var sx = (rng() - 0.5) * 2200;
      var sy = (rng() - 0.5) * 2200;
      var sr = 0.5 + rng() * 1.2;
      ctx.beginPath();
      ctx.arc(sx, sy, sr, 0, Math.PI * 2);
      ctx.fill();
    }
  };

  // Draw 1 Constellation
  RabbitSkyCanvas.prototype.drawConstellation = function(ctx, node) {
    var stars = node.constellation.stars;
    var lines = node.constellation.lines;
    var palette = node.palette;
    var starsLit = node.starsLit;
    var isComp = node.isCompleted;

    var scale = 0.45; // scale 300x300 bounding box to fit sky map
    var offsetX = node.centerX - 150 * scale;
    var offsetY = node.centerY - 150 * scale;

    // 1. Draw Connecting Lines
    ctx.lineWidth = isComp ? 1.5 : 0.8;
    for (var l = 0; l < lines.length; l++) {
      var s1 = stars[lines[l][0]];
      var s2 = stars[lines[l][1]];
      var lit1 = starsLit.indexOf(s1.n) !== -1;
      var lit2 = starsLit.indexOf(s2.n) !== -1;

      var x1 = offsetX + s1.x * scale;
      var y1 = offsetY + s1.y * scale;
      var x2 = offsetX + s2.x * scale;
      var y2 = offsetY + s2.y * scale;

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);

      if (isComp) {
        ctx.strokeStyle = palette.color;
        ctx.shadowColor = palette.color;
        ctx.shadowBlur = 8;
      } else if (lit1 && lit2) {
        ctx.strokeStyle = 'rgba(188, 166, 255, 0.5)';
        ctx.shadowBlur = 0;
      } else {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
        ctx.shadowBlur = 0;
      }
      ctx.stroke();
    }
    ctx.shadowBlur = 0;

    // 2. Draw Stars
    for (var s = 0; s < stars.length; s++) {
      var star = stars[s];
      var isLit = starsLit.indexOf(star.n) !== -1;
      var sx = offsetX + star.x * scale;
      var sy = offsetY + star.y * scale;
      var r = isLit ? (star.magnitude + 1.2) : star.magnitude * 0.7;

      ctx.beginPath();
      ctx.arc(sx, sy, r, 0, Math.PI * 2);

      if (isLit) {
        ctx.fillStyle = '#FFFFFF';
        ctx.shadowColor = palette.color;
        ctx.shadowBlur = 12;
        ctx.fill();

        // Star sparkle cross
        ctx.strokeStyle = palette.color;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(sx - r * 1.8, sy);
        ctx.lineTo(sx + r * 1.8, sy);
        ctx.moveTo(sx, sy - r * 1.8);
        ctx.lineTo(sx, sy + r * 1.8);
        ctx.stroke();
      } else {
        ctx.fillStyle = 'rgba(255, 255, 255, 0.22)';
        ctx.shadowBlur = 0;
        ctx.fill();
      }
    }
    ctx.shadowBlur = 0;

    // 3. Constellation Label (fades in when progress > 0)
    if (starsLit.length > 0 || this.camera.zoom > 1.3) {
      ctx.font = '600 11px -apple-system, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillStyle = isComp ? '#FFFFFF' : 'rgba(255, 255, 255, 0.55)';
      ctx.fillText(node.book.title, node.centerX, node.centerY + 55);
    }
  };

  // Open Inspection Modal
  RabbitSkyCanvas.prototype.openConstellationModal = function(node) {
    var modal = document.getElementById('constellation-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'constellation-modal';
      modal.className = 'rabbit-constellation-modal';
      document.body.appendChild(modal);
    }

    var book = node.book;
    var total = book.chapters ? book.chapters.length : 6;
    var lit = node.starsLit.length;
    var pct = Math.round((lit / total) * 100);

    var html = '<div class="constellation-modal-content">';
    html += '  <button class="modal-close-btn" onclick="document.getElementById(\'constellation-modal\').classList.remove(\'open\')">✕</button>';
    html += '  <div class="cmodal-header">';
    html += '    <img class="cmodal-cover" src="' + (book.cover_url || '') + '" alt="' + escapeHtml(book.title) + '">';
    html += '    <div>';
    html += '      <span style="font-size:10px;font-weight:700;color:' + node.palette.color + ';letter-spacing:1px;text-transform:uppercase;">' + escapeHtml(book.genre) + '</span>';
    html += '      <h2 style="font-size:20px;margin:4px 0;color:#fff;">' + escapeHtml(book.title) + '</h2>';
    html += '      <p style="font-size:12px;color:#9E96B0;margin:0;">by ' + escapeHtml(book.author) + '</p>';
    html += '      <div style="font-size:13px;font-weight:700;color:#FBBF24;margin-top:8px;">' + (node.isCompleted ? '✦ Constellation Completed' : lit + ' / ' + total + ' Stars Lit (' + pct + '%)') + '</div>';
    html += '    </div>';
    html += '  </div>';

    html += '  <h3 style="font-size:14px;color:#BCA6FF;margin:20px 0 10px 0;text-transform:uppercase;letter-spacing:0.8px;">Chapters in this Constellation</h3>';
    html += '  <div class="cmodal-chapters-list">';
    var chapters = book.chapters || [];
    for (var c = 0; c < chapters.length; c++) {
      var ch = chapters[c];
      var isLit = node.starsLit.indexOf(ch.n) !== -1;
      html += '    <div class="cmodal-chapter-row ' + (isLit ? 'lit' : '') + '" onclick="window.jumpToBookDeck(\'' + book.id + '\', ' + ch.n + '); document.getElementById(\'constellation-modal\').classList.remove(\'open\');">';
      html += '      <span class="cmodal-ch-star">' + (isLit ? '✦' : '✧') + '</span>';
      html += '      <div class="cmodal-ch-info">';
      html += '        <strong>Ch ' + ch.n + ': ' + escapeHtml(ch.title) + '</strong>';
      html += '        <small>' + escapeHtml(ch.hook || '') + '</small>';
      html += '      </div>';
      html += '      <span class="cmodal-ch-action">' + (isLit ? 'Lit' : 'Read →') + '</span>';
      html += '    </div>';
    }
    html += '  </div>';
    html += '</div>';

    modal.innerHTML = html;
    modal.classList.add('open');
  };

  // Constellation Completion Celebration (lines draw, title fades in, soft glow, no confetti)
  RabbitSkyCanvas.prototype.celebrateConstellation = function(bookId) {
    var self = this;
    for (var i = 0; i < this.constellationNodes.length; i++) {
      if (this.constellationNodes[i].book.id === bookId) {
        var node = this.constellationNodes[i];
        node.isCompleted = true;
        // Smoothly pan camera to this constellation
        self.camera.x = -node.centerX;
        self.camera.y = -node.centerY;
        self.camera.zoom = 1.6;
        self.render();
        break;
      }
    }
  };

  function escapeHtml(str) {
    if (!str) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  window.RabbitSkyCanvas = RabbitSkyCanvas;

})(window);
