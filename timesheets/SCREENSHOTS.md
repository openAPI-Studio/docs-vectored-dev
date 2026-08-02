# TimeSheets docs — screenshots needed

64 screenshots. Save each one into `assets/screenshots/` using the
exact filename below. The docs pick them up automatically on the next build —
until then each slot renders a dashed placeholder naming the file it wants.

Guidance: capture the app at a comfortable browser width (about 1440px), use
the light theme unless the shot is specifically about dark mode, and use
realistic but fictional names and figures rather than real people's data.

## Getting Started

- [ ] `timesheets-marketplace-install.png`
      The TimeSheets listing on the Atlassian Marketplace, with the Get it now button
- [ ] `timesheets-hub-overview.png`
      The TimeSheets Hub with the Dashboard tab open, showing the tab bar across the top
- [ ] `timesheets-log-time-modal.png`
      The Log time dialog with a project, cost centre, date and duration filled in

## Logging Time

- [ ] `timesheets-log-time-modal-filled.png`
      The Log time dialog with one project and cost centre selected at the top, and three rows below for different dates and durations
- [ ] `timesheets-daily-hours-meter.png`
      The daily hours meter in the Log time dialog showing hours logged against the working day

## Time Templates

- [ ] `timesheets-template-editor.png`
      The template editor on Project Settings, showing several lines each with its own project, cost centre and duration
- [ ] `timesheets-apply-template.png`
      Applying a template from the Summary tab, with the date picker and the template's lines listed

## Cost Centers

- [ ] `timesheets-cost-centre-tree.png`
      The cost centre tree in Admin Settings, showing a parent with two children
- [ ] `timesheets-cost-centre-budget-fields.png`
      The cost centre editor showing the hours allotment and money budget fields side by side
- [ ] `timesheets-budget-status-card.png`
      The Budget status card showing hours and money bars for several cost centres, one of them over budget

## Approvals

- [ ] `timesheets-project-approvers-config.png`
      Project Settings showing the worklog approvers and leave approvers pickers with a person and a group selected
- [ ] `timesheets-approvals-queue.png`
      The Approvals tab showing a mixed queue of time entries and leave requests awaiting decision
- [ ] `timesheets-approvals-multiselect.png`
      The Approvals queue with several rows selected and the bulk approve and reject buttons visible

## Weekly Submission

- [ ] `timesheets-week-submit-bar.png`
      The weekly submission bar showing the week total and the Submit button
- [ ] `timesheets-weekly-approval-card.png`
      A submitted week in the Approvals queue showing the person, week and total hours with approve and reject actions

## Approver Delegation

- [ ] `timesheets-delegation-panel.png`
      The delegation panel showing an active delegation with dates and a Revoke action
- [ ] `timesheets-on-behalf-of-history.png`
      An approval history entry showing a decision made by one person on behalf of another

## Approval History

- [ ] `timesheets-entry-approval-history.png`
      The approval history for a single time entry showing submission and approval with a comment

## Leave Management

- [ ] `timesheets-apply-leave-modal.png`
      The Apply for leave dialog with a type, date range and the optional reason field visible
- [ ] `timesheets-leave-balances.png`
      A person's leave balances showing entitlement, used and remaining for several leave types
- [ ] `timesheets-leave-multi-project-approvals.png`
      A leave request showing per-project approval rows, one approved and one still pending

## Leave Auto-Decision

- [ ] `timesheets-leave-auto-decision-settings.png`
      The leave auto-decision settings showing the enable toggle, day count and action selector

## Public Holidays

- [ ] `timesheets-public-holidays-admin.png`
      The Public Holidays admin screen listing dates with names and regions

## Timesheet Locking

- [ ] `timesheets-calendar-locked-days.png`
      The Calendar with older days greyed out and a lock indicator, alongside editable recent days
- [ ] `timesheets-unlock-request-form.png`
      The unlock request form with a date range and a reason entered
- [ ] `timesheets-unlock-requests-admin.png`
      The Unlock Requests admin screen listing pending requests with grant and deny actions

## Dashboard & Gadgets

- [ ] `timesheets-gadget-picker.png`
      The gadget picker open, showing the available gadgets grouped by category
- [ ] `timesheets-dashboard-arranged.png`
      The Dashboard with several gadgets arranged in a grid, one being dragged

## Calendar

- [ ] `timesheets-calendar-month-view.png`
      The Calendar in month view showing logged hours per day, leave, and a public holiday
- [ ] `timesheets-calendar-multi-select.png`
      The Calendar with several days selected and the bulk log time action available
- [ ] `timesheets-calendar-work-mode.png`
      The right-click menu on a calendar day showing the work mode options

## Summary & Missing Days

- [ ] `timesheets-summary-month-totals.png`
      The Summary tab showing month totals broken down by project with billable split
- [ ] `timesheets-summary-missing-days.png`
      The missing days list showing working days with no time logged and a quick log action
- [ ] `timesheets-team-browser-pins.png`
      The team browser showing pinned colleagues with their work mode and status

## Reports & Exports

- [ ] `timesheets-team-matrix.png`
      The team matrix showing people down the side and days across, with hours in each cell
- [ ] `timesheets-matrix-cell-drilldown.png`
      The drill-down panel for a matrix cell listing the individual entries behind the total
- [ ] `timesheets-breakdown-view.png`
      The Breakdown view grouped by cost centre and person, showing hours, billable split and a proportion bar

## Scheduled Reports

- [ ] `timesheets-scheduled-report-form.png`
      The scheduled report form showing projects, cadence, run day and recipients
- [ ] `timesheets-scheduled-report-period-note.png`
      The scheduled report form showing the plain-language note explaining what period each run will cover

## Clients

- [ ] `timesheets-clients-list.png`
      The Clients admin screen listing clients with their currency and payment terms
- [ ] `timesheets-project-client-setting.png`
      Project Settings showing the client selector with a client chosen

## Billing Rates

- [ ] `timesheets-rates-list.png`
      The Billing Rates screen with rates grouped by scope, showing person, project, cost centre and site rates
- [ ] `timesheets-add-rate-modal.png`
      The Add billing rate dialog showing the scope selector, amount, currency and effective dates
- [ ] `timesheets-rate-preview.png`
      The rate preview showing the winning rate for a person and date, with the layer that produced it

## Invoices

- [ ] `timesheets-invoice-preview.png`
      The invoice preview showing lines, totals and a warning about unpriced work
- [ ] `timesheets-invoice-issued.png`
      An issued invoice showing its number, client details, lines and total
- [ ] `timesheets-invoice-numbering-audit.png`
      The numbering check showing the next number, issued and voided counts, and any gaps
- [ ] `timesheets-invoice-void-dialog.png`
      The void invoice dialog with the required reason field

## Billing Health

- [ ] `timesheets-billing-health-card.png`
      The Billing health card showing the four figures with two of them highlighted as needing attention

## Project Settings

- [ ] `timesheets-project-settings-overview.png`
      The Project Settings screen showing approval requirements, approvers and cost centre assignment
- [ ] `timesheets-project-teams-events.png`
      The project teams list and important dates section in Project Settings

## Jira Worklog Sync

- [ ] `timesheets-jira-worklog-synced.png`
      A Jira issue's Work log tab showing an entry created by TimeSheets

## Email Notifications

- [ ] `timesheets-email-ses-settings.png`
      The Email admin tab showing the SES credential fields and the sender in use
- [ ] `timesheets-email-template-editor.png`
      The email template editor showing a subject line, body and the available smart values

## Scheduler & Automation

- [ ] `timesheets-scheduler-jobs.png`
      The Scheduler admin tab listing the available jobs with their cadence and enabled state
- [ ] `timesheets-scheduler-dry-run.png`
      A dry run result showing what a job would have done without making changes

## Personal Settings

- [ ] `timesheets-personal-settings.png`
      The personal settings screen showing timezone, working days and logging defaults
- [ ] `timesheets-notification-preferences.png`
      The notification preferences screen listing categories with individual toggles

## Admin Settings

- [ ] `timesheets-admin-settings-general.png`
      The Admin Settings General tab showing working hours, weekdays, approval mode and lock window
- [ ] `timesheets-data-retention-settings.png`
      The Data retention card showing the four windows at their keep-forever defaults with a warning about a short window
- [ ] `timesheets-scheduler-audience.png`
      The scheduler audience settings showing the source selector, lookback window and recipient cap

## Erasure & Data Export

- [ ] `timesheets-erasure-preview.png`
      The erasure preview showing per-table counts of what would be deleted, replaced and retained
- [ ] `timesheets-data-export.png`
      The personal data export screen with an account entered and the resulting JSON summary
- [ ] `timesheets-erasure-log.png`
      The erasure log listing completed erasures with dates, actors and hashed subjects
