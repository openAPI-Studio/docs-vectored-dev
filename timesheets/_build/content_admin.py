"""Settings, integrations, automation and the admin pages."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, SHOT

ADMIN = [
    ("scheduled-reports", dict(
        label="Scheduled Reports", title="Scheduled Reports", icon="send",
        desc="Email a recurring timesheet summary on a schedule you choose",
        keywords=["scheduled report", "recurring", "email report", "weekly", "monthly", "run day"],
        blocks=[
            P("A scheduled report emails a timesheet summary to a fixed list of people, on a schedule you set. It is for the recurring question — *how did last week go* — that otherwise gets asked by hand every Monday."),

            H("Creating a scheduled report"),
            STEPS([
                "Choose the projects|it should cover. You can only pick ones you manage.",
                "Choose the cadence|weekly or monthly.",
                "Choose the run day|see below.",
                "Add recipients|any email address, not only app users.",
                "Save|the first run happens on the next matching day.",
            ]),
            SHOT("timesheets-scheduled-report-form.png", "The scheduled report form showing projects, cadence, run day and recipients"),

            H("Choosing the run day"),
            P("The run day is configurable rather than fixed. A weekly report can run on any weekday; a monthly one on any day of the month."),
            P("When you set it up, the form states in plain language **which period each run will cover** — for example, a weekly report running on Monday covers the previous Monday to Sunday. That sentence exists because *last week* means different things to different people, and getting it wrong is only noticed a month later."),
            SHOT("timesheets-scheduled-report-period-note.png", "The scheduled report form showing the plain-language note explaining what period each run will cover"),

            H("Recipients and preferences"),
            P("Recipients are an explicit list — this is not derived from a project roster, so nobody is added by accident when a team changes."),
            P("People who have muted or opted out of app notifications still receive scheduled reports they are explicitly listed on, because somebody chose to send it to them. Personal notification controls are covered in [Personal Settings](personal-settings.html)."),

            H("Sending now"),
            P("**Send now** runs the report immediately without waiting for its schedule. Use it to check the recipients and the content before trusting it to run unattended."),
        ])),

    ("project-settings", dict(
        label="Project Settings", title="Project Settings", icon="settings",
        desc="Approval rules, teams, caps, cost centres and the billing client",
        keywords=["project settings", "approvers", "cap", "teams", "client", "overrides"],
        blocks=[
            P("Most of what makes TimeSheets behave differently for one team lives here. Open it from the project, or from **Admin Settings** if you administer several."),
            SHOT("timesheets-project-settings-overview.png", "The Project Settings screen showing approval requirements, approvers and cost centre assignment"),

            H("Approval requirements"),
            P("Two independent switches: whether **worklogs** need approval, and whether **leave** does. A project can require one and not the other."),
            P("Turning worklog approval off means entries on that project are final as soon as they are saved — and, if billing is configured, priced at that moment."),

            H("Approvers"),
            P("Name the people or groups who can decide, separately for worklogs and leave. Project administrators and site administrators can always decide as well. See [Approvals](approvals.html)."),

            H("Cost centres"),
            P("Assign the cost centres that may be used on this project. A project with none cannot have time logged to it at all."),

            H("Weekly billable cap"),
            P("An optional ceiling on billable hours per person per week for this project. Saving time above it is refused, on the server as well as in the browser."),
            P("It applies to billable cost centres only — internal work does not consume it."),

            H("Billing client"),
            P("Attach the project to a [client](clients.html) so its work can be invoiced. Optional; a project with no client is still tracked and reported on."),

            H("Overrides"),
            P("A project can override some site-wide settings, such as leave auto-decision. Whether overrides are permitted at all is itself a site setting, so an administrator can keep the configuration uniform if they prefer."),

            H("Teams, important dates and quick events"),
            P("Group members into named teams for the team browser, and record dates that matter to the project — a release, a client workshop — so they show on people's calendars alongside their own work."),
            SHOT("timesheets-project-teams-events.png", "The project teams list and important dates section in Project Settings"),
        ])),

    ("worklog-sync", dict(
        label="Jira Worklog Sync", title="Jira Worklog Sync", icon="link",
        desc="Mirror approved entries into native Jira worklogs",
        keywords=["worklog", "sync", "jira", "tempo", "native", "issue"],
        blocks=[
            P("TimeSheets keeps its own record of time so that entries without an issue are first-class. If you also want approved time to appear on the Jira issue itself, turn on worklog sync."),

            H("Enabling sync"),
            P("Switch it on in [Admin Settings](admin-settings.html). It is off by default, because writing to Jira issues is a visible change that should be a decision rather than a surprise."),

            H("What gets synced"),
            UL([
                "Only **approved** entries. Pending and rejected time never reaches Jira.",
                "Only entries that are **linked to an issue**. Time logged without one has nowhere to go, and is not an error.",
            ]),
            P("The worklog carries the duration, the date and the description."),
            SHOT("timesheets-jira-worklog-synced.png", "A Jira issue's Work log tab showing an entry created by TimeSheets"),

            H("Edits and deletions"),
            P("Changing an approved entry updates its Jira worklog. Rejecting or deleting one removes the worklog again, so Jira does not keep a record of time that was withdrawn."),

            H("Sync errors"),
            P("If Jira refuses a write — permissions, a deleted issue, a temporary outage — the entry keeps its approval and records the error. Approval never fails because a downstream sync did."),
            P("Failed syncs are visible so they can be retried rather than silently lost."),
            NOTE("Worklog sync writes to Jira using the `write:jira-work` scope. If you would rather TimeSheets never wrote to issues, leave sync off — everything else works without it."),
        ])),

    ("email", dict(
        label="Email Notifications", title="Email Notifications", icon="send",
        desc="SES delivery with editable templates and smart values",
        keywords=["email", "ses", "notification", "template", "bounce", "suppression", "aws"],
        blocks=[
            P("TimeSheets sends email through Amazon SES. This is the only thing the app sends outside Atlassian."),

            H("Built-in sender or your own"),
            TABLE(["Option", "What it means"], [
                ["Built-in", "Mail goes through our SES account. Nothing to configure. We are a processor and AWS a sub-processor for the message in transit"],
                ["Your own SES", "You supply AWS credentials and mail goes through your account. No third party in the path"],
            ]),
            P("Your own credentials always win over the built-in sender. They are stored **write-only** — no screen and no API returns them once saved."),
            SHOT("timesheets-email-ses-settings.png", "The Email admin tab showing the SES credential fields and the sender in use"),
            WARN("Leave notification emails include the **leave type name**. If you have Sick Leave enabled, those words travel with a person's name through whichever email path you choose. Using your own SES account keeps that inside your infrastructure."),

            H("Editing templates"),
            P("Every notification has an editable template — subject and body. Edit them under **Admin Settings → Email** to match your own tone or language."),
            SHOT("timesheets-email-template-editor.png", "The email template editor showing a subject line, body and the available smart values"),

            H("Smart values"),
            P("Templates support placeholders that are substituted when the mail is sent — the person's name, the dates, the project, a link back into the app. The editor lists the values available for the template you are editing."),

            H("Bounces and suppression"),
            P("SES reports bounces and complaints back to the app. An address that hard-bounces or reports a message as spam is added to a **suppression list** and is not emailed again."),
            P("This protects delivery for everyone on your site: a sender that keeps mailing dead addresses gets throttled. Suppressions are kept indefinitely by default — see [Privacy & Data Handling](privacy-security.html) for the retention control."),

            H("Test sends"),
            P("Send a test to yourself after changing credentials or a template. It is the quickest way to find a misconfigured sender before a real notification depends on it."),
        ])),

    ("scheduler", dict(
        label="Scheduler & Automation", title="Scheduler & Automation", icon="clock",
        desc="Recurring jobs, their audience, and the bulk-email cost gate",
        keywords=["scheduler", "job", "cron", "automation", "reminder", "dry run", "cleanup"],
        blocks=[
            P("Several things happen on a schedule rather than when somebody clicks. They are all listed, all optional, and all can be run as a dry run first."),

            H("Available jobs"),
            TABLE(["Job", "What it does", "Sends email"], [
                ["Timesheet reminders", "Nudges people who have missing days", "Yes"],
                ["Approval reminders", "Nudges approvers with a stale queue", "Yes"],
                ["Leave auto-decision", "Settles leave pending too long", "Yes"],
                ["Scheduled reports", "Sends the recurring summaries you configured", "Yes"],
                ["Approval history cleanup", "Deletes audit rows past their retention window", "No"],
                ["Data retention sweep", "Deletes leave, timesheet and suppression data past their windows", "No"],
                ["Unlock expiry cleanup", "Marks granted unlocks expired once their window passes", "No"],
            ]),
            SHOT("timesheets-scheduler-jobs.png", "The Scheduler admin tab listing the available jobs with their cadence and enabled state"),

            H("Enabling a job"),
            P("Each job has a cadence and, where relevant, a day. Enable only what you want; nothing runs unless you turn it on."),

            H("Choosing the audience"),
            P("Reminder jobs let you choose who they reach — everyone, or a narrower set. A reminder that goes to people it does not concern is a reminder people learn to ignore."),

            H("The bulk-email cost gate"),
            P("Jobs that fan email out to a derived list of people are gated behind using **your own SES account**. Sending to a whole site on the built-in sender is a cost we are not able to carry on your behalf, and a surprise bill for us is a surprise outage for you."),
            P("Jobs that send nothing, or send only to a short list you typed yourself, are not gated."),

            H("Dry runs and history"),
            P("**Dry run** reports what a job would do and changes nothing. Use it before enabling anything that deletes or emails."),
            P("Run history shows what each job did and when, so an unexpected change has somewhere to be traced to."),
            SHOT("timesheets-scheduler-dry-run.png", "A dry run result showing what a job would have done without making changes"),
        ])),

    ("personal-settings", dict(
        label="Personal Settings", title="Personal Settings", icon="gear",
        desc="Timezone, working days, logging defaults and notification controls",
        keywords=["personal", "timezone", "preferences", "notifications", "mute", "snooze"],
        blocks=[
            P("Your own settings, which affect only you. Nothing here changes anybody else's experience."),

            H("Opening your settings"),
            P("From the Hub, open your personal settings. Site-wide configuration is a separate screen and needs administrator rights — see [Admin Settings](admin-settings.html)."),
            SHOT("timesheets-personal-settings.png", "The personal settings screen showing timezone, working days and logging defaults"),

            H("Timezone"),
            P("Your timezone decides which calendar day an entry belongs to, and when the [lock window](locking.html) closes for you. Someone in Auckland should not lose access to a day before their colleague in Lisbon."),
            P("If you have not set one, it is derived from where you last logged time, falling back to the site default."),

            H("Working days"),
            P("Which days count as working days for you. This drives your capacity and which days are flagged as missing. Useful for part-time patterns that differ from the site default."),

            H("Logging defaults"),
            P("Pre-fill the project, cost centre or duration you use most, so the common case is one click rather than four."),

            H("Notification preferences"),
            P("Choose which emails you receive, per category. Turning one off does not turn it off for anybody else."),
            SHOT("timesheets-notification-preferences.png", "The notification preferences screen listing categories with individual toggles"),

            H("Mute and snooze"),
            P("**Mute** stops a category until you turn it back on. **Snooze** stops everything for a period — for when you are on leave and do not want a reminder about the timesheet you deliberately have not filled in."),
            NOTE("Scheduled reports you are explicitly listed on still arrive, because somebody chose to send them to you. See [Scheduled Reports](scheduled-reports.html)."),
        ])),

    ("data-requests", dict(
        label="Erasure & Data Export", title="Erasure & Data Export", icon="shield",
        desc="Handle a request to export or delete everything held about one person",
        keywords=["erasure", "export", "gdpr", "dsar", "right to be forgotten", "delete person"],
        blocks=[
            P("When someone asks for a copy of their data, or asks you to delete it, these are the tools. Both are **site-administrator only** and both are recorded."),
            NOTE("What the app does is described here. Whether you must act on a particular request, and within what deadline, is a decision for your organisation — see [Privacy & Data Handling](privacy-security.html)."),

            H("Before you start"),
            UL([
                "Confirm the request is genuine and comes from the person it concerns.",
                "Have the **Atlassian account ID**, not just a name. Two people can share a name.",
                "Remember erasure is **irreversible**. There is no undo and no backup restore inside the app.",
            ]),

            H("Previewing an erasure"),
            P("Always preview first. The preview counts exactly what would be deleted, replaced and kept, table by table, and changes nothing."),
            P("This is the only chance to notice that a request names the wrong person while noticing is still useful."),
            SHOT("timesheets-erasure-preview.png", "The erasure preview showing per-table counts of what would be deleted, replaced and retained"),

            H("Running an erasure"),
            P("Confirm explicitly to proceed — a typed confirmation rather than a checkbox, because this is the one action in the app with no undo at all."),
            P("Running it twice for the same person is safe: the second run reports that the account was already erased and does nothing."),

            H("What is deleted, replaced and kept"),
            TABLE(["Kind of record", "Treatment"], [
                ["Their own timesheets, leave, preferences, dashboard, status", "Deleted"],
                ["Decisions they made about other people's records", "Identity replaced, record kept — deleting it would break someone else's audit trail"],
                ["Work on an issued invoice", "Identity replaced, every amount untouched"],
                ["Free text anywhere — reasons, descriptions, comments", "Cleared, including on records that are otherwise kept"],
            ]),
            P("Where an identity is replaced it becomes a stable label such as `Former member #a1b2c3d4`, the same everywhere, so one person still reads as one person across a document."),

            H("Exporting one person's data"),
            P("The export produces a JSON document of everything held about one account. Each section says what erasure **would** do to those rows, so the person can see in advance what would go and what would be kept."),
            P("It is built from the same list of tables erasure uses, so the two can never disagree. If it hits its size limit it says so rather than presenting a partial answer as complete."),
            SHOT("timesheets-data-export.png", "The personal data export screen with an account entered and the resulting JSON summary"),

            H("The erasure log"),
            P("Every erasure is recorded: when, by whom, and how many rows in each category. The account itself is stored as a **one-way hash** — a record saying *we erased this person* that named the person would defeat the point."),
            P("The log is enough to prove an erasure happened and to match it to a request. It is not enough to reverse."),
            SHOT("timesheets-erasure-log.png", "The erasure log listing completed erasures with dates, actors and hashed subjects"),

            H("Data retention windows"),
            P("Erasure handles one person on request. Retention handles everybody, on a schedule. They are separate controls and you probably want both — see [Admin Settings](admin-settings.html)."),
        ])),

    ("permissions", dict(
        label="Permissions & Security", title="Permissions & Security", icon="shield",
        desc="Who can see and do what, and how access is enforced",
        keywords=["permission", "role", "access", "security", "scope", "admin", "approver"],
        blocks=[
            P("TimeSheets does not maintain its own user directory or its own roles. Access follows Jira, so removing somebody from a project in Jira removes their access here too, with nothing extra to remember."),

            H("Roles"),
            TABLE(["Role", "Where it comes from", "What it grants"], [
                ["Person", "Any licensed user", "Log their own time, book their own leave, see their own data"],
                ["Approver", "Named in Project Settings", "Decide time or leave for that project"],
                ["Project administrator", "Jira project admin", "Project settings, reports and approvals for that project"],
                ["Site administrator", "Jira site admin", "All settings, all projects, erasure and export"],
                ["Billing administrator", "Currently the same as site administrator", "Rates, invoices and every money figure"],
            ]),
            NOTE("Billing administrator is a separate check in the code even though it currently resolves to site administrator. That way introducing a distinct finance role later is one change, not thirty."),

            H("Project-scoped access"),
            P("Nearly everything is scoped by project. You see a project's data if you can browse it in Jira **and** you have a reason — you logged the time, you approve for it, or you administer it."),
            P("Requesting data for a project outside your scope is refused rather than silently returning nothing, so a report is never quietly narrower than you believe it to be."),

            H("Rules that have no exceptions"),
            UL([
                "Nobody approves their own time or leave — **including site administrators**.",
                "A delegate can never approve more than the person who delegated to them.",
                "Nobody sees their own billing rate in their own timesheet.",
                "An entry on an issued invoice cannot be edited by anyone until that invoice is voided.",
            ]),

            H("Enforcement is on the server"),
            P("Every check described here runs on the server. The interface hides what you cannot use as a convenience, but hiding a button is not a permission — calling the API directly gets the same refusal."),

            H("Scopes the app requests"),
            P("The Jira permissions TimeSheets asks for, and why each one is needed, are listed in [Privacy & Data Handling](privacy-security.html#4)."),

            H("Where your data lives"),
            P("Everything is stored in Atlassian's own Forge infrastructure. The only outbound traffic is email. Full detail in [Privacy & Data Handling](privacy-security.html)."),
        ])),
]
