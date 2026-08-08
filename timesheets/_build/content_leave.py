"""Leave, holidays, and the Hub views."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, SHOT

LEAVE = [
    ("leave", dict(
        label="Leave Management", title="Leave Management", icon="umbrella",
        desc="Leave types, balances, half-days and multi-project approval",
        keywords=["leave", "holiday", "absence", "pto", "vacation", "sick", "balance"],
        blocks=[
            P("Leave sits alongside time tracking so capacity, missing-day detection and reports all agree about who was actually available."),

            H("Applying for leave"),
            STEPS([
                "Open Apply for leave|from the Hub or the Calendar.",
                "Choose a type|the list is what your administrator has enabled.",
                "Pick your dates|weekends and public holidays are excluded from the day count automatically.",
                "Mark it as a half day|if it is one.",
                "Add a reason if you want to|it is optional — see below.",
                "Submit|it goes to the leave approvers of the projects you work on.",
            ]),
            SHOT("timesheets-apply-leave-modal.png", "The Apply for leave dialog with a type, date range and the optional reason field visible"),

            H("The reason field is optional, deliberately"),
            P("You do not have to give a medical or personal reason, and the form says so. If you leave it blank the request works exactly the same way."),
            P("If you do write something, it is handled carefully: it is not included in the approvals queue that every approver loads, it is fetched only by the approver actually deciding your request, and it stops being available to approvers once a decision is made. It is also not searchable."),
            NOTE("Full detail of how this data is treated is in [Privacy & Data Handling](privacy-security.html)."),

            H("Leave types and balances"),
            P("Each type has an annual entitlement in days. Your remaining balance is the entitlement, minus leave taken or pending, plus any manual adjustment an administrator has made."),
            P("Pending leave reserves balance. That stops two requests being submitted against the same last three days."),
            SHOT("timesheets-leave-balances.png", "A person's leave balances showing entitlement, used and remaining for several leave types"),
            P("Administrators configure types under **Admin Settings → Leave Types**, including whether a type auto-approves."),
            WARN("Types that imply health or family status — Sick, Maternity, Paternity, Bereavement and Half-day Personal — arrive **switched off** in a new installation. Turn on only what you have a basis to collect. A generic *Leave* type that implies nothing is enabled by default."),

            H("Half days"),
            P("A half day counts as 0.5 against the balance and half a working day against capacity. Whether half days are allowed at all is a site-level leave policy."),

            H("The multi-project rule"),
            P("Somebody who works across three projects is absent from all three. TimeSheets creates a **separate approval per project**, so each project's approver sees a request that concerns them."),
            P("The overall request is settled once every project has decided. If any project rejects, the request is rejected — one team cannot commit another team's approver to cover the gap."),
            SHOT("timesheets-leave-multi-project-approvals.png", "A leave request showing per-project approval rows, one approved and one still pending"),

            H("Cancelling"),
            P("You can cancel your own leave, including after it has been approved — plans change, and holding somebody to a booking they no longer need helps nobody."),
            P("Two rules apply, and neither is configurable:"),
            UL([
                "You can only cancel **your own** request.",
                "Leave that has already **finished** cannot be cancelled. Its end date is in the past, the days were consumed, and rewriting that would misstate the balance.",
            ]),
            P("A request that was **rejected** is already settled and cannot be cancelled either — there is nothing left to withdraw."),

            H("Leave on the calendar"),
            P("Approved and pending leave appears on your [Calendar](calendar.html) and in your team's view, so nobody schedules work into an absence that was already agreed."),
        ])),

    ("leave-auto-decision", dict(
        label="Leave Auto-Decision", title="Leave Auto-Decision", icon="zap",
        desc="Automatically settle leave that stays pending too long",
        keywords=["auto approve leave", "timeout", "pending leave", "escalation"],
        blocks=[
            P("A leave request nobody answers is worse than a rejected one — the person cannot plan. Auto-decision settles requests that have been pending too long, in a direction you choose."),

            H("How it works"),
            P("A scheduled job looks for leave that has been pending longer than the configured number of days and settles it. The result is recorded as a system decision, not as a person's judgement."),
            TABLE(["Setting", "Meaning"], [
                ["Enabled", "Off by default. Nothing happens until you turn it on"],
                ["Days", "How long a request may stay pending before it is settled"],
                ["Action", "Approve or reject once the time is up"],
            ]),

            H("Choosing a direction"),
            P("**Approve** suits organisations where leave is a notification rather than a negotiation, and silence means yes. **Reject** suits the opposite: nothing is agreed unless somebody agrees to it."),
            P("Either is defensible. What is not defensible is leaving requests pending indefinitely and letting people guess."),

            H("Site configuration"),
            P("Set it under [Admin Settings](admin-settings.html). It applies everywhere unless a project overrides it."),
            SHOT("timesheets-leave-auto-decision-settings.png", "The leave auto-decision settings showing the enable toggle, day count and action selector"),

            H("Per-project overrides"),
            P("A project can override the site setting under [Project Settings](project-settings.html) — useful where one team's leave genuinely needs a positive decision and the rest of the organisation is happy with silence."),

            H("Advance warning"),
            P("Approvers are emailed before a request auto-settles, so the deadline is not a surprise. If nobody acts, the request settles and everyone is told what happened and why."),
        ])),

    ("holidays", dict(
        label="Public Holidays", title="Public Holidays", icon="sun",
        desc="Site-wide holiday calendars that exclude days from capacity",
        keywords=["holiday", "bank holiday", "public holiday", "region", "calendar"],
        blocks=[
            P("Public holidays stop the app reporting a whole office as having missed a working day."),

            H("Adding holidays"),
            P("Add them under **Admin Settings → Public Holidays**: a date, a name, and optionally a region."),
            SHOT("timesheets-public-holidays-admin.png", "The Public Holidays admin screen listing dates with names and regions"),
            P("Mark a holiday as **recurring annually** if it falls on the same date every year — New Year's Day, for instance. Holidays that move, such as Easter, need adding per year."),

            H("How holidays affect capacity"),
            UL([
                "A holiday is not a working day, so it is not reported as a missing day.",
                "Leave spanning a holiday does not consume balance for it.",
                "Capacity figures in reports exclude it.",
            ]),

            H("Regions"),
            P("Region is a label for holidays that apply to only part of your organisation. Use it to keep several countries' calendars in one list without confusion."),
            NOTE("Which working days count at all is a separate, site-wide setting — see [Admin Settings](admin-settings.html)."),
        ])),

    ("dashboard", dict(
        label="Dashboard & Gadgets", title="Dashboard & Gadgets", icon="grid",
        desc="A configurable gadget dashboard, per person and per screen size",
        keywords=["dashboard", "gadget", "widget", "layout", "drag", "resize"],
        blocks=[
            P("The Dashboard is the first thing most people see. It is a grid of gadgets that each person arranges for themselves — what a delivery lead wants on screen is not what a developer wants."),

            H("What you start with"),
            P("A new dashboard opens with eleven gadgets in three rows — what to act on, what is outstanding, then context:"),
            TABLE(["Row", "Gadgets"], [
                ["Act", "Quick log · My week · Capacity · Billing days"],
                ["Outstanding", "Missing days · My week submissions · Leave balance · Logging streak"],
                ["Context", "Time by project · My open issues · Holidays & my leave"],
            ]),
            P("**Reset layout** puts this back if you rearrange things and want to start again. There are 23 gadgets in total; the rest are one click away in the picker."),
            NOTE("*Awaiting my approval* is deliberately not in the default set — it is useful only if you approve for a project, and would be a permanently empty tile for everyone else. Add it if it applies to you."),

            H("The weekly submit bar"),
            P("In [weekly approval mode](weekly-submission.html) a bar appears at the top of the Dashboard for the current week, showing its state and the button to submit it. On sites using per-entry approval it renders nothing at all."),

            H("Adding gadgets"),
            P("Open the gadget picker and choose what to add. Gadgets cover your own time, approvals waiting on you, Jira context, leave, and personal summaries."),
            SHOT("timesheets-gadget-picker.png", "The gadget picker open, showing the available gadgets grouped by category"),

            H("Rearranging and resizing"),
            P("Drag a gadget by its header to move it; drag its corner to resize. The layout saves automatically."),
            P("Layouts are stored **per screen size**, so the arrangement you build on a wide monitor does not produce an unusable stack on a laptop."),
            SHOT("timesheets-dashboard-arranged.png", "The Dashboard with several gadgets arranged in a grid, one being dragged"),

            H("Available gadgets"),
            TABLE(["Group", "What you get"], [
                ["Time", "This week at a glance, recent entries, quick log actions"],
                ["Approvals", "What is waiting on your decision, and what you have submitted"],
                ["Jira", "Issues assigned to you, recent activity, sprint context"],
                ["Leave", "Your balances and upcoming absence"],
                ["Personal", "Your own summaries, pinned teammates and status"],
            ]),

            H("Refreshing"),
            P("Gadgets load when the Dashboard opens and can be refreshed individually. They do not poll continuously — a dashboard that re-queries every few seconds is expensive for everyone on the site."),
        ])),

    ("calendar", dict(
        label="Calendar", title="Calendar", icon="calendar",
        desc="Month and week views, the month summary, and the day panel",
        keywords=["calendar", "month", "week", "select days", "right click", "work mode",
                  "day panel", "summary strip", "unlogged days", "capacity"],
        blocks=[
            P("The Calendar is the fastest way to see and fix a period of time. It has three parts: a **summary** of the month, the **grid**, and a **day panel** describing whichever day you last clicked."),
            P("The split is deliberate. A day cell is narrow, so the grid shows the shape of your month — how much, what status, which days are empty — while the panel beside it carries the detail for one day. That is why the grid abbreviates a day's total as `6:30` and the panel spells it out as `6h 30m`."),
            SHOT("timesheets-calendar-month-view.png", "The Calendar in month view showing the summary strip, the month grid with logged hours and leave, and the day panel on the right"),

            H("The month summary"),
            P("Four figures across the top, all about **you** and all about the month you are looking at."),
            TABLE(["Figure", "What it counts"], [
                ["Logged this month", "Everything except sent-back entries, against a target of your working days multiplied by the site's hours per day"],
                ["Awaiting approval", "Minutes and entries still pending, plus how long the oldest one has been waiting"],
                ["Unlogged days", "Working days already past with nothing logged. Holidays and days of leave are never counted, and neither is today"],
                ["Leave & holidays", "Days off this month, listed as spans rather than one date at a time"],
            ]),
            NOTE("**Unlogged days looks backwards, not forwards.** Today is not counted until it is over, and the rest of the month is not counted at all — otherwise every month would open by telling you that you had not yet done work that is not yet due."),
            SHOT("timesheets-calendar-summary-strip.png", "The four-cell month summary strip showing logged hours against target, awaiting approval, unlogged days and leave"),

            H("Reading a day"),
            P("Each day shows its number, the day's total, and up to four entries — ten in week view — with a coloured bar for each entry's status. Beyond that the cell says **+N more** rather than growing; the day panel lists them all."),
            P("Below the entries a day can carry a work-mode chip, a public holiday, leave, and a thin capacity bar showing the day's total against your daily target. The bar turns green once the target is met."),
            TABLE(["Colour", "Meaning"], [
                ["Green", "Approved, or auto-approved"],
                ["Amber", "Pending — waiting for a decision"],
                ["Red", "Sent back"],
            ]),
            P("The same three colours appear in the legend under the grid, so nothing depends on remembering them."),
            NOTE("A sent-back entry still appears on its day, but it is **not** counted in the day's total or in the month summary. Sent-back work is not logged time until it has been fixed and approved."),

            H("The day panel"),
            P("Click any day to describe it in the panel on the right: the date, your work mode, the day's total against target and how much is left, then every entry with its duration, description and status."),
            P("From the panel you can add an entry to that day, switch the day between **WFH** and **WFO**, see the week's running total against the week's target, and — on sites that approve by the week — submit or recall that week."),
            P("The panel stays put while a long month scrolls past it. On a narrow window it moves below the grid instead of beside it."),
            SHOT("timesheets-calendar-day-panel.png", "The day panel showing the selected day's total against target, its entries with durations and statuses, and the work mode toggle"),
            NOTE("Clicking a **locked** day still shows it in the panel, read-only. Being unable to change a day is not a reason to be unable to look at it."),

            H("Navigating"),
            P("The arrows step a month at a time, or a week in week view. **Today** returns to the current period. Today's date is always marked with a filled circle, wherever you have navigated to."),
            P("Switching between month and week returns you to the current period — the two views keep one position, not two."),

            H("Selecting days"),
            P("Selection works like a spreadsheet:"),
            TABLE(["Action", "Result"], [
                ["Click and drag", "Selects a range"],
                ["⌘-click, or Ctrl-click on Windows", "Adds or removes a single day, including a weekend"],
                ["Double-click", "Opens Log time for that day"],
                ["Right-click", "Opens the actions menu"],
            ]),
            P("Dragging a range covers **working days only**. Dragging across a fortnight to log five days each week should not sweep up the weekends in between — but ⌘-click still picks an individual Saturday when you did work one."),
            P("With days selected, **Log time** and **Apply leave** in the toolbar apply to all of them, and say how many."),
            SHOT("timesheets-calendar-multi-select.png", "The Calendar with a range of days selected and the toolbar showing the selection count"),

            H("Right-click actions"),
            P("Right-clicking a day offers: log time, apply for leave, work from home, work from office, and clear the selection. Each names how many days it will affect."),
            P("Right-clicking a day that is **not** already selected moves the selection to it first, so the menu always acts on the day you actually pointed at."),
            P("On a **locked** day the menu shows a single line explaining that the day is locked and needs an unlock request. It deliberately offers no actions — a menu that quietly applied to some other day would be worse than one that does nothing."),
            SHOT("timesheets-calendar-work-mode.png", "The right-click menu on a calendar day showing log time, apply leave and the two work mode options"),

            H("Leave and holidays"),
            P("Public holidays and leave both appear on the day. Leave is shown whatever its state — pending, approved or refused — with the status carried by the dot's colour, and spelled out in words when the window is wide enough. The day panel always names both."),

            H("Work modes"),
            P("A day can be marked **WFH** (working from home) or **WFO** (working from the office). Those are the only two values."),
            P("Work modes are informational: they do not affect capacity, totals or approval. What they are for is the team view — knowing who is where next Tuesday is the whole point."),
            P("Set one from the right-click menu for a whole selection, or from the day panel for the day you are looking at."),
        ])),

    ("summary", dict(
        label="Summary & Missing Days", title="Summary & Missing Days", icon="list",
        desc="Your month at a glance, your week, your leave, and where everybody is",
        keywords=["summary", "missing days", "unlogged", "team", "pins", "status", "totals",
                  "my week", "templates", "work mode", "contributors", "chart", "target"],
        blocks=[
            P("The Summary tab answers two questions: how is my own month going, and where is everybody. It is a personal view — for team and project reporting, see [Reports & Exports](reports.html)."),
            P("It is laid out in two columns. The **left** is your work, read top to bottom: the month, this week, your leave. The **right** is context you glance at rather than work through: the people you are watching, and the days you have not logged."),

            H("The month overview"),
            P("One headline figure — everything you have logged this month — against a target of your working days multiplied by the site's hours per day, with how many working days are left to close the gap."),
            P("Underneath, the same total split by state:"),
            TABLE(["Row", "What it counts"], [
                ["Approved", "Approved and auto-approved time"],
                ["Awaiting approval", "Submitted and still waiting for a decision"],
                ["Sent back", "Rejected time, **shown only when there is some**"],
                ["Leave taken this year", "Approved leave days so far this calendar year"],
            ]),
            NOTE("**Sent back time is not counted in the headline total.** It is reported so you know it needs attention, but work that has to be redone is not logged time. The same rule applies everywhere in the app."),
            NOTE("These are totals by **state**, not by project. For a breakdown by project, cost centre or person — and the billable split — use the [Breakdown view in Reports](reports.html), which is available to approvers and project administrators."),
            SHOT("timesheets-summary-month-overview.png", "The month overview card showing the headline logged total against target, the split by status, and the daily bar chart"),

            H("The daily chart"),
            P("One bar per day of the month, beside the totals. A dashed line marks your daily target."),
            P("**Every calendar day is drawn, including the empty ones** — the gaps are the point. A chart that showed only the days you logged against would make a patchy month look identical to a complete one."),
            TABLE(["Bar", "Meaning"], [
                ["Green", "Everything on that day is approved"],
                ["Amber", "Some of that day is still awaiting approval"],
                ["Flat grey stub", "Nothing logged that day"],
            ]),
            P("A day with a mix of both is drawn amber: the unfinished part is the part you can act on. Its height is still the whole day."),
            P("Bars are scaled with headroom above the target rather than against it, so a day you ran over is visibly taller than one that exactly hit the target rather than being clipped flat to the same height. Hovering a bar gives the date and the exact total."),

            H("My week"),
            P("This week's entries, grouped under each day with that day's running total — the question being asked of this list is nearly always \"is Tuesday complete?\" rather than \"what is my fourteenth entry\"."),
            P("The header carries the week total against the week's target, arrows to step between weeks, **Copy previous week**, and — on sites that approve by the week — **Submit week**. See [Logging Time](logging-time.html) for what copying does and when it refuses, and [Weekly Submission](weekly-submission.html) for submitting."),
            P("Each entry row shows its duration, project, issue and description, a status pill, and buttons to edit or delete it. An entry Jira could not sync carries a **sync** warning with the reason on hover."),
            P("On a **locked** day the edit and delete buttons are disabled rather than removed, so it is clear the entry exists and is simply closed to changes."),
            SHOT("timesheets-summary-week-list.png", "The My week card with entries grouped by day, each showing duration, project, status and the edit and delete buttons"),

            H("My leave"),
            P("Your own leave requests with their state, and the allowance they draw on — \"11 of 25 days used\"."),
            P("The allowance counts only leave types that **have** an entitlement. A type with no allowance configured is left out rather than counted as zero, which would quietly understate how much of your real allowance is gone."),
            P("Pending requests can be cancelled here. **History** on any request opens the decision trail, including which projects have decided and which have not, and the comment whoever decided it left."),
            P("Applying for leave starts from the [Calendar](calendar.html)."),

            H("Unlogged days"),
            P("Working days this month with nothing logged against them, in the right-hand column. Each is a row with its own **Log** button, which opens the log form already set to that date."),
            P("Days off, public holidays and approved leave are never listed, and neither is today — a day is not missing until it is over."),
            P("The card disappears entirely when there is nothing missing, so a complete month is silent rather than reassuring you at length."),
            SHOT("timesheets-summary-rail.png", "The right-hand column showing the Team card with pinned teammates and the Unlogged days card with per-day Log buttons"),

            H("Team"),
            P("The people you have pinned, shown with each person's work mode, their status, and any upcoming leave. This is what the section shows at rest — no picking a project first."),
            P("A dot on each avatar summarises the same thing at a glance: amber for somebody away, green for somebody with a status set, grey where nothing is known. The line underneath always says it in words too, so nothing depends on the colour."),
            P("Where somebody has both a status and upcoming leave, the leave is shown: it is the thing that changes whether you contact them."),

            H("Finding people to pin"),
            P("**Add** reveals a project picker and, where one exists, a team picker. Star anybody to pin them; the pickers stay out of the way the rest of the time."),
            P("Which projects you can pick follows your Jira access — you never see people on a project you cannot already see."),
            P("**It works without any setup.** With no team configured, the list is everyone who has logged time on that project in the last 90 days. That is derived rather than declared, so it stays current on its own, and the screen says when a list came from there."),
            TABLE(["Where the list comes from", "When"], [
                ["Recent contributors", "The default — no team has been set up, or a team exists but has no Atlassian group bound"],
                ["An Atlassian group", "A team was set up in [Project Settings](project-settings.html) and a group bound to it. A deliberate list always wins over the derived one"],
            ]),
            P("A project nobody has logged time against, and with no group bound, genuinely has nobody to show — and says so rather than looking broken."),
            SHOT("timesheets-team-browser-pins.png", "The Team card with Add open, showing the project picker and a list of people with star buttons"),

            H("Status and work mode"),
            P("Set a short status message to say what you are focused on, and mark a day's work mode from the [Calendar](calendar.html). Both are visible to colleagues who can see you here."),
            P("Pins are personal to you — pinning somebody does not tell them, and does not change what either of you can see."),

            H("Templates"),
            P("Your **personal** templates: create, edit, and apply them to a date. These belong to you alone."),
            P("The section is collapsed to a single row, with the number you have saved on the heading. Click it to open."),
            P("Templates shared with a whole project are managed in [Project Settings](project-settings.html) instead. Both kinds work the same way — see [Time Templates](templates.html)."),

            H("History"),
            P("Everything of yours that has been **decided** — time and leave, approved, auto-approved, rejected or cancelled. Collapsed by default; click the heading to open it."),
            P("It loads only when opened, and pages ten at a time. Time and leave are listed side by side and page independently, so one running out does not stop the other."),
            P("Each row carries the **reason** the decider gave, where they gave one, in red for a rejection. That comment lives in the audit trail rather than on the record itself, so it is fetched alongside."),
            P("In [weekly mode](weekly-submission.html) a third list appears for **weeks**. It has to: rejecting a week sends its entries back to draft so they can be fixed, which means the entry list holds no record of the rejection at all — the week does, comment and all."),
            NOTE("Work still waiting on somebody is not here — that is live, and lives in **My leave**, **My week** and the week-submissions gadget. History is the record of what already happened."),

            H("When something is sent back"),
            P("A rejection shows as a red **sent back** row in the alert strip at the top of the Hub, counting rejected time and leave from the last fortnight, with a link down to the History section."),
            P("You are also emailed, if email is configured, with whatever comment the approver left. A rejected time entry becomes editable again so you can correct and resubmit it; a rejected week goes back to draft — see [Weekly Submission](weekly-submission.html)."),
        ])),

]
