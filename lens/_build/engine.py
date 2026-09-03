"""Block markup for the Lens docs.

Mirrors timesheets/_build/engine.py, trimmed to the blocks these pages use. A
page is a list of blocks so the content file reads like an outline rather than a
template language.
"""
import html
import re

SHOTS = []  # (filename, caption, page_label) — collected for SCREENSHOTS.md


# --- blocks ------------------------------------------------------------------

def P(text):
    return ("p", text)


def H(text):
    return ("h", text)


def UL(items):
    return ("ul", items)


def OL(items):
    return ("ol", items)


def STEPS(items):
    """Numbered procedure. "Do this|and here is why" splits into step + detail."""
    return ("steps", items)


def TABLE(cols, rows):
    return ("table", (cols, rows))


def NOTE(text):
    return ("note", text)


def WARN(text):
    return ("warn", text)


def SHOT(filename, caption):
    """A screenshot slot. `filename` is what the user saves into lens/assets."""
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


# --- rendering ---------------------------------------------------------------

NOTE_ICON = ('<svg class="w-5 h-5 shrink-0 text-cta mt-0.5" fill="none" stroke="currentColor" '
             'stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewBox="0 0 24 24">'
             '<circle cx="12" cy="12" r="10"></circle><line x1="12" x2="12" y1="16" y2="12"></line>'
             '<line x1="12" x2="12.01" y1="8" y2="8"></line></svg>')

WARN_ICON = ('<svg class="w-5 h-5 shrink-0 text-amber-400 mt-0.5" fill="none" stroke="currentColor" '
             'stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewBox="0 0 24 24">'
             '<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>'
             '<line x1="12" x2="12" y1="9" y2="13"></line><line x1="12" x2="12.01" y1="17" y2="17"></line></svg>')

SHOT_ICON = ('<svg class="w-7 h-7 text-muted" fill="none" viewBox="0 0 24 24" stroke="currentColor" '
             'stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/>'
             '<circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>')


def render(blocks, page_label):
    out = []
    hn = 0
    for kind, val in blocks:
        if kind == "p":
            out.append('<p class="text-muted mb-4">%s</p>' % inline(val))

        elif kind == "h":
            hn += 1
            out.append('<h2 class="text-2xl font-semibold mt-10 mb-4">%d. %s</h2>'
                       % (hn, inline(val)))

        elif kind == "ul":
            items = "".join('<li class="mb-2">%s</li>' % inline(i) for i in val)
            out.append('<ul class="list-disc pl-6 text-muted mb-4">%s</ul>' % items)

        elif kind == "ol":
            items = "".join('<li class="mb-2">%s</li>' % inline(i) for i in val)
            out.append('<ol class="list-decimal pl-6 text-muted mb-4">%s</ol>' % items)

        elif kind == "steps":
            lis = []
            for raw in val:
                head, _, detail = raw.partition("|")
                body = '<strong class="text-text">%s</strong>' % inline(head.strip())
                if detail.strip():
                    body += ' <span class="text-muted">%s</span>' % inline(detail.strip())
                lis.append('<li class="mb-3">%s</li>' % body)
            out.append('<ol class="list-decimal pl-6 text-muted mb-4">%s</ol>' % "".join(lis))

        elif kind == "table":
            cols, rows = val
            head = "".join("<th>%s</th>" % inline(c) for c in cols)
            body = "".join(
                "<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r)
                for r in rows)
            out.append('<div class="tbl-wrap"><table><thead><tr>%s</tr></thead>'
                       "<tbody>%s</tbody></table></div>" % (head, body))

        elif kind == "note":
            out.append('<div class="flex gap-3 rounded-xl border border-cta/30 bg-cta/10 '
                       'px-4 py-3 my-6" role="note">%s<p class="text-sm text-muted">%s</p></div>'
                       % (NOTE_ICON, inline(val)))

        elif kind == "warn":
            out.append('<div class="flex gap-3 rounded-xl border border-amber-500/40 '
                       'bg-amber-500/10 px-4 py-3 my-6" role="note">%s'
                       '<p class="text-sm text-muted">%s</p></div>'
                       % (WARN_ICON, inline(val)))

        elif kind == "shot":
            filename, caption = val
            SHOTS.append((filename, caption, page_label))
            # The <img> is attempted first; if the file is not there yet its
            # onerror reveals the placeholder frame, so an unshot page looks
            # unfinished rather than showing a broken image.
            out.append(
                '<figure class="shot mb-6">\n'
                '        <img src="../assets/%s" alt="%s" loading="lazy"\n'
                '             class="rounded-lg border border-border"\n'
                '             onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'">\n'
                '        <div style="display:none" class="flex-col items-center justify-center '
                'text-center gap-2 rounded-lg border-2 border-dashed border-border bg-surface/50 px-6 py-10">\n'
                '          %s\n'
                '          <p class="text-sm text-muted">Screenshot needed</p>\n'
                '          <p class="font-mono text-xs text-cta break-all">%s</p>\n'
                '          <p class="text-xs text-muted max-w-md">%s</p>\n'
                '        </div>\n'
                '        <figcaption class="text-xs text-muted mt-2">%s</figcaption>\n'
                '      </figure>'
                % (filename, html.escape(caption, quote=True), SHOT_ICON,
                   html.escape(filename), html.escape(caption), html.escape(caption)))

        else:
            raise ValueError("unknown block: " + kind)

    return "\n".join(out)


# --- page shell --------------------------------------------------------------
# A doc page ships only its own <head>, an <h1>, an optional lede and the
# <article>. Everything else is built at runtime by the shared assets.

PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Lens Docs</title>
  <meta name="description" content="{desc}">
  <meta name="vc-updated" content="{updated}">
  <link rel="icon" type="image/svg+xml" href="../../favicon.svg">
  <script>(function(){{var t=null;try{{t=localStorage.getItem('theme')}}catch(e){{}}
    var light=t?t==='light':window.matchMedia('(prefers-color-scheme:light)').matches;
    var d=document.documentElement;d.dataset.theme=light?'light':'dark';
    d.classList.toggle('dark',!light);d.classList.toggle('light',light);}})();</script>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="../../assets/tailwind-config.js"></script>
  <link rel="stylesheet" href="../../assets/tokens.css">
</head>
<body>

<div id="vc-header"></div>
<script src="../../assets/nav.js"></script>
<script src="../../assets/header.js"></script>

<div class="bg-cta/10 border-b border-cta/20 px-4 py-2 text-center text-sm font-medium"><span class="text-cta">Lens is out.</span> <a class="text-cta hover:underline" href="https://chromewebstore.google.com/detail/lens-by-vectored-tab-capt/gjonlnbkjjlhkcbbebagiadphdfipdki" data-store="lens" target="_blank" rel="noopener">Install for Chrome or Edge &rarr;</a></div>

<div class="vc-shell">
  <aside class="vc-side" data-noprint="1"></aside>

  <main class="vc-main">
    <div class="vc-col">
      <div data-vc="printhead"></div>
      <div data-vc="crumbs"></div>
      <div class="page-icon-chip w-11 h-11 rounded-xl bg-cta/10 border border-cta/20 text-cta flex items-center justify-center mt-6"><svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24">{icon}</svg></div>
      <h1 class="vc-h1">{title}</h1>
      <p class="vc-lede">{lede}</p>
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

ICONS = {
    "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91 0z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/>',
    "crop": '<path d="M6 2v14a2 2 0 0 0 2 2h14"/><path d="M18 22V8a2 2 0 0 0-2-2H2"/>',
    "video": '<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>',
    "folder": '<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>',
    "list": '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>',
    "sliders": '<line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/>',
    "keyboard": '<rect x="2" y="4" width="20" height="16" rx="2"/><line x1="6" y1="9" x2="6" y2="9"/><line x1="10" y1="9" x2="10" y2="9"/><line x1="14" y1="9" x2="14" y2="9"/><line x1="18" y1="9" x2="18" y2="9"/><line x1="7" y1="14" x2="17" y2="14"/>',
    "life-buoy": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><line x1="4.93" y1="4.93" x2="9.17" y2="9.17"/><line x1="14.83" y1="14.83" x2="19.07" y2="19.07"/><line x1="14.83" y1="9.17" x2="19.07" y2="4.93"/><line x1="4.93" y1="19.07" x2="9.17" y2="14.83"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
}
