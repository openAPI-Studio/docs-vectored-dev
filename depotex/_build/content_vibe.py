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
            NOTE("AI coding tools publish and pull projects through the Depotex AI tools (MCP), see [Use vibe projects from AI tools](#use-vibe-projects-from-ai-tools); scripts push with three HTTP requests (see [Push a check-in](#push-a-check-in))."),

            H("Turn vibe artifacts on or off"),
            STEPS([
                "Open the settings|Go to **Settings → Repositories → Vibe artifacts** (super admins, the `repository_settings:manage` permission).",
                "Turn them on|Turn on **Turn on vibe artifacts**. **Vibe** appears in the left menu for everyone signed in, on every server at once.",
                "Turn them off|Clear the switch. The Vibe entry disappears for everyone; what was published is kept and comes back when you turn it on again.",
            ]),
            SHOT("vibe-settings.png", "Settings → Repositories → Vibe artifacts with the switch on, and Vibe in the left menu"),
            P("The page shows when the switch last changed. Each change is recorded in the audit log (`vibe:update_settings`)."),

            H("Find projects in the Vibe browser"),
            P("Open **Vibe** in the left menu. One search box looks through project names, descriptions and tags, milestones, what each check-in changed, and screenshot captions; every word you type must match, and the start of a word is enough (`stre` finds \"Streaks work\")."),
            SHOT("vibe-browser.png", "The Vibe browser: search, filters and the Projects view, newest check-in first"),
            TABLE(["Filter", "What it keeps"], [
                ["**Project**", "One project (the list holds the projects you can see)"],
                ["**Milestone**", "**Milestones only**, or one milestone by name"],
                ["**Pushed**", "Today, the last 7 or 30 days, or dates you pick"],
                ["**With screenshots**", "Only check-ins that have a screenshot"],
            ]),
            P("Three views show what matches:"),
            UL([
                "**Projects**: a card per project with its newest screenshot, description, latest check-in and milestone. Projects with the newest matching check-in come first.",
                "**Timeline**: every matching check-in, grouped by day, milestones marked with a bar.",
                "**Screenshots**: every screenshot, newest first; one opens its check-in at that screenshot. The search looks in each screenshot's own caption.",
            ]),
            SHOT("vibe-browser-timeline.png", "The Timeline view: check-ins grouped by day, milestones marked"),
            SHOT("vibe-browser-screenshots.png", "The Screenshots view: every screenshot with its caption, project and check-in"),
            P("The search and filters are part of the page address, so you can bookmark a search or send it to someone. On a phone the filters fold behind the filter button beside the search box."),
            SHOT("vibe-browser-phone.png", "The Vibe browser on a phone"),

            H("Project and check-in pages"),
            P("A project's page shows its newest screenshot, what the latest check-in changed and **How to run it** (the run and test commands, each with Copy, and whether the tests passed), then the milestones it reached. Below are its **Check-ins**, **About** (the memory file of the latest check-in), **What's unfinished** (its known gaps file), every **Screenshot** and the **Files** of the latest check-in."),
            SHOT("vibe-project.png", "A project's page: the latest check-in, how to run it, milestones and every check-in"),
            P("A check-in's page, which the link from every push opens, shows its screenshots full size with their captions (arrows and the strip below switch between them), what changed, who pushed it and when, the check-in it builds on, and how to run it. Its tabs show its memory file, known gaps and files. The memory file is the first of `AGENTS.md`, `CLAUDE.md` and `README.md` at the top of the project; the known gaps file is `KNOWN_GAPS.md` or `GAPS.md`."),
            SHOT("vibe-checkin.png", "A check-in's page: screenshots, details, how to run it, and the actions to pick it up"),
            UL([
                "**Copy prompt for your agent** copies a short instruction for an AI coding tool: download this check-in, read its memory and known gaps, carry on and push a new check-in to the same project.",
                "**Download archive** downloads every file of the check-in as a zip, with the files' modes.",
                "**Copy link** copies the page's address (the public URL when one is set).",
            ]),
            SHOT("vibe-checkin-gaps.png", "A check-in's What's unfinished tab: its known gaps file"),
            P("What you see follows the space's permissions: a project shows only to people who may browse its repository, and screenshots, files and the archive only to people who may read them. A quarantined check-in is left out of search and its page says it is held; a check-in the [block list](blocklist.html) refuses can't be opened either."),
            P("Vibe repositories don't show in [Browse](browse.html). When you can see a vibe project, Browse shows a line that opens the Vibe browser."),
            SHOT("browse-vibe-notice.png", "Browse with the line that opens the Vibe browser"),

            H("Vibe artifact repositories"),
            P("Projects live in **vibe artifacts** repositories. Add the format to a space (the space's **Formats**), then create a repository with the format **Vibe artifacts** in that space (**New repository** on the space's Repositories tab). They are hosted repositories only: there are no proxy or group vibe repositories, so the form offers **Hosted** only. The format is offered only while vibe artifacts are on: turned off, the format isn't listed anywhere, the repositories answer `404` and keep everything, and turning it back on brings them back as they were."),
            SHOT("vibe-repository-create.png", "A new repository in a space, with the Vibe artifacts format: only Hosted is offered"),
            P("A repository holds projects (a name such as `todo-app`: lower-case letters, digits, dots, dashes and underscores). Each push of a project is a **check-in**, numbered from 1: every file of the project at that moment, a milestone name (\"Login works\"), a line on what changed, how to run and test it with whether the test passed, and up to 10 screenshots. A check-in can't be changed later. Only files the repository doesn't have yet are uploaded, so a push that changes one file uploads one file."),
            P("Space roles decide who does what, by path in the repository as for any format: readers download, developers push, maintainers delete projects. A check-in is a version of its project (`todo-app`, version `3`), so [cleanup policies](spaces.html#cleanup), [quarantine](quarantine.html) and the [block list](blocklist.html) work on check-ins, and [upload rules](spaces.html#upload-rules) judge each added or changed file by its path in the project. Vibe repositories are left out of [Browse](browse.html): they are found in the Vibe browser."),

            H("Push a check-in"),
            P("Pushing is three requests: `curl` calls (or your own script) with an [API token](api-tokens.html). AI coding tools can use the [AI tools](#use-vibe-projects-from-ai-tools) instead, which make the same requests for the person. `checkin.json` describes the whole check-in:"),
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

            H("Use vibe projects from AI tools"),
            P("The Depotex AI tools plugin (`depotex-mcp`, see [MCP servers for AI applications](plugins.html#mcp-servers-for-ai-applications)) gives AI coding tools such as Claude Code, Cursor or VS Code tools to find, pull and publish vibe projects. They act as the person who connected the AI app, with that person's access, and they are listed only while vibe artifacts are on (Enterprise): on other tiers, or with the switch off, the AI app doesn't see them at all."),
            TABLE(["Tool", "What it does"], [
                ["`vibe_search`", "Find projects or check-ins by words, project, milestone, date or screenshots, the same search as the Vibe browser"],
                ["`vibe_versions`", "A project's check-ins, newest first"],
                ["`vibe_pull`", "One check-in (the latest by default): what changed, how to run and test it, the screenshot captions, the memory file and known gaps as text, and a short-lived link to download every file as a zip"],
                ["`vibe_list_files`, `vibe_get_file`", "A check-in's files, and one file's text (files that aren't text, or are over 256 KiB, come as a short-lived download link)"],
                ["`vibe_diff`", "What changed between two check-ins, and for one file a line-by-line diff"],
                ["`vibe_push_begin`, `vibe_push_commit`", "Publish a new check-in: begin lists the files to upload, each with an address; commit saves the check-in and answers with its link in the Vibe browser, which the AI app is told to show you"],
            ]),
            UL([
                "**Permissions:** the AI app needs the plugin's permission **Find and pull the vibe projects you can see** (`mcp:depotex:vibe`) to read, and **Publish vibe projects as new check-ins** (`mcp:depotex:vibe:push`) to publish. The person's space role still decides what each tool may do, as it does for a push over HTTP.",
                "**Publishing is a write tool.** `vibe_push_begin` and `vibe_push_commit` show only when an administrator turns on **Allow write tools for AI agents**, the plugin is **Read-write** and the AI app's access is **Read and change** (see [Write tools](plugins.html#write-tools)).",
                "**Every publish answers with the browser link** (`https://<your Depotex address>/vibe/<space>/<repository>/<project>/<n>`), so you can open the check-in straight away. Set **Settings → General → Public URL** so the link works for others.",
                "**Download links** from `vibe_pull` and `vibe_get_file` work without a token for `VIBE_PULL_LINK_TTL` (15 minutes), for that file or archive only.",
                "Through the AI tools a check-in can list up to about 5,000 files; push bigger projects with the HTTP requests above.",
                "What a project holds (memory files, known gaps, code) was written by someone else, so results carry a notice telling the AI app to treat them as data, not instructions.",
            ]),

            H("Read and download"),
            TABLE(["Request", "Answers"], [
                ["`GET <repository URL>`", "The projects you can see, by name"],
                ["`GET …/todo-app`", "The project: description, tags, latest check-in and its link"],
                ["`GET …/todo-app/checkins`", "Its check-ins, newest first (`?before=` the number to page)"],
                ["`GET …/todo-app/checkins/3` (or `latest`)", "The check-in's manifest: every file with its SHA-256, size and mode, the screenshots and the details"],
                ["`GET …/todo-app/checkins/3/files/src/app.tsx`", "A file at that check-in, as a download"],
                ["`GET …/todo-app/checkins/3/screenshots/1`", "A screenshot (1 is the first); add `/thumbnail` for a small preview"],
                ["`GET …/todo-app/checkins/3/archive`", "Every file of the check-in as a zip, with the files' modes"],
            ]),
            P("Files are always downloads, never shown as web pages, so a pushed HTML file can't run on Depotex's address."),

            H("Delete a project"),
            P("`DELETE <repository URL>/todo-app` (maintainers) deletes the project with every check-in and screenshot. Its name can be used again; the new project starts at check-in 1."),

            H("Limits and server settings"),
            TABLE(["Setting", "Default", "What"], [
                ["`VIBE_UPLOAD_LINK_TTL`", "`1h`", "How long upload addresses work (1m to 48h)"],
                ["`VIBE_PULL_LINK_TTL`", "`15m`", "How long download links from the AI tools work (1m to 24h)"],
                ["`VIBE_MAX_FILES`", "`20000`", "Most files in a check-in"],
                ["`VIBE_MAX_SCREENSHOTS`", "`10`", "Most screenshots in a check-in (0 to 100)"],
                ["`VIBE_MAX_SCREENSHOT_SIZE`", "`10485760`", "Largest screenshot in bytes (64 KiB to 100 MiB); PNG, JPEG or GIF"],
                ["`VIBE_GC_GRACE`", "`24h`", "How long uploads no check-in uses are kept before the `vibe-gc` job removes them (1h to 30d)"],
            ]),
            P("The largest file is the repository's size limit, else the installation's (**Settings → Repositories**). Every server of a cluster must use the same values. The `vibe-gc` job runs daily in [Scheduler](scheduler.html); it removes only uploads no check-in uses."),

            H("Events"),
            P("`vibe.settings.update` is raised when vibe artifacts are turned on or off, before (so a [policy](policies.html) or plugin can refuse it) and after, with `enabled` and `previous_enabled`. Use [automation](automation.html) to tell someone when it changes."),
            P("`vibe.checkin.push` is raised for every push: before, so a policy can refuse it (for example pushes without a milestone, or to a space you name), and after, with the check-in's number, what changed and its link, so [automation](automation.html) can post the link to a chat. `vibe.project.delete` is raised when a project is deleted. Each added or changed file also raises `artifact.upload`. Pushes are recorded in the audit log as `vibe:push`, deletions as `vibe:delete_project`; a push from an AI tool raises the same events and its audit entry names the plugin and AI app (`via: mcp:depotex-mcp/<app>`). Searching and pulling, from the browser or an AI tool, raise no events. See [Events](events.html)."),

            H("API"),
            TABLE(["Route", "Who", "What"], [
                ["`GET /api/vibe/settings`", "Enterprise, `repository_settings:manage`", "Whether vibe artifacts are on (`enabled`) and when that last changed (`updated_at`)"],
                ["`PUT /api/vibe/settings`", "Enterprise, `repository_settings:manage`", "`{\"enabled\": true}` turns them on, `false` off"],
                ["`GET /api/features`", "Anyone signed in", "The optional features this installation has now; `vibe` is listed while vibe artifacts are on"],
                ["`GET /api/vibe/projects`", "Enterprise, signed in", "Projects with a check-in matching the search (`q`, `project`, `milestones`, `milestone`, `from`, `to`, `screenshots`), newest match first, paged with `cursor` and `limit`"],
                ["`GET /api/vibe/checkins`", "Enterprise, signed in", "Matching check-ins, newest first (the Timeline view), same filters"],
                ["`GET /api/vibe/screenshots`", "Enterprise, signed in", "Matching screenshots, newest first (the Screenshots view)"],
                ["`GET /api/vibe/filters`", "Enterprise, signed in", "The projects and milestone names the filters offer"],
                ["`GET /api/vibe/projects/{space}/{repository}/{project}`", "`repo:browse` on the project", "A project's page: latest check-in and milestones"],
                ["`GET …/{project}/checkins`, `…/checkins/{n}`, `…/checkins/{n}/files`", "`repo:browse` (screenshots and files: `repo:read`)", "Its check-ins, one check-in's page, and the check-in's files"],
            ]),
        ],
    )),
]
