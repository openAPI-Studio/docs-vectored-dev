"""Wiki doc pages, gathered from the content_*.py modules.

Each feature page is kept in step with the code in the depotex repo
(apps/wiki and the platform it builds on). When a feature is added or
changed there, update its page and add a line at the top of CHANGELOG, then
run `python3 wiki/_build/build.py`.
"""
from engine import H, P, UL, TABLE, NOTE, SHOT
from content_user_a import USER_A
from content_user_b import USER_B
from content_admin_wiki import ADMIN_WIKI
from content_platform_config import PLATFORM_CONFIG
from content_platform_operate import PLATFORM_OPERATE

# Releases after the initial one, newest first: (date, feature, one-sentence change).
# Only changes people using or running the Wiki notice; nothing internal.
CHANGELOG = [
    ("2026-11-21", "Editor", "Fixed: on a published page, changing Figures, heading numbers or the title closed the editor and showed the page, as if it had been published. The unpublished changes were kept as a draft and weren't published."),
    ("2026-11-21", "Mentions", "In a private space, administrators who read every space can be mentioned as well as the space's members, so the @ list is no longer empty in a private space nobody was added to."),
    ("2026-11-21", "Editor", "Fixed: after adding an image or another whole block to a column, clicking into another column left the block selected, so the next thing typed replaced it."),
    ("2026-11-21", "Imports", "Confluence page layouts are imported as rows of columns instead of one block under the other, and the editor's Layout menu gains Two columns."),
    ("2026-11-21", "Editor", "Sections: the editor groups a page into sections (a heading, text up to an empty line, each macro or other block) that can be moved up and down or selected whole from a handle at the right; text colour and highlight in six theme colours; and rows of columns (three equal, wide left, wide right) from the new Layout menu."),
    ("2026-11-20", "Install", "The reverse proxy can send everything under `/api` straight to the server, and the Caddy and nginx examples now do: API calls no longer use the web app's CPU, which was the first thing to run out under load. The server sets the security headers of API responses itself. A proxy that routes only `/api/ws` keeps working. See [Install the Wiki](install.html)."),
    ("2026-11-20", "Security", "The server takes `X-Forwarded-For`, `X-Forwarded-Host`, `X-Forwarded-Proto` and `X-Real-IP` only from the proxies in `TRUSTED_PROXIES` (the same host by default) and removes them from anyone else. If your reverse proxy runs on another host and isn't listed, add it: the system check's new **Forwarded headers** line names an address that was refused."),
    ("2026-11-20", "Performance", "Pages are much smaller: each one carried every text of the screen's area again, and now the browser loads those once and keeps them."),
    ("2026-11-20", "Sign-in", "Links from invitation and password emails now open when the web app passes API calls on: the link's token was dropped on the way, so the page said the link was invalid."),
    ("2026-11-20", "Interface", "Counts read right for one: a board's \"1 of 1 vote left\", an import's \"1 of 1 page\", the Recently updated block's summary and the note when a mirror source is removed."),
    ("2026-11-19", "Pages", "Page locks: a page and the pages under it can be kept to some people and groups, or opened to everyone to read and only some to edit; locked pages stay out of the tree, search, labels, the calendar, analytics, alerts and blocks for everyone else, and space admins see and remove locks in Space settings → Locked pages."),
    ("2026-11-19", "Spaces", "Spaces get an icon (one of 24 built-in images, initials in a theme colour, or an uploaded image), up to 10 labels shared with pages, a category from Settings → Space categories, archiving (read-only until restored) and personal stars that pin spaces to the top of the space list, which can now be filtered by category and label."),
    ("2026-11-19", "Templates", "A template library under Settings → Templates that every space starts pages from, with twelve ready-made templates; a template can create a whole tree of pages; spaces can switch library templates off or keep their own version; and templates can be written in a template editor."),
    ("2026-11-18", "Mirror spaces", "Mirror spaces (Pro): a space can show the docs of a git repository (GitHub, GitLab, Gitea, Forgejo, Bitbucket Cloud) or of uploaded archives as read-only pages, synced on a schedule, by webhook or from a pipeline, with suggested edits as pull or merge requests and a button to convert the space back. A mirror space is chosen when the space is created and has only the tabs a mirror needs."),
    ("2026-11-18", "Pages", "Mermaid diagrams: flowcharts, sequence diagrams and more drawn from text on any page, in the reader's light or dark theme."),
    ("2026-11-18", "Pages", "HTML blocks: space admins can run their own HTML, CSS and JavaScript on pages in a sandbox that reaches only the sites listed in Settings → Security → HTML blocks (off by default)."),
    ("2026-11-18", "Whiteboards", "Whiteboards are safer to share: visitors of public spaces who aren't signed in no longer see history or downloads, a board too large to read keeps showing its last picture and can be reset to it, very complex boards are drawn within limits (downloads say when a board is too complex), and new comment pins need the Enterprise licence."),
    ("2026-11-18", "Whiteboards", "Whiteboards can be facilitated (a shared timer, dot voting, private mode that hides new notes until revealed, and follow me), new boards can start with notes hidden, mind maps grow with Enter and Tab, an items list reads the board in order for keyboards and screen readers, and the toolbar folds to seven tools on phones."),
    ("2026-11-18", "Whiteboards", "Live whiteboards (Enterprise): sticky notes, pens, shapes, connectors and frames drawn together with everyone's cursors, six canvas types and space templates, comments, versions and downloads, a read-only view, and a whiteboard block for pages."),
    ("2026-11-18", "Space blogs", "Blog posts in a Confluence export can become posts on the space's blog, a post downloaded as Word or PDF starts with its date, authors and cover image, and plugins can add a panel to a space's Blog tab."),
    ("2026-11-18", "Space blogs", "A Blogs page gathers the posts of every blog you can read, the dashboard shows the latest posts of the blogs you follow, search finds posts, and space analytics have a Posts tab."),
    ("2026-11-17", "Space blogs", "Blogs can require review before a post is first published, tell their followers about new posts, and be followed in a feed reader through a public or personal feed address."),
    ("2026-11-17", "Space blogs", "Each space has a Blog tab for dated posts, with featured posts, an archive by month, following, co-authors, cover images and blog settings for space admins."),
]

INTRO = [
    NOTE("The Wiki isn't released yet. Early adopters: [contact us for access](../support.html?tool=wiki&type=access) to get the server and a license."),
    P("The Wiki is a self-hosted team wiki. People write pages together in spaces, see each other's edits live, ask and answer questions, plan with space calendars and see what is read. It runs on a single server or as a cluster, with the same features either way, on the same platform as [Depotex](../depotex/): the same sign-in, settings, backups, plugins and audit log."),
    SHOT("home-overview.png", "Spaces, where the Wiki opens: every space you can read, with its visibility and your role"),
    H("What it does"),
    TABLE(["Capability", "What the Wiki does"], [
        ["**Spaces for every team**", "[Spaces](docs/spaces.html) hold pages and decide who reads and writes them: private, internal or public, with roles for people and groups."],
        ["**Pages written together**", "A Word-like [editor](docs/editor.html) with headings, tables, images, videos and [macros](docs/macros.html); [live editing](docs/editing-together.html) with everyone's cursors; autosave, [drafts, reviews and publishing](docs/drafts-and-publishing.html), [versions](docs/page-history-and-versions.html) you can compare and restore, and [comments](docs/comments.html)."],
        ["**Whiteboards**", "[Live whiteboards](docs/whiteboards.html) to sketch, plan and run retrospectives together, with timers, dot voting and notes hidden until revealed (Enterprise)."],
        ["**Questions and answers**", "Company-wide [Q&A](docs/qna.html): ask, answer, vote and accept, with mentions and links to pages."],
        ["**Calendars**", "[Space calendars](docs/calendar.html) with events, leave, publishing plans and review dates, and a feed for your own calendar app."],
        ["**Analytics**", "[Page, space and personal analytics](docs/analytics.html) and content health: stale pages, broken links, searches that find nothing."],
        ["**Moves in and out**", "[Import](docs/import-and-export.html) Markdown files or a whole space from Confluence; export pages as Word or PDF."],
        ["**Runs where you do**", "PostgreSQL holds everything; Redis is optional on one server and required for a [cluster](admin/deployment-modes.html); attachments go to a local disk, S3, MinIO or Azure Blob. See the [admin guide](admin/index.html)."],
    ]),
    H("Where to start"),
    UL([
        "[Getting started](docs/getting-started.html): sign in, open a space and write your first page.",
        "[Admin guide](admin/index.html): install, set up, configure and run the Wiki.",
        "[Changelog](docs/changelog.html): what's new.",
    ]),
]

CHANGELOG_PAGE = [
    ("changelog", dict(
        label="Changelog", title="Changelog", icon="history",
        desc="What each release of the Wiki includes, newest first",
        keywords=["changelog", "release notes", "whats new"],
        blocks=[
            *([H("Since the initial release"), TABLE(["Date", "Feature", "Change"], [list(row) for row in CHANGELOG])] if CHANGELOG else []),
            H("Initial release"),
            P("The first release of the Wiki: a self-hosted team wiki that runs on a single server or as a cluster, with the same features either way. Later releases are listed above this one as they ship."),
            TABLE(["Area", "What's included"], [
                ["Spaces", "[Spaces](spaces.html) that are private, internal or public, with roles for people and groups, a page tree, space settings, templates and a trash for deleted pages."],
                ["Pages and the editor", "A Word-like [editor](editor.html) with headings and heading numbers, lists, tables, images with captions, videos and the \"/\" menu; [blocks and macros](macros.html) such as panels, expands, decisions, excerpts and includes, page properties and reports, status, child pages, the page tree, recently updated and spreadsheet tables with formulas; [labels and \"Was this page helpful?\"](labels-and-feedback.html); [copies and templates](copies-and-templates.html)."],
                ["Writing together", "[Live editing](editing-together.html) with everyone's cursors, autosave, [drafts, publishing and scheduled publishing](drafts-and-publishing.html), [review requests and review-by dates](reviews.html), [versions you can compare and restore](page-history-and-versions.html), [comments](comments.html), and [watching and mentions](profile-and-notifications.html)."],
                ["Q&A", "Company-wide [questions and answers](qna.html): votes, accepted answers, comments, follows, duplicates, mentions of people and pages, reputation, and public questions for anonymous readers; [moderation](qna-moderation.html)."],
                ["Calendars", "[Space calendars](calendar.html) with events, leave and repeats, publishing plans and review dates, and a [secret feed address](calendar-feeds.html) for calendar apps."],
                ["Analytics", "[Page, space and personal analytics](analytics.html) and content health (stale pages, old drafts, broken links, disliked pages, searches that find nothing), with CSV export (Pro)."],
                ["Moving content", "[Import](import-and-export.html) Markdown files or [a space from Confluence](confluence-import.html), [mirror](mirror-spaces.html) a docs repository, and export pages as Word or PDF."],
                ["Readers outside the company", "[Anonymous access](anonymous-access.html) to public spaces and public questions, and [robots.txt for search engines](search-engines-and-robots.html)."],
                ["Platform", "Everything the Wiki shares with Depotex: [users and directories](users-and-directories.html), [single sign-on](single-sign-on.html), [API tokens](api-tokens.html), [OAuth applications](oauth-applications.html), [rate limits](rate-limits.html), [policies](policies.html), [automation](automation.html) on [events](events.html), [plugins](plugins.html) (including plugin blocks in pages), the [audit log](logging-and-audit.html), [personal data export and erasure](personal-data.html), [backups](backups.html), the [system check](system-check.html), [monitoring](monitoring.html), [email](email.html) and [branding](branding-and-banners.html)."],
                ["Installation", "A [setup wizard](setup-wizard.html) or an [unattended setup file](headless-setup.html); a [single server or a cluster](deployment-modes.html); [storage](storage.html) on a local disk, S3, MinIO or Azure Blob; [recovery mode](recovery.html) when an installed server can't start; phones and tablets supported throughout ([Mobile](mobile.html))."],
            ]),
        ])),
]

PAGES = USER_A + USER_B + ADMIN_WIKI + PLATFORM_CONFIG + PLATFORM_OPERATE + CHANGELOG_PAGE
