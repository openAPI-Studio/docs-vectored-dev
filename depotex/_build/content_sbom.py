"""SBOMs page. Keep in step with apps/depotex/backend/internal/sbom and
internal/inspect/sbom.go in the depotex repo."""
from engine import H, P, UL, TABLE, NOTE, CODE, SHOT

SBOM = [
    ("sbom", dict(
        label="SBOMs", title="SBOMs", icon="shield",
        desc="What your software is made of: the SBOMs stored with artifacts, read component by component, and applications whose SBOMs you upload from CI",
        keywords=["sbom", "software bill of materials", "cyclonedx", "spdx", "components", "purl", "application", "upload", "supply chain", "vex", "vulnerability", "osv", "cve", "ghsa", "cvss", "advisory", "vex", "not affected", "csaf", "false positive", "alert", "policy", "license", "quarantine", "ntia", "export", "share", "completeness", "ai bom", "ml-bom", "model card", "hugging face", "mcp", "ai agent"],
        blocks=[
            H("Overview"),
            P("A software bill of materials (SBOM) lists what a piece of software is built from. Depotex reads every SBOM it holds, component by component, into one store, so the same questions can be asked of everything: a library published to a Maven repository with its CycloneDX file, a container image with a buildx attestation, or a deployed service whose SBOM CI uploads after each release."),
            UL([
                "**SBOMs stored with artifacts** are read when the artifact is published or fetched: files by name (`-cyclonedx.json`, `.spdx.json`, `bom.xml`, …), in-toto SBOM attestations, Docker buildx attestations and OCI referrers. The version's **Signatures & SBOMs** tab shows them; the [API](#api) lists their components. Every license tier.",
                "**Applications** are software that isn't stored in a repository. Register one in a space, then upload an SBOM for each of its versions. **Enterprise**.",
                "Formats: **CycloneDX** (JSON and XML, 1.2 to 1.6) and **SPDX** (JSON and tag-value, 2.2 and 2.3). Every component's purl, name, version, type, supplier, licenses and hashes are kept, and the relationships between components.",
            ]),
            NOTE("An SBOM is read like any other artifact content: within size, depth and time limits, never fetching anything from the network. For an artifact, content over a limit quarantines the version (see [Browse](browse.html#unsafe-content-is-quarantined)); an uploaded application SBOM is simply refused with the reason."),

            H("In the browser"),
            UL([
                "A version's **Signatures & SBOMs** tab lists each SBOM with a **Components** section: the components it lists (name, version, ecosystem, type, supplier, licenses), searchable by name or package URL, and the **Vulnerabilities** among them, worst first, each with its severity and CVSS score, aliases, the components it affects and the version that fixes it, and links to the advisory.",
                "The version's header and side panel show how many known vulnerabilities it carries, by severity, or that it has none among the components checked.",
                "On **Browse**, the **Vulnerabilities** filter keeps artifacts whose newest version matches any advisory, or one of a given worst severity; rows show the worst severity as a badge.",
            ]),

            H("How complete is an SBOM?"),
            P("Every SBOM shows a **completeness** score against the NTIA minimum elements: how many of its components carry a supplier, a name, a version and a unique identifier (a package URL or a hash), and whether the document records dependency relationships, who made it and when. The chip lists what is missing. It measures the document, not the software: a complete SBOM of vulnerable software scores 100."),

            H("Exporting and sharing"),
            P("Besides the uploaded or stored file (**Download**), every SBOM exports from what Depotex read of it, in either format, so a CycloneDX upload can be handed on as SPDX and the other way round:"),
            UL([
                "**CycloneDX** 1.5 JSON, with the known vulnerabilities, their scores and the VEX statements merged in.",
                "**SPDX** 2.3 JSON, with package URLs, checksums, licenses and relationships (no vulnerabilities: SPDX 2.3 has no place for them).",
                "**Share link**: a link anyone can open until it expires (1 to 90 days, 30 by default), without an account, to hand an SBOM to a customer or an auditor. Making one needs `spaces:sbom:write`, raises `sbom.share.create` (a policy can forbid sharing or cap the days) and is in the audit log. A link can't be revoked before it expires.",
            ]),
            P("Exports and share links need **Pro**."),
            TABLE(["Request", "Returns"], [
                ["`GET …/sbom/{n}/export?format=cyclonedx` or `spdx`, `&vex=1` (a version); `GET …/documents/{n}/export?…` (an application)", "The export as a file"],
                ["`POST …/sbom/{n}/share`, `POST …/documents/{n}/share` `{format, vex, expiresDays}`", "A link: `url`, `expiresAt`"],
                ["`GET /api/sbom/shared/{token}`", "The export, for anyone, until the link expires"],
            ]),

            H("Watching for new vulnerabilities"),
            P("Advisories arrive after software ships. With vulnerability data on, every re-check that finds new advisories for the components of an SBOM raises `sbom.vulnerability.found` (one per SBOM, worst first) and sends an in-app alert to the space's owners and maintainers: which artifact or application version, how many new advisories, the worst one, and how many critical and high ones are open now. Automation can forward the event to chat, e-mail or a ticket."),

            H("Policies on SBOMs"),
            P("Every SBOM is evaluated by the event `sbom.document.evaluate` when it is read (an artifact version), when it is uploaded (an application), and again whenever new advisories match its components. The policy sees the licenses its components declare, the component counts (and whether some have no package URL or the document was cut), and what is known of its vulnerabilities at that moment, with VEX assessments applied: counts by severity, the worst, the advisory ids. A policy that denies:"),
            UL([
                "**quarantines the artifact version** (source **Refused by policy** in the quarantine list, with the policy's message as the reason). Release it as usual; it isn't quarantined again until something changes.",
                "**refuses an application SBOM upload** with the policy's message; nothing is kept.",
            ]),
            P("Ready-made templates under **Settings → Policies** (Pro):"),
            TABLE(["Template", "Does"], [
                ["**Refuse SBOMs with severe vulnerabilities**", "Pick the worst severities that aren't allowed (critical, high, …)."],
                ["**Refuse components under some licenses**", "List license identifiers (GPL-3.0-only, AGPL-3.0-only, …) no component may carry."],
                ["**Require complete SBOMs with package URLs**", "Refuse SBOMs with components that can't be checked (no package URL) or that were cut at the component limit."],
            ]),
            NOTE("Vulnerabilities are checked a few minutes after an SBOM arrives, so a severity policy mostly acts on the re-evaluation that follows the check, not at upload time. A denied artifact version is quarantined, never deleted."),

            H("Assessing a vulnerability (VEX)"),
            P("Not every reported vulnerability matters: the vulnerable code may not be reachable, the configuration never used, a mitigation in place. A **VEX statement** records that for one advisory in one SBOM, for the people who read it and for the exported document. Space developers and up (`spaces:sbom:write`) make them from **Assess** on a vulnerability, in a version's Signatures & SBOMs tab or an application's SBOM. Needs **Enterprise**."),
            TABLE(["State", "Meaning", "Counted?"], [
                ["**Under investigation**", "Someone is looking at it", "yes"],
                ["**Affected**", "It applies; a response says what happens next (update, workaround, won't fix…)", "yes"],
                ["**Not affected**", "It doesn't apply, with a justification: vulnerable code not present or not reachable, requires a configuration, dependency or environment not used, protected by the compiler, at runtime, at the perimeter or by a mitigating control", "no"],
                ["**Fixed**", "Already fixed in this software", "no"],
            ]),
            UL([
                "A vulnerability assessed **not affected** or **fixed** leaves the counts: the version's badge and side panel, the Browse filter and the application's report say what still applies, and show how many were assessed away.",
                "An uploaded CycloneDX document that carries its own analysis (`vulnerabilities[].analysis`) brings those statements along, marked as the document's own; a person's statement replaces them.",
                "**Export VEX** on the vulnerabilities panel downloads the statements as a **CycloneDX VEX** document (with the advisories' ratings and the affected components) or as **CSAF 2.0 VEX**, to hand to customers or auditors.",
                "Each statement names who made it and when; making, changing and removing one is in the audit log and raises `sbom.vex.update` / `sbom.vex.delete`, so a policy can require a justification or a detail.",
            ]),
            NOTE("A statement covers one SBOM. The same advisory in another version, or in an application's next release, is assessed again."),
            TABLE(["Request", "Returns"], [
                ["`PUT …/sbom/{n}/vex/{advisory}` (a version), `PUT …/documents/{n}/vex/{advisory}` (an application) `{state, justification, response, detail}`", "Makes or changes the statement"],
                ["`DELETE …/vex/{advisory}`", "Removes it"],
                ["`GET …/sbom/{n}/vex?format=cyclonedx` or `csaf`, `GET …/documents/{n}/vex?format=`", "The export as a file"],
            ]),

            H("Models and datasets (AI BOM)"),
            P("A [Hugging Face](huggingface.html) model or dataset gets an SBOM of its own, read from its model card: the repository itself as a machine-learning model (or data), its base models and the datasets it was trained on as components, with the card's license. It behaves like any SBOM here: components and completeness in the browser, licence policies, and **Components** search across everything, so \"which models were fine-tuned from Llama-3-8B?\" is one search. Models and datasets carry Hub package URLs (`pkg:huggingface/…`), which vulnerability databases don't cover: they are listed, not matched."),

            H("AI agents"),
            P("AI agents connected through the [MCP plugin](plugins.html#mcp-servers-for-ai-applications) read the same store, as the person who signed in: `get_sbom` lists a version's SBOMs and their components, `get_vulnerabilities` what is known about them with the assessments, `search_components` finds a component across every SBOM the person can see, `get_advisory` what a CVE affects. Pro features (search, advisories) and spaces the person can't open are refused to the agent as they would be in the browser."),

            H("Finding a component everywhere"),
            P("**Browse → Components** searches every SBOM you can see at once, stored with artifacts or uploaded for applications: type part of a name (`log4j`) or a package URL (`pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1`; without a version, every version of the package), and narrow to an ecosystem. Each result is one component version with how many SBOMs list it, how many of those belong to artifacts and to applications, and the worst vulnerability it matches; **Show where** opens the list, linking to each artifact version or application version. An advisory's id, wherever it appears, opens its page: what it says, its references, and everything you can see that it affects with the fixing version. Needs **Pro**."),
            SHOT("browse-components.png", "Browse → Components: find every SBOM that lists a component"),
            NOTE("The search covers repositories you can browse whole and spaces you can read. Access limited to part of a repository (a content selector) doesn't bring its SBOMs into the search. Version ranges (\"below 2.17\") aren't supported yet: search by name and read the versions."),
            TABLE(["Request", "Returns"], [
                ["`GET /api/browse/components?q=&purl=&ecosystem=`", "Components across every SBOM you can see, with counts and the worst severity; `q` of at least two characters, or a package URL"],
                ["`GET /api/browse/components/holders?ecosystem=&namespace=&name=&version=`", "What holds one component: artifact versions (with their browser address) and application versions"],
                ["`GET /api/browse/advisories/{id}`", "An advisory and everything you can see that it affects, with fixing versions"],
            ]),

            H("Applications"),
            P("An application belongs to a space and has a key (`shop`, `billing-api`), a name and a description. Its versions appear as SBOMs are uploaded for them: there's nothing to create first. A version can hold more than one document (one for the service, one for its base image) and can be linked to the artifact versions it was built from, so the connection between what was published and what was deployed is recorded. Everything is in the space's **SBOMs** tab: the applications with search, each one's versions with an upload form and the CI command, and each version's SBOMs with their components, vulnerabilities and downloads, plus the linked artifact versions."),
            SHOT("sbom-applications.png", "A space's SBOMs tab: registered applications"),
            SHOT("sbom-version.png", "An application version: its SBOM with completeness, components, vulnerabilities and export"),
            TABLE(["Who", "Needs", "Can"], [
                ["Space viewers", "`spaces:read`", "See applications, their versions, documents and components; download the documents"],
                ["Space developers and up", "`spaces:sbom:write`", "Register, rename and delete applications; upload and delete SBOMs; set links"],
            ]),
            P("Without an Enterprise license what exists stays readable, but nothing can be registered or uploaded (`402 license_required`)."),

            H("Uploading from CI"),
            P("Upload the SBOM a build tool produced as the request body, with an API token that carries `spaces:sbom:write`. The version is created when it doesn't exist; a second upload to the same version adds another document."),
            CODE("""# syft, trivy, cdxgen, cyclonedx-maven-plugin, … produce the file
syft packages dir:. -o cyclonedx-json > sbom.cdx.json

curl -f -X POST -H "Authorization: Bearer $DEPOTEX_TOKEN" \\
  --data-binary @sbom.cdx.json \\
  "https://depotex.example.com/api/spaces/platform/sbom/applications/shop/versions/3.1.0/documents?name=sbom.cdx.json\""""),
            P("The answer describes the stored document: its format, the tool that made it, how many components it lists and the software it describes (CycloneDX `metadata.component`, SPDX `DESCRIBES`). Documents over `BROWSE_GUARD_MAX_COMPONENTS` components (50,000) are kept up to the limit and marked **truncated**."),
            TABLE(["Refusal", "Meaning"], [
                ["`422 sbom_refused`", "Not an SPDX or CycloneDX document, or over a limit; `details.reason` says which (`malformed`, `too_large`, `too_deep`, `too_many_elements`, `entity_declared`, `timeout`)"],
                ["`400 sbom_too_large`", "Larger than `BROWSE_GUARD_MAX_SBOM` (32 MB)"],
                ["`400 invalid_version`", "A version is 1-200 letters, digits, dots, dashes, pluses, tildes or underscores"],
                ["`409 key_taken`", "An application with that key exists in the space"],
            ]),

            H("Vulnerability data"),
            P("With vulnerability data on, every component that has a package URL is checked against known vulnerabilities, and each SBOM reports what its components carry: the advisories, their severity and score, and the version that fixes each one. The check uses the **OSV** service (osv.dev), which covers npm, PyPI, Maven, Go, crates.io, NuGet, Packagist, RubyGems, Hex, Pub, Linux distributions and GitHub's advisories. Needs **Pro**."),
            SHOT("vulnerability-data.png", "Settings → Vulnerability data: the OSV service, how often components are checked again, and a test"),
            UL([
                "Turn it on under **Settings → Vulnerability data** (super admins). Only package names and versions are sent; nothing about your repositories, users or files.",
                "Each distinct package version is asked about once, then again after the re-check interval (24 hours by default), so new advisories are found for what you already have. The check runs every few minutes as the job `sbom-vuln-sync`; **Test** on the settings page asks the endpoint about a known vulnerable package.",
                "In an air-gapped network, point the endpoint at a mirror of the OSV API inside your network.",
                "Severity is the CVSS v3 base score when the advisory has a v3 vector (critical from 9.0, high from 7.0, medium from 4.0), otherwise the advisory database's own rating.",
                "Unknown is unknown: a component without a package URL, or one not checked yet, is reported as such, never as clean. Each report says how many components were checked and how many still wait.",
                "If the endpoint can't be reached, what was found stays as it was; the settings page shows the error.",
            ]),
            TABLE(["Request", "Returns"], [
                ["`GET /api/browse/versions/{id}/sbom/{n}/vulnerabilities`", "What matched an SBOM stored with a version: a summary per severity and each advisory (id, aliases, summary, severity, score, references) with the components it hits and the fixing version"],
                ["`GET …/applications/{app}/versions/{version}/documents/{n}/vulnerabilities`", "The same for an application's SBOM"],
                ["`GET`, `PUT /api/sbom/vulnerability-data`", "The settings (`enabled`, `endpoint`, `recheckHours`) and status (last check, errors, counts); `vulnerability_data:manage`"],
                ["`POST /api/sbom/vulnerability-data/test`", "Checks that the endpoint answers like OSV"],
            ]),

            H("Events"),
            P("Registering and deleting an application and uploading and deleting a document raise `sbom.application.create`, `sbom.application.delete`, `sbom.document.upload` and `sbom.document.delete` (before and after). Policies can refuse them: for example only CycloneDX, or no document listing fewer than ten components. The upload event carries the format, the tool, the component count and whether the document was truncated. Changing the vulnerability data settings raises `sbom.vulnerability_data.update`; VEX statements raise `sbom.vex.update` and `sbom.vex.delete`; every SBOM is evaluated by `sbom.document.evaluate`, new advisories raise `sbom.vulnerability.found`, and a share link raises `sbom.share.create`. See [Events](events.html)."),

            H("API"),
            P("Applications live under the space; SBOMs of artifact versions under the browser's version. Lists use cursor paging (`cursor`, `limit`)."),
            TABLE(["Request", "Returns"], [
                ["`GET /api/spaces/{space}/sbom/applications?q=`", "The space's applications by key, with version counts; `licensed`"],
                ["`POST /api/spaces/{space}/sbom/applications` `{key, name, description}`", "Registers an application (201)"],
                ["`GET`, `PUT`, `DELETE …/applications/{app}`", "One application; rename; delete with everything in it"],
                ["`GET …/applications/{app}/versions`", "Its versions, newest first, with document and component counts"],
                ["`GET …/versions/{version}`", "A version with its documents and links"],
                ["`DELETE …/versions/{version}`", "Removes the version and its documents"],
                ["`PUT …/versions/{version}/links` `{versionIds: []}`", "Replaces the linked artifact versions (ids from the browser, in the space)"],
                ["`POST …/versions/{version}/documents?name=` (body: the SBOM)", "Stores a document (201); `X-File-Name` names it too"],
                ["`GET …/documents/{n}`", "The document and the relationships between its components (at most 5,000)"],
                ["`GET …/documents/{n}/components?q=`", "Its components (purl, name, version, type, supplier, licenses, hashes), paged; `q` matches name or purl"],
                ["`GET …/documents/{n}/download`", "The file as uploaded"],
                ["`DELETE …/documents/{n}`", "Removes the document"],
                ["`GET /api/browse/versions/{id}/sbom/{n}`, `…/components`", "The same for an SBOM stored with an artifact version (`n` from `/attachments`)"],
            ]),
            P("Deleting a space removes its applications and their files."),
        ],
    )),
]
