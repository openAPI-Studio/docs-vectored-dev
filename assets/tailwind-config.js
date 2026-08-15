/* Shared Tailwind CDN configuration. Load immediately after the CDN script:

     <script src="https://cdn.tailwindcss.com"></script>
     <script src="<relative-path>/assets/tailwind-config.js"></script>

   Colours here are the dark-theme values. They are re-pointed at the CSS
   custom properties in assets/tokens.css, which is what makes light mode and
   print a token swap; the hex values below only matter for the opacity
   modifiers Tailwind computes at build time (bg-cta/10 and friends). */
window.tailwind = window.tailwind || {};
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: '#1A2740',
        secondary: '#1A2740',
        cta: '#22C55E',
        bg: '#0F172A',
        surface: '#131F35',
        card: '#1A2740',
        text: '#F8FAFC',
        body: '#CBD5E1',
        muted: '#8FA3BF',
        border: '#2B3A54'
      },
      fontFamily: {
        sans: ['IBM Plex Sans', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace']
      }
    }
  }
};
