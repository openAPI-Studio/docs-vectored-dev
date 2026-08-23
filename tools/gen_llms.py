#!/usr/bin/env python3
"""Generate llms.txt from the nav registry.

llms.txt is a convention for handing an LLM a clean map of a documentation
site instead of making it scrape rendered HTML. Ours is generated rather than
hand-maintained: the product registry in assets/nav.js already knows every doc
page and its group, so this reads that and never drifts from the sidebar.

Link text comes from the registry label. Descriptions come from each page's
meta description, which is written for humans and properly cased, rather than
the registry's lowercased search blob.

Root-level pages (privacy, security, support, the blog) are not in the registry
because they belong to no product, so they are listed explicitly below.

Run after adding pages, alongside tools/gen_nav.py:
    python3 tools/gen_nav.py && python3 tools/gen_llms.py
"""
import re, os, json, glob, subprocess, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://docs.vectored.dev/'

SUMMARY = (
    "Documentation for Vectored's developer tools. API Studio is an offline API "
    "client for VS Code and the command line covering REST, GraphQL, WebSocket "
    "and gRPC, with mock servers, MCP servers, CI/CD integration and git-based "
    "collections. Lens captures and documents screen recordings locally. "
    "TimeSheets, Macro Toolkit, Forms & Frontdoor and Recognition Hub are "
    "Atlassian Confluence apps. Everything here is offline-first: the apps "
    "collect no usage data and require no account."
)

# Pages outside the product registry, in the order they should appear.
ROOT_PAGES = [
    ('index.html',    'Vectored Docs Home',      'Index of every product and its documentation.'),
    ('support.html',  'Support',                 'How to get help, report a bug, or request a feature.'),
    ('security.html', 'Security',                'Security posture and vulnerability reporting.'),
    ('privacy.html',  'Privacy Policy',          'What the apps collect (nothing) and what this website measures.'),
    ('feedback.html', 'Feedback',                'Send feedback on any Vectored product.'),
    ('blog/',         'Blog',                    'Release notes and product announcements.'),
]



# Pages that live directly under a product directory rather than in its docs
# folder — privacy, security, support, terms. Discovered rather than listed so
# a new one is picked up without editing this file.
# Mirrors the sitemap's exclusions: the directory index is linked separately,
# and landing-old.html is a superseded page kept only for reference.
SIDECAR_SKIP = {'index.html', 'landing-old.html'}


def sidecars(pdir):
    found = []
    for path in sorted(glob.glob(os.path.join(ROOT, pdir, '*.html'))):
        name = os.path.basename(path)
        if name in SIDECAR_SKIP:
            continue
        title = ''
        src = open(path, encoding='utf-8').read()
        m = re.search(r'<title>(.*?)</title>', src, re.S)
        if m:
            # Titles read "Privacy Policy — Lens"; keep the leading part.
            title = html.unescape(re.sub(r'\s+', ' ', m.group(1))).split('—')[0].strip()
        found.append((f'{pdir}/{name}', title or name))
    return found


def read_products():
    """Evaluate assets/nav.js in Node and return window.VC_PRODUCTS as data.

    Parsing the registry with a regex would break the first time the file is
    reformatted, so let the actual JS engine do it.
    """
    script = (
        "global.window={};"
        f"require({json.dumps(os.path.join(ROOT, 'assets', 'nav.js'))});"
        "process.stdout.write(JSON.stringify(window.VC_PRODUCTS));"
    )
    out = subprocess.run(['node', '-e', script], capture_output=True, text=True)
    if out.returncode:
        raise SystemExit('node failed reading nav.js:\n' + out.stderr)
    return json.loads(out.stdout)


def description(rel):
    """Meta description for a page, or '' when the file has none."""
    path = os.path.join(ROOT, rel)
    if rel.endswith('/'):
        path = os.path.join(path, 'index.html')
    if not os.path.isfile(path):
        return ''
    src = open(path, encoding='utf-8').read()
    m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', src)
    if not m:
        return ''
    # Collapse whitespace so a wrapped attribute becomes one line.
    return re.sub(r'\s+', ' ', html.unescape(m.group(1))).strip()


def line(url_rel, label, desc):
    entry = f'- [{label}]({BASE}{url_rel})'
    return f'{entry}: {desc}' if desc else entry


def main():
    products = read_products()
    out = ['# Vectored Docs', '', f'> {SUMMARY}', '']

    for p in products:
        docs_dir = f"{p['dir']}/docs/"
        out.append(f"## {p['label']}")
        out.append('')
        # Product landing page sits above its documentation.
        landing_desc = description(f"{p['dir']}/")
        out.append(line(f"{p['dir']}/", f"{p['label']} — Overview",
                        landing_desc or p.get('blurb', '')))
        for group in p['groups']:
            for item in group['items']:
                rel = docs_dir + item['h']
                # "Overview — Overview" reads badly; drop the redundant prefix.
                label = item['l'] if group['title'] == item['l'] else f"{group['title']} — {item['l']}"
                out.append(line(rel, label, description(rel)))
        for rel, title in sidecars(p['dir']):
            out.append(line(rel, f"{p['label']} — {title}", description(rel)))
        out.append('')

    out.append('## About')
    out.append('')
    for rel, label, fallback in ROOT_PAGES:
        out.append(line(rel, label, description(rel) or fallback))
    for path in sorted(glob.glob(os.path.join(ROOT, 'blog', 'posts', '*.html'))):
        rel = os.path.relpath(path, ROOT)
        src = open(path, encoding='utf-8').read()
        m = re.search(r'<title>(.*?)</title>', src, re.S)
        title = html.unescape(re.sub(r'\s+', ' ', m.group(1))).split('—')[0].strip() if m else rel
        out.append(line(rel, f'Blog — {title}', description(rel)))
    out.append('')

    text = '\n'.join(out)
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write(text)

    links = sum(1 for l in out if l.startswith('- ['))
    print(f'wrote llms.txt — {links} links, {len(text)} bytes')
    missing = [l for l in out if l.startswith('- [') and ': ' not in l]
    if missing:
        print(f'  {len(missing)} links have no description:')
        for m in missing:
            print('   ', m)


if __name__ == '__main__':
    main()
