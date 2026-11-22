"""Settings → AI in Depotex. The platform's AI settings (libs/platform/ai and
libs/platform-ui src/admin/routes/settings/ai in the depotex repo) are
mounted in every product. Depotex registers no AI feature of its own yet, so
this page says what the screen is and that nothing in Depotex uses it. The
Wiki's docs (wiki/_build/content_kee.py) describe the same screens in full,
where they drive Kee."""
from engine import H, P, UL, TABLE, NOTE, SHOT

AI = [
    ("ai-settings", dict(
        label="AI settings", title="AI settings", icon="sliders",
        desc="Settings → AI: the platform's model provider settings, and why Depotex doesn't use them yet",
        keywords=["ai", "artificial intelligence", "llm", "model provider", "anthropic", "openai", "gemini", "bedrock", "settings ai"],
        blocks=[
            P("**Settings → AI** (marked **New**) is where the platform connects an organisation's own model provider account: Anthropic, OpenAI, Google Gemini or Amazon Bedrock. It is shown to people who hold **Manage AI settings** (`ai:manage`) on a **Pro** licence or higher."),
            NOTE("Depotex has no AI features of its own yet. The page says so under **What people get once it is on**, and turning AI on makes nothing appear for anyone. Leave it off: while it is off, no text leaves the server."),
            SHOT("ai-settings-off.png", "Settings → AI while AI is off: Turn on AI, the three set-up steps, and that Depotex has no AI features of its own yet"),
            H("What the page holds"),
            TABLE(["Tab", "What it configures"], [
                ["**Providers and models**", "Provider accounts (keys are encrypted on the server and never shown again), the models people may use, the default and the fallback"],
                ["**Features and access**", "A switch per feature (none in Depotex yet), and a permissions grid: **Use AI**, **See usage** and **Manage AI settings** per role, plus groups"],
                ["**Limits and usage**", "Requests per person per day and per minute, a monthly budget, and a usage report"],
                ["**Data handling**", "What would be sent to the provider, the providers' own terms, how long usage records are kept"],
            ]),
            P("The switch at the top right turns AI on or off for the whole installation. Off, every AI route answers as if it didn't exist and nothing is sent anywhere."),
            H("Events"),
            P("Changes on this page raise `ai.provider.*`, `ai.model.*`, `ai.settings.update` and `ai.permissions.update`, which [policies](policies.html) can refuse and which are in the audit log. See [Events](events.html)."),
        ])),
]
