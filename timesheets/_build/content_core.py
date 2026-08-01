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
            TABLE(["Tab", "What it is for"], [
                ["Dashboard", "A configurable grid of gadgets — your week, pending approvals, leave balance and so on"],
                ["Calendar", "Month and week views of what you logged, plus leave and holidays"],
                ["Summary", "Month totals, missing working days, and what your team is up to"],
                ["Approvals", "Anything waiting on your decision. Only appears if you approve for at least one project"],
                ["Reports", "Team matrices and exports, for projects you manage"],
                ["Notifications", "Which emails you receive, and mute or snooze controls"],
            ]),
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

            H("The Log time dialog"),
            P("Open it from the Hub, from a project page, or by double-clicking a day in the Calendar. Starting from the Calendar pre-fills the date."),
            SHOT("timesheets-log-time-modal-filled.png", "The Log time dialog with three rows filled in for different projects on the same day"),
            TABLE(["Field", "Notes"], [
                ["Date", "Defaults to today, or to the day you clicked in the Calendar"],
                ["Project", "Only projects you can browse in Jira, and which have at least one cost centre"],
                ["Cost centre", "Only those assigned to the chosen project. Changing project resets this"],
                ["Duration", "Hours and minutes, in 5-minute steps. The smallest entry is 5 minutes"],
                ["Issue", "Optional. Search by key or summary"],
                ["Description", "Optional free text — see the note below"],
            ]),
            NOTE("Descriptions are visible to your approvers and appear in exports. Keep them about the work."),

            H("Several rows at once"),
            P("The dialog takes multiple rows, so a whole day goes in as one save. Add a row with **Add row**; each row can have its own project, cost centre, issue and duration."),
            P("Rows can also span **different dates**, which is the quickest way to catch up after a few days away without opening the dialog repeatedly."),
            P("If any row is invalid the save is refused and the offending row is marked — nothing is saved by halves."),

            H("The daily hours meter"),
            P("As you type, a meter shows how much you have logged that day against your working day. It reads, for example, `6h / 8h` when your working day is eight hours."),
            P("The meter is guidance, not a limit. The only hard ceiling is **24 hours per person per day**, which the server enforces as well as the browser — you cannot get past it by calling the API directly."),
            SHOT("timesheets-daily-hours-meter.png", "The daily hours meter in the Log time dialog showing hours logged against the working day"),

            H("Increments, and why they are five minutes"),
            P("Entries are whole 5-minute steps. That is small enough to be honest about short pieces of work and large enough that a timesheet does not become an exercise in false precision."),
            P("Billing can round differently — an organisation that bills in 15-minute or hourly blocks sets that separately, and the timesheet still shows what was actually worked. See [Billing Rates](billing-rates.html)."),

            H("Copying a previous week"),
            P("**Copy previous week** duplicates last week's entries onto this week, matching day for day. It is meant for genuinely repeating work — a standing allocation to a project, a recurring internal meeting."),
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
        desc="Save recurring work as reusable one-click entries",
        keywords=["template", "recurring", "preset", "shortcut"],
        blocks=[
            P("A template is a saved set of rows you log often — a standing project allocation, a weekly ceremony, a fixed support rotation. Applying one fills the Log time dialog rather than saving behind your back, so you can adjust before committing."),

            H("Creating a template"),
            STEPS([
                "Fill in the Log time dialog|with the rows you want to keep.",
                "Choose Save as template|and give it a name you will recognise in a list.",
                "It appears in your template list|available from the Log time dialog from then on.",
            ]),
            SHOT("timesheets-save-as-template.png", "The Save as template control in the Log time dialog with a name entered"),
            P("A template stores the project, cost centre, optional issue, duration and description of each row. It does **not** store a date — that is chosen when you apply it."),

            H("Applying a template"),
            P("Pick a template from the Log time dialog and its rows appear, pre-filled. Change anything you like, set the date, and save."),
            P("Applying a template goes through exactly the same validation as typing the rows yourself, including cost-centre and cap checks. A template made before a cost centre was detached from a project will be refused, naming the cost centre."),
            SHOT("timesheets-apply-template.png", "The template picker open in the Log time dialog, with a template's rows loaded below"),

            H("Managing templates"),
            P("Templates are personal to you by default. Rename or delete them from the same picker."),
            P("Deleting a template does not touch any time already logged from it — the entries are ordinary entries once saved."),
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
