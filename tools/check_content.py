#!/usr/bin/env python3
"""Compare the visible text of two copies of the site, page by page.

Used to prove the redesign migration did not drop content: run it with the
pre-migration tree as OLD and the migrated tree as NEW. The comparison is a
word multiset difference, so re-flowed markup (a heading that moved out of
<main>, a paragraph promoted to the lede) does not register — only words that
genuinely disappeared do.

  python3 tools/check_content.py OLD NEW
"""
import sys, os, re, glob, collections
from bs4 import BeautifulSoup

OLD, NEW = sys.argv[1], sys.argv[2]

# Text that lived only in the old per-page shell and is now rendered once by
# the shared header/sidebar/footer.
SHELL = set('''overview docs support search all macros home ← previous next
getting started documentation'''.split())


def words(path, whole_body):
    soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
    for t in soup(['script', 'style']):
        t.decompose()
    node = soup.body if whole_body else soup.find('main')
    if node is None:
        return collections.Counter()
    if not whole_body:
        for aside in node.find_all('aside'):
            aside.decompose()
    text = re.sub(r'\s+', ' ', node.get_text(' ')).lower()
    return collections.Counter(w for w in re.findall(r"[a-z0-9][a-z0-9'./_-]*", text) if w not in SHELL)


bad = 0
for old in sorted(glob.glob(os.path.join(OLD, '*', 'docs', '*.html'))):
    rel = os.path.relpath(old, OLD)
    new = os.path.join(NEW, rel)
    if not os.path.exists(new):
        print('MISSING', rel)
        bad += 1
        continue
    lost = words(old, False) - words(new, True)
    if lost:
        print(rel, '->', ', '.join('%s x%d' % (w, n) for w, n in lost.most_common(8)))
        bad += 1
print('pages with lost words:', bad)
