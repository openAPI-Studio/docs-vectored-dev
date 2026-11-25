"""Wiki doc pages (user_c): the blocks added with the Confluence macro catch-up:
files and attachments (file card, attachments list, gallery), lists of pages
and page information (pages by label, blog posts, contributors, change
history), tasks and task reports, link cards and link previews. See content.py.
Keep in step with apps/wiki in the depotex repo."""
from engine import H, P, UL, TABLE, NOTE, WARN, STEPS, SHOT

USER_C = [
    # ------------------------------------------------------------------
    ("files-and-attachments", dict(
        label="Files &amp; attachments", title="Files and attachments", icon="file",
        desc="Attach any file to a page and show it as a card, a PDF preview, a list of the page's files or a gallery of its images",
        keywords=["file", "files", "attachment", "attachments", "pdf", "preview", "view file", "viewpdf", "word", "excel", "powerpoint",
                  "office", "zip", "download", "attachments list", "gallery", "lightbox", "slideshow", "images", "blocked extensions",
                  "largest file", "rename", "upload"],
        blocks=[
            H("Overview"),
            P("Besides images and videos, a page can hold any file: PDFs, Word, Excel and PowerPoint documents, archives, drawings. Three blocks show a page's files to its readers:"),
            TABLE(["Block", "Shows", "Insert with"], [
                ["**File**", "One file as a card with its name, kind and size, with **Preview** and **Download**; a PDF or an image can also be shown in the page itself", "**/file** or **Insert file**, or drop the file onto the page"],
                ["**Attachments list**", "Every file attached to the page, with an **Upload files** button for people who edit it", "**/attachments** or **Insert attachments list**"],
                ["**Gallery**", "The page's images as a grid of tiles that open full size", "**/gallery** or **Insert gallery**"],
            ]),
            P("The blocks show the files of the page they are on. Readers see a file only once the page shows it to them: see [Who sees which files](#who-sees-which-files)."),

            H("File"),
            P("Choose **/file** (or **Insert file** in the toolbar's Insert menu) and pick one of **Files of this page**, find one by name, or **Upload a file**. Dropping or pasting a file that isn't an image onto the page uploads it and puts a File block where you dropped it."),
            SHOT("page-file-card.png", "A File block as readers see it: a Word document's name, kind and size, with Preview and Download"),
            UL([
                "**Display**: **Card** (the default) shows the file's name, kind (Image, Video, PDF or File) and size. **Shown in the page**, for PDFs and images, draws the file itself in the page, with a **Height** of 200 to 1,200 pixels (600 by default).",
                "**Preview** opens images, videos and PDFs full size over the page; **Esc** or **Close** goes back. Other files, such as Word or ZIP files, only download.",
                "**Download** saves the file under its name. Files other than images, videos and PDFs always download, never open in the browser.",
                "When a file is renamed, the card shows its new name. When a file is deleted from the page, the card says **File removed**, with the name it had.",
            ]),
            P("A PDF shown in the page is drawn page by page as you scroll to it, up to 50 pages; after that it says how many more pages there are and offers the download. The PDF's links, forms and scripts don't run. A PDF that can't be drawn says so and offers the download instead."),
            SHOT("page-file-inline-pdf.png", "A PDF shown in the page, 600 pixels high, with its first page drawn"),

            H("Attachments list"),
            P("The **Attachments list** lists the page's files, newest first, with each file's kind, size and date and a **Download** link (and **Preview** for images, videos and PDFs). The first 100 show at once; **Show more** shows the rest."),
            SHOT("page-attachments-list.png", "An attachments list showing PDFs and Office files, with Upload files for an editor"),
            TABLE(["Setting", "What it does"], [
                ["**File types**", "Only images, videos, PDFs or other files, or any mix. None ticked lists every kind."],
                ["**File name filter**", "Only files whose names match, with `*` for any characters and `?` for one, and commas between several: `*.pdf, *.docx`."],
                ["**Order**", "**Newest first**, **Oldest first**, **Name** or **Size**."],
                ["**Show an upload button to editors**", "On by default. People who may edit the page get **Upload files**; what they upload there is listed for readers at once, without publishing the page again."],
            ]),
            P("Templates can hold an attachments list too: a page made from the template lists its own files."),

            H("Gallery"),
            P("A **Gallery** shows images as square tiles. Select one to see it full size: the arrows (or the arrow keys, and swiping on a phone) go to the previous and next image, and **Esc** closes it."),
            SHOT("page-gallery.png", "A gallery of six images in four columns, with a title and the file names under them"),
            SHOT("page-gallery-lightbox.png", "An image of a gallery opened full size: image 3 of 6, with the previous and next arrows"),
            TABLE(["Setting", "What it does"], [
                ["**Images**", "**Every image of the page** (new images join it by themselves), or **Images I choose**, up to 60, in an order you set with **Move up** and **Move down**."],
                ["**Title**", "Shown above the gallery (optional)."],
                ["**Columns**", "2 to 6 (4 by default). Phones show two."],
                ["**Order**", "For every image of the page: **Name** (the default), **Newest first**, **Oldest first** or **Size**."],
                ["**Show file names**", "On by default: each tile shows its image's name."],
            ]),
            P("A page holds up to 10 galleries. Galleries show the images as they were uploaded, so a gallery of many large photos takes a while on a slow connection: the tiles further down load as you scroll to them."),

            H("Who sees which files"),
            UL([
                "People who may edit a page see all of its files, in the editor and in the blocks.",
                "Readers see a file that a published version of the page shows (in a File block or a gallery you chose the images of, or as an image or video) and every file uploaded through an attachments list's **Upload files**.",
                "A file uploaded in the editor and not yet published reaches readers when the page is published.",
                "Inside a page included in another ([Include page](macros.html#include-page)), an attachments list and a gallery of every image say that the files are on the included page; File blocks and galleries of chosen images still show.",
            ]),

            H("Versions of a file"),
            P("Upload a newer version of a file and it replaces the old one everywhere: every File block, list, gallery, image and link that shows the file shows the new version, and its address stays the same. Published versions of the page keep the file they were published with, so readers see the new version once you publish the page."),
            STEPS([
                "Open the versions|Choose **Versions** on a File block, or the clock button on a row of an attachments list.",
                "Upload|Choose **Upload new version** and pick the file. It must be the same kind of file as the old one (an image for an image, a PDF for a PDF); anything else is refused, and can be attached as a new file instead.",
                "Check|The new version is listed as **Current**. Each version has its own download.",
            ]),
            P("When you upload a file through an attachments list's **Upload files** and the page already has a file of the same name, the Wiki asks: **New version** makes it a new version of that file, **Keep both** attaches it as a second file."),
            SHOT("files-versions.png", "The Versions dialog of a PDF: version 2 marked Current, version 1 below, each with a download, and Upload new version"),
            UL([
                "Readers see **Versions** once a file has two published versions, and only the versions a published version of the page showed.",
                "An older version is kept while a published version of the page shows it; others are deleted when the next version is uploaded. Every version counts toward the page's 500 files and 1 GB.",
                "Comparing two versions of the page in **History** shows each side's images as they were then.",
                "Restoring an old version of the page shows the latest version of each file. A copy of a page copies only the latest version of each file.",
            ]),

            H("Rename and delete"),
            P("A file keeps the name it was uploaded with. People who may edit the page can rename or delete one through the [API](#api); a renamed file stays in every block that shows it, and a deleted one shows as **File removed** in the blocks and versions that showed it."),

            H("Downloads and imports"),
            UL([
                "In a page downloaded as Word or PDF, a File block is a line with the file's name, kind and size, linked to the file; an attachments list lists the files you may see (up to 100); a gallery prints its images one under another (up to 24). PDFs shown in the page are printed as their line.",
                "Confluence's file macros (**View file**, **PDF**, **Office** viewers, **Multimedia**), **Attachments** and **Gallery** become these blocks in an [import](confluence-import.html#how-confluence-macros-are-imported), and every attachment is imported, except blocked or too-large files.",
            ]),

            H("Limits"),
            TABLE(["What", "Limit"], [
                ["Images, videos, subtitles", "20 MB, 200 MB and 512 KB, as before (see [Images and videos](attachments-and-media.html))"],
                ["PDFs and other files", "100 MB by default; your administrator sets it between 1 and 200 MB"],
                ["Blocked file names", "Files ending in `.exe`, `.msi`, `.bat`, `.cmd`, `.com`, `.scr`, `.ps1`, `.dll`, `.jar`, `.app` or `.dmg` can't be attached, unless your administrator changes the list"],
                ["Per page", "500 files and 1 GB together"],
                ["Galleries", "10 a page; 60 chosen images each"],
            ]),
            P("A refused file says why: **Files ending in .exe can't be attached here**, or that the file is too large."),

            H("For administrators"),
            P("**Settings → Security → Attachments** (`settings:write`) decides which files pages take, for the whole installation:"),
            SHOT("settings-security-attachments.png", "Settings → Security → Attachments: the largest file and the blocked extensions"),
            TABLE(["Setting", "Default", "Effect"], [
                ["**Largest file**", "100 MB", "For PDFs and other files, from 1 to 200 MB. Images, videos and subtitles keep their own limits."],
                ["**Blocked extensions**", "exe, msi, bat, cmd, com, scr, ps1, dll, jar, app, dmg", "Files whose names end in one of these can't be attached to any page. Type an extension (without the dot) and choose **Block**; up to 100."],
            ]),
            P("Save with the Security page's **Save** bar. Files already attached stay as they are. Imports follow the same settings: a blocked or too-large file is left out and counted in the import report."),
            WARN("The Wiki doesn't scan files for viruses. Files other than images, videos and PDFs are always downloaded, never opened in the browser, but keep the blocked list for files that run when opened."),
            P("Changing the settings raises `attachment_settings.update`; renaming a file raises `page.attachment.update`; a new version of a file raises `page.attachment.version`; uploading and deleting any file raise `page.attachment.create` and `page.attachment.delete`. Policies can refuse each of them; see [Events](events.html). The changes are in the audit log."),

            H("API"),
            TABLE(["Method", "Path", "Who", "What"], [
                ["GET", "`/api/spaces/{key}/pages/{id}/attachments`", "Read the page", "The page's files you may see: everything for its editors, the listed files and those its latest published version shows for readers. `kind` (`image`, `video`, `pdf`, `file`, comma-separated), `q` (part of the name), `sort` (`new`, `old`, `name`, `size`), `cursor`, `limit`"],
                ["POST", "`/api/spaces/{key}/pages/{id}/attachments`", "Edit the page", "Upload a file (multipart, field `file`). `any=true` takes PDFs and other files; `listed=true` puts it in the attachments list. Both go before `file`"],
                ["GET", "`/api/spaces/{key}/pages/{id}/attachments/{attachment}`", "Read the page", "The file; `?download=1` saves it instead of opening it. `?version=N` asks for a version of it, `?pageVersion=N` for the one a published version of the page showed"],
                ["PATCH", "`/api/spaces/{key}/pages/{id}/attachments/{attachment}`", "Edit the page", "Rename: `{filename}`, 1 to 255 characters"],
                ["GET", "`/api/spaces/{key}/pages/{id}/attachments/{attachment}/versions`", "Read the page", "The file's versions you may see, newest first (`number`, `filename`, `size`, `createdAt`, `latest`)"],
                ["POST", "`/api/spaces/{key}/pages/{id}/attachments/{attachment}/versions`", "Edit the page", "Upload a new version (multipart, field `file`), of the same kind; refused with `version_kind_mismatch` otherwise"],
                ["DELETE", "`/api/spaces/{key}/pages/{id}/attachments/{attachment}`", "Edit the page", "Delete the file from the page and the versions that showed it"],
                ["GET", "`/api/wiki/attachment-settings`", "Signed in", "`blockedExtensions` and `maxFileMb`"],
                ["PUT", "`/api/wiki/attachment-settings`", "`settings:write`", "Change them"],
            ]),
        ])),

    # ------------------------------------------------------------------
    ("lists-of-pages", dict(
        label="Lists of pages", title="Lists of pages and page information", icon="list",
        desc="Blocks that list pages with some labels, a blog's latest posts, a page's contributors and its change history",
        keywords=["pages by label", "content by label", "label list", "blog posts", "latest posts", "news", "contributors", "authors",
                  "change history", "versions", "history", "content report table", "list", "table"],
        blocks=[
            H("Overview"),
            P("Four blocks list pages or facts about a page, worked out each time the page is shown, for the person reading it:"),
            TABLE(["Block", "Lists", "\"/\" menu"], [
                ["**Pages by label**", "Published pages that carry some [labels](labels-and-feedback.html), in this space or others", "**/labels**: opens its settings"],
                ["**Blog posts**", "The latest posts of this space's [blog](blogs.html) or of other blogs", "**/blog**"],
                ["**Contributors**", "The people who published versions of this page", "**/contributors**"],
                ["**Change history**", "This page's latest published versions", "**/history**"],
            ]),
            P("Blog posts, Contributors and Change history go in with their usual settings; select one and choose **Block settings** to change them."),
            NOTE("Each reader sees only what they may read: pages in spaces they can't read, locked pages they aren't on, drafts and trashed pages never show. What you see in the editor may be more than a reader sees; **Preview** the page to check."),

            H("Pages by label"),
            P("Lists the published pages that carry the labels you give, such as every `runbook` page across the teams' spaces."),
            SHOT("page-pages-by-label.png", "A Pages by label block in table view: runbooks from three spaces, with the space, when each was updated and who edited it last"),
            TABLE(["Setting", "Choices"], [
                ["**Labels**", "1 to 5 labels, separated by commas"],
                ["**Pages must have**", "**Any of the labels** (the default) or **All of the labels**"],
                ["**From**", "**This space**, **Every space the reader can read**, or **These spaces** (up to 5 space keys, separated by commas)"],
                ["**Show as**", "**List** or **Table** (with the space when the list spans spaces, when each was updated and, for readers who may see people, who edited it last)"],
                ["**Sort by**", "**Title**, **Last updated** or **Created**, and **Reverse the order**"],
                ["**How many**", "10, 25 (the default) or 50"],
                ["**Include blog posts**", "List posts that carry the labels too"],
            ]),

            H("Blog posts"),
            P("Lists the newest published posts of a blog, with their date, authors and summary: for example the team's latest announcements at the top of its space's overview."),
            TABLE(["Setting", "Choices"], [
                ["**From**", "**This space**, **Every space the reader can read** (blogs whose posts show on the company Blogs page) or **These spaces**"],
                ["**Labels (optional)**", "Only posts with any of these labels, up to 5"],
                ["**Show as**", "**Titles and excerpts** (the default) or **Titles only**"],
                ["**How many**", "3, 5 (the default) or 10"],
            ]),
            P("Only blogs that are on are listed. See [Space blogs](blogs.html#blog-posts-on-a-page)."),

            H("Contributors and change history"),
            SHOT("page-contributors-history.png", "A Contributors block with names and how many versions each published, and a Change history block with the five latest versions"),
            TABLE(["Block", "Settings"], [
                ["**Contributors**", "**Show as** names (the default) or a list; **How many**: 5, 10 (the default) or 20; **Show how many versions each published**. People who published the most versions come first; authors of imported versions show with the name the import gave."],
                ["**Change history**", "**How many**: 5 (the default), 10 or 20 versions, newest first, with the version number, date, who published it, its note and whether it was a minor change."],
            ]),
            P("People's names show only to readers who may see people in the space. Others read **Contributors aren't shown to you** in place of the contributors, and the change history without names. Visitors who aren't signed in are treated the same way."),

            H("Limits"),
            UL([
                "A page shows at most six lists that read other pages (Pages by label, Blog posts and [Task report](tasks.html#task-report) together); further ones say the page has too many blocks that show other pages.",
                "These blocks count toward the blocks that show other pages ([Include page](macros.html#include-page) and the others).",
                "In a page downloaded as Word or PDF, each list prints as lines with their details, as you may see it; a table prints as lines too.",
            ]),

            H("From Confluence"),
            P("An [import from Confluence](confluence-import.html#how-confluence-macros-are-imported) turns **Content by label** and **Content report table** into Pages by label, **Blog posts** into Blog posts, **Contributors** about the page itself into Contributors and **Change history** into Change history. Filters the Wiki doesn't have (excluded labels, unknown spaces, authors) are dropped, so the list may show more; the import report counts them."),
        ])),

    # ------------------------------------------------------------------
    ("tasks", dict(
        label="Tasks &amp; task reports", title="Tasks and task reports", icon="check",
        desc="Give a checklist item an assignee and a due date, and list open tasks across pages with a task report",
        keywords=["task", "tasks", "action item", "action items", "todo", "checklist", "assignee", "assign", "due date", "due", "deadline",
                  "overdue", "task report", "my tasks", "date", "//"],
        blocks=[
            H("Overview"),
            P("Every item of a **Checklist** is a task. A task can name who does it and when it is due, and a **Task report** block lists tasks from many pages: the open tasks of a project, or each reader's own."),

            H("Dates"),
            P("A date is a day written as a small chip that every reader sees in their own language and date format. Insert one with **/date**, **Insert → Date**, or by typing `//` at the start of a line or after a space. Pick a day, or **Today** or **Tomorrow**; select a date later to change it."),
            SHOT("editor-date-picker.png", "Typing // in a task: the date field with Today and Tomorrow"),
            P("Dates can be from 1900 to 2200. In a page downloaded as Word or PDF, a date is written in the language of the person downloading it."),

            H("Assign a task and give it a due date"),
            P("In a checklist item, type **@** and pick a person to assign the task, and **//** to give it a due date. An empty checklist item hints at both: **Type @ to assign the task, // for a due date**."),
            SHOT("page-tasks.png", "A checklist of tasks, each with its assignee and due date, one of them overdue"),
            UL([
                "The first person mentioned in a task is its **assignee**, and its first date its **due date**. Other mentions and dates are part of its text.",
                "An open task whose date has passed shows its date in the overdue colour, and **due today** on the day. Done tasks show their dates as they are.",
                "A mentioned person gets the usual [mention](profile-and-notifications.html#mentions) alert; there is no separate alert for being assigned.",
                "Tasks of a page count once the page is published: a task report lists the tasks of each page's latest published version.",
            ]),

            H("Task report"),
            P("**/tasks** (or **/task report**) inserts a **Task report**, which lists tasks from the published pages you choose: each task's text, its due date, its assignee and its page. Open a task's page to tick it."),
            SHOT("page-task-report.png", "A task report of open tasks in two spaces, by due date: text, due date, assignee and page"),
            TABLE(["Setting", "Choices"], [
                ["**From**", "**This space**, **Every space the reader can read**, or **These spaces** (up to 5 space keys)"],
                ["**Label (optional)**", "Only tasks on pages with this label"],
                ["**Assigned to**", "**Anyone**, **The person reading** (each reader sees their own tasks), or **Someone in particular** (find them by name)"],
                ["**Tasks**", "**Open** (the default) or **Done**"],
                ["**Sort by**", "**By due date** (tasks without a date last) or **By page**"],
                ["**How many**", "10, 20 (the default) or 40"],
            ]),
            UL([
                "A report lists tasks of pages only, not of blog posts, and only pages the reader may read (not locked pages they aren't on, drafts or trashed pages).",
                "Names of assignees show only to readers who may see people in the space. To others, a report of **Someone in particular** isn't shown at all.",
                "Visitors who aren't signed in see **Sign in to see the tasks assigned to you** in a report of **The person reading**.",
                "Tasks can't be ticked from the report yet.",
                "A report shares the limit of six lists a page with [Pages by label and Blog posts](lists-of-pages.html#limits).",
            ]),
            P("In a page downloaded as Word or PDF, a report prints as lines (☐ or ☑, the task linked to its page, due date, assignee, page). Confluence **Action items** keep their assignee and due date when [imported](confluence-import.html#how-confluence-macros-are-imported), and a **Task report** macro becomes a task report."),
            NOTE("When someone's personal data is erased, their tasks lose their assignee in reports. Their personal data export lists the tasks assigned to them."),
        ])),

    # ------------------------------------------------------------------
    ("link-cards", dict(
        label="Link cards", title="Link cards and link previews", icon="link",
        desc="Show a link as a card with its title, description and site, filled in from the linked page when link previews are on",
        keywords=["link card", "card", "smart link", "bookmark", "preview", "link preview", "unfurl", "url", "embed", "widget", "iframe",
                  "blocked hosts", "og:title"],
        blocks=[
            H("Overview"),
            P("A **Link card** shows a link as a box with a title, a short description and the site's name, so readers see where it goes before they follow it. Insert one with **/link card**."),
            SHOT("page-link-card.png", "A link card: the title, the description and the site name of a page on another site"),

            H("Add a link card"),
            STEPS([
                "Insert it|Type **/link card** (or **/card**, **/bookmark**).",
                "Give the link|A web address (`https://…`) or a path on this wiki (`/spaces/…`).",
                "Fill it in|**Fill in from the page** reads the linked page's title, description and site name, when your administrator has turned link previews on. Otherwise, or if the page can't be read, type them yourself.",
                "Check and save|Change anything the page gave; **Description** and **Site name** are optional. **Add** puts the card in the page.",
            ]),
            UL([
                "Select a card to change it (**Change the link card**), remove it, or **Turn into a link**: the card becomes an ordinary link with its title as text.",
                "The card keeps the text it was saved with: readers never make the Wiki or their browser read the other site, and the card shows no picture or icon from it. To refresh the text, change the card and fill it in again.",
                "A card to another site opens it in a new tab; a card to a wiki page opens it in the same tab.",
                "A title has up to 200 characters, a description 300 and a site name 100. A page holds up to 100 link cards.",
            ]),
            P("Word and PDF downloads print a card as a box with its linked title, description, site and address. Confluence **Smart links** shown as cards, **Widget connector** and **iframe** macros become link cards when [imported](confluence-import.html#how-confluence-macros-are-imported), or videos when they show YouTube or Vimeo."),

            H("Link previews"),
            P("Filling in a card from the linked page needs **link previews**, which are off until an administrator turns them on in **Settings → Security → Link previews** (`settings:write`)."),
            SHOT("settings-security-link-previews.png", "Settings → Security → Link previews: on, with two hosts that are never fetched"),
            TABLE(["Setting", "Default", "Effect"], [
                ["**Fill in link cards from the linked page**", "Off", "Off: editors type the title and description themselves."],
                ["**Hosts never fetched**", "None", "Pages on these hosts are never read for a preview, such as `intranet.example.com`. Start with `*.` to include every subdomain (`*.intranet.example.com`). Up to 100."],
            ]),
            P("How a preview is read:"),
            UL([
                "Only the Wiki's server reads the page, never a reader's browser, and only when an editor asks for it.",
                "Private, internal and loopback addresses are never read, nor addresses that lead to one through a redirect, whatever the blocked list says.",
                "Only `http` and `https` on their usual ports, at most 3 redirects, 5 seconds and the first 512 KB of the page. The page's title, description and site name are read; images and site icons never are.",
                "Pages that aren't HTML in UTF-8 can't be read, and **Couldn't read that page** asks the editor to type the text. It never says why, so a preview can't be used to probe your network.",
                "Answers are kept for a day. Each person may ask for 20 previews a minute, and only in spaces where they edit pages.",
            ]),
            P("Changing the setting raises `link_previews.update`, which a [policy](policies.html) can refuse, and is in the audit log."),

            H("API"),
            TABLE(["Method", "Path", "Who", "What"], [
                ["GET", "`/api/wiki/link-previews`", "Signed in", "Whether previews are on; the blocked hosts for `settings:write`"],
                ["PUT", "`/api/wiki/link-previews`", "`settings:write`", "`{enabled, blockedHosts}`"],
                ["POST", "`/api/wiki/link-preview`", "Edit pages of the space", "`{space, url}`: the page's title, description and site name. Refused with `link_previews_off`, `invalid_link` or `preview_unavailable`"],
            ]),
        ])),
    # ------------------------------------------------------------------
    ("slides", dict(
        label="Slides", title="Slides", icon="presentation",
        desc="Put a slide deck in a page, an HTML deck from an AI tool, reveal.js or Marp, or a PDF, and present it full screen",
        keywords=["slides", "slide deck", "deck", "presentation", "present", "full screen", "fullscreen", "reveal.js", "marp", "html deck",
                  "pdf deck", "powerpoint", "pptx", "keynote", "slideshow", "sandbox", "ai tool"],
        blocks=[
            H("Overview"),
            P("A **Slides** block puts a slide deck in a page: an HTML deck, such as the ones AI tools, reveal.js or Marp write, or a deck exported as PDF. Readers step through it under the page's text with the Wiki's own controls, or press **Present** to show it full screen."),
            SHOT("slides-reading.png", "A page with an HTML deck: the deck's title slide, the controls below it and the caption"),
            UL([
                "Below the deck: previous and next, the slide counter (**3 / 12**), a progress bar, **Present** and **Open in new tab**. Once the deck has focus, the arrow keys work too.",
                "An HTML deck shows its title and first lines until someone presses play; only then does the deck load and run.",
                "Under it, the caption: the title the editor gave it, the kind of deck and its slide count.",
            ]),

            H("Add a deck"),
            P("People who edit a page can add decks, unless an administrator has kept them to space admins ([below](#for-administrators))."),
            SHOT("slides-insert.png", "Adding a deck: \"/\" on an empty line and Slides, then the Add slides dialog with an HTML deck that has 12 slides"),
            STEPS([
                "Insert it|Type **/** on an empty line and pick **Slides**, or use **Insert → Slides**. Dropping a `.html` file on the page opens the same dialog.",
                "Give the deck|**Upload a file** takes an `.html` or `.pdf` file, up to the size your administrator allows (20 MB unless changed). **Paste HTML** takes the deck's HTML, for example straight from an AI tool.",
                "Check what was found|The Wiki reads the deck and says how many slides it found and how (reveal.js, Marp, one element per slide). A deck whose slides it can't tell apart still plays with its own keys; the counter then shows a dash.",
                "Title and insert|Change the title if you like (it is shown under the deck, found by search and printed in exports), then **Insert**.",
            ]),
            NOTE("PowerPoint, Keynote and OpenDocument decks (`.pptx`, `.ppt`, `.key`, `.odp`) aren't taken: export them as PDF from your slide tool and add the PDF. Attach the original file with a [File block](files-and-attachments.html) if people need it."),

            H("Change a deck"),
            P("In the editor a deck is shown as a still: it doesn't run while you type. Select it for a bar with settings, present, download and remove."),
            SHOT("slides-editor.png", "A selected deck in the editor with its bar and the Slides settings panel"),
            TABLE(["Setting", "What it does"], [
                ["**Title**", "Shown under the deck, in search and in exports."],
                ["**Start slide**", "The slide readers see first, such as the agenda of a long deck."],
                ["**Replace file**", "Uploads a new version of the deck in its place, of the same kind (an HTML deck for an HTML deck, a PDF for a PDF): the block keeps its file, and published versions of the page keep showing the deck they were published with. A deck of the other kind is added as a new file. See [Versions of a file](files-and-attachments.html#versions-of-a-file)."],
                ["**Download**", "The deck's file, as it was uploaded."],
            ]),
            P("The maximize button in the bar plays the deck full screen, so you can check it without leaving the editor."),

            H("Present"),
            P("**Present** shows the deck on the whole screen. A thin bar at the top shows how far through the deck you are; the controls at the bottom fade after 2 seconds and come back when the pointer moves or a key is pressed. **←**, **→** or **Space** move, **Home** and **End** jump to the first and last slide, and **Esc** leaves."),
            SHOT("slides-fullscreen.png", "A deck presented full screen: the slide, the progress bar, the controls and the key hints"),

            H("PDF decks"),
            P("A PDF deck is shown by the Wiki's own PDF viewer, one page a slide, with a strip of page thumbnails below the controls: click one to jump to it. Nothing in a PDF runs, so it is the safest kind of deck."),
            SHOT("slides-pdf.png", "A PDF deck on slide 3 of 18, with the thumbnail strip"),

            H("On a phone"),
            P("On a phone the deck is as wide as the screen. Swipe to move between slides (a hint says so the first time), and the full-screen button turns it to landscape where the phone allows."),
            SHOT("slides-phone.png", "A deck on a phone: full width, with dots, the counter and the full-screen button"),

            H("What HTML decks can do"),
            P("An HTML deck runs in a sandbox, like an [HTML block](macros.html#html-blocks):"),
            UL([
                "It can't read the Wiki, its cookies or the page around it, can't submit forms or open pop-ups, and never acts as the person reading it.",
                "It can load scripts, styles and fonts only from the hosts your administrator lists in **Settings → Security → Slides**, and from nowhere else. Anything else it needs must be in the file.",
                "The Wiki draws the controls outside the deck and steps it with messages the deck can't use for anything else.",
                "A deck shows only in a page: an HTML file attached to a page any other way is never served as a page.",
            ]),
            P("Readers are whoever can read the page, visitors who aren't signed in included on public spaces. Word and PDF downloads print the deck's title, its kind and slide count in its place. Copying a page or starting one from a template keeps its decks."),

            H("For administrators"),
            P("**Settings → Security → Slides** (`settings:write`) sets who adds decks, the largest deck and the hosts HTML decks may load from. Save with the Security page's Save bar."),
            SHOT("slides-settings.png", "Settings → Security → Slides: page editors add decks, 20 MB, the five default library hosts"),
            TABLE(["Setting", "Default", "Effect"], [
                ["**Who may add Slides blocks**", "Page editors", "**Page editors**: anyone who can edit the page adds, replaces or removes a deck. **Space admins only**: like HTML blocks. Everyone else can still read and present decks."],
                ["**Largest deck**", "20 MB", "1 to 100 MB. Decks are page attachments and count toward the attachment storage."],
                ["**Slides libraries**", "`cdnjs.cloudflare.com`, `cdn.jsdelivr.net`, `unpkg.com`, `fonts.googleapis.com`, `fonts.gstatic.com`", "The only hosts HTML decks may load scripts, styles and fonts from, up to 20. Empty the list to allow none: decks then show only what they carry. **Restore the defaults** brings back the five."],
            ]),
            P("Adding a deck raises the blocking `page.slides.create` event, so a [policy](policies.html) can, for example, refuse HTML decks in some spaces; changing the setting raises `slides_settings.update`. Both are in the audit log. See [Events](events.html)."),
            P("Confluence imports need nothing new: Confluence has no slides macro, so PowerPoint and PDF files stay file cards, and an editor can replace a PDF's card with a Slides block."),

            H("API"),
            TABLE(["Method", "Path", "Who", "What"], [
                ["GET", "`/api/spaces/{key}/slides`", "Read the space", "Whether you may add decks here (`mayAdd`), the largest deck (`maxBytes`), and the library hosts for people who edit pages"],
                ["POST", "`/api/spaces/{key}/pages/{id}/slides`", "`mayAdd`", "Multipart `file`: an HTML file or a PDF; a `replace` field (one of the page's decks) before it makes it a new version of that deck. Answers what was found: `attachment`, `version`, `format`, `engine`, `slides`, `texts`, `title`. Refused with `slides_not_allowed`, `unsupported_deck` or `deck_too_large`"],
                ["GET", "`/api/spaces/{key}/pages/{id}/slides/{attachment}/frame`", "Read the page", "An HTML deck as the sandboxed page the block frames; `not_a_deck` for a file not added as a deck"],
                ["GET", "`/api/wiki/slides-settings`", "`settings:write`", "`{editors, maxMb, hosts}`"],
                ["PUT", "`/api/wiki/slides-settings`", "`settings:write`", "`{editors, maxMb, hosts}`; `editors` is `page_editors` or `space_admins`. Refused with `invalid_slides_editors`, `invalid_slides_max_size`, `invalid_slides_host` or `too_many_slides_hosts`"],
            ]),
        ])),
]
