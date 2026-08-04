"""Core workflow pages: getting started, logging, templates, cost centres."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, SHOT

CORE = [
    ("getting-started", dict(
        label="Getting Started", title="Getting Started", icon="rocket",
        desc="Install TimeSheets and log your first entry",
        keywords=["install", "setup", "first run", "onboarding", "hub"],
        blocks=[
            P("TimeSheets adds time tracking, approvals, leave and billing to Jira Cloud. It runs entirely on Atlassian Forge, so there is nothing to host and no data leaves your Atlassian site except email."),
            P("This page takes you from a fresh install to a first logged entry. It should take about ten minutes."),

            H("Install the app"),
            P("Install TimeSheets from the Atlassian Marketplace. On first load the app creates its own tables, which takes a few seconds; if a screen looks empty immediately after installing, reload it once."),
            P("You need to be a **Jira site administrator** to install and to reach the admin screens. Everyone else can start logging time straight away."),
            SHOT("timesheets-marketplace-install.png", "The TimeSheets listing on the Atlassian Marketplace, with the Get it now button"),

            H("Open the Hub"),
            P("Everything a person needs day to day lives in one place, called the **Hub**. Find it under **Apps → TimeSheets** in the Jira top navigation."),
            P("The Hub has these tabs:"),
            TABLE(["Tab", "What it is for", "Shown to"], [
                ["Dashboard", "A configurable grid of gadgets — your week, pending approvals, leave balance and so on", "Everyone"],
                ["Summary", "Month totals, missing working days, and what your team is up to", "Everyone"],
                ["Calendar", "Month and week views of what you logged, plus leave and holidays", "Everyone"],
                ["Approvals", "Anything waiting on your decision, with the pending count in the tab label", "Approvers only"],
                ["Reports", "Team matrices, breakdowns and exports", "Approvers and project admins"],
            ]),
            P("Which emails you receive, and the mute and snooze controls, are in your [personal settings](personal-settings.html) rather than a tab of their own."),
            SHOT("timesheets-hub-overview.png", "The TimeSheets Hub with the Dashboard tab open, showing the tab bar across the top"),

            H("Log your first entry"),
            STEPS([
                "Open the Hub|and stay on the Dashboard, or go to the Calendar.",
                "Click Log time|or double-click a day in the Calendar to start on that date.",
                "Pick a project and a cost centre|the cost centre is how the work is classified for reporting and billing.",
                "Enter the time|in hours or minutes. Entries go in 5-minute increments.",
                "Optionally link a Jira issue|type a key or search by summary.",
                "Save|the entry appears immediately on your Calendar and Dashboard.",
            ]),
            SHOT("timesheets-log-time-modal.png", "The Log time dialog with a project, cost centre, date and duration filled in"),
            NOTE("If the project you want is not in the list, it either has no cost centres assigned to it yet, or you cannot browse it in Jira. Both are fixed by an administrator — see [Project Settings](project-settings.html)."),

            H("What an administrator should set up next"),
            P("TimeSheets works out of the box, but four things are worth deciding early because they shape everything else:"),
            OL([
                "**Cost centres.** How work is classified. Nothing can be logged until at least one is assigned to a project — see [Cost Centers](cost-centers.html).",
                "**Approvals.** Whether time needs approving at all, per entry or per week, and who approves it — see [Approvals](approvals.html).",
                "**Working hours and days.** The basis for capacity, missing-day detection and leave — see [Admin Settings](admin-settings.html).",
                "**Leave types.** Which categories your organisation uses. Health-related types arrive switched off on purpose — see [Leave Management](leave.html).",
            ]),
            P("Billing is entirely optional and off until you add a client and a rate. If you only want timesheets, you can ignore it."),

            H("Where to go next"),
            UL([
                "Logging in bulk, copying weeks and using templates — [Logging Time](logging-time.html)",
                "Getting time approved — [Approvals](approvals.html)",
                "Booking and approving leave — [Leave Management](leave.html)",
                "Turning approved hours into invoices — [Invoices](invoices.html)",
                "What is stored and who can see it — [Privacy & Data Handling](privacy-security.html)",
            ]),
        ])),

    ("logging-time", dict(
        label="Logging Time", title="Logging Time", icon="clock",
        desc="Log against cost centres and Jira issues, in 5-minute increments",
        keywords=["log", "worklog", "hours", "minutes", "duration", "copy week", "bulk"],
        blocks=[
            P("Time is logged against a **project** and a **cost centre**, on a date, for a number of minutes. A Jira issue is optional — plenty of real work does not have one, and TimeSheets does not pretend otherwise."),

            H("The Log time button"),
            P("**Log time** in the Hub header is a split control. The button itself opens the dialog, one click as always. The three dots beside it offer the alternatives:"),
            TABLE(["Choice", "What it does"], [
                ["Log time…", "The dialog — one project, as many rows as you need"],
                ["From a template…", "A saved set of rows applied to a date, and the only way to log across several projects at once"],
            ]),
            NOTE("The main button is deliberately not a menu. Turning the common case into a two-step choice to expose an occasional alternative would tax every routine use."),

            H("The Log time dialog"),
            P("Open it from the Hub, from a project page, or by double-clicking a day in the Calendar. Starting from the Calendar pre-fills the date."),
            SHOT("timesheets-log-time-modal-filled.png", "The Log time dialog with one project and cost centre selected at the top, and three rows below for different dates and durations"),
            TABLE(["Field", "Notes"], [
                ["Date", "Defaults to today, or to the day you clicked in the Calendar"],
                ["Project", "Chosen once for the whole dialog. Only projects you can browse in Jira, and which have at least one cost centre"],
                ["Cost centre", "Chosen once for the whole dialog. Only those assigned to the project; changing project resets it"],
                ["Duration", "Hours and minutes, in 5-minute steps. The smallest entry is 5 minutes"],
                ["Issue", "Optional. Search by key or summary"],
                ["Description", "Optional free text — see the note below"],
            ]),
            NOTE("Descriptions are visible to your approvers and appear in exports. Keep them about the work."),

            H("Several rows at once"),
            P("The dialog takes multiple rows, so several pieces of work go in as one save. Add a row with **Add row**."),
            WARN("**The project and cost centre are chosen once and shared by every row.** A row varies only by date, duration, description and issue. To log against two different projects you save twice — or use a [template](templates.html), which is the one thing that can span projects in a single action."),
            P("Rows can span **different dates**, which is the quickest way to catch up after a few days away without opening the dialog repeatedly."),
            P("If any row is invalid the save is refused and the offending row is marked — nothing is saved by halves."),

            H("The daily hours meter"),
            P("As you type, a meter shows how much you have logged that day against your working day. It reads, for example, `6h / 8h` when your working day is eight hours."),
            P("The meter is guidance, not a limit. The only hard ceiling is **24 hours per person per day**, which the server enforces as well as the browser — you cannot get past it by calling the API directly."),
            SHOT("timesheets-daily-hours-meter.png", "The daily hours meter in the Log time dialog showing hours logged against the working day"),

            H("Increments, and why they are five minutes"),
            P("Entries are whole 5-minute steps. That is small enough to be honest about short pieces of work and large enough that a timesheet does not become an exercise in false precision."),
            P("Billing can round differently — an organisation that bills in 15-minute or hourly blocks sets that separately, and the timesheet still shows what was actually worked. See [Billing Rates](billing-rates.html)."),

            H("Copying a previous week"),
            P("**Copy previous week** duplicates last week's entries onto this week, matching day for day. Find it on the **Summary** tab, in the *My week* panel, and on the matching dashboard gadget. It is meant for genuinely repeating work — a standing allocation to a project, a recurring internal meeting."),
            P("Copies are new entries in draft or pending state, exactly as if you had typed them. Review them before submitting: a copied week that nobody looked at is how a timesheet stops meaning anything."),
            WARN("If a cost centre used last week has since been detached from the project or deactivated, the copy fails and names the cost centre. Fix the entry or ask an administrator to reattach it."),

            H("Editing and deleting"),
            P("You can edit or delete your own entries while they are still editable. An entry stops being editable when:"),
            UL([
                "its date falls outside the **lock window** — see [Timesheet Locking](locking.html);",
                "in weekly mode, its week has been **submitted or approved** — see [Weekly Submission](weekly-submission.html);",
                "it has been **billed on an issued invoice**, which cannot be undone without voiding that invoice.",
            ]),
            P("Each of those gives a distinct message so you know which one applies and what to do about it."),

            H("Caps you may run into"),
            TABLE(["Cap", "Where it is set", "What happens"], [
                ["24 hours per day", "Fixed", "The save is refused"],
                ["Cost centre allotment", "Cost centre", "Refused once the cost centre's total hours are used up"],
                ["Weekly billable cap", "Project settings", "Refused once billable time on that project exceeds the weekly limit"],
            ]),
            P("All three are checked on the server at save time, not only in the browser."),
        ])),

    ("templates", dict(
        label="Time Templates", title="Time Templates", icon="file",
        desc="Save a recurring set of work as a one-click entry, across projects",
        keywords=["template", "recurring", "preset", "shortcut", "multi project", "standing allocation"],
        blocks=[
            P("A template is a saved set of lines you log often — a standing allocation, a weekly ceremony, a fixed support rotation. Applying one creates the entries in a single action."),
            NOTE("Templates are the **only** way to log against several projects at once. The [Log time dialog](logging-time.html) uses one project and one cost centre for all its rows; a template line carries its own."),

            H("Personal and project templates"),
            P("There are two kinds, using the same editor and behaving identically:"),
            TABLE(["Kind", "Managed from", "Who can use it"], [
                ["Personal", "The Templates section of the Summary tab", "Only you"],
                ["Project", "Project Settings → Templates", "People working on that project"],
            ]),
            P("Create a personal one for your own recurring pattern; create a project one when a whole team logs the same shape of work each week."),
            SHOT("timesheets-template-editor.png", "The template editor showing several lines, each with its own project, cost centre and duration"),

            H("Creating a template"),
            STEPS([
                "Open the Templates section|on the Summary tab for a personal template, or Project Settings for a project one.",
                "Add a line|for each piece of work.",
                "Set the project and cost centre per line|these can differ from line to line.",
                "Set a duration|in 5-minute steps, and optionally an issue and a description.",
                "Name and save it|the name is what you pick from later, so make it recognisable.",
            ]),
            P("A template stores project, cost centre, issue, duration and description for each line. It stores **no date** — that is chosen when the template is applied."),
            WARN("The lines of a template may not exceed 24 hours in total, since applying it puts them all on one day."),

            H("Applying a template"),
            P("Three ways in: the **three dots beside Log time** in the Hub header, the Templates section of the **Summary** tab, or a dashboard gadget. You choose the date; every line lands on that date."),
            SHOT("timesheets-apply-template.png", "Applying a template from the Summary tab, with the date picker and the template's lines listed"),
            P("Applying creates the entries directly rather than opening the Log time dialog for you to confirm. Check the date before you apply — a template dropped on the wrong day is corrected by deleting the entries, not by undoing the apply."),

            H("Applying runs the same checks as typing"),
            P("A template goes through exactly the validation a manual entry does. It will be refused if:"),
            UL([
                "a cost centre on one of its lines has since been **detached** from its project or deactivated;",
                "the date is inside a **locked** period, or a submitted or approved week;",
                "a line would breach a **cost centre allotment** or the project's **weekly billable cap**;",
                "the lines would take the day past 24 hours.",
            ]),
            P("Where a cost centre is the problem, the error names it, so a template that has gone stale after a reorganisation is quick to fix rather than mysterious."),

            H("Managing templates"),
            P("Rename, edit and delete templates from the same screen. Deleting one does not touch time already logged from it — those are ordinary entries once created."),
        ])),

    ("cost-centers", dict(
        label="Cost Centers", title="Cost Centres", icon="tag",
        desc="Hierarchical cost centres, hour allotments and money budgets",
        keywords=["cost center", "cost centre", "budget", "allotment", "billable", "hierarchy"],
        blocks=[
            P("A cost centre is how work is classified once it has been logged. Every entry has exactly one. They are internal structure — the customer being billed is a separate concept, see [Clients](clients.html)."),

            H("The cost centre tree"),
            P("Cost centres are hierarchical: a parent such as *Delivery* can contain *Delivery — Implementation* and *Delivery — Support*. The hierarchy is for reporting and for rate inheritance; it does not by itself restrict who can log what."),
            P("Create and edit them under **Admin Settings → Cost Centers**."),
            SHOT("timesheets-cost-centre-tree.png", "The cost centre tree in Admin Settings, showing a parent with two children"),
            TABLE(["Field", "What it does"], [
                ["Name", "Shown wherever a cost centre is picked"],
                ["Code", "Optional short reference for your finance system"],
                ["Parent", "Optional. Used for rate inheritance and reporting rollup"],
                ["Billable", "Whether work here counts as billable by default"],
                ["Max allotable hours", "An optional lifetime hours limit"],
                ["Budget", "An optional money limit, with its own currency"],
            ]),

            H("Assigning cost centres to projects"),
            P("A cost centre only appears in the Log time dialog for projects it has been assigned to. Assign them under **Project Settings**."),
            WARN("A project with no cost centres cannot have time logged against it at all. This is the most common reason a project is missing from the Log time dialog."),
            P("Detaching a cost centre stops it being used for **new** entries. Existing entries keep their cost centre — history is never rewritten — but copying an old week or applying an old template will fail and tell you why."),

            H("Billable, and what it really means"),
            P("The **Billable** flag is the default policy for new work. It decides whether hours land in the billable or non-billable bucket in reports."),
            P("Once work has been priced for billing, the answer to *was this billable* is frozen with it. Turning the flag off later changes what happens next; it does not restate what already happened. That distinction is deliberate — it is tolerable for a checkbox to reclassify hours, and not tolerable for it to silently restate money."),

            H("Hour allotments"),
            P("**Max allotable hours** caps the total hours that can ever be logged against a cost centre. Leave it empty for no limit."),
            P("Two things about it are easy to get wrong, so they are stated plainly in the interface:"),
            UL([
                "It is a **lifetime** total, not a per-month allowance. There is no date window on it.",
                "It counts the cost centre **on its own**. Time logged to a child cost centre does not consume the parent's allotment.",
            ]),

            H("Money budgets"),
            P("A cost centre can also carry a **money budget**, in its own currency. This exists because hours and money genuinely come apart: a hundred hours of a junior and a hundred hours of a principal are the same capacity and very different cost. A team can be comfortably inside its hours allowance and far past its budget at the same moment."),
            P("Money budgets are visible to billing administrators only, and spend is measured from the priced snapshot of approved work — the same figures that reach an invoice."),
            SHOT("timesheets-cost-centre-budget-fields.png", "The cost centre editor showing the hours allotment and money budget fields side by side"),

            H("Budget status and rollup"),
            P("**Budget status** on the Cost Centers screen shows both limits as separate bars, because a single combined health score would have to pick a winner exactly when the two disagree — which is when you are looking at it."),
            P("**Include sub-centres** rolls children into the parent's totals. This is for information only: the limits that actually block time logging still count each cost centre on its own. Turning the display on does not tighten anything, and the screen says so."),
            SHOT("timesheets-budget-status-card.png", "The Budget status card showing hours and money bars for several cost centres, one of them over budget"),

            H("Remaining balance"),
            P("When you pick a cost centre with an allotment, the Log time dialog shows what is left. If a save would exceed it, the save is refused with the remaining figure — on the server as well as in the browser."),
            P("Where an allotment is empty, no limit is shown and none is applied."),
        ])),
]
