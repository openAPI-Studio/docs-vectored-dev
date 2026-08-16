/* Smoke-test the shared documentation shell.

   Loads pages in jsdom with the local scripts running (the Tailwind CDN is
   stubbed — it only supplies utility classes, not behaviour) and asserts that
   header.js, docs.js and footer.js actually built what each page needs:
   sidebar, breadcrumbs, meta row, table of contents, prev/next and footer.

     node tools/smoke.js            # a representative page per product
     node tools/smoke.js --all      # every doc page
     node tools/smoke.js --pages    # the landing, legal, blog and error pages
*/
const fs = require('fs');
const path = require('path');
const { JSDOM, VirtualConsole, requestInterceptor } = require('jsdom');
const { fileURLToPath } = require('url');

const ROOT = path.dirname(__dirname);

// Everything the shell needs is local; the CDN only ships utility CSS.
const localOnly = {
  interceptors: [requestInterceptor(request => {
    if (!request.url.startsWith('file:')) {
      return new Response('', { headers: { 'Content-Type': 'application/javascript' } });
    }
  })]
};

// Pages that are not documentation: they take the header, footer and tokens
// but none of the docs shell.
const OTHER_PAGES = [
  'index.html', '404.html', 'feedback.html', 'feedback-thanks.html',
  'privacy.html', 'security.html', 'support.html',
  'apistudio/index.html', 'apistudio/support.html', 'apistudio/landing-old.html',
  'forms/index.html', 'macrotoolkit/index.html', 'macrotoolkit/support.html',
  'macrotoolkit/privacy.html', 'macrotoolkit/security.html', 'macrotoolkit/terms.html',
  'rewardhub/index.html', 'timesheets/index.html', 'blog/index.html',
  'blog/posts/introducing-forms-and-frontdoor.html',
  'blog/posts/slack-teams-notifications-confluence-forms.html'
];

function pagesFor(all) {
  const dirs = ['apistudio', 'timesheets', 'macrotoolkit', 'forms', 'rewardhub'];
  const out = [];
  for (const d of dirs) {
    const dir = path.join(ROOT, d, 'docs');
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f !== 'print.html').sort();
    out.push(...(all ? files : files.slice(0, 2)).map(f => path.join(d, 'docs', f)));
  }
  return out;
}

async function check(rel) {
  const file = path.join(ROOT, rel);
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => errors.push(String(e.message)));
  vc.on('error', m => errors.push(String(m)));

  const dom = await JSDOM.fromFile(file, {
    runScripts: 'dangerously',
    resources: localOnly,
    virtualConsole: vc,
    pretendToBeVisual: true,
    beforeParse(window) {
      // jsdom has no media queries; the theme bootstrap asks for the system
      // preference before anything else runs.
      window.matchMedia = () => ({
        matches: false, media: '', onchange: null,
        addListener() {}, removeListener() {},
        addEventListener() {}, removeEventListener() {}, dispatchEvent() { return false; }
      });
    },
  });
  await new Promise(r => setTimeout(r, 120));
  const d = dom.window.document;
  const problems = [];
  const need = (sel, label) => { if (!d.querySelector(sel)) problems.push('missing ' + label); };

  const isDoc = !!d.querySelector('.vc-shell');

  need('header.vc-hd', 'header');
  need('.vc-hd .vc-switch', 'product switcher');
  need('#doc-search', 'search input');
  need('footer.vc-ft', 'footer');
  if (isDoc) need('.vc-side .vc-grp-links a', 'sidebar links');
  if (isDoc) need('.vc-crumbs strong', 'breadcrumbs');
  if (isDoc) need('.vc-meta .vc-meta-item', 'meta row');
  if (isDoc) need('.vc-meta [data-print="page"]', 'PDF button');
  if (isDoc) need('.vc-fb', 'feedback block');
  if (isDoc) need('.vc-print-head', 'print title block');
  if (isDoc) need('article.vc-doc', 'article');

  if (isDoc) {
    if (d.querySelectorAll('article.vc-doc h2').length && !d.querySelector('.vc-toc a')) {
      problems.push('missing table of contents');
    }
    if (!d.querySelector('.vc-side a.active')) problems.push('sidebar has no active page');
    if (!d.querySelector('.vc-pn a')) problems.push('missing prev/next');
    if (d.querySelectorAll('article.vc-doc pre').length && !d.querySelector('.vc-code .vc-copy')) {
      problems.push('code block not framed');
    }
  }
  if (d.querySelector('[data-vc]')) problems.push('unfilled placeholder: ' + d.querySelector('[data-vc]').dataset.vc);

  // The header, footer and sidebar links are built at runtime, so a static
  // scan of the HTML never sees them — this is where a switcher entry
  // pointing at a directory with no index.html shows up.
  const pageDir = path.dirname(file);
  for (const a of d.querySelectorAll('a[href]')) {
    const href = a.getAttribute('href');
    if (!href || /^(https?:|mailto:|tel:|data:|javascript:|#)/.test(href)) continue;
    let target = decodeURIComponent(href.split('#')[0].split('?')[0]);
    if (!target) continue;
    if (target.startsWith('file:')) target = fileURLToPath(target);
    // A leading slash means the deployed site root, not the filesystem root.
    let full = target.startsWith('/') && !target.startsWith(ROOT)
      ? path.join(ROOT, target)
      : path.resolve(pageDir, target);
    if (fs.existsSync(full) && fs.statSync(full).isDirectory()) full = path.join(full, 'index.html');
    if (!fs.existsSync(full)) problems.push('dead link: ' + href);
  }

  dom.window.close();
  return { rel, problems, errors };
}

(async () => {
  const all = process.argv.includes('--all');
  const pages = process.argv.includes('--pages') ? OTHER_PAGES : pagesFor(all);
  let bad = 0;
  for (const p of pages) {
    const r = await check(p);
    const issues = r.problems.concat(r.errors.map(e => 'JS: ' + e.split('\n')[0]));
    if (issues.length) { bad++; console.log('FAIL', r.rel, '->', issues.join('; ')); }
  }
  console.log(`${pages.length - bad}/${pages.length} pages passed`);
  process.exit(bad ? 1 : 0);
})();
