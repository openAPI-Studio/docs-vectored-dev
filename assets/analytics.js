/* Vectored docs analytics — Cloudflare Web Analytics.

   Loaded by footer.js, which every page already includes, so there is no
   per-page script tag to keep in sync across the ~170 HTML files.

   Cloudflare Web Analytics is cookieless: it sets no cookies, writes nothing
   to localStorage, and builds no cross-site profile. That is why this needs no
   consent banner and why it does not contradict the no-tracking promises the
   apps make in privacy.html. If this is ever swapped for something that does
   set cookies, privacy.html section 5 has to change with it.

   TOKEN is the site tag from the Cloudflare dashboard (Web Analytics > your
   site > Manage site). It is a public identifier, not a secret — it ships in
   the page source of every site using this product, so it lives in the repo
   rather than in a build-time injection. An empty TOKEN disables the beacon
   entirely, which is what keeps this safe to commit before the site is set up
   in Cloudflare.

   The beacon is skipped on localhost and file:// so local editing does not
   land in production stats. */
(function () {
  var TOKEN = '1345e3082dad4e24bcfce29ce97fa5e2';

  if (!TOKEN) return;

  var host = location.hostname;
  var isLocal = location.protocol === 'file:' ||
                host === 'localhost' ||
                host === '127.0.0.1' ||
                host === '[::1]' ||
                host === '' ||
                /\.local$/.test(host);
  if (isLocal) return;

  // Respect an explicit opt-out. Not required for a cookieless beacon, but the
  // apps take a hard line on tracking and the docs should not be the exception.
  if (navigator.doNotTrack === '1' || window.doNotTrack === '1' || navigator.globalPrivacyControl) return;

  // type="module" matches the snippet Cloudflare currently hands out. Modules
  // defer by default, so there is no separate defer flag to set here.
  var s = document.createElement('script');
  s.type = 'module';
  s.src = 'https://static.cloudflareinsights.com/beacon.min.js';
  s.setAttribute('data-cf-beacon', JSON.stringify({ token: TOKEN }));
  document.head.appendChild(s);
})();
