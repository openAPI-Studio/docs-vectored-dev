"""Wiki doc pages, gathered from the content_*.py modules.

Each feature page is kept in step with the code in the depotex repo
(apps/wiki and the platform it builds on). When a feature is added or
changed there, update its page and add a line at the top of CHANGELOG, then
run `python3 wiki/_build/build.py`.
"""
from engine import H, P, UL, TABLE, NOTE, SHOT
from content_user_a import USER_A
from content_user_b import USER_B
from content_user_c import USER_C
from content_admin_wiki import ADMIN_WIKI
from content_platform_config import PLATFORM_CONFIG
from content_platform_operate import PLATFORM_OPERATE
from content_database import DATABASE
from content_kee import KEE_USER, KEE_ADMIN
from content_kee_r2 import KEE_R2_USER, KEE_R2_ADMIN, KEE_R2_SHARED

# Releases after the initial one, newest first: (date, feature, one-sentence change).
# Only changes people using or running the Wiki notice; nothing internal.
CHANGELOG = [
    ("2026-11-23", "Kee", "Ask Kee can propose changes: a new page draft, a change to a page or one section, a comment or labels, shown in a card with the text before and after. Nothing is written until you select **Apply**, which writes as you with your own permissions; someone who may only comment gets the change as a comment. See [Proposed changes](ask-kee.html#proposed-changes)."),
    ("2026-11-23", "Kee", "**Kee studio** (Pro): build agents (Kee with instructions, the spaces and pages it reads first, and the actions it may take), try them, publish them with a version history, and share them with people, groups, a space's readers or everyone. Pick an agent in Ask Kee, **Write the page** and **Write a section**. Agents always run with the access of the person using them. See [Kee studio](kee-studio.html)."),
    ("2026-11-23", "Kee", "Connect your own AI app, such as Claude, Cursor or VS Code, to the Wiki's built-in server (Pro): it reads as you, and changes pages, comments and labels as you where an administrator allows it. Administrators turn it on with its own switch, **Let outside AI apps connect**, which works while Kee is off, and set what apps may do per group of tools under **Settings → Kee → Outside AI apps**. See [Connect AI apps](connect-ai-apps.html) and [Outside AI apps](kee-outside-apps.html)."),
    ("2026-11-23", "Kee", "Kee reads the text of files attached to pages: PDF (text layer), Word (`.docx`) and plain-text files such as CSV and Markdown. Spreadsheets, presentations, images and scans are not read. See [Ask Kee](ask-kee.html#what-kee-can-read)."),
    ("2026-11-23", "Kee", "**What changed, in words** in a page's history describes the changes between two versions in plain words, made once and shared by everyone who compares the same versions. See [Page history](page-history-and-versions.html#what-changed-in-words)."),
    ("2026-11-23", "Kee", "Scheduled help, off by default: the stale page finder lists pages that look out of date for a space's admins, and new questions in Q&A get suggested pages, earlier questions and people, shown to the asker only. Both read and suggest only, never pages under a lock, with a monthly budget of their own and a switch per space. See [Scheduled help](kee-scheduled-help.html)."),
    ("2026-11-23", "Kee", "Ask Kee answers \"how do I…\" questions about the Wiki from the product documentation built into your version, knows which screen you asked on, and **Show me** walks you through the steps with a ring around each control; you do every click yourself. See [Ask Kee](ask-kee.html#help-with-the-wiki-itself)."),
    ("2026-11-22", "Database", "The database password can be changed without downtime: `DATABASE_URL` now wins over the saved copy at start, servers fail over to a second login (`DATABASE_URL_STANDBY`) when one is refused, and super admins rotate passwords now or on a schedule under **Settings → Database**. See [Database password](database-credentials.html)."),
    ("2026-11-22", "Kee", "Kee, the Wiki's AI (Pro): administrators turn it on in **Settings → Kee**, connect Anthropic, OpenAI, Google Gemini or Amazon Bedrock with their organisation's own key, choose the models people may use with a default and a fallback, switch each feature on or off, decide who may use Kee in a permissions grid, and set a daily limit per person and a monthly budget. Nothing is sent anywhere until it is set up. See [Set up Kee](kee-setup.html)."),
    ("2026-11-22", "Kee", "Writing with Kee in the editor: a section's menu can improve, shorten, lengthen or fix the spelling of a section, change its tone, translate it or follow a request of your own, and write a new section below; selected words can be rewritten on their own; an empty page can get a first draft. You see the changes first and choose **Replace** or **Keep original**. See [Writing with Kee](kee-editor.html)."),
    ("2026-11-22", "Kee", "**Summarise with Kee** above a long published page: a short summary made once per version and language and shared by every reader of it. See [Page summaries](kee-summaries.html)."),
    ("2026-11-22", "Kee", "**Ask Kee** in the top bar answers questions from the pages you can read, with numbered links to its sources, earlier conversations and feedback on answers. It finds pages by their titles for now. See [Ask Kee](ask-kee.html)."),
    ("2026-11-22", "Kee", "A space's admins can turn Kee off for their space (nothing of it is then sent to a model) and tell readers when a page holds text written with Kee; the page history marks versions written with Kee. Each person sees their Kee requests left today under **Profile → Kee**. See [Kee data handling](kee-data.html#kee-in-a-space)."),
    ("2026-11-22", "Pages", "Slides: put an HTML deck (from an AI tool, reveal.js or Marp) or a PDF deck in a page, step through it with the Wiki's controls or present it full screen; HTML decks run in a sandbox that loads libraries only from the hosts in the new Settings → Security → Slides, which also sets who adds decks (page editors by default) and the largest deck. See [Slides](slides.html)."),
    ("2026-11-21", "Upgrades", "New blocks wait for the whole installation: the \"/\" menu and imports offer them once every server runs the new version, and an editor tab whose web app is older than the servers says **A newer version of the wiki is running** and asks to reload. Upgrade the web app first; see [Upgrades](upgrades.html#new-blocks-during-an-upgrade)."),
    ("2026-11-21", "Imports", "Confluence task reports become task reports, Widget connector and iframe macros become videos (YouTube, Vimeo) or link cards, and smart links shown as cards become link cards; action items keep their assignee and due date."),
    ("2026-11-21", "Pages", "Link cards: a link shown with its title, description and site name, filled in from the linked page when an administrator turns on Settings → Security → Link previews (off by default; the server reads only the page's text, never private addresses)."),
    ("2026-11-21", "Pages", "Tasks: a checklist item's first @mention is its assignee and its first date its due date, overdue dates stand out, and the new Task report block lists open or done tasks across spaces, for anyone, one person or whoever is reading."),
    ("2026-11-21", "Imports", "Confluence Content by label, Content report table, Blog posts, Contributors and Change history macros become the matching blocks; filters the Wiki doesn't have are counted in the import report."),
    ("2026-11-21", "Pages", "Four new blocks: Pages by label (pages with some labels, in this space or others, as a list or a table), Blog posts (a blog's latest posts), Contributors and Change history."),
    ("2026-11-21", "Imports", "Every Confluence attachment is imported, not only images and videos; View file, PDF, Office viewer and Multimedia macros become File blocks, Attachments an attachments list and Gallery a gallery. The import report counts files that are missing, blocked or too large, and attachments lists whose name filter was simplified."),
    ("2026-11-21", "Settings", "Settings → Security → Attachments sets the largest PDF or other file (100 MB by default) and the file extensions no page takes (`.exe`, `.msi`, `.bat` and other programs by default)."),
    ("2026-11-21", "Pages", "Any file can be attached to a page, and three blocks show them: File (a card with preview and download, or a PDF or image shown in the page), Attachments list (the page's files, with an upload button for editors) and Gallery (images that open full size)."),
    ("2026-11-21", "Editor", "Dates: **//**, \"/\" Date or Insert → Date puts a date in the text, shown in each reader's language."),
    ("2026-11-21", "Imports", "Sections and columns made with Confluence's older Section and Column macros are imported as rows of columns too."),
    ("2026-11-21", "Clustering", "A server that is refused at start (for example because its storage isn't shared) no longer stays in **Settings → Clustering** as **Left**, and the Statuses help explains Left. See [Clustering page](deployment-modes.html#clustering-page)."),
    ("2026-11-21", "Editor", "Page width: each page can be Narrow (as before), Medium or Full width, chosen from a new menu at the end of the editor toolbar. Readers see the page at the chosen width; small screens are unchanged."),
    ("2026-11-21", "Editor", "Fixed: on a published page, changing Figures, heading numbers or the title closed the editor and showed the page, as if it had been published. The unpublished changes were kept as a draft and weren't published."),
    ("2026-11-21", "Mentions", "In a private space, administrators who read every space can be mentioned as well as the space's members, so the @ list is no longer empty in a private space nobody was added to."),
    ("2026-11-21", "Editor", "Fixed: after adding an image or another whole block to a column, clicking into another column left the block selected, so the next thing typed replaced it."),
    ("2026-11-21", "Imports", "Confluence page layouts are imported as rows of columns instead of one block under the other, and the editor's Layout menu gains Two columns."),
    ("2026-11-21", "Clustering", "Redis can be added to, changed on or removed from a running installation in **Settings → Clustering → Redis**, with a connection test, so a single server can grow into a cluster. The page shows which servers use Redis and which need a restart. A second server can't join while a server runs without Redis. See [Add Redis to a running installation](deployment-modes.html#add-redis-to-a-running-installation)."),
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
        ["**Kee, AI in the Wiki**", "[Writing help](docs/kee-editor.html) in the editor, [page summaries](docs/kee-summaries.html), [Ask Kee](docs/ask-kee.html) with changes you apply, [agents](docs/kee-studio.html) you build and share, and [your own AI apps](docs/connect-ai-apps.html) connected to the Wiki, on your organisation's own model provider account, with switches, limits and a switch per space (Pro). See [Kee](docs/kee.html)."],
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

PAGES = USER_A + USER_B + USER_C + KEE_USER + KEE_R2_USER + KEE_R2_SHARED + ADMIN_WIKI + KEE_ADMIN + KEE_R2_ADMIN + PLATFORM_CONFIG + PLATFORM_OPERATE + DATABASE + CHANGELOG_PAGE
