"""Wiki doc pages for Kee release 2: Kee studio (agents and sharing), Connect
AI apps (a person's own outside AI apps), the administrators' Outside AI apps
tab, and scheduled help (stale page finder, suggestions for new questions,
findings). Facts come from the depotex repo: apps/wiki/backend/internal/agents,
internal/outsideapps, internal/kee (help, changes), their screens in
apps/wiki/frontend/src/components (studio, outside-apps, kee/help) and the
developer guides (wiki-agents, wiki-outside-apps, wiki-tools). Only what is
built is described."""
from engine import H, P, UL, TABLE, NOTE, WARN, STEPS, SHOT

KEE_R2_USER = [
    # ------------------------------------------------------------- kee-studio
    ("kee-studio", dict(
        label="Kee studio: agents", title="Kee studio: agents", icon="zap",
        desc="Build an agent (Kee with instructions, knowledge and allowed actions), try it, publish it, share it, and use it in Ask Kee and the editor",
        keywords=["kee", "ai", "studio", "kee studio", "agent", "agents", "assistant", "instructions", "knowledge", "starters", "try it", "publish", "version history", "restore", "share", "sharing", "pause", "duplicate", "export", "import", "no owner", "take over"],
        blocks=[
            P("An **agent** is Kee with a job: instructions it always follows, the spaces and pages it reads first, what it may do, and buttons to start with. It is saved settings, not code. You build one in **Kee studio**, try it, publish it and share it; people then pick it in Ask Kee or in the editor's writing dialogs."),
            NOTE("An agent always runs as the person using it, with that person's access. Its instructions and knowledge can't give anyone access to a page they can't read, and sharing an agent never shares your access."),
            H("Who can build agents"),
            UL([
                "**Kee studio** is in the left navigation (marked **New**) for people who may make agents: the **Make agents** permission in the Kee permissions grid. Organization admins hold it by default; an administrator can give it to members or groups (see [Features and permissions](kee-access.html)).",
                "The **Kee studio** feature must be on (it is, once Kee is on).",
                "Everyone with **Use Kee** can use an agent that was shared with them, without the studio permission.",
            ]),
            SHOT("kee-studio-list.png", "Kee studio: your agents as cards, a draft and a published one, with New agent and the search box"),
            H("Make an agent"),
            STEPS([
                "Open **Kee studio** in the left navigation.",
                ("Select **New agent**.", "studio.new"),
                "Give it a **Name**, say **What it is for**, and pick an icon.",
                "Write its **Instructions**: what this agent should always do, such as the headings every runbook has.",
                "Under **Knowledge**, find the spaces and pages it reads first. Under **What it may do**, tick its actions. Add **Starters** if you like.",
                "Ask it something under **Try it** on the right, and change the settings until the answers are right.",
                "Select **Save draft** to keep it to yourself, or **Publish** to make version 1 that you can share.",
            ], howto="make-a-kee-agent", task="Make, try and publish an agent in Kee studio"),
            SHOT("kee-studio-builder.png", "The builder: icon, name, what it is for, instructions, model, knowledge and what it may do on the left, and a test conversation under Try it on the right"),
            TABLE(["Field", "What it does", "Limit"], [
                ["**Icon**, **Name**, **What it is for**", "How people find the agent in the pickers and the studio", ""],
                ["**Instructions**", "What the agent should always do: tone, structure, what to answer from. They guide the agent; they can't give it access to anything", "8,000 characters"],
                ["**Model**", "**Default model** or one of the models your administrator offers. **People may switch model when using it** shows the model picker to people using the agent; off, the agent always runs on its own model", ""],
                ["**Knowledge**", "Spaces and pages the agent reads first. Always limited to what the person using it can read: anything they can't read is skipped without its title", "20 spaces or pages"],
                ["**What it may do**", "The actions it may take, in two groups: **Find and read** (search, read pages, comments, labels, versions, templates, the page tree) and **Change the wiki** (create page drafts, change pages, comment, add and remove labels). Every action runs as the person using the agent. Changes are never written at once: they are **proposed**, and the person applies them (see [Proposed changes](ask-kee.html#proposed-changes))", "25 actions"],
                ["**Starters**", "Buttons people see when they pick the agent, such as \"Write a runbook for…\"", "6"],
            ]),
            P("Each person may have up to 200 agents."),
            H("Try it"),
            UL([
                "**Try it** runs the agent with the settings in the form, saved or not. Give it a name first.",
                "The test conversation is **not saved**, and each question counts towards your [daily limit](kee.html#your-daily-limit).",
                "Kee never proposes changes in **Try it**, even when the agent has change actions: nothing of a test is stored to apply.",
                "**Start over** clears the conversation. Saving a new agent for the first time also starts it over.",
                "On a phone or a narrow window, **Show** switches between the settings and the test conversation.",
            ]),
            H("Draft, published and versions"),
            UL([
                "A new agent is a **Draft**: only you see it and it can't be shared. **Publish** makes version 1.",
                "On a published agent, **Publish changes** makes a new version. The header says **Published · version N**, or **Unsaved changes**.",
                "**Version history** lists every version with what changed and who changed it. **Restore** publishes an old version's settings again as a new version; nothing is rewritten. The last 100 versions are kept.",
            ]),
            SHOT("kee-studio-versions.png", "Version history of an agent: version 3 restored from version 1, version 2 with changed instructions, version 1 first published, each with Restore"),
            H("Share an agent"),
            P("Share a published agent from **Share** in its builder (the owner, or someone who may manage everyone's agents):"),
            STEPS([
                "Open the agent in Kee studio and select **Share**.",
                "Under **Add people, groups or a space**, find who should have it.",
                "For a person or a group, choose **Can use** or **Can edit**. A space is always **Can use**: everyone who can read that space gets the agent, and loses it when they lose the space.",
                "Tick **Everyone in the wiki** to offer it to anyone who may use Kee. This needs the **Share agents with everyone** permission.",
                "Select **Done**. The list is saved as a whole; **Cancel** leaves it as it was.",
            ], howto="share-a-kee-agent", task="Share an agent with people, groups, a space or everyone"),
            SHOT("kee-studio-share.png", "Share an agent: a space found by its name, the owner, a person who can use it, Everyone in the wiki, and the note that sharing gives the agent, not your access"),
            TABLE(["Level", "May"], [
                ["**Can use**", "Pick the agent in Ask Kee and the editor, and see its name, description and starters. Not how it is built: the builder says **This agent was shared with you for use**"],
                ["**Can edit**", "Also change and publish it, restore versions, pause and resume it, copy it, export it, and see its usage and who has it"],
                ["**Owner**", "Also share it and delete it. People with **Manage everyone's agents** may do the same, see every agent on the **Everyone's** tab, and take one over"],
            ]),
            UL([
                "Removing someone from the list stops the agent for them at their next request, on every server.",
                "A space you can't see in someone else's agent shows as **A space you can't see** and stays on the list.",
                "Up to 100 people, groups and spaces per agent.",
            ]),
            H("The studio list"),
            UL([
                "Tabs: **All I can use**, **Made by me**, **Shared with me**, and **Everyone's** for people who manage everyone's agents. **Search agents** finds by name.",
                "**Use** opens Ask Kee with the agent picked.",
                "The **More** menu of a card, for people who may edit the agent: **Duplicate**, **Export as a file**, **Pause** or **Resume**, **Take over** (for an agent with no owner) and **Delete**, as far as their level allows. Someone who may only use an agent has no menu.",
                "**Import** (at the top) makes a new private draft from an agent file.",
                "Editors see how often the agent was used in the last 30 days, and by how many people. The numbers never say who asked what.",
            ]),
            H("Use an agent"),
            UL([
                "**In Ask Kee**: the agent picker under the question box lists **Recently used** agents and **Agents you can use**, with a search. **Kee** (no agent) is the assistant as it is. A picked agent shows its starters under **Ways to start**, and its name on every answer. See [Ask Kee](ask-kee.html#ask-with-an-agent).",
                "**In the editor**: **Write the page with Kee** and **Write a section below…** have the same picker. There the agent's instructions and model are used; its knowledge and actions are not. Rewrites of a section or a selection don't use agents. See [Writing with Kee](kee-editor.html#write-with-an-agent).",
                "An agent that doesn't let people switch models hides the model picker and always runs on its own model.",
                "Paused agents and drafts are not in the pickers.",
            ]),
            SHOT("kee-studio-picker.png", "The agent picker in Ask Kee: Kee with no agent, and an agent you can use, picked"),
            H("Agents over time"),
            TABLE(["Situation", "What happens"], [
                ["**Pause**", "Nobody can use the agent until it is resumed. It is hidden from the pickers; the studio still lists it, marked **Paused**. A question to a paused agent says **This agent is paused**"],
                ["**Its model is switched off or removed**", "The agent runs on the default model, with the usual notice, until someone picks another. The builder says so"],
                ["**The owner leaves**", "When the owner's personal data is erased, their agents nobody else uses are deleted. A shared agent keeps working for the people it is shared with and is marked **No owner**. Someone with **Manage everyone's agents** chooses **Take over** to make it theirs. A new owner must be allowed to make agents"],
                ["**Duplicate**", "Makes a private draft of your own, shared with nobody. Needs edit. Knowledge you can't read, actions that can't run here and a model that isn't available are left out, with a notice that counts them"],
                ["**Export as a file**", "Downloads the agent's settings: name, description, icon, instructions, the model's name, actions, knowledge by name (space keys and page numbers, never page text) and starters. No people, shares or usage"],
                ["**Import**", "Makes a private draft from such a file (at most 256 KB). Actions, knowledge or a model this Wiki doesn't have are left out, with a notice each"],
                ["**Delete**", "The agent and its version history are deleted for good. Pages it helped write stay as they are; usage numbers stay in the reports"],
            ]),
            WARN("Instructions reach the model on every run. Don't put anything secret in them."),
            H("For administrators"),
            P("The **Kee studio** feature and the three agent permissions are on **Settings → Kee → Features and access**: see [Features and permissions](kee-access.html). Agent events and audit entries are listed in [Events](events.html#agents-and-outside-ai-apps)."),
        ])),

    # ------------------------------------------------------- connect-ai-apps
    ("connect-ai-apps", dict(
        label="Connect AI apps", title="Connect AI apps", icon="link",
        desc="Connect your own AI app, such as Claude, Cursor or VS Code, to the Wiki: the address, signing in, toolsets, keys, and ending a connection",
        keywords=["connect ai apps", "outside ai apps", "ai app", "mcp", "mcp server", "model context protocol", "claude", "cursor", "vs code", "custom connector", "client id", "toolsets", "tools", "key", "bearer token", "disconnect", "read and change"],
        blocks=[
            P("The Wiki has a built-in server that AI apps outside the Wiki can connect to, such as Claude, Cursor or VS Code. Your app signs in **as you**: it reads only what you can read, and changes something only when you allowed it and an administrator allowed changes. It uses the same tools as [Ask Kee](kee-tools.html)."),
            H("What you need"),
            UL([
                "An administrator turned on **Let outside AI apps connect** and registered the AI app you use (see [Outside AI apps](kee-outside-apps.html)). This works whether or not Kee itself is on.",
                "You hold the **Connect AI apps** permission (organization admins by default).",
                "An AI app that supports remote **MCP** servers (Model Context Protocol, over streamable HTTP) with sign-in. Some apps call it a custom connector.",
            ]),
            P("While all of this is true, your profile settings have **Connect AI apps** under **Access**."),
            H("Connect an app"),
            STEPS([
                "Open your profile settings and select **Connect AI apps** under **Access**.",
                "Copy the **Server address**. It is your Wiki's address followed by `/mcp/wiki`.",
                "Under **How to connect**, pick your app (**Claude**, **Cursor**, **VS Code** or **Other apps**) and follow its steps: add the address as a remote server and, when the app asks, enter the client ID shown for it.",
                "When the app opens the Wiki in your browser, sign in and read what it asks for. Allow it.",
                "The app is listed under **Your connections**, marked **Read only** or **Read and change**.",
            ], howto="connect-an-ai-app", task="Connect an outside AI app such as Claude, Cursor or VS Code to the Wiki"),
            SHOT("connect-ai-apps.png", "Connect AI apps in the profile settings: the server address, how to connect each app, the registered apps with their client IDs, and your connections"),
            P("If the page says the public address isn't set, or that no AI app is registered, ask an administrator."),
            H("What an app can do"),
            UL([
                "**Read**: everything [Ask Kee can read](kee-tools.html), with your access: pages, the page tree, spaces, comments, labels, versions, templates, attached files' text, and the Wiki's product docs. Never a page you can't open, a page under a lock you are not on, or anything of a space that turned Kee off.",
                "**Change**: create page drafts, change pages (the whole page or one section, a new title, and publish only when asked), comment and reply, add and remove labels. Only when all three allow it: the app was registered for reading and changing, you agreed to that when signing in (it is listed apart, under a warning), and an administrator set that group of tools to **Read and change**.",
                "A change is written at once, as you, with your permissions, page locks and limits, like a change you make yourself. It is in the audit log with you, the app and the page, and the next version of a page an app wrote into is marked **With an AI app** in the page history.",
                "An app never manages settings, permissions, people, keys or sign-in, and never deletes anything.",
            ]),
            WARN("An app that may change the Wiki acts with your name. Give it only to apps you trust, and only the access it needs."),
            H("Choose the tools a connection is shown"),
            P("AI apps choose less well from a long list of tools. Every connection gets the core tools (search, pages and their tree, spaces, comments, labels, plus the change tools when it may change), tool search and the product docs. Under each connection, **Tools this connection is shown** adds more groups:"),
            TABLE(["Group", "Adds"], [
                ["**Versions**", "A page's version history and earlier versions"],
                ["**Templates**", "Page templates of a space and the library"],
                ["**Attachments**", "Files attached to pages: list them and read their text"],
            ]),
            UL([
                "The line under the list says how many tools the connection will see with your choice. More than 40 shows advice; it is never blocked.",
                "Tools you leave out stay reachable through tool search, with the same checks.",
                "A group an administrator switched off can't be chosen.",
                "**Save**: the app sees the new list the next time it asks for it.",
            ]),
            SHOT("connect-ai-apps-toolsets.png", "A connection marked Read and change, with the groups of tools it is shown and how many tools that makes"),
            H("Keys"),
            P("For an app that can't open a browser to sign in, make a key under **Your keys**. The app sends the server address and the key as a bearer token. A key acts as you."),
            STEPS([
                "Under **Your keys**, give the key a **Name**: where you will use it.",
                "Choose how long it **Works for**, up to the longest your administrator allows (90 days by default).",
                "Choose what it **May** do: **Read only**, or **Read and change** (tick that you understand anything holding the key can change pages, comments and labels as you).",
                "Select **Make key**, copy the key and select **I copied it**. It is never shown again.",
            ], howto="make-a-key-for-an-ai-app", task="Make a key for an AI app that can't sign in with a browser"),
            SHOT("connect-ai-apps-keys.png", "A new key, shown once and masked here, with I copied it"),
            UL([
                "Afterwards only the start of the key is shown, with its end date and when it was last used. Only a fingerprint is stored: if you lose it, remove it and make a new one.",
                "**Remove** stops a key at once, everywhere it is used.",
                "If the section says new keys can't be made, keys are switched off for the installation or you may not make them.",
            ]),
            H("End a connection"),
            UL([
                "**Disconnect** stops the app using the Wiki as you until you sign in to it again.",
                "When an administrator ends a connection, it says **An administrator ended this connection**. Its calls are refused. To use the app again, remove the connection and connect again.",
            ]),
            H("Limits"),
            UL([
                "All your connections together make up to 60 calls a minute by default (an administrator can change it); a change counts as two. Over it, the app is told how long to wait.",
                "Changes also take from your usual budgets for publishing, comments and labels.",
                "Calls through an app don't count against your Kee daily limit: your app uses its own model.",
            ]),
        ])),
]

KEE_R2_ADMIN = [
    # ------------------------------------------------------ kee-outside-apps
    ("kee-outside-apps", dict(
        label="Outside AI apps", title="Outside AI apps", icon="link",
        desc="Let people connect their own AI apps to the Wiki's built-in server: the switch, what apps may do per group of tools, who may connect, keys, the call limit, registered apps, usage and connections",
        keywords=["outside ai apps", "ai apps", "mcp", "mcp server", "model context protocol", "let outside ai apps connect", "toolsets", "read and change", "call limit", "keys", "end connection", "registered apps", "client id", "claude", "cursor", "audit"],
        blocks=[
            P("People can connect their own AI apps (Claude, Cursor, VS Code and others) to a server built into the Wiki. An app signs in as the person: it reads only what that person can read, and changes only what they may change, where you allow changes. It uses the same tool list as [Ask Kee](kee-tools.html). For what people see, see [Connect AI apps](connect-ai-apps.html)."),
            H("What it needs"),
            TABLE(["What", "Details"], [
                ["Licence", "**Pro** or higher"],
                ["Its own switch", "**Let outside AI apps connect**, off by default. It is separate from Kee: it needs no model provider and works while Kee is off"],
                ["The public address", "Set under **Settings → General**. The server's address is that address followed by `/mcp/wiki`"],
                ["A registered AI app", "Each AI app people use is registered under **Settings → Access management → Applications**; there is no self-registration"],
                ["The permission", "**Connect AI apps**, a row of the Kee permissions grid. Organization admins by default"],
            ]),
            H("Where it is"),
            P("**Settings → Kee → Outside AI apps** (`ai:manage`). While Kee is off, the same settings show as a card under the Kee page."),
            SHOT("kee-outside-apps-tab.png", "Settings → Kee → Outside AI apps: the switch, and for each group of tools what apps may do"),
            STEPS([
                "Open **Settings → Kee** and the **Outside AI apps** tab (with Kee off: the card under the page).",
                "Turn on **Let outside AI apps connect**.",
                "Under **What apps may do**, set each group of tools to **Off**, **Read** or **Read and change**.",
                "Under **Who may connect, and how**, tick the roles that may connect apps, and save.",
                "Register each AI app under **Settings → Access management → Applications** (see [Register an AI app](#register-an-ai-app)). Its client ID then shows to people on **Connect AI apps**.",
            ], howto="let-outside-ai-apps-connect", task="Let people connect outside AI apps to the Wiki"),
            P("Turning the switch off asks first. Every connected app stops at once, on every server; connections and their settings are kept and work again when it is turned back on. A space whose admins turned Kee off is closed to outside apps too."),
            H("What apps may do"),
            P("Each group of tools has a mode. A change is written at once, under the person's name, with the same permissions, page locks and limits as in the Wiki."),
            TABLE(["Group", "Tools", "Modes"], [
                ["**Core** (in every connection)", "Search, pages and their tree, spaces, comments and labels: 7 that read, 4 that change", "**Read** (default) or **Read and change**; it can't be off"],
                ["**Tool search** (in every connection)", "Find and run the tools that aren't in a connection's list", "Always on"],
                ["**Product docs** (in every connection)", "The Wiki's own documentation, built into your version", "**Off** or **Read**"],
                ["**Versions**", "A page's version history and earlier versions", "**Off** or **Read** (default)"],
                ["**Templates**", "Page templates of a space and the library", "**Off** or **Read** (default)"],
                ["**Attachments**", "Files attached to pages: list them and read their text", "**Off** or **Read** (default)"],
            ]),
            SHOT("kee-outside-apps-toolsets.png", "What apps may do: Core set to Read and change, Tool search always on, Product docs and Versions set to Read"),
            UL([
                "**Off** hides a group from the tool list, from tool search and from calls. People can't choose it for a connection.",
                "Only the Core group has tools that change today: create page drafts, change pages, comment, add and remove labels. No tool deletes anything or touches settings, permissions, people, keys or sign-in.",
                "An app changes something only when all three allow it: the application is registered for reading and changing, the person agreed to it when signing in, and the group is set to **Read and change** here. A key changes only when the person made it for reading and changing.",
                "A change applies to every connection from its next call.",
            ]),
            H("Who may connect, and how"),
            SHOT("kee-outside-apps-access.png", "Who may connect, and how: the roles that may connect apps, Let people make keys, calls per person per minute, the registered AI apps, use in the last 7 days and the connections with End connection"),
            TABLE(["Setting", "Default", "Meaning"], [
                ["**Who may connect AI apps**", "Administrators", "The roles of the **Connect AI apps** permission. Super admins always may. Groups are added in the Kee permissions grid on **Features and access**. A person's app never gets more than the person has"],
                ["**Let people make keys**", "Off", "For apps that can't open a browser to sign in. A key acts as the person who made it, is shown once and ends after at most 90 days. The switch is the installation's: it also covers keys for plugins that serve AI apps, and shows only to people who manage applications. Turning it off stops existing keys"],
                ["**Calls per person per minute**", "60", "All of a person's connections together; a change counts as two. 1 to 6000. Over it, the app is told how long to wait"],
            ]),
            H("Register an AI app"),
            P("Each AI app people sign in through is an application under **Settings → Access management → Applications**: a public application of the kind **AI agent**, with the app's redirect addresses, and this Wiki's server (`wiki`) among the servers it may use. Choose **Read only**, or **Read and change** for apps that may write. See [AI agents](oauth-applications.html#ai-agents)."),
            UL([
                "**Registered AI apps** on the tab lists them, marked **Read only** or **Read and change**.",
                "People find each app's client ID on their **Connect AI apps** page.",
                "The person signing in sees what the app asks for; changing the Wiki is listed apart, under a warning.",
            ]),
            H("Usage and connections"),
            UL([
                "**Use in the last 7 days**: people, tool calls, changes, and calls refused or failed.",
                "**Connections used in the last 7 days** (at most 50): the app, the person, key or sign-in, read only or read and change, calls, tools and changes.",
                "**End connection** asks first, then blocks that connection on every server: the app can no longer read or change the Wiki as that person. Their other connections are not affected. There is no undo: the person removes the connection and signs in again to reconnect.",
            ]),
            H("Audit and events"),
            UL([
                "Every change is in the audit log with the person, the app and the page: the page's own entry carries `via` and `via_app`, and the server adds `wiki_outside_apps:change` (tool, app, page, version; never content).",
                "Reads are counted in the usage numbers, not logged one by one.",
                "Settings changes raise `wiki.outside_apps.update` (audit `wiki_outside_apps:update_settings`); ending a connection raises `wiki.outside_apps.connection.revoke` (audit `wiki_outside_apps:revoke_connection`). A person's choice of groups for a connection is audited as `wiki_outside_apps:update_connection`.",
                "A change raises the page's own events (`page.create`, `page.publish`, `page.comment.create` and the rest) with `via: mcp`. See [Events](events.html#agents-and-outside-ai-apps).",
            ]),
            H("Cluster and Redis"),
            P("Settings, connections and ended connections are in the database and apply on every server with the next request. The call limit and the write budgets are shared through Redis; without Redis each server counts on its own."),
            H("Scheduled job"),
            TABLE(["Job", "When", "What it does"], [
                ["`wiki-outside-apps-cleanup`", "Daily at 03:41", "Deletes usage counts and unused connections older than 13 months, and retry keys older than a day"],
            ]),
            H("Limits"),
            UL([
                "Ending a connection doesn't remove the person's sign-in or key: it blocks the connection in the Wiki until they remove it.",
                "Usage and the connections list cover the whole installation, not one organization.",
                "An app that retries a new page or comment with the same retry key gets the first answer; if the first call never finished, the app is told the outcome isn't known and nothing is written.",
            ]),
        ])),
]

KEE_R2_SHARED = [
    # ---------------------------------------------------- kee-scheduled-help
    ("kee-scheduled-help", dict(
        label="Scheduled help", title="Scheduled help: stale pages and question suggestions", icon="clock",
        desc="Kee work that runs without anyone asking: the stale page finder for space admins and suggestions for new Q&A questions; the switches, the budget, a space's opt-in and the findings",
        keywords=["kee", "ai", "scheduled help", "stale page finder", "stale pages", "out of date", "findings", "question routing", "suggestions for new questions", "q&a", "budget", "scheduled budget", "archive", "review"],
        blocks=[
            P("Scheduled help is the only Kee work that runs without someone asking. It reads and suggests; it never changes a page. Two jobs exist: the **stale page finder**, which lists pages that look out of date for a space's admins, and **suggestions for new questions**, which shows the asker of a Q&A question pages and people that may answer it."),
            H("What it never does"),
            UL([
                "It never changes, archives or deletes a page, and never posts anything. A finding's **Update**, **Archive** or **Review** is advice to a person.",
                "It never reads a page under a page lock, of any kind, and never suggests one.",
                "It never reads a space whose admins didn't turn it on, or a space where Kee is off.",
                "It never shows anyone a page they can't read: findings and suggestions are checked against the reader's access when shown.",
            ]),
            H("Turn it on (administrators)"),
            P("Both jobs are off until an administrator turns them on in the **Scheduled help** card on **Settings → Kee → Features and access**, and then a space's admins turn them on for their space."),
            SHOT("kee-scheduled-help-settings.png", "The Scheduled help card: Suggestions for new questions and Stale page finder, each with its switch"),
            TABLE(["Setting", "Default", "Meaning"], [
                ["**Stale page finder**", "Off", "About once a week, looks for pages that seem out of date in the spaces that switched it on"],
                ["**Suggestions for new questions**", "Off", "When a question is asked in Q&A, suggests pages, earlier questions and people. Shown to the asker only"],
                ["**Monthly budget for scheduled help**", "0 (no budget)", "Separate from the budget for people's requests, so background work can never use it up. When it is spent, scheduled help stops until next month. The card shows what was spent this month"],
            ]),
            UL([
                "Scheduled help needs Kee on, a **Pro** licence and a default model, which it always uses.",
                "Its requests are in the usage report under their own features, with no person.",
                "A run stops at once when Kee, the feature or the space's switch is turned off, or the budget is spent; the space's settings say why it stopped.",
            ]),
            H("Turn it on for a space (space admins)"),
            STEPS([
                ("Open the space and select **Space settings** in its sidebar.", "space-rail.settings"),
                ("Open the **Kee** tab.", "space-tabs.ai"),
                "Under **Scheduled help**, tick **Look for pages that are out of date**, **Suggest this space's pages for new questions**, or both. It is saved at once.",
            ], howto="turn-on-scheduled-help-in-a-space", task="Turn on the stale page finder or question suggestions for a space"),
            SHOT("kee-scheduled-help-space.png", "A space's Kee tab, Scheduled help: Look for pages that are out of date, and Suggest this space's pages for new questions"),
            P("If the tab says **Your wiki's administrators have not turned this on**, ask them. Changing the switches raises `space.ai_help.update`, which a [policy](policies.html) can refuse."),
            H("The stale page finder"),
            UL([
                "It looks at published pages that haven't changed for six months, or that link to pages that are gone.",
                "Kee reads each one with its age and views and decides whether it looks stale. Every finding has a reason and a suggestion: **Update**, **Archive** or **Review**.",
                "It runs on Mondays at 06:00 (`wiki-ai-stale-pages`). An administrator can change the schedule or run it now under **Settings → Scheduler**.",
            ]),
            H("Findings"),
            P("A space's admins see **Pages that may be out of date** at the bottom of the space's **Kee** tab, with when the finder last ran."),
            SHOT("kee-scheduled-help-findings.png", "Pages that may be out of date in a space's Kee tab: a finding with its reason, the suggestion, the page's age and views, Mark as done and Dismiss"),
            UL([
                "Each finding names the page, why it looks stale, the suggestion, when it was published, its views in 90 days and its broken links.",
                "**Mark as done** or **Dismiss** closes it; **Open again** brings it back. The tabs **Open**, **Done** and **Dismissed** filter the list. Changing a finding raises `space.ai_finding.update`.",
                "Closed findings are removed after 90 days. A newer finding about the same page replaces the old one.",
                "Kee can be wrong. Open the page and decide for yourself.",
            ]),
            H("Suggestions for new questions"),
            P("A few minutes after a question is asked in [Q&A](qna.html), the asker may see **Kee suggests** under it: pages that may answer it, questions asked before, people who could answer and tags that fit. See [Q&A](qna.html#suggestions-from-kee)."),
            UL([
                "Only the asker sees them, and only pages and questions they can read.",
                "Pages come only from spaces that turned the suggestions on.",
                "Matching is by words in titles; the suggestions are a hint, not an answer.",
            ]),
            H("What is sent to the provider"),
            TABLE(["Job", "Sent"], [
                ["**Stale page finder**", "The text of pages that have not changed for six months or have broken links, with their age and view count"],
                ["**Suggestions for new questions**", "The question, and the titles and first lines of matching pages (from spaces that switched this on) and earlier questions"],
            ]),
            H("Scheduled jobs"),
            TABLE(["Job", "When", "What it does"], [
                ["`wiki-ai-stale-pages`", "Mondays at 06:00", "Starts the stale page finder (schedule editable, run now)"],
                ["`wiki-ai-help-continue`", "Every 2 minutes", "Carries on a run in batches, and makes suggestions for new questions"],
                ["`wiki-ai-help-cleanup`", "Daily at 03:47", "Removes closed findings after 90 days and old runs"],
            ]),
        ])),
]
