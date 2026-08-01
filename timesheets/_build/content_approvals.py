"""Approvals, weekly submission, delegation, history, locking."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, SHOT

APPROVALS = [
    ("approvals", dict(
        label="Approvals", title="Approvals", icon="check",
        desc="Per-project approvers, bulk decisions, and a full audit trail",
        keywords=["approve", "reject", "approver", "queue", "pending", "auto-approve"],
        blocks=[
            P("Time can require approval before it counts as final. Whether it does, and by whom, is decided per project."),

            H("How routing works"),
            P("An entry needs approval if the project it was logged to is configured to require it. The people who can decide are, in order:"),
            UL([
                "**Worklog approvers** named on that project's settings — individuals or groups;",
                "**Project administrators** for that project;",
                "**Jira site administrators**, who can decide anything.",
            ]),
            P("Nobody can approve their own time, including site administrators. That rule has no exceptions and no override."),
            NOTE("If a project requires approval but has no approvers named, its entries would otherwise sit forever. Those projects surface to site administrators so the gap is visible rather than silent."),

            H("Configuring approvers"),
            P("Set them under **Project Settings → Approvals**. Worklog and leave approvers are configured separately, because they are often different people — a delivery lead signs off hours, a line manager signs off absence."),
            SHOT("timesheets-project-approvers-config.png", "Project Settings showing the worklog approvers and leave approvers pickers with a person and a group selected"),
            P("Approvers can be individuals or Jira groups. Adding a group means anyone in it can decide."),

            H("The approvals queue"),
            P("The **Approvals** tab in the Hub is everything waiting on you. It appears only if you approve for at least one project."),
            P("Each row shows who logged the time, which project and cost centre, the date, the duration and the description. Leave requests appear here too, with the leave type and dates."),
            SHOT("timesheets-approvals-queue.png", "The Approvals tab showing a mixed queue of time entries and leave requests awaiting decision"),
            P("Use **Refresh** after someone tells you they have submitted something — the queue does not poll continuously."),

            H("Filters and multi-select"),
            P("Filter by type, project or person, or search by name, project, issue or description. Filters are there because approving fifty entries one at a time is how approval becomes rubber-stamping."),
            P("Tick rows and use the bulk actions to approve or reject several at once. Selection is scoped to what is on screen: applying a filter that hides a selected row also unselects it, so nothing gets decided that you could not see."),
            SHOT("timesheets-approvals-multiselect.png", "The Approvals queue with several rows selected and the bulk approve and reject buttons visible"),

            H("Rejecting"),
            P("A rejection requires a comment. The person gets told what to fix, and the comment is kept in the audit trail."),
            P("A rejected entry stays visible to its owner so they can correct and resubmit it. Rejecting also removes any price that had been captured for it — rejected work is not revenue."),

            H("Automatic approval"),
            P("Entries left pending beyond the **auto-approve timeout** are approved automatically by a scheduled job. The default is 72 hours; set it in [Admin Settings](admin-settings.html), or set it to zero to switch it off."),
            P("Automatically approved entries are marked as such and recorded as decided by the system, so a reviewer can always tell a considered approval from a lapsed one."),
            WARN("Auto-approval is a convenience, not a control. If your organisation needs every entry positively approved, set the timeout to zero and staff the queue."),

            H("What approval changes"),
            UL([
                "The entry counts as final in reports.",
                "If [worklog sync](worklog-sync.html) is on and the entry has an issue, a Jira worklog is written.",
                "If billing is configured, the entry is **priced** and that price is recorded — see [Billing Health](billing-health.html).",
            ]),
        ])),

    ("weekly-submission", dict(
        label="Weekly Submission", title="Weekly Submission", icon="calendar-check",
        desc="Submit a whole week for approval instead of individual entries",
        keywords=["weekly", "submit", "recall", "week", "timesheet submission"],
        blocks=[
            P("Some organisations approve time entry by entry; others expect a person to submit a complete week and a manager to sign it off in one go. TimeSheets supports both, chosen site-wide."),

            H("Switching to weekly mode"),
            P("Set **Approval mode** to *Weekly* in [Admin Settings](admin-settings.html). This changes how everyone works, so it is a site-wide decision rather than a per-project one."),
            P("In weekly mode individual entries are no longer approved on their own. They move as a week."),

            H("Submitting a week"),
            P("A week starts on Monday. While it is open, entries are **drafts** — yours to change freely. Submitting hands the whole week to your approver at once."),
            STEPS([
                "Fill in the week|as normal, from the Calendar or the Log time dialog.",
                "Check the totals|the submit bar shows the week's hours before you commit.",
                "Submit|every draft entry in that week becomes pending together.",
            ]),
            SHOT("timesheets-week-submit-bar.png", "The weekly submission bar showing the week total and the Submit button"),

            H("Recalling a submission"),
            P("Made a mistake? **Recall** pulls the week back, provided nobody has decided it yet. The entries return to draft and you can edit them."),
            P("Once a week has been approved or rejected it cannot be recalled — that would rewrite a decision someone already made."),

            H("Approving a week"),
            P("Approvers see submitted weeks in the Approvals queue as a single item with the week's total. Approving accepts every entry in it; rejecting sends the whole week back with a comment."),
            SHOT("timesheets-weekly-approval-card.png", "A submitted week in the Approvals queue showing the person, week and total hours with approve and reject actions"),
            NOTE("Weekly mode has its own automatic-approval sweep, using the same timeout as per-entry mode. A week left undecided long enough is approved and marked as system-decided."),

            H("What locks while a week is out"),
            P("A submitted or approved week cannot be edited. Attempting to change an entry in one gives a message saying whether it is submitted (recall it) or approved (it is final). This is separate from, and additional to, the [lock window](locking.html)."),
        ])),

    ("delegation", dict(
        label="Approver Delegation", title="Approver Delegation", icon="umbrella",
        desc="Nominate someone to approve on your behalf while you are away",
        keywords=["delegate", "cover", "holiday", "out of office", "stand in", "on behalf of"],
        blocks=[
            P("An approver going on leave leaves a queue behind them. Delegation lets someone else act in their place for a defined period, without handing over permissions permanently."),

            H("Why delegate rather than add an approver"),
            P("Adding somebody as a permanent approver is easy to do and easy to forget to undo. A delegation has an **end date**, is visible to everyone involved, and every decision made under it records who actually clicked as well as whose queue it came from."),

            H("Setting up cover"),
            STEPS([
                "Open your delegation panel|from the Hub.",
                "Choose a delegate|anyone who can browse the relevant projects.",
                "Set the dates|start and end. The end date is required.",
                "Optionally add a reason|useful for whoever reviews the audit trail later.",
                "Save|the delegate sees your queue from the start date.",
            ]),
            SHOT("timesheets-delegation-panel.png", "The delegation panel showing an active delegation with dates and a Revoke action"),

            H("What a delegate can do"),
            P("Everything you could do as an approver, for the projects you approve: approve, reject with a comment, and act in bulk. Their decisions carry both names — theirs as the actor, yours as the person on whose behalf they acted."),
            SHOT("timesheets-on-behalf-of-history.png", "An approval history entry showing a decision made by one person on behalf of another"),

            H("What a delegate cannot do"),
            UL([
                "Approve **their own** time or leave, even through your delegation.",
                "Approve for projects **you** do not approve for. A delegation cannot grant more than the delegator has.",
                "Change project settings, add approvers, or delegate onward to somebody else.",
            ]),

            H("Both of you can decide"),
            P("A delegation is additive, not a handover. While it is running, you and your delegate can both act. If you check in from holiday and clear the queue yourself, nothing breaks."),

            H("Ending cover early"),
            P("**Revoke** ends a delegation immediately. Decisions already made under it stand — they were validly made at the time, and the record says so."),

            H("Admin-arranged delegation"),
            P("Site administrators can set up a delegation on someone else's behalf, for the case that matters most: an approver who is already away and did not arrange cover. The audit trail records who created the delegation as well as who used it."),
            NOTE("Delegation can be switched off site-wide in [Admin Settings](admin-settings.html) without deleting anything, as an emergency control. With no delegations set up, the feature is already inert."),
        ])),

    ("approval-history", dict(
        label="Approval History", title="Approval History", icon="history",
        desc="The record of every approval decision, and how long it is kept",
        keywords=["audit", "history", "trail", "who approved", "record", "retention"],
        blocks=[
            P("Every decision TimeSheets makes or records — approvals, rejections, automatic sweeps, unlock grants, invoice issues, erasures — appends a row to an audit trail. Nothing in the app edits an existing row."),

            H("Per-entry history"),
            P("Open any entry's history to see what happened to it: who submitted it, who decided it, when, and any comment they left."),
            SHOT("timesheets-entry-approval-history.png", "The approval history for a single time entry showing submission and approval with a comment"),

            H("Project activity"),
            P("Project administrators can see the decision feed for a whole project — useful when a customer asks how a month was signed off, or when you are trying to work out why something was rejected."),

            H("Automatic decisions"),
            P("Decisions made by a scheduled job are recorded as made by the system, with the rule that triggered them. An automatic approval is never presented as a person's judgement."),

            H("Acting on behalf of someone"),
            P("Where a decision was made under a [delegation](delegation.html), the trail records both people. This is the reason delegation is preferred over quietly adding an approver: the record stays truthful about who actually acted."),

            H("Retention"),
            P("The audit trail only ever grows, so it is the one table with a retention window switched on by default: **365 days**. Change it in [Admin Settings](admin-settings.html), or set it to zero to keep everything forever."),
            P("Other categories of data default to keeping everything — see [Privacy & Data Handling](privacy-security.html) for the full picture."),
            WARN("Check your own compliance requirements before shortening this. Approval history is often the evidence that a timesheet was reviewed at all."),

            H("What happens when someone is erased"),
            P("Erasing a person does not delete the decisions they made about other people's timesheets — that would break the record of someone who did not ask for anything. Their identity is replaced with a stable label and the decision itself survives. See [Erasure & Data Export](data-requests.html)."),
        ])),

    ("locking", dict(
        label="Timesheet Locking", title="Timesheet Locking", icon="lock-closed",
        desc="Freeze past periods, with admin-granted unlock windows",
        keywords=["lock", "freeze", "closed period", "unlock request", "read only"],
        blocks=[
            P("Once a period has been reported on or invoiced, letting people quietly change it undermines every number that came out of it. Locking freezes the past after a set number of days."),

            H("The lock window"),
            P("Set **Timesheet lock** in [Admin Settings](admin-settings.html) to a number of days. Entries older than that become read-only. The default is 30 days; zero disables locking entirely."),
            P("The window is measured in **each person's own timezone**, derived from their settings — so a lock does not arrive a day early for someone in Auckland."),

            H("What locking prevents"),
            UL([
                "Creating an entry on a locked day.",
                "Editing or deleting an existing entry on a locked day.",
                "Moving an entry onto a locked day.",
            ]),
            P("The Calendar greys out locked days, right-click actions are disabled on them, and the server refuses the same operations independently — the interface is a convenience, not the control."),
            SHOT("timesheets-calendar-locked-days.png", "The Calendar with older days greyed out and a lock indicator, alongside editable recent days"),

            H("Requesting an unlock"),
            P("If a genuine correction is needed, request an unlock from the locked day itself. Say why — the reason is what the reviewer decides on."),
            STEPS([
                "Open the locked day|and choose Request unlock.",
                "Give a reason and the dates|you need reopened.",
                "Wait for a decision|you are notified either way.",
                "Make the correction|the unlock window is time-limited.",
            ]),
            SHOT("timesheets-unlock-request-form.png", "The unlock request form with a date range and a reason entered"),

            H("Reviewing unlock requests"),
            P("Requests go to site administrators, under **Admin Settings → Unlock Requests**. A granted unlock reopens the named dates for that person only, for a limited window."),
            SHOT("timesheets-unlock-requests-admin.png", "The Unlock Requests admin screen listing pending requests with grant and deny actions"),

            H("Automatic re-locking"),
            P("Granted unlocks expire on their own; a scheduled job marks them expired once the window has passed. Nobody has to remember to re-lock anything."),

            H("Billed time is a stronger lock"),
            P("An entry that has been billed on an issued invoice cannot be edited even inside an unlock window, and the message says so. Requesting an unlock will not help, because the constraint is the invoice, not the calendar. The invoice has to be voided first — see [Invoices](invoices.html)."),
        ])),
]
