# Depotex docs — screenshots needed

86 screenshots. Save each one into `depotex/assets/` using the
exact filename below. The docs pick them up automatically on the next build —
until then each slot renders a dashed placeholder naming the file it wants.

Guidance: capture the app at a comfortable browser width (about 1440px), use
the light theme unless the shot is specifically about dark mode, and use
realistic but fictional names and figures rather than real people's data.

## Getting Started

- [ ] `setup-wizard.png`
      The setup wizard's first step: the installation ID to request a license with, and the license

## Dashboard

- [ ] `dashboard-overview.png`
      Dashboard: what needs attention, the installation's figures, spaces by size and the system's health

## Spaces

- [ ] `spaces-list.png`
      Spaces: every space you can see, with its repositories, formats, members and storage
- [ ] `spaces-space.png`
      A space's overview: figures, recently published versions, what needs attention, formats and upstreams
- [ ] `spaces-create.png`
      New space: name, key, description, visibility and formats
- [ ] `spaces-repositories.png`
      A space's Repositories tab: hosted, proxy and group repositories with their format, size and last upload
- [ ] `repository-page.png`
      A repository's page: its address, setup for the package manager, and its contents
- [ ] `upload.png`
      Upload: pick a hosted repository you can publish to, then add files
- [ ] `spaces-members.png`
      A space's Members tab: add people, groups and service accounts, and change their role

## Repository groups

- [ ] `repository-group.png`
      A group repository: its members in the order they're asked, and the space's universal URL

## Browse

- [ ] `browse-search.png`
      Browse: search every repository you can see, filter by space, format and type
- [ ] `browse-tree.png`
      The tree of a repository, with its address and setup instructions
- [ ] `browse-version.png`
      A version: install command, overview, files, dependencies and security, with downloads and recent activity

## Upstreams

- [ ] `upstreams-list.png`
      Upstreams: each registry's format, address, the spaces that use it and its health
- [ ] `upstreams-linked-source.png`
      Add upstream from a linked instance: its spaces and repositories, loaded live

## Repository settings

- [ ] `repository-settings.png`
      Settings → Repositories: largest artifact, timeouts, retries, outbound proxy and a connection test

## Storage

- [ ] `storage-settings.png`
      Settings → Storage: the storage in use with its status and Test connection, then the backend cards, location, credentials and upload limits

## Backups

- [ ] `backups-list.png`
      Settings → Backups: the summary of target, encryption and latest test restore over the list of backups with status, size, Keep, expiry and actions
- [ ] `backups-restore-dialog.png`
      The Restore dialog: the last pre-checks, what happens, and the installation name and password that confirm it
- [ ] `backups-maintenance.png`
      The maintenance screen every server shows while a restore runs, with the current step
- [ ] `backups-encryption.png`
      The Encryption section: Encrypt new backups, public keys or passphrase, and Generate a key pair
- [ ] `backups-add-upload.png`
      The Add a backup dialog, Upload tab: choose a .dxbak file and, optionally, its expected SHA-256
- [ ] `backups-add-import.png`
      The Add a backup dialog, Import folder tab: files with their version, date and state, and Check
- [ ] `setup-restore-step.png`
      The setup wizard's last step with Restore from a backup: the chosen backup's summary, key field and consent box
- [ ] `backups-target.png`
      The Backup target section: a separate S3 location with Test and Save, and the warning shown while the installation's storage is used
- [ ] `backups-test-restore.png`
      A backup row with its test restore result: passed, tables and rows compared, duration

## Integrity

- [ ] `integrity.png`
      Settings → Integrity: status, settings and recent checks

## Quarantine

- [ ] `quarantine.png`
      Settings → Quarantine: versions held back in every space, and the installation's rules
- [ ] `quarantine-block.png`
      Delete and block: choosing where the block applies, every version, and the reason
- [ ] `repository-quarantine.png`
      A repository's Quarantine tab: its quarantined versions and its own rules

## Block list

- [ ] `blocklist-rules.png`
      Settings → Block list: the installation's rules

## Vibe artifacts

- [ ] `vibe-settings.png`
      Settings → Repositories → Vibe artifacts: the switch, the checks on every push and the package list
- [ ] `vibe-settings-refusals-off.png`
      Checks on every push with secrets no longer refusing a push, and the warning the page shows
- [ ] `vibe-browser.png`
      The Vibe browser: search, filters and the Projects view, newest check-in first
- [ ] `vibe-browser-timeline.png`
      The Timeline view: check-ins grouped by day, milestones marked
- [ ] `vibe-browser-screenshots.png`
      The Screenshots view: every screenshot with its caption, project and check-in
- [ ] `vibe-browser-phone.png`
      The Vibe browser on a phone
- [ ] `vibe-project.png`
      A project's page: the latest check-in, how to run it, milestones and every check-in
- [ ] `vibe-checkin.png`
      A check-in's page: screenshots, details, how to run it, and the actions to pick it up
- [ ] `vibe-checkin-gaps.png`
      A check-in's What's unfinished tab: its known gaps file
- [ ] `browse-vibe-notice.png`
      Browse with the line that opens the Vibe browser
- [ ] `vibe-repository-create.png`
      A new repository in a space, with the Vibe artifacts format: only Hosted is offered
- [ ] `vibe-repository-usage.png`
      A vibe artifacts repository's page: Use this repository → Publish lists the three push requests
- [ ] `vibe-checkin-keep-working.png`
      A check-in's page: what must keep working and the environment it needs, with the outside service marked as not in the files
- [ ] `vibe-project-last-passing.png`
      A project's page after a check-in whose tests failed: the last passing check-in, with the rollback prompt
- [ ] `vibe-milestone-dialog.png`
      Naming a check-in's milestone from its page
- [ ] `vibe-checkin-findings.png`
      A check-in's Findings tab: what the check found, worst first, with the file and line, and one finding from the AI tool

## SBOMs

- [ ] `browse-components.png`
      Browse → Components: find every SBOM that lists a component
- [ ] `sbom-applications.png`
      A space's SBOMs tab: registered applications
- [ ] `sbom-version.png`
      An application version: its SBOM with completeness, components, vulnerabilities and export
- [ ] `vulnerability-data.png`
      Settings → Vulnerability data: the OSV service, how often components are checked again, and a test

## Users &amp; Directories

- [ ] `directories-list.png`
      Settings → Directories: where accounts come from, in order
- [ ] `users-list.png`
      Settings → Users: everyone who can sign in, their directory, role, status and last sign-in
- [ ] `users-user.png`
      A user's page: profile, sign-in and security, and groups
- [ ] `groups-group.png`
      A group: its directories and members

## Single Sign-On

- [ ] `sso-new.png`
      Add an identity provider: OpenID Connect and SAML 2.0 presets
- [ ] `sso-provider.png`
      An OpenID Connect provider: redirect URI, sign-in button, directory, connection and accounts
- [ ] `security-signin.png`
      Settings → Security → Sign-in: require single sign-on, with a preview of the sign-in page

## OAuth Applications

- [ ] `oauth-applications.png`
      Settings → Applications: registered applications and the addresses they use
- [ ] `applications-add-choice.png`
      Add application: a custom application, or another Depotex instance
- [ ] `applications-link-wizard.png`
      Link a Depotex instance: the other installation as it describes itself, the directions and what the link acts as
- [ ] `applications-link-request.png`
      The other installation's Link request page: the application it creates for the installation that asked
- [ ] `applications-linked-instances.png`
      Linked instances: an active link both ways, as a service account and as each person
- [ ] `service-accounts.png`
      Settings → Service accounts

## Branding &amp; Banners

- [ ] `branding-appearance.png`
      Settings → Appearance: application name and, per theme, brand color, logo and browser icon, with a preview
- [ ] `banners-list.png`
      Settings → Banners: each banner's status, message, audience and schedule
- [ ] `banner-bar.png`
      A warning banner at the top of the page, with a link and a close button

## Logging &amp; Audit

- [ ] `logging-levels.png`
      Settings → Logging & profiling → Log levels: one level for everything and a level per part
- [ ] `logging-audit.png`
      The audit log: filters, and who did what, when and from where

## System Check

- [ ] `system-check.png`
      Settings → System check: what needs attention and every check's result

## Email

- [ ] `email-settings.png`
      Settings → Application → Email: delivery status, provider, server and security, with the test email and recipient preview beside them
- [ ] `email-ses-api.png`
      Settings → Application → Email: Amazon SES signing in with AWS credentials, with a region and a role to assume

## Scheduled Jobs

- [ ] `scheduler-jobs.png`
      Settings → Advanced → Scheduled jobs

## Alerts

- [ ] `alerts-bell.png`
      The bell's dropdown: unread alerts, newest first
- [ ] `alerts-page.png`
      Notifications: filters by state, severity and category, and every alert with its actions

## Policies

- [ ] `policies-list.png`
      Settings → Policies: each policy's event, effect, mode, priority and decisions in the last 7 days
- [ ] `policies-editor.png`
      A policy made from a template: its rule, effect, message and priority

## Automation

- [ ] `automation-rules.png`
      Settings → Automation: the rules with their on/off switch, event and condition, steps and last run
- [ ] `automation-rule.png`
      A rule's settings: When, Only if and Then, with Try it beside them
- [ ] `automation-webhook-headers.png`
      A webhook step with two extra headers; values are hidden as you type
- [ ] `automation-email-step.png`
      An email step with two addresses, a subject and a message using event fields

## Plugins

- [ ] `plugins-list.png`
      Settings → Plugins: installed plugins, their version and status

## Rate Limits &amp; Quotas

- [ ] `rate-limits.png`
      Settings → Security → Rate limits: requests per period for each kind of caller

## Repositories

- [ ] `repositories-list.png`
      Repositories: every repository, grouped by space, for administrators

## Licensing

- [ ] `licensing.png`
      Settings → Application → Licensing: the license, its features and IDs, and the update section

## API Tokens

- [ ] `api-tokens.png`
      Profile → API tokens: your tokens and your rate limits
