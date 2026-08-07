// Crawfords Reviews — shared behaviour
(function () {
  // Mobile hamburger menu
  var burger = document.getElementById('burger');
  var menu = document.getElementById('menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open);
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        menu.classList.remove('open');
        burger.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }
  // Cookie consent banner — drives Google Consent Mode v2
  var banner = document.getElementById('consent');
  if (banner) {
    var stored = null;
    try { stored = localStorage.getItem('cmd_consent'); } catch (e) {}
    if (!stored) banner.hidden = false;

    function setConsent(state) {
      try { localStorage.setItem('cmd_consent', state); } catch (e) {}
      if (typeof gtag === 'function') {
        var granted = state === 'granted';
        gtag('consent', 'update', {
          ad_storage: granted ? 'granted' : 'denied',
          ad_user_data: granted ? 'granted' : 'denied',
          ad_personalization: granted ? 'granted' : 'denied',
          analytics_storage: granted ? 'granted' : 'denied'
        });
      }
      banner.hidden = true;
    }
    var acc = document.getElementById('consent-accept');
    var rej = document.getElementById('consent-reject');
    if (acc) acc.addEventListener('click', function () { setConsent('granted'); });
    if (rej) rej.addEventListener('click', function () { setConsent('denied'); });
  }

  // Review wall: star filters + progressive reveal
  var wall = document.getElementById('revwall');
  if (wall) {
    var all = Array.prototype.slice.call(wall.querySelectorAll('.rev'));
    var step = 24, shown = step, filter = 'all';
    var moreBtn = document.getElementById('revmore');

    function matches(el) {
      var s = parseInt(el.getAttribute('data-stars'), 10);
      if (filter === '5') return s === 5;
      if (filter === 'lt5') return s < 5;
      if (filter === 'prod') return !!el.querySelector('.rev-rec');
      return true;
    }
    function render() {
      var n = 0;
      all.forEach(function (el) {
        if (matches(el) && n < shown) { el.hidden = false; n++; }
        else { el.hidden = true; }
      });
      var total = all.filter(matches).length;
      if (moreBtn) {
        moreBtn.hidden = n >= total;
        moreBtn.textContent = 'Show more reviews (' + (total - n) + ' left)';
      }
    }
    document.querySelectorAll('.rf').forEach(function (b) {
      b.addEventListener('click', function () {
        document.querySelectorAll('.rf').forEach(function (x) { x.classList.remove('on'); });
        b.classList.add('on');
        filter = b.getAttribute('data-f');
        shown = step;
        render();
      });
    });
    if (moreBtn) moreBtn.addEventListener('click', function () { shown += step; render(); });
    render();
  }

  // Safety net: ensure the affiliate tracking code is on every shop link,
  // even if a future page forgets to bake it in at build time.
  document.querySelectorAll('a[href*="crawfordsmd.com"]').forEach(function (a) {
    try {
      var u = new URL(a.href);
      if (/crawfordsmd\.com$/i.test(u.hostname) && !u.searchParams.get('tracking')) {
        u.searchParams.set('tracking', '682a88c59a');
        if (!u.searchParams.get('utm_source')) {
          u.searchParams.set('utm_source', 'cmd-reviews');
          u.searchParams.set('utm_medium', 'referral');
          u.searchParams.set('utm_campaign', 'reviews-site');
        }
        a.href = u.toString();
      }
    } catch (e) {}
  });
})();
