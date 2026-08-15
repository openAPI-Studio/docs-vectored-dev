#!/usr/bin/env python3
"""
Rendering engine for the TimeSheets docs.

Content lives in `content.py` as a list of BLOCKS per page, so prose stays
readable and is never buried in escaped HTML. This file owns the markup, the
theme, the shared nav and the screenshot placeholders.

SCREENSHOTS. A `SHOT(...)` block renders a visible dashed frame naming the exact
file it expects, so an unshot page is obviously unfinished rather than quietly
missing an image. Every SHOT is also collected into SCREENSHOTS.md, which is the
list to work from when taking them. Drop a file into assets/screenshots/ with the
matching name and the frame is replaced by the image on the next build.
"""
import html
import pathlib
import re

# The docs tree, resolved relative to this file so the build works from a
# clone rather than from one machine.
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT.parent

# --- block constructors ------------------------------------------------------
# Each returns a tuple the renderer switches on. Deliberately tiny: the content
# file should read like an outline, not like a template language.

def H(text):                 return ("h", text)
def P(text):                 return ("p", text)
def UL(items):               return ("ul", items)
def OL(items):               return ("ol", items)
def TABLE(headers, rows):    return ("table", (headers, rows))
def NOTE(text):              return ("note", text)
def WARN(text):              return ("warn", text)
def STEPS(items):            return ("steps", items)
def CODE(text):              return ("code", text)

def SHOT(filename, caption):
    """A screenshot slot. `filename` is what the user will save into assets."""
    return ("shot", (filename, caption))


# --- inline markup -----------------------------------------------------------
# **bold**, `code`, [text](href). Everything else is escaped.

def inline(text):
    out = html.escape(text, quote=False)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                 r'<a href="\2" class="text-cta hover:underline">\1</a>', out)
    out = re.sub(r"\*\*([^*]+)\*\*", r'<strong class="text-text">\1</strong>', out)
    out = re.sub(r"`([^`]+)`", r'<span class="font-mono text-sm">\1</span>', out)
    return out


ICONS = {
    "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91 0z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z"/><polyline points="15 2 15 7 20 7"/>',
    "tag": '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>',
    "check": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    "calendar-check": '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><polyline points="9 16 11 18 15 14"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "history": '<path d="M3 3v5h5"/><path d="M3.05 13A9 9 0 1 0 6 5.3L3 8"/><polyline points="12 7 12 12 15 15"/>',
    "umbrella": '<path d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"/>',
    "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    "sun": '<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>',
    "lock-closed": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "grid": '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    "list": '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>',
    "table": '<path d="M3 3h18v18H3z"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/>',
    "send": '<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.6V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.2 4.2l2.8 2.8M17 17l2.8 2.8M1 12h4M19 12h4M4.2 19.8L7 17M17 7l2.8-2.8"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "activity": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "lock": '<rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "bell": '<path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/>',
}

# The page shell lives in assets/tokens.css, header.js, docs.js and footer.js.
# Generated pages carry nothing but their own metadata and content.
HEAD = """  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/svg+xml" href="{favicon}">
  <script>(function(){{var t=null;try{{t=localStorage.getItem('theme')}}catch(e){{}}
    var light=t?t==='light':window.matchMedia('(prefers-color-scheme:light)').matches;
    var d=document.documentElement;d.dataset.theme=light?'light':'dark';
    d.classList.toggle('dark',!light);d.classList.toggle('light',light);}})();</script>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="{up}assets/tailwind-config.js"></script>
  <link rel="stylesheet" href="{up}assets/tokens.css">"""

BANNER = '  <div class="bg-amber-500/10 border-b border-amber-500/20 px-4 py-2 text-center text-sm font-medium text-amber-400">Coming soon &mdash; TimeSheets is in active development.</div>'

# The theme toggle, sidebar, search and on-this-page nav that used to be
# emitted after every page's content now live in the shared assets, so there
# is no tail script left to write.

SHOTS = []  # (filename, caption, page label) — collected during render

# The on-this-page rail and its scrollspy are rendered by assets/docs.js.


def slugify(text):
    t = re.sub(r"<[^>]+>", "", text)
    t = html.unescape(t)
    t = re.sub(r"^\s*\d+\.\s*", "", t)          # drop the "3. " numbering
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "section"


def add_toc(path):
    """Give every h2 a stable anchor.

    Run as a post-process over the finished HTML rather than during rendering,
    so a hand-written page gets exactly the same treatment as a generated one
    and there is only one implementation to keep correct. The on-this-page rail
    itself is built at runtime by assets/docs.js from these headings — the
    anchors are stamped here so deep links stay stable across rebuilds.
    """
    doc = path.read_text(encoding="utf-8")

    heads = re.findall(r'<h2 class="([^"]*)">(.*?)</h2>', doc, flags=re.S)
    if not heads:
        return 0

    seen = {}
    entries = []

    def anchor(m):
        cls, text = m.group(1), m.group(2)
        base = slugify(text)
        seen[base] = seen.get(base, 0) + 1
        sid = base if seen[base] == 1 else f"{base}-{seen[base]}"
        label = re.sub(r"^\s*\d+\.\s*", "", re.sub(r"<[^>]+>", "", text)).strip()
        entries.append((sid, label))
        return f'<h2 id="{sid}" class="{cls} scroll-mt-28">{text}</h2>'

    doc = re.sub(r'<h2 class="([^"]*)">(.*?)</h2>', anchor, doc, flags=re.S)

    path.write_text(doc, encoding="utf-8")
    return len(entries)



def render_blocks(blocks, page_label):
    out = []
    n = 0
    for kind, val in blocks:
        if kind == "h":
            n += 1
            out.append(f'      <h2 class="text-2xl font-semibold mt-10 mb-4">{n}. {inline(val)}</h2>')
        elif kind == "p":
            out.append(f'      <p class="text-muted mb-4">{inline(val)}</p>')
        elif kind == "ul":
            items = "".join(f'<li>{inline(i)}</li>' for i in val)
            out.append(f'      <ul class="text-muted mb-4 space-y-2 list-disc pl-6">{items}</ul>')
        elif kind == "ol":
            items = "".join(f'<li>{inline(i)}</li>' for i in val)
            out.append(f'      <ol class="text-muted mb-4 space-y-2 list-decimal pl-6">{items}</ol>')
        elif kind == "steps":
            lis = "".join(
                f'<li class="pl-2"><span class="text-text font-medium">{inline(i.split("|")[0])}</span>'
                + (f' &mdash; {inline(i.split("|",1)[1])}' if "|" in i else "")
                + "</li>"
                for i in val
            )
            out.append(f'      <ol class="text-muted mb-4 space-y-3 list-decimal pl-6 marker:text-cta marker:font-semibold">{lis}</ol>')
        elif kind == "table":
            headers, rows = val
            th = "".join(f"<th>{inline(h)}</th>" for h in headers)
            tr = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in rows
            )
            out.append(f'      <div class="tbl-wrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
        elif kind == "note":
            out.append(
                '      <div class="rounded-xl border border-border bg-surface/90 p-4 mb-6">'
                f'<p class="text-sm text-muted">{inline(val)}</p></div>'
            )
        elif kind == "warn":
            out.append(
                '      <div class="rounded-xl border border-amber-500/30 bg-amber-500/5 p-4 mb-6">'
                f'<p class="text-sm text-amber-200/90">{inline(val)}</p></div>'
            )
        elif kind == "code":
            out.append(
                '      <pre class="bg-bg border border-border rounded-xl p-4 mb-6 overflow-x-auto">'
                f'<code class="font-mono text-xs text-muted">{html.escape(val)}</code></pre>'
            )
        elif kind == "shot":
            filename, caption = val
            SHOTS.append((filename, caption, page_label))
            # Per-app assets, matching how forms/assets works and where
            # timesheets/assets/icon.png already lives.
            src = f"../assets/{filename}"
            # The <img> is attempted first; if the file is not there yet its
            # onerror reveals the placeholder frame, so an unshot page looks
            # unfinished instead of showing a broken-image icon.
            out.append(f"""      <figure class="shot mb-6">
        <img src="{src}" alt="{html.escape(caption, quote=True)}" loading="lazy"
             class="rounded-lg border border-border"
             onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
        <div style="display:none" class="flex-col items-center justify-center text-center gap-2 rounded-lg border-2 border-dashed border-border bg-surface/50 px-6 py-10">
          <svg class="w-7 h-7 text-muted" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>
          <p class="text-sm text-muted">Screenshot needed</p>
          <p class="font-mono text-xs text-cta break-all">{html.escape(filename)}</p>
          <p class="text-xs text-muted max-w-md">{inline(caption)}</p>
        </div>
        <figcaption class="text-xs text-muted mt-2">{inline(caption)}</figcaption>
      </figure>""")
        else:
            raise SystemExit(f"unknown block: {kind}")
    return "\n".join(out)


# The sidebar and the search index used to be written into every page here.
# Both now come from assets/nav.js, which tools/gen_nav.py regenerates from the
# pages on disk — so adding a page is one edit, not thirty.


def doc_page(slug, p, pages):
    body = render_blocks(p["blocks"], p["label"])
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
{HEAD.format(title=p["title"] + " — TimeSheets Docs", desc=p["desc"], favicon="../../favicon.svg", up="../../")}
</head>
<body>

<div id="vc-header"></div>
<script src="../../assets/nav.js"></script>
<script src="../../assets/header.js"></script>
{BANNER}

<div class="vc-shell">
  <aside class="vc-side" data-noprint="1"></aside>

  <main class="vc-main">
    <div class="vc-col">
      <div data-vc="printhead"></div>
      <div data-vc="crumbs"></div>
      <div class="page-icon-chip w-11 h-11 rounded-xl bg-cta/10 border border-cta/20 text-cta flex items-center justify-center"><svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{ICONS[p["icon"]]}</svg></div>
      <h1 class="vc-h1">{inline(p["title"])}</h1>
      <p class="vc-lede">{inline(p["desc"])}</p>
      <div data-vc="meta"></div>
      <div data-vc="contents"></div>

      <article class="vc-doc">
{body}
      </article>

      <div data-vc="pagefoot"></div>
    </div>
  </main>

  <aside class="vc-rail" data-noprint="1"></aside>
</div>

<div id="vc-footer"></div>
<script src="../../assets/footer.js"></script>
<script src="../../assets/docs.js"></script>
</body>
</html>
"""


def landing(pages, intro_blocks):
    cards = []
    for slug, p in pages:
        cards.append(f"""        <a href="docs/{slug}.html" class="block bg-surface border border-border rounded-2xl p-6 hover:border-cta/40 transition-all duration-200 cursor-pointer group">
          <div class="text-cta mb-3"><svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{ICONS[p["icon"]]}</svg></div>
          <h3 class="font-semibold group-hover:text-cta transition-colors duration-200">{p["label"]}</h3>
          <p class="text-sm text-muted mt-2">{p["desc"]}.</p>
        </a>""")
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
{HEAD.format(title="TimeSheets — Time tracking &amp; approvals for Jira | Vectored", desc="Timesheets, approvals, leave, billing and reporting for Jira Cloud teams, from Vectored", favicon="../favicon.svg", up="../")}
</head>
<body>

<div id="vc-header"></div>
<script src="../assets/nav.js"></script>
<script src="../assets/header.js"></script>
{BANNER}

  <main class="vc-page">
    <h1 class="text-4xl font-bold mb-3">TimeSheets</h1>
    <p class="text-lg text-muted mb-10">Time tracking, approvals, leave and billing for Jira Cloud.</p>

{render_blocks(intro_blocks, "Overview")}

    <h2 class="text-2xl font-bold mb-6 mt-14">Documentation</h2>
    <div class="grid sm:grid-cols-2 gap-4">
{chr(10).join(cards)}
    </div>
  </main>

<div id="vc-footer"></div>
<script src="../assets/footer.js"></script>
</body>
</html>
"""


def build(pages, intro_blocks, handwritten=()):
    (ROOT / "docs").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets").mkdir(parents=True, exist_ok=True)

    for slug, p in pages:
        target = ROOT / "docs" / f"{slug}.html"
        if slug in handwritten:
            refresh_nav(target, pages)
            continue
        target.write_text(doc_page(slug, p, pages), encoding="utf-8")

    (ROOT / "index.html").write_text(landing(pages, intro_blocks), encoding="utf-8")

    tocs = 0
    for slug, _ in pages:
        if add_toc(ROOT / "docs" / f"{slug}.html"):
            tocs += 1

    write_manifest()
    return len(pages), len(SHOTS), tocs


def refresh_nav(path, pages):
    """Hand-written pages need nothing refreshed any more.

    They used to carry their own copy of the sidebar and the search index, so
    a new page meant rewriting all of them. Both now live in assets/nav.js, and
    a hand-written page is simply left alone.
    """
    if not path.exists():
        raise SystemExit(f"{path.name}: hand-written page is missing")


def write_manifest():
    lines = [
        "# TimeSheets docs — screenshots needed",
        "",
        f"{len(SHOTS)} screenshots. Save each one into `timesheets/assets/` using the",
        "exact filename below. The docs pick them up automatically on the next build —",
        "until then each slot renders a dashed placeholder naming the file it wants.",
        "",
        "Guidance: capture the app at a comfortable browser width (about 1440px), use",
        "the light theme unless the shot is specifically about dark mode, and use",
        "realistic but fictional names and figures rather than real people's data.",
        "",
    ]
    by_page = {}
    for filename, caption, page in SHOTS:
        by_page.setdefault(page, []).append((filename, caption))
    for page, shots in by_page.items():
        lines.append(f"## {page}")
        lines.append("")
        for filename, caption in shots:
            lines.append(f"- [ ] `{filename}`")
            lines.append(f"      {caption}")
        lines.append("")
    (ROOT / "SCREENSHOTS.md").write_text("\n".join(lines), encoding="utf-8")
