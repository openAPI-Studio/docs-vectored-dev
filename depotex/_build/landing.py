"""The Depotex overview page (depotex/index.html), from the Claude Design
"Depotex Landing" file. Header, footer and search are the site's shared ones
(header.js, footer.js); everything else is here. Links are relative to
depotex/index.html."""
import html

D = "docs/"

# Name, client, docs page and icon. Neutral line icons per format, except the
# five ecosystems the design shows with their own logo.
FORMATS = [
    ("Maven", "mvn · gradle", "maven"), ("npm", "npm · pnpm · yarn", "npm"), ("PyPI", "pip · uv · twine", "pypi"),
    ("Docker &amp; OCI", "docker", "docker"), ("Helm", "helm", "helm"), ("Go", "go", "go"),
    ("NuGet", "dotnet", "nuget"), ("Cargo", "cargo", "cargo"), ("APT", "apt", "apt"), ("YUM", "dnf", "yum"),
    ("Terraform", "terraform init", "terraform"), ("Hugging Face", "huggingface_hub", "huggingface"),
    ("Git LFS", "git lfs", "git-lfs"), ("Composer", "composer", "composer"), ("RubyGems", "gem", "rubygems"),
    ("Conda", "conda · pixi", "conda"), ("Conan", "conan", "conan"),
    ("Raw", "curl", "raw"),
]

L = "assets/formats/logos/"
LOGOS = {
    # key: (light src, dark src, width, height, slot width, extra classes for the dark one)
    "pypi": (L + "python-logo-only.svg", L + "python-logo-only.svg", 16, 16, 18, ""),
    "go": (L + "go-logo-blue.svg", L + "go-logo-white.svg", 27.5, 10.5, 29, ""),
    "cargo": (L + "rust-logo-blk.svg", L + "rust-logo-blk.svg", 20.5, 20.5, 18, "dx-invert"),
    "apt": (L + "debian-openlogo-nd.svg", L + "debian-openlogo-nd.svg", 12.5, 16, 18, ""),
}


def icon(key):
    if key == "composer":
        # On dark, the logo sits on a light tile so it stays legible.
        return (f'<span class="dx-slot" style="width:18px"><img src="{L}composer-logo.png" alt="" class="dx-light" style="width:13px;height:16px">'
                f'<img src="{L}composer-logo.png" alt="" class="dx-dark dx-tile" style="width:18px;height:18px"></span>')
    if key in LOGOS:
        lt, dk, w, h, slot, cls = LOGOS[key]
        if lt == dk and not cls:
            return f'<span class="dx-slot" style="width:{slot}px"><img src="{lt}" alt="" style="width:{w}px;height:{h}px"></span>'
        return (f'<span class="dx-slot" style="width:{slot}px"><img src="{lt}" alt="" class="dx-light" style="width:{w}px;height:{h}px">'
                f'<img src="{dk}" alt="" class="dx-dark {cls}" style="width:{w}px;height:{h}px"></span>')
    return (f'<span class="dx-slot" style="width:18px"><img src="assets/formats/light/{key}.svg" alt="" class="dx-light" style="width:18px;height:18px">'
            f'<img src="assets/formats/dark/{key}.svg" alt="" class="dx-dark" style="width:18px;height:18px"></span>')


def chip(name, client, key, hidden=False):
    aria = ' aria-hidden="true" tabindex="-1"' if hidden else ""
    return (f'<a href="{D}{key}.html" class="dx-chip"{aria}>{icon(key)}<span class="dx-chip-name">{name}</span>'
            f'<span class="dx-mono dx-chip-client">{html.escape(client)}</span></a>')


def marquee_row(items, dur, reverse):
    # Four copies so the strip is always wider than the screen; the animation
    # moves it by half, so the loop is seamless. Copies after the first are
    # hidden from screen readers and the keyboard.
    chips = "".join(chip(*f, hidden=i >= len(items)) for i, f in enumerate(items * 4))
    return f'<div class="dx-marq-row" style="animation-duration:{dur};animation-direction:{"reverse" if reverse else "normal"}">{chips}</div>'


GROUPS = [
    ("Start here", [("getting-started", "Getting Started", "Install Depotex and complete the setup wizard."), ("kubernetes", "Docker &amp; Kubernetes", "Container images and the Helm chart."), ("deployment-modes", "Single Node &amp; Cluster", "One node or many, with the same features."), ("recovery", "Recovery Mode", "When an installed server can't start, and how to fix it."), ("dashboard", "Dashboard", "What needs a look, figures and system health."), ("changelog", "Changelog", "What each release includes, newest first.")]),
    ("Repositories", [("spaces", "Spaces", "Who can use repositories, visibility and allowed formats."), ("repositories", "Repositories", "Create and manage artifact repositories."), ("repository-groups", "Repository groups", "Several repositories of one format behind one URL."), ("upstreams", "Upstreams", "External registries spaces may proxy."), ("browse", "Browse", "Search, walk trees and open any version."), ("repository-settings", "Repository settings", "Size limits, remote timeouts, proxies and CA certificates."), ("storage", "Storage", "Where files live, credentials and upload limits."), ("formats", "Supported formats", "Every format and the tools that work with it.")]),
    ("Security", [("sbom", "SBOMs", "What your software is made of, and known vulnerabilities."), ("quarantine", "Quarantine", "Hold new or suspect versions until released."), ("blocklist", "Block list", "Stop a version from being used anywhere."), ("integrity", "Integrity", "Check every stored file is present and unchanged."), ("policies", "Policies", "Rules that block, warn or adjust actions."), ("rate-limits", "Rate Limits &amp; Quotas", "Request and download limits per person, token and address.")]),
    ("Identity &amp; access", [("users-and-directories", "Users &amp; Directories", "Where accounts come from and how people sign in."), ("single-sign-on", "Single Sign-On", "Entra ID, Google, Okta, Keycloak, any OIDC or SAML provider."), ("oauth-applications", "OAuth Applications", "Pipelines, CLIs and AI agents without personal tokens."), ("api-tokens", "API Tokens", "Scoped tokens for automation and integrations."), ("licensing", "Licensing", "Tiers, installation ID and updating a license.")]),
    ("Operations", [("backups", "Backups", "Encrypted, checked and test-restored backups."), ("system-check", "System Check", "Health of every dependency and server, with alerts."), ("logging-and-audit", "Logging &amp; Audit", "Log levels, log files and who changed what."), ("monitoring", "Monitoring (Prometheus)", "Each server's metrics for Prometheus."), ("scheduler", "Scheduled Jobs", "The background jobs Depotex runs."), ("email", "Email", "SMTP, SES, Microsoft 365, SendGrid and more."), ("branding-and-banners", "Branding &amp; Banners", "App name, colors, logos and announcements.")]),
    ("Events &amp; automation", [("events", "Events", "What Depotex raises for policies, automation and plugins."), ("automation", "Automation", "Alerts, webhooks and emails when something happens."), ("plugins", "Plugins", "Signed plugins, including MCP tools for AI."), ("alerts", "Alerts", "The bell, toasts and your preferences."), ("alerts-admin", "Managing Alerts", "Send alerts, force categories, the alerts API.")]),
]


def docs_groups(slugs):
    out = []
    for title, items in GROUPS:
        items = [i for i in items if i[0] in slugs]
        links = "".join(f'<a href="{D}{s}.html" class="dx-doc"><span class="dx-doc-l">{l}</span><span class="dx-doc-d">{d}</span></a>' for s, l, d in items)
        out.append(f'<div><div class="dx-doc-head"><span class="dx-doc-title">{title}</span><span class="dx-mono dx-muted dx-12">{len(items):02d}</span></div>'
                   f'<div class="dx-col">{links}</div></div>')
    return "".join(out)


def links(items):
    return "".join(f'<a href="{D}{h}.html" class="dx-row-link"><span>{l}</span><span class="dx-muted">→</span></a>' for h, l in items)


def feature(eyebrow, title, body, items, img, alt, image_first):
    text = (f'<div><div class="dx-eyebrow">{eyebrow}</div><h3 class="dx-h3">{title}</h3><p class="dx-body dx-mb24">{body}</p>'
            f'<div class="dx-links">{links(items)}</div></div>')
    pic = f'<div class="dx-frame"><img src="assets/{img}" alt="{alt}" class="dx-frame-img" loading="lazy"></div>'
    return f'<div class="dx-feature">{pic + text if image_first else text + pic}</div>'


CSS = """
:root{--amber:#FBBF24;--amberSoft:rgba(245,158,11,.1);--amberLine:rgba(245,158,11,.28);--shadow:0 20px 48px rgba(2,8,23,.45)}
html[data-theme="light"]{--amber:#B45309;--amberSoft:rgba(245,158,11,.12);--amberLine:rgba(180,83,9,.3);--shadow:0 20px 48px rgba(15,23,42,.14)}
html{scroll-behavior:smooth}
.dx a{color:var(--green);text-decoration:none}.dx a:hover{text-decoration:underline}
.dx .dx-mono{font-family:'JetBrains Mono',monospace}
.dx .dx-muted{color:var(--muted)}.dx .dx-12{font-size:12px}
.dx-sec{max-width:1240px;margin:0 auto;padding:clamp(72px,10vw,112px) clamp(20px,5vw,48px) 0;box-sizing:border-box}
.dx-eyebrow{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--green);margin-bottom:14px}
.dx-h2{font-size:clamp(28px,3.6vw,40px);line-height:1.15;font-weight:700;letter-spacing:-.03em;margin:0;color:var(--tx)}
.dx-h3{font-size:clamp(24px,3.4vw,30px);line-height:1.2;font-weight:700;letter-spacing:-.025em;margin:0 0 16px;color:var(--tx)}
.dx-body{font-size:17px;line-height:1.7;color:var(--body);margin:0;text-wrap:pretty}
.dx-mb24{margin-bottom:24px}
.dx-btn{display:inline-flex;align-items:center;gap:8px;background:var(--green);color:var(--onGreen)!important;font-weight:600;font-size:16px;padding:12px 20px;border-radius:10px}
.dx-btn:hover{text-decoration:none!important;opacity:.92}
.dx-btn2{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--border);color:var(--tx)!important;font-weight:500;font-size:16px;padding:11px 20px;border-radius:10px;background:var(--card)}
.dx-btn2:hover{text-decoration:none!important;border-color:var(--greenLine)}
.dx-pill{display:inline-flex;align-items:center;gap:10px;border:1px solid var(--amberLine);background:var(--amberSoft);border-radius:999px;padding:5px 14px 5px 10px;margin-bottom:28px}
.dx-dot{width:8px;height:8px;border-radius:50%;background:var(--amber);animation:dxpulse 1.8s ease-in-out infinite}
.dx-soon{font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--amber)}
@keyframes dxpulse{0%,100%{opacity:1}50%{opacity:.35}}
@keyframes dxmarq{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.dx-marq{display:flex;flex-direction:column;gap:12px;margin:0 calc(-1 * clamp(20px,5vw,48px));overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}
.dx-marq-row{display:flex;gap:12px;width:max-content;padding-right:12px;animation-name:dxmarq;animation-timing-function:linear;animation-iteration-count:infinite}
.dx-marq-row:hover,.dx-marq-row:focus-within{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.dx-marq-row{animation:none}.dx-marq{overflow-x:auto}.dx-dot{animation:none}}
.dx-chip{flex-shrink:0;display:flex;align-items:baseline;gap:12px;padding:clamp(12px,2.4vw,16px) clamp(16px,3vw,22px);border:1px solid var(--border);border-radius:12px;background:var(--surface);color:var(--tx)!important;white-space:nowrap}
.dx-chip:hover{border-color:var(--greenLine);text-decoration:none!important}
.dx-chip-name{font-size:17px;font-weight:600}.dx-chip-client{font-size:13px;color:var(--muted)}
.dx-slot{display:flex;align-items:center;justify-content:center;align-self:center;flex-shrink:0;height:18px}
.dx-slot img{display:block;object-fit:contain;box-sizing:border-box}
.dx-tile{background:#F1F5F9;padding:2px;border-radius:4px}
html[data-theme="light"] .dx-dark{display:none!important}
html:not([data-theme="light"]) .dx-light{display:none!important}
html:not([data-theme="light"]) .dx-invert{filter:invert(1)}
.dx-feature{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,400px),1fr));gap:clamp(28px,5vw,56px);align-items:center}
/* One column: the text first, then its screenshot, in every row. */
@media (max-width:900px){.dx-feature>.dx-frame{order:2}}
.dx-frame{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:10px}
.dx-frame-img{width:100%;aspect-ratio:16/11;object-fit:cover;object-position:top left;display:block;border-radius:7px}
.dx-links{display:flex;flex-direction:column;border-top:1px solid var(--border)}
.dx-row-link{display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-bottom:1px solid var(--border);color:var(--tx)!important;font-size:15px}
.dx-row-link:hover{color:var(--green)!important;text-decoration:none!important}
.dx-card{border:1px solid var(--border);border-radius:12px;padding:20px;background:var(--surface);display:flex;flex-direction:column;gap:8px}
.dx-card-t{font-size:18px;font-weight:600;color:var(--tx)}.dx-card-b{font-size:14.5px;line-height:1.6;color:var(--body)}
.dx-dl{margin:0;border:1px solid var(--border);border-radius:14px;overflow:hidden}
.dx-dl>div{display:grid;grid-template-columns:minmax(88px,140px) minmax(0,1fr);gap:16px;padding:13px clamp(14px,3vw,20px);border-bottom:1px solid var(--border)}
.dx-dl>div:last-child{border-bottom:0}
.dx-dl dt{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--muted)}.dx-dl dd{margin:0;font-size:15px;color:var(--tx)}
.dx-tier{border:1px solid var(--border);border-radius:16px;padding:clamp(20px,4vw,28px);background:var(--surface);display:flex;flex-direction:column;gap:14px}
.dx-tier-n{font-size:22px;font-weight:700;color:var(--tx)}.dx-tier-b{font-size:15.5px;line-height:1.65;color:var(--body)}
.dx-doc-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;padding-bottom:12px;border-bottom:1px solid var(--border);margin-bottom:6px}
.dx-doc-title{font-size:17px;font-weight:600;color:var(--tx)}
.dx-col{display:flex;flex-direction:column}
.dx-doc{display:flex;flex-direction:column;gap:3px;padding:10px;margin:0 -10px;border-radius:8px;color:var(--tx)!important}
.dx-doc:hover{background:var(--surface);text-decoration:none!important}
.dx-doc-l{font-size:15px;font-weight:500}.dx-doc-d{font-size:13.5px;line-height:1.5;color:var(--muted)}
.dx code.dx-code{font-family:'JetBrains Mono',monospace;font-size:.88em;background:var(--surface);border:1px solid var(--border);border-radius:5px;padding:1px 6px;color:var(--tx)}
"""


def render(head, banner, slugs):
    rows = marquee_row(FORMATS[:8], "50s", False) + marquee_row(FORMATS[8:], "44s", True)
    features = "".join([
        feature("For developers and CI", "Host, cache and group behind one URL.",
                "Hosted repositories hold what you publish. Proxy repositories fetch from Maven Central, npm, PyPI, Docker Hub or another Depotex and keep a copy, so builds keep working when the internet doesn't. Group repositories put both behind a single address.",
                [("repositories", "Repositories"), ("upstreams", "Upstreams"), ("repository-groups", "Repository groups")],
                "repositories-list.png", "The repositories list", False),
        feature("For everyone", "Find any version and see what's inside it.",
                "The artifact browser searches every repository you can see. Open a version for its install command, files, dependencies and security status. Depotex reads the SPDX and CycloneDX SBOMs stored with artifacts, finds a component everywhere it's used and checks it against known vulnerabilities from OSV.",
                [("browse", "Browse"), ("sbom", "SBOMs")], "browse-search.png", "Searching across repositories in the artifact browser", True),
        feature("For security teams", "Keep bad versions out, even through proxies.",
                "Quarantine holds new or suspect versions until someone releases them. The block list refuses a version everywhere, including through proxies. Integrity checks confirm every stored file is present and unchanged, and hostile metadata is quarantined on arrival.",
                [("quarantine", "Quarantine"), ("blocklist", "Block list"), ("integrity", "Integrity")], "quarantine.png", "Quarantined versions awaiting release", False),
        feature("For platform teams", "Enforce rules and react to events.",
                "Every major operation is an event. Policies can block, warn about or adjust it before it happens, with a dry run first. Automation sends alerts, webhooks and emails after. Signed plugins add checks, screens and tools for AI agents.",
                [("policies", "Policies"), ("automation", "Automation"), ("plugins", "Plugins")], "policies-editor.png", "Editing a policy", True),
    ])
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in [
        ("Deploy", "Container images, Helm chart"), ("Topology", "One server or a cluster"), ("Database", "PostgreSQL"),
        ("Cache", "Redis, optional on one server, required for a cluster"), ("Files", "Local disk, S3, MinIO or Azure Blob"),
        ("Directories", "Local, LDAP, Active Directory, Entra ID, Google Workspace, SCIM"),
        ("Sign-in", "OpenID Connect, SAML, device sign-in, workload identity"), ("Setup", "Setup wizard or an unattended setup file")])
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
{head}
  <style>{CSS}</style>
</head>
<body>

<div id="vc-header"></div>
<script src="../assets/nav.js"></script>
<script src="assets/nav-local.js"></script>
<script src="../assets/header.js"></script>
{banner}

<main class="dx">
  <section class="dx-hero" style="max-width:1240px;margin:0 auto;padding:clamp(40px,7vw,72px) clamp(20px,5vw,48px) 0;box-sizing:border-box">
    <div style="max-width:820px">
      <div class="dx-pill"><span class="dx-dot"></span><span class="dx-soon">Coming soon</span><span style="width:1px;height:12px;background:var(--amberLine)"></span><span style="font-size:13px;color:var(--body)">In active development</span></div>
      <h1 style="font-size:clamp(40px,6vw,64px);line-height:1.04;font-weight:700;letter-spacing:-.038em;margin:0 0 22px;text-wrap:balance;color:var(--tx)">Every package your teams build and use, on a server you run.</h1>
      <p style="font-size:clamp(17px,2.4vw,20px);line-height:1.6;color:var(--body);margin:0 0 34px;max-width:680px;text-wrap:pretty">Depotex is a self-hosted artifact repository for 18 package formats. It caches the public registries your builds depend on and gives security teams SBOMs, quarantine and policies around every version. Run it on one server or a cluster, with the same features either way.</p>
      <div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">
        <a href="{D}getting-started.html" class="dx-btn">Read Getting Started <span aria-hidden="true">→</span></a>
        <a href="{D}kubernetes.html" class="dx-btn2">Docker &amp; Kubernetes</a>
        <span class="dx-mono dx-muted" style="font-size:13px">Container images · Helm chart · setup wizard</span>
      </div>
    </div>
    <figure style="margin:clamp(40px,6vw,64px) 0 0">
      <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:12px;box-shadow:var(--shadow)">
        <div style="display:flex;align-items:center;gap:6px;padding:2px 6px 12px" aria-hidden="true">
          <span style="width:10px;height:10px;border-radius:50%;background:var(--border)"></span><span style="width:10px;height:10px;border-radius:50%;background:var(--border)"></span><span style="width:10px;height:10px;border-radius:50%;background:var(--border)"></span>
          <span class="dx-mono dx-muted dx-12" style="margin-left:12px">depotex / dashboard</span>
        </div>
        <img src="assets/dashboard-overview.png" alt="The Depotex dashboard: what needs attention, the installation's figures, spaces by size and the health of every part of the system" style="width:100%;height:auto;display:block;border-radius:8px">
      </div>
      <figcaption class="dx-mono dx-muted dx-12" style="margin-top:12px">The dashboard: what needs attention, spaces by size and the health of every part of the system.</figcaption>
    </figure>
  </section>

  <section id="formats" class="dx-sec">
    <div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:24px;margin-bottom:32px">
      <div style="max-width:640px">
        <div class="dx-eyebrow">18 formats</div>
        <h2 class="dx-h2" style="margin-bottom:14px">Works with the tools developers already use.</h2>
        <p class="dx-body" style="overflow-wrap:anywhere">Point your package manager at Depotex and keep your existing commands. Each space has one address per format: <code class="dx-code">/repository/&lt;space&gt;/&lt;format&gt;/</code></p>
      </div>
      <a href="{D}formats.html" style="font-size:15px;font-weight:500">All supported formats →</a>
    </div>
    <div class="dx-marq">{rows}</div>
  </section>

  <section class="dx-sec" style="display:flex;flex-direction:column;gap:clamp(64px,9vw,96px)">{features}</section>

  <section class="dx-sec">
    <div class="dx-eyebrow">How it's organised</div>
    <h2 class="dx-h2" style="margin-bottom:36px;max-width:720px">Spaces hold repositories. Repositories hold versions.</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px">
      <div class="dx-card"><span class="dx-mono dx-muted dx-12">01</span><span class="dx-card-t">Space</span><span class="dx-card-b">Private, internal or public. Viewer, Developer, Maintainer and Owner roles, upload rules, cleanup and quotas.</span></div>
      <div class="dx-card"><span class="dx-mono dx-muted dx-12">02</span><span class="dx-card-t">Repository</span><span class="dx-card-b">One format and one type: hosted, proxy or group.</span></div>
      <div class="dx-card"><span class="dx-mono dx-muted dx-12">03</span><span class="dx-card-t">Version</span><span class="dx-card-b">A component's release, with its files, dependencies, SBOMs and security status.</span></div>
      <div class="dx-card" style="border-color:var(--greenLine);background:var(--greenSoft)"><span class="dx-mono dx-12" style="color:var(--green)">Address</span><span class="dx-mono" style="font-size:14px;font-weight:600;color:var(--tx);overflow-wrap:anywhere">/repository/&lt;space&gt;/&lt;repository&gt;/…</span><span class="dx-card-b">What package managers and CI use. People use the same Depotex in the browser.</span></div>
    </div>
    <p style="font-size:16px;line-height:1.7;color:var(--muted);margin:20px 0 0;max-width:820px">Permissions come from a person's system role and their role in each space. Tokens and applications never do more than the person behind them.</p>
  </section>

  <section class="dx-sec" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:clamp(32px,5vw,56px)">
    <div>
      <div class="dx-eyebrow">For admins</div>
      <h2 class="dx-h2" style="margin-bottom:16px">Runs where you do, and looks after itself.</h2>
      <p class="dx-body dx-mb24">Backups with encryption and test restores, a system check with per-server cluster health, scheduled jobs, an audit log and Prometheus metrics. Recovery mode explains what's wrong when an installed server can't start.</p>
      <div style="display:flex;flex-wrap:wrap;gap:8px 18px;font-size:15px;font-weight:500">
        <a href="{D}deployment-modes.html">Single node &amp; cluster →</a><a href="{D}backups.html">Backups →</a><a href="{D}recovery.html">Recovery mode →</a>
      </div>
    </div>
    <dl class="dx-dl">{dl}</dl>
  </section>

  <section id="editions" class="dx-sec">
    <div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:24px;margin-bottom:32px">
      <div><div class="dx-eyebrow">Editions</div><h2 class="dx-h2">Start with Standard. Add what you need.</h2></div>
      <a href="{D}licensing.html" style="font-size:15px;font-weight:500">Licensing →</a>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:16px">
      <div class="dx-tier"><span class="dx-tier-n">Standard</span><span class="dx-tier-b">Hosted and group repositories in every format, spaces, the artifact browser, users and groups, backups and email.</span></div>
      <div class="dx-tier"><span class="dx-tier-n">Pro</span><span class="dx-mono dx-muted dx-12">Standard, plus</span><span class="dx-tier-b">Proxy repositories, clustering, the system check, the audit log, policies, automation and plugins.</span></div>
      <div class="dx-tier" style="border-color:var(--greenLine)"><span class="dx-tier-n">Enterprise</span><span class="dx-mono dx-12" style="color:var(--green)">Pro, plus</span><span class="dx-tier-b">Single sign-on, quarantine, the block list, branding and managing everyone's API tokens.</span></div>
    </div>
    <p style="font-size:15px;color:var(--muted);margin:16px 0 0">Each feature's page says which tier it needs.</p>
  </section>

  <section id="docs" class="dx-sec">
    <div class="dx-eyebrow">Documentation</div>
    <h2 class="dx-h2" style="margin-bottom:40px">Everything in the docs, by topic.</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,320px),1fr));gap:48px 56px">{docs_groups(slugs)}</div>
  </section>

  <section class="dx-sec" style="padding-bottom:clamp(64px,8vw,96px)">
    <div class="dx-cta" style="border:1px solid var(--border);border-radius:20px;background:var(--surface);padding:clamp(24px,5vw,48px);display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:32px">
      <div style="max-width:620px">
        <div style="display:inline-flex;align-items:center;gap:8px;margin-bottom:16px"><span style="width:7px;height:7px;border-radius:50%;background:var(--amber)"></span><span class="dx-soon">Coming soon</span></div>
        <h2 style="font-size:clamp(26px,3vw,34px);line-height:1.2;font-weight:700;letter-spacing:-.025em;margin:0 0 12px;color:var(--tx)">Install, enter the setup key, and follow the wizard.</h2>
        <p style="font-size:16.5px;line-height:1.65;color:var(--body);margin:0">Then create a space and its first repository, and point your package manager at it.</p>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:12px"><a href="{D}getting-started.html" class="dx-btn">Get started →</a><a href="{D}changelog.html" class="dx-btn2">Changelog</a></div>
    </div>
  </section>
</main>

<div id="vc-footer"></div>
<script src="../assets/footer.js"></script>
</body>
</html>
"""
