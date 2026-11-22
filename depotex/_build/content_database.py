"""Database password page. Keep in step with libs/platform/dbadmin,
libs/platform/kernel/database.go and libs/go-common/db/source.go in the
depotex repo. The same page is in the other product's guide (wiki/_build/content_database.py):
change both."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, CODE, SHOT

DATABASE = [
    ("database-credentials", dict(
        label="Database password", title="Database Password", icon="grid",
        desc="Change or rotate the PostgreSQL password Depotex signs in with, by hand, from a secret manager or on a schedule, without stopping the servers",
        keywords=["database", "postgresql", "password", "rotate", "rotation", "credentials", "DATABASE_URL", "DATABASE_URL_FILE", "DATABASE_URL_STANDBY", "DATABASE_OWNER_ROLE", "secret manager", "vault", "standby login", "bootstrap file"],
        blocks=[
            H("Overview"),
            P("Depotex signs in to PostgreSQL with the URL you give it in `DATABASE_URL`. Each server also keeps the URL, encrypted with `CONFIG_ENCRYPTION_KEY`, in its bootstrap file, so it can start without the environment variable later. This page is about changing that password afterwards. Available on every license tier."),
            TABLE(["You want to", "Do this"], [
                ["Change the password once, by hand", "[Change it in PostgreSQL and in the environment](#change-the-password-by-hand)"],
                ["Let Depotex rotate it, now or on a schedule", "[Settings → Database](#settings-database)"],
                ["Let a secret manager rotate it", "[Give the URL as a file](#secret-managers)"],
                ["Rotate with no refused sign-in at all", "[Use two logins](#two-logins)"],
            ]),
            P("The password is never shown, logged or returned by the API, wherever it is stored."),

            H("Where a server gets its credentials"),
            P("When a server starts it tries, in this order:"),
            OL([
                "`DATABASE_URL` (or the file named by `DATABASE_URL_FILE`), when set;",
                "`DATABASE_URL_STANDBY` (or `DATABASE_URL_STANDBY_FILE`), when set;",
                "the URL saved in its bootstrap file, and the other logins it has used or been given."
            ]),
            P("The first that signs in is used and saved in the bootstrap file, with the others kept as fallbacks. So **the environment wins**: put a new password in `DATABASE_URL`, restart, and the server uses it. A server whose saved password stopped working, and that has nothing newer, starts in [recovery mode](recovery.html), which says the credentials were refused."),
            NOTE("**A URL from the environment must reach the same installation.** The server compares the installation ID in the database with the one it saved. A `DATABASE_URL` that points at another installation's database is refused (shown as **Wrong database**) and the saved one is used. To move an installation to another database on purpose, use [recovery mode](recovery.html) or restore a [backup](backups.html)."),
            P("While a server runs, connections it already has stay open after a password change: PostgreSQL only checks a password when a connection is opened. Before it opens a new one, the server checks the login it uses, and when PostgreSQL refuses it the server moves to the next credential that works, so no request fails."),

            H("Change the password by hand"),
            STEPS([
                "Change it in PostgreSQL|`ALTER ROLE depotex PASSWORD '…';` (use `\\password depotex` in `psql` so the password doesn't reach the server log). Running servers keep working on the connections they have.",
                "Put the new URL where the servers read it|`DATABASE_URL` in each server's environment, the Kubernetes secret, or the file `DATABASE_URL_FILE` names.",
                "Restart the servers, one at a time|Each signs in with the new password and saves it. With `DATABASE_URL_FILE` no restart is needed: a server reads the file again when a sign-in is refused.",
            ]),
            P("Between the first and the last step a server that needs a new connection has only the old password. Do the steps close together, or use [two logins](#two-logins) so there is always one that works."),

            H("Settings → Database"),
            P("Super admins find the logins under **Settings → Database**: the database the servers connect to, the stored logins with their state, the rotation schedule, and what each server signs in with."),
            SHOT("database-settings.png", "Settings → Database: the connection, two stored logins with Rotate now, the rotation schedule and the servers"),
            UL([
                "**Stored logins.** A few seconds after its first start, a server stores the login it uses (and a second one from `DATABASE_URL_STANDBY`) encrypted in the database, where every server reads it. **Add a second login** or **Replace a login** stores a role you created in PostgreSQL; the page tests that it signs in and can act as the owner of the tables before it is saved.",
                "**Test credentials** makes the server you are on sign in with every credential it holds and shows which work.",
                "**Rotate now** makes a new random password for one login.",
                "**Rotation schedule** rotates one password whenever the newest is older than the days you choose (30, 60 or 90, or your own number up to 365). Off by default.",
                "The server address, port and database name are shown but can't be changed here: they come from each server's start configuration.",
            ]),
            H("What a rotation does"),
            SHOT("database-rotate.png", "The Rotate now dialog names the login that gets a new password"),
            STEPS([
                "The new password is handed out|It is stored encrypted and every running server takes it, without using it yet. The page shows how many servers hold it.",
                "The password is changed|When every running server holds it, the login changes its own password in PostgreSQL. This usually takes a few seconds.",
                "Servers move to it|Nobody restarts anything, and each server saves the new password in its bootstrap file.",
            ]),
            P("If a running server doesn't take the new password within 5 minutes, the rotation is given up: nothing was changed, the page says why, and super admins get an alert."),
            TABLE(["Situation", "What happens"], [
                ["Two logins are stored", "The login the servers aren't using is changed, then becomes the preferred one. No sign-in is refused."],
                ["One login is stored", "The login in use is changed. A server opening a new connection in the instant before it takes the change can meet one refused sign-in, and retries. The page says so before you confirm."],
                ["A server is off (one login)", "Refused: a server that is off can't learn the new password. Start it, remove it under **Settings → Clustering**, or add a second login. An administrator can rotate anyway; that server then needs the new password from its environment or recovery mode before it starts."],
                ["A server is off (two logins)", "Allowed once: the server still starts on the login that didn't change. A second rotation is refused until it has been started or removed."],
                ["Something else signs in as the same role", "A backup tool or dashboard using that login stops working: the new password is never shown. Give such tools their own role."],
            ]),
            WARN("**When your environment or secret also holds the password.** After a rotation from this page, the copy in `DATABASE_URL` or your secret is out of date. Running servers are fine (they hold the stored logins) and the [system check](system-check.html) warns. A **new** server that has only that secret can't start until you update it. If a secret manager owns the password, leave rotation here off and let it rotate; see below."),

            H("Two logins"),
            P("With two logins that act as one owner role, one password can change while the servers run on the other. Create them once:"),
            CODE("""CREATE ROLE depotex NOLOGIN CREATEROLE;              -- owns the database and its tables
CREATE ROLE depotex_a LOGIN NOINHERIT PASSWORD '…';
CREATE ROLE depotex_b LOGIN NOINHERIT PASSWORD '…';
GRANT depotex TO depotex_a, depotex_b;
GRANT CONNECT ON DATABASE depotex TO depotex_a, depotex_b;"""),
            CODE("""DATABASE_URL=postgres://depotex_a:…@db.internal:5432/depotex?sslmode=verify-full
DATABASE_URL_STANDBY=postgres://depotex_b:…@db.internal:5432/depotex?sslmode=verify-full
DATABASE_OWNER_ROLE=depotex"""),
            UL([
                "`DATABASE_OWNER_ROLE` makes every connection act as that role, so tables have one owner whichever login is used. Set it from the first start, on every server.",
                "The names are yours to choose. `CREATEROLE` is needed only for [plugins](plugins.html) that keep their own tables.",
                "An installation that started with one login that owns its tables can stay that way: rotation works with one login, with the brief refused sign-in described above.",
            ]),
            H("Kubernetes and the Helm chart"),
            P("The [Helm chart](helm-chart.html)'s built-in PostgreSQL is set up with two logins from the start: `prime-secrets.sh init` puts both URLs in the app secret, and the chart sets the owner role."),
            CODE("""deploy/helm/prime-secrets.sh rotate-db -n depotex -r depotex"""),
            UL([
                "`rotate-db` gives the login the servers aren't using a new password and makes it the preferred one in the secret. Run it twice to change both.",
                "With `backend.database.secretAsFile: true` the pods read the secret as files and pick the change up themselves. Without it, restart the server pods when convenient (`kubectl rollout restart statefulset`): until then they keep running on the other login.",
                "For an external database, pass `--database-url` and, for a second login, `--database-url-standby` to `init`, and set `backend.database.ownerRole` when the logins act as another role. `rotate-db` works with the built-in database only; rotate an external one from **Settings → Database** or your secret manager.",
            ]),
            H("Secret managers"),
            P("When Vault, AWS Secrets Manager, an external secrets operator or a similar tool owns the password, let the servers read it from a file the tool keeps current:"),
            CODE("""DATABASE_URL_FILE=/run/secrets/database-url
DATABASE_URL_STANDBY_FILE=/run/secrets/database-url-standby   # optional"""),
            UL([
                "Each file holds one URL. A server reads it again when PostgreSQL refuses a sign-in (at most every 5 seconds), so a rotated password needs no restart.",
                "A tool that rotates by switching between two users (AWS's alternating-users rotation, for example) fits the two logins above: give both URLs.",
                "A tool that changes the one password in place leaves a short gap between the change in PostgreSQL and the new file. Servers keep their open connections during it; a second login closes the gap.",
                "Leave the rotation schedule in **Settings → Database** off, so only one side changes passwords. The page reminds you when a server signs in with a credential from its environment.",
            ]),

            H("Environment variables"),
            TABLE(["Variable", "Meaning"], [
                ["`DATABASE_URL`", "The preferred login. Wins over the saved one at every start when it reaches the same installation"],
                ["`DATABASE_URL_FILE`", "A file holding that URL, read again while the server runs. A path that doesn't exist counts as not set"],
                ["`DATABASE_URL_STANDBY`, `DATABASE_URL_STANDBY_FILE`", "A second login for the same database, used when the first is refused"],
                ["`DATABASE_OWNER_ROLE`", "The role connections act as. Needed when the logins don't own the tables themselves"],
            ]),
            P("All of them are listed with the others under [Environment variables](environment-variables.html)."),

            H("System check, alerts and events"),
            UL([
                "The [system check](system-check.html) has **Database credentials** (each server: a credential it holds is refused or points at another installation, or its environment holds an out-of-date password) and **Database password rotation** (the last change was given up, or the schedule is overdue).",
                "A rotation that is given up, or a scheduled one that can't run, alerts super admins with a link to the page.",
                "[Events](events.html): `database.credential.rotate` and `database.credential.update` (before and after, blocking) and `database.credential.rotation_failed` (after). They carry the login name and the reason, never a password.",
            ]),

            H("Permissions"),
            TABLE(["Permission", "Who", "Allows"], [
                ["`database:admin`", "Super admins only", "Viewing the page, testing, storing and removing logins, rotating, and the schedule"],
            ]),
            NOTE("Every rotation, stored or removed login and schedule change is recorded in the audit log, without the password."),
        ],
    )),
]
