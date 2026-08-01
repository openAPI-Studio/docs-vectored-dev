"""Admin Settings — a full reference for every site setting and what it affects."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, SHOT, CODE

SETTINGS = [
    ("admin-settings", dict(
        label="Admin Settings", title="Admin Settings", icon="gear",
        desc="Every site-wide setting, what it changes, and what it does not",
        keywords=["admin", "settings", "site", "configuration", "working hours", "approval mode",
                  "lock", "timezone", "branding", "defaults", "override", "reference"],
        blocks=[
            P("Site-wide settings, available to Jira site administrators under **Apps → TimeSheets → Settings**. This page is a reference: for each setting, what it actually changes, and — where it matters — what it deliberately does not."),
            NOTE("Two things to know before changing anything. **Some settings are overridden per person** (timezone, working weekdays) and some **per project** (leave auto-decision), so a site value is a default rather than a guarantee. And **settings apply going forward**: none of them retroactively rewrite entries, approvals or prices that already exist."),

            H("At a glance"),
            TABLE(["Setting", "Default", "Takes effect"], [
                ["Working hours", "09:00–17:00, 8h/day", "Immediately, on capacity displays"],
                ["Working weekdays", "Mon–Fri", "Immediately, on leave counts and missing days"],
                ["Approval mode", "Per entry", "Immediately, for new submissions"],
                ["Auto-approve timeout", "72 hours", "On the next scheduled sweep"],
                ["Timesheet lock", "30 days", "Immediately"],
                ["Leave policies", "Half-days on, no negative balance", "On the next leave request"],
                ["Leave auto-decision", "Off", "On the next scheduled sweep"],
                ["Worklog sync", "Off", "On the next approval"],
                ["Approver delegation", "On", "Immediately"],
                ["Project overrides", "Allowed", "Immediately"],
                ["Site timezone", "UTC", "Only for people with no timezone of their own"],
                ["Reminders", "On, 7 days", "On the next scheduled run"],
                ["Retention windows", "Audit 365 days, everything else forever", "On the next sweep"],
                ["Billing", "Off", "On the next approval"],
            ]),
            SHOT("timesheets-admin-settings-general.png", "The Admin Settings General tab showing working hours, weekdays, approval mode and lock window"),

            H("Working hours"),
            P("A start time, an end time, and **hours per day**. Of the three, hours per day is the one that does real work."),
            TABLE(["Affects", "How"], [
                ["The daily hours meter", "The denominator in `6h / 8h` while someone is logging time"],
                ["Capacity in dashboard gadgets", "What a full day is worth when showing utilisation"],
                ["Reports", "The expected total against which a person's logged time is compared"],
            ]),
            P("**What it does not do:** it does not stop anybody logging more or fewer hours. The meter is guidance. The only hard daily ceiling is 24 hours, and that is fixed."),
            P("Start and end times are presentational — they set expectations on screen and in reminder copy. TimeSheets does not record clock-in and clock-out times, so nothing is validated against them."),

            H("Working weekdays"),
            P("Which days of the week count as working days. This one reaches further than most people expect:"),
            TABLE(["Affects", "How"], [
                ["Leave day counts", "A request spanning a weekend consumes balance only for working days"],
                ["Missing days", "A non-working day is never reported as missing"],
                ["Reminders", "The nudge for unlogged time skips non-working days"],
                ["Calendar", "Non-working days are shown differently"],
                ["Report capacity", "The expected hours for a period"],
            ]),
            WARN("**A person's own working weekdays override this.** Somebody on a four-day week sets that in their [personal settings](personal-settings.html), and their leave counts and missing days follow their pattern, not the site's. Change the site value and part-time people are unaffected — which is usually what you want, and occasionally a surprise."),

            H("Approval mode"),
            P("**Per entry** or **weekly**. This changes how everybody works, which is why it is site-wide rather than per project."),
            TABLE(["Mode", "How time moves"], [
                ["Per entry", "Each entry is submitted and decided on its own"],
                ["Weekly", "Entries are drafts until a whole week is submitted, then decided together"],
            ]),
            P("Switching modes does not convert work already in flight. Entries already pending in per-entry mode stay pending and are still decidable; weeks already submitted stay submitted. Only new work follows the new mode."),
            P("See [Weekly Submission](weekly-submission.html) for what weekly mode changes day to day."),

            H("Auto-approve timeout"),
            P("Hours a pending item may sit before a scheduled job approves it. **Set it to 0 to switch it off** and require a positive decision on everything."),
            TABLE(["Affects", "How"], [
                ["Pending time entries", "Approved automatically once older than the timeout"],
                ["Submitted weeks", "The weekly sweep uses the same timeout"],
                ["Billing", "An auto-approved entry is priced exactly like a manually approved one"],
            ]),
            P("Automatically approved items are recorded as decided by the system, so a reviewer can always distinguish a considered approval from a lapsed one."),
            WARN("This is a convenience, not a control. If your organisation needs every entry positively approved — for a client contract, or an audit — set it to 0 and staff the queue. A timeout is not evidence that anybody looked."),

            H("Timesheet lock"),
            P("How many days back people may still edit their own time. **0 disables locking entirely.**"),
            TABLE(["Affects", "How"], [
                ["Creating entries", "Refused on a locked day"],
                ["Editing and deleting", "Refused on a locked day"],
                ["Moving an entry", "Refused if either the old or new date is locked"],
                ["The Calendar", "Locked days are greyed out and their right-click actions disabled"],
            ]),
            P("The window is measured in **each person's own timezone**, so a lock does not arrive a day early for a colleague further east."),
            P("**Shortening the window locks more days immediately.** Anyone mid-correction will be stopped, so a shorter window is worth announcing. Lengthening it reopens days, which is safe but may be surprising."),
            P("Locking can be relieved case by case with an [unlock request](locking.html). It cannot relieve a **billed** entry — that constraint comes from the invoice, not the calendar."),

            H("Leave policies"),
            TABLE(["Policy", "Effect when on", "Effect when off"], [
                ["Half-days allowed", "People can book 0.5 of a day", "The half-day option is not offered"],
                ["Allow negative balance", "A request may exceed the remaining balance", "A request exceeding the balance is refused"],
            ]),
            P("Negative balances suit organisations that accrue leave through the year and would rather allow a January holiday than block it. Leaving it off suits organisations where the balance is the entitlement."),
            P("Turning half-days off does not alter existing half-day leave — history is not rewritten."),

            H("Leave auto-decision"),
            P("Settles leave that has been pending too long, in a direction you choose. Three parts: **enabled**, **days**, and **action** (approve or reject). Off by default."),
            P("This is the one policy a project can override, if project overrides are allowed. A team whose leave genuinely needs a positive decision can require one while the rest of the site is happy with silence. See [Leave Auto-Decision](leave-auto-decision.html)."),
            P("Approvers are emailed before a request settles, so the deadline is not a surprise."),

            H("Worklog sync"),
            P("Whether approved, issue-linked entries are mirrored into native Jira worklogs. **Off by default**, because writing to Jira issues is a visible change that ought to be a decision."),
            TABLE(["Affects", "How"], [
                ["Approval", "An approved, issue-linked entry writes a Jira worklog"],
                ["Editing an approved entry", "The worklog is updated"],
                ["Rejection or deletion", "The worklog is removed"],
                ["Entries with no issue", "Nothing — they have nowhere to sync, and that is not an error"],
            ]),
            P("**Turning it on does not backfill.** Previously approved entries are not synced retroactively; only approvals from that point forward write worklogs. Turning it off leaves existing worklogs in place."),
            P("If Jira refuses a write, the approval still stands and the error is recorded. Approval never fails because a downstream sync did."),

            H("Approver delegation"),
            P("Whether [delegation](delegation.html) is available at all. On by default."),
            P("This exists as an emergency switch: it disables the delegation lookup site-wide without deleting anybody's arrangements. With no delegations set up the feature is already inert, so most sites never touch this."),
            WARN("Switching it off means existing delegates immediately stop being able to act. Their past decisions stand and remain attributed correctly."),

            H("Project overrides"),
            P("Whether projects may override site settings at all. On by default."),
            P("Turn it off to keep every team on identical rules — useful where consistency matters more than local judgement, or where you have been asked to demonstrate uniform policy. Existing overrides stop being applied while it is off, and start applying again if you turn it back on."),

            H("Site timezone"),
            P("The fallback timezone, used only for people who have none of their own."),
            P("TimeSheets resolves a person's timezone in this order:"),
            OL([
                "their **personal setting**, if they have set one;",
                "the timezone their **last logged entry** was recorded in;",
                "this **site setting**.",
            ]),
            P("Timezone decides which calendar day an entry belongs to and when the lock window closes for that person. Changing the site value affects only people who have never set one and never logged time."),

            H("Reminders"),
            P("Whether the in-app and email nudge for unlogged time runs, and after how many days a gap counts as worth mentioning."),
            TABLE(["Setting", "Effect"], [
                ["Reminders enabled", "Master switch for the reminder sweep"],
                ["Threshold days", "How far back a missing working day must be before it is flagged"],
            ]),
            P("Missing days are computed from working weekdays, public holidays and approved leave — so a holiday or a booked absence is never nudged about."),

            H("Data retention windows"),
            P("How long each category is kept before the retention sweep deletes it. All are in days; **0 means keep forever**."),
            TABLE(["Window", "Default", "Note"], [
                ["Approval history", "365 days", "The only one with a non-zero default — this table grows with every decision"],
                ["Leave history", "Keep forever", "The category with the strongest argument for a shorter window"],
                ["Timesheet history", "Keep forever", "Entries on an issued invoice are never deleted, whatever this says"],
                ["Email suppressions", "Keep forever", "Deleting these means the app may email an address that previously bounced"],
            ]),
            WARN("Deletion is irreversible and there is no restore inside the app. Every window except approval history ships at keep-forever on purpose: an upgrade that quietly started removing people's history would be worse than continuing to hold it while you decide."),
            P("The sweep reports what it deleted **and what it declined to delete**, so a protected row never looks like an empty run. Full detail in [Privacy & Data Handling](privacy-security.html)."),
            SHOT("timesheets-data-retention-settings.png", "The Data retention card showing the four windows at their keep-forever defaults with a warning about a short window"),

            H("Billing"),
            P("Billing is off until you configure it, and configuring it does nothing until a client and a rate exist."),
            TABLE(["Setting", "Effect"], [
                ["Default currency", "Suggested when creating a client or a rate. Does not convert anything"],
                ["Increment", "Rounds billed time up to a block: none, 6 minutes, 15 minutes or an hour"],
                ["Rounding mode", "How a half unit resolves when an amount is rounded"],
                ["Show rates to approvers", "Off, and named honestly — an amount reveals the rate behind it"],
            ]),
            P("**Increment is the one worth understanding.** With `none`, a client is billed for exactly the time logged. With `15min`, a 5-minute entry is billed as 15. The timesheet keeps showing 5 — what was worked and what is charged for are two different numbers, and an invoice line prints the charged one."),
            WARN("Changing the increment does not re-price work already captured. Existing prices keep the increment in force when they were captured; only new approvals use the new setting. Re-price a period explicitly if you want the change applied — see [Billing Health](billing-health.html)."),
            P("There is deliberately no currency conversion anywhere in TimeSheets. A rate in a currency other than the client's cannot bill that client, and is reported rather than converted."),

            H("Scheduler audience"),
            P("Who recurring reminders reach. There is no *everyone with a licence* option, because Jira does not offer a reliable way to enumerate that — so the roster is derived from sources you choose:"),
            TABLE(["Source", "Covers", "Misses"], [
                ["Past loggers", "Anyone who logged time in the lookback window — organic and self-maintaining", "Brand-new joiners who have not logged anything yet"],
                ["Jira groups", "Everybody in the named groups, including new joiners", "People outside those groups"],
                ["Projects", "The teams bound to the named projects", "People not on a project team"],
            ]),
            P("Sources are combined and de-duplicated. **Maximum recipients per run** is a hard cost backstop: a run over the cap is truncated and says so, rather than quietly mailing a whole site."),
            P("Reminder jobs that fan out to a derived roster also require your **own SES account** — see [Scheduler & Automation](scheduler.html)."),
            SHOT("timesheets-scheduler-audience.png", "The scheduler audience settings showing the source selector, lookback window and recipient cap"),

            H("Hub URL"),
            P("The link emails point back to. TimeSheets derives it automatically; set it explicitly only if your site is reached through a URL the app cannot infer."),
            P("Get it wrong and notifications still send — their links just land in the wrong place. Send a test after changing it."),

            H("Branding and welcome message"),
            P("A brand colour and the greeting on the Hub. Cosmetic: neither affects permissions, calculations or what anybody can see."),
            P("Leaving the colour empty uses the Jira brand token, so the app follows your site's own theme."),

            H("How settings interact"),
            P("A few combinations produce behaviour that is not obvious from either setting on its own:"),
            TABLE(["Combination", "What happens"], [
                ["Weekly mode + lock window", "A week can be locked by the calendar before it is submitted. People must submit inside the window"],
                ["Auto-approve + billing", "Time is priced by an unattended job. Prices are dated by the work's date, not the sweep's, so this stays deterministic"],
                ["Lock window + issued invoice", "Billed entries are frozen regardless of the window, and an unlock will not reopen them"],
                ["Project overrides off + per-project settings", "Existing overrides stop applying but are not deleted, and resume if you turn overrides back on"],
                ["Retention + invoices", "The sweep never deletes an entry on an issued invoice, whatever the timesheet window says"],
            ]),

            H("What no setting can do"),
            UL([
                "Let anybody approve their **own** time or leave.",
                "Let a delegate act beyond what the person who delegated to them can do.",
                "Show somebody their **own billing rate** in their own timesheet.",
                "Edit an entry that is on an **issued invoice**, without voiding it first.",
                "Convert between currencies.",
            ]),
            P("These are properties of the design rather than defaults, which is why they are not on this screen."),
        ])),
]
