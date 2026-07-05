/* Vectored shared footer. Include on any page as:
     <div id="vc-footer"></div>
     <script src="<relative-path>/assets/footer.js"></script>
   Links resolve relative to the site root (parent of /assets/), so the same
   file works at any page depth. Edit here once; every page updates. */
(function () {
  var script = document.currentScript;
  if (!script || !script.src) return;
  var root = new URL('..', script.src).href;
  var mount = document.getElementById('vc-footer');
  if (!mount) return;
  function u(p) { return root + p; }
  var year = new Date().getFullYear();
  mount.outerHTML =
    '<footer class="border-t border-border px-4 sm:px-6 lg:px-8 py-12">' +
      '<div class="max-w-6xl mx-auto">' +
        '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-8 mb-10">' +
          '<div>' +
            '<span class="font-mono font-bold text-lg text-cta block">Vectored</span>' +
            '<p class="text-sm text-muted mt-2">Production-grade tools for Atlassian, VS Code, and the command line.</p>' +
          '</div>' +
          '<div>' +
            '<h4 class="text-sm font-semibold mb-3">Products</h4>' +
            '<ul class="space-y-2 text-sm text-muted">' +
              '<li><a href="' + u('macrotoolkit/') + '" class="hover:text-text transition-colors duration-200 cursor-pointer">Macro Toolkit</a></li>' +
              '<li><a href="' + u('forms/') + '" class="hover:text-text transition-colors duration-200 cursor-pointer">Forms &amp; Frontdoor</a></li>' +
              '<li><a href="' + u('apistudio/') + '" class="hover:text-text transition-colors duration-200 cursor-pointer">API Studio</a></li>' +
            '</ul>' +
          '</div>' +
          '<div>' +
            '<h4 class="text-sm font-semibold mb-3">Get the apps</h4>' +
            '<ul class="space-y-2 text-sm text-muted">' +
              '<li><a href="https://marketplace.atlassian.com/apps/3972300183" target="_blank" rel="noopener" class="hover:text-text transition-colors duration-200 cursor-pointer">Macro Toolkit on Marketplace</a></li>' +
              '<li><a href="https://marketplace.atlassian.com/apps/2466520058/forms-frontdoor-by-vectored?hosting=cloud&amp;tab=overview" target="_blank" rel="noopener" class="hover:text-text transition-colors duration-200 cursor-pointer">Forms &amp; Frontdoor on Marketplace</a></li>' +
              '<li><a href="https://github.com/openAPI-Studio" target="_blank" rel="noopener" class="hover:text-text transition-colors duration-200 cursor-pointer">API Studio on GitHub</a></li>' +
            '</ul>' +
          '</div>' +
          '<div>' +
            '<h4 class="text-sm font-semibold mb-3">Company</h4>' +
            '<ul class="space-y-2 text-sm text-muted">' +
              '<li><a href="' + u('macrotoolkit/support.html') + '" class="hover:text-text transition-colors duration-200 cursor-pointer">Support</a></li>' +
              '<li><a href="' + u('macrotoolkit/security.html') + '" class="hover:text-text transition-colors duration-200 cursor-pointer">Security</a></li>' +
              '<li><a href="' + u('macrotoolkit/privacy.html') + '" class="hover:text-text transition-colors duration-200 cursor-pointer">Privacy</a></li>' +
            '</ul>' +
          '</div>' +
        '</div>' +
        '<p class="text-center text-xs text-muted border-t border-border pt-6">&copy; ' + year + ' Vectored. Built for developers.</p>' +
      '</div>' +
    '</footer>';
})();
