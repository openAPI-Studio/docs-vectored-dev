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

            H("Cancelling and recalling"),
            P("You can cancel your own request while it is pending. Once approved, cancelling depends on your administrator's policy — the days are already reserved and other people may have planned around them."),

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
        desc="Month and week views with multi-select and right-click actions",
        keywords=["calendar", "month", "week", "select days", "right click", "work mode"],
        blocks=[
            P("The Calendar is the fastest way to see and fix a period of time. Month view for shape, week view for detail."),

            H("Navigating"),
            P("Switch between month and week, and step through periods with the arrows. Today is always marked."),
            SHOT("timesheets-calendar-month-view.png", "The Calendar in month view showing logged hours per day, leave, and a public holiday"),

            H("Selecting days"),
            P("Click a day to select it; drag or shift-click for a range. With days selected you can log time across all of them at once — useful for a week of the same standing allocation."),
            SHOT("timesheets-calendar-multi-select.png", "The Calendar with several days selected and the bulk log time action available"),

            H("Right-click actions"),
            P("Right-click a day for its actions: log time, apply for leave, set a work mode, or request an unlock if the day is locked."),
            P("On a locked day the editing actions are disabled rather than hidden, so it is clear the day exists and is simply closed."),

            H("Leave and holidays"),
            P("Approved and pending leave shows on the calendar, as do public holidays. Pending leave is distinguished from approved so you can see what is still uncertain."),

            H("Work modes"),
            P("Mark a day as office, remote or anything else your organisation uses. Work modes are informational — they do not affect capacity or approval — but they make the team view genuinely useful for planning who is where."),
            SHOT("timesheets-calendar-work-mode.png", "The right-click menu on a calendar day showing the work mode options"),
        ])),

    ("summary", dict(
        label="Summary & Missing Days", title="Summary & Missing Days", icon="list",
        desc="Month totals, missing working days, and your team at a glance",
        keywords=["summary", "missing days", "team", "pins", "status", "totals"],
        blocks=[
            P("The Summary tab answers two questions: how did my month go, and where is everyone?"),

            H("Month summary"),
            P("Totals for the month, split by project and cost centre, with billable and non-billable separated."),
            SHOT("timesheets-summary-month-totals.png", "The Summary tab showing month totals broken down by project with billable split"),

            H("Missing days"),
            P("A working day with no time logged and no leave booked is a **missing day**. The list is calculated from your working weekdays, your public holidays and your approved leave — so a holiday or a booked absence is never flagged."),
            P("It is a prompt, not an accusation. People forget; this is what reminds them before a month closes."),
            SHOT("timesheets-summary-missing-days.png", "The missing days list showing working days with no time logged and a quick log action"),

            H("Team browser"),
            P("See what your colleagues have going on — who is on leave, who is working remotely, and their status. Which teams you can see follows your Jira project access."),

            H("Pins and status"),
            P("Pin the people you work with most so they stay at the top of your team view. Set a short status message to say what you are focused on."),
            P("Pins are personal to you. Status messages are visible to colleagues who can see you in the team browser."),
            SHOT("timesheets-team-browser-pins.png", "The team browser showing pinned colleagues with their work mode and status"),
        ])),
]
