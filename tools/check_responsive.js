/* Render pages in real Chrome at phone, tablet and desktop widths and report
   anything that overflows sideways or lands off-screen.

   jsdom has no layout engine, so the other checks in this directory cannot see
   a header that is wider than the viewport — the exact failure this catches.

     node tools/check_responsive.js [--all]

   Needs Chrome installed and puppeteer-core resolvable (NODE_PATH is fine).
*/
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const ROOT = path.dirname(__dirname);
const CHROME = process.env.CHROME_PATH ||
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const VIEWPORTS = [
  { name: 'phone', width: 390, height: 844, mobile: true },
  { name: 'small-phone', width: 320, height: 568, mobile: true },
  { name: 'tablet', width: 820, height: 1180, mobile: true },
  { name: 'laptop', width: 1280, height: 800, mobile: false },
];

const SAMPLE = [
  'index.html',
  'feedback.html',
  'support.html',
  'apistudio/index.html',
  'macrotoolkit/index.html',
  'timesheets/index.html',
  'blog/index.html',
  'forms/docs/getting-started.html',
  'apistudio/docs/quick-start.html',
  'timesheets/docs/reports.html',
  'macrotoolkit/docs/clock.html',
];

function allPages() {
  const out = [];
  const walk = dir => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        if (!['.git', 'node_modules', 'tools', '_build'].includes(entry.name)) walk(p);
      } else if (entry.name.endsWith('.html') && !entry.name.startsWith('_')) {
        out.push(path.relative(ROOT, p));
      }
    }
  };
  walk(ROOT);
  return out.sort();
}

(async () => {
  const pages = process.argv.includes('--all') ? allPages() : SAMPLE;
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new' });
  const page = await browser.newPage();
  let bad = 0;

  for (const rel of pages) {
    for (const vp of VIEWPORTS) {
      await page.setViewport({ width: vp.width, height: vp.height, isMobile: vp.mobile });
      await page.goto('file://' + path.join(ROOT, rel), { waitUntil: 'networkidle0' });
      await new Promise(r => setTimeout(r, 120));

      // Menus are the easiest thing to get wrong on a phone and the easiest to
      // miss, since they measure fine while closed.
      await page.evaluate(() => {
        const sw = document.getElementById('vc-switch');
        if (sw) sw.click();
        const sb = document.getElementById('vc-search-toggle');
        if (sb && getComputedStyle(sb).display !== 'none') sb.click();
      });
      await new Promise(r => setTimeout(r, 100));

      const report = await page.evaluate(w => {
        const de = document.documentElement;
        const overflow = de.scrollWidth - w;
        const wide = [];
        if (overflow > 1) {
          for (const el of document.querySelectorAll('body *')) {
            const r = el.getBoundingClientRect();
            if (r.width === 0 || r.height === 0) continue;
            if (r.right > w + 1 || r.left < -1) {
              const cs = getComputedStyle(el);
              if (cs.position === 'fixed' && cs.visibility === 'hidden') continue;
              if (el.closest('[data-printonly]')) continue;
              // Something inside a scroll container is allowed to be wider.
              let scroller = el.parentElement, inScroller = false;
              while (scroller && scroller !== document.body) {
                const o = getComputedStyle(scroller).overflowX;
                if (o === 'auto' || o === 'scroll') { inScroller = true; break; }
                scroller = scroller.parentElement;
              }
              if (inScroller) continue;
              wide.push(el.tagName.toLowerCase() +
                (el.id ? '#' + el.id : '') +
                (el.className && typeof el.className === 'string'
                  ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '') +
                ' [' + Math.round(r.left) + '→' + Math.round(r.right) + ']');
            }
          }
        }
        const header = document.querySelector('header.vc-hd');
        return {
          overflow,
          wide: [...new Set(wide)].slice(0, 4),
          headerH: header ? Math.round(header.getBoundingClientRect().height) : null,
          switcherVisible: !!document.querySelector('.vc-switch') &&
            getComputedStyle(document.querySelector('.vc-switch-wrap')).display !== 'none',
        };
      }, vp.width);

      const issues = [];
      if (report.overflow > 1) {
        issues.push(`overflows by ${report.overflow}px` +
          (report.wide.length ? ' — ' + report.wide.join('; ') : ''));
      }
      if (report.headerH && report.headerH > 72) issues.push(`header ${report.headerH}px tall`);
      if (report.headerH && !report.switcherVisible) issues.push('no product switcher');
      if (issues.length) {
        bad++;
        console.log(`FAIL ${rel} @${vp.name} (${vp.width}px) -> ${issues.join('; ')}`);
      }
    }
  }

  await browser.close();
  console.log(`${pages.length} pages × ${VIEWPORTS.length} viewports, ${bad} failing combinations`);
  process.exit(bad ? 1 : 0);
})();
