/* Vectored docs — page shell behaviour.

   Include at the end of a doc page, after nav.js/header.js/footer.js:
     <script src="<relative-path>/assets/docs.js"></script>

   The page itself only ships its own content: an <h1 class="vc-h1">, an
   optional <p class="vc-lede"> and an <article class="vc-doc">. Everything
   else on the page — sidebar, breadcrumbs, meta row, table of contents,
   feedback, prev/next and the print-only blocks — is built here from the
   product registry in nav.js, so 130 pages stay consistent by construction.

   Placeholders the page provides, in order inside .vc-col:
     [data-vc="printhead"] [data-vc="crumbs"] h1 lede
     [data-vc="meta"] [data-vc="contents"] article.vc-doc [data-vc="pagefoot"]
*/
(function () {
  var script = document.currentScript;
  if (!script || !script.src) return;
  var root = new URL('..', script.src).href;
  function u(p) { return root + p; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }

  var REPO = 'https://github.com/openAPI-Studio/docs-vectored-dev';
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  function fmtDate(d) {
    return d.getDate() + ' ' + MONTHS[d.getMonth()] + ' ' + d.getFullYear();
  }
  function slugify(s) {
    return s.toLowerCase().replace(/[^\w]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60);
  }
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function slot(name) { return document.querySelector('[data-vc="' + name + '"]'); }
  function fill(name, node) {
    var s = slot(name);
    if (!s || !node) return null;
    s.parentNode.replaceChild(node, s);
    return node;
  }

  var article = document.querySelector('article.vc-doc');
  if (!article) return;

  var product = window.VC_PRODUCT_FOR ? window.VC_PRODUCT_FOR(location.pathname) : null;
  var file = location.pathname.split('/').pop() || 'index.html';
  var pages = product && window.VC_PAGES ? window.VC_PAGES(product) : [];
  var idx = -1;
  pages.forEach(function (p, i) { if (p.h === file) idx = i; });

  var h1 = document.querySelector('h1.vc-h1');
  var pageTitle = h1 ? h1.textContent.trim() : document.title;
  var updatedMeta = document.querySelector('meta[name="vc-updated"]');
  var updated = updatedMeta ? updatedMeta.content : '';
  var exported = fmtDate(new Date());
  var printGuide = product ? u(product.dir + '/docs/print.html') : null;

  /* ------------------------------------------------------ content passes -- */

  /* Stable ids on every h2 so the TOC and deep links keep working. */
  var heads = [].slice.call(article.querySelectorAll('h2'));
  var used = {};
  heads.forEach(function (h) {
    var id = h.id || slugify(h.textContent) || 'section';
    while (used[id]) id = id + '-1';
    used[id] = 1;
    h.id = id;
  });

  /* Bare <pre> blocks get the framed code block with a copy button. */
  [].slice.call(article.querySelectorAll('pre')).forEach(function (pre) {
    if (pre.closest('.vc-code')) return;
    var lang = pre.getAttribute('data-lang') || '';
    if (!lang) {
      var codeEl = pre.querySelector('code');
      var m = (codeEl && codeEl.className || pre.className || '').match(/language-([\w-]+)/);
      lang = m ? m[1] : 'code';
    }
    var wrap = el('div', 'vc-code');
    var bar = el('div', 'vc-code-bar',
      '<span class="vc-code-lang">' + esc(lang) + '</span>' +
      '<button class="vc-copy" type="button">Copy</button>');
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(bar);
    wrap.appendChild(pre);
    bar.querySelector('.vc-copy').addEventListener('click', function () {
      var btn = this;
      var text = pre.innerText;
      var done = function () {
        btn.textContent = 'Copied';
        setTimeout(function () { btn.textContent = 'Copy'; }, 1600);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, done);
      else done();
    });
  });

  /* Screenshots get the figure frame, which caps their height — raw
     screenshots vary wildly in aspect ratio and otherwise own the column. */
  var INLINE_ICON = /\b[wh]-(?:3|3\.5|4|5|6|7|8|9|10|11|12|14|16)\b|inline-block/;
  [].slice.call(article.querySelectorAll('img')).forEach(function (img) {
    if (img.closest('figure') || img.closest('a') || img.closest('.vc-fig-frame')) return;
    if (INLINE_ICON.test(img.className)) return;
    var parent = img.parentNode;
    var topLevel = parent === article || parent.tagName === 'SECTION' ||
      (parent.tagName === 'P' && parent.children.length === 1 && !parent.textContent.trim());
    if (!topLevel) return;
    var fig = el('figure');
    var frame = el('div', 'vc-fig-frame');
    parent.insertBefore(fig, img);
    fig.appendChild(frame);
    frame.appendChild(img);
    img.removeAttribute('class');
    var caption = img.getAttribute('alt');
    if (caption) fig.appendChild(el('figcaption', null, esc(caption)));
    if (parent.tagName === 'P' && !parent.textContent.trim() && !parent.children.length) {
      parent.parentNode.removeChild(parent);
    }
  });

  /* Tables that are not already inside a bordered container get one. */
  [].slice.call(article.querySelectorAll('table')).forEach(function (t) {
    var parent = t.parentNode;
    if (parent.classList && (/rounded|border|overflow/.test(parent.className) || parent.classList.contains('vc-table-wrap'))) return;
    var wrap = el('div', 'vc-table-wrap');
    parent.insertBefore(wrap, t);
    wrap.appendChild(t);
  });

  /* ------------------------------------------------------------- sidebar -- */
  var side = document.querySelector('.vc-side');
  if (side && product) {
    var html = '<a class="vc-back" href="' + u(product.dir + '/') + '">' +
      '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path></svg>' +
      esc(product.homeLabel) + '</a>';
    product.groups.forEach(function (g) {
      html += '<div class="vc-grp"><span class="vc-label">' + esc(g.title) + '</span><div class="vc-grp-links">' +
        g.items.map(function (it) {
          return '<a href="' + esc(it.h) + '"' + (it.h === file ? ' class="active" aria-current="page"' : '') + '>' + esc(it.l) + '</a>';
        }).join('') + '</div></div>';
    });
    side.innerHTML = html;
    side.setAttribute('aria-label', 'Documentation');
  }

  var toggle = document.getElementById('vc-sidebar-toggle');
  function setSidebar(open) {
    if (!side) return;
    side.classList.toggle('closed', !open);
    if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  var stored = null;
  try { stored = localStorage.getItem('vc-docs-sidebar'); } catch (e) {}
  setSidebar(stored ? stored === 'open' : window.innerWidth > 1024);
  if (toggle) toggle.addEventListener('click', function () {
    var open = side.classList.contains('closed');
    setSidebar(open);
    try { localStorage.setItem('vc-docs-sidebar', open ? 'open' : 'closed'); } catch (e) {}
  });

  /* --------------------------------------------------------- breadcrumbs -- */
  fill('crumbs', (function () {
    var nav = el('nav', 'vc-crumbs');
    nav.setAttribute('data-noprint', '1');
    nav.setAttribute('aria-label', 'Breadcrumb');
    nav.innerHTML = '<a href="' + u('') + '">Docs</a><span>/</span>' +
      (product ? '<a href="' + u(product.docsHome || product.dir + '/docs/') + '">' + esc(product.label) + '</a><span>/</span>' : '') +
      '<strong aria-current="page">' + esc(pageTitle) + '</strong>';
    return nav;
  })());

  /* ------------------------------------------------------------ meta row -- */
  var words = (article.textContent || '').trim().split(/\s+/).length;
  var readTime = Math.max(1, Math.round(words / 220));

  fill('meta', (function () {
    var row = el('div', 'vc-meta');
    var bits = '';
    if (updated) bits += '<span class="vc-meta-item">Updated ' + esc(updated) + '</span><span class="vc-vdiv"></span>';
    bits += '<span class="vc-meta-item">' + readTime + ' min read</span>';
    bits += '<span class="vc-print-exp" data-printonly="1">Exported ' + exported + ' · docs.vectored.dev</span>';
    bits += '<div class="vc-meta-actions" data-noprint="1">' +
      '<button class="vc-pdfbtn" type="button" data-print="page">' +
        '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v11m0 0l-4-4m4 4l4-4M4 19h16"></path></svg>' +
        'PDF: this page</button>' +
      (printGuide ? '<a class="vc-pdfbtn" href="' + printGuide + '">' +
        '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h10"></path></svg>' +
        'PDF: full guide</a>' : '') +
      '</div>';
    row.innerHTML = bits;
    row.querySelector('[data-print="page"]').addEventListener('click', function () { window.print(); });
    return row;
  })());

  /* --------------------------------------------- print-only title/contents -- */
  fill('printhead', (function () {
    var d = el('div', 'vc-print-head');
    d.setAttribute('data-printonly', '1');
    d.innerHTML = '<div><b>Vectored</b><span>' + esc(product ? product.label : 'Vectored') + ' · Documentation</span></div>';
    return d;
  })());

  fill('contents', (function () {
    if (!heads.length) return el('span');
    var d = el('div', 'vc-print-contents');
    d.setAttribute('data-printonly', '1');
    d.innerHTML = '<div>Contents</div><ol>' +
      heads.map(function (h) { return '<li>' + esc(h.textContent.trim()) + '</li>'; }).join('') + '</ol>';
    return d;
  })());

  /* ----------------------------------- feedback, print footer, prev/next -- */
  fill('pagefoot', (function () {
    var wrap = el('div');
    var key = 'vc-fb:' + location.pathname;

    var fb = el('div', 'vc-fb');
    fb.setAttribute('data-noprint', '1');
    function thanks() { fb.innerHTML = '<span class="vc-fb-q">Thanks — feedback recorded.</span>'; }
    var voted = null;
    try { voted = localStorage.getItem(key); } catch (e) {}
    if (voted) thanks();
    else {
      fb.innerHTML = '<span class="vc-fb-q">Was this page helpful?</span>' +
        '<div class="vc-fb-btns"><button type="button" data-v="yes">Yes</button>' +
        '<button type="button" data-v="no">No</button></div>';
      fb.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-v]');
        if (!b) return;
        try { localStorage.setItem(key, b.dataset.v); } catch (err) {}
        thanks();
      });
    }
    wrap.appendChild(fb);

    var pf = el('div', 'vc-print-foot');
    pf.setAttribute('data-printonly', '1');
    pf.setAttribute('data-print-footer', '1');
    pf.innerHTML = '<span>Vectored · ' + esc(product ? product.label : '') + ' · ' + esc(pageTitle) + '</span>' +
      '<span>Exported ' + exported + ' · docs.vectored.dev' + esc(location.pathname.replace(/\.html$/, '')) + '</span>';
    wrap.appendChild(pf);

    if (idx !== -1) {
      var prev = idx > 0 ? pages[idx - 1] : null;
      var next = idx < pages.length - 1 ? pages[idx + 1] : null;
      if (prev || next) {
        var pn = el('div', 'vc-pn');
        pn.setAttribute('data-noprint', '1');
        if (prev) pn.innerHTML += '<a href="' + esc(prev.h) + '"><div class="lbl">← Previous</div><div class="ttl">' + esc(prev.l) + '</div></a>';
        if (next) pn.innerHTML += '<a class="next" href="' + esc(next.h) + '"><div class="lbl">Next →</div><div class="ttl">' + esc(next.l) + '</div></a>';
        wrap.appendChild(pn);
      }
    }
    return wrap;
  })());

  /* ---------------------------------------------------------- right rail -- */
  var rail = document.querySelector('.vc-rail');
  if (rail) {
    var editPath = location.pathname.replace(/^\//, '');
    rail.setAttribute('aria-label', 'On this page');
    rail.innerHTML =
      '<span class="vc-label">On this page</span>' +
      '<nav class="vc-toc">' + heads.map(function (h) {
        return '<a href="#' + h.id + '">' + esc(h.textContent.trim()) + '</a>';
      }).join('') + '</nav>' +
      '<div class="vc-rail-links">' +
        '<a href="' + REPO + '/edit/main/' + esc(editPath) + '" target="_blank" rel="noopener">' +
          '<svg viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>' +
          'Suggest an edit</a>' +
        (printGuide ? '<a href="' + printGuide + '">Download full guide (PDF)</a>' : '') +
        '<a href="' + u('support.html') + '">Ask support</a>' +
      '</div>';

    /* Scrollspy: the last heading that has passed the sticky header wins. */
    var links = [].slice.call(rail.querySelectorAll('.vc-toc a'));
    var active = null;
    function spy() {
      var current = heads.length ? heads[0].id : null;
      heads.forEach(function (h) {
        if (h.getBoundingClientRect().top <= 140) current = h.id;
      });
      if (current === active) return;
      active = current;
      links.forEach(function (a) {
        a.classList.toggle('active', a.getAttribute('href') === '#' + current);
      });
    }
    spy();
    window.addEventListener('scroll', spy, { passive: true });
  }
})();
