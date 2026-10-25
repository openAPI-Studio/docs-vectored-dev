#!/usr/bin/env python3
"""Build the Depotex docs. Same engine as timesheets/_build."""
import html
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import engine
from engine import H, P, UL, NOTE, TABLE, SHOT
from content import PAGES

INTRO = [
    P("Depotex is a self-hosted artifact repository: one place for the packages, container images, models and files your teams build and depend on. It serves 15 package formats to the tools developers already use, keeps copies of public registries close to your builds, and gives security and platform teams the controls around them: SBOMs and known vulnerabilities, quarantine, a block list, policies and a full audit log. It runs on a single server or as a cluster, with the same features either way."),
    SHOT("dashboard-overview.png", "The dashboard: what needs attention, the installation's figures, spaces by size and the health of every part of the system"),
    H("What it does"),
    TABLE(["Capability", "What Depotex does"], [
        ["**Hosts your packages**", "Maven, npm, PyPI, Docker and OCI images, Helm, Go, NuGet, Cargo, APT, YUM, Terraform and OpenTofu, Hugging Face, Git LFS, Composer and raw files, each with its own client: `mvn` and Gradle, `npm`/`pnpm`/Yarn, `pip`/`uv`/`twine`, `docker`, `helm`, `go`, `dotnet`, `cargo`, `apt`, `dnf`, `terraform init`, `huggingface_hub`, `git lfs`, `composer` and `curl`. See [Supported formats](docs/formats.html)."],
        ["**Caches public registries**", "Proxy repositories fetch from Maven Central, npm, PyPI, Docker Hub, an internal mirror or another Depotex, and keep a copy, so builds keep working when the internet doesn't. Upstreams are registered once, health-checked, and allowed per space. See [Upstreams](docs/upstreams.html)."],
        ["**Gives every format one address**", "Group repositories put hosted and proxy repositories behind one URL: downloads come from the first member that has the file, uploads go where rules say. Each space has a universal address per format, `/repository/<space>/<format>/`. See [Repository groups](docs/repository-groups.html)."],
        ["**Organises by team**", "[Spaces](docs/spaces.html) hold repositories and decide who uses them: private, internal or public, with Viewer, Developer, Maintainer and Owner roles for people, groups and service accounts, plus upload rules, cleanup policies and storage quotas."],
        ["**Lets people find things**", "The [artifact browser](docs/browse.html) searches every repository you can see, walks each one as a tree, and opens a version with its install command, files, dependencies and security status. Files can also be uploaded from the browser."],
        ["**Knows what's inside**", "Reads the SBOMs (SPDX, CycloneDX) stored with artifacts or uploaded from CI for deployed applications, scores how complete they are, finds a component everywhere it's used, checks components against known vulnerabilities (OSV), records VEX assessments and exports. See [SBOMs](docs/sbom.html)."],
        ["**Keeps bad versions out**", "[Quarantine](docs/quarantine.html) holds new or suspect versions until someone releases them; the [block list](docs/blocklist.html) refuses a version everywhere, also through proxies; [integrity checks](docs/integrity.html) confirm every stored file is really there and unchanged; hostile metadata and SBOMs are quarantined on arrival."],
        ["**Enforces and automates**", "[Policies](docs/policies.html) block, warn about or adjust actions (repository formats, token lifetimes, SBOM licenses, sign-in networks), with a dry run first. [Automation](docs/automation.html) sends alerts, webhooks and emails when [events](docs/events.html) happen. Signed [plugins](docs/plugins.html) add checks, screens and tools for AI agents."],
        ["**Fits your identity setup**", "Accounts from the Local directory, LDAP, Active Directory, Microsoft Entra ID, Google Workspace or SCIM; [single sign-on](docs/single-sign-on.html) with OpenID Connect or SAML; [OAuth applications](docs/oauth-applications.html), device sign-in for command-line tools, service accounts and workload identity for CI without secrets; scoped [API tokens](docs/api-tokens.html) with [rate limits](docs/rate-limits.html)."],
        ["**Looks after itself**", "[Backups](docs/backups.html) with checks, encryption and test restores; a [system check](docs/system-check.html) and per-server cluster health; [scheduled jobs](docs/scheduler.html); log levels, log files and the [audit log](docs/logging-and-audit.html); Prometheus [metrics](docs/monitoring.html); [email](docs/email.html); [alerts](docs/alerts.html); your own [branding and banners](docs/branding-and-banners.html)."],
        ["**Runs where you do**", "Container images and a Helm chart for [Docker and Kubernetes](docs/kubernetes.html). PostgreSQL holds the records; Redis is optional on one server and required for a [cluster](docs/deployment-modes.html); files go to a local disk, S3, MinIO or Azure Blob. A setup wizard (or an unattended setup file) gets a new installation going, and [recovery mode](docs/recovery.html) explains what's wrong when an installed server can't start."],
    ]),
    H("How it's organised"),
    UL([
        "**Spaces** belong to the installation and hold **repositories**; a repository has one format and one type (hosted, proxy or group) and holds **versions** of components, each with its files.",
        "Every artifact has an address under `/repository/<space>/<repository>/…`, which is what package managers and CI use; people use the same Depotex in the browser.",
        "What someone may do comes from their system role (member, organization admin, super admin) and their role in each space. Tokens and applications never do more than the person behind them.",
        "Every major operation is an event: policies can stop it before it happens, and automation, plugins and the audit log see it after.",
    ]),
    H("Editions"),
    TABLE(["Tier", "For"], [
        ["**Standard**", "Hosted and group repositories in every format, spaces, the artifact browser, users and groups, backups and email"],
        ["**Pro**", "Proxy repositories, clustering, the system check, the audit log, policies, automation and plugins"],
        ["**Enterprise**", "Single sign-on, quarantine, the block list, branding and managing everyone's API tokens"],
    ]),
    P("Each feature's page says which tier it needs. See [Licensing](docs/licensing.html)."),
    H("Where to start"),
    UL([
        "[Getting Started](docs/getting-started.html): install, the setup key and the setup wizard.",
        "[Docker & Kubernetes](docs/kubernetes.html): the container images and the Helm chart.",
        "[Spaces](docs/spaces.html) and [Supported formats](docs/formats.html): create a space and its first repository, then point your package manager at it.",
        "[Users & Directories](docs/users-and-directories.html): bring people in.",
        "[Changelog](docs/changelog.html): what's new.",
    ]),
]

# Sidebar groups, in reading order. Depotex isn't in the shared
# assets/nav.js (tools/gen_nav.py) until launch, so the build writes its own
# registry entry to depotex/assets/nav-local.js, which only Depotex pages
# load. Pages missing from GROUPS land in "More" so none disappear.
GROUPS = [
    ("Start here", ["getting-started", "kubernetes", "deployment-modes", "recovery"]),
    ("Users & access", ["users-and-directories", "single-sign-on", "oauth-applications", "api-tokens", "rate-limits"]),
    ("Operations", ["branding-and-banners", "logging-and-audit", "system-check", "monitoring", "email", "scheduler", "licensing"]),
    ("Alerts & automation", ["alerts", "alerts-admin", "events", "policies", "automation", "plugins"]),
    ("Repositories", ["repositories"]),
    ("Formats", ["formats", "maven", "npm", "pypi", "go", "helm", "nuget", "cargo", "apt", "yum", "terraform", "huggingface", "git-lfs", "composer", "rubygems", "docker", "raw"]),
    ("What's new", ["changelog"]),
]


def write_local_nav(pages):
    by_slug = dict(pages)
    placed = set()
    groups = []

    def item(slug):
        p = by_slug[slug]
        label = html.unescape(p["label"])
        text = " ".join([label, html.unescape(p.get("desc", "")), " ".join(p.get("keywords", []))]).lower()
        return {"h": slug + ".html", "l": label, "t": text}

    for title, slugs in GROUPS:
        items = [item(s) for s in slugs if s in by_slug]
        placed.update(s for s in slugs if s in by_slug)
        if items:
            groups.append({"title": title, "items": items})
    rest = [item(s) for s, _ in pages if s not in placed]
    if rest:
        groups.append({"title": "More", "items": rest})
    entry = {
        "key": "depotex", "label": "Depotex", "blurb": "Self-hosted artifact repository", "dir": "depotex",
        "icon": "favicon.svg", "cta": "depotex/docs/getting-started.html", "ctaLabel": "Get started",
        "homeLabel": "Depotex Overview", "docsHome": "depotex/docs/getting-started.html",
        "count": sum(len(g["items"]) for g in groups), "groups": groups,
    }
    out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "nav-local.js"
    out.parent.mkdir(exist_ok=True)
    out.write_text(
        "/* Generated by depotex/_build/build.py: Depotex's sidebar and search entry, loaded\n"
        "   only by Depotex pages until Depotex joins assets/nav.js at launch. */\n"
        "window.VC_PRODUCTS = (window.VC_PRODUCTS || []).filter(function (p) { return p.key !== 'depotex'; });\n"
        "window.VC_PRODUCTS.push(" + json.dumps(entry, ensure_ascii=False) + ");\n",
        encoding="utf-8",
    )
    return entry["count"]


if __name__ == "__main__":
    pages, shots, tocs = engine.build(PAGES, INTRO)
    print(f"pages: {pages}")
    print(f"screenshot slots: {shots}")
    print(f"pages with on-this-page nav: {tocs}")
    print(f"sidebar entries: {write_local_nav(PAGES)}")
