"""Depotex doc pages. Placeholder content — expand as features ship.

Each feature page is kept in step with the code in the depotex repo. When a
feature is added or changed there, update its page here and add a line to
CHANGELOG, then run `python3 depotex/_build/build.py`.
"""
from engine import H, P, UL, TABLE, NOTE, STEPS, CODE, WARN, SHOT
from content_scheduler import SCHEDULER
from content_alerts import ALERTS
from content_events import EVENTS
from content_policies import POLICIES
from content_automation import AUTOMATION
from content_plugins import PLUGINS
from content_directories import DIRECTORIES
from content_email import EMAIL
from content_sso import SSO
from content_logging import LOGGING
from content_systemcheck import SYSTEM_CHECK
from content_oauth import OAUTH
from content_branding import BRANDING
from content_spaces import SPACES
from content_groups import GROUPS
from content_upstreams import UPSTREAMS
from content_storage import STORAGE
from content_backups import BACKUPS
from content_integrity import INTEGRITY
from content_quarantine import QUARANTINE
from content_blocklist import BLOCKLIST
from content_vibe import VIBE
from content_sbom import SBOM
from content_reposettings import REPO_SETTINGS
from content_browse import BROWSE
from content_formats import FORMATS
from content_dashboard import DASHBOARD
from content_kubernetes import KUBERNETES
from content_ratelimits import RATE_LIMITS

PLACEHOLDER = NOTE("Placeholder page. Full documentation lands before the public release.")

# Newest first. One line per shipped or changed feature: (date, feature, summary).
# Releases after the initial one, newest first: (date, feature, one-sentence change).
# Only changes people using or running Depotex notice; nothing internal.
CHANGELOG = [
    ("2026-10-14", "Vibe artifacts", "Enterprise: every push is checked: secrets and hidden characters in AI instruction files refuse it, and packages that don't exist or are new, open database rules, lockfile vulnerabilities and risky code show as findings on the check-in's new Findings tab."),
    ("2026-10-14", "Vibe artifacts", "Enterprise: AI coding tools can search, pull, compare and publish vibe projects through the Depotex AI tools (MCP); every publish answers with the check-in's link in the Vibe browser."),
    ("2026-10-14", "Vibe artifacts", "Enterprise: the Vibe browser searches projects, milestones, what changed and screenshot captions, with project and check-in pages, a timeline, a screenshot wall and a zip download of each check-in."),
    ("2026-10-13", "Vibe artifacts", "Enterprise: vibe artifact repositories hold projects pushed as numbered check-ins with files and screenshots; every push answers with a link to the check-in in the Vibe browser."),
    ("2026-10-13", "Vibe artifacts", "Enterprise: turn on vibe artifacts in Settings → Repositories → Vibe artifacts to add the Vibe browser to the menu, beside Browse."),
]

PAGES = [
    ("getting-started", dict(
        label="Getting Started", title="Getting Started", icon="rocket",
        desc="Install Depotex and complete the setup wizard",
        keywords=["install", "setup", "wizard", "first run", "bootstrap", "help", "support", "version", "footer", "about"],
        blocks=[
            P("Depotex is a self-hosted platform. It needs PostgreSQL. Redis is optional for a single node and required for a cluster. On Kubernetes, use the container images and Helm chart: see [Docker & Kubernetes](kubernetes.html)."),
            H("First boot"),
            P("Set `DATABASE_URL` and `CONFIG_ENCRYPTION_KEY`, then start the server. After the first boot the database URL is saved encrypted on the node, so later boots only need the encryption key."),
            H("The setup key"),
            P("A fresh installation starts in setup mode and prints a one-time setup key in its log, in a line like `open the setup wizard … setup_url=https://…/setup?token=…`. Open that URL: setup only proceeds with the key, so nobody else who can reach the server can take it over before you do. The page removes the key from the address bar as soon as it has read it and keeps it only for that browser tab, so it doesn't stay in your history; reloading the tab keeps working, a new tab needs the link again."),
            P("The key changes each time the server restarts. Set `SETUP_TOKEN` to choose it yourself, for example when several nodes share the setup."),
            H("Setup wizard"),
            SHOT("setup-wizard.png", "The setup wizard's first step: the installation ID to request a license with, and the license"),
            STEPS([
                "License|paste the license token issued for this installation.",
                "Database|confirm the PostgreSQL connection.",
                "Storage|choose local, S3, MinIO or Azure.",
                "Cache|add a Redis URL (one server, a Sentinel group or a Redis Cluster: see [Single Node & Cluster](deployment-modes.html#redis)), or skip it for a single node.",
                "Admin user|create the first administrator, or choose **Restore from a backup** to bring back a lost installation (see [Backups → Disaster recovery](backups.html#disaster-recovery)).",
            ]),
            P("Use the language menu at the top of the wizard to set it up in your language. The administrator account you create keeps that language; change it later from the profile menu."),
            P("Credentials entered in the wizard are stored encrypted in the database, not in environment variables."),
            NOTE("`CONFIG_ENCRYPTION_KEY` is required on every start and protects every stored credential. Use a long random value (for example `openssl rand -base64 32`) and keep it somewhere safe: without it the installation cannot start."),
            H("Unattended setup"),
            P("To set up without the wizard — for scripts, containers or configuration management — describe the installation in a YAML file and pass it at first start:"),
            CODE("chmod 600 setup.yaml\nCONFIG_ENCRYPTION_KEY=... ADMIN_PASSWORD=... ./server --setup-config setup.yaml"),
            P("The file has the same sections as the wizard: `database`, `cache`, `storage`, `license` and `admin`. Write secrets as `${VARIABLE}` and pass them in the environment, so they never sit in the file. An example ships as `setup.example.yaml`."),
            UL([
                "The file is only read on a fresh installation. Delete it afterwards.",
                "It must not be readable by other users (`chmod 600`), and unknown keys are rejected so typos don't go unnoticed.",
                "If anything is wrong the server stops with an error explaining what to fix.",
                "Run `./server --machine-id` to get the installation ID for your license request.",
            ]),
            H("Behind a proxy"),
            P("Set `TRUSTED_PROXIES` to the addresses of your load balancer and any other proxy in front of Depotex (IPs or CIDRs, comma-separated). The default trusts only the same host. Client addresses are used for IP allowlists, [rate limits](rate-limits.html) and audit logs: without the right setting, everyone behind the proxy shares one address and one budget."),
            P("**Tell the web frontend a proxy is in front.** Set `FRONTEND_BEHIND_PROXY=true` on the web frontend when a reverse proxy or load balancer in front of it sets `X-Forwarded-For`, `X-Forwarded-Host` and `X-Forwarded-Proto` (Caddy does by default, the nginx example below does, as do Kubernetes ingress controllers and cloud load balancers). The frontend then passes them on to the server. Without it the frontend ignores them, because anyone who reaches its port directly could send their own: every browser then counts as one address for rate limits, the sign-in lockout and the audit log, and repository addresses in package metadata (npm, PyPI) are built from the `Host` header the browser sent. The [Helm chart](kubernetes.html) sets it when its ingress is enabled."),
            WARN("With `FRONTEND_BEHIND_PROXY=true`, only the proxy may reach the frontend's port (3000 by default): a client that reaches it directly can choose the address Depotex sees."),
            P("**Request size.** The web frontend refuses API requests (`/api`) larger than `FRONTEND_API_BODY_LIMIT` bytes with `413 payload_too_large` before they reach the server. The default, `33554432` (32 MiB), is the largest the server takes there: an SBOM upload (`BROWSE_GUARD_MAX_SBOM`). Raise it with `BROWSE_GUARD_MAX_SBOM`, or when `PLUGIN_MAX_PACKAGE_SIZE` goes above 31 MiB. Uploads to repositories, from the browser or a package manager, aren't affected. The proxy must allow bodies at least this large (nginx: `client_max_body_size`)."),
            P("**Route live updates to the backend.** Alerts arrive instantly over a WebSocket at `/api/ws` on the same address as the app. The web frontend can't pass that connection on, so the proxy in front of Depotex must send `/api/ws` (and paths under it) straight to the backend with WebSocket upgrades allowed, and everything else to the frontend:"),
            TABLE(["Path", "Goes to", "Notes"], [
                ["`/api/ws`, `/api/ws/…`", "Backend (port 8080 by default)", "Allow the WebSocket upgrade; keep idle connections open for at least an hour"],
                ["Everything else", "Frontend (port 3000 by default)", ""],
            ]),
            CODE("""# Caddy
depotex.example.com {
    @live path /api/ws /api/ws/*
    reverse_proxy @live 127.0.0.1:8080
    reverse_proxy 127.0.0.1:3000
}

# nginx (inside server { … })
location /api/ws {
    proxy_pass http://127.0.0.1:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_read_timeout 1h;
}
location / {
    proxy_pass http://127.0.0.1:3000;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}"""),
            P("Cloud load balancers (AWS ALB, Azure Application Gateway, Google Cloud Load Balancing) pass WebSockets through; add a path rule for `/api/ws*` to the backend and raise the idle timeout. Without this route nothing breaks: alerts refresh every 30 seconds instead, and the system check shows a **Live updates** warning until it's fixed."),
            H("After an update"),
            P("When Depotex is updated, pages people already have open notice within a few minutes, or as soon as they return to the tab, and show **A new version is available** with **Reload** and **Later**. Nothing reloads on its own, so unsaved work isn't lost. During a rolling upgrade of several servers the message appears once the new version is serving. Proxies and CDNs must not cache the `/app-version` address. It answers anyone, signed in or not, with the build identifier of the running frontend; that is intended (open pages compare it) and it tells nothing else about the installation."),
            H("Security headers"),
            P("Pages are served with security headers (frames from other sites are refused, the referrer is trimmed, HSTS). A Content-Security-Policy is sent in report-only mode by default; violations are logged by the frontend as `[csp]` lines. Set `CSP_ENFORCE=true` on the frontend once the log stays quiet."),
            H("Help menu and footer"),
            P("Once signed in, everyone has a **?** (Help) menu at the top of every page and a footer at the bottom:"),
            TABLE(["Where", "What"], [
                ["**? menu**", "**Documentation**, **Getting started**, **What's new**, **Send feedback**, **Report a bug**, **Contact support**, and **About**"],
                ["**About**", "The version, build, build date and which server answered; **Copy details** copies them, with the page and browser, for a support request"],
                ["**Footer**", "On the left, the version, build and the server that answered the page (with several servers it can change between pages), whether Depotex runs as a cluster or a single server, and a button that copies these details for a support request. On the right, the Documentation, What's new, Support and Report a bug links your administrators set, the language (when more than one is installed), and a switch between the light, dark and high-contrast themes."],
            ]),
            P("Neither is shown on the sign-in page. When **Report a bug** or **Contact support** is an email address, the new message already holds the version and server details."),
            P("**Point the links elsewhere.** Under **Settings → General → Help menu** (`settings:write`, every license tier) set each link to an `https://` address or a `mailto:` email address, for example your own wiki or service desk. Leave a link empty to hide its item, and **Reset to defaults** to go back. Changes raise the `site.help.update` event."),
        ])),

    ("recovery", dict(
        label="Recovery Mode", title="Recovery Mode", icon="shield",
        desc="What happens when an installed server can't start, and how to fix it",
        keywords=["recovery", "troubleshooting", "startup", "database", "redis", "license", "encryption key"],
        blocks=[
            P("If an installed server can't start — the database is down, the encryption key is wrong, Redis or storage is unreachable, the license no longer matches — it doesn't just exit. It starts in recovery mode, finds what's wrong, and shows you how to fix it."),
            H("Open the recovery page"),
            P("The server log shows a line like `open the recovery page … recovery_url=https://…/recovery?token=…`. Open that URL. The key keeps the diagnostics private; set `RECOVERY_TOKEN` to choose it. Like the setup key, it is removed from the address bar once the page has read it."),
            H("What it checks"),
            TABLE(["Check", "Common causes"], [
                ["Bootstrap file", "The server was started with a different CONFIG_ENCRYPTION_KEY, or the file is damaged"],
                ["Database connection", "PostgreSQL is down, unreachable, or its credentials changed"],
                ["Database schema", "An upgrade's migration failed partway"],
                ["Stored configuration", "Wrong encryption key, or the wrong database"],
                ["Redis", "Redis is down or moved"],
                ["File storage", "Directory not writable, bucket missing, credentials expired"],
                ["License", "Expired, or issued for another installation ID (the server moved)"],
            ]),
            H("Fixing it"),
            P("Each failed check lists ways to fix it. Some can be applied from the page — entering a new database or Redis URL, applying a new license, or running without Redis on a single node. The server tests the change, saves it encrypted, and restarts; the page reloads when it's back."),
            WARN("Recovery never changes data on its own. Repairs such as fixing a failed migration are described, not performed — take a backup first."),
            NOTE("The server only enters recovery mode on a machine that was already set up. A brand-new installation always starts the setup wizard."),
        ])),
    ("deployment-modes", dict(
        label="Single Node &amp; Cluster", title="Single Node &amp; Cluster", icon="grid",
        desc="Run Depotex on one node or many with the same features",
        keywords=["cluster", "single node", "redis", "high availability", "scaling"],
        blocks=[
            P("Every Depotex feature works the same on one node or many. What changes is how the nodes coordinate. On Kubernetes, the Helm chart runs the server as a StatefulSet and scales it with `backend.replicas`: see [Docker & Kubernetes](kubernetes.html#clustering)."),
            TABLE(["", "Single node", "Cluster"], [
                ["License", "Standard or higher", "Pro or higher"],
                ["PostgreSQL", "Required", "Required, shared by all nodes"],
                ["Redis", "Optional", "Required, shared by all nodes"],
                ["Storage", "Any backend", "S3, MinIO, Azure, or a shared volume"],
                ["Nodes", "1", "Up to the license limit"],
            ]),
            H("Redis"),
            P("Give Redis as a URL in the setup wizard, the unattended setup file (`cache.redis_url`) or the recovery page. Depotex supports three kinds:"),
            TABLE(["Kind", "URL"], [
                ["One server", "`redis://:password@redis.internal:6379/0`, or `rediss://` for TLS"],
                ["Sentinel group", "`redis+sentinel://:password@s1:26379?master_name=mymaster&addr=s2:26379&addr=s3:26379`: Depotex follows the primary when Sentinel fails over"],
                ["Redis Cluster", "`redis+cluster://:password@n1:6379?addr=n2:6379&addr=n3:6379`: every shard is used"],
            ]),
            UL([
                "Each kind takes TLS (`rediss`, `rediss+sentinel`, `rediss+cluster`), a private certificate authority (`ca_file=/path/ca.pem`) and Redis ACL users (`user:password@`).",
                "Redis coordinates; PostgreSQL keeps the records. If Redis becomes unavailable, Depotex keeps working: each server counts [rate limits](rate-limits.html#redis-and-clusters) on its own, sign-in keeps working, and changes reach other servers within 30 seconds instead of at once. It logs one warning when Redis goes and one message when it returns.",
                "A failover can lose the last few writes to Redis; results stay correct because PostgreSQL holds the records.",
            ]),
            H("Clustering"),
            P("Nodes register themselves, send heartbeats, and elect a leader. **Settings → Clustering** lists every node in a table: status (the leader has a crown), [health](system-check.html#cluster-health), name and machine ID, version, CPU, memory, uptime and last heartbeat. **Cluster health** above the table sums up every server's latest self-check, with **View server** for each thing that needs attention. Select a node to open its identity, resources and recent events below its row, and rename it with the pencil (Pro). A node that stops responding gets a red notice above the table saying how many heartbeats it missed, with **View node**. How clustering works and the environment variables that tune it are explained below the table."),
            TABLE(["Status", "Meaning"], [
                ["**active**", "Running."],
                ["**draining**", "Shutting down: finishing its work before it stops."],
                ["**left**", "Shut down cleanly. Removed from the list after a day (CLUSTER_DEAD_NODE_TTL); a server that starts again with the same identity becomes active again."],
                ["**dead**", "Stopped sending heartbeats (30 seconds by default, longer for the leader) without shutting down cleanly. Also removed after a day."],
            ]),
        ])),

    *KUBERNETES,
    *DASHBOARD,
    *SPACES,
    *GROUPS,
    *FORMATS,
    *BROWSE,
    *UPSTREAMS,
    *REPO_SETTINGS,
    *STORAGE,
    *BACKUPS,
    *INTEGRITY,
    *QUARANTINE,
    *BLOCKLIST,
    *VIBE,
    *SBOM,
    *DIRECTORIES,
    *SSO,
    *OAUTH,
    *BRANDING,
    *LOGGING,
    *SYSTEM_CHECK,
    *EMAIL,
    *SCHEDULER,
    *ALERTS,
    *EVENTS,
    *POLICIES,
    *AUTOMATION,
    *PLUGINS,
    *RATE_LIMITS,
    ("repositories", dict(
        label="Repositories", title="Repositories", icon="briefcase",
        desc="Create and manage artifact repositories",
        keywords=["repositories", "artifacts", "maven", "npm", "pypi", "python", "pip", "docker", "raw", "hosted", "proxy", "group"],
        blocks=[
            P("A repository holds artifacts of one format and belongs to a [space](spaces.html). Its address is `/repository/<space>/<repository>/`, so the name only has to be unique within its space. There are three types: **hosted** (stores what is published to it), **proxy** (fetches from an upstream such as Maven Central and keeps a copy; Pro license or higher) and **group** (combines repositories of the format behind one address; see [Repository groups](repository-groups.html))."),
            H("Create a repository"),
            STEPS([
                "Open the space|Choose **Spaces** in the sidebar, open the space and its **Repositories** tab.",
                "Select New repository|You need the space's **Maintainer** or **Owner** role, or to be a super admin.",
                "Enter a name|2–64 characters: lowercase letters, digits, dots, underscores or hyphens, starting with a letter or digit. It is part of every artifact address and can't be changed later. Format names (`npm`, `maven`, …) are reserved: `/repository/<space>/<format>/` is the space's universal address for that format.",
                "Pick a format and a type|Only the formats the space allows are offered (see [Supported formats](formats.html)); the format can't be changed later. A proxy repository also needs an upstream from the space's list; a group needs its members, in the order they're asked, and the member uploads go to, and can become the space's universal address for the format.",
                "Add a description|optional.",
                "Select Create repository|It appears in the list and can be used at once.",
            ]),
            P("A repository opens on **Browse**, with its address, setup instructions for its package manager and its contents; **Versions**, **Settings** and **Access** are beside it. See [Spaces → Repositories](spaces.html#repositories) for settings, access, upload rules and cleanup."),
            H("Every repository"),
            P("**Repositories** in the sidebar (super admins) lists every repository of the installation, grouped by space: its format, type, whether it can be published to and overwritten, and when it last changed. Filter by format, type, space or name; **Browse** opens a repository in the [artifact browser](browse.html), **Open space** opens its space."),
            SHOT("repositories-list.png", "Repositories: every repository, grouped by space, for administrators"),
            H("Delete a repository"),
            P("Choose the bin next to a repository, in its space or in the list above, and confirm. The repository and everything in it are deleted; this can't be undone. A repository that belongs to a group is taken out of it; if it was where the group's uploads went, the group has no upload target until you choose one."),
            H("Permissions"),
            TABLE(["Permission", "Who has it", "Allows"], [
                ["`spaces:repos:write`", "Space Maintainer and Owner", "Create, change and delete the space's repositories"],
                ["`depot:read`", "Super admins", "See every repository of the installation"],
                ["`depot:write`", "Super admins", "Delete any repository from the list of every repository"],
            ]),
            P("Creating a repository raises the `depot.repository.create` event, so a [policy](policies.html) can restrict names or formats (the **Allowed repository formats** template)."),
        ])),
    ("licensing", dict(
        label="Licensing", title="Licensing", icon="shield",
        desc="License tiers, installation ID and updating a license",
        keywords=["license", "tier", "installation id", "entitlements"],
        blocks=[
            P("A Depotex license is a signed file bound to the installation's ID. Its tier decides which features are available; it can also cap how many people may sign in and how many servers may run."),
            H("Tiers"),
            TABLE(["Tier", "Adds, for example"], [
                ["**Standard**", "Spaces with hosted and group repositories in every format, the artifact browser, users and groups, backups, email and viewing scheduled jobs"],
                ["**Pro**", "Proxy repositories, clustering (several servers), the [system check](system-check.html), the audit log, [policies](policies.html), [automation](automation.html), [plugins](plugins.html), API token IP allowlists and rotation"],
                ["**Enterprise**", "[Single sign-on](single-sign-on.html), [quarantine](quarantine.html), the [block list](blocklist.html), [branding](branding-and-banners.html), [vibe artifacts](vibe-artifacts.html) and managing everyone's API tokens"],
            ]),
            P("Each feature's page says which tier it needs. A feature the license doesn't cover shows what it would need instead of its settings, and its API answers `402 license_required`."),
            P("**Settings → Application → Licensing** (the `licenses:admin` permission) shows the license at a glance: its tier and status, who it's issued to, when it expires, and how many users and servers are in use against its limits (amber from 80%, red at the limit). Below are the features it turns on, its license ID, and the installation ID to quote when requesting a new license (**Copy** puts it on the clipboard)."),
            P("Super admins see a banner at the top when the license expires within 30 days (information, then a warning in the last 14 days and a problem in the last 7), is in its grace period, has expired or isn't valid; its **Update license** button takes you to the update section. `LICENSE_BANNER_DAYS` changes the 30 days (`0` turns the banner off)."),
            H("When a license expires"),
            UL([
                "**Grace period:** a license can allow some days of grace after its expiry date. Everything keeps working; the page and the banner say how many days ago it expired.",
                "**After the grace period**, or with a license that isn't valid (issued for another installation ID, damaged), Depotex only answers sign-in, health checks and the license itself: every other page, API call and package download is refused with `402 license_required` until a valid license is applied. Nothing is deleted.",
                "Apply the renewal as below; it takes effect at once, without a restart.",
            ]),
            H("Updating the license"),
            SHOT("licensing.png", "Settings → Application → Licensing: the license, its features and IDs, and the update section"),
            STEPS([
                "Load the new license|Under **Update license**, select **Upload .json file** (or drop the file on it), or open **Paste the license instead**, paste it and select **Check license**.",
                "Compare|Depotex checks the signature and that the license was issued for this installation, then shows the current and the new license side by side. Changed rows are highlighted, with notes such as how much later it expires, a user or server limit below what's in use now, or features it adds or removes.",
                "Apply|Select **Apply license**, or **Cancel** to keep the current one. The page shows the new license at once.",
            ]),
        ])),

    ("api-tokens", dict(
        label="API Tokens", title="API Tokens", icon="link",
        desc="Scoped tokens for automation and integrations",
        keywords=["api", "token", "automation", "ip allowlist", "rate limit"],
        blocks=[
            P("API tokens let scripts, package managers and integrations call Depotex without a browser session. Each token belongs to a person, carries a chosen set of their permissions, can expire, can be limited to some network addresses, and has its own rate limit. For applications acting for many people, see [OAuth applications](oauth-applications.html)."),
            SHOT("api-tokens.png", "Profile → API tokens: your tokens and your rate limits"),
            H("Create a token"),
            STEPS([
                "Open your API tokens|Open the profile menu (your initials, top right) and choose **API tokens**.",
                "Select New token|Above the list of your tokens.",
                "Name it|Up to 128 characters, for example `CI/CD pipeline`.",
                "Choose its permissions|Only permissions you hold yourself are offered.",
                "Choose when it expires|7, 30, 60, 90, 180 or 365 days, or never. An organization policy can set a shorter maximum.",
                "Optionally, limit where it's used from|Up to 20 IP addresses or ranges (CIDR). Pro license or higher.",
                "Select Create token|Copy the token now: it starts with `dpt_` and is shown only once. Depotex keeps only a hash of it.",
            ]),
            H("Use a token"),
            P("Send it as a bearer token. Tools that only know user names and passwords (Maven, pip, curl `-u`) can send it as the password, with any user name."),
            CODE('curl -H "Authorization: Bearer $DEPOTEX_TOKEN" https://depotex.example.com/api/spaces\ncurl -u ci:$DEPOTEX_TOKEN https://depotex.example.com/repository/platform/tools/scripts/bootstrap.sh'),
            H("Rotate and revoke"),
            UL([
                "**Rotate** gives the token a new secret. The old one keeps working for 60 seconds, so a pipeline can switch without failing. Pro license or higher.",
                "**Revoke** stops a token at once.",
                "Each person may have 25 active tokens unless the organization policy says otherwise.",
            ]),
            H("API description"),
            P("`GET /api/openapi.json` answers an OpenAPI 3.1 description of every `/api` route this server serves, for anyone signed in (with a token or the web app's session). It is built from the running code, so it always matches the server's version. Each operation says what it does, the permission (`x-permission`) and licence tier (`x-tier`) it needs, its error reasons (`x-reasons`), and its request and response bodies; routes not described yet are listed with `x-undocumented`. Routes that answer with a secret, such as creating a token, are marked `x-returns-secret`. Package-format routes (`/repository/…`) aren't in it: each format's page shows its client setup."),
            CODE('curl -H "Authorization: Bearer $DEPOTEX_TOKEN" https://depotex.example.com/api/openapi.json > depotex-openapi.json'),
            H("Rate limits"),
            UL([
                "Each token has its own budget on the API, set by the license: 1,000 requests a minute on Standard, 5,000 on Pro, 10,000 on Enterprise. All of one person's tokens together may make twice that (2,000 / 10,000 / 20,000). Package downloads and uploads have their own, larger budget (20,000 a minute).",
                "A token's requests don't use up its owner's budget in the browser.",
                "Administrators can give one token, or everyone in a role or organization, a different budget: the gauge button on a token, or [Rate limits](rate-limits.html#overrides).",
                "**Profile → API tokens → Your rate limits** shows your budgets.",
                "A token that was never issued counts as a failed sign-in for the address that sent it, so guessing tokens is refused after 20 tries in 15 minutes.",
            ]),
            H("What a token can do"),
            UL([
                "A token can only be given permissions its owner already has. The permission list when creating a token shows every permission you can give, including repository, space and upstream permissions (hover one for what it allows).",
                "A token used to create another token can only give it permissions it has itself.",
                "A token never does more than its owner can do right now. If the owner's role is reduced, their tokens lose the extra permissions immediately.",
                "If the owner is suspended or deactivated, their tokens stop working.",
            ]),
            H("Organization policy"),
            P("With an Enterprise license, administrators with `api_tokens:admin` can set, through the API (`GET`/`PUT /api/admin/tokens/policy`), the longest a new token may live, how many active tokens each person may have, and permissions no token may carry; and list or revoke every token in the organization (`GET /api/admin/tokens`, `DELETE /api/admin/tokens/{id}`). A [policy](policies.html) can also limit tokens on every tier from Pro: the **Maximum API token lifetime**, **Keep permissions out of API tokens** and **API tokens need an IP allowlist** templates."),
            H("IP allowlists behind a proxy"),
            P("If Depotex runs behind a load balancer or reverse proxy, list every proxy in `TRUSTED_PROXIES` so the allowlist sees the real client address. Forwarding headers from anyone else are ignored."),
        ])),

    ("changelog", dict(
        label="Changelog", title="Changelog", icon="history",
        desc="What each release of Depotex includes, newest first",
        keywords=["changelog", "release notes", "whats new"],
        blocks=[
            *([H("Since the initial release"), TABLE(["Date", "Feature", "Change"], [list(row) for row in CHANGELOG])] if CHANGELOG else []),
            H("Initial release"),
            P("The first release of Depotex: a self-hosted artifact repository that runs on a single server or as a cluster, with the same features either way. Later releases are listed above this one as they ship."),
            TABLE(["Area", "What's included"], [
                ["Package formats", "[Maven](maven.html), [npm](npm.html), [PyPI](pypi.html), [Docker and OCI images](docker.html), [Helm](helm.html), [Go](go.html), [NuGet](nuget.html), [Cargo](cargo.html), [APT](apt.html), [YUM](yum.html), [Terraform and OpenTofu](terraform.html), [Hugging Face](huggingface.html), [Git LFS](git-lfs.html), [Composer](composer.html) and [raw files](raw.html), each working with its standard client for downloading and publishing."],
                ["Repositories", "Hosted repositories; [proxy repositories](upstreams.html) that cache Maven Central, npm, PyPI, Docker Hub, internal mirrors or another Depotex; [group repositories](repository-groups.html) that combine them behind one address, with a universal address per format in every space. Write policies, upload rules, cleanup policies, storage quotas and uploads from the browser."],
                ["Spaces and access", "[Spaces](spaces.html) that are private, internal or public, with Viewer, Developer, Maintainer and Owner roles for people, groups and service accounts, per-repository access and content selectors."],
                ["Browsing and search", "The [artifact browser](browse.html): search across every repository you can see, filters, a tree per repository, and a page per version with install commands, files, checksums, dependencies and security status."],
                ["SBOMs and vulnerabilities", "[SBOMs](sbom.html) in SPDX and CycloneDX, stored with artifacts or uploaded for applications from CI; completeness scores, component search everywhere, vulnerability data from OSV, VEX assessments, AI BOMs for models and datasets, and export and sharing."],
                ["Supply-chain controls", "[Quarantine](quarantine.html) rules and manual holds, the [block list](blocklist.html), [integrity checks](integrity.html) of every stored file, and automatic quarantine of unsafe package metadata."],
                ["Policies, automation and plugins", "[Policies](policies.html) that block, warn about or adjust actions, from templates or your own conditions, with dry runs, exemptions and compliance scans; [automation](automation.html) rules that send alerts, webhooks and emails on [events](events.html); signed [plugins](plugins.html), including MCP servers for AI applications and an API explorer."],
                ["Users and sign-in", "[Directories](users-and-directories.html): Local, LDAP, Active Directory, Microsoft Entra ID, Google Workspace and SCIM; [single sign-on](single-sign-on.html) with OpenID Connect and SAML; invitations and password resets by email, sessions and timeouts, CAPTCHA, lockout after failed attempts, anonymous access, and GDPR data export and anonymization."],
                ["Applications and tokens", "[OAuth applications](oauth-applications.html) with consent, device sign-in for command-line tools, service accounts and workload identity for CI; [API tokens](api-tokens.html) with permissions, expiry, IP allowlists and rotation; [rate limits](rate-limits.html), overrides and download quotas."],
                ["Notifications", "In-app [alerts](alerts.html) with the bell, a notifications page and preferences; [email](email.html) through SMTP providers or the Amazon SES API with an IAM role; [banners](branding-and-banners.html) for announcements."],
                ["Administration", "The [dashboard](dashboard.html), the [system check](system-check.html) and cluster health, [scheduled jobs](scheduler.html), log levels, log files and exports, the [audit log](logging-and-audit.html), profiling, Prometheus [metrics](monitoring.html), [branding](branding-and-banners.html) per theme and your own help links."],
                ["Backups and recovery", "[Backups](backups.html) on a schedule or on demand, encrypted, kept on a separate target, checked and test-restored; restore into a new installation from the setup wizard; [recovery mode](recovery.html) when an installed server can't start."],
                ["Installation", "A [setup wizard](getting-started.html) or an unattended setup file; [container images and a Helm chart](kubernetes.html); a [single server or a cluster](deployment-modes.html) with Redis as one server, Sentinel or Redis Cluster; [storage](storage.html) on a local disk, S3 (with IAM roles), MinIO or Azure Blob."],
            ]),
        ])),
]
