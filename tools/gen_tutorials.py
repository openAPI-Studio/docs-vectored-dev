#!/usr/bin/env python3
"""Embed the API Studio YouTube tutorials in the docs.

The VIDEOS table is the single source of truth: each video's number, YouTube
id, title, length and the doc pages it belongs on. Running this script

  * rewrites the block between <!-- tutorial:begin --> and <!-- tutorial:end -->
    at the top of every listed page's <article class="vc-doc"> (inserting it
    the first time), and removes it from pages no longer listed;
  * writes apistudio/docs/tutorials.html, the full series index.

Run from the site root, then regenerate the sidebar and llms files:
    python3 tools/gen_tutorials.py && python3 tools/gen_nav.py && \
      python3 tools/gen_llms.py && python3 tools/gen_llms_full.py

Embeds use youtube-nocookie.com with loading="lazy", so a page loads no
YouTube code until the player scrolls into view.
"""
import os, re, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'apistudio', 'docs')
PLAYLIST = 'PLL0Sge2Sie6I'
PLAYLIST_URL = 'https://www.youtube.com/playlist?list=' + PLAYLIST
PLAYLIST_NAME = 'API Studio: Complete Tutorial Series'

# (number, youtube id, short title, length "m:ss", track, [doc pages])
# Order matches the playlist. #44 and #45 were never recorded.
VIDEOS = [
  (1,  'XNi-RNKDfsY', 'What is API Studio?',                      '2:08', 'Getting started', ['index']),
  (2,  'jIcXwzZG-bo', 'Installing API Studio',                    '1:43', 'Getting started', ['installation']),
  (3,  'xubzZvTf85s', 'UI tour and Advanced mode',                '2:32', 'Getting started', ['ui-overview']),
  (4,  'HCVXjV4Z7Y0', 'Send your first request',                  '2:25', 'Getting started', ['quick-start', 'sending-requests', 'params-headers']),
  (5,  '3q6udm3NNfY', 'Request body editors',                     '2:10', 'Requests and responses', ['request-body']),
  (6,  'PZW4fl7_26A', 'Reading responses',                        '2:17', 'Requests and responses', ['response-viewer']),
  (7,  '96ApSjbD-KA', 'Collections and folders',                  '1:52', 'Requests and responses', ['creating-collections', 'folders-organization']),
  (8,  'Jd_u0KxJvqM', 'Tabs and session restore',                 '1:38', 'Requests and responses', ['tabs-sessions']),
  (9,  'mv9CFRbamIU', 'Request history',                          '1:36', 'Requests and responses', ['request-history']),
  (10, '0uEJyH4o3Jk', 'Environments and variables',               '1:49', 'Requests and responses', ['managing-environments', 'variables-interpolation', 'variable-priority']),
  (11, '9mL_Rw8s0go', 'Extract values from responses',            '1:40', 'Testing', ['set-variables']),
  (12, 'v8bwyK8yAPs', 'No-code test rules',                       '1:30', 'Testing', ['gui-test-rules']),
  (13, '9zrXVUJt9Zs', 'Pre-request and test scripts',             '1:41', 'Testing', ['pre-request-scripts', 'test-scripts', 'scripting-api']),
  (14, 'QWMylqxYET4', 'Collection editor and inheritance',        '1:41', 'Testing', ['collection-editor', 'auth-inheritance']),
  (15, '6TI_KnqK77s', 'Running a whole collection',               '1:37', 'Testing', ['collection-runs']),
  (16, 'Ge-O02PHKCY', 'Snapshots and contract tracking',          '1:30', 'Testing', []),
  (17, 'jfPaiBKE5VI', 'Auth basics: Basic, API key, Bearer, Digest', '1:48', 'Auth and security', ['auth-overview', 'basic-auth', 'bearer-token', 'api-key', 'digest-auth']),
  (18, 'bZ-eVX0YI80', 'OAuth 2.0 and AWS SigV4',                  '1:33', 'Auth and security', ['oauth2', 'aws-sigv4']),
  (19, 'tCkA0drpil0', 'The encrypted vault',                      '1:30', 'Auth and security', ['creating-vault', 'managing-secrets']),
  (20, 'ZnY3-ZLMWMg', 'Secret sets and certificates',             '1:34', 'Auth and security', ['secret-sets', 'certificates']),
  (21, '-3Tg5gXn54c', 'Proxies, SSL and cookies',                 '1:43', 'Auth and security', ['proxy']),
  (22, 'xVeIKAtWc8M', 'The GraphQL client',                       '1:42', 'Protocols', ['graphql']),
  (23, 'LoOi_lxRk-Q', 'GraphQL subscriptions',                    '1:32', 'Protocols', ['graphql']),
  (24, 'EnqIogWyyKQ', 'The WebSocket client',                     '1:37', 'Protocols', ['websocket']),
  (25, '7Hse65cBd0k', 'Server-Sent Events',                       '1:40', 'Protocols', ['sse']),
  (26, '_NFkhq4Y2cY', 'The gRPC client',                          '1:44', 'Protocols', ['grpc']),
  (27, 'LQvCU_RAfSc', 'Build a mock server',                      '1:35', 'Mocks, MCP and AI', ['creating-mock-servers', 'mock-routes']),
  (28, 'ouIvzP5KJ34', 'Mock request log and Swagger',             '1:21', 'Mocks, MCP and AI', ['mock-request-log', 'mock-swagger']),
  (29, 'x0BXe2-e_rA', 'Turn a collection into MCP tools',         '2:04', 'Mocks, MCP and AI', ['collection-mcp', 'connecting-ai-clients']),
  (30, 'pzWmbdHQLAE', 'Mock MCP and the management MCP',          '1:51', 'Mocks, MCP and AI', ['mock-mcp', 'management-mcp']),
  (31, 'KDoLaKTzuFQ', 'Code export',                              '1:09', 'Mocks, MCP and AI', ['code-export-languages']),
  (32, 'kTyPAtNKwFQ', 'AI prompts',                               '1:21', 'Mocks, MCP and AI', ['ai-prompts']),
  (33, 'VnOyUQ_c1Bk', 'Import and export',                        '1:24', 'Workflow', ['import-export']),
  (34, 'DMCNvx6jOFo', 'Version control with Git',                 '1:31', 'Workflow', ['version-control']),
  (35, 'WMkTvZIy838', 'Settings and keyboard shortcuts',          '2:08', 'Workflow', ['settings', 'keyboard-shortcuts']),
  (36, '913_UmYC6v4', 'API Studio inside VS Code',                '1:37', 'Workflow', ['ui-overview']),
  (37, 'HPDe1ZjWKMo', 'CLI getting started',                      '1:19', 'The openpost CLI', ['cli-overview']),
  (38, 'xLXY2QDbPWE', 'Run collections from the terminal',        '1:07', 'The openpost CLI', ['cli-run']),
  (39, 'LHwnNe9KuR0', 'Load testing from the CLI',                '1:21', 'The openpost CLI', ['cli-perf']),
  (40, 'MOrajEs4TgM', 'Security scan (openpost scan)',            '1:23', 'The openpost CLI', ['management-mcp']),
  (41, 'CydUsx-WhIU', 'CLI import, environments and vault',       '1:17', 'The openpost CLI', ['cli-import-export', 'cli-vault']),
  (42, 'VoZP8ktAdrI', 'Mock and MCP servers from the CLI',        '1:09', 'The openpost CLI', ['cli-serve']),
  (43, '_y6XyJ_dBuI', 'API tests in CI/CD',                       '1:36', 'The openpost CLI', ['cicd']),
  (46, '_-mu-6TIx7A', 'The agent skill in Cursor, Copilot and Kiro', '1:17', 'AI agents', ['ai-agent-skills']),
  (47, 'M4C5iWpMYOI', 'YAML API tests and reports',               '1:29', 'AI agents', ['cli-api-tests', 'cli-reports']),
  (48, '3gmncmCbEuA', 'Generate API docs from tests',             '1:13', 'AI agents', ['cli-api-tests']),
]

BEGIN, END = '<!-- tutorial:begin -->', '<!-- tutorial:end -->'
BLOCK_RE = re.compile(r'\n?' + re.escape(BEGIN) + r'.*?' + re.escape(END) + r'\n?', re.S)
ARTICLE_RE = re.compile(r'(<article class="vc-doc">\n?)')

PLAY = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M8 5.14v13.72a1 1 0 0 0 1.52.85l10.9-6.86a1 1 0 0 0 0-1.7L9.52 4.29A1 1 0 0 0 8 5.14z"/></svg>')


def e(s):
    return html.escape(s, quote=True)


def watch(v):
    return 'https://www.youtube.com/watch?v=%s&list=%s' % (v[1], PLAYLIST)


def player(v):
    n, vid, title, length = v[0], v[1], v[2], v[3]
    return (
        '<figure class="vc-video">\n'
        '<div class="vc-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0" '
        'title="%s (video)" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; '
        'gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" '
        'allowfullscreen></iframe></div>\n'
        '<figcaption>Video tutorial #%d · %s · %s · <a href="%s" target="_blank" rel="noopener">Watch on YouTube</a></figcaption>\n'
        '</figure>' % (vid, e(title), n, e(title), length, e(watch(v)))
    )


def block(videos):
    inner = '<div class="vc-videos">\n%s\n</div>' % '\n'.join(player(v) for v in videos)
    more = ('<p class="vc-video-more">Part of the <a href="tutorials.html">%s</a>, '
            '%d short videos covering every feature.</p>' % (e(PLAYLIST_NAME), len(VIDEOS)))
    return '%s\n%s\n%s\n%s\n' % (BEGIN, inner, more, END)


def update_pages():
    by_page = {}
    for v in VIDEOS:
        for p in v[5]:
            by_page.setdefault(p, []).append(v)
    changed = []
    for path in sorted(glob.glob(os.path.join(DOCS, '*.html'))):
        slug = os.path.basename(path)[:-5]
        if slug in ('tutorials', 'print'):
            continue
        src = open(path, encoding='utf-8').read()
        out = BLOCK_RE.sub('\n', src, count=1) if BEGIN in src else src
        if slug in by_page:
            if not ARTICLE_RE.search(out):
                raise SystemExit('no <article class="vc-doc"> in ' + path)
            out = ARTICLE_RE.sub(lambda m: m.group(1) + block(by_page[slug]), out, count=1)
        if out != src:
            open(path, 'w', encoding='utf-8').write(out)
            changed.append(slug)
    missing = set(by_page) - {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(DOCS, '*.html'))}
    if missing:
        raise SystemExit('VIDEOS lists pages that do not exist: ' + ', '.join(sorted(missing)))
    return changed


def card(v):
    n, vid, title, length, _, pages = v
    docs = ''
    if pages:
        docs = ' · <a href="%s.html">Read the docs</a>' % pages[0]
    return (
        '<div class="vc-vcard">\n'
        '<a class="vc-vcard-thumb" href="%s" target="_blank" rel="noopener" aria-label="Watch %s on YouTube">'
        '<img src="https://i.ytimg.com/vi/%s/mqdefault.jpg" alt="" loading="lazy" width="320" height="180">'
        '<span class="vc-vcard-play">%s</span><span class="vc-vcard-len">%s</span></a>\n'
        '<p class="vc-vcard-title"><span>#%d</span> <a href="%s" target="_blank" rel="noopener">%s</a></p>\n'
        '<p class="vc-vcard-meta">%s%s</p>\n'
        '</div>' % (e(watch(v)), e(title), vid, PLAY, length, n, e(watch(v)), e(title), length, docs)
    )


PAGE_HEAD = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Video Tutorials — API Studio Docs</title>
  <meta name="description" content="The API Studio: Complete Tutorial Series on YouTube — 46 short videos covering the desktop app, VS Code, the openpost CLI, mocks, MCP and AI agent skills.">
  <meta name="vc-updated" content="16 Nov 2026">
  <link rel="icon" type="image/svg+xml" href="../../favicon.svg">
  <script>(function(){var t=null;try{t=localStorage.getItem('theme')}catch(e){}
    var light=t?t==='light':window.matchMedia('(prefers-color-scheme:light)').matches;
    var d=document.documentElement;d.dataset.theme=light?'light':'dark';
    d.classList.toggle('dark',!light);d.classList.toggle('light',light);})();</script>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="../../assets/tailwind-config.js"></script>
  <link rel="stylesheet" href="../../assets/tokens.css">
</head>
<body>

<div id="vc-header"></div>
<script src="../../assets/nav.js"></script>
<script src="../../assets/header.js"></script>

<div class="vc-shell">
  <aside class="vc-side" data-noprint="1"></aside>

  <main class="vc-main">
    <div class="vc-col">
      <div data-vc="printhead"></div>
      <div data-vc="crumbs"></div>
      <h1 class="vc-h1">Video Tutorials</h1>
      <p class="vc-lede">The API Studio: Complete Tutorial Series on YouTube. Short, focused videos, most under two minutes, from your first request to AI agents that test your API for you.</p>
      <div data-vc="meta"></div>
      <div data-vc="contents"></div>

      <article class="vc-doc">
'''

PAGE_FOOT = '''      </article>

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
'''


def tutorials_page():
    parts = [PAGE_HEAD]
    parts.append(
        '<section id="playlist">\n'
        '<h2>Watch the whole series</h2>\n'
        '<p>Play the series from the start, or pick a topic below. Every video also appears on the doc page it covers. '
        'Open the <a href="%s" target="_blank" rel="noopener">playlist on YouTube</a> to subscribe or watch full screen.</p>\n'
        '<figure class="vc-video">\n'
        '<div class="vc-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/videoseries?list=%s&amp;rel=0" '
        'title="%s (playlist)" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; '
        'picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>\n'
        '<figcaption>%s · %d videos · <a href="%s" target="_blank" rel="noopener">Open on YouTube</a></figcaption>\n'
        '</figure>\n'
        '</section>\n' % (e(PLAYLIST_URL), PLAYLIST, e(PLAYLIST_NAME), e(PLAYLIST_NAME), len(VIDEOS), e(PLAYLIST_URL)))
    tracks = []
    for v in VIDEOS:
        if v[4] not in tracks:
            tracks.append(v[4])
    for t in tracks:
        vids = [v for v in VIDEOS if v[4] == t]
        parts.append('<section>\n<h2>%s</h2>\n<div class="vc-vgrid">\n%s\n</div>\n</section>\n'
                     % (e(t), '\n'.join(card(v) for v in vids)))
    parts.append(PAGE_FOOT)
    open(os.path.join(DOCS, 'tutorials.html'), 'w', encoding='utf-8').write(''.join(parts))


if __name__ == '__main__':
    changed = update_pages()
    tutorials_page()
    print('updated %d pages: %s' % (len(changed), ', '.join(changed)))
    print('wrote apistudio/docs/tutorials.html')
