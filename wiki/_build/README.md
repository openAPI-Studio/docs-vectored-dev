# Wiki docs build

The Wiki's public docs: the user guide (`wiki/docs/`) and the admin guide
(`wiki/admin/`). Until the Wiki launches it is listed as coming soon, like
Depotex: a switcher entry in `tools/gen_nav.py`, its own sidebars in
`wiki/assets/nav-local.js`, pages in `sitemap.xml`, nothing in the `llms` files.

```bash
python3 wiki/_build/build.py
```

Same engine and block syntax as `depotex/_build` (see `timesheets/_build/README.md`).

| File | What is in it |
|---|---|
| `engine.py` | Copy of the Depotex engine, renamed; the overview page is the intro in the doc layout |
| `guides.py` | Which page is in which guide, and the two sidebars |
| `build.py` | Builds the pages and writes `wiki/assets/nav-local.js` |
| `content.py` | The overview intro and the changelog, and the list of every page |
| `content_user_a.py`, `content_user_b.py` | User guide pages |
| `content_admin_wiki.py` | Admin pages about the Wiki itself (install, setup, licensing, anonymous access, imports, Q&A moderation, known issues) |
| `content_platform_config.py`, `content_platform_operate.py` | Platform features the Wiki shares with Depotex, rewritten for the Wiki |

## Keeping docs in step with the code

The Wiki lives in `apps/wiki` of the depotex repo. Its `docs-sync.md` rule
sends every Wiki change here:

1. Update or add the feature's page.
2. Add a line at the top of `CHANGELOG` in `content.py`.
3. Run the build. `WIKI_DOCS_PARTIAL=1` lets it run while pages named in
   `guides.py` are still being written; the published build is strict.

Screenshots go in `wiki/assets/` under the name their `SHOT` gives;
`SCREENSHOTS.md` lists every slot. A platform screen that changes in Depotex
usually changes here too.
