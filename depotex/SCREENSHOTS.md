# Depotex docs — screenshots needed

199 screenshots. Save each one into `depotex/assets/` using the
exact filename below. The docs pick them up automatically on the next build —
until then each slot renders a dashed placeholder naming the file it wants.

Guidance: capture the app at a comfortable browser width (about 1440px), use
the light theme unless the shot is specifically about dark mode, and use
realistic but fictional names and figures rather than real people's data.

## Getting started

- [ ] `quickstart-sign-in.png`
      The sign-in page
- [ ] `quickstart-find-repository.gif`
      From the dashboard to a space, its repositories, and a repository's setup instructions
- [ ] `quickstart-repository-setup.png`
      An npm repository's setup: the address, then the commands to point npm, pnpm, Yarn and Bun at it

## Install Depotex

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
- [ ] `repository-settings-proxy-cache.png`
      A proxy repository's Proxy cache card: Re-check now, and the remembered “not found” paths with when each is asked for again, a filter and Forget all
- [ ] `repository-settings-tab.png`
      A repository's Settings tab: the Repository and Artifacts cards, with switches, choices and the largest artifact in MB
- [ ] `repository-settings-metadata.png`
      A Helm repository's Metadata card after a check: two chart archives missing from index.yaml, with Check and Repair
- [ ] `repository-access-tab.png`
      A repository's Access tab: repository roles and path access, each with a row to add someone
- [ ] `spaces-cleanup-revision-rules.png`
      A cleanup policy's Revisions (Conan) settings and its preview of the revisions a run would delete
- [ ] `spaces-trash.png`
      A space's Trash tab: trashed Maven versions with the cleanup policy that removed them, their size, when, and Restore
- [ ] `spaces-cleanup-undo-run.png`
      A cleanup policy's row with its last run and the button that restores what that run removed
- [ ] `spaces-tags.png`
      A space's Tags tab: two tags with their description and attributes, one opened to the four Maven versions it carries
- [ ] `spaces-tags-promote.png`
      The Promote dialog for a tag: source repository, target repository in another space, Move and Run in the background
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

## RubyGems (Ruby)

- [ ] `rubygems-usage-hosted.png`
      A hosted RubyGems repository's Usage tab: the Gemfile source block, bundle install and gem install with the repository's address
- [ ] `rubygems-yank.png`
      Yanking one platform's file of a version: the confirmation on the version's Overview
- [ ] `rubygems-settings.png`
      A RubyGems repository's settings: the owners-only and new-names switches, and the reserved gem names with their owners
- [ ] `rubygems-usage-proxy.png`
      A RubyGems proxy repository's Usage tab: the Gemfile source, the Bundler mirror and gem install
- [ ] `rubygems-proxy-settings.png`
      A RubyGems proxy's settings: keep versions yanked upstream, cache every platform's file, the upstream index, and the versions yanked upstream
- [ ] `rubygems-usage.png`
      A RubyGems group's Usage tab: the group as the Gemfile source, the link to use it as Bundler's mirror of rubygems.org instead, and gem install; gem push through the group is on its Publish tab
- [ ] `rubygems-import.png`
      A hosted RubyGems repository's Import gems panel: the date source, what to do without a date, and a result per gem file
- [ ] `rubygems-version-platforms.png`
      A gem version's Overview: the gemspec, the owners and the platforms table with each platform's file
- [ ] `rubygems-attestations.png`
      A gem version's Overview with verified attestations: the Attestations row with the signer, and each platform's result

## Conda

- [ ] `conda-usage.png`
      Use this repository on a hosted conda channel: the channel for conda, micromamba and pixi, the credentials each reads, and the install and upload commands
- [ ] `conda-web-upload.png`
      Conda packages uploaded from the web: each file stored in the platform folder its info/index.json names
- [ ] `conda-yank.png`
      Yanking one build of a conda version: the broken linux-64 build ticked, with a reason
- [ ] `conda-labels-dialog.png`
      Labels of a conda version: two builds ticked, the label rc added and dev removed
- [ ] `conda-labels.png`
      A hosted conda channel's Labels card: main, dev and rc with their file counts and channel addresses
- [ ] `conda-patches.png`
      A hosted conda channel's Repodata patches card: noarch and linux-64 patched, with their entry counts and who changed them
- [ ] `conda-settings.png`
      A conda repository's Conda card: Serve sharded repodata, with what micromamba and conda do after a change
- [ ] `conda-group-settings.png`
      A conda group's Conda card: Serve sharded repodata, and Hosted packages hide upstream packages of the same name
- [ ] `conda-version-builds.png`
      A conda version's page: its builds per platform with size and install-time scripts, and Yank in the version's menu
- [ ] `sbom-conda-payload.png`
      A conda-forge package's Security tab: vulnerabilities of the Python package inside it, found by the Depotex package scan, with its coverage

## Conan (C/C++)

- [ ] `conan-usage.png`
      Use this repository on the Conan group a space uses by default: its universal address, the remote name, then the commands to add the remote first, turn ConanCenter off, sign in with an API token and install
- [ ] `conan-proxy-usage.png`
      Use this repository on a proxy of ConanCenter: add it as the first remote, turn ConanCenter off, sign in with an API token and install
- [ ] `conan-group-settings.png`
      A Conan group's Conan card: Hosted recipes hide upstream recipes of the same name, on (the default)
- [ ] `conan-integrity.png`
      A Conan version's page: its recipe revision Verified, the recipe's description, licence, homepage, topics and sources, and two binaries, each Verified with ID matches, its size and its number of package revisions
- [ ] `conan-version-revisions.png`
      A Conan version's page: the install command and its recipe revisions, the latest marked, with who published each, integrity, size and number of binaries
- [ ] `conan-version-packages.png`
      The binaries of a recipe revision: package ID, settings, integrity with ID matches, size, and the package revision of each with how many it has
- [ ] `conan-security-git-match.png`
      A Conan version's Security tab: zlib 1.2.11 with three advisories found through its upstream repository, each with fixing version not known, and the note that three advisories couldn't be decided, most because they mix several projects' versions

## Browse

- [ ] `browse-search.png`
      Browse: search every repository you can see, filter by space, format and type
- [ ] `browse-tree.png`
      The tree of a repository, with its address and setup instructions
- [ ] `browse-version-tags.png`
      A version's heading: name, version menu, status and its two tags, with Download
- [ ] `browse-version.png`
      A version: install command, overview, files, dependencies and security, with downloads and recent activity
- [ ] `browse-version-file-picker.png`
      A version with several files: the File picker under the Install bar, with the download and checksums following the file picked

## Upstreams

- [ ] `upstreams-list.png`
      Upstreams: each registry's format, address, the spaces that use it and its health
- [ ] `upstreams-test-not-conan-2.png`
      Test connection on a Conan upstream whose address is a Conan 1 server: the failure, not a Conan 2 server, next to the form
- [ ] `upstreams-hosts.png`
      An upstream whose file host is paused while its own address keeps answering

## Repository settings

- [ ] `repository-settings.png`
      Settings → Repositories: largest artifact, timeouts, retries, outbound proxy and a connection test
- [ ] `repository-settings-default-quota.png`
      Settings → Repositories → Artifacts: the default storage quota for new spaces, 50 GB, warn at 80%
- [ ] `settings-repositories-metadata.png`
      The Metadata of every repository card: a format choice, Check all and Repair all, and the latest results per repository

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

- [ ] `quarantine-rule-vulnerabilities.png`
      A quarantine rule holding versions with known vulnerabilities: lowest severity, only with a fix, always holding known-malicious packages, and what happens to versions that can't be checked
- [ ] `quarantine-vulnerable-versions.png`
      Quarantined versions with their advisories and the fixed version, and one held until it can be checked
- [ ] `quarantine.png`
      Settings → Quarantine: versions held back in every space, and the installation's rules
- [ ] `quarantine-release-malicious.png`
      Releasing a held version with a known-malicious record: the dialog names the record it confirms
- [ ] `quarantine-refused-malicious.png`
      The released list with a version refused at download as a known-malicious package, and its Release button
- [ ] `quarantine-block.png`
      Delete and block: choosing where the block applies, every version, and the reason
- [ ] `repository-quarantine.png`
      A repository's Quarantine tab: its quarantined versions and its own rules

## Block list

- [ ] `blocklist-rules.png`
      Settings → Block list: the installation's rules, each with its switch, what it blocks and its formats
- [ ] `blocklist-rule-range.png`
      Adding a block-list rule for RubyGems with a RubyGems requirement as its version range

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
- [ ] `sbom-finding-malicious.png`
      A finding marked Known malicious on a version's Security tab
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
- [ ] `sbom-not-covered.png`
      A version's Security tab: components no vulnerability data covers shown as not covered
- [ ] `vulnerability-data.png`
      Settings → Vulnerability data: turning checks on and where components are checked: the OSV API, OSV's data files or uploaded files
- [ ] `vuln-settings-malicious.png`
      Settings → Vulnerability data: the Malicious packages setting
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
- [ ] `security-attestation-trust.png`
      Settings → Security → Attestation trust: the built-in public Sigstore root, an uploaded root and the attestations still to check

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
- [ ] `oauth-workload-identity-exchange.png`
      The Workload identity dialog's pipeline examples: with the client ID, and the token exchange without it
- [ ] `settings-applications-add.png`
      Settings → Applications → Add application: a custom application or another Depotex instance
- [ ] `settings-applications-link-instance.png`
      Link a Depotex instance: the other installation's address, looked up before you choose directions

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

## Alert Tuning

- [ ] `alert-tuning.png`
      Settings → Alert tuning: active mutes and each check's notification rule
- [ ] `alert-tuning-mute.png`
      Settings → Alert tuning: a new mute for the problems in an alert

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

- [ ] `policies-create.gif`
      Creating a policy: New policy, a template, its networks, Try it, then Create policy
- [ ] `policies-new.png`
      New policy: templates grouped by area, each with the effect it has
- [ ] `policies-try-it.png`
      Try it: a sample sign-in from outside the ranges matches, so the policy would block it
- [ ] `policies-created.png`
      The new policy in dry run, with its Settings, Decisions, Compliance, History and Exemptions tabs
- [ ] `policies-list.png`
      Settings → Policies: each policy's event, effect, mode, priority and decisions in the last 7 days
- [ ] `policies-editor.png`
      A policy made from a template: its rule, effect, message and priority

## Automation

- [ ] `automation-create.gif`
      Creating a rule: New rule, the event, a condition, an alert step, Try it, then Create rule
- [ ] `automation-new-rule.png`
      A new rule: When a repository is created, Only if it is a Docker repository, Then send an alert; Try it shows the condition matches
- [ ] `automation-alert.png`
      The alert the rule sent, in the notifications panel
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

## Settings reference

- [ ] `settings-general.png`
      Settings → General: the Depotex address, other addresses, and the help links

## How access fits together

- [ ] `groups-group.png`
      A group: the directories that sync into it, and each member with where they came from
- [ ] `repository-access-tab.png`
      A repository's Access tab: repository roles and path access

## Setup wizard

- [ ] `setup-wizard.gif`
      The setup wizard from the license to the first administrator
- [ ] `setup-wizard-license.png`
      Setup wizard, License: the installation ID to request a license with, and the license to upload or paste
- [ ] `setup-wizard-database.png`
      Setup wizard, Database: the connection, its checks, and what the database already holds
- [ ] `setup-wizard-storage.png`
      Setup wizard, File storage: the backend and its settings, checked before you go on
- [ ] `setup-wizard-cache.png`
      Setup wizard, Cache: an optional Redis URL
- [ ] `setup-wizard-admin.png`
      Setup wizard, Administrator: the first super admin, or restore from a backup

## Support

- [ ] `support-about-dialog.png`
      ? → About: the version, build and server, with Copy details for a support request
