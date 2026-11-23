# Wiki docs build

The Wiki's public docs: the user guide (`wiki/docs/`) and the admin guide
(`wiki/admin/`). Until the Wiki launches it is listed as coming soon, like
Depotex: a switcher entry in `tools/gen_nav.py`, its own sidebars in
`wiki/assets/nav-local.js`, pages in `sitemap.xml`, nothing in the `llms` files.

```bash
python3 wiki/_build/build.py
```

Same engine and block syntax as `depotex/_build` (see `timesheets/_build/README.md`),
plus how-to steps (below).

| File | What is in it |
|---|---|
| `engine.py` | Copy of the Depotex engine, renamed; the overview page is the intro in the doc layout |
| `guides.py` | Which page is in which guide, and the two sidebars |
| `build.py` | Builds the pages and writes `wiki/assets/nav-local.js` |
| `index.py` | Writes the docs index the product embeds (pages, sections, how-to steps); not part of the site |
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

## How-to steps and "Show me"

The Wiki's assistant answers "how do I..." questions from these docs and can
walk a person through the steps, marking each control on screen. The steps are
this data, written by hand; nothing is made up at run time.

A `STEPS` block becomes a how-to when it has an id and a task:

```python
STEPS([
    ("Open the space and select **Space settings** in its sidebar.", "space-rail.settings"),
    ("Open the **Members** tab.", "space-tabs.members"),
    "To change a role, pick another one next to the member.",
], howto="add-a-space-member", task="Add a person or a group to a space, or change their role"),
```

- `howto`: a kebab-case id, unique across the Wiki docs, and stable: the
  product's tests name it.
- `task`: what the steps achieve, in the words a person would ask with.
- A step is text, or `(text, "screen.control")`: the control it points at,
  by the anchor the product registers for it (`data-kee-anchor`; the registry
  is `apps/wiki/frontend/src/kee-screens/` in the depotex repo). A step
  without an anchor is shown as text only.
- The page renders the same with or without them.

When a screen changes (a moved button, a new step, a renamed tab), change its
steps and its screenshot together. The product's test `ai-reach.test.ts` fails
when a step names an anchor that is not registered, and its index check fails
when the embedded index is older than these files.

## The docs index

```bash
python3 wiki/_build/index.py --out   <depotex>/apps/wiki/backend/internal/docsindex/docs-index.json
python3 wiki/_build/index.py --check <depotex>/apps/wiki/backend/internal/docsindex/docs-index.json
```

(`make wiki-docs-index` and `make check-wiki-docs-index` in the depotex repo
run these.) One line per page: its sections as Markdown, links made absolute,
how-tos with their steps and anchors. The changelog is left out. The file is
written into the product's source tree only: until the Wiki launches, no index
is published on the site (the same rule that keeps the Wiki out of the `llms`
files), and the script refuses a path inside this repo.
