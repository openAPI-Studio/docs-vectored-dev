/* Blog post registry. To publish a post:
   1. Copy blog/_template.html to blog/posts/<slug>.html and write your content.
   2. Add an entry at the TOP of this array (newest first).
   The blog listing page and search render from this file. */
var BLOG_POSTS = [
  {
    slug: "slack-teams-notifications-confluence-forms",
    title: "Slack and Teams notifications from Confluence forms",
    date: "2026-07-04",
    tag: "Forms & Frontdoor",
    excerpt: "Route every form submission to the channel where your team actually looks — no middleware, no Zapier, just a webhook URL and the automation canvas."
  },
  {
    slug: "introducing-forms-and-frontdoor",
    title: "Introducing Forms & Frontdoor for Confluence",
    date: "2026-07-03",
    tag: "Forms & Frontdoor",
    excerpt: "A visual form builder with 13 field types, theming, access control — and a post-submit automation canvas that talks to Confluence, Jira, Slack, and Teams. Now on the Atlassian Marketplace."
  }
];
