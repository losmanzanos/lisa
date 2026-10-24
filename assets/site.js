/* Brilliantly Sane: shared behavior */
(function () {
  'use strict';

  /* mobile menu */
  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.site-nav');
  if (btn && nav) {
    var setOpen = function (open) {
      nav.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? 'Close' : 'Menu';
      document.documentElement.style.overflow = open ? 'hidden' : '';
    };
    btn.addEventListener('click', function () {
      setOpen(!nav.classList.contains('open'));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        setOpen(false);
        btn.focus();
      }
    });
    /* a resize past the breakpoint should not strand the menu open */
    window.addEventListener('resize', function () {
      if (window.innerWidth > 980 && nav.classList.contains('open')) setOpen(false);
    });
  }

  /* scroll lock that actually holds on iOS */
  var lockY = 0;
  window.bsLock = function (on) {
    var b = document.body;
    if (on) {
      lockY = window.scrollY || window.pageYOffset || 0;
      b.style.top = -lockY + 'px';
      b.classList.add('locked');
    } else {
      b.classList.remove('locked');
      b.style.top = '';
      window.scrollTo(0, lockY);
    }
  };

  /* keep focus inside an open dialog */
  window.bsTrap = function (container) {
    return function (e) {
      if (e.key !== 'Tab') return;
      var f = container.querySelectorAll('a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    };
  };
})();

/* hovering a wayfinder link lights its segment */
(function () {
  var nav = document.querySelector('.ringnav');
  if (!nav) return;
  document.querySelectorAll('.wgroup a[data-k]').forEach(function (a) {
    var seg = nav.querySelector('.nseg[data-k="' + a.dataset.k + '"]');
    if (!seg) return;
    ['mouseenter', 'focus'].forEach(function (e) {
      a.addEventListener(e, function () { seg.classList.add('hot'); });
    });
    ['mouseleave', 'blur'].forEach(function (e) {
      a.addEventListener(e, function () { seg.classList.remove('hot'); });
    });
  });
})();
