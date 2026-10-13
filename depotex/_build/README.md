# Depotex docs build

Private placeholder docs. The whole `depotex/` folder is gitignored until the
product is ready to publish — nothing here reaches the public site.

```bash
python3 depotex/_build/build.py
```

Same engine and block syntax as `timesheets/_build` (see its README).

| File | What is in it |
|---|---|
| `engine.py` | Copy of the TimeSheets engine, rebranded, Ko-fi pill removed |
| `build.py` | Landing intro |
| `content.py` | Every page, plus the `CHANGELOG` list |

## Keeping docs in step with the code

The depotex repo has hooks (Kiro `agentStop`, Claude Code `Stop`) that ask the
agent to update these docs whenever a feature is added or changed:

1. Update or add the feature's page in `content.py`.
2. Add a line at the top of `CHANGELOG`.
3. Run the build.

## Before publishing

- Remove `depotex/` from `.gitignore`.
- Add a `depotex` entry to `GROUPS` and the product list in `tools/gen_nav.py`,
  then regenerate `assets/nav.js` so the sidebar lists these pages.
- Add a product card to the homepage `index.html`, and to `sitemap.xml`.
- Add `assets/icon.png` / `icon-64.png`.
