#!/usr/bin/env python3
"""Check that every local href/src on the site points at a file that exists.

External links, mailto:, tel: and in-page anchors are skipped — this is about
catching a path that broke during the redesign, not about pinging the web.

    python3 tools/check_links.py
"""
import os, re, glob, urllib.parse
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ('http://', 'https://', 'mailto:', 'tel:', 'data:', 'javascript:', '#')

bad = 0
checked = 0
for path in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    # _template.html carries the paths it will have once copied into posts/.
    if '/.git/' in path or '/_build/' in path or os.path.basename(path).startswith('_'):
        continue
    rel = os.path.relpath(path, ROOT)
    soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
    refs = []
    for tag, attr in (('a', 'href'), ('link', 'href'), ('script', 'src'), ('img', 'src'), ('source', 'src')):
        for el in soup.find_all(tag):
            v = el.get(attr)
            if v:
                refs.append(v)
    for ref in refs:
        if ref.startswith(SKIP) or not ref.strip():
            continue
        target = urllib.parse.unquote(ref.split('#')[0].split('?')[0])
        if not target:
            continue
        base = ROOT if target.startswith('/') else os.path.dirname(path)
        full = os.path.normpath(os.path.join(base, target.lstrip('/')))
        checked += 1
        if os.path.isdir(full):
            if os.path.exists(os.path.join(full, 'index.html')):
                continue
            print('%s -> %s (directory has no index.html)' % (rel, ref))
            bad += 1
        elif not os.path.exists(full):
            print('%s -> %s' % (rel, ref))
            bad += 1
print('checked %d local references, %d broken' % (checked, bad))
