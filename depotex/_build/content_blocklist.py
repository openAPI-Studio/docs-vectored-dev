"""Block list page. Keep in step with apps/depotex/backend/internal/blocklist
in the depotex repo."""
from engine import H, P, UL, TABLE, NOTE, SHOT

BLOCKLIST = [
    ("blocklist", dict(
        label="Block list", title="Block list", icon="shield",
        desc="Stop versions from being used anywhere: refused downloads and uploads, never fetched by proxies, left out of metadata",
        keywords=["block list", "blocklist", "deny", "ban", "vulnerable", "cve", "log4shell", "version range", "gem requirement", "firewall", "blocked", "checksum", "quarantine"],
        blocks=[
            H("Overview"),
            P("Versions on the block list can't be used: downloads and uploads answer **403** with the reason `blocked` and the rule's reason, proxy repositories never fetch them, and they're left out of the version lists clients resolve from and of folder listings, so builds pick another version. People who browse a repository still see them, with a **Blocked** badge in the **Versions** tab. Rules apply at once to versions already stored, too. Needs an **Enterprise** license."),
            UL([
                "**Space rules** are in the space's **Settings** under **Block list** (maintainers and owners); a rule can be narrowed to one repository.",
                "**Installation rules** are under **Settings → Repositories → Block list** (super admins), for every repository of every space.",
                "**From quarantine**: blocking a quarantined version ([Block, or Delete and block](quarantine.html#block-or-delete-and-block)) adds a rule here, marked **From quarantine**, with where the version came from and whether it was deleted. Deleting such a rule unblocks the version: a version that was kept goes back to quarantine.",
            ]),
            H("Rules"),
            SHOT("blocklist-rules.png", "Settings → Block list: the installation's rules"),
            TABLE(["Setting", "Meaning"], [
                ["**Formats**", "Which formats; none ticked means all."],
                ["**Namespace**, **Name**", "Patterns; `*` matches anything, `?` one character, case doesn't matter. Fill in at least one. A Maven name is `groupId:artifactId`, an npm name may have its `@scope`, a Go name is the module path, a Helm name the chart, a NuGet name the package ID, and a raw file's name is its path (so `tools/*.exe`)."],
                ["**Version pattern**", "A pattern such as `*-SNAPSHOT`; empty matches every version."],
                ["**Version range**", "Maven style: `[1.0,2.0)` is 1.0 up to but not including 2.0, `(,1.2]` up to 1.2, `[2.0,)` from 2.0, `[1.4]` exactly 1.4; join several with commas. For example `org.apache.logging.log4j:log4j-core` with `[2.0,2.15.0)` blocks the Log4Shell versions. Python-style specifiers work too: `>=2.0,<2.3`, `==1.4.*`, `~=3.1`. Both styles work for every format. A rule for RubyGems only can also use RubyGems requirements, written as in a `Gemfile`: `~> 1.2` (1.2 up to but not including 2.0), `>= 1.0, < 2`, `>= 1.0, < 2, != 1.5` (the same, except 1.5), or `1.2` for exactly that version. On its own, `!= 1.3` blocks every version except 1.3. For gems, a range such as `>=2.0,<2.3` is read as a RubyGems requirement too, so it covers `2.3.a`, which comes before `2.3`. A range that only some of the rule's formats can read is refused, and the message names the formats that can: tick only those, or use a Maven-style range. The range is kept as you type it, except that spaces are taken out of Maven-style ranges and from inside a version or an operator (`>= 1 .0` is saved as `>=1.0`). Versions compare the way their format orders them: for PyPI as pip does (`1.0.post1` after `1.0`, `1.1.dev0` before `1.1`); for npm, Go and Helm by semver (Go and Helm with or without the leading `v`); for NuGet as NuGet does (up to four numbers, `1.0` is `1.0.0`); for RubyGems as RubyGems does (`1.0.a` before `1.0`, `1.10` after `1.9`); for conda as conda does (`1.1dev1`, `1.1_`, `1.1a1`, `1.1`, `1.1post1` in that order); for Conan as Conan does (`1.0` is `1.0.0`, `1.0-rc1` before `1.0`, `1.0+b2` after it). Apart from the requirements RubyGems reads, Python-style specifiers compare as pip does whatever the format, and many conda versions aren't Python versions (`1.1.1w`, `9e`, `1.1_`) and never match one, so give conda versions as a Maven-style range. Conan's own range syntax (`[>=1.0 <2]`) isn't read here: give Conan versions as a Maven-style range too. PyPI names match however they are written (`Foo_Bar` is `foo-bar`), and NuGet IDs in any case."],
                ["**Reason**", "Shown to anyone whose download is refused."],
            ]),
            SHOT("blocklist-rule-range.png", "Adding a block-list rule for RubyGems with a RubyGems requirement as its version range"),
            P("**Try a version** in the space's Block list shows which rule, if any, would block a name and version in one of its repositories."),
            H("What is refused"),
            UL([
                "Downloads, `HEAD` requests and checksum files of the version's files.",
                "Uploads of the version, to any repository the rule covers, and storing a copy a proxy fetched.",
                "Rules made from quarantine also refuse their files' content under any other name or version: a file with the same SHA-256 can't be uploaded or cached (the error says `checksum`). Checksum files and files under 128 bytes aren't compared.",
                "Proxy repositories don't fetch a blocked version and don't serve a copy they cached before.",
                "Maven: blocked versions are left out of `maven-metadata.xml`, both what hosted repositories generate and what proxies pass on from their upstream (whose checksum files then match what is served). A blocked snapshot's own metadata is refused.",
                "npm: blocked versions are left out of package documents (dist-tags move to the newest version left), and `npm audit` reports them as critical advisories.",
                "Docker: blocked tags are left out of tag lists, and pulling them (or their digest) is refused.",
                "Raw: blocked files are left out of folder listings.",
                "RubyGems: blocked versions are left out of the `info/` files Bundler and `gem` resolve from and of the JSON API, both what hosted repositories generate and what proxies pass on, so Bundler picks another version; hosted repositories leave them out of the specs files too. A proxy's specs files are RubyGems.org's and still list them. A group leaves out what its members do; a version blocked after it was pushed leaves a group's list of gems within about a minute. See [Hidden versions](rubygems.html#hidden-versions).",
                "Another Depotex linked to the repository ([Depotex link](upstreams.html#depotex-link)) is refused them too, and removes copies it cached.",
            ]),
            NOTE("A change applies at once on the server you made it on, and to downloads on other servers of a cluster within a few seconds (`BLOCKLIST_REFRESH_INTERVAL`, 5s by default). Uploads and proxy caching check for changes every time."),
            H("Without Enterprise"),
            P("Rules can't be added or changed, but existing rules keep applying, and you can delete them."),
            H("Events"),
            P("`artifact.blocked` (after) is raised when a request is refused, at most once per version and server every 10 minutes (`BLOCKLIST_EVENT_INTERVAL`), so [automation](automation.html) can tell you a build is still asking for a blocked version. `blocklist.rule.create`, `.update` and `.delete` wrap rule changes (before and after; a failing policy or plugin refuses the change). Rule changes are recorded in the audit log. See [Events](events.html)."),
            H("Permissions"),
            TABLE(["Permission", "Who", "Allows"], [
                ["`spaces:blocklist:manage`", "Space maintainers and owners", "The space's block list and its dry run"],
                ["`artifacts:blocklist:manage`", "Super admins only", "Settings → Repositories → Block list: the installation rules"],
                ["`repo:quarantine`", "Repository admins", "Blocking the repository's quarantined versions in that repository, and deleting those rules"],
            ]),
        ],
    )),
]
