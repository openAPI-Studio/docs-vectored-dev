# tools

Maintenance scripts for docs.vectored.dev. All are run from the site root and
need only Python 3 (`beautifulsoup4`) or Node (`jsdom`, for the smoke test).

| Script | What it does |
| --- | --- |
| `gen_nav.py` | Regenerates `assets/nav.js` — the grouped sidebar, search index and switcher counts — from the pages on disk. Run after adding, removing or renaming a doc page, and add the new page to that script's `GROUPS` table first; it fails loudly if a page belongs to no group. |
| `stamp_updated.py` | Writes each doc page's `<meta name="vc-updated">` from the file's last commit date, which is what the meta row prints. Run after regenerating pages. |
| `migrate_docs.py` | One-shot: ported the 130 doc pages onto the shared shell. Kept because it documents exactly what was stripped from each page and can be re-run if a page is restored from an old revision. |
| `migrate_pages.py` | The same, for the landing, support, legal, blog and error pages. |
| `check_content.py` | Diffs the visible words of two copies of the site, page by page. Used to prove the migration lost no content: `python3 tools/check_content.py OLD_TREE .` |
| `check_links.py` | Verifies every local `href`/`src` resolves to a file that exists. |
| `smoke.js` | Loads pages in jsdom with the real scripts running and asserts the shell built everything: sidebar, breadcrumbs, meta row, contents, TOC, prev/next, footer. `node tools/smoke.js --all` covers every doc page. |

## The shared shell

A doc page ships only its own `<head>`, an `<h1 class="vc-h1">`, an optional
`<p class="vc-lede">` and an `<article class="vc-doc">`. Everything around it
comes from:

- `assets/tokens.css` — colour tokens, light theme, print rules, the page shell
  and the prose layer;
- `assets/tailwind-config.js` — the shared Tailwind CDN config;
- `assets/nav.js` — per-product navigation, search index and switcher data;
- `assets/header.js`, `assets/footer.js` — the header and footer;
- `assets/docs.js` — sidebar, breadcrumbs, meta row, TOC and scrollspy,
  code-block framing, figures, feedback, prev/next and the print blocks;
- `assets/print-guide.js` — the per-product `docs/print.html` full-guide export.
