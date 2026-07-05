/* Vectored shared header. Include on any page as:
     <div id="vc-header"></div>
     <script src="<relative-path>/assets/header.js"></script>
   Must be included synchronously where the nav should render — it exposes the
   ids page scripts rely on (#doc-search, #search-results, #theme-toggle,
   #icon-dark, #icon-light, #menu-toggle, #menu-open, #menu-close).
   Behavior (theme toggle, sidebar toggling, search wiring) stays in each
   page's own script; this file only renders markup. Edit here once. */
(function () {
  var script = document.currentScript;
  if (!script || !script.src) return;
  var root = new URL('..', script.src).href;
  var mount = document.getElementById('vc-header');
  if (!mount) return;
  function u(p) { return root + p; }

  // Product context from the page URL.
  var path = location.pathname;
  var ctx = null;
  if (path.indexOf('/forms/') !== -1) {
    ctx = { label: 'Forms & Frontdoor', home: u('forms/'), cta: 'https://marketplace.atlassian.com/apps/2466520058/forms-frontdoor-by-vectored?hosting=cloud&tab=overview', ctaLabel: 'Try now for free' };
  } else if (path.indexOf('/macrotoolkit/') !== -1) {
    ctx = { label: 'Macro Toolkit', home: u('macrotoolkit/'), cta: 'https://marketplace.atlassian.com/apps/3972300183', ctaLabel: 'Try now for free' };
  } else if (path.indexOf('/blog/') !== -1) {
    ctx = { label: 'Blog', home: u('blog/'), cta: null };
  }

  var html =
    '<nav class="sticky top-0 z-50 bg-surface/90 backdrop-blur-md border-b border-border px-4 sm:px-6 lg:px-8 py-3">' +
      '<div class="max-w-6xl mx-auto flex items-center">' +
        '<a href="' + u('') + '" class="shrink-0 leading-tight cursor-pointer">' +
          '<span class="font-mono font-bold text-lg text-cta block">Vectored</span>' +
          '<span class="text-[10px] text-muted">Tools for developers</span>' +
        '</a>' +
        (ctx ? '<div class="hidden md:block w-px h-5 bg-border mx-4"></div>' +
               '<a href="' + ctx.home + '" class="hidden md:block text-sm font-medium text-text hover:text-cta transition-colors duration-200 cursor-pointer">' + ctx.label + '</a>' : '') +
        '<div class="hidden md:flex items-center gap-5 text-sm text-muted ml-6">' +
          '<a href="' + u('') + '#products" class="hover:text-text transition-colors duration-200 cursor-pointer">Products</a>' +
          '<a href="' + u('blog/') + '" class="hover:text-text transition-colors duration-200 cursor-pointer">Blog</a>' +
          '<a href="' + u('macrotoolkit/support.html') + '" class="hover:text-text transition-colors duration-200 cursor-pointer">Support</a>' +
        '</div>' +
        '<button id="menu-toggle" class="lg:hidden ml-3 p-1.5 rounded-lg hover:bg-bg transition-colors duration-200 cursor-pointer text-muted hover:text-text" aria-label="Menu">' +
          '<svg id="menu-open" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>' +
          '<svg id="menu-close" class="w-5 h-5 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>' +
        '</button>' +
        '<div class="flex items-center gap-3 ml-auto">' +
          '<div class="relative hidden md:block">' +
            '<input type="text" id="doc-search" placeholder="Search docs..." autocomplete="off" class="bg-bg border border-border rounded-lg px-3 py-1.5 text-sm text-text placeholder:text-muted/60 w-44 focus:outline-none focus:border-cta/50 transition-colors duration-200">' +
            '<div id="search-results" class="absolute top-full right-0 mt-2 w-72 bg-surface border border-border rounded-xl shadow-xl hidden max-h-80 overflow-y-auto z-50"></div>' +
          '</div>' +
          '<a href="https://github.com/openAPI-Studio" target="_blank" rel="noopener" class="hidden sm:block p-1.5 rounded-lg hover:bg-bg transition-colors duration-200 cursor-pointer text-muted hover:text-text" aria-label="GitHub">' +
            '<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>' +
          '</a>' +
          '<button id="theme-toggle" class="p-1.5 rounded-lg hover:bg-bg transition-colors duration-200 cursor-pointer text-muted hover:text-text" aria-label="Toggle theme">' +
            '<svg id="icon-dark" class="w-5 h-5" style="display:none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>' +
            '<svg id="icon-light" class="w-5 h-5" style="display:none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>' +
          '</button>' +
          (ctx && ctx.cta ? '<a href="' + ctx.cta.replace(/&/g, '&amp;') + '" target="_blank" rel="noopener" class="hidden sm:inline-block bg-cta text-bg font-semibold text-sm px-4 py-2 rounded-lg hover:bg-cta/90 transition-colors duration-200 cursor-pointer">' + ctx.ctaLabel + '</a>' : '') +
        '</div>' +
      '</div>' +
    '</nav>';

  mount.outerHTML = html;

  // Hide the hamburger on pages with nothing for it to toggle.
  document.addEventListener('DOMContentLoaded', function () {
    if (!document.getElementById('mobile-sidebar') && !document.getElementById('mobile-menu')) {
      var mt = document.getElementById('menu-toggle');
      if (mt) mt.style.display = 'none';
    }
  });
})();
