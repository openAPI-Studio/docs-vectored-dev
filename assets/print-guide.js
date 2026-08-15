/* Vectored docs — full-guide export.

   Powers <product>/docs/print.html: fetches every page in the product's nav
   order, lifts each one's <h1>, lede and <article>, and concatenates them into
   one continuous document with a Contents list built from the page titles.
   The same @media print rules in tokens.css then produce the PDF, so the
   full-guide export and the single-page export look identical.

   Relative image and link paths resolve unchanged because print.html sits in
   the same directory as the pages it pulls in. */
(function () {
  var script = document.currentScript;
  if (!script || !script.src) return;
  var root = new URL('..', script.src).href;
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

  var host = document.getElementById('vc-guide');
  if (!host) return;
  var product = window.VC_PRODUCT_FOR ? window.VC_PRODUCT_FOR(location.pathname) : null;
  if (!product) { host.textContent = 'Unknown product.'; return; }

  var pages = window.VC_PAGES(product);
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var now = new Date();
  var exported = now.getDate() + ' ' + MONTHS[now.getMonth()] + ' ' + now.getFullYear();

  document.title = product.label + ' — full documentation';

  host.innerHTML =
    '<div class="vc-print-head"><div><b>Vectored</b><span>' + esc(product.label) +
      ' · Documentation</span></div></div>' +
    '<h1 class="vc-h1">' + esc(product.label) + ' documentation</h1>' +
    '<p class="vc-lede">The complete guide — all ' + pages.length +
      ' pages in one document, ready to print or save as PDF.</p>' +
    '<div class="vc-meta"><span class="vc-meta-item">Exported ' + exported +
      ' · docs.vectored.dev</span>' +
      '<div class="vc-meta-actions" data-noprint="1">' +
        '<button class="vc-pdfbtn" id="vc-print-now" type="button">Print / save as PDF</button>' +
      '</div></div>' +
    '<div class="vc-print-contents" style="display:block"><div>Contents</div><ol>' +
      pages.map(function (p) { return '<li>' + esc(p.l) + '</li>'; }).join('') +
    '</ol></div>' +
    '<div id="vc-guide-body"><p class="vc-lede" id="vc-guide-status">Loading ' +
      pages.length + ' pages…</p></div>';

  document.getElementById('vc-print-now').addEventListener('click', function () { window.print(); });

  var body = document.getElementById('vc-guide-body');
  var status = document.getElementById('vc-guide-status');

  Promise.all(pages.map(function (p) {
    return fetch(p.h).then(function (r) { return r.ok ? r.text() : ''; }).catch(function () { return ''; });
  })).then(function (docs) {
    var out = '';
    docs.forEach(function (text, i) {
      var page = pages[i];
      if (!text) {
        out += '<section class="vc-guide-page"><h2>' + esc(page.l) +
          '</h2><p>Could not load this page.</p></section>';
        return;
      }
      var d = new DOMParser().parseFromString(text, 'text/html');
      var h1 = d.querySelector('h1.vc-h1');
      var lede = d.querySelector('p.vc-lede');
      var art = d.querySelector('article.vc-doc');
      out += '<section class="vc-guide-page">' +
        '<h2 class="vc-guide-title">' + (h1 ? h1.innerHTML : esc(page.l)) + '</h2>' +
        (lede ? '<p class="vc-lede">' + lede.innerHTML + '</p>' : '') +
        (art ? '<div class="vc-doc">' + art.innerHTML + '</div>' : '') +
        '</section>';
    });
    body.innerHTML = out;
    if (status && status.parentNode) status.parentNode.removeChild(status);
    if (/[?&]print=1/.test(location.search)) setTimeout(function () { window.print(); }, 400);
  });
})();
