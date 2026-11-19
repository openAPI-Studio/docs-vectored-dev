"""Which guide each page belongs to, and the two sidebars.

Same layout as depotex/_build/guides.py:

- the **user guide** (wiki/docs/): for people who read and write pages;
- the **admin guide** (wiki/admin/): for the people who install, license,
  configure, secure and run the wiki.

A page lives in one folder. Pages both audiences need (SHARED) stay in docs/
and are listed in both sidebars; the sidebar a shared page shows is the guide
the reader came from (assets/nav-local.js remembers it for the tab).

Content links pages by bare file name (`spaces.html`); the engine points each
link into the right folder.

While several people write pages at once, `WIKI_DOCS_PARTIAL=1` lets the build
run with pages still missing; the published build is always strict.
"""
import os

# Pages written for the admin guide.
ADMIN = [
    "index", "install-planning", "install", "deployment-modes", "environment-variables",
    "setup-wizard", "headless-setup", "licensing", "recovery",
    "settings-reference", "access-overview", "users-and-directories", "single-sign-on", "rate-limits",
    "storage", "email", "branding-and-banners",
    "analytics-settings", "calendar-feeds", "confluence-import", "qna-moderation", "template-library",
    "security-hardening", "anonymous-access", "search-engines-and-robots", "policies", "logging-and-audit",
    "personal-data",
    "system-check", "alert-tuning", "monitoring", "backups", "upgrades", "scheduler", "alerts-admin",
    "automation", "plugins",
    "known-issues", "faq", "support",
]

# In docs/, listed in both sidebars.
SHARED = ["changelog", "api-tokens", "oauth-applications", "spaces", "events"]

USER_GROUPS = [
    ("Start here", ["getting-started", "home-and-navigation", "search", "profile-and-notifications", "alerts",
                    "api-tokens", "@admin"]),
    ("Spaces & pages", ["spaces", "pages-and-the-page-tree", "editor", "macros", "drafts-and-publishing", "reviews",
                        "page-history-and-versions", "comments", "editing-together", "copies-and-templates",
                        "attachments-and-media", "labels-and-feedback", "import-and-export", "mirror-spaces", "blogs", "whiteboards"]),
    ("Q&A", ["qna"]),
    ("Calendar & analytics", ["calendar", "analytics"]),
    ("Mobile", ["mobile"]),
    ("Integrations & what's new", ["events", "oauth-applications", "changelog"]),
]

ADMIN_GROUPS = [
    ("Admin guide", ["index", "@user"]),
    ("Install", ["install-planning", "install", "deployment-modes", "environment-variables"]),
    ("Set up", ["setup-wizard", "headless-setup", "licensing", "recovery"]),
    ("Configure", ["settings-reference", "access-overview", "users-and-directories", "single-sign-on",
                   "oauth-applications", "api-tokens", "rate-limits", "storage", "email", "branding-and-banners"]),
    ("Spaces & content", ["spaces", "analytics-settings", "calendar-feeds", "confluence-import", "template-library", "qna-moderation"]),
    ("Security", ["security-hardening", "anonymous-access", "search-engines-and-robots", "policies",
                  "logging-and-audit", "personal-data"]),
    ("Operate", ["system-check", "alert-tuning", "monitoring", "backups", "upgrades", "scheduler", "alerts-admin",
                 "events", "automation", "plugins"]),
    ("Help", ["known-issues", "faq", "support", "changelog"]),
]

PARTIAL = os.environ.get("WIKI_DOCS_PARTIAL") == "1"


def _check(cond, msg):
    if not cond:
        if PARTIAL:
            print("warning (partial build):", msg)
        else:
            raise SystemExit(msg)


def place(pages):
    """Mark each page with its folder (dir) and guide (user, admin, shared)."""
    admin, shared = set(ADMIN), set(SHARED)
    slugs = {s for s, _ in pages}
    missing = (admin | shared) - slugs
    _check(not missing, f"guides.py names pages that don't exist: {sorted(missing)}")
    seen = set()
    for slug, p in pages:
        _check(slug not in seen, f"page {slug!r} is defined twice")
        seen.add(slug)
        if slug in admin:
            p["dir"], p["guide"] = "admin", "admin"
        else:
            p["dir"] = "docs"
            p["guide"] = "shared" if slug in shared else "user"
    listed = set()
    for title, items in USER_GROUPS + ADMIN_GROUPS:
        for s in items:
            listed.add(s)
            if not s.startswith("@"):
                _check(s in slugs, f"guides.py: sidebar group {title!r} names unknown page {s!r}")
    _check(slugs <= listed, f"pages in no sidebar group: {sorted(slugs - listed)}")
    return pages
