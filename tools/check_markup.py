#!/usr/bin/env python3
"""Check that every page's <body> closes what it opens.

Cheap insurance against a bad edit: a regex that removes an element but stops
at the wrong closing tag leaves orphaned content and unbalanced markup, which
browsers quietly paper over. This does not.

    python3 tools/check_markup.py
"""
import os, re, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta',
        'source', 'track', 'wbr',
        # SVG leaf elements, which the pages write without a closing tag
        'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'use', 'stop',
        'animate', 'animatetransform', 'ellipse', 'fegaussianblur'}

bad = 0
pages = 0
for path in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    if '/.git/' in path:
        continue
    rel = os.path.relpath(path, ROOT)
    s = open(path, encoding='utf-8').read()
    if '<body' not in s:
        continue
    pages += 1
    body = s.split('<body', 1)[1].split('>', 1)[1].rsplit('</body>', 1)[0]
    body = re.sub(r'<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->', '', body, flags=re.S)

    stack, problem = [], None
    for m in re.finditer(r'<(/?)([a-zA-Z][\w-]*)\b[^>]*?(/?)>', body):
        closing, tag, self_close = m.group(1), m.group(2).lower(), m.group(3)
        if tag in VOID or self_close:
            continue
        if closing:
            if stack and stack[-1] == tag:
                stack.pop()
            elif tag in stack:
                while stack and stack.pop() != tag:
                    pass
            else:
                problem = 'stray </%s>' % tag
                break
        else:
            stack.append(tag)
    if not problem and stack:
        problem = 'unclosed ' + ', '.join('<%s>' % t for t in stack[:5])
    if problem:
        print('%s -> %s' % (rel, problem))
        bad += 1

print('checked %d pages, %d with unbalanced markup' % (pages, bad))
sys.exit(1 if bad else 0)
