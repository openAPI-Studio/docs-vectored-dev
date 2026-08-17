#!/usr/bin/env python3
"""Generate assets/nav.js from the doc pages on disk.

Labels come from each page's <title>, search tags from its meta description, so
the registry can be regenerated whenever pages are added or renamed.
"""
import re, os, json, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = '/Users/akshaykg/Documents/tst/open-tools/docs-site'

GROUPS = {
 'apistudio': [
   ('Overview', ['index']),
   ('Getting started', ['installation','quick-start','ui-overview']),
   ('HTTP client', ['sending-requests','request-body','params-headers','response-viewer','request-history','tabs-sessions']),
   ('Protocols', ['graphql','websocket','grpc','sse']),
   ('Collections', ['creating-collections','folders-organization','collection-editor','collection-runs','import-export','collection-schema']),
   ('Environments', ['managing-environments','variables-interpolation','variable-priority']),
   ('Authentication', ['auth-overview','basic-auth','bearer-token','api-key','oauth2','aws-sigv4','digest-auth','auth-inheritance']),
   ('Testing', ['gui-test-rules','pre-request-scripts','test-scripts','scripting-api','set-variables']),
   ('Mock servers', ['creating-mock-servers','mock-routes','mock-request-log','mock-swagger']),
   ('MCP servers', ['collection-mcp','mock-mcp','management-mcp','connecting-ai-clients']),
   ('Secret vault', ['creating-vault','managing-secrets','secret-sets','certificates']),
   ('CLI', ['cli-overview','cli-run','cli-import-export','cli-vault','cli-serve']),
   ('Code export', ['code-export-languages','ai-prompts']),
   ('Settings & data', ['settings','proxy','data-storage','keyboard-shortcuts','license','support-us']),
 ],
 'timesheets': [
   ('Start here', ['getting-started']),
   ('Time entry', ['logging-time','templates','cost-centers','calendar','summary']),
   ('Approvals', ['approvals','weekly-submission','delegation','approval-history','locking']),
   ('Leave', ['leave','leave-auto-decision','holidays']),
   ('Reports', ['dashboard','reports','scheduled-reports']),
   ('Billing', ['clients','billing-rates','invoices','billing-health']),
   ('Administration', ['project-settings','worklog-sync','email','scheduler','personal-settings','admin-settings','data-requests','permissions','privacy-security']),
 ],
 'macrotoolkit': [
   ('Start here', ['index']),
   ('Lite & Pro', ['mermaid','markdown','poll','mood','graph','typewriter','sticky-note','spoiler','clock','stopwatch']),
   ('Pro edition', ['swagger','drawio','plantuml','excalidraw','carousel','3d-viewer']),
 ],
 'forms': [
   ('Start here', ['getting-started','building-forms','field-types']),
   ('Configure', ['smart-values','validation','multi-section','embedding','styling']),
   ('Manage', ['access-control','collaboration','responses','automation','dashboard','free-vs-pro']),
 ],
 'lens': [
   ('Start here', ['getting-started']),
   ('Capture', ['capturing','recording']),
   ('Organise', ['projects','timeline']),
   ('Configure', ['settings','shortcuts']),
   ('AI', ['ai']),
   ('Help', ['troubleshooting']),
 ],
 'rewardhub': [
   ('Start here', ['getting-started']),
   ('Recognize', ['giving-recognition','ai-assist','reactions-comments','sharing-and-macro']),
   ('Configure', ['company-values','email-notifications','moderation']),
 ],
}

# Label overrides where the <title> is not the right sidebar label.
LABELS = {
 ('apistudio','index'): 'Overview',
 ('macrotoolkit','index'): 'All macros',
 ('timesheets','cost-centers'): 'Cost Centres',
 ('timesheets','privacy-security'): 'Privacy & Data Handling',
}

PRODUCTS = [
 dict(key='apistudio', label='API Studio', blurb='Requests, mocks, CLI',
      dir='apistudio', icon='apistudio/assets/icon.svg',
      cta='https://marketplace.visualstudio.com/items?itemName=open-post.open-post',
      ctaLabel='Try free', homeLabel='API Studio Overview'),
 dict(key='timesheets', label='TimeSheets', blurb='Time, leave, approvals',
      dir='timesheets', icon='timesheets/assets/icon-64.png',
      cta='timesheets/docs/getting-started.html', ctaLabel='Get started',
      homeLabel='TimeSheets Overview'),
 dict(key='macrotoolkit', label='Macro Toolkit', blurb='Confluence macros',
      dir='macrotoolkit', icon='macrotoolkit/assets/icon_lite-64.png',
      cta='https://marketplace.atlassian.com/apps/3972300183',
      ctaLabel='Try free', homeLabel='Macro Toolkit Overview'),
 dict(key='forms', label='Forms & Frontdoor', blurb='Forms and automation',
      dir='forms', icon='forms/assets/icon-64.png',
      cta='https://marketplace.atlassian.com/apps/2466520058/forms-frontdoor-by-vectored?hosting=cloud&tab=overview',
      ctaLabel='Try free', homeLabel='Forms & Frontdoor Overview'),
 dict(key='rewardhub', label='Recognition Hub', blurb='Recognition',
      dir='rewardhub', icon='rewardhub/assets/logo-64.png',
      cta='https://marketplace.atlassian.com/apps/564712405',
      ctaLabel='Try free', homeLabel='Recognition Hub Overview'),
 dict(key='lens', label='Lens', blurb='Screenshots, GIF & MP4',
      dir='lens', icon='lens/assets/icon-64.png',
      cta='lens/docs/getting-started.html', ctaLabel='Read the docs',
      homeLabel='Lens Overview'),
]


def page_meta(path):
    s = open(path, encoding='utf-8').read()
    t = re.search(r'<title>(.*?)</title>', s, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    title = html.unescape(' '.join(t.group(1).split())) if t else ''
    # strip the " — Product Docs" suffix
    title = re.split(r'\s+[—|]\s+', title)[0].strip()
    desc = html.unescape(d.group(1)) if d else ''
    return title, desc


def build():
    out = []
    for p in PRODUCTS:
        d = p['dir']
        groups = []
        seen = set()
        for gtitle, slugs in GROUPS[p['key']]:
            items = []
            for slug in slugs:
                fp = os.path.join(ROOT, d, 'docs', slug + '.html')
                if not os.path.exists(fp):
                    raise SystemExit('missing page: ' + fp)
                title, desc = page_meta(fp)
                label = LABELS.get((p['key'], slug), title)
                items.append({'h': slug + '.html', 'l': label,
                              't': (label + ' ' + desc).lower()})
                seen.add(slug)
            groups.append({'title': gtitle, 'items': items})
        actual = {os.path.basename(f)[:-5] for f in glob.glob(os.path.join(ROOT, d, 'docs', '*.html'))}
        actual.discard('print')  # the generated full-guide export, not a doc page
        missing = actual - seen
        if missing:
            raise SystemExit('%s: pages not in any group: %s' % (p['key'], sorted(missing)))
        # Where "<Product> docs" should land. Only two products have a
        # docs/index.html; linking the bare directory for the rest 404s, so
        # fall back to the first page in nav order.
        first = groups[0]['items'][0]['h']
        docs_home = d + '/docs/' if 'index' in seen else d + '/docs/' + first

        out.append({
            'key': p['key'], 'label': p['label'], 'blurb': p['blurb'], 'dir': d,
            'icon': p['icon'], 'cta': p['cta'], 'ctaLabel': p['ctaLabel'],
            'homeLabel': p['homeLabel'], 'docsHome': docs_home,
            'count': len(actual), 'groups': groups,
        })
    return out


data = build()
body = ',\n'.join(
    '  ' + json.dumps(p, ensure_ascii=False, separators=(',', ':')) for p in data)

js = """/* Vectored docs — product registry.

   One source of truth for every product's grouped sidebar navigation, search
   index and switcher metadata. Adding a doc page means editing this file, not
   every sibling page. Regenerate with tools/gen_nav.py after adding pages.

   Shape:
     key        directory name under the site root
     label      display name
     blurb      one-line description shown in the product switcher
     icon       switcher icon, root-relative (64px copies, not the originals)
     cta        header call-to-action target; root-relative when not absolute
     docsHome   where "<Product> docs" links to — the directory when it has an
                index.html, otherwise the first page in nav order
     count      number of doc pages, shown in the switcher
     groups     [{ title, items: [{ h: href, l: label, t: search text }] }]
*/
window.VC_PRODUCTS = [
%s
];

/* Resolve the product a page belongs to from its path. */
window.VC_PRODUCT_FOR = function (path) {
  for (var i = 0; i < window.VC_PRODUCTS.length; i++) {
    var p = window.VC_PRODUCTS[i];
    if (path.indexOf('/' + p.key + '/') !== -1) return p;
  }
  return null;
};

/* Flat page list for a product, in sidebar order — drives prev/next. */
window.VC_PAGES = function (p) {
  var out = [];
  p.groups.forEach(function (g) {
    g.items.forEach(function (it) { out.push(it); });
  });
  return out;
};
""" % body

open(os.path.join(ROOT, 'assets', 'nav.js'), 'w', encoding='utf-8').write(js)
print('wrote assets/nav.js', sum(p['count'] for p in data), 'pages')
for p in data:
    print(' ', p['key'], p['count'], len(p['groups']), 'groups')
