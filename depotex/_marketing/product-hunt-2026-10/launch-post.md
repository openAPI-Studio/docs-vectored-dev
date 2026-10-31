# Depotex: Product Hunt launch kit

Everything below is ready to paste into the Product Hunt launch form (producthunt.com/posts/new). Placeholders in **[brackets]** need your answer before launch.

---

## 1. Name

**Depotex**

## 2. Tagline (60 characters max)

Pick one:

1. **The self-hosted artifact repository built for AI agents** (55)
2. Every package your teams build and use, on your server (54)
3. 18 package formats, one URL, quarantine and AI built in (55)

Recommended: **1**. It says what it is and what's new about it.

## 3. Links

| Field | Value |
|---|---|
| Website (main link) | **[website, sign-up, trial or waitlist URL]** |
| Documentation | https://docs.vectored.dev/depotex/ |
| Getting started | https://docs.vectored.dev/depotex/docs/getting-started.html |
| Supported formats | https://docs.vectored.dev/depotex/docs/formats.html |
| Changelog | https://docs.vectored.dev/depotex/docs/changelog.html |
| X / LinkedIn | **[company handles, if any]** |

Don't add the GitHub repo: it's private and the code is under a proprietary licence.

## 4. Short description (260 characters max)

> Depotex is a self-hosted artifact repository for 18 package formats: Maven, npm, PyPI, Docker, Helm, Go, Cargo, Conda and more behind one URL. Quarantine, block lists, SBOMs and backups are built in, and AI agents can search it over MCP, as you.

(245 characters)

## 5. Topics

Pick up to three: **Developer Tools**, **Security**, **Artificial Intelligence**. If Product Hunt offers **DevOps** or **Open Source**, use DevOps in place of AI if you want to reach platform teams. Don't pick Open Source.

## 6. Pricing

**Paid** (Standard, Pro, Enterprise licences). **[Change this to "Free options" if there will be a free tier or trial at launch.]**

## 7. Maker's first comment

> Hi Product Hunt 👋 I'm Akshay, maker of Depotex.
>
> Every company that builds software runs an artifact repository: the server that holds your own packages and caches the ones from Maven Central, npm, PyPI and Docker Hub. Most teams use JFrog Artifactory or Sonatype Nexus. Both work, but they come with a long list of extras sold separately, admin screens from another decade, and nothing for the AI agents that now write and ship half the code.
>
> So I built Depotex: one self-hosted server for every package your teams build and use.
>
> **What it does**
> • **18 formats behind one URL**: Maven, npm, PyPI, Docker & OCI, Helm, Go, NuGet, Cargo, APT, YUM, Terraform, Hugging Face, Git LFS, Composer, RubyGems, Conda, Conan and raw files. Hosted, proxy and group repositories, so builds keep working when a public registry doesn't.
> • **Supply-chain security in the box**: quarantine new or suspect versions ("new npm versions wait 3 days" is one rule), a block list that works through proxies, SBOMs with OSV vulnerability data, and integrity checks on every stored file.
> • **Built for AI agents**: a signed MCP plugin lets AI assistants search artifacts, read SBOMs and docs and get download links, signed in as the person using them. Write tools are off by default.
> • **Vibe artifacts**: a home for what AI coding tools build, with each check-in's code, memory, known gaps and screenshots, scanned for secrets on every push.
> • **Runs itself**: encrypted backups with automatic test restores, policies with a dry run, automation, audit log, Prometheus metrics, SSO and SCIM. One server or a cluster, same features either way.
>
> **What I'd love from you**
> Tell me which format or migration path matters most to your team, and what annoys you most about the repository you use today. I'm here all day to answer questions.
>
> Docs: https://docs.vectored.dev/depotex/

## 8. Gallery (upload in this order)

Images are 2540×1520 (2× the recommended 1270×760, same shape). The first one is the cover.

1. `gallery/01-dashboard.png`: what Depotex is, with the dashboard
2. `gallery/02-browse.png`: 18 formats, one URL
3. `gallery/03-quarantine.png`: quarantine and installation rules
4. `gallery/04-sbom.png`: SBOMs and vulnerabilities
5. `gallery/05-ai-agents.png`: MCP tools for AI agents
6. `gallery/06-vibe.png`: vibe artifacts
7. `gallery/07-backups.png`: backups with test restores
8. `gallery/08-platform.png`: policies and automation

Thumbnail (logo): `gallery/thumbnail-240.png`.

## 9. Video

`depotex-tour.mp4` (1920×1080, 36 seconds, no sound): a walkthrough of the eight gallery screens. Product Hunt only takes a YouTube or Loom link for video, so upload it there (unlisted works) and paste the link in the video field.

### Narrated explainer (main video)

`depotex-explainer.mp4` (1920×1080, 2 min 5 s): a flat illustrated explainer with a narrator, music, sound effects and burned-in captions (so it works muted). It follows Maya, who vibe-codes a dinner-planner app, through four problems (a secret key in the code, a made-up or look-alike package, hidden instructions in AGENTS.md, no last working version) and then shows how Depotex vibe artifacts fix each one. It closes on Depotex, "by Vectored" and vectored.dev. Source and narration script: `explainer-source/`.

### Vibe coding story video

`depotex-vibe-coding-story.mp4` (1920×1080, 51 seconds, with an original soundtrack), made with three.js: code cards flying around ("Everyone is vibe coding"), five problems turning them red (keys in code, made-up packages, hidden instructions in AGENTS.md, no last working version, lost context), then the cards locking into ordered check-ins with how Depotex fixes each one, the Vibe browser, and a close on Depotex and vectored.dev. Use this one as the main Product Hunt video and the tour as a second. Source to edit it: `video-source/`.

## 10. Launch-day checklist

- [ ] Fill the **[bracketed]** placeholders above
- [ ] Make the docs public for launch: the `depotex/` docs are unlisted and every page shows a "Coming soon" banner
- [ ] Schedule for 12:01 AM Pacific, ideally Tuesday to Thursday
- [ ] Post the maker's comment as soon as it goes live
- [ ] Share the launch link with your network (ask people to try it and comment, never to "upvote")

## Notes

- All screenshots are from the product docs and use fictional data (Acme, Orion, example.com).
- No format logos in the gallery: several owners (npm, Docker, Maven, NuGet, Terraform) haven't given permission yet.
- The copy doesn't name Claude or any AI vendor's product. Anthropic allows the "Claude Code" text label in the product but no implied affiliation, so marketing says "AI assistants" and "MCP".
