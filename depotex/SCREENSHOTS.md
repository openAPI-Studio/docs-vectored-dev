# Depotex docs — screenshots needed

134 screenshots. Save each one into `depotex/assets/` using the
exact filename below. The docs pick them up automatically on the next build —
until then each slot renders a dashed placeholder naming the file it wants.

Guidance: capture the app at a comfortable browser width (about 1440px), use
the light theme unless the shot is specifically about dark mode, and use
realistic but fictional names and figures rather than real people's data.

## Getting Started

- [ ] `setup-wizard.png`
      The setup wizard's first step: the installation ID to request a license with, and the license
- [ ] `settings-general-addresses.png`
      Settings → General: the Depotex address, other addresses clients use, and the package links switch

## Single Node &amp; Cluster

- [ ] `clustering-redis-degraded.png`
      Settings → Clustering while Redis can't be reached: the notice above the node table

## Dashboard

- [ ] `dashboard-overview.png`
      Dashboard: what needs attention, the installation's figures, spaces by size and the system's health

## Search

- [ ] `search-palette.png`
      Search: spaces, repositories, artifacts, people and groups matching what was typed
- [ ] `search-results.png`
      The Search page: every kind of result for "orion", with a tab per kind
- [ ] `search-settings.png`
      Search: settings matching "session", each with its page and tab

## Your profile

- [ ] `profile-overview.png`
      Profile settings → Profile: the sections on the left, your avatar and account details
- [ ] `profile-preferences.png`
      Profile settings → Preferences: the three themes and the language
- [ ] `profile-security.png`
      Profile settings → Security: change your password, download your data
- [ ] `profile-sessions.png`
      Profile settings → Active sessions: this device, other sessions, and the confirmation before signing one out
- [ ] `api-tokens.png`
      Profile → API tokens: your tokens and your rate limits
- [ ] `profile-connected-apps.png`
      Profile settings → Connected apps: two applications and the linked installations
- [ ] `profile-connect-ai-agent.png`
      Profile settings → Connect an AI agent: the server address and the AI apps, one open to its instructions

## Spaces

- [ ] `spaces-list.png`
      Spaces as tiles: who can see each space, your role, its formats with how many repositories use each, and its last change, quarantined versions and storage
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
- [ ] `repository-settings-proxy-checksums.png`
      A proxy repository's Checksums set to Use the Security setting, with what that means at the moment: Strict
- [ ] `repository-settings-tab.png`
      A repository's Settings tab: the Repository and Artifacts cards, with switches, choices and the largest artifact in MB
- [ ] `repository-access-tab.png`
      A repository's Access tab: repository roles and path access, each with a row to add someone
- [ ] `spaces-create-quota.png`
      New space: the storage quota section, prefilled with the installation default of 50 GB, with No limit and the warning threshold
- [ ] `spaces-members.png`
      A space's Members tab: add people, groups and service accounts, and change their role

## Repository groups

- [ ] `repository-group.png`
      A group repository: its members in the order they're asked, and the space's universal URL

## APT

- [ ] `repository-signing-key-next.png`
      The Signing key card during an overlap: the current key, the next key and its date, Cancel switch and Switch now
- [ ] `repository-signing-key-rotate.png`
      Generate a new signing key: the overlap in days before it signs
- [ ] `apt-release-validity.png`
      An APT repository's settings with its Release valid for 7 days
- [ ] `apt-upstream-keys.png`
      An APT proxy's Upstream keys: the keys its upstream must sign its Release files with
- [ ] `repository-distribution.png`
      An APT repository's settings with its distribution release set to debian-12

## YUM

- [ ] `yum-proxy-signatures.png`
      A YUM proxy's settings: the upstream's trusted key, with signed packages and signed repodata required

## Terraform

- [ ] `terraform-login.png`
      The page terraform login opens: approve or deny the token for terraform on this computer

## Conda

- [ ] `conda-usage.png`
      Use this repository on a hosted conda channel: the channel for conda, micromamba and pixi, the credentials each reads, and the install and upload commands
- [ ] `conda-web-upload.png`
      Conda packages uploaded from the web: each file stored in the platform folder its info/index.json names
- [ ] `conda-yank.png`
      Yanking one build of a conda version: the broken linux-64 build ticked, with a reason
- [ ] `conda-settings.png`
      A conda repository's Conda card: Serve sharded repodata, with what micromamba and conda do after a change
- [ ] `conda-version-builds.png`
      A conda version's page: its builds per platform with size and install-time scripts, and Yank in the version's menu

## Browse

- [ ] `browse-search.png`
      Browse: search every repository you can see, filter by space, format and type
- [ ] `browse-tree.png`
      The tree of a repository, with its address and setup instructions
- [ ] `browse-version.png`
      A version: install command, overview, files, dependencies and security, with downloads and recent activity
- [ ] `browse-version-file-picker.png`
      A version with several files: the File picker under the Install bar, with the download and checksums following the file picked

## Upstreams

- [ ] `upstreams-list.png`
      Upstreams: each registry's format, address, the spaces that use it and its health
- [ ] `upstreams-hosts.png`
      An upstream whose file host is paused while its own address keeps answering

## Repository settings

- [ ] `repository-settings.png`
      Settings → Repositories: largest artifact, timeouts, retries, outbound proxy and a connection test
- [ ] `repository-settings-default-quota.png`
      Settings → Repositories → Artifacts: the default storage quota for new spaces, 50 GB, warn at 80%

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
      Settings → Integrity: status, broken files, recent checks and settings

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
- [ ] `vibe-skill-download.png`
      Profile menu → Connect an AI agent → Vibepack skill: the download button, the install and use steps, and the commands for saving without an agent
- [ ] `vibe-get-api-token.gif`
      Creating an API token for the vibepack skill: your picture → API Tokens → New token, the permissions to tick, and saving it with vibepack.py login

## SBOMs

- [ ] `sbom-unreadable.png`
      A version's Security tab with an SBOM marked Unreadable and the reason under it
- [ ] `sbom-security-tab.png`
      A version's Security tab beside the version's side panel: the summary with vulnerabilities, coverage and re-check, and the vulnerabilities as cards
- [ ] `sbom-finding-details.png`
      A vulnerability card opened: score and severity, the weakness by name, the affected component with its fix and range, what an attacker needs and can affect, the description and the references
- [ ] `sbom-coverage.png`
      The Coverage card of a version's Security tab, opened: the score, the three parts with their points and why each scored what it did
- [ ] `sbom-fix-checklist.png`
      An SBOM's Fix-it checklist: a step per affected component with the version that fixes it and the command, one ticked, and the check-again step
- [ ] `vulnerability-data-rescan.png`
      Settings → Vulnerability data: when a re-check breaks a policy, alert only or quarantine after a grace period
- [ ] `browse-components.png`
      Browse → Components: find every SBOM that lists a component
- [ ] `advisory-page.png`
      An advisory's page: the weakness, what an attacker needs and can affect, its references, the affected versions of each release line with the one in use marked, and what it affects
- [ ] `sbom-applications.png`
      A space's SBOMs tab: registered applications
- [ ] `sbom-version.png`
      An application version: its SBOM with completeness, components, vulnerabilities and export
- [ ] `vulnerability-data-status.png`
      Settings → Vulnerability data: the status block with its counts, Re-scan now and Re-inspect every version
- [ ] `security-reinspect.png`
      A version's Security tab: Re-check vulnerabilities, Re-inspect SBOMs and when it was last inspected
- [ ] `vulnerability-data.png`
      Settings → Vulnerability data: turning checks on and where components are checked: the OSV API, OSV's data files or uploaded files
- [ ] `vulnerability-data-scanners.png`
      Settings → Vulnerability data: the scanner plugins, where each may send data, and when each was last asked
- [ ] `vulnerability-data-distributions.png`
      Settings → Vulnerability data: the Amazon Linux, Fedora and Oracle Linux releases read, and the repository mirror
- [ ] `vulnerability-data-offline.png`
      Settings → Vulnerability data: downloading OSV's data files, each ecosystem's state, and uploading OSV data

## Users &amp; Directories

- [ ] `directories-list.png`
      Settings → Directories: where accounts come from, in order
- [ ] `users-list.png`
      Settings → Users: everyone who can sign in, their directory, role, status and last sign-in
- [ ] `users-user.png`
      A user's page: profile, sign-in and security, and groups
- [ ] `groups-group.png`
      A group: its directories and members
- [ ] `security-proxy-checksums.png`
      Settings → Security → Proxy checksums: the switch, the formats whose new proxies start at it, and how it differs from a repository's own setting

## Single Sign-On

- [ ] `sso-new.png`
      Add an identity provider: OpenID Connect and SAML 2.0 presets
- [ ] `sso-provider.png`
      An OpenID Connect provider: redirect URI, sign-in button, directory, connection and accounts
- [ ] `security-signin.png`
      Settings → Security → Sign-in: require single sign-on, with a preview of the sign-in page

## OAuth Applications

- [ ] `oauth-applications.png`
      Settings → Applications: the list of applications and the selected one beside it
- [ ] `service-accounts.png`
      Settings → Service accounts

## Branding &amp; Banners

- [ ] `branding-appearance.png`
      Settings → Appearance: application name and, per theme, brand color, logo and browser icon, with a preview
- [ ] `banners-list.png`
      Settings → Banners: each banner's status, message, audience and schedule
- [ ] `banner-bar.png`
      A warning banner at the top of the page: its title, its message with a link, and a close button

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
- [ ] `scheduler-edit-schedule.png`
      Editing a job's schedule, with the next run in the viewer's time

## Alerts

- [ ] `alerts-bell.png`
      The bell's dropdown: unread alerts, newest first
- [ ] `alerts-page.png`
      Notifications: filters by state, severity and category, and every alert with its actions
- [ ] `profile-notifications.png`
      Profile settings → Notifications: opt-out, muted and forced categories, and the save bar

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
      Settings → Plugins: plugins that need attention, the list by status, the upload area and the side column
- [ ] `plugins-mcp-ai-tools.png`
      A plugin's AI tools tab: tools by permission with switches, the server address and the mode
- [ ] `plugins-connect-ai-app-form.png`
      Connect an AI app: the Add an application form filled in for Claude Code and the plugin
- [ ] `plugins-connect-ai-agent.png`
      Profile menu → Connect an AI agent: the Connect tab with the server address and the Claude Code app's client ID and command

## Rate Limits &amp; Quotas

- [ ] `rate-limits.png`
      Settings → Security → Rate limits: requests per period for each kind of caller

## Repositories

- [ ] `repositories-list.png`
      Repositories: every repository, grouped by space, for administrators
- [ ] `settings-deleted-repositories.png`
      Settings → Deleted repositories: two deleted repositories, each with Restore and Delete permanently

## Licensing

- [ ] `licensing.png`
      Settings → Application → Licensing: the license, its features and IDs, and the update section

## API Tokens

- [ ] `api-tokens.png`
      Profile → API tokens: your tokens and your rate limits
- [ ] `profile-api-token-create.png`
      Profile → API tokens → New token: expiration, templates and permissions
