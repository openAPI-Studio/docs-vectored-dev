"""Admin guide: the setup wizard, step by step, and setting up without the UI.
Keep in step with libs/platform/setup (wizard, configfile.go) and
apps/depotex/backend/setup.example.yaml in the depotex repo."""
from engine import H, P, UL, TABLE, NOTE, WARN, STEPS, CODE, SHOT

SETUP = [
    ("setup-wizard", dict(
        label="Setup wizard", title="Setup wizard", icon="rocket",
        desc="Set up a new installation step by step: license, database, storage, cache and the first administrator",
        keywords=["setup", "wizard", "first run", "setup key", "setup token", "installation id", "license", "database", "storage", "redis", "administrator", "restore"],
        blocks=[
            P("A server that has never been set up starts in **setup mode**: it serves only the setup wizard, protected by a one-time setup key. The wizard collects what the installation needs, stores every credential encrypted in the database, and restarts the server into normal mode. It takes about five minutes once PostgreSQL and your storage exist."),
            SHOT("setup-wizard.gif", "The setup wizard from the license to the first administrator"),
            H("Before you start"),
            TABLE(["You need", "Details"], [
                ["A PostgreSQL database", "An empty database and a role that owns it (it creates tables, and roles for plugins that use a database: `CREATEROLE`). Not a superuser. See [Plan an installation](install-planning.html#postgresql)."],
                ["Storage for artifacts", "A directory on the server, an S3 bucket, a MinIO bucket or an Azure Blob container, which must already exist."],
                ["Redis (optional)", "Needed only for a cluster. One server, a Sentinel group or a Redis Cluster."],
                ["`CONFIG_ENCRYPTION_KEY`", "Set on the server before its first start, and kept safe: it encrypts every stored credential. See [Environment variables](environment-variables.html#bootstrap)."],
                ["A license", "Bound to the installation ID the wizard shows on its first step. See [Get a license](licensing.html#get-a-license)."],
            ]),
            H("Open the wizard"),
            STEPS([
                "Start the server|With `DATABASE_URL` and `CONFIG_ENCRYPTION_KEY` set (see [Install Depotex](install.html)).",
                "Find the setup link|The log prints a line like `open the setup wizard … setup_url=https://depotex.example.com/setup?token=…`. On Kubernetes the key is `SETUP_TOKEN` in the keys file `prime-secrets.sh` wrote.",
                "Open it|The page reads the key and removes it from the address bar. Anyone without the key gets nothing from setup mode, so nobody else who can reach the server can take it over first.",
                "Choose your language|The language menu at the top. The first administrator keeps it as their language.",
            ]),
            NOTE("The key changes each time the server restarts, unless you set it with `SETUP_TOKEN` (do that when several servers share one setup, or to script it). Requests in setup mode are limited to `RATE_LIMIT_SETUP` a minute per address (30 by default)."),
            H("Step 1: License"),
            SHOT("setup-wizard-license.png", "Setup wizard, License: the installation ID to request a license with, and the license to upload or paste"),
            UL([
                "**Installation ID**: what the license is bound to. **Copy installation ID** and send it with your license request (see [Get a license](licensing.html#get-a-license)). The same ID is printed by `./server --machine-id`.",
                "**Upload file** (or drop the `.json` file on the box) or **Paste text**, then **Validate license**. A valid license shows its licensee, tier, expiry and user and server limits.",
                "**Next** stays off until the license is valid for this installation.",
            ]),
            H("Step 2: Database"),
            SHOT("setup-wizard-database.png", "Setup wizard, Database: the connection, its checks, and what the database already holds"),
            UL([
                "Enter the database to keep Depotex's data in (the wizard doesn't fill it in from `DATABASE_URL`, which is only what the server boots with). Use **Connection string**, or **Connection details** (host, port, database name, user name, password and SSL mode: Disable, Prefer, Require, Verify CA or Verify full).",
                "**Test connection** checks that Depotex can sign in, that it may create tables, and whether the database is empty.",
                "A database that already holds tables is flagged: setup runs migrations, which may clash with what's there. **Wipe database** deletes every table, all data and every schema in it, after you confirm. Use it only on a database you made for Depotex.",
                "Add `pool_max_conns` to the URL to size the connection pool now: a value set at first boot is kept. See [Database connections](deployment-modes.html#database-connections).",
            ]),
            H("Step 3: Storage"),
            SHOT("setup-wizard-storage.png", "Setup wizard, File storage: the backend and its settings, checked before you go on"),
            TABLE(["Backend", "Settings"], [
                ["**Local filesystem**", "**Base path**: a directory on the server. In a cluster, a volume mounted at the same path on every server."],
                ["**AWS S3**", "**Bucket**, **Region**; **Access key ID** and **Secret access key**, or leave both empty to use the server's IAM role; optionally a **Role to assume** and its **External ID**."],
                ["**MinIO (S3-compatible)**", "**Endpoint** (`host:port`), **Bucket**, **Use SSL**, **Access key** and **Secret key**"],
                ["**Azure Blob Storage**", "**Container**, **Storage account** and **Storage key** (base64)"],
            ]),
            P("The bucket or container must exist. The wizard writes and reads a test object before it lets you go on; credentials are stored encrypted. Change storage later in **Settings → Storage** (see [Storage](storage.html))."),
            H("Step 4: Cache"),
            SHOT("setup-wizard-cache.png", "Setup wizard, Cache: an optional Redis URL"),
            UL([
                "Leave it empty for a single server: everything works without Redis.",
                "For a cluster, give a **Redis URL**: `redis://` or `rediss://` for one server, `redis+sentinel://…?master_name=…` for Sentinel, `redis+cluster://…` for a Redis Cluster. **Connection details** fill in a single server only. See [Single Node & Cluster → Redis](deployment-modes.html#redis).",
                "**Test connection** connects before you go on.",
            ]),
            H("Step 5: Administrator, or restore"),
            SHOT("setup-wizard-admin.png", "Setup wizard, Administrator: the first super admin, or restore from a backup"),
            P("Choose how this installation starts:"),
            UL([
                "**Create an administrator**: full name, email and password of the first **super admin**. Choose a long password (the wizard takes 8 characters or more; people's passwords later need `AUTH_PASSWORD_MIN_LENGTH`, 12 by default).",
                "**Restore from a backup**: bring back an installation from a `.dxbak` file, uploaded here (sent in pieces, resumed after a dropped connection) or copied beforehand into `backups/import/` of the storage from step 3. The backup must have been made with the same `CONFIG_ENCRYPTION_KEY`; people sign in with the backup's accounts afterwards; artifacts themselves aren't in backups and must already be in that storage. See [Backups → Disaster recovery](backups.html#disaster-recovery).",
            ]),
            P("**Complete setup** saves everything, runs the database migrations and restarts the server in normal mode. The page waits and then takes you to sign-in."),
            H("After setup"),
            STEPS([
                "Sign in|As the administrator you created.",
                "Set the Depotex address|**Settings → General**: the address people and package managers use. Links in emails, single sign-on and package metadata depend on it.",
                "Configure email|**Settings → Application → Email**, so invitations and password resets work. See [Email](email.html).",
                "Bring people in|Directories, single sign-on or invitations. See [Users & Directories](users-and-directories.html).",
                "Turn on backups|**Settings → Backups**. See [Backups](backups.html).",
                "Check health|**Settings → Advanced → System check** (Pro). See [System Check](system-check.html).",
                "Harden it|Work through the [production checklist](security-hardening.html).",
            ]),
            H("If setup fails"),
            TABLE(["What you see", "What to do"], [
                ["The setup page says the key is missing or wrong", "Open the exact `setup_url` from the newest log line; the key changes on every restart unless `SETUP_TOKEN` is set"],
                ["Database: can't connect or can't create tables", "Check host, port and SSL mode; the role needs to own the database (or `CREATE` on it)"],
                ["Storage isn't accessible", "The bucket or container must exist; check the credentials, region or endpoint, and that the server can reach it (proxy, firewall)"],
                ["Couldn't connect to Redis", "Check the URL scheme for Sentinel or Cluster, the password and TLS (`rediss`)"],
                ["Setup couldn't be completed", "The step named in the message has a value that no longer works; go back to it. The server log says what failed"],
            ]),
            P("Nothing is saved until **Complete setup** succeeds, so you can restart the server and begin again at any point before that."),
        ])),

    ("headless-setup", dict(
        label="Set up without the UI", title="Set up without the UI", icon="terminal",
        desc="Unattended setup from a YAML file for scripts, containers and configuration management",
        keywords=["headless", "unattended", "passive setup", "setup file", "setup.yaml", "SETUP_CONFIG_FILE", "--setup-config", "--machine-id", "automation", "ansible", "terraform", "ci", "gitops", "restore cli"],
        blocks=[
            P("Everything the setup wizard asks can come from a YAML file instead, so a new installation can be set up by a script, a container entrypoint, Ansible, Terraform or a GitOps pipeline with nobody at a browser. This is **passive setup**. The Helm chart uses it too (`setup.mode: passive` or `auto`; see [Install with Helm](helm-chart.html#first-boot-setup))."),
            H("How it works"),
            STEPS([
                "Get the installation ID|`./server --machine-id` prints it and exits. In a container, run the image with `--machine-id` on the host (or pod) that will run Depotex: the ID belongs to that machine.",
                "Get the license|Request it for that ID (see [Get a license](licensing.html#get-a-license)).",
                "Write the setup file|The same sections as the wizard; secrets as `${VARIABLE}` references (below).",
                "Start the server once with it|`--setup-config setup.yaml`, or `SETUP_CONFIG_FILE=setup.yaml`. The server checks the file, sets up, and continues in normal mode.",
                "Remove the file|It's read only on a fresh installation and ignored afterwards; don't leave secrets lying around.",
            ]),
            CODE("""chmod 600 setup.yaml
export CONFIG_ENCRYPTION_KEY="$(cat /run/secrets/depotex-encryption-key)"
export DATABASE_URL='postgres://depotex:…@db.internal:5432/depotex?sslmode=verify-full&pool_max_conns=25'
export ADMIN_PASSWORD="$(cat /run/secrets/depotex-admin-password)"
./server --setup-config setup.yaml"""),
            H("The setup file"),
            P("An annotated example ships as `setup.example.yaml`. Every key:"),
            CODE("""database:
  url: ${DATABASE_URL}           # may be left out when DATABASE_URL is set

cache:
  redis_url: ""                  # empty: single server without Redis; required for a cluster

storage:
  backend: s3                    # local | s3 | minio | azure
  local:
    path: /var/lib/depotex/artifacts
  s3:
    bucket: my-depotex-artifacts
    region: eu-west-1
    access_key: ${S3_ACCESS_KEY} # leave both keys out to use the server's IAM role
    secret_key: ${S3_SECRET_KEY}
    role_arn: ""                 # optional: a role to assume
    external_id: ""              # optional: its external ID
  minio:
    endpoint: minio.internal:9000
    bucket: depotex
    use_ssl: true
    access_key: ${MINIO_ACCESS_KEY}
    secret_key: ${MINIO_SECRET_KEY}
  azure:
    container: depotex
    account: ${AZURE_STORAGE_ACCOUNT}
    key: ${AZURE_STORAGE_KEY}

license:
  file: license.json             # relative to this file; or data: | with the JSON inline

admin:
  email: admin@example.com
  name: Administrator
  password: ${ADMIN_PASSWORD}    # at least 8 characters"""),
            TABLE(["Key", "Required", "Meaning"], [
                ["`database.url`", "When `DATABASE_URL` isn't set", "PostgreSQL URL. Query options such as `sslmode` and `pool_max_conns` are kept."],
                ["`cache.redis_url`", "For a cluster", "Redis URL: one server, Sentinel (`redis+sentinel://`) or Redis Cluster (`redis+cluster://`); `rediss` variants for TLS"],
                ["`storage.backend`", "Yes", "`local`, `s3`, `minio` or `azure`; only that backend's section is read"],
                ["`storage.local.path`", "With `local`", "Directory for artifacts (a shared volume in a cluster)"],
                ["`storage.s3.*`", "With `s3`", "`bucket`, `region`; `access_key` and `secret_key` (or neither, for the IAM role); optional `role_arn`, `external_id`"],
                ["`storage.minio.*`", "With `minio`", "`endpoint`, `bucket`, `use_ssl`, `access_key`, `secret_key`"],
                ["`storage.azure.*`", "With `azure`", "`container`, `account`, `key`"],
                ["`license.file` or `license.data`", "Yes, one of them", "The license JSON: a file (relative to the setup file) or inline"],
                ["`admin.email`, `admin.name`, `admin.password`", "Yes", "The first super admin"],
            ]),
            H("Rules the server enforces"),
            UL([
                "**Private file.** The file must not be readable by group or others (`chmod 600`); otherwise the server stops and prints the `chmod` to run.",
                "**No unknown keys.** A misspelled key is an error, so a typo can't silently drop a setting.",
                "**Secrets from the environment.** Any value may use `${NAME}`; only that form is expanded, so a literal `$` stays as it is. A referenced variable that isn't set stops the server with its name.",
                "**One license source.** `license.file` or `license.data`, not both.",
                "**Fresh installations only.** On an installed server the file is ignored.",
                "**Fails loudly.** If a value doesn't work (database, storage, Redis, license), the server stops with an error that says what to fix; nothing is half set up.",
            ]),
            H("In containers"),
            CODE("""docker run --rm \\
  -e CONFIG_ENCRYPTION_KEY -e DATABASE_URL -e ADMIN_PASSWORD -e S3_ACCESS_KEY -e S3_SECRET_KEY \\
  -e SETUP_CONFIG_FILE=/config/setup.yaml \\
  -v "$PWD/setup:/config:ro" \\
  -v depotex-data:/app/data \\
  -p 8080:8080 \\
  <your-registry>/depotex-backend:<version>"""),
            P("Mount the setup file read-only with mode 0600, owned by the server's user (UID 65532 in the image). The `/app/data` volume keeps the server's bootstrap file, search index and logs: keep it across restarts. With the Helm chart you don't write the file yourself: the chart builds it from its values and the secrets (see [Install with Helm](helm-chart.html#first-boot-setup))."),
            H("After setup, without the UI"),
            UL([
                "Everything in the web app is also an API: `GET /api/openapi.json` describes every route, its permission and its license tier (see [API Tokens → API description](api-tokens.html#api-description)). Sign in once as the administrator to create an [API token](api-tokens.html) for automation, or register an [OAuth application](oauth-applications.html) with a service account for machine access.",
                "Write the configuration you script (spaces, repositories, upstreams, directories, policies) against that API, so a new installation can be rebuilt the same way.",
                "Disaster recovery also works without the UI: `./server --restore-file backup.dxbak` checks a backup with no server running, and `--yes` restores it. See [Backups → Disaster recovery](backups.html#disaster-recovery).",
            ]),
            H("Command-line flags"),
            TABLE(["Flag", "What it does"], [
                ["`--setup-config <file>`", "Set up a fresh installation from this file (overrides `SETUP_CONFIG_FILE`)"],
                ["`--machine-id`", "Print this machine's installation ID, for a license request, and exit"],
                ["`--restore-file <file>`", "Check a backup archive (`.dxbak`) with no server running; with `--yes`, restore it, then exit"],
                ["`--restore-import <name>`", "The same for a file in the backup storage's import folder (`backups/import/`)"],
                ["`--restore-key-file <file>`", "The key of an encrypted backup: an age identity file, or the passphrase"],
                ["`--restore-sha256 <hex>`", "The SHA-256 the backup must have (from its `.sha256` file)"],
                ["`--restore-accept-foreign`", "Restore a backup signed by another installation"],
                ["`--restore-force`", "Restore although other servers of this installation are running"],
                ["`--yes`", "With a restore flag: restore (without it only the checks run)"],
            ]),
        ])),
]
