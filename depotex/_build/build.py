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
import guides

INTRO = [
    P("Depotex is a self-hosted artifact repository: one place for the packages, container images, models and files your teams build and depend on. It serves 18 package formats to the tools developers already use, keeps copies of public registries close to your builds, and gives security and platform teams the controls around them: SBOMs and known vulnerabilities, quarantine, a block list, policies and a full audit log. It runs on a single server or as a cluster, with the same features either way."),
    SHOT("dashboard-overview.png", "The dashboard: what needs attention, the installation's figures, spaces by size and the health of every part of the system"),
    H("What it does"),
    TABLE(["Capability", "What Depotex does"], [
        ["**Hosts your packages**", "Maven, npm, PyPI, Docker and OCI images, Helm, Go, NuGet, Cargo, APT, YUM, Terraform and OpenTofu, Hugging Face, Git LFS, Composer, RubyGems, Conda, Conan and raw files, each with its own client: `mvn` and Gradle, `npm`/`pnpm`/Yarn, `pip`/`uv`/`twine`, `docker`, `helm`, `go`, `dotnet`, `cargo`, `apt`, `dnf`, `terraform init`, `huggingface_hub`, `git lfs`, `composer`, `gem` and Bundler, `conda`/`micromamba`/`pixi`, `conan` and `curl`. See [Supported formats](docs/formats.html)."],
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
        "[Getting started](docs/getting-started.html): sign in, find a repository and point your package manager at it.",
        "[Admin guide](admin/index.html): install, set up, configure and run Depotex.",
        "[Docker & Kubernetes](docs/kubernetes.html): the container images and the Helm chart.",
        "[Spaces](docs/spaces.html) and [Supported formats](docs/formats.html): create a space and its first repository, then point your package manager at it.",
        "[Users & Directories](docs/users-and-directories.html): bring people in.",
        "[Changelog](docs/changelog.html): what's new.",
    ]),
]

# Sidebars. The shared assets/nav.js (tools/gen_nav.py) lists Depotex in the
# product switcher only, as coming soon; the build writes the real registry
# entries to depotex/assets/nav-local.js, which only Depotex pages load and
# which replaces that entry there. There are two:
# the user guide and the admin guide (guides.py says which page is where).
# Pages missing from a guide's groups land in its "More" group so none
# disappear.
CROSS = {
    "@admin": {"h": "../admin/index.html", "l": "Admin guide →", "t": "admin guide administrators install configure", "x": 1},
    "@user": {"h": "../docs/getting-started.html", "l": "User guide →", "t": "user guide getting started", "x": 1},
}


def nav_entry(pages, groups, key, label, home_label, docs_home, guide):
    by_slug = dict(pages)

    def item(slug):
        if slug in CROSS:
            return dict(CROSS[slug])
        p = by_slug[slug]
        label = html.unescape(p["label"])
        text = " ".join([label, html.unescape(p.get("desc", "")), " ".join(p.get("keywords", []))]).lower()
        h = slug + ".html" if p.get("dir", "docs") == "docs" else f"../{p['dir']}/{slug}.html"
        return {"h": h, "l": label, "t": text}

    placed, out = set(), []
    for title, slugs in groups:
        items = [item(s) for s in slugs if s in by_slug or s in CROSS]
        placed.update(slugs)
        if items:
            out.append({"title": title, "items": items})
    rest = [item(s) for s, p in pages if s not in placed and p.get("guide", "user") == guide]
    if rest:
        out.append({"title": "More", "items": rest})
    return {
        "key": key, "label": label, "blurb": "Self-hosted artifact repository" if guide == "user" else "Install, configure and run Depotex",
        "dir": "depotex", "icon": "favicon.svg", "cta": docs_home, "ctaLabel": "Get started" if guide == "user" else "Open the admin guide",
        "homeLabel": home_label, "docsHome": docs_home, "soon": 1,
        "count": sum(1 for g in out for i in g["items"] if not i.get("x")), "groups": out,
    }


# Product picked for a page: the admin guide under depotex/admin/; a shared
# page in the guide the reader came from (remembered for the tab); otherwise
# the user guide. Other products keep nav.js's own lookup.
PICKER = """(function () {
  var base = window.VC_PRODUCT_FOR;
  var user = window.VC_PRODUCTS.filter(function (p) { return p.key === 'depotex'; })[0];
  var admin = window.VC_PRODUCTS.filter(function (p) { return p.key === 'depotex-admin'; })[0];
  var shared = %s;
  function file(path) { return (path.split('/').pop() || '').replace(/\\.html$/, ''); }
  function remembered() { try { return sessionStorage.getItem('dx-guide'); } catch (e) { return null; } }
  window.VC_PRODUCT_FOR = function (path) {
    if (path.indexOf('/depotex/admin/') !== -1) return admin;
    if (path.indexOf('/depotex/') === -1) return base ? base(path) : null;
    if (shared[file(path)] && remembered() === 'admin') return admin;
    return user;
  };
  try {
    var here = location.pathname;
    if (here.indexOf('/depotex/admin/') !== -1) sessionStorage.setItem('dx-guide', 'admin');
    else if (here.indexOf('/depotex/docs/') !== -1 && !shared[file(here)]) sessionStorage.setItem('dx-guide', 'user');
  } catch (e) {}
})();
"""


def write_local_nav(pages):
    user = nav_entry(pages, guides.USER_GROUPS, "depotex", "Depotex", "Depotex Overview", "depotex/docs/getting-started.html", "user")
    admin = nav_entry(pages, guides.ADMIN_GROUPS, "depotex-admin", "Depotex Admin Guide", "Depotex Overview", "depotex/admin/index.html", "admin")
    shared = {s: 1 for s, p in pages if p.get("guide") == "shared"}
    out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "nav-local.js"
    out.parent.mkdir(exist_ok=True)
    out.write_text(
        "/* Generated by depotex/_build/build.py: Depotex's two sidebars (user guide and\n"
        "   admin guide) and search entries, loaded only by Depotex pages; they replace\n"
        "   the coming-soon entry assets/nav.js has for the switcher. */\n"
        "window.VC_PRODUCTS = (window.VC_PRODUCTS || []).filter(function (p) { return p.key !== 'depotex' && p.key !== 'depotex-admin'; });\n"
        "window.VC_PRODUCTS.push(" + json.dumps(user, ensure_ascii=False) + ");\n"
        "window.VC_PRODUCTS.push(" + json.dumps(admin, ensure_ascii=False) + ");\n"
        + PICKER % json.dumps(shared),
        encoding="utf-8",
    )
    return user["count"], admin["count"]


if __name__ == "__main__":
    guides.place(PAGES)
    # docs/getting-started.html was the install page and is now the user
    # quickstart: its old deep links (#behind-a-proxy, …) go on to the install page.
    by_slug = dict(PAGES)
    by_slug["getting-started"]["hash_moved"] = ("../admin/install.html", {
        engine.slugify(t) for k, t in by_slug["install"]["blocks"] if k == "h"
    } - {engine.slugify(t) for k, t in by_slug["getting-started"]["blocks"] if k == "h"})
    pages, shots, tocs = engine.build(PAGES, INTRO)
    import content_advisories
    feed = pathlib.Path(__file__).resolve().parent.parent / content_advisories.FEED
    feed.write_text(content_advisories.rss(), encoding="utf-8")
    print(f"advisories feed: {feed.name} ({len(content_advisories.ADVISORIES)} items)")
    print(f"pages: {pages}")
    print(f"screenshot slots: {shots}")
    print(f"pages with on-this-page nav: {tocs}")
    print("sidebar entries (user guide, admin guide): %d, %d" % write_local_nav(PAGES))
