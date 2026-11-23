"""Wiki admin guide: installing, setting up, licensing and running the Wiki,
and the settings only the Wiki has (analytics, calendar feeds, imports, Q&A
moderation, anonymous readers, search engines). Platform parts are adapted
from depotex/_build (content.py, content_admin.py, content_setup.py,
content_envvars.py, content_access.py, content_help.py) with everything
Depotex-only left out. Facts come from apps/wiki and libs/platform in the
depotex repo; keep in step with them."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, CODE, SHOT

SUPPORT_MAIL = "support@vectored.dev"
ACCESS_NOTE = NOTE("The Wiki isn't released yet. Early adopters: [contact us for access](../../support.html?tool=wiki&type=access) to get the server and a licence.")
T = ["Variable", "Default", "Meaning"]

ADMIN_WIKI = [
    # ------------------------------------------------------------------ index
    ("index", dict(
        label="Admin guide", title="Wiki Admin Guide", icon="book",
        desc="Install, license, configure, secure and run the Wiki: everything administrators and operators need",
        keywords=["admin", "administrator", "operator", "install", "configure", "super admin", "organization admin", "runbook"],
        blocks=[
            P("This guide is for the people who install and run the Wiki: platform and infrastructure engineers, the Wiki's super admins and organization admins, and security teams. People who read and write pages need the [user guide](getting-started.html) instead. Pages both need, such as spaces, API tokens and the changelog, are in both guides."),
            ACCESS_NOTE,
            H("From nothing to production"),
            STEPS([
                "Plan|Choose a single server or a cluster, and size PostgreSQL, Redis and file storage. [Plan an installation](install-planning.html), [Sizing & performance](sizing.html)",
                "Install|Start the server and the web app, and put a reverse proxy in front that sends `/api` to the server. [Install the Wiki](install.html)",
                "License|Read the installation ID and request a licence. [Licensing](licensing.html)",
                "Set up|In the [setup wizard](setup-wizard.html), or [without the UI](headless-setup.html) from a YAML file.",
                "Configure|The Wiki's address, email, directories and single sign-on, storage. [Settings reference](settings-reference.html)",
                "Decide what's public|Anonymous readers, public spaces and questions, and what search engines may index. [Anonymous access](anonymous-access.html), [Search engines](search-engines-and-robots.html)",
                "Secure|Work through the [production checklist](security-hardening.html).",
                "Operate|Backups, the system check, monitoring, alerts and [upgrades](upgrades.html).",
            ]),
            H("Who administers what"),
            TABLE(["Role", "Can", "Typical person"], [
                ["**Super admin**", "Everything: installation settings, licence, storage, backups, plugins, every space, labels; only super admins create spaces", "Platform team"],
                ["**Organization admin**", "People, groups, roles and policies of their organization; moderates its Q&A", "Team or department lead"],
                ["**Space admin**", "A space's members, settings, imports and deletion", "Team that owns the space"],
                ["**Operator** (no role in the Wiki)", "The servers, PostgreSQL, Redis, storage, the reverse proxy and the environment", "Infrastructure / SRE"],
            ]),
            P("[How access fits together](access-overview.html) shows how system roles, groups and space roles combine."),
            H("In this guide"),
            TABLE(["Section", "Pages"], [
                ["Install", "[Plan an installation](install-planning.html) · [Sizing & performance](sizing.html) · [Install the Wiki](install.html) · [Single server & cluster](deployment-modes.html) · [Environment variables](environment-variables.html)"],
                ["Set up", "[Setup wizard](setup-wizard.html) · [Set up without the UI](headless-setup.html) · [Licensing](licensing.html) · [Recovery mode](recovery.html)"],
                ["Configure", "[Settings reference](settings-reference.html) · [How access fits together](access-overview.html) · [Users & directories](users-and-directories.html) · [Single sign-on](single-sign-on.html) · [OAuth applications](oauth-applications.html) · [API tokens](api-tokens.html) · [Rate limits](rate-limits.html) · [Storage](storage.html) · [Email](email.html) · [Branding](branding-and-banners.html)"],
                ["Spaces & content", "[Spaces](spaces.html) · [Analytics](analytics-settings.html) · [Calendar feeds](calendar-feeds.html) · [Imports](confluence-import.html) · [Q&A moderation](qna-moderation.html)"],
                ["Kee (AI)", "[Set up Kee](kee-setup.html) · [Providers & models](kee-providers.html) · [Features & permissions](kee-access.html) · [Limits & usage](kee-limits.html) · [Data handling & privacy](kee-data.html) · [Outside AI apps](kee-outside-apps.html) · [Scheduled help](kee-scheduled-help.html) · [What Kee can do](kee-tools.html)"],
                ["Security", "[Production checklist](security-hardening.html) · [Anonymous access](anonymous-access.html) · [Search engines](search-engines-and-robots.html) · [Policies](policies.html) · [Logging & audit](logging-and-audit.html) · [Personal data](personal-data.html)"],
                ["Operate", "[System check](system-check.html) · [Alert tuning](alert-tuning.html) · [Monitoring](monitoring.html) · [Backups](backups.html) · [Upgrades](upgrades.html) · [Scheduled jobs](scheduler.html) · [Managing alerts](alerts-admin.html) · [Events](events.html) · [Automation](automation.html) · [Plugins](plugins.html)"],
                ["Help", "[Known issues](known-issues.html) · [FAQ](faq.html) · [Support](support.html) · [Changelog](changelog.html)"],
            ]),
            H("Getting help"),
            P("Licences, renewals and questions: [vectored.dev/#contact](https://vectored.dev/#contact) or **" + SUPPORT_MAIL + "**. For a problem with a running installation, [Support](support.html) says what to send so it can be answered the first time."),
        ])),

    # ------------------------------------------------------- install-planning
    ("install-planning", dict(
        label="Plan an installation", title="Plan an installation", icon="grid",
        desc="Components, requirements, sizing, network and storage to decide before installing the Wiki",
        keywords=["requirements", "system requirements", "sizing", "capacity", "hardware", "postgresql version", "redis", "s3", "ports", "firewall", "network", "architecture", "high availability"],
        blocks=[
            P("The Wiki is two programs, the **server** (the API, live editing, background jobs) and the **web app**, in front of PostgreSQL, optional Redis and file storage. Decide these before installing: they're the parts that are hard to change later."),
            H("Components"),
            TABLE(["Part", "Role", "Notes"], [
                ["Server", "Every API request, live editing sessions, scheduled jobs (imports, analytics, scheduled publishing), events, plugins", "Port 8080. Stateless apart from a small per-server data folder. Several servers form a cluster"],
                ["Web app", "The pages people use; forwards `/api` to the server", "Port 3002 by default. Stateless; run two or more for availability"],
                ["PostgreSQL", "Every record: people, settings (encrypted), spaces, pages and their versions, comments, Q&A, calendars, analytics, the audit log", "Required. The single source of truth"],
                ["Redis", "Coordination between servers: rate limits, live updates", "Optional on one server, required for a cluster. See [Single server & cluster](deployment-modes.html)"],
                ["File storage", "Images and videos on pages, imports while they run, logos, avatars and plugin packages", "Local disk, S3 (or S3-compatible), MinIO or Azure Blob"],
                ["Reverse proxy", "TLS, the public address, compression, `/api` to the server", "Any proxy or load balancer; examples for Caddy and nginx in [Install the Wiki](install.html)"],
            ]),
            NOTE("How much CPU and memory each part needs for your number of people: [Sizing & performance](sizing.html)."),
            H("Single server or cluster"),
            TABLE(["", "Single server", "Cluster"], [
                ["Licence", "Standard or higher", "Pro or higher, with enough servers"],
                ["Redis", "Optional", "Required (one server, Sentinel or Redis Cluster)"],
                ["Storage", "Any", "Shared by every server: S3, MinIO, Azure, or one volume mounted at the same path everywhere"],
                ["Availability", "Downtime for restarts and upgrades", "Rolling upgrades; a failed server's work is taken over"],
            ]),
            P("Every feature behaves the same either way, live editing included: two people on different servers edit the same page together. Start with one server if you're unsure: going to a cluster later means adding Redis (in **Settings → Clustering → Redis**, then a restart) and shared storage, not reinstalling."),
            H("PostgreSQL"),
            UL([
                "A supported PostgreSQL release, 15 or later. Managed services (Amazon RDS and Aurora PostgreSQL, Google Cloud SQL, Azure Database for PostgreSQL) work.",
                "One database for the Wiki, owned by the role the Wiki connects as. The role needs `CREATEROLE` if plugins use databases, and must not be a superuser.",
                "Connections: each server opens up to `pool_max_conns` (default 4, or the number of CPUs if more). Keep servers × `pool_max_conns` plus room for maintenance under `max_connections`.",
                "Page views are kept month by month; on a busy installation the database grows with readers (see [Analytics](analytics-settings.html) for what is kept and for how long).",
                "Use TLS (`sslmode=verify-full`) when the database isn't on the same host, and back it up with your platform's tools as well as with the Wiki's [backups](backups.html).",
                "The Wiki's [backups](backups.html) run `pg_dump` and `pg_restore` on the server: install the PostgreSQL client tools on each server host, at least as new as the database server.",
            ]),
            H("Storage"),
            UL([
                "Size it for the images and videos people put on pages: images are up to 20 MiB each, videos up to 200 MiB. An import keeps its upload in storage until it ends (2 GiB per export by default).",
                "Object storage (S3, MinIO, Azure) is the usual choice and the only one that needs nothing extra for a cluster. On AWS the server can use its IAM role instead of keys.",
                "Each server also has a small **data folder** of its own: the encrypted bootstrap file and its log files. Give it persistent disk.",
            ]),
            H("Network"),
            TABLE(["From", "To", "Port", "Why"], [
                ["People", "Reverse proxy", "443", "The web app and the API, on one host name"],
                ["Calendar apps", "Reverse proxy", "443", "[Calendar feeds](calendar-feeds.html), without signing in"],
                ["Reverse proxy", "Web app", "3002", "Pages, scripts and styles: everything except `/api`"],
                ["Reverse proxy", "Server", "8080", "`/api`: the API, and live editing and alerts (WebSocket) under `/api/ws`"],
                ["Web app", "Server", "8080", "What the web app asks for itself, and API calls that reach it instead of the server"],
                ["Server", "PostgreSQL, Redis, storage", "5432, 6379, 443/9000", "Its records, coordination and files"],
                ["Servers", "Each other", "none", "Servers coordinate through PostgreSQL and Redis only"],
            ]),
            P("**Outbound from the server**, only for what you use: identity providers (single sign-on, Entra ID, Google), SMTP or Amazon SES, webhook targets, plugins' declared hosts, and the model providers you connect for [Kee](kee-providers.html#network). Videos embedded from YouTube, Vimeo or the sites you allow are played by the reader's browser, not fetched by the server."),
            H("Address and TLS"),
            UL([
                "Give the Wiki its own host name (`https://wiki.example.com`); it can't be served under a path.",
                "Terminate TLS at your proxy. Single sign-on and calendar apps need HTTPS in practice.",
                "Set `TRUSTED_PROXIES` on the server to your proxy's address (and `FRONTEND_BEHIND_PROXY=true` on the web app), or every request seems to come from the proxy.",
                "Don't limit request bodies under `/api` at the proxy (the server does), or allow at least 201 MiB, so videos up to 200 MiB can be uploaded (see [Install the Wiki](install.html)).",
            ]),
            H("Before you install"),
            UL([
                "PostgreSQL database and role created; Redis ready if you run a cluster; bucket or container created.",
                "DNS name and TLS certificate.",
                "A place to keep secrets: `CONFIG_ENCRYPTION_KEY`, the first administrator's password, the setup and recovery keys.",
                "Who will request the licence, and with which tier, user and server counts (see [Licensing](licensing.html)).",
                "Email (SMTP or Amazon SES) for invitations and password resets.",
                "Your identity source: local accounts, LDAP or Active Directory, Entra ID, Google Workspace, SCIM, and single sign-on.",
                "Whether anything will be public: public spaces and questions need [anonymous access](anonymous-access.html).",
            ]),
        ])),

    # ------------------------------------------------------------- sizing
    ("sizing", dict(
        label="Sizing & performance", title="Sizing & performance",
        icon="activity",
        desc="How much CPU and memory the Wiki needs, from a team of 50 to 100,000 people, and the load test results behind the numbers",
        keywords=["sizing", "capacity", "performance", "load test", "benchmark", "hardware", "cpu", "memory", "ram", "how many users", "concurrent users", "scaling", "100000 users", "postgresql size", "replicas"],
        blocks=[
            P("How big the servers, the web app and PostgreSQL should be for the number of people who use the Wiki. The numbers come from load tests of the current release (results at the end of this page); start from the table for your size, then watch the real load and adjust."),
            H("How to read the numbers"),
            UL([
                "**People** is everyone with an account who uses the Wiki. **Active at peak** is how many of them have the Wiki open and are clicking through pages at the busiest moment of the day. For a company wiki that is usually 5–10% of the people; the tables use **10%**, so most installations have room to spare.",
                "An active person in the tests opens a page every 10 seconds on average and keeps a tab open with its live connection. Someone reading a long page for a few minutes costs less.",
                "The tables size for about **half** the CPU at peak, so a spike, a large import or a server restart doesn't slow everyone down.",
                "Every part scales out: more servers (a [cluster](deployment-modes.html), Pro), more web app processes behind your proxy, and a bigger PostgreSQL.",
            ]),
            H("What one active person costs"),
            TABLE(["Part", "Per 1,000 active people", "Notes"], [
                ["Web app", "About **0.2 CPU** with `/api` routed to the server; 150 MB per process", "It draws the pages only. One process can't use more than about one CPU; run one per CPU behind the proxy. If API calls go through the web app instead, it needs about **1.9 CPU** per 1,000 active people"],
                ["Server", "About **0.3 CPU** and 150 MB, plus about 200 MB for the server itself", "Measured up to 3,500 active people on one CPU"],
                ["PostgreSQL", "About **0.3 CPU**", "Plus memory for the data people read most (see below)"],
                ["Redis", "Small (well under 0.1 CPU)", "Only for a cluster"],
            ]),
            H("Recommended sizes"),
            TABLE(["People", "Active at peak", "Servers", "Web app", "PostgreSQL", "Redis"], [
                ["Up to 500", "50", "1 × 1 CPU, 1 GB", "1 process, 1 CPU, 1 GB", "2 CPU, 4 GB", "—"],
                ["2,000", "200", "1 × 1 CPU, 1 GB", "1 process (2 for availability)", "2 CPU, 4 GB", "—"],
                ["5,000", "500", "1 × 2 CPU, 2 GB (2 for availability)", "2 processes, 1 CPU, 1 GB each", "2 CPU, 8 GB", "Cluster only"],
                ["10,000", "1,000", "2 × 2 CPU, 2 GB", "2 processes", "4 CPU, 16 GB", "1 CPU, 1 GB"],
                ["25,000", "2,500", "2 × 2 CPU, 4 GB", "3 processes", "8 CPU, 32 GB", "1 CPU, 2 GB"],
                ["50,000", "5,000", "3 × 2 CPU, 4 GB", "4 processes (2 hosts × 2 CPU)", "8 CPU, 32 GB, a standby replica", "2 CPU, 2 GB, Sentinel"],
                ["100,000", "10,000", "4 × 2 CPU, 4 GB", "8 processes (2 hosts × 4 CPU)", "16 CPU, 64 GB, a standby replica", "2 CPU, 4 GB, Sentinel"],
            ]),
            P("Up to about 2,000 people everything can share one machine of 4 CPU and 8 GB (server, web app and PostgreSQL), as long as it is backed up. From 5,000 people, give PostgreSQL its own machine or use a managed database. A cluster needs the Pro licence, Redis and shared storage; see [Single server & cluster](deployment-modes.html)."),
            NOTE("The web app column assumes your proxy sends `/api` straight to the server (see [Install the Wiki](install.html)). Without that route every API call passes through the web app, which then needs about ten times as many processes."),
            NOTE("If more of your people are active at once (for example everyone opens the Wiki at 9 a.m. for a stand-up), size by the number of active people you expect, not by the number of accounts."),
            H("Settings that matter at scale"),
            UL([
                "**Memory limit.** Give each server at least 1 GB and set `GOMEMLIMIT` to about 80% of its memory limit (for example `GOMEMLIMIT=800MiB` for 1 GB). A server that runs out of CPU queues requests and its memory grows; past its limit it is stopped. Keep peak CPU at about half and add servers before that.",
                "**Database connections.** Each server opens `pool_max_conns` connections (default 4, or the number of CPUs if more). The default carried 3,500 active people per server CPU in the tests. Raise it at a server's first start, in `DATABASE_URL` (`…?pool_max_conns=16`), only when PostgreSQL has CPUs to spare, and keep servers × `pool_max_conns` plus 20 under PostgreSQL's `max_connections`.",
                "**PostgreSQL CPUs.** Give PostgreSQL at least as many CPUs as the servers together: in the tests it needed as much CPU as the server did.",
                "**PostgreSQL memory.** Enough to keep the pages, versions and people that are read most in memory: `shared_buffers` about a quarter of its memory. The test database (2,000 people, 2,100 pages) was 31 MB; a page with its versions and analytics takes about 15 KB on average, so 100,000 pages with history is roughly 2–5 GB, plus page views (kept month by month, see [Analytics](analytics-settings.html)).",
                "**API traffic.** Send `/api` from the proxy straight to the server, not through the web app (see [Behind a proxy](install.html)). A call passed on by the web app costs it about ten times the CPU the server spends answering it; in the tests, routing `/api` directly cut the web app's CPU from 1.9 to 0.2 CPU per 1,000 active people. The sizes above assume this route.",
                "**Web app processes.** Run one process per CPU on each host and spread them behind the proxy. Compress responses at the proxy (gzip or Brotli), and let it cache `/_next/static/` for a long time: those files never change within a release.",
                "**The live connection.** Every open tab holds one WebSocket on `/api/ws`, and editors one more for the page they edit. Allow enough open files for them on each server (`LimitNOFILE` in systemd, `ulimits` in a container): at least 4 × the active people you expect per server.",
                "**Rate limits.** The default limits suit the sizes above. Behind a proxy, set `TRUSTED_PROXIES` so limits apply to each person's address, not the proxy's (see [Rate limits](rate-limits.html)).",
            ]),
            H("Watching the load"),
            UL([
                "**Settings → Clustering** shows each server's CPU and memory; the [system check](system-check.html) warns when one is unhealthy.",
                "[Monitoring](monitoring.html) gives Prometheus metrics for request rates, live editing and the server process. Add a server when peak CPU stays above about 60%, or when page loads in your monitoring slow down.",
                "Watch the web app's CPU separately, above all if API calls pass through it.",
            ]),
            H("Load test results"),
            P("The numbers above come from these tests, run on 20 November 2026 against the current release. They are a guide for planning, not a promise: your pages, plugins and habits differ."),
            TABLE(["Setting", "Value"], [
                ["Machine", "One 4-CPU cloud machine; each part pinned to its own CPUs and limited like a container (`--cpus`, `--memory`)"],
                ["Data", "2,000 people, 17 spaces, 2,100 pages made from the ready-made templates (720 published)"],
                ["People", "Signed in, a tab open with its live connection, a new page every 10 s on average: 60% reading pages, 10% space overviews, 8% the dashboard, 8% search, 4% editing (editors open the live editor), the rest the spaces list, Q&A, history and blogs. One view in five is a full page load"],
                ["Pass", "95% of page loads (all of a screen's requests) within 1.5 seconds, under 1% of requests failing"],
                ["Not included", "Typing in the editor, uploads, imports and exports; static files the browser caches"],
            ]),
            P("**The server alone** (requests straight to the server, PostgreSQL on two CPUs):"),
            TABLE(["Server limit", "Active people that passed", "Page views per second", "Requests per second", "Page load, 95%", "Server CPU used", "Server memory", "PostgreSQL CPU used"], [
                ["0.5 CPU, 512 MB", "1,500", "150", "1,520", "0.15 s", "0.44", "213 MB", "0.45"],
                ["1 CPU, 1 GB", "3,000", "300", "2,980", "0.26 s", "0.84", "362 MB", "0.89"],
                ["1 CPU, 1 GB", "3,500 (limit)", "332", "3,330", "1.3 s", "0.92", "562 MB", "0.91"],
            ]),
            P("**With the web app** in front and `/api` routed straight to the server (pages from one web app process limited to 1 CPU and 1 GB, the server at 1 CPU, PostgreSQL on one CPU):"),
            TABLE(["Active people", "Page views per second", "Page load, 95%", "Web app CPU used", "Web app memory", "Server CPU used"], [
                ["500", "50", "0.04 s", "0.11", "121 MB", "0.16"],
                ["1,000", "100", "0.04 s", "0.21", "129 MB", "0.32"],
                ["1,500", "150", "0.06 s", "0.30", "131 MB", "0.45"],
                ["2,000", "200", "0.12 s", "0.38", "137 MB", "0.61"],
            ]),
            P("At twice that load (240 page views a second) the server and PostgreSQL, sharing the test machine, ran short first; the web app was at 0.43 CPU. The test had 2,000 accounts, so the web app's own limit is above that."),
            P("**Every request through the web app** (no `/api` route at the proxy; same limits):"),
            TABLE(["Active people", "Page views per second", "Page load, 95%", "Web app CPU used", "Web app memory", "Server CPU used"], [
                ["100", "10", "0.11 s", "0.21", "147 MB", "0.05"],
                ["200", "20", "0.16 s", "0.43", "150 MB", "0.09"],
                ["300", "30", "0.19 s", "0.61", "157 MB", "0.12"],
                ["400", "40", "0.36 s", "0.78", "173 MB", "0.15"],
                ["500 (over the limit)", "48", "2.0 s", "0.93", "176 MB", "0.16"],
            ]),
            UL([
                "The server's cost grows in a straight line with the number of people until its CPU is used up; then page loads slow down within seconds. Plan for half.",
                "Forwarding a request costs the web app about ten times what answering it costs the server, so route `/api` to the server. Pages now carry only the text their screen needs (about 46 KB, 13 KB compressed, down from 177 KB); the rest loads once as files the browser caches.",
                "A server that ran out of CPU and memory together was stopped by its memory limit instead of slowing down: set `GOMEMLIMIT` and keep headroom (above).",
                "No screen asks the server for the same thing twice: a browser check of 24 screens found one repeated request (the space overview's \"Start here\" list), now fixed.",
            ]),
        ])),

    # ---------------------------------------------------------------- install
    ("install", dict(
        label="Install the Wiki", title="Install the Wiki", icon="rocket",
        desc="Start the server and the web app, the setup key, the reverse proxy with its WebSocket paths, and request sizes",
        keywords=["install", "setup", "first run", "bootstrap", "proxy", "nginx", "caddy", "websocket", "live editing", "request size", "413", "help menu", "early access"],
        blocks=[
            ACCESS_NOTE,
            P("The Wiki is self-hosted: a server program and a web app, in front of PostgreSQL, optional Redis and file storage. Before you start, [plan the installation](install-planning.html). There are no container images or Helm chart for the Wiki yet: run the two programs as services on your own hosts or in your own containers."),
            H("The two programs"),
            TABLE(["Program", "Listens on", "Needs"], [
                ["Server (`wiki-server`)", "`PORT` (8080) on `BIND_ADDR` (127.0.0.1)", "`CONFIG_ENCRYPTION_KEY` on every start; `DATABASE_URL` on its first start"],
                ["Web app", "Port 3002", "`BACKEND_URL`, where the server is (default `http://127.0.0.1:8080`)"],
            ]),
            P("Keep the default `BIND_ADDR` when the web app and the proxy run on the same host as the server; set `0.0.0.0` (or a private address) when they don't."),
            H("First boot"),
            P("Set `DATABASE_URL` and `CONFIG_ENCRYPTION_KEY`, then start the server. After the first boot the database URL is saved encrypted on the server, so later boots only need the encryption key."),
            CODE("export CONFIG_ENCRYPTION_KEY=\"$(cat /run/secrets/wiki-encryption-key)\"\nexport DATABASE_URL='postgres://wiki:…@db.internal:5432/wiki?sslmode=verify-full'\n./wiki-server"),
            NOTE("`CONFIG_ENCRYPTION_KEY` is required on every start and protects every stored credential. Use a long random value (for example `openssl rand -base64 32`), the same on every server, and keep it somewhere safe: without it the installation can't start."),
            H("The setup key"),
            P("A fresh installation starts in setup mode and prints a one-time setup key in its log, in a line like `open the setup wizard … setup_url=https://…/setup?token=…`. Open that address: setup only proceeds with the key, so nobody else who can reach the server can take it over first. The page removes the key from the address bar as soon as it has read it. The key changes on every restart; set `SETUP_TOKEN` to choose it yourself."),
            P("The [setup wizard](setup-wizard.html) then asks for the licence, the database, storage, the optional Redis cache and the first administrator. To set up with nobody at a browser, see [Set up without the UI](headless-setup.html)."),
            H("Behind a proxy"),
            P("Set `TRUSTED_PROXIES` on the server to the addresses of your load balancer and any other proxy in front (IPs or CIDRs, comma-separated). Client addresses are used for IP allowlists, [rate limits](rate-limits.html), the audit log and the per-address limits on anonymous readers and calendar feeds: without the right setting, everyone behind the proxy shares one address and one budget."),
            P("Set `FRONTEND_BEHIND_PROXY=true` on the web app when the proxy in front of it sets `X-Forwarded-For`, `X-Forwarded-Host` and `X-Forwarded-Proto` (Caddy does by default, the nginx example below does). The web app then passes them on to the server. Without it they're ignored, because anyone who reaches the web app's port directly could send their own."),
            WARN("With `FRONTEND_BEHIND_PROXY=true`, only the proxy may reach the web app's port: a client that reaches it directly can choose the address the Wiki sees."),
            H("Route the API to the server"),
            P("Everything under `/api` is answered by the server: the API the pages call, and the WebSockets under `/api/ws` for live editing and instant alerts (each page being edited has its own connection at `/api/ws/spaces/<space>/pages/<page>/collab`). Have the proxy send `/api` and everything under it straight to the server, with WebSocket upgrades allowed, and everything else to the web app:"),
            TABLE(["Path", "Goes to", "Notes"], [
                ["`/api`, `/api/…`", "Server (port 8080)", "Allow the WebSocket upgrade; keep idle connections open for at least an hour; no body limit of the proxy's own"],
                ["Everything else", "Web app (port 3002)", "Pages, scripts and styles"],
            ]),
            CODE("""# Caddy
wiki.example.com {
    encode zstd gzip
    @api path /api /api/*
    reverse_proxy @api 127.0.0.1:8080
    reverse_proxy 127.0.0.1:3002
}

# nginx (inside server { … })
gzip on;
gzip_proxied any;
gzip_types application/json application/javascript text/css text/plain image/svg+xml;
location /api/ {
    proxy_pass http://127.0.0.1:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;  # map $http_upgrade $connection_upgrade { default upgrade; '' ''; } in http { … }
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_read_timeout 1h;        # live connections stay open
    client_max_body_size 0;       # the server applies its own limits
    proxy_request_buffering off;
}
location / {
    proxy_pass http://127.0.0.1:3002;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}"""),
            P("The server sets the security headers of API responses itself and refuses requests that are too large, so it is safe to reach this way. It doesn't compress: turn compression on at the proxy, as in the examples."),
            NOTE("The web app can pass API calls on too, and does when a request for `/api` reaches it. That keeps an installation without this route working, with two limits: WebSockets can't pass, so the route for `/api/ws` is the least a proxy needs, and every call uses the web app's CPU, which is the first thing to run out as more people use the Wiki. Route all of `/api` unless you have a reason not to."),
            WARN("Without a route for `/api/ws`, the editor can't connect: after three tries it says so, and people can't edit pages together. Alerts still arrive, every 30 seconds instead of at once, and the system check shows a **Live updates** warning until it's fixed."),
            P("Cloud load balancers (AWS ALB, Azure Application Gateway, Google Cloud Load Balancing) pass WebSockets through: add a path rule for `/api/*` to the server and raise the idle timeout."),
            P("A proxy on another host than the server must be in the server's `TRUSTED_PROXIES`: the server removes `X-Forwarded-For`, `X-Forwarded-Host`, `X-Forwarded-Proto` and `X-Real-IP` from any sender that isn't listed. The system check's **Forwarded headers** line on each server says when that happened and from which address."),
            H("Kee answers through the proxy"),
            P("[Kee](kee-setup.html) sends its answers word by word as an event stream (`text/event-stream`). The server marks these answers `Cache-Control: no-cache, no-transform` and `X-Accel-Buffering: no`, which nginx honours, and Caddy passes event streams on at once. If your proxy or load balancer buffers or compresses responses another way, turn that off for event streams under `/api`, or answers arrive all at once at the end and long ones may time out. Keep the read timeout at least 10 minutes (the examples keep an hour)."),
            H("Request size"),
            P("The server refuses API requests larger than 32 MiB with `413 payload_too_large`, also when they arrive in chunks. Uploads to a page (images and videos) have their own limit of 201 MiB, enough for a 200 MiB video. With `/api` routed to the server, let the proxy take bodies of any size there (nginx: `client_max_body_size 0` in that location) and leave the limits to the server. API requests that go through the web app are checked there first, against `FRONTEND_API_BODY_LIMIT` bytes (32 MiB by default; page uploads 201 MiB whatever that variable says)."),
            H("Logs and secrets in addresses"),
            P("Calendar apps read a person's [calendar feed](calendar-feeds.html) with its secret in the address, because they can't send headers. The Wiki's server never logs request queries, but a proxy in front may: leave queries out of your proxy's access log for `/api/calendar/ical`, or keep that log as private as the feeds."),
            H("After an update"),
            P("When the Wiki is updated, pages people already have open notice within a few minutes, or as soon as they return to the tab, and show **A new version is available** with **Reload** and **Later**. Nothing reloads on its own. Proxies and CDNs must not cache the `/app-version` address."),
            H("Security headers"),
            P("Pages are served with security headers (frames from other sites are refused, the referrer is trimmed, HSTS) and an enforced Content-Security-Policy; violations are logged by the web app as `[csp]` lines (`CSP_ENFORCE=false` sends it report-only). Pages may frame videos only from the sites allowed in **Settings → Security → Video sites**. [HTML blocks](macros.html#html-blocks) run in a sandboxed frame with a policy of their own: they can reach only the sites in **Settings → Security → HTML blocks**, and never the Wiki itself. HTML [slide decks](slides.html) run under the same kind of policy, with the hosts in **Settings → Security → Slides**."),
            NOTE("The Wiki needs its own host name: it can't be served under a path such as `https://tools.example.com/wiki/`."),
            H("Help menu and footer"),
            P("Once signed in, everyone has a **?** (Help) menu at the top of every page and a footer at the bottom with the version, build and the server that answered. Out of the box, **Documentation**, **Getting started** and **What's new** open these docs, and **Report a bug** and **Contact support** reach Vectored. Point them at your own help desk under **Settings → General → Help menu** (`settings:write`), or leave a link empty to hide it."),
        ])),

    # ------------------------------------------------------- deployment-modes
    ("deployment-modes", dict(
        label="Single server &amp; cluster", title="Single server &amp; cluster", icon="server",
        desc="Run the Wiki on one server or many with the same features",
        keywords=["cluster", "single node", "single server", "redis", "high availability", "scaling", "sentinel", "redis cluster", "live editing"],
        blocks=[
            P("Every feature of the Wiki works the same on one server or many. What changes is how the servers coordinate."),
            TABLE(["", "Single server", "Cluster"], [
                ["Licence", "Standard or higher", "Pro or higher"],
                ["PostgreSQL", "Required", "Required, shared by all servers"],
                ["Redis", "Optional", "Required, shared by all servers"],
                ["Storage", "Any backend", "S3, MinIO, Azure, or a shared volume"],
                ["Servers", "1", "Up to the licence limit"],
            ]),
            H("What a cluster shares"),
            UL([
                "**Pages and edits** are saved in PostgreSQL first, then announced to the other servers, so two people editing the same page on different servers see each other's changes.",
                "**Background work** (imports, analytics rollups, scheduled publishing, review-by reminders, Q&A reputation) runs once per cluster, whichever server picks it up.",
                "**Settings**, such as anonymous access, search engines and video sites, apply on every server within seconds of being saved.",
                "**Files** go to the shared storage, so any server serves any image or video.",
            ]),
            H("Redis"),
            P("Give Redis as a URL in the setup wizard, the unattended setup file (`cache.redis_url`), on a running installation in **Settings → Clustering → Redis** (see [Add Redis to a running installation](#add-redis-to-a-running-installation)), or on the recovery page when a server can't start:"),
            TABLE(["Kind", "URL"], [
                ["One server", "`redis://:password@redis.internal:6379/0`, or `rediss://` for TLS"],
                ["Sentinel group", "`redis+sentinel://:password@s1:26379?master_name=mymaster&addr=s2:26379&addr=s3:26379`"],
                ["Redis Cluster", "`redis+cluster://:password@n1:6379?addr=n2:6379&addr=n3:6379`"],
            ]),
            UL([
                "Each kind takes TLS (`rediss`, `rediss+sentinel`, `rediss+cluster`), a private certificate authority (`ca_file=/path/ca.pem`) and Redis ACL users (`user:password@`).",
                "Redis coordinates; PostgreSQL keeps the records. If Redis becomes unavailable, the Wiki keeps working: sign-in and sessions (kept in PostgreSQL), scheduled jobs once per cluster, and live updates through PostgreSQL. Rate limits are then counted by each server on its own. It logs one warning when Redis goes and one message when it returns.",
                "A failover can lose the last few writes to Redis; results stay correct because PostgreSQL holds the records.",
            ]),
            H("Add Redis to a running installation"),
            P("An installation set up without Redis runs on one server. To grow it into a cluster, add Redis first. Super admins do it on **Settings → Clustering**, in the **Redis** card:"),
            STEPS([
                "Open Settings → Clustering|The **Redis** card says **Not set up** and lists the servers that are running, each with **No Redis**.",
                "Select Set up Redis|Enter the Redis URL (one server, Sentinel or Redis Cluster, as in the table above). Put the password in the URL or in **Password**.",
                "Select Test connection|The Wiki connects to every server the URL names. It says **Connected**, or why not: the URL can't be used, Redis refused the user name or password, or Redis can't be reached from this server. Nothing is saved yet.",
                "Select Save|The URL is tested again and saved, encrypted, with the rest of the setup configuration.",
                "Restart the server|A server starts using Redis when it restarts. Until then the card marks it **Restart needed**; after the restart it shows **Uses Redis**.",
                "Start the next server|Once every running server shows **Uses Redis**, start the second server with the same database and shared storage. A server can't join while another one runs without Redis: it stops with an error that says what to do.",
            ]),
            UL([
                "**Change** works the same way. The saved password is never shown: the form shows the URL without it, and leaving **Password** empty keeps it. Each server shows **Restart needed** until it restarts with the new setting.",
                "Changing to a different Redis while several servers run splits the cluster until every server has restarted: live updates and rate limits aren't shared between restarted servers and the others for that time. Restart them one after another without a pause, or change Redis while one server runs.",
                "**Remove** forgets the URL, so the server runs without Redis after its next restart. It is only offered while one server runs: a cluster needs Redis.",
                "Each change raises `cluster.redis.update` (see [Events](events.html)) and is in the audit log as `redis:update`, `redis:remove` and `redis:test`. Only super admins have the `redis:admin` permission this needs.",
            ]),
            H("Database connections"),
            P("Each server opens up to `pool_max_conns` connections to PostgreSQL (by default 4, or the number of CPUs if that is more). Set it in `DATABASE_URL`, for example `postgres://wiki:…@db:5432/wiki?pool_max_conns=25`, at a server's first start. In a cluster every server opens its own, so keep servers × `pool_max_conns`, plus room for maintenance, under PostgreSQL's `max_connections`."),
            H("Read cache"),
            P("Each server keeps what most requests look up, such as roles and settings, in its own memory. PostgreSQL tells every server the moment one of these changes, and each server also checks every second, so a change applies everywhere almost at once, with or without Redis. `READ_CACHE_ENABLED=false` turns it off on one server (see [Environment variables](environment-variables.html))."),
            H("Clustering page"),
            P("**Settings → Clustering** (super admins) lists every server: its status, health, name and machine ID, version, CPU, memory, uptime and last heartbeat, and the leader. A server that stops responding gets a notice above the table."),
            TABLE(["Status", "Meaning"], [
                ["**active**", "Running."],
                ["**draining**", "Shutting down: finishing its work before it stops."],
                ["**left**", "Shut down cleanly. Removed from the list after a day (`CLUSTER_DEAD_NODE_TTL`)."],
                ["**dead**", "Stopped sending heartbeats without shutting down cleanly. It becomes active again by itself with its next heartbeat; one that stays dead is removed after a day."],
            ]),
            P("A server whose start is refused after it registered, for example because its storage isn't the cluster's shared storage, is not listed as **left**: it never served. A new server is taken off the list again; a server that ran before goes back to how it was listed before that start (one that had crashed shows as **dead**), and its recent events show **Start refused**. **Statuses** under How clustering works on the page explains each status."),
        ])),

    # -------------------------------------------------- environment-variables
    ("environment-variables", dict(
        label="Environment variables", title="Environment variables", icon="sliders",
        desc="The environment variables the Wiki's server and web app read: what each does, its default, and where to set it",
        keywords=["environment", "env", "variables", "configuration", "CONFIG_ENCRYPTION_KEY", "DATABASE_URL", "TRUSTED_PROXIES", "BIND_ADDR", "PORT", "BACKEND_URL", "FRONTEND_API_BODY_LIMIT", "tuning", "systemd"],
        blocks=[
            P("Environment variables are for what a server needs before it can read its settings (the encryption key, the database on first boot) and for per-server tuning. Everything else is a setting: stored encrypted in PostgreSQL, changed in **Settings**, and the same on every server at once (see [Settings reference](settings-reference.html))."),
            H("Where to set them"),
            TABLE(["Running the Wiki as", "Set them in"], [
                ["A service (systemd)", "An `EnvironmentFile=` readable only by the service user, for example `/etc/wiki/server.env` (mode 0600)"],
                ["Containers you build", "`docker run -e NAME=value` or `--env-file`; secrets from your orchestrator's secret store"],
            ]),
            UL([
                "A value the server can't read (a duration that isn't one, a number out of range) stops it at startup with a message naming the variable.",
                "Durations are written `30s`, `15m`, `24h`. Sizes are bytes unless the name says otherwise. Schedules are cron expressions (`minute hour day month weekday`, UTC).",
                "Some defaults apply only until an administrator saves the matching settings page; the page then wins on every server.",
            ]),
            WARN("In a cluster, give every server the same values, except the per-server ones (`PORT`, `BIND_ADDR`, `NODE_DISPLAY_NAME`, directories, `LOG_LEVEL`)."),
            H("Bootstrap"),
            TABLE(T, [
                ["`CONFIG_ENCRYPTION_KEY`", "none, **required**", "Encrypts the bootstrap file and every credential stored in the database. Required on every start; the same on every server; keep it with your backups"],
                ["`DATABASE_URL`", "none", "PostgreSQL URL. Needed on a server's first start (and for setup); then saved, encrypted, in the bootstrap file. When set on a later start it wins over the saved one, as long as it reaches the same installation: that is how a [changed password](database-credentials.html) is rolled out. Add `pool_max_conns=N` and `sslmode=verify-full` as needed"],
                ["`DATABASE_URL_FILE`", "none", "A file holding the database URL (a mounted secret), instead of `DATABASE_URL`. Read again while the server runs, so a password a secret manager changes needs no restart"],
                ["`DATABASE_URL_STANDBY`, `DATABASE_URL_STANDBY_FILE`", "none", "A second login for the same database. The server moves to it when the first is refused; see [Database password](database-credentials.html#two-logins)"],
                ["`DATABASE_OWNER_ROLE`", "none", "The role every connection acts as, when the logins don't own the tables themselves (two logins, one owner). Set it from the first start, the same on every server"],
                ["`BOOTSTRAP_FILE_PATH`", "`./data/bootstrap.enc`", "Where the server keeps its encrypted bootstrap file. Per server; keep it on persistent disk"],
                ["`PORT`", "`8080`", "The server's HTTP port"],
                ["`BIND_ADDR`", "`127.0.0.1`", "Address the server listens on"],
                ["`FRONTEND_URL`", "`http://localhost:3000` (set it: the web app listens on 3002)", "Where the web app is; also the default allowed CORS origin. Set it to the Wiki's address"],
                ["`CORS_ALLOWED_ORIGINS`", "`FRONTEND_URL`", "Comma-separated origins allowed to call the API from a browser"],
                ["`APP_ENV`", "empty", "`development` prints the log as readable lines instead of JSON; leave it unset in production"],
            ]),
            H("Setup and recovery"),
            TABLE(T, [
                ["`SETUP_TOKEN`", "random, new on every start", "The setup key the wizard needs. Set it to choose it"],
                ["`SETUP_CONFIG_FILE`", "empty", "A setup file for [unattended setup](headless-setup.html); same as `--setup-config`"],
                ["`SETUP_UPLOAD_DIR`", "`./data/setup-upload`", "Where a backup uploaded to the wizard's **Restore from a backup** waits"],
                ["`RECOVERY_TOKEN`", "random", "The key of the [recovery page](recovery.html)"],
                ["`LICENSE_BANNER_DAYS`", "`30`", "Super admins see a banner this many days before the licence expires (0 turns it off)"],
            ]),
            H("Reverse proxy and web app"),
            TABLE(T, [
                ["`TRUSTED_PROXIES`", "`127.0.0.0/8,::1/128`", "Proxies whose forwarding headers the server trusts (IPs or CIDRs). List the web app and every proxy in front that reaches the server. `X-Forwarded-For`, `-Host`, `-Proto` and `X-Real-IP` from any other sender are removed, and the system check reports it"],
                ["`FRONTEND_BEHIND_PROXY`", "`false`", "Web app: `true` when a proxy in front sets `X-Forwarded-For`, `-Host` and `-Proto`. Then only the proxy may reach the web app's port"],
                ["`FRONTEND_API_BODY_LIMIT`", "`33554432` (32 MiB)", "Web app: largest `/api` request it forwards. Uploads to a page have their own 201 MiB limit"],
                ["`BACKEND_URL`", "`http://127.0.0.1:8080`", "Web app: where the server is"],
                ["`CSP_ENFORCE`", "unset (enforced)", "Web app: `false` sends the Content-Security-Policy report-only"],
            ]),
            H("Sign-in and sessions"),
            TABLE(T, [
                ["`AUTH_LOCKOUT_THRESHOLD`, `AUTH_LOCKOUT_WINDOW`, `AUTH_LOCKOUT_DURATION`", "`5`, `15m`, `15m`", "Wrong passwords that lock an account, how long they count, how long it stays locked"],
                ["`AUTH_IP_RATE_LIMIT`, `AUTH_IP_RATE_WINDOW`", "`20`, `15m`", "Failed sign-ins and unknown tokens per address before it's blocked"],
                ["`AUTH_PASSWORD_MIN_LENGTH`", "`12`", "Minimum password length (8–64)"],
                ["`AUTH_SESSION_LIFETIME`, `AUTH_REMEMBER_SESSION_LIFETIME`", "`24h`, `168h`", "Longest session without and with **Remember me** (until saved in Settings → Security → Sessions)"],
                ["`AUTH_MAX_SESSIONS`", "`5`", "Sessions per person"],
                ["`AUTH_COOKIE_DOMAIN`, `AUTH_COOKIE_SECURE`", "the host, `true`", "Session cookies: their domain, and HTTPS only"],
                ["`AUTH_PASSWORD_RESET_TTL`, `AUTH_INVITATION_TTL`", "`30m`, `168h`", "Lifetimes of password reset and invitation links"],
                ["`AUTH_LOGIN_HISTORY_RETENTION_DAYS`", "`90`", "Days of sign-in history kept"],
                ["`SSO_ENFORCEMENT_OVERRIDE`", "`false`", "**Emergency only**: `true` ignores **Require single sign-on** on this server so an administrator can sign in with a password while the identity provider is down"],
            ]),
            H("Rate limits"),
            P("Defaults until saved in **Settings → Security → Rate limits** (see [Rate limits](rate-limits.html)); `0` turns a limit off. The Wiki's own limits (Q&A posts, calendar reads and writes, page views reported by anonymous readers) are built in."),
            TABLE(T, [
                ["`RATE_LIMIT_PREAUTH`", "`10000`", "Requests per minute per address before sign-in is checked"],
                ["`RATE_LIMIT`", "`600`", "Per minute per person in the browser"],
                ["`RATE_LIMIT_ANON`", "`60`", "Per minute per address for anonymous requests"],
                ["`RATE_LIMIT_WS`", "`20`", "WebSocket connections per minute per address"],
                ["`RATE_LIMIT_SETUP`", "`30`", "Per minute per address in setup and recovery mode"],
                ["`RATE_LIMIT_DRY_RUN`", "`false`", "`true` logs requests over a limit instead of refusing them"],
            ]),
            H("Database, Redis and cluster"),
            TABLE(T, [
                ["`DB_CONNECT_TIMEOUT`", "`30s`", "How long a starting server keeps trying the database"],
                ["`DB_SLOW_QUERY_THRESHOLD`", "`500ms`", "Queries slower than this are logged as warnings"],
                ["`NODE_DISPLAY_NAME`", "empty", "This server's name in **Settings → Clustering**"],
                ["`CLUSTER_HEARTBEAT_INTERVAL`, `CLUSTER_DEAD_THRESHOLD`, `CLUSTER_LEADER_GRACE`", "`10s`, `3`, `5`", "Heartbeats, and missed ones before a server, or the leader, is replaced"],
                ["`CLUSTER_DEAD_NODE_TTL`, `CLUSTER_EVENT_RETENTION_DAYS`", "`24h`, `7`", "When servers that left drop off the list; days of cluster events kept"],
                ["`READ_CACHE_ENABLED`", "`true`", "Per-server cache of roles and settings; `false` reads the database every time"],
                ["`READ_CACHE_CHECK_INTERVAL`, `READ_CACHE_MAX_AGE`, `READ_CACHE_MAX_ENTRIES`", "`1s`, `5m`, `20000`", "How often it checks for changes, the longest it keeps an item, items per kind"],
            ]),
            NOTE("Redis, storage and the licence are not environment variables: they're entered in the setup wizard (or setup file), stored encrypted, and changed in Settings or on the recovery page."),
            H("Logging, audit and metrics"),
            TABLE(T, [
                ["`LOG_LEVEL`", "`info`", "`debug`, `info`, `warn`, `error`; change it live in Settings → Logging"],
                ["`LOG_REDACT_ENABLED`", "`true`", "Remove secrets from log lines"],
                ["`LOG_FILE_ENABLED`, `LOG_FILE_DIR`", "`true`, `./data/logs`", "This server's log files"],
                ["`AUDIT_LOG_RETENTION_DAYS`", "`90`", "Days of audit log kept"],
                ["`METRICS_ADDR`", "off", "A separate listener serving `/metrics` **without authentication**: bind it to a private interface. See [Monitoring](monitoring.html)"],
                ["`METRICS_TOKEN`", "off", "Also serve `/metrics` on the main port to `Authorization: Bearer <token>`"],
                ["`SYSTEM_CHECK_INTERVAL`", "`1h`", "How often each server runs its [system check](system-check.html)"],
            ]),
            H("Scheduler, events and plugins"),
            TABLE(T, [
                ["`SCHEDULER_LOCK_TTL`, `SCHEDULER_SHUTDOWN_GRACE_PERIOD`", "`5m`, `30s`", "How long a job's lock lasts without renewal; time running jobs get on shutdown"],
                ["`PAGINATION_CURSOR_SECRET`", "unset", "Signs paging cursors so clients can't forge them. Recommended; the same on every server"],
                ["`EVENT_MAX_ATTEMPTS`, `EVENT_OUTBOX_RETENTION_DAYS`", "`8`, `7`", "Retries and retention of durable event deliveries"],
                ["`AUTOMATION_WEBHOOK_ALLOW_PRIVATE`, `AUTOMATION_WEBHOOK_ALLOW_HTTP`", "`false`", "Allow webhooks to private addresses, or plain `http`"],
                ["`PLUGIN_SIGNING_REQUIRED`", "`true`", "Refuse plugins not signed by a trusted key"],
                ["`PLUGIN_MAX_PACKAGE_SIZE`", "20 MiB", "Largest plugin package"],
                ["`PLUGIN_DATABASE_URL`", "the main database", "Put plugin schemas on another PostgreSQL database"],
            ]),
            P("Most scheduled jobs' times and retention are changed in **Settings → Advanced → Scheduled jobs** instead (see [Scheduled jobs](scheduler.html)); backups in **Settings → Backups** (see [Backups](backups.html))."),
        ])),

    # ----------------------------------------------------------- setup-wizard
    ("setup-wizard", dict(
        label="Setup wizard", title="Setup wizard", icon="rocket",
        desc="Set up a new installation step by step: licence, database, storage, cache and the first administrator",
        keywords=["setup", "wizard", "first run", "setup key", "setup token", "installation id", "license", "licence", "database", "storage", "redis", "administrator", "restore"],
        blocks=[
            P("A server that has never been set up starts in **setup mode**: it serves only the setup wizard, protected by a one-time setup key. The wizard collects what the installation needs, stores every credential encrypted in the database, and restarts the server into normal mode. It takes about five minutes once PostgreSQL and your storage exist."),
            SHOT("setup-wizard-license.png", "Setup wizard, License: the installation ID to request a licence with, and the licence to upload or paste"),
            H("Before you start"),
            TABLE(["You need", "Details"], [
                ["A PostgreSQL database", "An empty database and a role that owns it. Not a superuser. See [Plan an installation](install-planning.html)."],
                ["File storage", "A directory on the server, an S3 bucket, a MinIO bucket or an Azure Blob container, which must already exist."],
                ["Redis (optional)", "Needed only for a cluster."],
                ["`CONFIG_ENCRYPTION_KEY`", "Set on the server before its first start, and kept safe."],
                ["A licence", "Bound to the installation ID the wizard shows on its first step. See [Licensing](licensing.html)."],
            ]),
            H("Open the wizard"),
            STEPS([
                "Start the server|With `DATABASE_URL` and `CONFIG_ENCRYPTION_KEY` set (see [Install the Wiki](install.html)).",
                "Find the setup link|The log prints a line like `open the setup wizard … setup_url=https://wiki.example.com/setup?token=…`.",
                "Open it|The page reads the key and removes it from the address bar.",
                "Choose your language|The language menu at the top. The first administrator keeps it as their language.",
            ]),
            H("The steps"),
            TABLE(["Step", "What it asks"], [
                ["**1. License**", "Shows the **Installation ID** (**Copy installation ID**). **Upload file** or **Paste text**, then **Validate license**. **Next** stays off until the licence is valid for this installation"],
                ["**2. Database**", "A **Connection string** or **Connection details** (host, port, database, user, password, SSL mode). **Test connection** checks that the Wiki can sign in and create tables; a database that already holds tables is flagged, with **Wipe database** for one you made for the Wiki"],
                ["**3. Storage**", "**Local filesystem** (a base path), **AWS S3** (bucket, region, keys or the server's IAM role), **MinIO** or **Azure Blob Storage**. The wizard writes and reads a test object before you go on"],
                ["**4. Cache**", "An optional **Redis URL**; leave it empty for a single server"],
                ["**5. Administrator**", "The first **super admin**'s name, email and password, or **Restore from a backup**"],
            ]),
            SHOT("setup-wizard-admin.png", "Setup wizard, Administrator: the first super admin, or restore from a backup"),
            P("**Complete setup** saves everything, runs the database migrations and restarts the server in normal mode. The page waits and then takes you to sign-in. Nothing is saved until **Complete setup** succeeds, so you can restart the server and begin again at any point before that."),
            P("Setup never changes an installation that exists: when the database already holds one, this server only joins it as one more server (with that installation's `CONFIG_ENCRYPTION_KEY`), and what you entered isn't applied."),
            H("After setup"),
            STEPS([
                "Sign in|As the administrator you created.",
                "Set the Wiki's address|**Settings → General**: the address people use. Links in emails and single sign-on depend on it.",
                "Configure email|**Settings → Application → Email**, so invitations and password resets work. See [Email](email.html).",
                "Bring people in|Directories, single sign-on or invitations. See [Users & directories](users-and-directories.html).",
                "Create the first spaces|Only super admins create spaces. See [Spaces](spaces.html).",
                "Turn on backups|**Settings → Backups**. See [Backups](backups.html).",
                "Harden it|Work through the [production checklist](security-hardening.html).",
            ]),
            H("If setup fails"),
            TABLE(["What you see", "What to do"], [
                ["The setup page says the key is missing or wrong", "Open the exact `setup_url` from the newest log line; the key changes on every restart unless `SETUP_TOKEN` is set"],
                ["Database: can't connect or can't create tables", "Check host, port and SSL mode; the role needs to own the database"],
                ["Storage isn't accessible", "The bucket or container must exist; check the credentials, region or endpoint, and that the server can reach it"],
                ["Couldn't connect to Redis", "Check the URL scheme for Sentinel or Cluster, the password and TLS (`rediss`)"],
            ]),
        ])),

    # ---------------------------------------------------------- headless-setup
    ("headless-setup", dict(
        label="Set up without the UI", title="Set up without the UI", icon="terminal",
        desc="Unattended setup from a YAML file for scripts, containers and configuration management",
        keywords=["headless", "unattended", "passive setup", "setup file", "setup.yaml", "SETUP_CONFIG_FILE", "--setup-config", "--machine-id", "automation", "ansible", "restore"],
        blocks=[
            P("Everything the setup wizard asks can come from a YAML file instead, so a new installation can be set up by a script, a container entrypoint or configuration management with nobody at a browser."),
            H("How it works"),
            STEPS([
                "Get the installation ID|`./wiki-server --machine-id` prints it and exits. Run it on the machine that will run the Wiki: the ID belongs to that machine.",
                "Get the licence|Request it for that ID (see [Licensing](licensing.html)).",
                "Write the setup file|The same sections as the wizard; secrets as `${VARIABLE}` references.",
                "Start the server once with it|`--setup-config setup.yaml`, or `SETUP_CONFIG_FILE=setup.yaml`. The server checks the file, sets up, and continues in normal mode.",
                "Remove the file|It's read only on a fresh installation and ignored afterwards.",
            ]),
            CODE("""chmod 600 setup.yaml
export CONFIG_ENCRYPTION_KEY="$(cat /run/secrets/wiki-encryption-key)"
export DATABASE_URL='postgres://wiki:…@db.internal:5432/wiki?sslmode=verify-full'
export ADMIN_PASSWORD="$(cat /run/secrets/wiki-admin-password)"
./wiki-server --setup-config setup.yaml"""),
            H("The setup file"),
            CODE("""database:
  url: ${DATABASE_URL}           # may be left out when DATABASE_URL is set

cache:
  redis_url: ""                  # empty: single server without Redis; required for a cluster

storage:
  backend: s3                    # local | s3 | minio | azure
  local:
    path: /var/lib/wiki/files
  s3:
    bucket: my-wiki-files
    region: eu-west-1
    access_key: ${S3_ACCESS_KEY} # leave both keys out to use the server's IAM role
    secret_key: ${S3_SECRET_KEY}
  minio:
    endpoint: minio.internal:9000
    bucket: wiki
    use_ssl: true
    access_key: ${MINIO_ACCESS_KEY}
    secret_key: ${MINIO_SECRET_KEY}
  azure:
    container: wiki
    account: ${AZURE_STORAGE_ACCOUNT}
    key: ${AZURE_STORAGE_KEY}

license:
  file: license.json             # relative to this file; or data: | with the JSON inline

admin:
  email: admin@example.com
  name: Administrator
  password: ${ADMIN_PASSWORD}    # at least 8 characters"""),
            TABLE(["Key", "Required", "Meaning"], [
                ["`database.url`", "When `DATABASE_URL` isn't set", "PostgreSQL URL; query options such as `sslmode` and `pool_max_conns` are kept"],
                ["`cache.redis_url`", "For a cluster", "Redis URL: one server, Sentinel or Redis Cluster"],
                ["`storage.backend`", "Yes", "`local`, `s3`, `minio` or `azure`; only that backend's section is read"],
                ["`storage.s3.*`", "With `s3`", "`bucket`, `region`; `access_key` and `secret_key` (or neither, for the IAM role); optional `role_arn`, `external_id`"],
                ["`license.file` or `license.data`", "Yes, one of them", "The licence JSON: a file (relative to the setup file) or inline"],
                ["`admin.email`, `admin.name`, `admin.password`", "Yes", "The first super admin"],
            ]),
            H("Rules the server enforces"),
            UL([
                "**Private file.** The file must not be readable by group or others (`chmod 600`); otherwise the server stops and prints the `chmod` to run.",
                "**No unknown keys.** A misspelled key is an error.",
                "**Secrets from the environment.** Any value may use `${NAME}`; a referenced variable that isn't set stops the server with its name.",
                "**Fresh installations only.** On an installed server the file is ignored.",
                "**Fails loudly.** If a value doesn't work, the server stops with an error that says what to fix; nothing is half set up.",
            ]),
            H("After setup, without the UI"),
            UL([
                "Everything in the web app is also an API: `GET /api/openapi.json` describes every route, its permission and its licence tier. Sign in once to create an [API token](api-tokens.html), or register an [OAuth application](oauth-applications.html) with a service account.",
                "Pages can be brought in from Confluence or Markdown with an [import](confluence-import.html) once a space exists.",
            ]),
            H("Command-line flags"),
            TABLE(["Flag", "What it does"], [
                ["`--setup-config <file>`", "Set up a fresh installation from this file (overrides `SETUP_CONFIG_FILE`)"],
                ["`--machine-id`", "Print this machine's installation ID, for a licence request, and exit"],
                ["`--restore-file <file>`", "Check a backup archive with no server running; with `--yes`, restore it, then exit. See [Backups](backups.html)"],
            ]),
        ])),

    # -------------------------------------------------------------- licensing
    ("licensing", dict(
        label="Licensing", title="Licensing", icon="lock-closed",
        desc="The installation ID, what each licence tier turns on in the Wiki, and updating a licence",
        keywords=["license", "licence", "tier", "installation id", "entitlements", "trial", "renewal", "pro", "enterprise", "standard", "expired", "402"],
        blocks=[
            P("A Wiki licence is a signed file bound to the installation's ID. Its tier decides which features are available; it can also cap how many people may sign in and how many servers may run."),
            ACCESS_NOTE,
            H("What each tier turns on"),
            P("Every Wiki feature works on every tier except page analytics and mirror spaces, which need **Pro**, and whiteboards, which need **Enterprise**. Plugin blocks need plugins, which need Pro:"),
            TABLE(["Wiki feature", "Tier"], [
                ["Spaces, pages and the editor with its built-in blocks, drafts, versions, reviews, page restrictions, copies and templates", "Standard"],
                ["Editing together, comments, attachments and videos, labels and page feedback", "Standard"],
                ["Q&A, space calendars and calendar feeds", "Standard"],
                ["Imports (Confluence, Markdown) and exports (Word, PDF)", "Standard"],
                ["Anonymous access to public spaces and questions", "Standard"],
                ["Page [analytics](analytics-settings.html)", "Pro"],
                ["[Kee](kee-setup.html), the Wiki's AI: writing help, page summaries, Ask Kee with proposed changes, Kee studio, change summaries, scheduled help and the weekly space digest, the writing helpers, title, label and duplicate suggestions, images, and [search by meaning](kee-search.html). A fallback model at another provider and the usage export by person need Enterprise", "Pro"],
                ["[Outside AI apps](kee-outside-apps.html): people connect their own AI apps to the Wiki's built-in server (works with Kee off)", "Pro"],
                ["The **Read, change and administer** level for outside AI apps: [administration tools](kee-outside-apps.html#administration-tools) such as who can do what in a space, labels across the Wiki and page locks", "Enterprise"],
                ["[Mirror spaces](mirror-spaces.html): spaces that follow a git repository or uploaded archives", "Pro"],
                ["Plugin blocks in pages", "Pro, as for every plugin"],
                ["[Whiteboards](whiteboards.html): live canvases, facilitation, whiteboard templates and the whiteboard block", "Enterprise"],
            ]),
            P("The tiers add these platform features:"),
            TABLE(["Tier", "Adds"], [
                ["**Standard**", "The Wiki features above marked Standard, users and groups, Local and Delegated directories, backups, email, banners"],
                ["**Pro**", "Page [analytics](analytics-settings.html), [Kee](kee-setup.html), clustering (several servers), the [system check](system-check.html), the audit log, [policies](policies.html), [automation](automation.html), [plugins](plugins.html), LDAP and Active Directory, API token IP allowlists and rotation"],
                ["**Enterprise**", "[Whiteboards](whiteboards.html), [single sign-on](single-sign-on.html), [branding](branding-and-banners.html), SCIM, Entra ID and Google Workspace directories, managing everyone's API tokens"],
            ]),
            P("A feature the licence doesn't cover shows what it would need instead of its settings, and its API answers `402`. Without Pro, the Analytics entry in the left navigation and the spaces' Analytics tab aren't shown, and page views aren't recorded. Below Pro the \"/\" menu offers no plugin blocks and existing plugin blocks show their saved text; moving back to Pro brings them back, and nothing is lost. Below Enterprise nobody can make or open whiteboards, and whiteboard blocks in pages show nothing; the whiteboards and their versions are kept, and come back with an Enterprise licence."),
            H("The licence page"),
            SHOT("licensing-overview.png", "Settings → Application → Licensing: tier, licensee and expiry, limits, the installation ID and Update license"),
            P("**Settings → Application → Licensing** (the `licenses:admin` permission) shows the tier and status, who it's issued to, when it expires, and how many users and servers are in use against its limits. Below are the features it turns on, its licence ID, and the **Installation ID** to quote when requesting a new licence (**Copy** puts it on the clipboard)."),
            P("Super admins see a banner when the licence expires within 30 days, is in its grace period, has expired or isn't valid. `LICENSE_BANNER_DAYS` changes the 30 days (`0` turns the banner off)."),
            H("Get a licence"),
            P("To get a licence, a trial or a renewal, or to change your tier, user limit or server limit, contact us through [vectored.dev/#contact](https://vectored.dev/#contact) or email [" + SUPPORT_MAIL + "](mailto:" + SUPPORT_MAIL + "). Include:"),
            TABLE(["What", "Where to find it"], [
                ["**Installation ID**", "The setup wizard's License step, **Settings → Application → Licensing**, or `./wiki-server --machine-id` on the machine that will set the Wiki up. A cluster has one ID, shared by every server"],
                ["**Licensee**", "The organization name to show on the licence"],
                ["**Tier**", "Standard, Pro or Enterprise"],
                ["**Users and servers**", "How many people will sign in, and how many servers will run"],
                ["**Term**", "Start date and length, or the licence ID you are renewing"],
            ]),
            NOTE("The installation ID is saved in the database when the Wiki is set up, so adding servers or moving them with the same database keeps it. A new installation (a new database, including one you restore a backup into) has its own ID and needs a licence for it: request it before you move."),
            H("When a licence expires"),
            UL([
                "**Grace period:** a licence can allow some days of grace after its expiry date. Everything keeps working; the page and the banner say how many days ago it expired.",
                "**After the grace period**, or with a licence that isn't valid, the Wiki only answers sign-in, health checks and the licence itself until a valid licence is applied. Nothing is deleted.",
                "Apply the renewal as below; it takes effect at once, without a restart.",
            ]),
            H("Update the licence"),
            STEPS([
                "Load the new licence|Under **Update license**, select **Upload .json file** (or drop the file on it), or open **Paste the license instead**.",
                "Compare|The Wiki checks the signature and that the licence was issued for this installation, then shows the current and the new licence side by side, with what changes.",
                "Apply|Select **Apply license**, or **Cancel** to keep the current one.",
            ]),
        ])),

    # --------------------------------------------------------------- recovery
    ("recovery", dict(
        label="Recovery mode", title="Recovery mode", icon="life-buoy",
        desc="What happens when an installed server can't start, and how to fix it",
        keywords=["recovery", "troubleshooting", "startup", "database", "redis", "license", "licence", "encryption key", "RECOVERY_TOKEN"],
        blocks=[
            P("If an installed server can't start (the database is down, the encryption key is wrong, storage is unreachable, the licence no longer matches) it doesn't just exit. It starts in recovery mode, finds what's wrong, and shows you how to fix it."),
            H("Open the recovery page"),
            P("The server log shows a line like `open the recovery page … recovery_url=https://…/recovery?token=…`. Open that address. The key keeps the diagnostics private; set `RECOVERY_TOKEN` to choose it. Like the setup key, it is removed from the address bar once the page has read it."),
            SHOT("recovery-page.png", "The recovery page: each check, what failed and how to fix it"),
            H("What it checks"),
            TABLE(["Check", "Common causes"], [
                ["Bootstrap file", "The server was started with a different `CONFIG_ENCRYPTION_KEY`, or the file is damaged"],
                ["Database connection", "PostgreSQL is down or unreachable, every credential the server holds is refused (the password changed: put the new one in `DATABASE_URL` and restart, see [Database password](database-credentials.html)), or the URL points at another installation's database"],
                ["Database schema", "An upgrade's migration failed partway"],
                ["Stored configuration", "Wrong encryption key, or the wrong database"],
                ["Redis", "Redis is down or moved"],
                ["File storage", "Directory not writable, bucket missing, credentials expired"],
                ["Licence", "Expired, or issued for another installation ID"],
            ]),
            H("Fixing it"),
            P("Each failed check lists ways to fix it. Some can be applied from the page: a new database or Redis URL, a new licence, or running without Redis on a single server. The server tests the change, saves it encrypted, and restarts; the page reloads when it's back."),
            WARN("Recovery never changes data on its own. Repairs such as fixing a failed migration are described, not performed: take a backup first."),
            NOTE("The server only enters recovery mode on a machine that was already set up. A brand-new installation always starts the setup wizard."),
        ])),

    # ----------------------------------------------------- settings-reference
    ("settings-reference", dict(
        label="Settings reference", title="Settings reference", icon="settings",
        desc="Every page under Settings and the Wiki's own admin screens: what each configures, who may change it, and the licence it needs",
        keywords=["settings", "configuration", "admin settings", "permissions", "general", "appearance", "security", "anonymous access", "search engines", "video sites", "html blocks", "imports", "labels", "space categories", "q&a settings", "clustering", "storage", "backups", "licensing"],
        blocks=[
            P("Settings live in PostgreSQL, encrypted where they hold a secret, and apply to every server as soon as they're saved. **Settings** (at the bottom of the left navigation) shows each person only the pages their permissions allow. Every change is recorded in the [audit log](logging-and-audit.html), and most raise an [event](events.html) a [policy](policies.html) can stop or [automation](automation.html) can react to."),
            SHOT("settings-reference-menu.png", "Settings: the menu and the Security tabs, with the Wiki's own Search engines, Video sites and Imports"),
            H("Installation"),
            TABLE(["Page", "What it configures", "Permission", "Tier", "Docs"], [
                ["**General**", "The address people use to reach the Wiki, and the Help menu's links", "`settings:write`", "All", "[Install the Wiki](install.html)"],
                ["**Appearance**", "Application name, brand colours, logos and browser icons per theme", "`settings:write`", "Enterprise", "[Branding](branding-and-banners.html)"],
                ["**Banners**", "Announcements at the top of every page", "`settings:write`", "All", "[Banners](branding-and-banners.html)"],
                ["**Application → Licensing**", "The licence, its use against limits, and updating it", "`licenses:admin`", "All", "[Licensing](licensing.html)"],
                ["**Application → Email**", "SMTP or Amazon SES, the sender, a test message", "`email:manage`", "All", "[Email](email.html)"],
                ["**Clustering**", "Servers, their health, leader, Redis state", "Super admins", "All (a cluster needs Pro)", "[Single server & cluster](deployment-modes.html)"],
                ["**Database**", "The PostgreSQL logins the servers sign in with; rotate a password now or on a schedule", "`database:admin`", "All", "[Database password](database-credentials.html)"],
                ["**Storage**", "Where images, videos and platform files are stored", "`storage:admin`", "All", "[Storage](storage.html)"],
                ["**Backups**", "Backups, targets, encryption, restores", "`backups:read` / `backups:write`", "All", "[Backups](backups.html)"],
            ]),
            H("People and access"),
            TABLE(["Page", "What it configures", "Permission", "Tier", "Docs"], [
                ["**Access management → Users**", "People: create, invite, suspend, roles, sessions", "`users:read` / `users:write`", "All", "[Users & directories](users-and-directories.html)"],
                ["**Access management → Groups**", "Groups and their members", "`groups:read`", "All", "[Users & directories](users-and-directories.html)"],
                ["**Access management → Directories**", "Local, LDAP, Active Directory, Entra ID, Google Workspace, SCIM, Delegated", "`directories:read`", "All (some directories Pro or Enterprise)", "[Users & directories](users-and-directories.html)"],
                ["**Access management → Single sign-on**", "OpenID Connect and SAML providers", "`sso:manage`", "Enterprise", "[Single sign-on](single-sign-on.html)"],
                ["**Access management → Applications**, **Service accounts**", "OAuth applications and non-human accounts", "`oauth_apps:manage`", "Pro", "[OAuth applications](oauth-applications.html)"],
                ["**Policies**", "Rules that block, warn or adjust actions", "`policies:read`", "Pro", "[Policies](policies.html)"],
                ["**Automation**", "Alerts, webhooks and emails on events", "`automation:read`", "Pro", "[Automation](automation.html)"],
                ["**Plugins**", "Install, permissions, settings and data of plugins", "`plugins:read`", "Pro", "[Plugins](plugins.html)"],
                ["**Kee**", "The Wiki's AI: the switch, providers and models, features, scheduled help and its budget, the Kee permissions grid, limits, the budget, usage and data handling", "`ai:manage` (usage: `ai:usage:read`)", "Pro", "[Set up Kee](kee-setup.html)"],
                ["**Kee → Outside AI apps**", "Let outside AI apps connect (its own switch, works with Kee off), what apps may do per group of tools, who may connect, keys, the call limit, registered apps, usage and connections", "`ai:manage`", "Pro", "[Outside AI apps](kee-outside-apps.html)"],
            ]),
            H("Security tabs"),
            P("**Settings → Security** has a tab for each part. The first five are the platform's; the rest are the Wiki's own."),
            TABLE(["Tab", "What it configures", "Permission", "Docs"], [
                ["**Sign-in**", "Require single sign-on, and whether super admins may still use a password", "`sso:manage` (Enterprise)", "[Single sign-on](single-sign-on.html)"],
                ["**Sessions**, **CAPTCHA**", "Session lifetimes and limits; CAPTCHA after failed sign-ins", "`settings:write`", "[Users & directories](users-and-directories.html)"],
                ["**Anonymous access**", "Whether signed-out visitors may read public spaces and questions", "`settings:write`", "[Anonymous access](anonymous-access.html)"],
                ["**Rate limits**", "Request budgets and overrides", "`settings:write`", "[Rate limits](rate-limits.html)"],
                ["**Search engines**", "What robots.txt tells crawlers", "`settings:write`", "[Search engines](search-engines-and-robots.html)"],
                ["**Video sites**", "YouTube, Vimeo and other sites whose players pages may embed; taking a site off stops it on every page", "`settings:write`", "[Attachments & media](attachments-and-media.html)"],
                ["**HTML blocks**", "Whether pages may hold HTML blocks (off by default), who adds them, and the only sites they may reach", "`settings:write`", "[Blocks and macros](macros.html#html-blocks)"],
                ["**Slides**", "Who adds slide decks to pages (page editors by default), the largest deck, and the only hosts HTML decks may load libraries from", "`settings:write`", "[Slides](slides.html#for-administrators)"],
                ["**Attachments**", "The largest PDF or other file attached to a page, and the file extensions no page takes", "`settings:write`", "[Files and attachments](files-and-attachments.html#for-administrators)"],
                ["**Imports**", "Whether space admins may import, and the largest export", "`settings:write`", "[Imports](confluence-import.html)"],
                ["**Mirrors**", "Whether spaces may mirror git repositories and uploaded archives (Pro), who sets mirrors up, the largest archive and internal git hosts", "`settings:write`", "[Mirror spaces](mirror-spaces.html#for-administrators)"],
                ["**Link previews**", "Whether the server may read a linked page to fill in a link card (off by default), and hosts it never reads", "`settings:write`", "[Link cards](link-cards.html#link-previews)"],
            ]),
            H("Advanced"),
            TABLE(["Page", "What it configures", "Permission", "Tier", "Docs"], [
                ["**Logging**", "Log levels, log files, exports, the audit log", "`audit_logs:read`", "All (audit log Pro)", "[Logging & audit](logging-and-audit.html)"],
                ["**System check**", "Health of every dependency and server", "`settings:write`", "Pro", "[System check](system-check.html)"],
                ["**Alert tuning**", "Mutes and thresholds of health alerts", "`settings:write`", "All", "[Alert tuning](alert-tuning.html)"],
                ["**Scheduled jobs**", "Every background job, the Wiki's included: imports, analytics, scheduled publishing, reminders", "`scheduler:read`", "All (changes Pro)", "[Scheduled jobs](scheduler.html)"],
                ["**Event deliveries**", "Durable event deliveries and failures", "`events:admin`", "Pro", "[Events](events.html)"],
            ]),
            H("Wiki screens outside Settings"),
            TABLE(["Screen", "What it configures", "Who", "Docs"], [
                ["**Templates**", "The template library every space starts pages from: ready-made and your own templates", "`wiki_templates:manage`: super admins", "[Template library](template-library.html)"],
                ["**Settings → Space categories**", "The categories that group the space list; each space is in one or none", "`settings:write`: super admins", "[Spaces](spaces.html#space-categories)"],
                ["**Labels** (left navigation)", "Rename, merge or remove a label on every page and space of the installation", "`wiki_labels:manage`: super admins", "[Labels & feedback](labels-and-feedback.html)"],
                ["**Q&A → Settings**", "Allow public questions in the organization", "Q&A moderators: organization admins", "[Q&A moderation](qna-moderation.html)"],
                ["A space's **Settings**, **Members** and **Import** tabs", "Name, description, visibility, icon, labels, category and archiving; who has which role; imports", "The space's admins", "[Spaces](spaces.html)"],
                ["A space's **Settings → Kee** tab", "Whether Kee works in the space, the notice for readers, scheduled help for the space and its findings", "The space's admins", "[Kee in a space](kee-data.html#kee-in-a-space), [Scheduled help](kee-scheduled-help.html)"],
                ["**Analytics** (left navigation)", "Nothing to set: views, readers and content health", "Pro licence", "[Analytics](analytics-settings.html)"],
            ]),
            H("Settings that aren't in Settings"),
            TABLE(["What", "Where"], [
                ["Encryption key, first-boot database URL, ports, proxies, request size", "[Environment variables](environment-variables.html)"],
                ["Database, Redis, storage, licence when the server can't start", "The [recovery page](recovery.html)"],
                ["Each person's language, theme, notifications, sessions, tokens and calendar address", "Their profile and the calendar ([Profile & notifications](profile-and-notifications.html), [Calendar feeds](calendar-feeds.html))"],
            ]),
        ])),

    # -------------------------------------------------------- access-overview
    ("access-overview", dict(
        label="How access fits together", title="How access fits together", icon="users",
        desc="Directories, system roles, groups, space roles and Q&A: what each decides and how they combine",
        keywords=["access", "permissions", "rbac", "roles", "groups", "space roles", "viewer", "commenter", "editor", "admin", "visibility", "private", "internal", "public", "service account", "super admin", "organization admin", "who can"],
        blocks=[
            P("Who can do what in the Wiki is decided in layers. A **directory** brings in the account, the account's **system role** decides what it may do across the installation, and **space roles** decide what it may do in each space. **Groups** hand out space roles to many people at once. Q&A has its own permissions, from the system role."),
            H("The layers"),
            CODE("""Directory            Local · Delegated · LDAP · Active Directory · SCIM · Entra ID · Google Workspace
  └─ User account    one per person
       ├─ System role      Member · Organization admin · Super admin   → Settings, Q&A moderation, creating spaces
       ├─ Groups           added by hand, or synced from the directory  → carry space roles
       └─ Space role       Viewer · Commenter · Editor · Admin         → one space's pages"""),
            H("System roles"),
            TABLE(["System role", "Can"], [
                ["**Member**", "Sign in, read and write in the spaces their roles allow, read internal spaces of their organization, ask, answer and vote in Q&A, create their own API tokens"],
                ["**Organization admin**", "Also the Settings area for their organization (users, groups, policies, automation), and moderating its Q&A"],
                ["**Super admin**", "Everything: installation settings, licence, storage, backups, plugins, every space, managing labels. Only super admins create spaces"],
            ]),
            P("A directory never grants an admin role: synced and provisioned accounts start as Member; promote people in **Settings → Access management → Users**. See [Users & directories](users-and-directories.html)."),
            H("Space roles"),
            SHOT("access-overview-members.png", "A space's Members tab: adding a person, group or service account with a role, and the members with their roles"),
            P("A space role applies to every page in the space. Give it to a person, a group or a service account on the space's **Members** tab (the space's admins and super admins)."),
            TABLE(["Space role", "Can"], [
                ["Viewer", "Read pages"],
                ["Commenter", "Also comment on pages"],
                ["Editor", "Also create, edit, move and delete pages, and write blog posts"],
                ["Admin", "Also manage members and settings, import pages, and delete the space; edit any blog post and manage the space's blog"],
            ]),
            UL([
                "When someone has several roles in a space (their own and their groups'), **the highest one counts**.",
                "Removing a person from **Members** leaves the roles they have through groups.",
                "Nothing stops an admin from removing the space's last admin; a super admin can still add one back.",
                "The Wiki has no per-page restrictions yet: every page of a space is readable by everyone who can read the space. Drafts are seen only by those who edit the space.",
                "Blog posts are the exception for editing: only a post's authors (its writer and co-authors) and the space's admins edit it, and only they see it while it is a draft. A space's admins can let Commenters write posts too.",
            ]),
            H("Visibility"),
            TABLE(["Visibility", "Who reads it", "Who writes"], [
                ["**Private**", "Only members of the space", "Members with Editor or Admin"],
                ["**Internal**", "Everyone in the organization who can sign in", "Members with Editor or Admin"],
                ["**Public**", "Anyone, even without signing in, while [anonymous access](anonymous-access.html) is on", "Members with Editor or Admin"],
            ]),
            P("A space's admins set its visibility in the space's **Settings**. **Public** can be chosen only while anonymous access is on; when it's turned off later, a public space is read only by signed-in people."),
            H("Q&A"),
            P("Q&A belongs to the organization, not to a space: everyone in it with the Member or Organization admin role may read, ask, answer and vote; organization admins moderate. See [Q&A moderation](qna-moderation.html)."),
            H("Kee"),
            P("Who may use [Kee](kee-setup.html), see its usage and manage its settings is set in its own grid under **Settings → Kee → Features and access**: roles and groups, on top of the system roles. Using Kee never widens what a person can read or edit, and a space's admins can turn Kee off in their space. The same grid says who may make agents in [Kee studio](kee-studio.html), share them with everyone or manage everyone's, and who may [connect their own AI apps](connect-ai-apps.html). An agent and an outside AI app always act with the access of the person using them. See [Features and permissions](kee-access.html)."),
            H("Service accounts and tokens"),
            UL([
                "A **service account** is a non-human account for integrations. It gets space roles like a person; see [OAuth applications](oauth-applications.html).",
                "An **API token** never gives more than its owner has. See [API tokens](api-tokens.html).",
                "Policies can limit what is allowed on top of roles; see [Policies](policies.html).",
            ]),
            H("Example: a team's handbook"),
            STEPS([
                "Create the space|As a super admin: **+ Create → Space**, visibility **Internal**, so the whole organization can read it.",
                "Give the team the pen|On the space's **Members** tab, add the group `Support` with **Editor**.",
                "Hand over the space|Add the team lead with **Admin**, so they manage members and settings themselves.",
                "Let reviewers comment|Add the group `Reviewers` with **Commenter**.",
            ]),
        ])),

    # ------------------------------------------------------ analytics-settings
    ("analytics-settings", dict(
        label="Analytics settings", title="Analytics for administrators", icon="activity",
        desc="What page analytics records, who sees which numbers, how long views are kept, and the jobs behind it",
        keywords=["analytics", "page views", "readers", "content health", "stale pages", "broken links", "searches with no results", "retention", "privacy", "pro", "csv export"],
        blocks=[
            P("Page analytics count how often published pages are read, by how many people and for how long, and point out content that needs care. They need a **Pro** licence. There is nothing to switch on: with Pro, views are recorded and the screens appear; without it, nothing is recorded. How readers and space admins use the screens is in the user guide's [Analytics](analytics.html)."),
            SHOT("analytics-settings-health.png", "Analytics → Content health: stale pages, open drafts, broken links, least helpful pages, searches with no results and Q&A"),
            H("What is recorded"),
            UL([
                "**A view** each time a published page is shown to someone allowed to read it. The same signed-in person on the same page within 10 minutes is one view. Views through API tokens aren't counted.",
                "**Reading time**, while the tab is visible, up to 30 minutes per view.",
                "**Anonymous readers** of public spaces are counted as views without any identity, each view on its own, within a limit per address.",
                "**Searches with no result** for pages, as words and a count per organization and day, without who searched.",
                "Drafts, history and other screens aren't counted. Recording a view raises no event and isn't audited.",
            ]),
            H("Who sees what"),
            TABLE(["Screen", "Who", "Shows"], [
                ["**Analytics** (left navigation)", "Everyone signed in", "Views, readers and publishing across the spaces they may see; the most viewed pages and spaces; content health"],
                ["A space's **Analytics** tab", "Anyone who reads the space", "The same for one space, and per page"],
                ["The space's **People** tab", "The space's admins", "Who reads most and who publishes most (100 of each)"],
                ["**Searches with no results**", "`settings:write`", "Searches made at least twice in the period that found nothing"],
                ["**Drafts left open**", "Editors of the space; across spaces, super admins", "Drafts and pages in review unchanged for 30 days"],
            ]),
            P("Names of people who published follow the space's rule for showing people: readers from another organization and anonymous readers see counts only. **Export CSV** gives the most viewed pages (up to 10,000) with counts, never people."),
            H("Content health"),
            TABLE(["List", "Means"], [
                ["Not updated in 180 days", "Published pages with no newer version for 180 days"],
                ["Drafts left open", "Drafts and pages in review nobody changed for 30 days"],
                ["Broken links", "Pages linking to or including pages that are gone, unpublished or in the trash; checked every hour"],
                ["Least helpful", "Pages readers most often marked as not helpful"],
                ["Searches with no results", "What people searched for at least twice and didn't find"],
                ["Questions and answers", "Questions asked, answered and accepted in the period, and those still open"],
            ]),
            H("How long data is kept"),
            TABLE(["Data", "Kept"], [
                ["Each view (raw)", "90 days"],
                ["Who read on which day (for exact reader counts)", "25 months"],
                ["Daily totals per page and space", "As long as the page or space exists"],
                ["Searches with no result", "90 days"],
            ]),
            P("These periods are fixed: there is no setting yet to change them or to stop recording who read what. Erasing a person's data ([Personal data](personal-data.html)) removes what they read and leaves their views as anonymous counts."),
            H("Jobs and timing"),
            TABLE(["Job", "When", "Does"], [
                ["`wiki-analytics-rollup`", "Every 15 minutes", "Adds up the day's views; today's numbers trail by up to 15 minutes"],
                ["`wiki-analytics-links`", "Hourly", "Reads new versions of published pages for links"],
                ["`wiki-analytics-retention`", "Nightly at 02:45 UTC (editable)", "Removes views and searches past their retention"],
            ]),
            P("They are listed in **Settings → Advanced → Scheduled jobs** ([Scheduled jobs](scheduler.html)). Days are UTC days: a reader far from UTC sees a day's views split at UTC midnight."),
        ])),

    # ---------------------------------------------------------- calendar-feeds
    ("calendar-feeds", dict(
        label="Calendar feeds", title="Calendar feeds", icon="calendar",
        desc="Personal calendar addresses for Outlook, Google Calendar and Apple Calendar: how they work and how to keep them safe",
        keywords=["calendar", "ical", "ics", "feed", "subscribe", "outlook", "google calendar", "apple calendar", "calendar address", "token", "reset", "stop"],
        blocks=[
            P("Everyone can subscribe to their Wiki calendar from a calendar app: events and leave of their spaces, scheduled publishes and review-by dates. Each person makes their own **calendar address** on the **Calendar** page with **Subscribe**. How people use it is in the user guide's [Calendar](calendar.html); this page is what administrators need to know."),
            SHOT("calendar-feeds-subscribe.png", "Calendar → Subscribe: making a calendar address for a calendar app"),
            H("How a feed works"),
            UL([
                "The address holds a secret. It is shown **once**, when it's made; the Wiki keeps only a hash of it, so nobody, administrators included, can read it back.",
                "Each person has at most one address. **Make a new address** replaces it (the old one stops at once); **Stop the address** deletes it.",
                "A calendar app reads it without signing in, at `/api/calendar/ical`, through the web app like any other address. Keep query strings of that path out of your proxy's access logs: the secret is in the query.",
                "It shows what the person may see **now**: their current roles decide, so losing access to a space removes its entries from the feed.",
                "A feed covers 30 days back to a year ahead, at most 2,000 entries. Repeating events are sent as single occurrences.",
                "An address can only be made or replaced from a browser session, not with an API token.",
            ]),
            H("When a feed stops by itself"),
            UL([
                "The person is suspended or deactivated, their directory is disabled, or they must change a temporary password.",
                "Their other sessions are signed out: a password change, **Sign out other sessions**, or an administrator ending their sessions.",
                "Their personal data is erased.",
            ]),
            P("They then make a new address and give it to their calendar app."),
            H("Keeping feeds private"),
            WARN("The secret travels in the address, because calendar apps can't send headers. The Wiki never logs request queries, but a reverse proxy may: leave queries out of the access log for `/api/calendar/ical`, or protect that log like the feeds themselves."),
            UL([
                "If an address leaks, the person makes a new one; an administrator can also end the person's sessions, which stops it.",
                "Requests with an unknown address are limited per network address, so addresses can't be guessed at speed.",
                "Making, replacing and stopping an address are recorded in the [audit log](logging-and-audit.html), and raise the `calendar.feed.create` and `calendar.feed.delete` [events](events.html); a [policy](policies.html) can refuse new addresses.",
            ]),
        ])),

    # ------------------------------------------------------- confluence-import
    ("confluence-import", dict(
        label="Imports from Confluence", title="Imports from Confluence and Markdown", icon="file",
        desc="Turn imports on or off, set the largest export, and what space admins can import from Confluence and Markdown",
        keywords=["import", "confluence", "confluence export", "xml export", "markdown", "md", "zip", "migration", "migrate from confluence", "max size", "imports disabled"],
        blocks=[
            P("Space admins can bring pages into their space from a **Confluence space export** or from **Markdown** files. Administrators decide whether imports are allowed and how large an export may be. How a space admin runs an import is in the user guide's [Import & export](import-and-export.html)."),
            H("Settings"),
            SHOT("confluence-import-settings.png", "Settings → Security → Imports: Allow imports and the largest export"),
            P("**Settings → Security → Imports** (`settings:write`):"),
            TABLE(["Setting", "Default", "Effect"], [
                ["**Allow imports**", "On", "Space admins see an **Import** tab in their spaces. Turning it off also stops imports under way after their current step"],
                ["**Largest export (MiB)**", "2,048", "Between 1 and 102,400. The upload is kept in file storage until the import ends, so make sure storage has room"],
            ]),
            P("Changing them raises the `import_settings.update` event and is audited."),
            H("What can be imported"),
            SHOT("confluence-import-space-tab.png", "A space's Import tab: choose a Confluence export or Markdown, and earlier imports"),
            TABLE(["Source", "What comes in"], [
                ["**Confluence space export** (Space tools → Export, XML, full export, a `.zip`)", "Pages with their tree, versions with dates and authors, comments, labels, blog posts (as posts on the space's blog, or under a page you name), and every attachment (images, videos, PDFs and other files the [attachment settings](files-and-attachments.html#for-administrators) allow). Page layouts become [rows of columns](editor.html#columns): two equal columns, a left or right sidebar and three equal columns keep their shape, and three columns with sidebars become three equal columns. Common macros become Wiki blocks; others become a plain-text block a plugin may convert"],
                ["**Markdown**: one `.md` file, or a `.zip` of a folder", "Each folder becomes a page holding its files' pages (`index.md` or `README.md` is the folder's text); titles from front matter or the first heading; `tags` become labels; images in the upload become attachments"],
            ]),
            UL([
                "Every import is **checked first** (a dry run with a report) and writes nothing until the space admin starts it.",
                "Authors are matched to accounts by email; others keep the name the export gave.",
                "Importing the same export again **updates** the pages the earlier import made, and leaves pages edited in the Wiki since as they are.",
                "Uploads resume after a dropped connection. Imports run in the background, one step at a time, on any server.",
            ]),
            H("How Confluence macros are imported"),
            P("Common macros become Wiki blocks. Blocks that came with a newer version are used only once every server runs that version (see [Upgrades](upgrades.html#new-blocks-during-an-upgrade)); until then, and for macros not listed here, the macro is kept as an imported macro that a [plugin](plugins.html) may convert."),
            TABLE(["Confluence", "Becomes"], [
                ["Page layouts, and the older **Section** macro with **Column** macros", "A [row of columns](editor.html#columns). Two columns keep their shape by their widths (a first column of 60 % or more is **Wide left**, 40 % or less **Wide right**, otherwise equal); three or more become three equal columns, from the fourth on joined to the third"],
                ["**View file**, **PDF**, **Office Word / Excel / PowerPoint** viewers, **Multimedia**", "A [File block](files-and-attachments.html#file): a PDF or image shown in the page, other files as a card. A video file becomes a video"],
                ["A paragraph holding only a link to an attachment", "A File block (a link inside a sentence stays a link)"],
                ["**Attachments**", "An [attachments list](files-and-attachments.html#attachments-list), with its order and upload setting. A file name filter is kept when it is a simple pattern (such as `.*\\.pdf`); otherwise the list shows every file and the report counts it"],
                ["**Gallery**", "A [gallery](files-and-attachments.html#gallery): the included images in their order, every image but the excluded ones, or every image; columns and order kept"],
                ["A file macro, Attachments or Gallery about another page, or naming a file not in the export", "Kept as an imported macro; the report counts the missing files"],
                ["**Content by label**, **Content report table**", "[Pages by label](lists-of-pages.html#pages-by-label): labels, any or all, spaces (no space named: every space), blog posts, how many and the order; a content report table as a table"],
                ["**Blog posts**", "[Blog posts](lists-of-pages.html#blog-posts)"],
                ["**Contributors** (about the page itself), **Change history**", "[Contributors and Change history](lists-of-pages.html#contributors-and-change-history). Contributors about other pages and **Contributors summary** stay imported macros"],
                ["**Action items** (task lists)", "Checklists whose tasks keep their assignee (a mention) and due date ([Tasks](tasks.html))"],
                ["**Task report**", "A [task report](tasks.html#task-report): its spaces, first label, first assignee (nobody matched: anyone), open or done, how many and the order"],
                ["**Widget connector**, **iframe**, smart links shown as a card or an embed", "A video when the address is YouTube or Vimeo (it plays where Settings → Security → Video sites allows it), else a [link card](link-cards.html) with the address. Imports never read the linked sites"],
            ]),
            SHOT("page-columns-imported.png", "A page imported from Confluence whose Section and Column macros became a row of two columns"),
            P("Filters the Wiki doesn't have (an excluded label, a space that isn't in the Wiki, an author, a date range, a page) are dropped, so a list may show more than it did in Confluence; the import report counts these lists. See [What the import report says](import-and-export.html#what-the-import-report-says)."),
            P("Where Kee is on, the person who imported can have Kee tidy the imported pages afterwards, as proposals they apply (the **Import cleanup** feature, on by default in **Settings → Kee → Features and access**). See [Tidy imported pages with Kee](kee-import-cleanup.html)."),
            H("What isn't imported"),
            UL([
                "View and edit restrictions: imported pages get the space's access.",
                "Files with a blocked extension or larger than the largest file (Settings → Security → Attachments); the report counts them.",
                "Notifications: nobody is told about imported pages, comments or mentions.",
                "Other formats than Confluence XML exports and Markdown.",
            ]),
            H("Limits"),
            TABLE(["Limit", "Value"], [
                ["Export size", "The **Largest export** setting"],
                ["Markdown", "1 MiB per file, 20,000 pages, 200,000 entries in a `.zip`"],
                ["A check", "30 minutes"],
                ["Failed steps", "An import that fails 5 steps in a row stops"],
                ["Waiting", "An unfinished upload is cancelled after a day; a checked import not started within 7 days"],
            ]),
            P("Starting an import raises `space.import.start`, which a [policy](policies.html) can refuse; `space.import.complete` follows when it ends. Both are in the audit log."),
        ])),

    # ---------------------------------------------------------- qna-moderation
    ("qna-moderation", dict(
        label="Q&amp;A moderation", title="Q&amp;A moderation", icon="help",
        desc="Who moderates Q&A, what moderators can do, public questions and the Q&A settings",
        keywords=["q&a", "qna", "questions", "answers", "moderation", "moderator", "duplicate", "lock comments", "merge tags", "public questions", "close", "reopen"],
        blocks=[
            P("Q&A belongs to the organization: questions and answers are shared by everyone in it, outside any space. Organization admins are its **moderators** (super admins too). How people ask and answer is in the user guide's [Q&A](qna.html)."),
            H("Who can do what"),
            TABLE(["", "Members", "Moderators"], [
                ["Read, ask, answer, comment, vote", "Yes", "Yes"],
                ["Edit and delete", "Their own posts (a question only while it has no answers)", "Anyone's"],
                ["Accept an answer", "The asker", "Yes"],
                ["Close and reopen questions", "", "Yes"],
                ["Mark as duplicate", "", "Yes"],
                ["Lock comments on a question", "", "Yes"],
                ["Merge tags", "", "Yes"],
                ["See a post's earlier versions", "Their own", "Anyone's"],
                ["Make a question public", "Their own, before anyone answers or comments", "Any time"],
            ]),
            P("Nobody votes on their own posts. Moderators' changes to other people's posts, and every delete, are recorded in the [audit log](logging-and-audit.html)."),
            H("Moderator actions"),
            UL([
                "**Mark as duplicate**: points readers to the original question; a duplicate takes no new answers. **Not a duplicate** reopens it. Deleting an original closes its duplicates.",
                "**Lock comments**: only moderators can comment or change comments on that question until it is unlocked.",
                "**Merge** a tag into another: its questions and followers move, and the tag goes.",
                "**Close** or **Reopen** a question.",
            ]),
            H("Q&A settings"),
            SHOT("qna-moderation-settings.png", "Q&A → Settings: Allow public questions"),
            P("**Q&A → Settings** (moderators) has one setting for the organization:"),
            UL([
                "**Allow public questions**: askers can make a question public before anyone answers or comments, and moderators at any time. Anyone can then read it, its answers and comments, with the writers' names, without signing in, under **Public questions**. Turning it off hides public questions again.",
                "Public questions also need [anonymous access](anonymous-access.html) for the installation; while it's off, they show only to signed-in people.",
            ]),
            STEPS([
                "Choose **Q&A** in the left menu, then **Settings**. Only Q&A moderators see it.",
                "Turn on **Allow public questions**.",
                "If the page says anonymous access is off, ask an administrator to turn it on under **Settings → Security**; until then public questions show only to signed-in people.",
            ], howto="allow-public-questions", task="Let Q&A questions be read by people who are not signed in"),
            H("Limits and alerts"),
            UL([
                "Per person: 30 questions an hour, 120 answers, 600 votes, 240 comments, 240 edits and deletes.",
                "Followers of a question or tag get in-app alerts for new answers, questions, comments and accepted answers; there are no Q&A emails yet.",
                "Reputation (+10 per upvote, −2 per downvote, +15 per accepted answer) is recomputed every 15 minutes.",
                "Every create, change, close, accept and delete raises an [event](events.html) (`qna.*`), so [policies](policies.html) can refuse them and [automation](automation.html) can react.",
            ]),
        ])),

    # -------------------------------------------------------- template-library
    ("template-library", dict(
        label="Template library", title="The template library", icon="file",
        desc="The templates every space can start pages from: the ready-made ones, your own, switching them off, and who manages them",
        keywords=["templates", "template library", "blueprint", "page tree", "ready-made", "sample templates", "wiki_templates:manage", "reset", "customise", "settings"],
        blocks=[
            P("The template library holds the templates every space offers under **New page**. A template is one page or a tree of pages. Spaces can switch a library template off for themselves, keep a customised copy, and have templates of their own; how that looks to space admins and writers is in the user guide's [Copies and templates](copies-and-templates.html)."),
            SHOT("template-library.png", "Settings → Templates: the library with each template's group, pages, last change, use in spaces and its switch"),
            H("Who manages it"),
            P("**Settings → Templates** needs the `wiki_templates:manage` permission, which super admins have. It is a permission of the installation: no space role grants it. The library is part of every licence tier."),
            H("Ready-made templates"),
            P("A new installation, and an existing one after upgrading, gets twelve templates marked **Ready-made**:"),
            TABLE(["Template", "Group", "Pages"], [
                ["Meeting notes", "Meetings", "1"],
                ["Retrospective", "Meetings", "1"],
                ["Weekly status report", "Meetings", "1"],
                ["Decision record", "Engineering", "1"],
                ["Postmortem", "Engineering", "1"],
                ["Service runbook", "Engineering", "1"],
                ["Software release", "Engineering", "5: the plan, test plan, release notes and rollback plan under a home page"],
                ["How-to guide", "Docs", "1"],
                ["Knowledge base", "Docs", "6: getting started, how-to guides, FAQ and troubleshooting under a home page"],
                ["Product requirements", "Product", "1"],
                ["Project workspace", "Product", "6: scope, meeting notes, decisions, risks and status updates under a home page"],
                ["Team space starter", "Team", "7: how we work, team rituals, onboarding, tools and access, and contacts under a home page"],
            ]),
            P("You can change a ready-made template like any other. **Reset to original** puts its name, description, group, icon, content and pages back to what the Wiki ships; whether it is on stays as it is. A ready-made template can't be deleted: switch it off instead."),
            H("What you can do"),
            TABLE(["Action", "What it does"], [
                ["**New template**", "Opens the template editor on an empty template. **From an existing page** makes one from a page you can edit instead, without its images, optionally with the pages under it."],
                ["The switch in the **On** column", "Off: no space offers the template. Spaces that keep a customised copy of it keep their copy."],
                ["**Edit content**", "Opens the template in the template editor: its pages, their content and its details."],
                ["**Name, group and icon**", "The name, the description people see when they pick a template, the group it is listed under and its icon."],
                ["**On in new spaces**", "Whether spaces offer the template unless they decide otherwise. Off: a space admin has to switch it on in the space."],
                ["**Preview**", "Shows the template's pages and content as people see them under New page."],
                ["**Duplicate**", "Adds a copy with its content, pages, group and icon."],
                ["**Delete**", "Spaces can no longer start pages from it. Spaces' own copies stay, and pages made from it keep their content."],
            ]),
            STEPS([
                "Open **Settings → Templates**.",
                "Choose **New template**, or **From an existing page** to start from a page you can edit.",
                "Write the template's pages in the template editor, and set its **Name, group and icon**.",
                "Make sure its switch in the **On** column is on, and choose whether it is **On in new spaces**.",
            ], howto="add-a-template-to-the-library", task="Add a template every space can start pages from"),
            P("The **Spaces** column says where each template is offered (**On in all 12**, **Off in 2 of 12**) and how many spaces keep a customised copy."),
            H("Limits"),
            UL([
                "200 templates in the library, and 100 of its own in each space.",
                "50 pages and 5 levels in one template, counting its top page.",
                "Templates hold text, tables and blocks, without images or videos.",
            ]),
            H("Audit and events"),
            UL([
                "Every change to a template is in the [audit log](logging-and-audit.html).",
                "Templates raise [events](events.html): `page.template.create`, `page.template.update` (a reset and a save in the editor too), `page.template.delete`, and `page.template.switch` when a space turns a library template on or off for itself. [Policies](policies.html) can refuse them and [automation](automation.html) can react.",
            ]),
            H("API"),
            TABLE(["Method", "Path", "Permission", "What it does"], [
                ["GET", "`/api/templates`", "`wiki_templates:manage`", "The library"],
                ["POST", "`/api/templates`", "`wiki_templates:manage`", "Add a template: written (`content`, `pages`) or from a page"],
                ["PUT", "`/api/templates/{id}/content`", "`wiki_templates:manage`", "Save a template whole: its details, top page and every page under it"],
                ["POST", "`/api/templates/{id}/reset`", "`wiki_templates:manage`", "Reset a ready-made template to the original"],
                ["GET", "`/api/spaces/{key}/templates`", "Read the space", "The templates the space offers; `?all=1` (space admins) adds the library ones it has switched off or replaced"],
                ["PUT", "`/api/spaces/{key}/templates/{id}/enabled`", "Space admin", "Switch a library template on or off for the space"],
                ["PUT", "`/api/spaces/{key}/templates/{id}/content`", "Space admin", "Save one of the space's templates whole"],
            ]),
            P("`GET /api/openapi.json` describes every template route with its fields."),
        ])),

    # -------------------------------------------------------- anonymous-access
    ("anonymous-access", dict(
        label="Anonymous access", title="Anonymous access", icon="lock",
        desc="Let signed-out visitors read public spaces and public questions, and what they can and can't see",
        keywords=["anonymous", "anonymous access", "public", "public spaces", "guest", "signed out", "without signing in", "public questions", "internet"],
        blocks=[
            P("By default everyone signs in. With **anonymous access** on, a space can be made **public**, and anyone who reaches the Wiki can read it without signing in. It is one switch for the whole installation."),
            H("Turn it on"),
            SHOT("anonymous-access-setting.png", "Settings → Security → Anonymous access"),
            STEPS([
                "Open the setting|**Settings → Security → Anonymous access** (`settings:write`).",
                "Allow anonymous access to public spaces|Turn it on and save. The page warns that anyone who can reach the server will be able to read everything in public spaces.",
                "Make spaces public|A space's admins set **Visibility → Public** in the space's **Settings**. Private and internal spaces always need a sign-in.",
            ]),
            P("Turning it off again makes every public space readable only by signed-in people; the spaces keep their visibility for when it is turned back on."),
            H("What signed-out visitors see"),
            SHOT("anonymous-access-guest-space.png", "A public space as a signed-out visitor sees it, with Sign in at the top"),
            UL([
                "The list of public spaces, a public space's overview, its published pages and their history.",
                "**Public questions** in Q&A, with their answers and comments, when Q&A moderators allow them (see [Q&A moderation](qna-moderation.html)).",
                "People's names as the authors typed them in mentions, but not who created or changed pages.",
                "Not drafts, members or settings. The pages for labels and search aren't shown to them, but public content can be searched and listed by label through the API (`/api/search`), so treat everything in a public space as findable.",
            ]),
            H("Things to know"),
            UL([
                "Anonymous visitors share the anonymous rate limit per address (`RATE_LIMIT_ANON`, 60 a minute by default; see [Rate limits](rate-limits.html)). Behind a proxy, set `FRONTEND_BEHIND_PROXY=true` on the web app and `TRUSTED_PROXIES` on the server so each visitor has their own address (see [Install the Wiki](install.html)).",
                "Their page views are counted in [analytics](analytics-settings.html) without any identity.",
                "Whether search engines index public spaces is a separate setting: [Search engines](search-engines-and-robots.html).",
                "A public page's history shows text since removed: check a page's history before making its space public.",
            ]),
            WARN("Anything in a public space can be read and copied by anyone who reaches the server. Keep anonymous access off unless the Wiki is meant to publish to people without accounts."),
        ])),

    # ------------------------------------------------ search-engines-and-robots
    ("search-engines-and-robots", dict(
        label="Search engines", title="Search engines and robots.txt", icon="search",
        desc="Choose what the Wiki's robots.txt tells Google, Bing and other crawlers",
        keywords=["robots.txt", "robots", "search engines", "google", "bing", "crawler", "seo", "index", "noindex", "sitemap", "public spaces"],
        blocks=[
            P("The Wiki serves `/robots.txt`, the file search engines read before crawling. **Settings → Security → Search engines** (`settings:write`) decides what it says, for the whole installation."),
            SHOT("search-engines-and-robots-settings.png", "Settings → Security → Search engines: the three choices and what robots.txt serves now"),
            H("The choices"),
            TABLE(["Choice", "robots.txt"], [
                ["**Index nothing** (the default)", "Asks every crawler to stay away"],
                ["**Index public spaces**", "Allows the space list and the published pages of public spaces, and nothing else. Page history stays blocked. Blocks everything while [anonymous access](anonymous-access.html) is off"],
                ["**Use my own robots.txt**", "Serves the text you enter, as it is (up to 16 KiB, no control characters). It is kept when you pick another choice"],
            ]),
            P("**What robots.txt serves now** shows the saved result. After a change, each server takes up to a minute to serve it, and crawlers may keep the old file for up to five minutes more. If the server can't be reached, robots.txt answers `503` so crawlers try again later rather than reading a wrong answer."),
            H("Things to know"),
            UL([
                "robots.txt is a request, not access control: what crawlers can read is decided by anonymous access and each space's visibility.",
                "**Index public spaces** lists at most 1,000 public spaces; any beyond stay blocked.",
                "There is no sitemap yet.",
                "Changing the setting raises the `robots.update` event and is audited.",
            ]),
        ])),

    # ---------------------------------------------------------------- upgrades
    ("upgrades", dict(
        label="Upgrades &amp; maintenance", title="Upgrades &amp; maintenance", icon="history",
        desc="Upgrade a single server or a cluster safely, roll back, and plan routine maintenance",
        keywords=["upgrade", "update", "rolling upgrade", "rollback", "migration", "maintenance", "downtime", "version", "release"],
        blocks=[
            P("The Wiki upgrades in place: a new version starts, migrates the database once, and carries on. In a cluster, servers are upgraded one at a time while the others keep serving."),
            H("What happens during an upgrade"),
            UL([
                "**Migrations run once.** The first new server to start takes a database lock and applies the migrations; others wait for it.",
                "**Old and new run side by side.** Database changes are backward compatible for one release.",
                "**The newest leads.** Leadership moves to a server on the highest version.",
                "**Open pages notice.** People see **A new version is available** with **Reload** and **Later**.",
            ]),
            H("New blocks during an upgrade"),
            P("A release can bring new blocks for pages. So that a server or a browser that doesn't know a block yet can't drop it from a page, new blocks are offered only once the whole installation can keep them:"),
            UL([
                "**Upgrade the web app first**, then the servers. A web app newer than the servers offers nothing new until the servers catch up.",
                "If the servers go first, editors whose web app is still the older one can't connect to a page: the editor says **A newer version of the wiki is running. Reload the page to go on editing**, and keeps changes not yet saved until they reload. Upgrade the web app to end it.",
                "The \"/\" menu, the Insert menu and imports offer a new block about a minute after the last server runs the new version. Until then imports keep those macros as before (imported macros or text).",
                "Editor tabs still running the previous web app are disconnected within about 30 seconds of the upgrade and asked to reload.",
                "Rolling back: a previous version doesn't know the new blocks and drops them from a page edited or published through it. Roll back before people use them, or restore the backup taken before the upgrade.",
            ]),
            H("Before you upgrade"),
            STEPS([
                "Read the notes|The [changelog](changelog.html) for every version between yours and the new one.",
                "Check health|**Settings → Advanced → System check** shows no problems, and no backup or import is running.",
                "Back up|Run a backup (**Settings → Backups**) and make sure it's verified. Note the current version (**?** → **About**).",
                "Plan the window|A single server is down while it restarts. A cluster needs no downtime.",
            ]),
            H("Single server"),
            STEPS([
                "Stop the server|`SIGTERM`; it finishes requests and jobs, then exits.",
                "Replace the programs|The server and the web app; keep the data folder and the environment.",
                "Start the server, then the web app|Watch the log until it serves.",
                "Check|About shows the new version; the system check is clean; a page opens and can be edited.",
            ]),
            H("Cluster"),
            STEPS([
                "Upgrade one server|Stop it, replace it, start it.",
                "Watch|**Settings → Clustering** shows it **active** on the new version.",
                "Continue|One server at a time.",
                "Upgrade the web apps|They're stateless. Roll them before the servers when the release brings new blocks (see [above](#new-blocks-during-an-upgrade)); otherwise after.",
            ]),
            H("Rolling back"),
            UL([
                "Within one release, the previous version can run against the upgraded database: put the previous programs back the same way.",
                "Further back, restore the backup taken before the upgrade (see [Backups](backups.html)). Changes made since the backup are lost.",
            ]),
            H("Routine maintenance"),
            TABLE(["How often", "Task"], [
                ["Daily (automatic)", "Backups, retention jobs, analytics and import clean-up: see [Scheduled jobs](scheduler.html)"],
                ["Weekly", "The system check, failed jobs and event deliveries"],
                ["Monthly", "Review super admins, space admins of important spaces, service accounts and long-lived tokens; storage growth"],
                ["Each release", "Upgrade within a reasonable time"],
                ["Yearly", "Rehearse a restore; rotate credentials for storage, email and identity providers; renew the licence"],
            ]),
            H("Moving or replacing servers"),
            UL([
                "A new server joins with `CONFIG_ENCRYPTION_KEY` and `DATABASE_URL`; it needs no setup.",
                "The installation ID is kept in the database, so moving servers with the same database keeps the licence. A new database needs a new licence: see [Licensing](licensing.html).",
            ]),
        ])),

    # ------------------------------------------------------------ known-issues
    ("known-issues", dict(
        label="Known issues", title="Known issues", icon="alert",
        desc="Limitations and known problems in the current release, with workarounds",
        keywords=["known issues", "limitations", "bugs", "workaround", "not supported", "caveats", "not yet"],
        blocks=[
            P("What doesn't work yet, or works with a catch, in the current release, and what to do meanwhile. Fixed issues leave this list and appear in the [changelog](changelog.html)."),
            NOTE("Last reviewed: 21 November 2026."),
            H("Installation"),
            TABLE(["Issue", "Workaround"], [
                ["No container images or Helm chart yet", "Run the server and web app as services, or in containers you build"],
                ["Live editing needs `/api/ws` routed to the server; without it the editor can't connect", "Route it (see [Install the Wiki](install.html))"],
                ["The Wiki can't be served under a path", "Give it its own host name"],
                ["Some platform screens still name Depotex (for example **Settings → General**'s address field, and the anonymous access text about downloads)", "—"],
            ]),
            H("Spaces, pages and media"),
            TABLE(["Issue", "Workaround"], [
                ["No per-page view or edit restrictions", "Put pages that need other access in their own space"],
                ["Nothing stops an admin from removing a space's last admin", "A super admin adds an admin back"],
                ["No per-space attachment quota, no virus scan of attached files, no \"Download all\" and no previews of Office files (they download)", "Keep the [blocked extensions](files-and-attachments.html#for-administrators) for programs"],
                ["Attachments lists and galleries show only the files of their own page; an old version's list shows today's files", "—"],
                ["Tasks can't be ticked from a task report, and blog posts' tasks aren't in reports", "Open the task's page"],
                ["A link card's text isn't refreshed after it is saved; previews read UTF-8 pages only", "Change the card and fill it in again, or type the text"],
                ["Videos are played as uploaded: no transcoding", "Upload MP4 (H.264) or WebM that browsers play"],
                ["PDF export draws Latin, Greek and Cyrillic text only", "Export to Word for other scripts"],
                ["A scheduled publish runs up to a minute late, and any edit after scheduling cancels it", "Schedule again after editing"],
                ["Review-by reminders go only to whoever set the date, as an in-app alert", "—"],
                ["Tablets get the compact desktop sizes of controls", "—"],
            ]),
            H("Search, imports and Q&A"),
            TABLE(["Issue", "Workaround"], [
                ["Search finds page text only in the newest published version, not in drafts, earlier versions or attached files", "Open the page's history or the attachment"],
                ["Imports: Confluence XML exports and Markdown only; restrictions aren't imported, and lists with filters the Wiki doesn't have are widened", "Recreate restrictions as separate spaces; check the lists the report counts"],
                ["Q&A, comment and mention alerts are in-app only, with no email", "—"],
                ["Signed-out visitors can't use search or label pages in the web app", "Link to pages directly"],
                ["No sitemap; robots.txt lists at most 1,000 public spaces", "—"],
            ]),
            H("Analytics and calendars"),
            TABLE(["Issue", "Workaround"], [
                ["Analytics retention can't be changed, and recording who read what can't be turned off", "See [Analytics](analytics-settings.html) for what is kept"],
                ["Analytics days are UTC days", "—"],
                ["Calendar feeds send at most 2,000 entries over a year and a month; repeats can't have exceptions", "—"],
                ["A calendar feed's secret is in its address, which a proxy may log", "Leave queries out of the proxy log for `/api/calendar/ical`"],
            ]),
            H("Kee"),
            TABLE(["Issue", "Workaround"], [
                ["Ask Kee doesn't read blog posts or Q&A yet. Of attached files it reads PDF text, Word (`.docx`), Excel (`.xlsx`) and plain text only: not presentations, scans, archives, old `.doc` or `.xls`, or password-protected files. Images are read only when you add them to a question", "Open them yourself"],
                ["Excel values are read as stored: dates show as numbers, and a formula shows its last saved result, or nothing when the file holds none", "Ask about the columns, or save the workbook again in Excel"],
                ["Search by meaning compares every passage a person may read, with no vector index, so it slows down on very large Wikis. It needs the `vector` extension in Postgres, and a server notices it only after a restart", "Use the budget on **Settings → Kee → Search**, or leave it off"],
                ["The switch on the **Search** tab is the same as **Search by meaning** on the Features tab; the other tab shows the old state until the page is reloaded", "Reload the page"],
                ["Questions you ask Kee are matched by meaning under the scheduled budget, not your own daily limit", "None needed"],
                ["The weekly space digest is shown only on the space's overview, with no email, and is written in the language of whoever turned it on", "Open the space's overview"],
                ["Merging a duplicate page brings over the other page's text only: its images, mentions and embedded items stay on the old page", "Copy them by hand before moving the old page to the trash"],
                ["The duplicate warning isn't shown for pages made by Ask Kee or an outside AI app, and never for pages under a page lock", "None needed"],
                ["Label suggestions offer new words, but know only the labels already used in the space", "Add other labels by hand"],
                ["A suggested alt text can be longer than the 150 characters asked for", "Shorten it before choosing **Use these**"],
                ["Outside AI apps with the administer scope list the administration tools to people who lack the permission; each call is refused", "None needed"],
                ["Kee proposes changes to pages, comments and labels only; it can't move, archive, delete or restore pages, or change spaces, blog posts or questions. A whole-page change shows the whole page, without folding unchanged parts", "Make those changes yourself"],
                ["A proposal is refused as **Page changed** when the page's draft holds edits it hasn't seen, even small ones", "**Ask again** on the page as it is now"],
                ["In the unlikely case a server stops between writing a new page or comment from a proposal and marking it applied, applying it again later can make it twice", "Delete the copy"],
                ["The \"with Kee\" mark on a version names the model, not the agent used. A picked agent isn't remembered across page loads. Reassigning an agent to someone other than yourself has no screen (only **Take over**)", "None needed"],
                ["A space can be given an agent for use only, not to edit", "Share with a group instead"],
                ["Outside AI apps: ending a connection blocks it but doesn't remove the person's sign-in or key, and can't be undone; the call limit and write budgets are counted per server without Redis; usage and the connections list cover the whole installation; each AI app is registered by an administrator", "The person removes the connection and signs in again"],
                ["The Outside AI apps tab edits who may connect by role only", "Add groups in the Kee permissions grid on **Features and access**"],
                ["Scheduled help: the findings' **Update**, **Archive** and **Review** are advice only, not actions; suggestions for questions match words in page titles only; the scheduled budget sends no alert at 80% or 100%", "Act on the page yourself; check the card on Features and access"],
                ["**Show me** walkthroughs can't point at the controls of the Wiki's own settings pages, of Kee's Search tab, or of several space settings tabs (trash, import, locked pages, analytics, blog) yet: their how-tos are shown as text", "Follow the steps in these docs"],
                ["Some screens of outside AI apps say \"the assistant\" or \"AI\" where they mean Kee", "None needed"],
                ["No screen for how long Ask Kee conversations are kept (30 days by default), or for the feedback people give on answers", "Use the API: `GET`/`PUT /api/wiki/ai-settings` (Manage Kee settings) and `GET /api/ai/feedback/summary` (See usage)"],
                ["While an answer or summary is being written, Markdown marks such as `**` show as typed; the formatted text replaces them when it is done", "None needed"],
                ["The Ask Kee panel lies over the right side of the page instead of narrowing it", "Close it to read the page"],
                ["In the editor, the selection's Kee button can lie over the line below the selection, and the panel for a selection opens under the whole block", "None needed"],
                ["A version is marked \"with Kee\" by time: a result applied and then removed by hand still marks the next version", "None"],
                ["Write the page is offered only on an empty page, and reads no other pages or files", "Write a short request with what the page needs"],
                ["The Bedrock model list doesn't show the regions of each inference profile, and adding a provider doesn't list its models in one step", "Add models after saving the provider"],
                ["Some notices say \"AI\" instead of \"Kee\" (the daily limit, provider and budget messages, the system check and alerts)", "None needed"],
            ]),
            H("Whiteboards"),
            TABLE(["Issue", "Workaround"], [
                ["The read-only view and whiteboard blocks refresh every 30 seconds, not live", "Open the whiteboard to see it live"],
                ["Private mode hides notes on screen, in downloads and in search, but their text reaches the browsers of everyone who can draw on the board; votes aren't secret either", "Don't use private mode for confidential input"],
                ["A template or copy made while private mode is on gets the hidden notes as blank notes", "Reveal the notes first"],
                ["Starting a timer or a vote isn't in the audit log and raises no event", "—"],
                ["Adding a node to a mind map lays out the whole map again, moving nodes placed by hand", "Undo the addition to put them back"],
                ["Word and PDF downloads of a page show a whiteboard block as a link, not its picture", "Download the whiteboard itself as SVG or PDF"],
                ["The PDF download doesn't turn rotated text, and wraps text a little differently from the board", "Use the SVG download"],
                ["Copies of a whiteboard stay in its space", "Copy its items and paste them into a new whiteboard in the other space"],
            ]),
        ])),

    # --------------------------------------------------------------------- faq
    ("faq", dict(
        label="FAQ", title="Frequently asked questions", icon="help",
        desc="Answers to the questions administrators ask most",
        keywords=["faq", "questions", "help", "how do i", "license", "licence", "redis", "backup", "upgrade", "confluence", "public", "locked out"],
        blocks=[
            H("Licensing"),
            UL([
                "**How do I get a licence?** Read the installation ID (setup wizard, Settings → Application → Licensing, or `./wiki-server --machine-id`) and send it through [vectored.dev/#contact](https://vectored.dev/#contact) or to " + SUPPORT_MAIL + ". See [Licensing](licensing.html).",
                "**Why is there no Analytics menu?** Page analytics need a Pro licence.",
                "**What happens when the licence expires?** Any grace period first, with banners; then only sign-in, health checks and the licence page answer, until a new licence is applied. Nothing is deleted.",
                "**Does the Wiki call home?** No. It doesn't need internet access to check its licence.",
            ]),
            H("Installation"),
            UL([
                "**Do I need Redis?** Not for a single server. A cluster needs it. See [Single server & cluster](deployment-modes.html).",
                "**Which PostgreSQL?** 15 or later; managed services work.",
                "**People can't edit pages together; the editor says it can't connect.** Route `/api/ws` to the server with WebSocket upgrades allowed. See [Install the Wiki](install.html).",
                "**Video uploads fail with 413.** The proxy in front of the Wiki refuses large bodies: let it take 201 MiB (nginx: `client_max_body_size 201m`).",
                "**Can I set it up with no browser?** Yes: [Set up without the UI](headless-setup.html).",
            ]),
            H("Content"),
            UL([
                "**How do we move from Confluence?** Export each space (XML, full export) and import it into a Wiki space: [Imports](confluence-import.html). Importing again later updates what the first import made.",
                "**Who can create spaces?** Super admins. They then hand a space to its team with the Admin role.",
                "**How do we publish a space to the internet?** Turn on [anonymous access](anonymous-access.html), make the space public, and choose what [search engines](search-engines-and-robots.html) may index.",
            ]),
            H("Access"),
            UL([
                "**I'm locked out: single sign-on is down.** Start one server with `SSO_ENFORCEMENT_OVERRIDE=true`, sign in with a password as a super admin, fix the provider, then remove the variable.",
                "**An account is locked after failed sign-ins.** It unlocks after `AUTH_LOCKOUT_DURATION` (15 minutes), or an administrator unlocks it in Settings → Access management → Users.",
                "**Someone's calendar address leaked.** They make a new one on the Calendar page; ending their sessions also stops it. See [Calendar feeds](calendar-feeds.html).",
                "**Why does everyone seem to come from the same address?** The web app ignores forwarding headers unless `FRONTEND_BEHIND_PROXY=true` is set on it, and the server trusts them only from the proxies in `TRUSTED_PROXIES` and removes them otherwise. Set both; the system check's **Forwarded headers** line names an address that was refused. See [Install the Wiki](install.html).",
            ]),
            H("Data"),
            UL([
                "**What's in a backup?** See [Backups](backups.html).",
                "**I lost CONFIG_ENCRYPTION_KEY.** Stored credentials and backups made with it can't be read; there is no recovery. Keep the key in a secret store and with your backup records.",
                "**How long are page views kept?** Raw views 90 days, daily totals as long as the page. See [Analytics](analytics-settings.html).",
            ]),
        ])),

    # ----------------------------------------------------------------- support
    ("support", dict(
        label="Support", title="Support", icon="life-buoy",
        desc="How to get help, what to send with a support request, and how to report a security problem",
        keywords=["support", "help", "contact", "ticket", "support request", "bug report", "severity", "diagnostics", "logs", "about", "copy details", "security report"],
        blocks=[
            P("Vectored supports the Wiki. Write to **" + SUPPORT_MAIL + "**, or use the form at [vectored.dev/#contact](https://vectored.dev/#contact). Licences, renewals and changes of tier go the same way."),
            ACCESS_NOTE,
            H("Before you write"),
            STEPS([
                "Check the system check|**Settings → Advanced → System check** often names the problem (Pro).",
                "Check known issues|[Known issues](known-issues.html) and the [FAQ](faq.html) may already have the answer.",
                "Check the server log|Errors carry a request ID; the log line with it says what went wrong.",
                "If the server can't start|It runs in [recovery mode](recovery.html), which lists what's wrong.",
            ]),
            H("What to send"),
            TABLE(["What", "Where to find it"], [
                ["Version, build and the server that answered", "**?** → **About** → **Copy details**, or the footer's copy button"],
                ["Your licence ID", "Settings → Application → Licensing"],
                ["Single server or cluster, and how many servers", "Settings → Clustering"],
                ["What you did, what you expected, what happened", "Steps to reproduce; the exact error, with its request ID"],
                ["When it started, and what changed then", "An upgrade, a setting, the proxy, the identity provider"],
                ["Logs from the time it happened", "Settings → Logging → Files → export, or your log platform"],
                ["For editing problems", "The browser and its version, and whether `/api/ws` reaches the server"],
            ]),
            WARN("Never send `CONFIG_ENCRYPTION_KEY`, passwords, API tokens, calendar addresses, licence files or backups. Log exports are redacted, but look through anything before you send it."),
            H("Severity"),
            TABLE(["Severity", "Meaning", "Examples"], [
                ["**1 — Critical**", "Production down or data at risk; no workaround", "No server starts; pages can't be read"],
                ["**2 — High**", "A major function fails; a workaround is hard", "Nobody can edit; single sign-on fails for everyone"],
                ["**3 — Normal**", "A function doesn't work as documented; a workaround exists", "An import fails; a setting doesn't apply"],
                ["**4 — Low**", "Questions, documentation, feature requests", "How to configure something"],
            ]),
            H("Security problems"),
            P("To report a vulnerability in the Wiki, email **security@vectored.dev** (or " + SUPPORT_MAIL + " with **Security** in the subject) instead of discussing it in public. Include what you found, how to reproduce it, and the version."),
            H("Your own help desk"),
            P("If your team supports the Wiki's users itself, point the **?** menu's links at your own service desk: **Settings → General → Help menu**. A `mailto:` link fills in the version and server for the person writing."),
        ])),
]
