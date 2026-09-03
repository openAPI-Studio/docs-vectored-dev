/* Vectored store links. Point any install link at the right browser's store:

     <a href="https://chromewebstore.google.com/detail/..." data-store="lens">Install</a>

   The href in the markup is the Chrome Web Store, and it is what a reader gets
   with no JavaScript, from a crawler, or on any browser this cannot identify.
   This file only ever *upgrades* that link — on Edge it swaps in the Edge
   Add-ons URL. A browser we do not recognise is sent to Chrome rather than
   guessed at, because a wrong store is worse than a slightly wrong one: the
   extension installs on any Chromium browser from the Chrome listing.

   Edge reports itself in userAgentData.brands as "Microsoft Edge", and in the
   classic user agent as "Edg/". Both are checked: the first is the supported
   API and the second still covers older builds. Note the missing "e" — "Edge/"
   with one is the pre-Chromium browser, which cannot run this extension at all,
   so matching "Edg/" as a substring would be wrong if it also caught "Edge/".
   It does, which is why the version digit is required after it. */
(function () {
  var STORES = {
    lens: {
      edge: 'https://microsoftedge.microsoft.com/addons/detail/lens-by-vectored-tab-ca/pnkipeejmankfpiajfcplokfoikecccg'
    }
  };

  function onEdge() {
    var data = navigator.userAgentData;
    if (data && Array.isArray(data.brands)) {
      for (var i = 0; i < data.brands.length; i++) {
        if (data.brands[i].brand === 'Microsoft Edge') return true;
      }
      // brands is authoritative where it exists; do not fall through to the UA
      return false;
    }
    // "Edg/120" is Chromium Edge. "Edge/18" is the old EdgeHTML browser, which
    // cannot install this, so the digit after the slash is what separates them.
    return /Edg\/\d/.test(navigator.userAgent);
  }

  function apply() {
    if (!onEdge()) return;
    var links = document.querySelectorAll('a[data-store]');
    for (var i = 0; i < links.length; i++) {
      var store = STORES[links[i].getAttribute('data-store')];
      if (!store || !store.edge) continue;
      links[i].href = store.edge;
      // The label often names the store it is going to
      var label = links[i].querySelector('[data-store-name]');
      if (label) label.textContent = 'Edge Add-ons';
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', apply);
  } else {
    apply();
  }
})();
