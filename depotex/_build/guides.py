"""Which guide each page belongs to, and the two sidebars.

The docs are two guides:

- the **user guide** (depotex/docs/): for people who use Depotex day to day —
  publish and download packages, browse, search, tokens, alerts;
- the **admin guide** (depotex/admin/): for the people who install, license,
  configure, secure and run it.

A page lives in one folder. Pages both audiences need (SHARED) stay in docs/
and are listed in both sidebars; the sidebar a shared page shows is the guide
the reader came from (assets/nav-local.js remembers it for the tab). A page
that moved from docs/ to admin/ (MOVED) leaves a redirect behind, so old
links and bookmarks keep working.

Content links pages by bare file name (`spaces.html`); the engine points each
link into the right folder, so moving a page here needs no other edit.
"""

# Pages that used to be in docs/ and now live in the admin guide.
MOVED = [
    "kubernetes", "deployment-modes", "recovery", "licensing",
    "users-and-directories", "single-sign-on", "rate-limits",
    "branding-and-banners", "logging-and-audit", "system-check", "monitoring", "email", "scheduler",
    "alerts-admin", "policies", "automation", "plugins",
    "storage", "backups", "integrity", "upstreams",
]

# New pages written for the admin guide.
ADMIN_NEW = [
    "index", "install-planning", "install", "helm-chart", "environment-variables", "setup-wizard", "headless-setup",
    "settings-reference", "security-hardening", "upgrades", "known-issues", "faq", "support",
]

# In docs/, listed in both sidebars.
SHARED = [
    "changelog", "security-advisories", "api-tokens", "oauth-applications", "repositories", "spaces",
    "repository-settings", "quarantine", "blocklist", "sbom", "events", "vibe-artifacts",
]

# "Admin guide" and "User guide" cross links sit in each sidebar; x marks them
# as outside the reading order (prev/next).
USER_GROUPS = [
    ("Start here", ["getting-started", "dashboard", "search", "profile", "api-tokens", "@admin"]),
    ("Spaces & repositories", ["spaces", "repositories", "repository-groups", "repository-settings", "browse"]),
    ("Formats", ["formats", "maven", "npm", "pypi", "go", "helm", "nuget", "cargo", "apt", "yum", "terraform",
                 "huggingface", "git-lfs", "composer", "rubygems", "conda", "conan", "docker", "raw"]),
    ("Security & supply chain", ["sbom", "quarantine", "blocklist", "vibe-artifacts", "security-advisories"]),
    ("Notifications & integrations", ["alerts", "events", "oauth-applications"]),
    ("What's new", ["changelog"]),
]

ADMIN_GROUPS = [
    ("Admin guide", ["index", "@user"]),
    ("Install", ["install-planning", "install", "helm-chart", "kubernetes", "deployment-modes",
                 "environment-variables"]),
    ("Set up", ["setup-wizard", "headless-setup", "licensing", "recovery"]),
    ("Configure", ["settings-reference", "users-and-directories", "single-sign-on", "oauth-applications", "api-tokens",
                   "rate-limits", "storage", "email", "branding-and-banners"]),
    ("Repositories", ["spaces", "repositories", "upstreams", "repository-settings"]),
    ("Security", ["security-hardening", "quarantine", "blocklist", "integrity", "sbom", "vibe-artifacts",
                  "policies", "logging-and-audit", "security-advisories"]),
    ("Operate", ["system-check", "monitoring", "backups", "upgrades", "scheduler", "alerts-admin", "events",
                 "automation", "plugins"]),
    ("Help", ["known-issues", "faq", "support", "changelog"]),
]


def place(pages):
    """Mark each page with its folder (dir) and guide (user, admin, shared)."""
    moved, new, shared = set(MOVED), set(ADMIN_NEW), set(SHARED)
    slugs = {s for s, _ in pages}
    missing = (moved | new | shared) - slugs
    if missing:
        raise SystemExit(f"guides.py names pages that don't exist: {sorted(missing)}")
    for slug, p in pages:
        if slug in moved or slug in new:
            p["dir"], p["guide"] = "admin", "admin"
            p["moved"] = slug in moved
        else:
            p["dir"] = "docs"
            p["guide"] = "shared" if slug in shared else "user"
    for title, items in USER_GROUPS + ADMIN_GROUPS:
        for s in items:
            if not s.startswith("@") and s not in slugs:
                raise SystemExit(f"guides.py: sidebar group {title!r} names unknown page {s!r}")
    return pages
