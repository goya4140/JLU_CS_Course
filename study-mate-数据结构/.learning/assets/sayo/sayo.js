/* ═══════════════════════════════════════════════════════════════
   SAYO UI — ELASTIC INTERACTION ENGINE
   Zero dependencies. Modular. Attribute-driven or JS API.
   ═══════════════════════════════════════════════════════════════ */

(function(global) {
  'use strict';

  /* ── UTILITIES ──────────────────────────────────────────────── */
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.from((ctx || document).querySelectorAll(sel)); }
  function on(el, evt, fn, opts) { el.addEventListener(evt, fn, opts); }
  function off(el, evt, fn, opts) { el.removeEventListener(evt, fn, opts); }
  function remove(el) { if (el && el.parentNode) el.parentNode.removeChild(el); }

  var raf = requestAnimationFrame.bind(window);
  var now = performance.now.bind(performance);
  var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── NAMESPACE ──────────────────────────────────────────────── */
  var Sayo = global.Sayo || {};

  /* ═══════════════════════════════════════════════════════════════
     CURSOR MODULE — global custom cursor ring + ambient glow
     Trigger: body[data-syo-cursor] or Sayo.cursor.init()
     ═══════════════════════════════════════════════════════════════ */
  Sayo.cursor = (function() {
    var el, canvas, ctx;
    var cx = -200, cy = -200;
    var pressing = false;
    var glowRadius = 40;
    var targetGlow = 40;
    var running = false;
    var idleTimer = null;
    var IDLE_TIMEOUT = 2000;  // stop rAF after 2s of no mouse movement

    // Configurable defaults
    var DEFAULTS = {
      size: 16,
      pressSize: 26,
      glowNormal: 40,
      glowHover: 50,
      glowPress: 70,
      glowIntensity: 0.08,
      glowIntensityHover: 0.14,
      glowIntensityPress: 0.18,
      accentR: 88, accentG: 166, accentB: 255,   // #58a6ff
      trailR: 121, trailG: 192, trailB: 255,     // #79c0ff
    };

    var cfg = {};

    var INTERACTIVE = 'a,button,input,select,textarea,[role="button"],.syo-btn,.syo-tab,.syo-dropdown-item,.syo-dropdown-toggle,.syo-tooltip,.syo-toggle,label.syo-checkbox,label.syo-radio,[onclick]';

    function isInteractive(x, y) {
      var el = document.elementFromPoint(x, y);
      if (!el || el === document.documentElement || el === document.body) return false;
      return el.matches(INTERACTIVE) || el.closest(INTERACTIVE);
    }

    function initCanvas() {
      canvas = document.createElement('canvas');
      canvas.id = 'syo-cursor-canvas';
      canvas.style.cssText =
        'position:fixed;inset:0;pointer-events:none;z-index:19999;';
      document.body.appendChild(canvas);
      ctx = canvas.getContext('2d');
      resize();
    }

    function initCursorEl() {
      el = document.createElement('div');
      el.id = 'syo-cursor';
      el.setAttribute('aria-hidden', 'true');
      el.style.cssText =
        'position:fixed;pointer-events:none;z-index:20000;' +
        'border-radius:50%;transform:translate(-50%,-50%);' +
        'width:' + cfg.size + 'px;height:' + cfg.size + 'px;' +
        'border:1.5px solid #c9d1d9;' +
        'background:rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.1);' +
        'box-shadow:0 0 8px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.2),' +
        '0 0 3px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.1);' +
        'transition:width 120ms cubic-bezier(0.34,1.56,0.64,1),' +
        'height 120ms cubic-bezier(0.34,1.56,0.64,1),' +
        'border-width 120ms cubic-bezier(0.34,1.56,0.64,1),' +
        'background 120ms ease-out,box-shadow 200ms ease-out;';
      document.body.appendChild(el);
    }

    function resize() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }

    function setSize(size) {
      el.style.width = size + 'px';
      el.style.height = size + 'px';
    }

    var hovering = false;

    function onMove(e) {
      cx = e.clientX;
      cy = e.clientY;
      el.style.left = cx + 'px';
      el.style.top = cy + 'px';

      // Detect interactive elements — expand ring instead of showing system cursor
      var overInteractive = !pressing && isInteractive(cx, cy);
      if (overInteractive && !hovering) {
        hovering = true;
        // Quick bounce: 16 → 22 → 16
        el.style.transition = 'width 80ms cubic-bezier(0.34,1.56,0.64,1), height 80ms cubic-bezier(0.34,1.56,0.64,1)';
        el.style.width = '22px';
        el.style.height = '22px';
        (function() {
          var settled = false;
          function settle() {
            if (settled) return;
            settled = true;
            if (!el) return; // destroyed mid-bounce
            el.style.transition = 'width 120ms cubic-bezier(0.34,1.56,0.64,1), height 120ms cubic-bezier(0.34,1.56,0.64,1)';
            el.style.width = cfg.size + 'px';
            el.style.height = cfg.size + 'px';
            setTimeout(function() { if (el) el.style.transition = ''; }, 140);
          }
          setTimeout(settle, 70);
        })();
        targetGlow = cfg.glowHover;
        el.style.borderWidth = '2px';
        el.style.borderColor = 'rgba(' + cfg.trailR + ',' + cfg.trailG + ',' + cfg.trailB + ',0.9)';
        el.style.background = 'rgba(' + cfg.trailR + ',' + cfg.trailG + ',' + cfg.trailB + ',0.15)';
        el.style.boxShadow =
          '0 0 16px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.3),' +
          '0 0 6px rgba(' + cfg.trailR + ',' + cfg.trailG + ',' + cfg.trailB + ',0.2)';
      } else if (!overInteractive && hovering && !pressing) {
        hovering = false;
        targetGlow = cfg.glowNormal;
        el.style.width = cfg.size + 'px';
        el.style.height = cfg.size + 'px';
        el.style.borderWidth = '1.5px';
        el.style.borderColor = '#c9d1d9';
        el.style.background = 'rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.1)';
        el.style.boxShadow =
          '0 0 8px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.2),' +
          '0 0 3px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.1)';
      }

      // Restart rAF if idle-timed out
      if (!running && !isReducedMotion) { running = true; raf(draw); }
      // Reset idle timer
      clearTimeout(idleTimer);
      idleTimer = setTimeout(function() { running = false; }, IDLE_TIMEOUT);
    }

    function onDown() {
      pressing = true;
      el.style.transition = ''; // instant, no bounce
      targetGlow = cfg.glowPress;
      el.style.width = cfg.pressSize + 'px';
      el.style.height = cfg.pressSize + 'px';
      el.style.borderWidth = '2.5px';
      el.style.background = 'rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.25)';
      el.style.boxShadow =
        '0 0 20px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.4),' +
        '0 0 8px rgba(' + cfg.trailR + ',' + cfg.trailG + ',' + cfg.trailB + ',0.2)';
    }

    function onUp() {
      pressing = false;
      el.style.transition = '';
      if (isInteractive(cx, cy)) {
        hovering = true;
        targetGlow = cfg.glowHover;
        el.style.width = cfg.size + 'px';
        el.style.height = cfg.size + 'px';
        el.style.borderWidth = '2px';
        el.style.borderColor = 'rgba(' + cfg.trailR + ',' + cfg.trailG + ',' + cfg.trailB + ',0.9)';
        el.style.background = 'rgba(' + cfg.trailR + ',' + cfg.trailG + ',' + cfg.trailB + ',0.15)';
        el.style.boxShadow =
          '0 0 16px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.3),' +
          '0 0 6px rgba(' + cfg.trailR + ',' + cfg.trailG + ',' + cfg.trailB + ',0.2)';
      } else {
        hovering = false;
        targetGlow = cfg.glowNormal;
        el.style.width = cfg.size + 'px';
        el.style.height = cfg.size + 'px';
        el.style.borderWidth = '1.5px';
        el.style.background = 'rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.1)';
        el.style.boxShadow =
          '0 0 8px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.2),' +
          '0 0 3px rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',0.1)';
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Smooth glow radius
      if (Math.abs(glowRadius - targetGlow) > 0.5) {
        glowRadius += (targetGlow - glowRadius) * 0.15;
      }

      // Ambient glow
      if (cx > 0 && cy > 0) {
        var intensity = pressing ? cfg.glowIntensityPress : (hovering ? cfg.glowIntensityHover : cfg.glowIntensity);
        var glow = ctx.createRadialGradient(cx, cy, 0, cx, cy, glowRadius);
        glow.addColorStop(0, 'rgba(' + cfg.accentR + ',' + cfg.accentG + ',' + cfg.accentB + ',' + intensity.toFixed(2) + ')');
        glow.addColorStop(0.5, 'rgba(' + cfg.trailR + ',' + cfg.trailG + ',' + cfg.trailB + ',' + (intensity * 0.35).toFixed(2) + ')');
        glow.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.beginPath();
        ctx.arc(cx, cy, glowRadius, 0, Math.PI * 2);
        ctx.fillStyle = glow;
        ctx.fill();
      }

      if (running) raf(draw);
    }

    function init(opts) {
      if (running) return;
      cfg = Object.assign({}, DEFAULTS, opts || {});

      // Skip on touch-only devices (no pointer:fine → no cursor to replace)
      var isTouchOnly = !window.matchMedia('(pointer: fine)').matches;
      if (isTouchOnly) return;

      // Always create cursor element (essential — we hide system cursor)
      initCursorEl();
      on(document, 'mousemove', onMove);
      on(document, 'mousedown', onDown);
      on(document, 'mouseup', onUp);
      document.body.style.cursor = 'none';
      running = true;

      // Glow canvas + animation — skipped for reduced motion
      if (!isReducedMotion) {
        initCanvas();
        on(window, 'resize', resize);
        raf(draw);
      }
    }

    function destroy() {
      running = false;
      clearTimeout(idleTimer);
      remove(el); el = null;
      if (canvas) { remove(canvas); canvas = null; ctx = null; }
      off(document, 'mousemove', onMove);
      off(document, 'mousedown', onDown);
      off(document, 'mouseup', onUp);
      if (!isReducedMotion) {
        off(window, 'resize', resize);
      }
      document.body.style.cursor = '';
    }

    return { init: init, destroy: destroy };
  })();

  /* ═══════════════════════════════════════════════════════════════
     TRAIL MODULE — smooth polyline comet trail
     Trigger: body[data-syo-trail] or Sayo.trail.init({ container })
     ═══════════════════════════════════════════════════════════════ */
  Sayo.trail = (function() {
    var canvas, ctx;
    var trail = [];
    var running = false;
    var container = null; // null = global

    var DEFAULTS = {
      maxLength: 25,
      colorR: 121, colorG: 192, colorB: 255, // #79c0ff
      maxWidth: 5,
      maxAlpha: 0.28,
    };

    var cfg = {};

    function initCanvas() {
      canvas = document.createElement('canvas');
      canvas.id = 'syo-trail-canvas';
      canvas.style.cssText =
        'position:fixed;inset:0;pointer-events:none;z-index:19998;';
      document.body.appendChild(canvas);
      ctx = canvas.getContext('2d');
      resize();
    }

    function resize() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }

    function onMove(e) {
      if (container && !container.contains(e.target)) {
        trail = [];
        return;
      }
      trail.push({ x: e.clientX, y: e.clientY });
      if (trail.length > cfg.maxLength) trail.shift();
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (trail.length < 2) { if (running) raf(draw); return; }

      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';

      for (var i = 1; i < trail.length; i++) {
        var t = i / (trail.length - 1);
        ctx.beginPath();
        ctx.moveTo(trail[i - 1].x, trail[i - 1].y);
        ctx.lineTo(trail[i].x, trail[i].y);
        ctx.strokeStyle = 'rgba(' + cfg.colorR + ',' + cfg.colorG + ',' + cfg.colorB + ',' + (t * cfg.maxAlpha).toFixed(3) + ')';
        ctx.lineWidth = t * cfg.maxWidth;
        ctx.stroke();
      }

      if (running) raf(draw);
    }

    function init(opts) {
      if (running) return;
      if (isReducedMotion) return;
      if (!window.matchMedia('(pointer: fine)').matches) return; // touch-only device
      cfg = Object.assign({}, DEFAULTS, opts || {});
      if (cfg.container) {
        container = typeof cfg.container === 'string' ? $(cfg.container) : cfg.container;
      }
      initCanvas();
      on(document, 'mousemove', onMove);
      on(window, 'resize', resize);
      running = true;
      raf(draw);
    }

    function destroy() {
      running = false;
      trail = [];
      remove(canvas); canvas = null; ctx = null;
      off(document, 'mousemove', onMove);
      off(window, 'resize', resize);
    }

    return { init: init, destroy: destroy };
  })();

  /* ═══════════════════════════════════════════════════════════════
     RIPPLE MODULE — click ripple + flash
     Trigger: [data-syo-ripple] (container) or Sayo.ripple.init()
     ═══════════════════════════════════════════════════════════════ */
  Sayo.ripple = (function() {
    var target;
    var initialized = false;
    var DEFAULTS = { flashR: 88, flashG: 166, flashB: 255, rippleR: 188, rippleG: 140, rippleB: 255 };

    var cfg = {};

    function createFlash(x, y) {
      var el = document.createElement('div');
      el.style.cssText =
        'position:fixed;pointer-events:none;z-index:9998;' +
        'width:80px;height:80px;border-radius:50%;' +
        'left:' + x + 'px;top:' + y + 'px;' +
        'background:radial-gradient(circle,rgba(' + cfg.flashR + ',' + cfg.flashG + ',' + cfg.flashB + ',0.4) 0%,transparent 70%);' +
        'transform:translate(-50%,-50%);' +
        'animation:syo-flash-pulse 350ms cubic-bezier(0.4,0,0.2,1) forwards;';
      document.body.appendChild(el);
      setTimeout(function() { remove(el); }, 380);
    }

    function createRipple(x, y) {
      var el = document.createElement('div');
      el.style.cssText =
        'position:absolute;pointer-events:none;z-index:5;' +
        'border:2px solid rgba(' + cfg.rippleR + ',' + cfg.rippleG + ',' + cfg.rippleB + ',0.6);' +
        'border-radius:50%;left:' + x + 'px;top:' + y + 'px;' +
        'transform:translate(-50%,-50%);' +
        'animation:syo-ripple-expand 600ms cubic-bezier(0.4,0,0.2,1) forwards;';
      return el;
    }

    function onDown(e) {
      createFlash(e.clientX, e.clientY);

      // Ripple only if click is inside a [data-syo-ripple] container,
      // or an explicit init container. Must be a real Element —
      // document/window have no getBoundingClientRect and would throw.
      var rippleTarget = e.target.closest('[data-syo-ripple]');
      if (!rippleTarget && target && target.nodeType === 1 && target !== document.body) {
        rippleTarget = target;
      }
      if (rippleTarget) {
        var rect = rippleTarget.getBoundingClientRect();
        var ring = createRipple(e.clientX - rect.left, e.clientY - rect.top);
        rippleTarget.appendChild(ring);
        setTimeout(function() { remove(ring); }, 650);
      }
    }

    function init(opts) {
      if (isReducedMotion) return;
      if (initialized) return;
      initialized = true;
      cfg = Object.assign({}, DEFAULTS, opts || {});
      // If called without args and body has [data-syo-ripple], use body
      target = (opts && opts.container) ? (typeof opts.container === 'string' ? $(opts.container) : opts.container) : document;
      on(document, 'mousedown', onDown);
    }

    function destroy() {
      initialized = false;
      off(document, 'mousedown', onDown);
      target = null;
    }

    return { init: init, destroy: destroy };
  })();

  /* ═══════════════════════════════════════════════════════════════
     TOAST MODULE — elastic slide-in notifications
     Call: Sayo.toast.show('message', { type: 'success'|'error'|'info'|'warning', duration: 4000 })
     ═══════════════════════════════════════════════════════════════ */
  Sayo.toast = (function() {
    var container;

    var ICONS = {
      success: '<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="8" stroke="var(--syo-green)" stroke-width="1.5"/><path d="M6 10l3 3 5-5" stroke="var(--syo-green)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
      error: '<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="8" stroke="var(--syo-red)" stroke-width="1.5"/><path d="M7 7l6 6M13 7l-6 6" stroke="var(--syo-red)" stroke-width="1.5" stroke-linecap="round"/></svg>',
      info: '<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="8" stroke="var(--syo-blue)" stroke-width="1.5"/><path d="M10 9v5M10 6.5v0" stroke="var(--syo-blue)" stroke-width="1.5" stroke-linecap="round"/></svg>',
      warning: '<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M10 2L1 18h18L10 2z" stroke="var(--syo-yellow)" stroke-width="1.5" stroke-linejoin="round"/><path d="M10 8v4M10 14.5v0" stroke="var(--syo-yellow)" stroke-width="1.5" stroke-linecap="round"/></svg>',
    };

    function ensureContainer() {
      if (container && container.parentNode) return;
      container = document.getElementById('syo-toast-container');
      if (!container) {
        container = document.createElement('div');
        container.id = 'syo-toast-container';
        container.className = 'syo-toast-container';
        document.body.appendChild(container);
      }
    }

    function show(message, opts) {
      ensureContainer();
      var cfg = Object.assign({ type: 'info', duration: 4000 }, opts || {});

      var el = document.createElement('div');
      el.className = 'syo-toast syo-toast--' + cfg.type;

      var icon = ICONS[cfg.type] || ICONS.info;

      el.innerHTML =
        '<span class="syo-toast-icon">' + icon + '</span>' +
        '<span class="syo-toast-body">' + escapeHtml(message) + '</span>' +
        '<button class="syo-toast-close" aria-label="Close">&times;</button>';

      container.appendChild(el);

      var timer;

      function dismiss() {
        clearTimeout(timer);
        el.classList.add('is-dismissing');
        setTimeout(function() { remove(el); }, 260);
      }

      el.querySelector('.syo-toast-close').addEventListener('click', dismiss);

      if (cfg.duration > 0) {
        timer = setTimeout(dismiss, cfg.duration);
      }

      // Keep max 5 toasts — container uses column-reverse, so
      // DOM order: [0]=oldest at bottom, [last]=newest at top
      var toasts = container.querySelectorAll('.syo-toast');
      if (toasts.length > 5) {
        var oldest = toasts[0];
        oldest.classList.add('is-dismissing');
        setTimeout(function() { remove(oldest); }, 260);
      }
    }

    function escapeHtml(str) {
      return str.replace(/[&<>"']/g, function(m) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m];
      });
    }

    function destroy() {
      if (container) { remove(container); container = null; }
    }

    return { show: show, destroy: destroy };
  })();

  /* ═══════════════════════════════════════════════════════════════
     COUNT-UP MODULE — Sayo-style score counting
     Trigger: [data-syo-countup] or Sayo.countUp(el, { to: 1337 })
     ═══════════════════════════════════════════════════════════════ */
  Sayo.countUp = (function() {
    var DURATION = 1500;

    function animate(el, opts) {
      var from = opts.from || 0;
      var to = opts.to;
      var start = now();
      var duration = opts.duration || DURATION;
      var lastDisplayed = -1;

      // Glow up the stat container during counting
      var stat = el.closest('.syo-stat');
      if (stat) {
        stat.style.transition = 'box-shadow 400ms ease-out, border-color 400ms ease-out';
        stat.style.boxShadow = '0 0 24px rgba(88,166,255,0.25), inset 0 0 24px rgba(88,166,255,0.06)';
        stat.style.borderColor = 'var(--syo-blue)';
      }

      function tick() {
        var elapsed = now() - start;
        var progress = Math.min(elapsed / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 5);
        var current = Math.round(from + (to - from) * eased);

        // Pulse on each value change
        if (current !== lastDisplayed) {
          lastDisplayed = current;
          el.textContent = formatNum(current);
          el.style.transform = 'scale(1.2)';
          el.style.transition = 'transform 80ms cubic-bezier(0.34,1.56,0.64,1)';
          var reset = function() { el.style.transform = 'scale(1)'; };
          setTimeout(reset, 90);
        }

        if (progress < 1) {
          raf(tick);
        } else {
          el.textContent = formatNum(to);
          // Big finish pop
          el.style.transform = 'scale(1.15)';
          el.style.transition = 'transform 250ms cubic-bezier(0.34,1.56,0.64,1)';
          setTimeout(function() { el.style.transform = 'scale(1)'; }, 280);

          // Fade glow
          if (stat) {
            stat.style.boxShadow = '';
            stat.style.borderColor = '';
            setTimeout(function() {
              stat.style.transition = '';
              stat.style.boxShadow = '';
              stat.style.borderColor = '';
            }, 500);
          }
        }
      }

      raf(tick);
    }

    function formatNum(n) {
      return n.toLocaleString ? n.toLocaleString() : String(n);
    }

    var _observer;

    function init() {
      if (_observer) return; // already initialized

      _observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            var to = parseInt(entry.target.getAttribute('data-syo-countup'), 10) ||
                     parseInt(entry.target.textContent.replace(/[^0-9]/g, ''), 10) || 0;
            animate(entry.target, { to: to });
            _observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });

      $$('[data-syo-countup]').forEach(function(el) {
        _observer.observe(el);
      });
    }

    // Auto-init
    if (document.readyState === 'loading') {
      on(document, 'DOMContentLoaded', init);
    } else {
      init();
    }

    return { animate: animate, init: init };
  })();

  /* ═══════════════════════════════════════════════════════════════
     INERTIA SCROLL — momentum drag-scroll with friction
     Trigger: [data-syo-inertia] on scroll container
     ═══════════════════════════════════════════════════════════════ */
  Sayo.inertiaScroll = (function() {
    var FRICTION = 0.92;
    var MIN_VELOCITY = 0.5;

    function init(el, opts) {
      var cfg = Object.assign({ friction: FRICTION, minVelocity: MIN_VELOCITY }, opts || {});
      var target = typeof el === 'string' ? $(el) : el;
      if (!target) return;

      var velocityX = 0, velocityY = 0;
      var lastX = 0, lastY = 0, lastTime = 0;
      var dragging = false;
      var animating = false;
      var startX = 0, startY = 0, startScrollX = 0, startScrollY = 0;

      // Normalise mouse and touch events
      function getXY(e) {
        if (e.touches && e.touches.length > 0) return { x: e.touches[0].clientX, y: e.touches[0].clientY };
        if (e.changedTouches && e.changedTouches.length > 0) return { x: e.changedTouches[0].clientX, y: e.changedTouches[0].clientY };
        return { x: e.clientX, y: e.clientY };
      }

      function onDown(e) {
        animating = false;
        dragging = true;
        velocityX = 0;
        velocityY = 0;
        var p = getXY(e);
        startX = p.x;
        startY = p.y;
        startScrollX = target.scrollLeft;
        startScrollY = target.scrollTop;
        lastX = startX;
        lastY = startY;
        lastTime = now();
        target.style.cursor = 'grabbing';
        target.style.userSelect = 'none';
      }

      function onMove(e) {
        if (!dragging) return;
        e.preventDefault();
        var t = now();
        var dt = t - lastTime;
        if (dt < 16) return;

        var p = getXY(e);
        var dx = p.x - startX;
        var dy = p.y - startY;
        target.scrollLeft = startScrollX - dx;
        target.scrollTop = startScrollY - dy;

        // Calculate velocity for both axes
        velocityX = (p.x - lastX) / dt * 16;
        velocityY = (p.y - lastY) / dt * 16;
        lastX = p.x;
        lastY = p.y;
        lastTime = t;
      }

      function onUp(e) {
        if (!dragging) return;
        dragging = false;
        target.style.cursor = '';
        target.style.userSelect = '';

        if (Math.abs(velocityX) > cfg.minVelocity || Math.abs(velocityY) > cfg.minVelocity) {
          animating = true;
          raf(tick);
        }
      }

      function tick() {
        if (!animating) return;

        target.scrollLeft -= velocityX;
        target.scrollTop -= velocityY;
        velocityX *= cfg.friction;
        velocityY *= cfg.friction;

        if (Math.abs(velocityX) < cfg.minVelocity && Math.abs(velocityY) < cfg.minVelocity) {
          animating = false;
          return;
        }

        raf(tick);
      }

      // Mouse
      on(target, 'mousedown', onDown);
      on(document, 'mousemove', onMove);
      on(document, 'mouseup', onUp);
      // Touch
      on(target, 'touchstart', onDown, { passive: false });
      on(document, 'touchmove', onMove, { passive: false });
      on(document, 'touchend', onUp);

      return {
        destroy: function() {
          off(target, 'mousedown', onDown);
          off(document, 'mousemove', onMove);
          off(document, 'mouseup', onUp);
          off(target, 'touchstart', onDown);
          off(document, 'touchmove', onMove);
          off(document, 'touchend', onUp);
        }
      };
    }

    // Auto-init
    function scan() {
      $$('[data-syo-inertia]').forEach(function(el) {
        if (!el._syoInertia) el._syoInertia = init(el);
      });
    }

    if (document.readyState === 'loading') {
      on(document, 'DOMContentLoaded', scan);
    } else {
      scan();
    }

    return { init: init };
  })();

  /* ═══════════════════════════════════════════════════════════════
     PARALLAX MODULE — mouse-driven parallax shift
     Trigger: [data-syo-parallax] on target element
     ═══════════════════════════════════════════════════════════════ */
  Sayo.parallax = (function() {
    var instances = [];

    function init(el, opts) {
      if (isReducedMotion) return;
      var cfg = Object.assign({ maxShift: 8 }, opts || {});
      var target = typeof el === 'string' ? $(el) : el;
      if (!target) return;
      var container = cfg.container ? (typeof cfg.container === 'string' ? $(cfg.container) : cfg.container) : target.parentElement;
      if (!container) return;

      // Track instantly, but return smoothly on mouseleave
      var returnTransition = 'transform 350ms cubic-bezier(0.25,0.46,0.45,0.94)';

      function onMove(e) {
        var rect = container.getBoundingClientRect();
        var cx = rect.width / 2;
        var cy = rect.height / 2;
        var ox = (e.clientX - rect.left - cx) / cx * cfg.maxShift;
        var oy = (e.clientY - rect.top - cy) / cy * cfg.maxShift;
        target.style.transition = 'none';
        target.style.transform = 'translate(' + ox.toFixed(1) + 'px, ' + oy.toFixed(1) + 'px)';
      }

      function onLeave() {
        target.style.transition = returnTransition;
        target.style.transform = 'translate(0,0)';
      }

      on(container, 'mousemove', onMove);
      on(container, 'mouseleave', onLeave);

      var instance = { target: target, container: container, onMove: onMove, onLeave: onLeave, cfg: cfg };
      instances.push(instance);
      return instance;
    }

    function destroy(instance) {
      if (!instance) { instances.forEach(destroy); return; }
      off(instance.container, 'mousemove', instance.onMove);
      off(instance.container, 'mouseleave', instance.onLeave);
      instance.target.style.transform = '';
      instance.target.style.transition = '';
      instances = instances.filter(function(i) { return i !== instance; });
    }

    return { init: init, destroy: destroy };
  })();

  /* ═══════════════════════════════════════════════════════════════
     REVEAL MODULE — scroll-triggered staggered entrance
     Trigger: add .syo-reveal class. Auto-inits on DOM load.
     ═══════════════════════════════════════════════════════════════ */
  Sayo.reveal = (function() {
    var observer;

    function scan(root) {
      root = root || document;
      var els = $$('.syo-reveal', root);
      els.forEach(function(el, i) {
        // Stagger: each sibling group gets sequential delays
        var parent = el.parentNode;
        var siblings = $$('.syo-reveal', parent);
        var idx = siblings.indexOf(el);
        el.style.transitionDelay = (idx * 40) + 'ms';
        observer.observe(el);
      });
    }

    function init() {
      if (isReducedMotion) return;
      if (observer) return;

      observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
          }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -30px 0px' });

      scan();
    }

    function destroy() {
      if (observer) {
        observer.disconnect();
        observer = null;
      }
    }

    // Auto-init on DOM ready
    if (document.readyState === 'loading') {
      on(document, 'DOMContentLoaded', init);
    } else {
      init();
    }

    return { init: init, scan: scan, destroy: destroy };
  })();

  /* ═══════════════════════════════════════════════════════════════
     DROPDOWN MODULE — click-to-open menu
     Trigger: [data-syo-dropdown] on container
     ═══════════════════════════════════════════════════════════════ */
  Sayo.dropdown = (function() {
    var openInstance = null;

    function closeCurrent() {
      if (openInstance) { openInstance.close(); openInstance = null; }
    }

    function init(el) {
      var target = typeof el === 'string' ? $(el) : el;
      if (!target) return;

      var toggle = target.querySelector('.syo-dropdown-toggle') || target;
      var menu = target.querySelector('.syo-dropdown-menu');
      if (!menu) return;

      function open(e) {
        e.stopPropagation();
        if (openInstance && openInstance !== instance) closeCurrent();
        target.classList.toggle('open');
        if (target.classList.contains('open')) {
          openInstance = instance;
        } else {
          openInstance = null;
        }
      }

      function close() {
        target.classList.remove('open');
        if (openInstance === instance) openInstance = null;
      }

      function onKey(e) {
        if (e.key === 'Escape') close();
      }

      on(toggle, 'click', open);
      on(target, 'keydown', onKey);

      var instance = { el: target, close: close, open: open };
      return instance;
    }

    // Global: close dropdown when clicking outside
    on(document, 'click', function(e) {
      if (openInstance && !openInstance.el.contains(e.target)) {
        openInstance.close();
      }
    });

    // Auto-init
    function scan() {
      $$('[data-syo-dropdown]').forEach(function(el) {
        if (!el._syoDropdown) el._syoDropdown = init(el);
      });
    }

    if (document.readyState === 'loading') {
      on(document, 'DOMContentLoaded', scan);
    } else {
      scan();
    }

    return { init: init };
  })();

  /* ═══════════════════════════════════════════════════════════════
     DIALOG MODULE — Sayo-style elastic modal
     Call: Sayo.dialog.show({ title, body }) | Sayo.dialog.confirm({ ... })
     ═══════════════════════════════════════════════════════════════ */
  Sayo.dialog = (function() {
    var activeOverlay = null;
    var titleIdCounter = 0;

    function createOverlay() {
      var overlay = document.createElement('div');
      overlay.className = 'syo-dialog-overlay';
      return overlay;
    }

    function createDialog(opts) {
      var dialog = document.createElement('div');
      dialog.className = 'syo-dialog';
      dialog.setAttribute('role', 'dialog');
      dialog.setAttribute('aria-modal', 'true');

      // Header
      if (opts.title) {
        var header = document.createElement('div');
        header.className = 'syo-dialog-header';
        var title = document.createElement('h3');
        title.className = 'syo-dialog-title';
        title.id = 'syo-dialog-title-' + (++titleIdCounter);
        title.textContent = opts.title;
        dialog.setAttribute('aria-labelledby', title.id);
        header.appendChild(title);
        if (opts.closable !== false) {
          var closeBtn = document.createElement('button');
          closeBtn.className = 'syo-dialog-close';
          closeBtn.setAttribute('aria-label', 'Close');
          closeBtn.innerHTML = '&times;';
          closeBtn.addEventListener('click', close);
          header.appendChild(closeBtn);
        }
        dialog.appendChild(header);
      }

      // Body
      var body = document.createElement('div');
      body.className = 'syo-dialog-body';
      if (typeof opts.body === 'string') {
        body.innerHTML = opts.body;
      } else if (opts.body) {
        body.appendChild(opts.body);
      }
      dialog.appendChild(body);

      // Footer
      if (opts.footer) {
        var footer = document.createElement('div');
        footer.className = 'syo-dialog-footer';
        if (typeof opts.footer === 'string') {
          footer.innerHTML = opts.footer;
        } else if (Array.isArray(opts.footer)) {
          opts.footer.forEach(function(btn) { footer.appendChild(btn); });
        } else {
          footer.appendChild(opts.footer);
        }
        dialog.appendChild(footer);
      }

      return dialog;
    }

    function show(opts) {
      opts = opts || {};
      close(); // dismiss any existing dialog

      var overlay = createOverlay();
      var dialog = createDialog(opts);
      var previousFocus = document.activeElement;
      var bodyOverflow = document.body.style.overflow;

      // Click overlay to close
      if (opts.closable !== false) {
        overlay.addEventListener('click', function(e) {
          if (e.target === overlay) close();
        });
      }

      // Escape to close + focus trap
      function onKey(e) {
        if (e.key === 'Escape' && opts.closable !== false) { close(); return; }
        if (e.key === 'Tab') trapFocus(e, dialog);
      }
      document.addEventListener('keydown', onKey);

      overlay.appendChild(dialog);
      document.body.appendChild(overlay);
      document.body.style.overflow = 'hidden';
      activeOverlay = overlay;

      // Store instance data on overlay for close() access
      overlay._syoDialog = {
        previousFocus: previousFocus,
        bodyOverflow: bodyOverflow,
        onKey: onKey
      };

      // Focus the dialog for keyboard nav
      dialog.setAttribute('tabindex', '-1');
      dialog.focus();

      return {
        el: dialog,
        overlay: overlay,
        close: close,
        _syoDialog: overlay._syoDialog
      };
    }

    function trapFocus(e, dialog) {
      var focusable = dialog.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      if (focusable.length === 0) { e.preventDefault(); return; }
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey) {
        if (document.activeElement === first) { e.preventDefault(); last.focus(); }
      } else {
        if (document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    }

    function close() {
      if (!activeOverlay) return;
      var overlay = activeOverlay;
      activeOverlay = null;

      // Restore body overflow and focus
      var data = overlay._syoDialog;
      if (data) {
        document.body.style.overflow = data.bodyOverflow || '';
        if (data.previousFocus) data.previousFocus.focus();
        if (data.onKey) document.removeEventListener('keydown', data.onKey);
      } else {
        document.body.style.overflow = '';
      }

      overlay.classList.add('is-closing');
      setTimeout(function() {
        if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
      }, 220);
    }

    function confirm(opts) {
      return new Promise(function(resolve) {
        var buttons = [
          createButton(opts.cancelText || 'Cancel', 'syo-btn syo-btn--sm', function() {
            instance.close();
            resolve(false);
          }),
          createButton(opts.confirmText || 'Confirm', 'syo-btn syo-btn--sm syo-btn--primary', function() {
            instance.close();
            resolve(true);
          })
        ];
        var instance = show({
          title: opts.title || '',
          body: '<p>' + (opts.message || '') + '</p>',
          footer: buttons,
          closable: opts.closable !== false
        });
      });
    }

    function alert(opts) {
      return new Promise(function(resolve) {
        var btn = createButton(opts.okText || 'OK', 'syo-btn syo-btn--sm syo-btn--primary', function() {
          instance.close();
          resolve();
        });
        var instance = show({
          title: opts.title || '',
          body: '<p>' + (opts.message || '') + '</p>',
          footer: [btn],
          closable: opts.closable !== false
        });
      });
    }

    function createButton(text, className, onClick) {
      var btn = document.createElement('button');
      btn.className = className;
      btn.textContent = text;
      btn.addEventListener('click', onClick);
      return btn;
    }

    return { show: show, confirm: confirm, alert: alert, close: close };
  })();

  /* ═══════════════════════════════════════════════════════════════
     SCROLL SPY — highlight nav links based on scroll position
     Trigger: [data-syo-scrollspy] or Sayo.scrollSpy.init({ nav, offset })
     ═══════════════════════════════════════════════════════════════ */
  Sayo.scrollSpy = (function() {
    var instances = [];

    function init(opts) {
      var cfg = Object.assign({
        nav: '[data-syo-scrollspy]',  // CSS selector or element
        offset: 80,                    // px offset from top (e.g. nav height)
        activeClass: 'active',         // class added to the active link
        scrollRoot: null,              // scroll container (null = window)
      }, opts || {});

      var nav = typeof cfg.nav === 'string' ? $(cfg.nav) : cfg.nav;
      if (!nav) return;

      // Build section map from [href^="#"] links
      var items = [];
      $$('a[href^="#"]', nav).forEach(function(a) {
        var target = $(a.getAttribute('href'));
        if (target) items.push({ el: target, link: a });
      });
      if (!items.length) return;

      var root = cfg.scrollRoot || window;

      function update() {
        var scrollY = (root === window ? root.scrollY : root.scrollTop) + cfg.offset;
        var active = null;

        items.forEach(function(item) {
          if (item.el.offsetTop <= scrollY) active = item;
        });

        items.forEach(function(item) { item.link.classList.remove(cfg.activeClass); });
        if (active) active.link.classList.add(cfg.activeClass);
      }

      on(root, 'scroll', update, { passive: true });
      update(); // set initial state

      var instance = { nav: nav, cfg: cfg, update: update, items: items, root: root };
      instances.push(instance);
      return instance;
    }

    function destroy(instance) {
      if (!instance) { instances.forEach(destroy); return; }
      off(instance.root, 'scroll', instance.update);
      instance.items.forEach(function(item) { item.link.classList.remove(instance.cfg.activeClass); });
      instances = instances.filter(function(i) { return i !== instance; });
    }

    // Auto-init: [data-syo-scrollspy] attribute
    function scan() {
      $$('[data-syo-scrollspy]').forEach(function(el) {
        if (!el._syoScrollspy) {
          var offset = parseInt(el.getAttribute('data-syo-scrollspy'), 10) || 80;
          el._syoScrollspy = init({ nav: el, offset: offset });
        }
      });
    }

    if (document.readyState === 'loading') {
      on(document, 'DOMContentLoaded', scan);
    } else {
      scan();
    }

    return { init: init, destroy: destroy };
  })();

  /* ═══════════════════════════════════════════════════════════════
     AUTO-INIT — scan DOM for [data-syo-*] attributes
     ═══════════════════════════════════════════════════════════════ */
  function autoInit() {
    // Cursor always inits (essential); glow/trail/ripple/parallax skip if reduced motion
    if (document.body.hasAttribute('data-syo-cursor')) {
      Sayo.cursor.init();
    }

    if (isReducedMotion) return; // remaining modules are purely decorative

    if (document.body.hasAttribute('data-syo-trail')) {
      Sayo.trail.init();
    }

    var rippleContainers = $$('[data-syo-ripple]');
    if (rippleContainers.length > 0) {
      Sayo.ripple.init();
    }

    $$('[data-syo-parallax]').forEach(function(el) {
      var opts = {};
      var val = el.getAttribute('data-syo-parallax');
      if (val && val !== '') {
        opts.maxShift = parseFloat(val) || 8;
      }
      Sayo.parallax.init(el, opts);
    });
  }

  if (document.readyState === 'loading') {
    on(document, 'DOMContentLoaded', autoInit);
  } else {
    autoInit();
  }

  /* ═══════════════════════════════════════════════════════════════
     GLOBAL TEARDOWN
     ═══════════════════════════════════════════════════════════════ */
  Sayo.destroy = function() {
    if (Sayo.cursor.destroy) Sayo.cursor.destroy();
    if (Sayo.trail.destroy) Sayo.trail.destroy();
    if (Sayo.ripple.destroy) Sayo.ripple.destroy();
    if (Sayo.toast.destroy) Sayo.toast.destroy();
    if (Sayo.reveal.destroy) Sayo.reveal.destroy();
    if (Sayo.parallax.destroy) Sayo.parallax.destroy();
    if (Sayo.scrollSpy.destroy) Sayo.scrollSpy.destroy();
    if (Sayo.dialog.close) Sayo.dialog.close();
  };

  /* ── EXPORT ─────────────────────────────────────────────────── */
  global.Sayo = Sayo;

})(typeof window !== 'undefined' ? window : this);
