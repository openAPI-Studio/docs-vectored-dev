"""Vibe artifacts page. Keep in step with
apps/depotex/backend/internal/vibe in the depotex repo."""
from engine import H, P, UL, TABLE, NOTE, STEPS, SHOT

VIBE = [
    ("vibe-artifacts", dict(
        label="Vibe artifacts", title="Vibe artifacts", icon="bolt",
        desc="Projects AI coding tools publish (code, memory, known gaps, screenshots) and the Vibe browser to find them; Enterprise, turned on in Settings",
        keywords=["vibe", "vibe coding", "vibe artifacts", "ai coding", "ai agent", "project", "milestone", "screenshots", "memory", "known gaps", "enterprise"],
        blocks=[
            H("Overview"),
            P("Vibe artifacts are projects that AI coding tools publish to Depotex: the code with its memory file, known gaps and screenshots. The **Vibe** browser, beside [Browse](browse.html) in the left menu, is a simple place to find them by project, milestone, date or screenshot. Browse keeps working as before for every other repository type."),
            NOTE("Vibe artifacts need an **Enterprise** license, and an administrator turns them on for the whole installation. On Standard and Pro nothing about them shows: no menu entry, no settings page, and their API answers `402` with the reason `vibe_requires_enterprise`."),
            NOTE("This first release adds the switch and the Vibe page. Publishing from AI coding tools, and searching projects in the browser, come in the next releases; until then the Vibe page says there are no projects yet."),

            H("Turn vibe artifacts on or off"),
            STEPS([
                "Open the settings|Go to **Settings → Repositories → Vibe artifacts** (super admins, the `repository_settings:manage` permission).",
                "Turn them on|Turn on **Turn on vibe artifacts**. **Vibe** appears in the left menu for everyone signed in, on every server at once.",
                "Turn them off|Clear the switch. The Vibe entry disappears for everyone; what was published is kept and comes back when you turn it on again.",
            ]),
            SHOT("vibe-settings.png", "Settings → Repositories → Vibe artifacts with the switch on, and Vibe in the left menu"),
            SHOT("vibe-browser.png", "The Vibe browser, before any project is published"),
            P("The page shows when the switch last changed. Each change is recorded in the audit log (`vibe:update_settings`)."),

            H("Events"),
            P("`vibe.settings.update` is raised when vibe artifacts are turned on or off, before (so a [policy](policies.html) or plugin can refuse it) and after, with `enabled` and `previous_enabled`. Use [automation](automation.html) to tell someone when it changes. See [Events](events.html)."),

            H("API"),
            TABLE(["Route", "Who", "What"], [
                ["`GET /api/vibe/settings`", "Enterprise, `repository_settings:manage`", "Whether vibe artifacts are on (`enabled`) and when that last changed (`updated_at`)"],
                ["`PUT /api/vibe/settings`", "Enterprise, `repository_settings:manage`", "`{\"enabled\": true}` turns them on, `false` off"],
                ["`GET /api/features`", "Anyone signed in", "The optional features this installation has now; `vibe` is listed while vibe artifacts are on"],
            ]),
        ],
    )),
]
