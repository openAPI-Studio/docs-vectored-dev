"""Quarantine page. Keep in step with
apps/depotex/backend/internal/quarantine and internal/artifactstore/quarantine.go
in the depotex repo."""
from engine import H, P, UL, TABLE, NOTE, STEPS, SHOT

QUARANTINE = [
    ("quarantine", dict(
        label="Quarantine", title="Quarantine", icon="shield",
        desc="Hold back new or suspect versions until someone releases them: rules for uploads and proxied files, by hand, and age rules against freshly published packages",
        keywords=["quarantine", "release", "hold", "review", "firewall", "malicious", "new packages", "age", "dependency age", "block", "approve"],
        blocks=[
            H("Overview"),
            P("A quarantined version stays listed in its repository but can't be downloaded until someone releases it. Builds that need it fail with a clear **quarantined** error and the reason, instead of quietly using something else. Versions are quarantined by **rules**, as they are published or fetched by a proxy repository, or **by hand**. Needs an **Enterprise** license."),
            UL([
                "Downloads, `HEAD` requests and checksum files of a quarantined version answer **403** with the reason `quarantined` and the rule's reason.",
                "Another Depotex linked to the repository ([Depotex link](upstreams.html#depotex-link)) is refused too, and removes copies it cached.",
                "Quarantined versions stay in the version lists clients resolve from (such as `maven-metadata.xml` and npm package documents). Turn on **Hide quarantined versions** in a repository's **Settings** to leave them out, so builds pick another version. `npm audit` reports quarantined versions as high advisories.",
                "A released version is never quarantined again by a rule; it can still be quarantined by hand.",
                "Depotex also quarantines versions carrying unsafe content (oversized or hostile SBOMs, attestations or metadata) by itself, on every license tier: see [Browse](browse.html#unsafe-content-is-quarantined). They show as **Refused content (automatic)**.",
                "A [policy on SBOMs](sbom.html#policies-on-sboms) that denies what a version's SBOM lists (severe vulnerabilities, forbidden licenses) quarantines it too; those show as **Refused by policy** with the policy's message.",
            ]),

            H("Quarantine rules"),
            P("Rules apply to new versions when their first file is published or fetched. There are rules at two levels:"),
            UL([
                "**Space rules**, in the space's **Settings** under **Quarantine rules** (maintainers and owners), with its other policies. A space rule can be narrowed to one repository.",
                "**Installation rules**, under **Settings → Repositories → Quarantine** (super admins), for every repository of every space.",
            ]),
            TABLE(["Setting", "Meaning"], [
                ["**Applies to**", "Uploads and proxied files, uploads only (hosted repositories), or proxied files only."],
                ["**Formats**", "Which formats; none ticked means all."],
                ["**Namespace**, **Name**, **Version**", "Patterns the version must match; `*` matches anything, `?` one character, case doesn't matter; empty matches everything. A Maven name is `groupId:artifactId` (so `com.acme:*`), an npm name may have its `@scope`, and a PyPI name matches however it is written (`Acme_Internal*` matches `acme-internal-tools`). For example, version `*-rc*` holds back release candidates."],
                ["**Published less than (days)**", "Only versions published less than this many days ago: proxied files by the upstream's date, uploads from when they're uploaded. Their quarantine ends by itself when they are old enough. This holds back freshly published packages, the way malicious ones usually arrive."],
                ["**Reason**", "Shown to anyone whose download is refused, and in the quarantine list."],
            ]),
            P("Every setting you fill in must match. When several rules match, one without an age limit wins; otherwise the one ending last."),
            NOTE("When a proxied file's upstream doesn't say when it was published, an age rule treats it as just published."),

            H("Quarantined versions"),
            P("The space's **Quarantine** tab lists its quarantined versions, newest first, and **Settings → Repositories → Quarantine** lists every space's. Show the versions held, released or all, and search by name, version or repository (on the installation-wide list, also by space). Select several to release them together."),
            SHOT("quarantine.png", "Settings → Quarantine: versions held back in every space, and the installation's rules"),
            STEPS([
                "Release|Tick the versions, or choose **Release** on one, add a note if you like (it goes in the audit log), and confirm. They can be downloaded again at once.",
                "Quarantine by hand|In a repository's **Versions** tab, choose **Quarantine** next to a version and give a reason. **Release** there does the opposite.",
            ]),
            P("AI agents can quarantine and release versions too, through [write tools](plugins.html#write-tools), once an administrator allows it. They act as the person using them, need the same rights in the space, and are recorded in the audit log with `via: mcp:<plugin>/<application>`."),
            P("Versions held by an age rule show until when; once that time passes they're downloadable again and are listed as ended."),

            H("Without Enterprise"),
            P("Rules don't apply and nothing new can be quarantined, but versions already quarantined stay quarantined, and you can still list and release them and delete rules."),

            H("Events"),
            P("`artifact.quarantine` is raised when a version is quarantined (by hand: before and after, so policies can refuse it; by a rule: after). `artifact.release` is raised when one is released (by hand: before, refused if a policy or plugin fails, and after; when an age rule ends: after). `quarantine.rule.create`, `.update` and `.delete` wrap rule changes. Use [automation](automation.html) to notify someone when versions are quarantined. Everything is recorded in the audit log. See [Events](events.html)."),

            H("Permissions"),
            TABLE(["Permission", "Who", "Allows"], [
                ["`spaces:quarantine:manage`", "Space maintainers and owners", "The space's quarantine list, quarantining and releasing its versions, and its rules"],
                ["`artifacts:quarantine:manage`", "Super admins only", "Settings → Repositories → Quarantine: every space's quarantined versions and the installation rules"],
            ]),
        ],
    )),
]
