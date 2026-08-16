/* Vectored shared header. Include on any page as:

     <div id="vc-header"></div>
     <script src="<relative-path>/assets/nav.js"></script>
     <script src="<relative-path>/assets/header.js"></script>

   Renders the sticky header: sidebar toggle, wordmark, product switcher,
   site-wide search, GitHub, theme toggle and the product CTA. Links resolve
   against the site root (the parent of /assets/) so the same file works at any
   page depth. Edit here once; every page updates. */
(function () {
  var script = document.currentScript;
  if (!script || !script.src) return;
  var root = new URL('..', script.src).href;
  var mount = document.getElementById('vc-header');
  if (!mount) return;
  function u(p) { return root + p; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }

  var products = window.VC_PRODUCTS || [];
  var ctx = window.VC_PRODUCT_FOR ? window.VC_PRODUCT_FOR(location.pathname) : null;

  var GITHUB = 'https://github.com/openAPI-Studio';
  var ICON_GITHUB = '<svg viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>';

  function ctaHref(p) {
    return /^https?:/.test(p.cta) ? p.cta : u(p.cta);
  }

  var switcherRows = products.map(function (p) {
    return '<a class="vc-prow' + (ctx && p.key === ctx.key ? ' cur' : '') + '" href="' + u(p.docsHome || p.dir + '/docs/') + '">' +
      '<span class="vc-picon" style="background-image:url(&quot;' + encodeURI(u(p.icon)) + '&quot;)"></span>' +
      '<span class="vc-pmeta">' +
        '<span class="vc-pname">' + esc(p.label) + '</span>' +
        '<span class="vc-pblurb">' + esc(p.blurb) + '</span>' +
      '</span>' +
      '<span class="vc-pcount">' + p.count + ' pages</span>' +
    '</a>';
  }).join('');

  var html =
    '<header class="vc-hd" data-noprint="1">' +
      '<div class="vc-hd-in">' +
        '<button id="vc-sidebar-toggle" class="vc-iconbtn vc-first" aria-label="Toggle sidebar" title="Toggle sidebar" aria-expanded="true">' +
          '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"></rect><path d="M9 4v16"></path></svg>' +
        '</button>' +
        '<a class="vc-wordmark" href="' + u('') + '"><b>Vectored</b><span>Docs</span></a>' +
        '<div class="vc-vdiv"></div>' +
        '<div class="vc-switch-wrap">' +
          '<button id="vc-switch" class="vc-switch" aria-expanded="false" aria-haspopup="true" aria-controls="vc-switch-panel">' +
            '<span class="vc-dot"></span>' +
            '<span class="vc-switch-label">' + esc(ctx ? ctx.label : 'All products') + '</span>' +
            '<svg class="vc-chev" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"></path></svg>' +
          '</button>' +
          '<div id="vc-switch-panel" class="vc-panel" hidden>' +
            '<div class="vc-label">Documentation</div>' + switcherRows +
            '<div class="vc-panel-foot">' +
              (ctx ? '<a href="' + u(ctx.dir + '/') + '">' + esc(ctx.label) + ' product page</a>' : '') +
              '<a href="' + u('') + '#products">Browse all products →</a>' +
            '</div>' +
          '</div>' +
        '</div>' +
        '<div class="vc-search">' +
          '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35M17 11a6 6 0 11-12 0 6 6 0 0112 0z"></path></svg>' +
          '<input type="text" id="doc-search" placeholder="Search all docs" autocomplete="off" aria-label="Search documentation">' +
          '<span class="vc-kbd">⌘K</span>' +
          '<div id="search-results" class="vc-sr" hidden></div>' +
        '</div>' +
        '<div class="vc-hd-actions">' +
          // Below 640px the search field collapses to this button and opens as
          // a full-width row under the header; there is no room for both it
          // and the product switcher on a phone.
          '<button id="vc-search-toggle" class="vc-iconbtn vc-search-btn" aria-label="Search" aria-expanded="false">' +
            '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35M17 11a6 6 0 11-12 0 6 6 0 0112 0z"></path></svg>' +
          '</button>' +
          '<a class="vc-iconbtn vc-gh" href="' + GITHUB + '" target="_blank" rel="noopener" aria-label="GitHub">' + ICON_GITHUB + '</a>' +
          '<button id="theme-toggle" class="vc-iconbtn" aria-label="Toggle theme" title="Toggle theme">' +
            '<svg id="icon-light" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>' +
            '<svg id="icon-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="display:none"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>' +
          '</button>' +
          (ctx ? '<a class="vc-cta" href="' + esc(ctaHref(ctx)) + '"' + (/^https?:/.test(ctx.cta) ? ' target="_blank" rel="noopener"' : '') + '>' + esc(ctx.ctaLabel) + '</a>' : '') +
        '</div>' +
      '</div>' +
    '</header>';

  mount.outerHTML = html;

  /* ------------------------------------------------------------- theme -- */
  function currentTheme() { return document.documentElement.dataset.theme === 'light' ? 'light' : 'dark'; }
  function paintTheme() {
    var light = currentTheme() === 'light';
    var el = document.documentElement;
    el.dataset.theme = light ? 'light' : 'dark';
    el.classList.toggle('dark', !light);   // API Studio pages use dark: variants
    el.classList.toggle('light', light);   // legacy html.light rules
    var d = document.getElementById('icon-dark'), l = document.getElementById('icon-light');
    if (d && l) { d.style.display = light ? 'block' : 'none'; l.style.display = light ? 'none' : 'block'; }
  }
  paintTheme();
  var tt = document.getElementById('theme-toggle');
  if (tt) tt.addEventListener('click', function () {
    document.documentElement.dataset.theme = currentTheme() === 'light' ? 'dark' : 'light';
    try { localStorage.setItem('theme', currentTheme()); } catch (e) {}
    paintTheme();
  });

  /* --------------------------------------------------- product switcher -- */
  var sw = document.getElementById('vc-switch'), panel = document.getElementById('vc-switch-panel');
  function closeSwitcher() { if (panel) { panel.hidden = true; sw.setAttribute('aria-expanded', 'false'); } }
  if (sw) {
    sw.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = panel.hidden;
      panel.hidden = !open;
      sw.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('#vc-switch-panel') && !e.target.closest('#vc-switch')) closeSwitcher();
    });
  }

  /* ---------------------------------------------------------- search -- */
  var index = [];
  products.forEach(function (p) {
    (window.VC_PAGES ? window.VC_PAGES(p) : []).forEach(function (it) {
      index.push({ label: it.l, product: p.label, tags: it.t, href: u(p.dir + '/docs/' + it.h) });
    });
  });

  var input = document.getElementById('doc-search'), results = document.getElementById('search-results');
  function hideResults() { if (results) { results.hidden = true; results.innerHTML = ''; } }

  /* Small screens: the field is hidden until the icon opens it. */
  var searchToggle = document.getElementById('vc-search-toggle');
  function setSearchOpen(open) {
    document.body.classList.toggle('vc-search-open', open);
    if (searchToggle) searchToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open && input) input.focus();
    if (!open) hideResults();
  }
  if (searchToggle) {
    searchToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      setSearchOpen(!document.body.classList.contains('vc-search-open'));
    });
  }
  if (input && results) {
    input.addEventListener('input', function () {
      var q = this.value.toLowerCase().trim();
      if (!q) return hideResults();
      var matches = index.filter(function (d) {
        return d.label.toLowerCase().indexOf(q) !== -1 || d.tags.indexOf(q) !== -1;
      }).slice(0, 24);
      results.innerHTML = matches.length
        ? matches.map(function (d) {
            return '<a href="' + d.href + '">' + esc(d.label) + '<small>' + esc(d.product) + '</small></a>';
          }).join('')
        : '<p>No results</p>';
      results.hidden = false;
    });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { hideResults(); this.blur(); }
      if (e.key === 'Enter') { var first = results.querySelector('a'); if (first) location.href = first.href; }
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.vc-search') && !e.target.closest('#vc-search-toggle')) setSearchOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        setSearchOpen(true);   // on small screens the field is collapsed
        input.focus(); input.select();
      }
      if (e.key === 'Escape') { closeSwitcher(); setSearchOpen(false); }
    });
  }

  /* ------------------------------------------------- sidebar toggle -- */
  /* docs.js owns the sidebar; on pages without one the toggle is pointless. */
  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('vc-sidebar-toggle');
    if (btn && !document.querySelector('.vc-side')) btn.style.display = 'none';
  });
})();
