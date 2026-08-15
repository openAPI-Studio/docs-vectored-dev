/* Vectored feedback templates.
   One registry that drives feedback.html and feedback-thanks.html.

   Adding a tool = add an entry to TOOLS below. Nothing else changes: the tool
   dropdown, the conditional questions, the aside card and the thank-you page
   all read from here. A tool that has no entry (or an unknown ?tool= value)
   falls back to GENERIC, so the form never breaks on a new product.

   Field schema:
     id        querystring key + submitted key
     label     visible label
     type      text | textarea | select | multiselect | radio | rating | checkbox
     options   [string] for select/multiselect/radio
     required  bool
     help      small grey hint under the field
     when      { field: [values] } — only shown when another field matches
*/
(function () {
  'use strict';

  // Questions every submission carries, whatever the tool.
  var BASE_QUESTIONS = [
    {
      id: 'type',
      label: 'What kind of feedback is this?',
      type: 'radio',
      required: true,
      options: ['Bug', 'Feature request', 'Usability', 'Praise', 'Question', 'Other'],
    },
    {
      id: 'severity',
      label: 'How badly is it hurting you?',
      type: 'select',
      options: ['Blocker — we cannot ship', 'Major — painful workaround', 'Minor — annoying', 'Cosmetic'],
      when: { type: ['Bug', 'Usability'] },
    },
    {
      id: 'frequency',
      label: 'How often do you hit this?',
      type: 'select',
      options: ['Every time', 'Most days', 'Weekly', 'Rarely', 'Saw it once'],
      when: { type: ['Bug', 'Usability'] },
    },
    { id: 'subject', label: 'Summary', type: 'text', required: true, placeholder: 'One line — what happened, or what you want' },
    {
      id: 'message',
      label: 'Tell us the details',
      type: 'textarea',
      required: true,
      rows: 6,
      placeholder: 'Steps you took, what you expected, what you got. Links and screenshots URLs welcome.',
    },
  ];

  var GENERIC = {
    id: 'other',
    name: 'Something else',
    platform: 'Vectored',
    tagline: 'General feedback about Vectored',
    badge: null,
    docs: 'https://docs.vectored.dev/',
    marketplace: null,
    accent: '#22C55E',
    initial: 'V',
    ratingLabel: 'How would you rate your experience with Vectored?',
    areas: ['Documentation', 'Website', 'Pricing / licensing', 'Support', 'Something else'],
    questions: [],
    nextSteps: [
      { label: 'Browse the documentation hub', href: 'https://docs.vectored.dev/' },
      { label: 'See what is on the roadmap', href: 'https://docs.vectored.dev/#products' },
    ],
  };

  var TOOLS = {
    macrotoolkit: {
      id: 'macrotoolkit',
      name: 'Macro Toolkit',
      platform: 'for Confluence',
      tagline: '15 macros for pages that do more.',
      badge: 'LIVE',
      docs: 'https://docs.vectored.dev/macrotoolkit/',
      marketplace: 'https://marketplace.atlassian.com/apps/3972300183',
      icon: 'macrotoolkit/assets/icon_lite.png',
      accent: '#22C55E',
      initial: 'M',
      ratingLabel: 'How would you rate Macro Toolkit?',
      areas: ['Mermaid', 'PlantUML', 'draw.io', 'Excalidraw', 'Charts', 'Polls', 'Markdown', 'Swagger / OpenAPI', 'Carousel', 'Mood board', 'Editor experience', 'Rendering / export', 'Something else'],
      questions: [
        { id: 'macro', label: 'Which macro is this about?', type: 'select', options: ['Mermaid', 'PlantUML', 'draw.io', 'Excalidraw', 'Chart', 'Poll', 'Markdown', 'Swagger / OpenAPI', 'Carousel', 'Mood board', 'Not macro-specific'] },
        { id: 'context', label: 'Where did you see it?', type: 'select', options: ['Page editor', 'Published page view', 'PDF / Word export', 'Mobile app', 'Not sure'] },
      ],
      nextSteps: [
        { label: 'Macro Toolkit documentation', href: 'https://docs.vectored.dev/macrotoolkit/' },
        { label: 'Mermaid macro guide', href: 'https://docs.vectored.dev/macrotoolkit/docs/mermaid.html' },
      ],
    },

    forms: {
      id: 'forms',
      name: 'Forms & Frontdoor',
      platform: 'for Confluence',
      tagline: 'Form builder with a post-submit automation canvas.',
      badge: 'LIVE',
      docs: 'https://docs.vectored.dev/forms/',
      marketplace: 'https://marketplace.atlassian.com/apps/2466520058/forms-frontdoor-by-vectored?hosting=cloud&tab=overview',
      icon: 'forms/assets/icon.png',
      accent: '#22C55E',
      initial: 'F',
      ratingLabel: 'How would you rate Forms & Frontdoor?',
      areas: ['Form builder', 'Field types', 'Theming', 'Access control', 'Automation canvas', 'Submissions & CSV export', 'Embedding', 'Notifications', 'Something else'],
      questions: [
        { id: 'automationTarget', label: 'Which automation step is involved?', type: 'select', options: ['Create Confluence page', 'Create / update Jira issue', 'Post to Slack', 'Post to Teams', 'Email', 'No automation involved'] },
        { id: 'formSize', label: 'Roughly how large is the form?', type: 'select', options: ['Under 10 fields', '10–30 fields', '30+ fields', 'Multi-section'] },
      ],
      nextSteps: [
        { label: 'Getting started with Forms', href: 'https://docs.vectored.dev/forms/docs/getting-started.html' },
        { label: 'Automation guide', href: 'https://docs.vectored.dev/forms/docs/automation.html' },
        { label: 'Embedding guide', href: 'https://docs.vectored.dev/forms/docs/embedding.html' },
      ],
    },

    apistudio: {
      id: 'apistudio',
      name: 'API Studio',
      platform: 'for VS Code & CLI',
      tagline: 'API development, testing and docs without leaving your editor.',
      badge: 'LIVE',
      docs: 'https://docs.vectored.dev/apistudio/',
      marketplace: 'https://github.com/openAPI-Studio',
      icon: 'apistudio/assets/icon.svg',
      accent: '#22C55E',
      initial: 'A',
      ratingLabel: 'How would you rate API Studio?',
      areas: ['Request editor', 'Collections', 'Environments & variables', 'Mock server', 'MCP server', 'Vault / secrets', 'Tests & assertions', 'Code export', 'CLI / CI', 'Something else'],
      questions: [
        { id: 'surface', label: 'Where are you running it?', type: 'select', options: ['VS Code', 'Cursor', 'Kiro', 'Antigravity', 'CLI', 'Other editor'] },
        { id: 'protocol', label: 'Which protocol?', type: 'select', options: ['HTTP', 'WebSocket', 'gRPC', 'GraphQL', 'Not protocol-specific'] },
        { id: 'version', label: 'Extension / CLI version', type: 'text', placeholder: 'e.g. 1.4.2', help: 'Shown in the extension sidebar or via the CLI --version flag.' },
      ],
      nextSteps: [
        { label: 'API Studio documentation', href: 'https://docs.vectored.dev/apistudio/' },
        { label: 'API Studio on GitHub', href: 'https://github.com/openAPI-Studio' },
      ],
    },

    rewardhub: {
      id: 'rewardhub',
      name: 'Recognition Hub',
      platform: 'for Confluence & Jira',
      tagline: 'Peer recognition that lives where the work happens.',
      badge: 'LIVE',
      docs: 'https://docs.vectored.dev/rewardhub/',
      marketplace: 'https://marketplace.atlassian.com/apps/564712405',
      icon: 'rewardhub/assets/logo.png',
      accent: '#22C55E',
      initial: 'R',
      ratingLabel: 'How would you rate Recognition Hub?',
      areas: ['Kudos mural', 'Card templates', 'Company values', 'GIFs & reactions', 'Email notifications', 'Page macro / embedding', 'Admin settings', 'Something else'],
      questions: [
        { id: 'host', label: 'Where do you use it?', type: 'select', options: ['Confluence', 'Jira', 'Both'] },
        { id: 'teamSize', label: 'How many people use it?', type: 'select', options: ['Under 25', '25–100', '100–500', '500+'] },
      ],
      nextSteps: [{ label: 'Recognition Hub documentation', href: 'https://docs.vectored.dev/rewardhub/' }],
    },

    timesheets: {
      id: 'timesheets',
      name: 'TimeSheets',
      platform: 'for Jira',
      tagline: 'Time tracking, approvals and leave inside Jira.',
      badge: 'COMING SOON',
      docs: 'https://docs.vectored.dev/timesheets/',
      marketplace: null,
      icon: 'timesheets/assets/icon.png',
      accent: '#F59E0B',
      initial: 'T',
      ratingLabel: 'How interested are you in TimeSheets?',
      areas: ['Time logging', 'Approvals', 'Leave & holidays', 'Cost centers', 'Period locking', 'Reporting', 'Worklog sync', 'Something else'],
      questions: [
        { id: 'earlyAccess', label: 'Want early access?', type: 'radio', options: ['Yes, put me on the beta list', 'No, just leaving feedback'] },
        { id: 'currentTool', label: 'What do you use for time tracking today?', type: 'text', placeholder: 'e.g. Tempo, spreadsheets, nothing' },
      ],
      nextSteps: [{ label: 'TimeSheets documentation', href: 'https://docs.vectored.dev/timesheets/' }],
    },

    frontdoor: {
      id: 'frontdoor',
      name: 'Front Door',
      platform: 'for Confluence',
      tagline: 'Customizable landing pages and portals for spaces.',
      badge: 'ROADMAP',
      docs: 'https://docs.vectored.dev/#products',
      marketplace: null,
      accent: '#F59E0B',
      initial: 'D',
      ratingLabel: 'How useful would Front Door be for you?',
      areas: ['Space landing pages', 'Portals & navigation', 'Branding / theming', 'Permissions', 'Something else'],
      questions: [
        { id: 'earlyAccess', label: 'Want early access?', type: 'radio', options: ['Yes, put me on the beta list', 'No, just leaving feedback'] },
        { id: 'useCase', label: 'What would you build with it?', type: 'textarea', rows: 3, placeholder: 'The portal or landing page you have in mind.' },
      ],
      nextSteps: [{ label: 'See the product list', href: 'https://docs.vectored.dev/#products' }],
    },

    docs: {
      id: 'docs',
      name: 'Documentation',
      platform: 'docs.vectored.dev',
      tagline: 'The docs themselves — gaps, errors, missing examples.',
      badge: null,
      docs: 'https://docs.vectored.dev/',
      marketplace: null,
      accent: '#22C55E',
      initial: 'D',
      ratingLabel: 'How would you rate our documentation?',
      areas: ['Missing content', 'Wrong / outdated content', 'Hard to find', 'Needs more examples', 'Search', 'Something else'],
      questions: [{ id: 'pageUrl', label: 'Which page?', type: 'text', placeholder: 'https://docs.vectored.dev/...' }],
      nextSteps: [{ label: 'Back to the documentation hub', href: 'https://docs.vectored.dev/' }],
    },
  };

  // Order the dropdown deliberately: live products first, then upcoming, then catch-alls.
  var ORDER = ['macrotoolkit', 'forms', 'apistudio', 'rewardhub', 'timesheets', 'frontdoor', 'docs'];

  // Aliases so old links, marketplace slugs and in-app links all resolve.
  var ALIASES = {
    'macro-toolkit': 'macrotoolkit',
    macro: 'macrotoolkit',
    mt: 'macrotoolkit',
    form: 'forms',
    'forms-frontdoor': 'forms',
    ff: 'forms',
    'api-studio': 'apistudio',
    api: 'apistudio',
    openapi: 'apistudio',
    as: 'apistudio',
    recognitionhub: 'rewardhub',
    'recognition-hub': 'rewardhub',
    kudos: 'rewardhub',
    rh: 'rewardhub',
    timesheet: 'timesheets',
    'time-log': 'timesheets',
    timelog: 'timesheets',
    ts: 'timesheets',
    'front-door': 'frontdoor',
    portal: 'frontdoor',
    documentation: 'docs',
    generic: 'other',
    general: 'other',
  };

  function resolve(key) {
    if (!key) return null;
    var k = String(key).trim().toLowerCase().replace(/\s+/g, '');
    k = ALIASES[k] || k;
    return TOOLS[k] || (k === 'other' ? GENERIC : null);
  }

  // Merge a tool template over the generic base. Unknown tool -> pure generic.
  function template(key) {
    var t = resolve(key);
    if (!t) t = GENERIC;
    return {
      id: t.id,
      name: t.name,
      platform: t.platform || '',
      tagline: t.tagline || GENERIC.tagline,
      badge: t.badge || null,
      docs: t.docs || GENERIC.docs,
      marketplace: t.marketplace || null,
      icon: t.icon || null,
      accent: t.accent || GENERIC.accent,
      initial: t.initial || t.name.charAt(0),
      ratingLabel: t.ratingLabel || GENERIC.ratingLabel,
      areas: (t.areas && t.areas.length ? t.areas : GENERIC.areas).slice(),
      questions: BASE_QUESTIONS.concat(t.questions || []),
      nextSteps: (t.nextSteps && t.nextSteps.length ? t.nextSteps : GENERIC.nextSteps).slice(),
      isFallback: t === GENERIC,
    };
  }

  function list() {
    var out = [];
    for (var i = 0; i < ORDER.length; i++) if (TOOLS[ORDER[i]]) out.push(TOOLS[ORDER[i]]);
    out.push(GENERIC);
    return out;
  }

  window.VectoredFeedback = {
    tools: TOOLS,
    generic: GENERIC,
    baseQuestions: BASE_QUESTIONS,
    list: list,
    resolve: resolve,
    template: template,
  };
})();
