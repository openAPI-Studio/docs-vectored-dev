"""Vibe artifacts page. Keep in step with
apps/depotex/backend/internal/vibe in the depotex repo."""
from engine import H, P, UL, TABLE, NOTE, STEPS, SHOT, CODE

VIBE = [
    ("vibe-artifacts", dict(
        label="Vibe artifacts", title="Vibe artifacts", icon="bolt",
        desc="Projects AI coding tools publish (code, memory, known gaps, screenshots) and the Vibe browser to find them; Enterprise, turned on in Settings",
        keywords=["vibe", "vibe coding", "vibe artifacts", "ai coding", "ai agent", "project", "milestone", "screenshots", "memory", "known gaps", "enterprise", "check-in", "push", "repository"],
        blocks=[
            H("Overview"),
            P("Vibe artifacts are projects that AI coding tools publish to Depotex: the code with its memory file, known gaps and screenshots. The **Vibe** browser, beside [Browse](browse.html) in the left menu, is a simple place to find them by project, milestone, date or screenshot. Browse keeps working as before for every other repository type."),
            NOTE("Vibe artifacts need an **Enterprise** license, and an administrator turns them on for the whole installation. On Standard and Pro nothing about them shows: no menu entry, no settings page, and their API answers `402` with the reason `vibe_requires_enterprise`."),
            NOTE("This release adds the switch, the Vibe page and vibe artifact repositories you push to over HTTP. Searching projects in the browser, project pages and publishing straight from AI coding tools come in the next releases; until then the Vibe page says so, and a check-in's link opens it."),

            H("Turn vibe artifacts on or off"),
            STEPS([
                "Open the settings|Go to **Settings → Repositories → Vibe artifacts** (super admins, the `repository_settings:manage` permission).",
                "Turn them on|Turn on **Turn on vibe artifacts**. **Vibe** appears in the left menu for everyone signed in, on every server at once.",
                "Turn them off|Clear the switch. The Vibe entry disappears for everyone; what was published is kept and comes back when you turn it on again.",
            ]),
            SHOT("vibe-settings.png", "Settings → Repositories → Vibe artifacts with the switch on, and Vibe in the left menu"),
            SHOT("vibe-browser.png", "The Vibe page, which a check-in's link opens until project pages arrive"),
            P("The page shows when the switch last changed. Each change is recorded in the audit log (`vibe:update_settings`)."),

            H("Vibe artifact repositories"),
            P("Projects live in **vibe artifacts** repositories. Add the format to a space (the space's **Formats**), then create a repository with the format **Vibe artifacts** in that space (**New repository** on the space's Repositories tab). They are hosted repositories only: there are no proxy or group vibe repositories, so the form offers **Hosted** only. The format is offered only while vibe artifacts are on: turned off, the format isn't listed anywhere, the repositories answer `404` and keep everything, and turning it back on brings them back as they were."),
            SHOT("vibe-repository-create.png", "A new repository in a space, with the Vibe artifacts format: only Hosted is offered"),
            P("A repository holds projects (a name such as `todo-app`: lower-case letters, digits, dots, dashes and underscores). Each push of a project is a **check-in**, numbered from 1: every file of the project at that moment, a milestone name (\"Login works\"), a line on what changed, how to run and test it with whether the test passed, and up to 10 screenshots. A check-in can't be changed later. Only files the repository doesn't have yet are uploaded, so a push that changes one file uploads one file."),
            P("Space roles decide who does what, by path in the repository as for any format: readers download, developers push, maintainers delete projects. A check-in is a version of its project (`todo-app`, version `3`), so [cleanup policies](spaces.html#cleanup), [quarantine](quarantine.html) and the [block list](blocklist.html) work on check-ins, and [upload rules](spaces.html#upload-rules) judge each added or changed file by its path in the project. Vibe repositories are left out of [Browse](browse.html): they are found in the Vibe browser."),

            H("Push a check-in"),
            P("Pushing is three requests. For now they are `curl` calls (or your own script) with an [API token](api-tokens.html); a later release lets AI coding tools send them for you. `checkin.json` describes the whole check-in:"),
            CODE("""{
  "milestone": "Login works",
  "summary": "Adds the sign-in page",
  "run": "npm run dev",
  "test": "npm test",
  "test_passed": true,
  "files": [
    {"path": "package.json", "sha256": "<sha-256 of the file>", "size": 512},
    {"path": "src/app.tsx", "sha256": "<sha-256 of the file>", "size": 2048}
  ],
  "screenshots": [
    {"sha256": "<sha-256 of the image>", "size": 81234, "caption": "Sign-in page"}
  ]
}"""),
            STEPS([
                "Start the check-in|`POST <repository URL>/todo-app/push/begin` with `checkin.json`. The answer lists the files and screenshots the repository doesn't have yet, each with an upload address.",
                "Upload what it asks for|`PUT` each file to its address (`curl --upload-file src/app.tsx \"<address>\"`). The address works without a token for an hour, for that file only; the file must match its SHA-256.",
                "Commit|`POST <repository URL>/todo-app/push/commit` with the same `checkin.json`. The answer has the check-in's number (`checkin`) and its `link`: the check-in in the Vibe browser. Show the link to whoever asked for the push.",
            ]),
            P("The first push creates the project; `description` and `tags` in `checkin.json` set the project's description and tags, and later pushes change them when they include them. A check-in builds on the latest one unless `parent` names another. The repository page's **Use this repository** box shows these commands for your repository."),
            SHOT("vibe-repository-usage.png", "A vibe artifacts repository's page: Use this repository → Publish lists the three push requests"),
            CODE("""R=https://depotex.example.com/repository/apps/projects
curl -f -H "Authorization: Bearer $DEPOTEX_TOKEN" -H "Content-Type: application/json" -d @checkin.json $R/todo-app/push/begin
curl -f --upload-file src/app.tsx "<address from the answer>"
curl -f -H "Authorization: Bearer $DEPOTEX_TOKEN" -H "Content-Type: application/json" -d @checkin.json $R/todo-app/push/commit"""),
            NOTE("The link uses the address in **Settings → General → Public URL** when one is set, so it works for the people you send it to."),

            H("Read and download"),
            TABLE(["Request", "Answers"], [
                ["`GET <repository URL>`", "The projects you can see, by name"],
                ["`GET …/todo-app`", "The project: description, tags, latest check-in and its link"],
                ["`GET …/todo-app/checkins`", "Its check-ins, newest first (`?before=` the number to page)"],
                ["`GET …/todo-app/checkins/3` (or `latest`)", "The check-in's manifest: every file with its SHA-256, size and mode, the screenshots and the details"],
                ["`GET …/todo-app/checkins/3/files/src/app.tsx`", "A file at that check-in, as a download"],
                ["`GET …/todo-app/checkins/3/screenshots/1`", "A screenshot (1 is the first); add `/thumbnail` for a small preview"],
            ]),
            P("Files are always downloads, never shown as web pages, so a pushed HTML file can't run on Depotex's address."),

            H("Delete a project"),
            P("`DELETE <repository URL>/todo-app` (maintainers) deletes the project with every check-in and screenshot. Its name can be used again; the new project starts at check-in 1."),

            H("Limits and server settings"),
            TABLE(["Setting", "Default", "What"], [
                ["`VIBE_UPLOAD_LINK_TTL`", "`1h`", "How long upload addresses work (1m to 48h)"],
                ["`VIBE_MAX_FILES`", "`20000`", "Most files in a check-in"],
                ["`VIBE_MAX_SCREENSHOTS`", "`10`", "Most screenshots in a check-in (0 to 100)"],
                ["`VIBE_MAX_SCREENSHOT_SIZE`", "`10485760`", "Largest screenshot in bytes (64 KiB to 100 MiB); PNG, JPEG or GIF"],
                ["`VIBE_GC_GRACE`", "`24h`", "How long uploads no check-in uses are kept before the `vibe-gc` job removes them (1h to 30d)"],
            ]),
            P("The largest file is the repository's size limit, else the installation's (**Settings → Repositories**). Every server of a cluster must use the same values. The `vibe-gc` job runs daily in [Scheduler](scheduler.html); it removes only uploads no check-in uses."),

            H("Events"),
            P("`vibe.settings.update` is raised when vibe artifacts are turned on or off, before (so a [policy](policies.html) or plugin can refuse it) and after, with `enabled` and `previous_enabled`. Use [automation](automation.html) to tell someone when it changes."),
            P("`vibe.checkin.push` is raised for every push: before, so a policy can refuse it (for example pushes without a milestone, or to a space you name), and after, with the check-in's number, what changed and its link, so [automation](automation.html) can post the link to a chat. `vibe.project.delete` is raised when a project is deleted. Each added or changed file also raises `artifact.upload`. Pushes are recorded in the audit log as `vibe:push`, deletions as `vibe:delete_project`. See [Events](events.html)."),

            H("API"),
            TABLE(["Route", "Who", "What"], [
                ["`GET /api/vibe/settings`", "Enterprise, `repository_settings:manage`", "Whether vibe artifacts are on (`enabled`) and when that last changed (`updated_at`)"],
                ["`PUT /api/vibe/settings`", "Enterprise, `repository_settings:manage`", "`{\"enabled\": true}` turns them on, `false` off"],
                ["`GET /api/features`", "Anyone signed in", "The optional features this installation has now; `vibe` is listed while vibe artifacts are on"],
            ]),
        ],
    )),
]
