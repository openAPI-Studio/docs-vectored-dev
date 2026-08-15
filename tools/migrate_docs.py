#!/usr/bin/env python3
"""Port every */docs/*.html page onto the shared documentation shell.

Each page currently repeats its own copy of the Tailwind config, a light-theme
override <style>, a theme bootstrap, the sidebar markup, the search index and
the theme/menu scripts. This script strips all of that and leaves the page with
what is genuinely its own: <head> metadata, the h1, the lede and the body
content — which is preserved verbatim. Everything else is rendered at runtime
by assets/header.js, assets/docs.js and assets/footer.js.

Run from the site root:  python3 tools/migrate_docs.py [--check]
"""
import os, re, sys, glob, html, subprocess
from bs4 import BeautifulSoup, NavigableString, Tag, Comment

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = '--check' in sys.argv

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def git_dates():
    """Last commit date per file — the honest source for 'Updated'."""
    out = subprocess.run(
        ['git', 'log', '--name-only', '--pretty=format:%cI', '--', '*/docs/*.html'],
        cwd=ROOT, capture_output=True, text=True).stdout
    dates, current = {}, None
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\d{4}-\d{2}-\d{2}T', line):
            current = line
        elif current and line not in dates:
            dates[line] = current
    return {k: '%d %s %s' % (int(v[8:10]), MONTHS[int(v[5:7]) - 1], v[0:4])
            for k, v in dates.items()}


DATES = git_dates()

HEAD = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
{meta}  <link rel="icon" type="image/svg+xml" href="{up}favicon.svg">
  <script>(function(){{var t=null;try{{t=localStorage.getItem('theme')}}catch(e){{}}
    var light=t?t==='light':window.matchMedia('(prefers-color-scheme:light)').matches;
    var d=document.documentElement;d.dataset.theme=light?'light':'dark';
    d.classList.toggle('dark',!light);d.classList.toggle('light',light);}})();</script>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="{up}assets/tailwind-config.js"></script>
  <link rel="stylesheet" href="{up}assets/tokens.css">
</head>
<body>

<div id="vc-header"></div>
<script src="{up}assets/nav.js"></script>
<script src="{up}assets/header.js"></script>
{banner}
<div class="vc-shell">
  <aside class="vc-side" data-noprint="1"></aside>

  <main class="vc-main">
    <div class="vc-col">
      <div data-vc="printhead"></div>
      <div data-vc="crumbs"></div>
{chip}      <h1 class="vc-h1">{h1}</h1>
{lede}      <div data-vc="meta"></div>
      <div data-vc="contents"></div>

      <article class="vc-doc">
{content}
      </article>

      <div data-vc="pagefoot"></div>
    </div>
  </main>

  <aside class="vc-rail" data-noprint="1"></aside>
</div>

<div id="vc-footer"></div>
<script src="{up}assets/footer.js"></script>
<script src="{up}assets/docs.js"></script>
{extra}</body>
</html>
"""


def inner_html(tag):
    parts = []
    for c in tag.contents:
        # str() on a Comment drops its delimiters; keep authors' notes intact.
        parts.append('<!--%s-->' % c if isinstance(c, Comment) else str(c))
    return ''.join(parts)


# html.parser lower-cases attribute names. Browsers repair the SVG ones during
# parsing, but keeping the original casing avoids surprising anyone reading the
# source or running it through a stricter tool later.
SVG_ATTRS = ['viewBox', 'preserveAspectRatio', 'patternUnits', 'gradientUnits',
             'gradientTransform', 'markerWidth', 'markerHeight', 'refX', 'refY',
             'clipPathUnits', 'spreadMethod', 'textLength', 'startOffset']


def restore_svg_case(s):
    for a in SVG_ATTRS:
        s = re.sub(r'\b' + a.lower() + r'=', a + '=', s)
    return s


def is_blank(node):
    if isinstance(node, NavigableString):
        return not node.strip()
    if isinstance(node, Tag):
        if node.name in ('img', 'svg', 'br', 'hr', 'input'):
            return False
        return not node.get_text(strip=True) and not node.find(['img', 'svg'])
    return True


def drop_empty_ancestors(node):
    """After lifting the h1 out, tidy the wrappers it left behind."""
    parent = node.parent
    node.decompose()
    while parent is not None and parent.name in ('div', 'span', 'header', 'section'):
        if any(not is_blank(c) for c in parent.contents):
            break
        nxt = parent.parent
        parent.decompose()
        parent = nxt


def migrate(path):
    rel = os.path.relpath(path, ROOT)
    depth = rel.count(os.sep)
    up = '../' * depth
    src = open(path, encoding='utf-8').read()
    soup = BeautifulSoup(src, 'html.parser')

    title = soup.title.get_text(strip=True) if soup.title else ''
    metas = []
    for name in ('description', 'keywords', 'robots', 'author'):
        m = soup.find('meta', attrs={'name': name})
        if m and m.get('content'):
            metas.append('  <meta name="%s" content="%s">' % (name, html.escape(m['content'], quote=True)))
    for prop in ('og:title', 'og:description', 'og:image', 'og:url', 'og:type'):
        m = soup.find('meta', attrs={'property': prop})
        if m and m.get('content'):
            metas.append('  <meta property="%s" content="%s">' % (prop, html.escape(m['content'], quote=True)))
    canon = soup.find('link', rel='canonical')
    if canon and canon.get('href'):
        metas.append('  <link rel="canonical" href="%s">' % html.escape(canon['href'], quote=True))
    updated = DATES.get(rel.replace(os.sep, '/'))
    if updated:
        metas.append('  <meta name="vc-updated" content="%s">' % updated)
    meta = ('\n'.join(metas) + '\n') if metas else ''

    body = soup.body
    main = body.find('main')
    if main is None:
        raise SystemExit('no <main> in ' + rel)

    # Content that lives outside <main> and is worth keeping: the product
    # notice banners, and API Studio's Ko-fi button.
    banner = ''
    for div in body.find_all('div', recursive=True):
        if div.find_parent('main'):
            continue
        cls = ' '.join(div.get('class') or [])
        if 'border-b' in cls and 'text-center' in cls and div.get_text(strip=True):
            banner = '\n' + str(div) + '\n'
            break
    extra = ''
    for a in body.find_all('a'):
        if a.find_parent('main'):
            continue
        cls = ' '.join(a.get('class') or [])
        if cls.startswith('fixed bottom-'):
            a['data-noprint'] = '1'
            extra = str(a) + '\n'
            break

    # --- strip the old in-page shell from the content -----------------------
    for aside in main.find_all('aside'):          # in-page TOC / mobile nav
        aside.decompose()
    for a in main.find_all('a'):                  # "← Product Overview" back links
        txt = a.get_text(strip=True)
        if txt.startswith('←') and len(txt) < 60:
            a.extract()
    for s in main.find_all(['script', 'style']):
        s.decompose()

    # --- lift the h1, its icon and the lede ---------------------------------
    h1 = main.find('h1')
    if h1 is None:
        raise SystemExit('no <h1> in ' + rel)
    h1_html = inner_html(h1).strip()
    parent = h1.parent
    if parent is not main and parent.name in ('div', 'header'):
        # API Studio's hero puts the product icon beside the h1 in a flex row.
        icons = [c for c in parent.find_all(['img', 'svg'], recursive=False)]
        if icons and all(is_blank(c) or c is h1 or c in icons for c in parent.contents):
            h1_html = ''.join(str(i) for i in icons) + h1_html
            for i in icons:
                i.extract()

    chip = ''
    prev = h1.find_previous_sibling()
    if prev is not None and 'page-icon-chip' in ' '.join(prev.get('class') or []):
        chip = '      ' + str(prev) + '\n'
        prev.decompose()

    # The lede is the first paragraph after the h1 — usually its sibling, but
    # API Studio wraps the h1 in a hero row, so search forward in document
    # order and stop at the first real section heading.
    lede = ''
    nxt = h1.find_next(['p', 'h2', 'h3', 'table', 'ul', 'ol'])
    if nxt is not None and nxt.name == 'p' and nxt.find_parent('main') is main:
        cls = ' '.join(nxt.get('class') or [])
        text = nxt.get_text(strip=True)
        looks_like_lede = any(k in cls for k in ('text-muted', 'text-lg', 'text-gray-600')) or not cls
        if looks_like_lede and 0 < len(text) < 600:
            lede = '      <p class="vc-lede">%s</p>\n' % inner_html(nxt).strip()
            drop_empty_ancestors(nxt)

    drop_empty_ancestors(h1)

    content = inner_html(main).strip('\n')
    content = re.sub(r'^[ \t]*\n', '', content)
    content = re.sub(r'\n{3,}', '\n\n', content).rstrip()

    out = restore_svg_case(
        HEAD.format(title=html.escape(title), meta=meta, up=up, banner=banner,
                    chip=chip, h1=h1_html, lede=lede, content=content, extra=extra))
    if not CHECK:
        open(path, 'w', encoding='utf-8').write(out)
    return rel, len(content)


def main():
    files = [f for f in sorted(glob.glob(os.path.join(ROOT, '*', 'docs', '*.html')))
             if os.path.basename(f) != 'print.html']  # generated, not a doc page
    total = 0
    for f in files:
        rel, n = migrate(f)
        total += n
    print(('checked ' if CHECK else 'migrated ') + str(len(files)) + ' doc pages, '
          + str(total) + ' bytes of content preserved')


if __name__ == '__main__':
    main()
