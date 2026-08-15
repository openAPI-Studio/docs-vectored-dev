#!/usr/bin/env python3
"""Port the non-documentation pages onto the shared shell.

Landing, support, legal, blog and error pages keep their own layouts — they
only need the redesign's header, footer and tokens. This script:

  * points every page at assets/tailwind-config.js and assets/tokens.css
    instead of its own inline config, light-theme override <style> and theme
    bootstrap;
  * keeps whatever page-specific CSS the <style> block also carried, with the
    hard-coded palette hexes swapped for the tokens;
  * replaces hand-rolled navbars and mobile drawers with the shared header;
  * drops the per-page theme / menu / doc-search wiring now that header.js
    owns all three, while leaving genuine page logic untouched.

Run from the site root:  python3 tools/migrate_pages.py
"""
import os, re, sys, glob, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = ['index.html', '404.html', 'feedback.html', 'feedback-thanks.html',
         'privacy.html', 'security.html', 'support.html',
         'apistudio/index.html', 'apistudio/support.html', 'apistudio/landing-old.html',
         'forms/index.html', 'macrotoolkit/index.html', 'macrotoolkit/support.html',
         'macrotoolkit/privacy.html', 'macrotoolkit/security.html', 'macrotoolkit/terms.html',
         'rewardhub/index.html', 'timesheets/index.html', 'blog/index.html',
         'blog/posts/introducing-forms-and-frontdoor.html',
         'blog/posts/slack-teams-notifications-confluence-forms.html']

# Inline scripts that were nothing but the old per-page shell: the theme
# toggle, the mobile menu, and the doc-search wiring the header now owns.
DEAD_SCRIPTS = {
    '9b5e55fd',  # head theme bootstrap (replaced)
    'b5b35e3e', 'b7366310', 'c27d72ea', 'a2746adb',  # tailwind.config (replaced)
    '21b46893', 'ca078671', 'f6902bd3', 'e7a4f8d1', '7f288a7b',  # theme toggle
    '38949476',  # mobile menu toggle
    '5c81de72', '37bc2bf9', '7dcf1dac', '7eea1455',  # doc-search wiring
    '9af1f1ab',  # timesheets: theme + menu + sidebar + search
    '4edd17ac',  # forms: theme + search
    '6a82617b',  # api studio: sidebar builder + theme + menu + search
}

THEME_FRAG = re.compile(
    r"[ \t]*(?://[^\n]*Theme[^\n]*\n)?[ \t]*var t\s*=\s*localStorage\.getItem\('theme'\);"
    r".*?upd\(\);\s*\}\);\n?", re.S)

# The wiring is sometimes bare and sometimes wrapped in `if(i&&r){ ... }`. The
# wrapped form has to be matched first and taken with its closing brace, or the
# cut leaves an orphan `}` and the whole script stops parsing.
_SEARCH_HEAD = (r"[ \t]*(?://[^\n]*\n[ \t]*)?var (?:i|input)\s*=\s*"
                r"document\.getElementById\('doc-search'\)")
_SEARCH_TAIL = (r"document\.addEventListener\('click',\s*function\(e\)\{"
                r"[^\n]*doc-search[^\n]*\}\);[ \t]*\n?")

SEARCH_FRAG_WRAPPED = re.compile(
    _SEARCH_HEAD + r"[^\n]*\n[ \t]*if\([^)]*\)\s*\{.*?" + _SEARCH_TAIL + r"[ \t]*\}[ \t]*\n?", re.S)
SEARCH_FRAG = re.compile(_SEARCH_HEAD + r".*?" + _SEARCH_TAIL, re.S)

SEARCH_BLOCK = re.compile(
    r"[ \t]*var docs\s*=\s*\[.*?wire\('doc-search','search-results'\);\n?", re.S)

# Palette hexes that used to be repeated in every page's <style> block.
HEX = {
    '#0f172a': 'var(--bg)', '#f8fafc': 'var(--tx)', '#94a3b8': 'var(--muted)',
    '#334155': 'var(--border)', '#1e293b': 'var(--surface)', '#22c55e': 'var(--green)',
    '#16a34a': 'var(--green)', '#171717': 'var(--tx)', '#525252': 'var(--muted)',
    '#e5e5e5': 'var(--border)', '#fafafa': 'var(--bg)', '#f1f5f9': 'var(--surface)',
    '#475569': 'var(--muted)', '#e2e8f0': 'var(--border)', '#0f0f0f': 'var(--bg)',
}

BOOTSTRAP = """<script>(function(){var t=null;try{t=localStorage.getItem('theme')}catch(e){}
    var light=t?t==='light':window.matchMedia('(prefers-color-scheme:light)').matches;
    var d=document.documentElement;d.dataset.theme=light?'light':'dark';
    d.classList.toggle('dark',!light);d.classList.toggle('light',light);})();</script>"""


def split_rules(css):
    """Yield top-level CSS rules, keeping @media blocks whole."""
    rules, depth, buf = [], 0, ''
    for ch in css:
        buf += ch
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                rules.append(buf)
                buf = ''
    if buf.strip():
        rules.append(buf)
    return rules


# The light-theme boilerplate every page repeated: overrides of Tailwind's own
# colour utilities, which the tokens now handle. Anything else under
# html.light is a page's own component styling and must survive.
UTILITY_OVERRIDE = re.compile(
    r'^html\.light\s+(?:body\b|(?:th|td)\b|'
    r'\.(?:bg|text|border|divide|hover|backdrop|placeholder|from|to)[\\:.a-z0-9/-]*)'
    r'\s*[>+~*\s]*$')


def is_boilerplate(sel):
    for part in sel.split(','):
        part = ' '.join(part.split())
        if not part.startswith('html.light'):
            return False
        if not UTILITY_OVERRIDE.match(part):
            return False
    return True


def clean_css(css):
    """Drop the light-theme override boilerplate, keep real page styles."""
    out = []
    for rule in split_rules(css):
        sel = rule.split('{', 1)[0].strip()
        low = sel.lower()
        if 'html.light' in low.replace(' ', '').replace('\n', ''):
            if is_boilerplate(low):
                continue
            # Hexes inside an html.light rule are already the light-theme
            # values; rewriting them to tokens would invert the colours.
            out.append(('keep', rule))
            continue
        if low == 'body' and re.search(r'background:\s*#(0f172a|fafafa|f8fafc)', rule, re.I):
            body_rest = re.sub(r'(background|color|font-family)\s*:[^;}]+;?', '', rule.split('{', 1)[1])
            if not body_rest.strip(' ;}'):
                continue
        if low in ('.font-mono', '.sidebar-link.active'):
            continue
        out.append(('map', rule))

    parts = []
    for mode, rule in out:
        if mode == 'map':
            for hexv, var in HEX.items():
                rule = re.sub(re.escape(hexv), var, rule, flags=re.I)
        parts.append(rule)
    return ''.join(parts).strip()


def rel_root(page):
    return '../' * page.count('/')


def migrate(page):
    path = os.path.join(ROOT, page)
    s = open(path, encoding='utf-8').read()
    up = rel_root(page)

    # <html> carries the theme so the first paint is right.
    s = re.sub(r'<html(?![^>]*data-theme)([^>]*)>', r'<html\1 data-theme="dark">', s, count=1)

    # --- head: shared config + tokens ---------------------------------------
    def script_sub(m):
        attrs, bodyjs = m.group(1), m.group(2)
        if 'src=' in attrs:
            return m.group(0)
        h = hashlib.md5(bodyjs.encode()).hexdigest()[:8]
        if 'tailwind.config' in bodyjs:
            return '<script src="%sassets/tailwind-config.js"></script>' % up
        if h == '9b5e55fd' or re.match(r'\s*var t=localStorage\.getItem\("theme"\)', bodyjs):
            return BOOTSTRAP
        if h in DEAD_SCRIPTS:
            return ''
        cut = THEME_FRAG.sub('', bodyjs)
        cut = SEARCH_FRAG_WRAPPED.sub('', cut)
        cut = SEARCH_BLOCK.sub('', SEARCH_FRAG.sub('', cut))
        if cut != bodyjs:
            hollow = re.sub(r"[\s;]|\(function\(\)\s*\{|\}\)\(\);|'use strict';", '', cut)
            if not hollow:
                return ''
            return '<script' + attrs + '>' + cut + '</script>'
        return m.group(0)

    s = re.sub(r'<script([^>]*)>(.*?)</script>', script_sub, s, flags=re.S)

    def style_sub(m):
        kept = clean_css(m.group(1))
        return ('<style>\n' + kept + '\n  </style>') if kept else ''

    s = re.sub(r'<style[^>]*>(.*?)</style>', style_sub, s, flags=re.S)

    if 'assets/tokens.css' not in s:
        s = s.replace('</head>', '  <link rel="stylesheet" href="%sassets/tokens.css">\n</head>' % up, 1)

    # --- body: shared header and footer --------------------------------------
    # A couple of pages loaded the shared scripts from an absolute path, which
    # only works at the deployed root. Relative keeps them portable.
    s = re.sub(r'(src|href)="/assets/', r'\1="%sassets/' % up, s)

    # The mobile drawer duplicated the old navbar's links; its toggle lived in
    # that navbar, so what is left is unreachable markup.
    s = re.sub(r'\s*<div\b[^>]*id="mobile-menu"[^>]*>.*?</div>\s*</div>\s*', '\n', s, flags=re.S)

    if 'id="vc-header"' not in s:
        # Drop the hand-rolled navbar and its mobile drawer.
        s = re.sub(r'\s*<!--\s*Navbar\s*-->', '', s)
        nav = re.search(r'<nav\b(?![^>]*id="sidebar-nav")[^>]*>.*?</nav>', s, re.S)
        # The version badge lived in that navbar and exists nowhere else; keep
        # it by moving it next to the page's own heading.
        badge = re.search(r'<span[^>]*>(v\d+\.\d+[\w.]*)</span>', nav.group(0)) if nav else None
        s = re.sub(r'<nav\b(?![^>]*id="sidebar-nav")[^>]*>.*?</nav>\s*', '', s, count=1, flags=re.S)
        if badge:
            s = re.sub(r'(</h1>)',
                       r'\1 <span class="font-mono text-xs px-2 py-0.5 rounded bg-cta/10 text-cta '
                       r'border border-cta/20 align-middle">' + badge.group(1) + '</span>',
                       s, count=1)
        s = re.sub(r'\s*<!--\s*Mobile sidebar overlay\s*-->', '', s)
        s = re.sub(r'<div\b[^>]*id="mobile-overlay"[^>]*>.*?</div>\s*', '', s, flags=re.S)
        s = re.sub(r'<aside\b[^>]*id="mobile-sidebar"[^>]*>.*?</aside>\s*', '', s, flags=re.S)
        s = re.sub(r'<div\b[^>]*id="mobile-menu"[^>]*>.*?</div>\s*', '', s, flags=re.S)
        s = re.sub(r'(<body[^>]*>)', r'\1\n\n<div id="vc-header"></div>', s, count=1)

    if 'assets/nav.js' not in s:
        s = s.replace('<div id="vc-header"></div>',
                      '<div id="vc-header"></div>\n<script src="%sassets/nav.js"></script>' % up, 1)
    if 'assets/header.js' not in s:
        s = s.replace('<script src="%sassets/nav.js"></script>' % up,
                      '<script src="%sassets/nav.js"></script>\n<script src="%sassets/header.js"></script>' % (up, up), 1)
    else:
        # header.js must run after nav.js
        s = re.sub(r'(<script src="[^"]*assets/header\.js"></script>)\s*', '', s)
        s = s.replace('<script src="%sassets/nav.js"></script>' % up,
                      '<script src="%sassets/nav.js"></script>\n<script src="%sassets/header.js"></script>' % (up, up), 1)

    if 'id="vc-footer"' not in s:
        s = s.replace('</body>', '<div id="vc-footer"></div>\n<script src="%sassets/footer.js"></script>\n</body>' % up, 1)
    elif 'assets/footer.js' not in s:
        s = s.replace('<div id="vc-footer"></div>',
                      '<div id="vc-footer"></div>\n<script src="%sassets/footer.js"></script>' % up, 1)

    # The old navbar was fixed-position, so pages padded the first row to clear
    # it. The new header is in flow and needs no such allowance.
    s = re.sub(r'(<div class="flex) pt-2\d(")', r'\1\2', s)
    s = re.sub(r'(<main[^>]*?)\bpt-2\d\b', r'\1', s)

    # Old fixed sidebars on landing pages: the shared header carries navigation
    # now, so the duplicate is dead weight.
    s = re.sub(r'<aside\b[^>]*>\s*<nav id="sidebar-nav"[^>]*></nav>\s*</aside>\s*', '', s, flags=re.S)
    s = re.sub(r'(<main[^>]*?)\bmd:ml-64\b', r'\1', s)

    s = re.sub(r'\n{3,}', '\n\n', s)
    open(path, 'w', encoding='utf-8').write(s)
    return page


# Pass page paths to migrate a subset — useful when one page comes back from
# another branch and needs the same treatment as the rest.
targets = [a for a in sys.argv[1:] if not a.startswith('-')] or PAGES
for p in targets:
    migrate(p)
print('migrated %d non-doc pages' % len(targets))
