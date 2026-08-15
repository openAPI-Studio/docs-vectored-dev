#!/usr/bin/env python3
"""Stamp each doc page with the date it was last changed.

The meta row prints "Updated <date>", and a wrong date there is worse than no
date, so the value comes from the file's last commit rather than its mtime.
Run after regenerating pages (for example after timesheets/_build/build.py):

    python3 tools/stamp_updated.py
"""
import os, re, glob, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def git_dates():
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
stamped = 0
for path in sorted(glob.glob(os.path.join(ROOT, '*', 'docs', '*.html'))):
    rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
    if os.path.basename(path) == 'print.html':
        continue
    date = DATES.get(rel)
    if not date:
        continue
    s = open(path, encoding='utf-8').read()
    tag = '  <meta name="vc-updated" content="%s">' % date
    if re.search(r'<meta name="vc-updated"[^>]*>', s):
        s = re.sub(r'[ \t]*<meta name="vc-updated"[^>]*>', tag, s, count=1)
    else:
        s = re.sub(r'([ \t]*<link rel="icon"[^>]*>)', tag + r'\n\1', s, count=1)
    open(path, 'w', encoding='utf-8').write(s)
    stamped += 1
print('stamped %d pages' % stamped)
