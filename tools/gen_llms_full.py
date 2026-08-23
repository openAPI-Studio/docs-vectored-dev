#!/usr/bin/env python3
"""Generate llms-full.txt — every documentation page as one markdown file.

Companion to gen_llms.py. Where llms.txt is an index an agent follows, this is
the whole corpus in a single fetch, which is what a model wants when it needs
the actual content rather than a map of it.

Page order follows llms.txt, which follows the nav registry, so the file reads
in the same order as the sidebar.

Deliberately stdlib-only. Some older scripts in this directory import bs4,
which is only present on /usr/bin/python3 on macOS and not on a Homebrew or
pyenv interpreter — that makes them fail depending on which python3 you happen
to invoke. The markup here is templated and consistent enough that html.parser
handles it, so this runs anywhere.
"""
import re, os, json, glob, html, subprocess
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://docs.vectored.dev/'

# Dropped entirely, children included. svg carries decorative icons only.
SKIP_TREE = {'script', 'style', 'svg', 'nav', 'noscript', 'button', 'select'}
BLOCK = {'p', 'div', 'section', 'article', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
         'ul', 'ol', 'li', 'table', 'tr', 'pre', 'figure', 'figcaption', 'header'}
HEADING = {'h1': '#', 'h2': '##', 'h3': '###', 'h4': '####', 'h5': '#####', 'h6': '######'}


class ToMarkdown(HTMLParser):
    def __init__(self, page_url, heading_offset=0):
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        # Page bodies nest under "# Product" and "## Page Title", so their own
        # h2s have to start at ### or the hierarchy collapses.
        self.heading_offset = heading_offset
        self.out = []
        self.skip_depth = 0
        self.pre_depth = 0
        self.list_stack = []      # 'ul' or ['ol', counter]
        self.row = None           # cells of the table row being built
        self.cell = None          # text of the cell being built
        self.table = None         # rows collected for the current table
        self.in_head_row = False
        self.pending_link = None

    # --- helpers -----------------------------------------------------------
    def emit(self, s):
        if self.cell is not None:
            self.cell.append(s)
        else:
            self.out.append(s)

    def nl(self, n=1):
        if self.cell is not None:
            return
        while self.out and self.out[-1] == '\n' and n > 0:
            # Collapse rather than stack blank lines.
            if self.out[-2:] == ['\n', '\n']:
                break
            break
        self.out.append('\n' * n)

    def absolute(self, href):
        if not href or href.startswith(('http://', 'https://', 'mailto:', '#')):
            return href
        base = self.page_url.rsplit('/', 1)[0] + '/'
        while href.startswith('../'):
            href = href[3:]
            base = base.rstrip('/').rsplit('/', 1)[0] + '/'
        return base + href.lstrip('./')

    # --- parser hooks ------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.skip_depth or tag in SKIP_TREE:
            if tag in SKIP_TREE:
                self.skip_depth += 1
            return

        if tag == 'br':
            self.emit('  \n'); return
        if tag == 'img':
            # An empty alt marks a decorative image; in a text corpus that is
            # pure noise, so only images that describe themselves survive.
            alt = a.get('alt', '').strip()
            src = self.absolute(a.get('src', ''))
            if src and alt:
                self.emit(f'![{alt}]({src})')
            return
        if tag == 'a':
            self.pending_link = self.absolute(a.get('href', ''))
            self.emit('[')
            return
        if tag in ('strong', 'b'):
            self.emit('**'); return
        if tag in ('em', 'i'):
            self.emit('*'); return
        if tag == 'kbd':
            self.emit('`'); return
        if tag == 'code' and not self.pre_depth:
            self.emit('`'); return

        if tag == 'pre':
            self.pre_depth += 1
            self.nl(2); self.out.append('```\n'); return

        if tag == 'table':
            self.table = []; return
        if tag == 'thead':
            self.in_head_row = True; return
        if tag == 'tr' and self.table is not None:
            self.row = []; return
        if tag in ('td', 'th') and self.row is not None:
            self.cell = []; return

        if tag in ('ul', 'ol'):
            self.list_stack.append([tag, 0]); self.nl(2); return
        if tag == 'li':
            if self.list_stack:
                kind = self.list_stack[-1]
                indent = '  ' * (len(self.list_stack) - 1)
                if kind[0] == 'ol':
                    kind[1] += 1
                    self.nl(); self.emit(f'{indent}{kind[1]}. ')
                else:
                    self.nl(); self.emit(f'{indent}- ')
            return

        if tag in HEADING:
            level = min(6, len(HEADING[tag]) + self.heading_offset)
            self.nl(2); self.emit('#' * level + ' '); return

        # The docs render checklist bullets as a flex div wrapping an icon and
        # a span. The icon is skipped, so turn the wrapper into a real bullet.
        if tag == 'div' and 'flex gap-2 items-start' in a.get('class', ''):
            self.nl(); self.emit('- '); return

        if tag in BLOCK:
            self.nl(2)

    def handle_endtag(self, tag):
        if tag in SKIP_TREE:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return

        if tag == 'a' and self.pending_link is not None:
            self.emit(f']({self.pending_link})' if self.pending_link else ']')
            self.pending_link = None
            return
        if tag in ('strong', 'b'):
            self.emit('**'); return
        if tag in ('em', 'i'):
            self.emit('*'); return
        if tag == 'kbd':
            self.emit('`'); return
        if tag == 'code' and not self.pre_depth:
            self.emit('`'); return

        if tag == 'pre':
            self.pre_depth = max(0, self.pre_depth - 1)
            if not self.out[-1].endswith('\n'):
                self.out.append('\n')
            self.out.append('```'); self.nl(2); return

        if tag in ('td', 'th') and self.cell is not None:
            text = re.sub(r'\s+', ' ', ''.join(self.cell)).strip().replace('|', r'\|')
            self.row.append(text); self.cell = None; return
        if tag == 'tr' and self.row is not None:
            self.table.append((self.in_head_row, self.row)); self.row = None; return
        if tag == 'thead':
            self.in_head_row = False; return
        if tag == 'table' and self.table is not None:
            self.flush_table(); self.table = None; return

        if tag in ('ul', 'ol'):
            if self.list_stack:
                self.list_stack.pop()
            self.nl(2); return
        if tag in HEADING or tag in BLOCK:
            self.nl(2)

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.pre_depth:
            self.out.append(data)
            return
        text = re.sub(r'\s+', ' ', data)
        if not text.strip():
            # Keep a single separating space between inline elements.
            if text == ' ' and self.out and not self.out[-1].endswith((' ', '\n')):
                self.emit(' ')
            return
        self.emit(text)

    def flush_table(self):
        rows = [r for _, r in self.table if r]
        if not rows:
            return
        head = next((r for h, r in self.table if h and r), None)
        body = [r for h, r in self.table if not h and r]
        if head is None:
            head, body = rows[0], rows[1:]
        width = max(len(r) for r in rows)
        pad = lambda r: r + [''] * (width - len(r))
        self.nl(2)
        self.out.append('| ' + ' | '.join(pad(head)) + ' |\n')
        self.out.append('|' + '|'.join([' --- '] * width) + '|\n')
        for r in body:
            self.out.append('| ' + ' | '.join(pad(r)) + ' |\n')
        self.nl(2)

    def markdown(self):
        text = ''.join(self.out)
        text = re.sub(r'[ \t]+\n', '\n', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'\n +([-*] )', r'\n\1', text)
        return text.strip()


def page_markdown(rel):
    """Title, lede and body of one page, as markdown."""
    path = os.path.join(ROOT, rel + 'index.html' if rel.endswith('/') else rel)
    src = open(path, encoding='utf-8').read()

    m = re.search(r'<h1[^>]*class="vc-h1"[^>]*>(.*?)</h1>', src, re.S)
    if not m:
        m = re.search(r'<h1[^>]*>(.*?)</h1>', src, re.S)
    title = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else rel

    lede = ''
    m = re.search(r'<p[^>]*class="vc-lede"[^>]*>(.*?)</p>', src, re.S)
    if m:
        p = ToMarkdown(BASE + rel); p.feed(m.group(1)); lede = p.markdown()

    m = re.search(r'<article[^>]*class="vc-doc"[^>]*>(.*?)</article>', src, re.S)
    if not m:
        m = re.search(r'<main[^>]*>(.*?)</main>', src, re.S)
    raw = m.group(1) if m else ''
    if not raw:
        # A few landing pages use neither wrapper; fall back to the body with
        # the chrome removed.
        m = re.search(r'<body[^>]*>(.*?)</body>', src, re.S)
        raw = m.group(1) if m else ''
        for chrome in ('header', 'footer', 'aside'):
            raw = re.sub(rf'<{chrome}\b.*?</{chrome}>', '', raw, flags=re.S)
    body = ''
    if raw:
        p = ToMarkdown(BASE + rel, heading_offset=1); p.feed(raw); body = p.markdown()
    return title, lede, body


def main():
    # Reuse llms.txt for ordering so the two files never disagree.
    index = open(os.path.join(ROOT, 'llms.txt'), encoding='utf-8').read()
    order, section_of = [], {}
    section = ''
    for ln in index.splitlines():
        if ln.startswith('## '):
            section = ln[3:].strip()
        m = re.match(r'^- \[[^\]]+\]\(' + re.escape(BASE) + r'([^)]*)\)', ln)
        if m:
            order.append(m.group(1)); section_of[m.group(1)] = section

    parts = ['# Vectored Docs — full text',
             '',
             '> Every documentation page on docs.vectored.dev, concatenated as markdown '
             'and ordered as the site navigation orders it. Generated from the HTML by '
             'tools/gen_llms_full.py; the index-only version is at '
             'https://docs.vectored.dev/llms.txt',
             '']

    current, skipped = None, []
    for rel in order:
        try:
            title, lede, body = page_markdown(rel)
        except FileNotFoundError:
            skipped.append(rel); continue
        if not body.strip():
            skipped.append(rel); continue
        sec = section_of.get(rel, '')
        if sec != current:
            parts += ['', f'# {sec}', '']
            current = sec
        parts += ['', f'## {title}', '', f'Source: {BASE}{rel}', '']
        if lede:
            parts += [lede, '']
        parts += [body, '']

    text = re.sub(r'\n{3,}', '\n\n', '\n'.join(parts)).strip() + '\n'
    open(os.path.join(ROOT, 'llms-full.txt'), 'w', encoding='utf-8').write(text)
    print(f'wrote llms-full.txt — {len(order) - len(skipped)} pages, '
          f'{len(text):,} bytes ({len(text)/1024:.0f} KB)')
    if skipped:
        print(f'  skipped {len(skipped)} with no extractable body:')
        for s in skipped:
            print('   ', s)


if __name__ == '__main__':
    main()
