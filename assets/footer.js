/* Vectored shared footer. Include on any page as:
     <div id="vc-footer"></div>
     <script src="<relative-path>/assets/footer.js"></script>
   Links resolve relative to the site root (parent of /assets/), so the same
   file works at any page depth. The footer is full-width and sits outside the
   docs flex row, so unlike the old one it needs no knowledge of the sidebar.
   Edit here once; every page updates. */
(function () {
  var script = document.currentScript;
  if (!script || !script.src) return;
  var root = new URL('..', script.src).href;

  // Analytics rides along here because footer.js is the one script every page
  // loads. Injected before the mount check so a page that somehow lacks the
  // footer div still reports. analytics.js no-ops unless a token is set.
  var a = document.createElement('script');
  a.defer = true;
  a.src = root + 'assets/analytics.js';
  document.head.appendChild(a);

  var mount = document.getElementById('vc-footer');
  if (!mount) return;
  function u(p) { return root + p; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  var year = new Date().getFullYear();

  var MARKETPLACE = 'https://marketplace.atlassian.com/search?query=vectored';
  var GITHUB = 'https://github.com/openAPI-Studio';

  var columns = [
    { title: 'Products', links: [
      ['API Studio', u('apistudio/')],
      ['TimeSheets', u('timesheets/')],
      ['Macro Toolkit', u('macrotoolkit/')],
      ['Forms & Frontdoor', u('forms/')],
      ['Recognition Hub', u('rewardhub/')]
    ]},
    // Doc landing targets come from the registry: only two products have a
    // docs/index.html, and the rest have to point at their first page. The
    // fallback keeps the column populated if nav.js is not on the page.
    { title: 'Documentation', links: (window.VC_PRODUCTS && window.VC_PRODUCTS.length
      ? window.VC_PRODUCTS.map(function (p) { return [p.label + ' docs', u(p.docsHome || p.dir + '/docs/')]; })
      : [
          ['API Studio docs', u('apistudio/docs/')],
          ['TimeSheets docs', u('timesheets/docs/getting-started.html')],
          ['Macro Toolkit docs', u('macrotoolkit/docs/')],
          ['Forms & Frontdoor docs', u('forms/docs/getting-started.html')],
          ['Recognition Hub docs', u('rewardhub/docs/getting-started.html')]
        ])},
    { title: 'Get the apps', links: [
      ['Atlassian Marketplace', MARKETPLACE, 1],
      ['API Studio on GitHub', GITHUB, 1],
      ['VS Code Marketplace', 'https://marketplace.visualstudio.com/items?itemName=open-post.open-post', 1],
      ['Release notes', u('blog/')]
    ]},
    { title: 'Company', links: [
      ['Support', u('support.html')],
      ['Security', u('security.html')],
      ['Privacy', u('privacy.html')],
      ['Blog', u('blog/')],
      ['Contact', u('feedback.html')]
    ]}
  ];

  function link(l) {
    return '<li><a href="' + esc(l[1]) + '"' + (l[2] ? ' target="_blank" rel="noopener"' : '') + '>' + esc(l[0]) + '</a></li>';
  }

  mount.outerHTML =
    '<footer class="vc-ft" data-noprint="1">' +
      '<div class="vc-ft-in">' +
        '<div class="vc-ft-grid">' +
          '<div class="vc-ft-brand">' +
            '<b>Vectored</b>' +
            '<p>Production-grade tools for Atlassian, VS Code, and the command line.</p>' +
            '<div class="vc-ft-social">' +
              '<a href="' + GITHUB + '" target="_blank" rel="noopener" aria-label="GitHub">' +
                '<svg viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>' +
              '</a>' +
            '</div>' +
          '</div>' +
          columns.map(function (c) {
            return '<div><h4>' + esc(c.title) + '</h4><ul>' + c.links.map(link).join('') + '</ul></div>';
          }).join('') +
        '</div>' +
        '<div class="vc-ft-bot">' +
          '<span>&copy; ' + year + ' Vectored. Built for developers.</span>' +
          '<nav>' +
            '<a href="' + u('privacy.html') + '">Privacy</a>' +
            '<a href="' + u('security.html') + '">Security</a>' +
            '<a href="' + u('support.html') + '">Support</a>' +
            '<a href="' + u('feedback.html') + '">Feedback</a>' +
          '</nav>' +
        '</div>' +
      '</div>' +
    '</footer>';
})();
