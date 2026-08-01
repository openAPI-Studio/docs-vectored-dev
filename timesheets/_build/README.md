# TimeSheets docs build

The HTML under `timesheets/docs/` is **generated**. Edit the content files here,
not the HTML — a hand edit to a generated page is lost on the next build.

```bash
python3 timesheets/_build/build.py
```

No dependencies beyond Python 3.

## Layout

| File | What is in it |
|---|---|
| `engine.py` | Markup, theme, shared nav, screenshot slots, on-this-page nav |
| `build.py` | Page order, the landing intro, and which pages are hand-written |
| `content_core.py` | Getting started, logging, templates, cost centres |
| `content_approvals.py` | Approvals, weekly submission, delegation, history, locking |
| `content_leave.py` | Leave, holidays, dashboard, calendar, summary |
| `content_billing.py` | Reports, clients, rates, invoices, billing health |
| `content_admin.py` | Scheduled reports, project settings, sync, email, scheduler, personal settings, data requests, permissions |
| `content_settings.py` | Admin settings — the long per-setting reference |

## Writing content

A page is a list of blocks. The blocks are deliberately few, so the content
files read like an outline rather than a template language:

```python
P("Prose. Supports **bold**, `code` and [links](other-page.html).")
H("A section heading")            # numbered automatically; gets an anchor
UL([...]) / OL([...])             # bullet and numbered lists
STEPS(["Do this|and here is why", ...])   # numbered procedure
TABLE(["Col", "Col"], [[...], ...])
NOTE("An aside.") / WARN("Something that bites.")
SHOT("filename.png", "What the screenshot should show")
```

## Screenshots

`SHOT(...)` renders an `<img>` pointing at `assets/screenshots/<filename>`. If
the file is not there, its `onerror` reveals a dashed frame naming the file it
wants — so an unshot page looks unfinished rather than showing a broken image.
Drop the file in and it appears on the next build; no code change.

Every `SHOT` is collected into `timesheets/SCREENSHOTS.md`, which is the
worklist. That file is generated too — do not edit it by hand.

## Hand-written pages

`build.py` lists them in `HANDWRITTEN`. Their bodies are never regenerated;
only their sidebar and search index are refreshed, so they still pick up links
to pages added later. `privacy-security.html` is one, because it is a reference
document that was written directly rather than assembled from blocks.

## On-this-page navigation

Added as a post-process over the finished HTML, so generated and hand-written
pages get identical treatment. It gives every `<h2>` a slug anchor, builds the
right-hand nav, and adds the scroll handler that highlights the current
section. Idempotent — a page that already has one is left alone.
