/* Smoke-test the shared documentation shell.

   Loads pages in jsdom with the local scripts running (the Tailwind CDN is
   stubbed — it only supplies utility classes, not behaviour) and asserts that
   header.js, docs.js and footer.js actually built what each page needs:
   sidebar, breadcrumbs, meta row, table of contents, prev/next and footer.

     node tools/smoke.js            # a representative page per product
     node tools/smoke.js --all      # every doc page
*/
const fs = require('fs');
const path = require('path');
const { JSDOM, VirtualConsole, requestInterceptor } = require('jsdom');

const ROOT = path.dirname(__dirname);

// Everything the shell needs is local; the CDN only ships utility CSS.
const localOnly = {
  interceptors: [requestInterceptor(request => {
    if (!request.url.startsWith('file:')) {
      return new Response('', { headers: { 'Content-Type': 'application/javascript' } });
    }
  })]
};

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

  need('header.vc-hd', 'header');
  need('.vc-hd .vc-switch', 'product switcher');
  need('#doc-search', 'search input');
  need('footer.vc-ft', 'footer');
  need('.vc-side .vc-grp-links a', 'sidebar links');
  need('.vc-crumbs strong', 'breadcrumbs');
  need('.vc-meta .vc-meta-item', 'meta row');
  need('.vc-meta [data-print="page"]', 'PDF button');
  need('.vc-fb', 'feedback block');
  need('.vc-print-head', 'print title block');
  need('article.vc-doc', 'article');

  if (d.querySelectorAll('article.vc-doc h2').length && !d.querySelector('.vc-toc a')) {
    problems.push('missing table of contents');
  }
  if (!d.querySelector('.vc-side a.active')) problems.push('sidebar has no active page');
  if (!d.querySelector('.vc-pn a')) problems.push('missing prev/next');
  if (d.querySelectorAll('article.vc-doc pre').length && !d.querySelector('.vc-code .vc-copy')) {
    problems.push('code block not framed');
  }
  if (d.querySelector('[data-vc]')) problems.push('unfilled placeholder: ' + d.querySelector('[data-vc]').dataset.vc);

  dom.window.close();
  return { rel, problems, errors };
}

(async () => {
  const all = process.argv.includes('--all');
  const pages = pagesFor(all);
  let bad = 0;
  for (const p of pages) {
    const r = await check(p);
    const issues = r.problems.concat(r.errors.map(e => 'JS: ' + e.split('\n')[0]));
    if (issues.length) { bad++; console.log('FAIL', r.rel, '->', issues.join('; ')); }
  }
  console.log(`${pages.length - bad}/${pages.length} pages passed`);
  process.exit(bad ? 1 : 0);
})();
