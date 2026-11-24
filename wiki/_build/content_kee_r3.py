"""Wiki doc pages for Kee release 3: the writing helpers (style review, action
items, diagrams, tables), title and label suggestions, the duplicate page
warning with its merge proposal, images (describe with Kee, images in Ask
Kee), the weekly space digest, the Search tab with search by meaning, and
tidying the pages a Confluence import made (kee/cleanup.go,
components/kee/cleanup).
Facts come from the depotex repo: apps/wiki/backend/internal/kee (helpers,
suggest, duplicates, digest, imageprep), internal/pagesearch, internal/tools
(admin.go), their screens in apps/wiki/frontend/src/components/kee and
components/pages/editor/kee/helpers, and the developer guides (wiki,
wiki-page-search, wiki-attachment-text, wiki-outside-apps). Only what is
built is described."""
from engine import H, P, UL, TABLE, NOTE, WARN, STEPS, SHOT

KEE_R3_USER = [
    # ----------------------------------------------------- kee-writing-helpers
    ("kee-writing-helpers", dict(
        label="Kee's writing helpers", title="Kee's writing helpers", icon="zap",
        desc="Review a section against the space's style guide, turn meeting notes into action items, draw a diagram from text, and make, fill, summarise or ask about tables with Kee",
        keywords=["kee", "ai", "writing helpers", "style guide", "style review", "house style", "review against the style guide", "action items", "meeting notes", "tasks", "owners", "due dates", "diagram", "mermaid", "flowchart", "draft a diagram", "table", "make a table", "add a column", "fill empty cells", "summarise the table", "ask about the table"],
        blocks=[
            P("Besides rewriting, Kee has four helpers in the editor: a review against your space's style guide, action items from meeting notes, a diagram drawn from text, and help with tables. You find them in a section's menu, in Kee's group under the rewrites. Each one shows its result in a panel under the section first: nothing changes on the page until you choose to apply or insert it, and one **Undo** takes it back off."),
            NOTE("You need to be able to edit the page, Kee must be on for you and in the space, and the **Writing help in the editor** feature must be on. Each helper's run counts as one request against your [daily limit](kee.html#your-daily-limit)."),
            TABLE(["Helper", "In the menu of", "What you get"], [
                ["**Review against the style guide**", "A text or heading section, when the space has a style guide", "Findings, each with a suggested change you apply or dismiss one by one"],
                ["**Turn into action items**", "A text section", "A task list to insert below"],
                ["**Draft a diagram…**", "A text or heading section", "A diagram (Mermaid) to insert below"],
                ["**Make a table**", "A text section", "The section as a table, in its place"],
                ["**Add a column…**, **Fill empty cells**", "A table", "The table with a new column, or its empty cells filled, in its place"],
                ["**Summarise the table**, **Ask about the table…**", "A table", "Text to insert below the table"],
            ]),
            P("Select some words in a paragraph, then the **Kee** button beside them: its panel also offers **Draft a diagram**, **Action items** and **Make a table** for just those words. The result is then inserted below."),
            H("Review against the style guide"),
            P("A space's admins can choose one published page of the space as its **style guide**: a page that lists your writing rules, such as \"Use plain words\" or \"Write dates with the year\". Kee checks a section against that page, and only that page."),
            STEPS([
                ("Open the page in the editor, rest the pointer on a section and open its menu (the handle at its right).", "page-edit.section-menu"),
                "Select **Review against the style guide**. Kee reads the section against the guide.",
                ("Read each finding: the rule it breaks and the change Kee suggests. Select **Apply** to make that change in the page, or **Dismiss** to leave it.", "page-edit.ai-findings"),
                "Select **Done** when you have gone through them, or **Try again** for a new review.",
            ], howto="review-a-section-against-the-style-guide", task="Review a section against the space's style guide with Kee"),
            SHOT("kee-helper-review.png", "Style review under a section: checked against House style, three findings with the suggested change marked, each with Apply and Dismiss, then Done and Try again"),
            UL([
                "The item is in the menu only while the space names a style guide. If the guide page was deleted, unpublished or locked away from you, the review says it can't be read.",
                "Kee reads the guide with your own access, every time. A very long guide is read in part: the panel says so.",
                "A finding whose text changed since Kee read it says **This text has changed, so the suggestion can't be applied.** Run the review again.",
                "Some findings suggest removing text: their button says **Remove this text**.",
                "Findings are never posted as comments, and nothing is kept once you close the panel.",
            ]),
            H("Choose the style guide (space admins)"),
            STEPS([
                ("Open the space and select **Space settings** in its sidebar.", "space-rail.settings"),
                ("Open the **Kee** tab.", "space-tabs.ai"),
                ("Under **Style guide**, choose a published page of this space. **Choose another page** changes it and **Remove** takes it away.", "space-ai.style-guide"),
            ], howto="choose-a-style-guide-for-a-space", task="Choose the style guide page Kee reviews a space's pages against"),
            SHOT("kee-style-guide-setting.png", "A space's Kee tab: Kee works in this space, Tell readers when a page holds text written with Kee, and Style guide: House style with Choose another page and Remove"),
            P("A good guide page is short and lists one rule a line, with an example of each. Only a published page of the same space can be the guide; a draft or another space's page is refused. Changing it raises `space.ai_settings.update` with the page chosen and the one before."),
            H("Meeting notes to action items"),
            STEPS([
                ("Open a section of notes in the editor and open its menu (the handle at its right).", "page-edit.section-menu"),
                "Select **Turn into action items**. Kee lists the tasks the notes give.",
                "Check each task, its owner and its date.",
                "Select **Insert below** to add them as a task list under the notes, **Discard** to drop them, or **Try again**.",
            ], howto="turn-meeting-notes-into-action-items", task="Turn meeting notes into action items with owners and due dates"),
            SHOT("kee-helper-items.png", "Action items from meeting notes: Update the runbook for Mira Okafor due Nov 27, 2026, Check the alert thresholds for Tom Reyes, Order the new badges with no owner, and Insert below"),
            UL([
                "An owner is only a person the notes name, and only when exactly one person you may mention matches that name; otherwise the name stays as text. Nobody is made up.",
                "A date is only one the notes give. \"By Friday\" becomes the date of that Friday.",
                "A task nobody was named for has no owner. The inserted tasks work like any [task](tasks.html): the mention is the assignee, the date the due date.",
            ]),
            H("A diagram from text"),
            STEPS([
                ("Open the menu of the section that describes the steps (the handle at its right).", "page-edit.section-menu"),
                "Select **Draft a diagram…**. Under **What to draw (optional)**, say what you want, for example \"a flowchart of the steps\", then **Draft**.",
                "Look at the diagram drawn in the panel.",
                "Select **Insert below** to add it as a Mermaid diagram under the section, or **Discard**.",
            ], howto="draw-a-diagram-from-text", task="Draw a diagram from a section's text with Kee"),
            SHOT("kee-helper-diagram.png", "The Diagram panel under a section: a flowchart of the release steps drawn from its text"),
            P("The diagram is checked before you see it. When it can't be drawn, Kee corrects it once; if it still can't be drawn the panel says **The diagram couldn't be drawn** and nothing is inserted. The diagram is an ordinary [Mermaid block](macros.html): edit its text afterwards like any other."),
            H("Tables"),
            STEPS([
                ("Open the menu of a text section, or of a table (the handle at its right).", "page-edit.section-menu"),
                "On text, select **Make a table**. On a table, select **Add a column…** (and say which column, for example \"the owner of each row\"), **Fill empty cells**, **Summarise the table** or **Ask about the table…** (and type your question).",
                "Read the result in the panel.",
                "Select **Replace** to put a new table in place of the old one, or **Insert below** for a summary or an answer. **Keep original** or **Discard** leaves the page as it was.",
            ], howto="make-or-change-a-table-with-kee", task="Make a table, add a column, fill empty cells, summarise or ask about a table with Kee"),
            SHOT("kee-helper-table.png", "A table of regions by quarter with Kee's summary of it in the Table panel underneath"),
            UL([
                "Kee works on real tables of the editor. A new column is checked to be exactly one more column; a fill only changes cells that were empty.",
                "When the table doesn't make any empty cell clear, the panel says **Nothing to fill** and the table stays as it was.",
                "Tables have no **Ask for more changes**. To change a result, run the helper again.",
            ]),
            H("Good to know"),
            UL([
                "The helpers use the same model picker, limits and notices as the rewrites (see [Writing with Kee](kee-editor.html)).",
                "A version with text applied from a helper is marked **with Kee** in the page history, like a rewrite.",
                "The section menu now opens above its handle when there is more room there, and scrolls when it is long.",
                "Nothing of a helper is available in a space where Kee is off.",
            ]),
        ])),

    # ------------------------------------------------------- kee-suggestions
    ("kee-suggestions", dict(
        label="Titles, labels & duplicates", title="Titles, labels and duplicate pages", icon="tag",
        desc="Let Kee suggest a title or labels for the page you are editing, see when a new page may already exist, and merge it into the other page through a proposal",
        keywords=["kee", "ai", "suggest a title", "title suggestions", "suggest labels", "label suggestions", "duplicate", "duplicate page", "this page may already exist", "merge", "merge pages", "not a duplicate"],
        blocks=[
            P("While you edit a page, Kee can suggest a title and labels from its text, and tell you when a new page covers the same subject as a page that already exists. Kee only suggests: nothing changes until you pick a suggestion or apply a merge."),
            H("Suggest a title"),
            STEPS([
                ("Open the page and select **Edit**.", "page.edit"),
                ("Under the title, select **Suggest a title**. Kee reads the page and offers three titles.", "page-edit.suggest-title"),
                "Select one to use it as the title, or close the suggestions with the cross. The title doesn't change until you pick one.",
            ], howto="suggest-a-title", task="Have Kee suggest a title for a page"),
            SHOT("kee-suggest-editor.png", "The editor with Suggest a title under the page's title and Suggest labels under the label field in Page details"),
            H("Suggest labels"),
            STEPS([
                ("Open the page and select **Edit**.", "page.edit"),
                ("Open **Page details**, the side panel of the editor, if it is hidden.", "page-edit.details"),
                ("Under **Labels**, select **Suggest labels**. Kee offers up to five labels.", "page-edit.suggest-labels"),
                "Select a label to add it to the page. The others stay offered until you close them.",
            ], howto="suggest-labels-for-a-page", task="Have Kee suggest labels for a page"),
            SHOT("kee-suggest.png", "Three suggested titles under the title, and suggested labels (tls, certificates, runbook, gateway, operations) under the label field"),
            UL([
                "Suggestions come from the title and the first part of the page's text. Labels the space already uses are preferred.",
                "Asking again while the text hasn't changed gives the same suggestions at once: nothing is sent and nothing counts against your limit. A new suggestion counts as one request.",
                "An empty page has nothing to suggest from: write some text first.",
                "The **Title and label suggestions** feature is on once Kee is on. An administrator can turn it off.",
            ]),
            H("This page may already exist"),
            P("When you give a new page its title, Kee looks for pages you can read on the same subject. If it finds some, a box under the title says **This page may already exist**, with up to three pages, each with why Kee thinks so. It never stops you from writing or publishing your page."),
            SHOT("kee-duplicates-warning.png", "This page may already exist under a new page's title: Certificate rotation runbook in Operations, why both pages cover the same subject, and Merge this page into it"),
            UL([
                "It is shown only for a page that was never published, in the editor, and only when an administrator turned on the **Duplicate page warning** feature (it is off by default).",
                "It names only pages you can read: never a page under a page lock, a draft, a whiteboard or blog post, or a page of a space where Kee is off.",
                "Kee first finds pages with similar words; only when there are some does it ask the model which really cover the same subject. When nothing is similar, nothing is sent and nothing counts.",
                "**Not a duplicate** (the cross) closes the box. If the check fails, nothing is shown.",
                "A page made by Ask Kee or by an outside AI app isn't checked.",
            ]),
            H("Merge into the other page"),
            STEPS([
                ("In the box **This page may already exist**, read why Kee thinks the pages cover the same subject.", "page-edit.duplicates"),
                ("Select **Merge this page into it**. Kee writes the other page with both pages' content, as a proposal.", "page-edit.merge"),
                "Read the proposal: **Result** shows the merged page, **Changes** what is new. Select **Apply** to write it into the other page's draft, or **Discard**.",
                "Open the other page in the editor, check it and publish it. Then delete or archive your new page yourself.",
            ], howto="merge-a-duplicate-page", task="Merge a new page into an existing page on the same subject"),
            SHOT("kee-duplicates-proposal.png", "The merge proposal for Certificate rotation runbook: Result with the merged text, Waiting for you, Apply, Open the editor and Discard"),
            UL([
                "**Merge this page into it** is offered only for a page you may edit.",
                "Apply writes into the other page's draft as you, with your permissions and page locks, like any [proposed change](ask-kee.html#proposed-changes). If the other page changed since Kee read it, Apply says so and writes nothing.",
                "Your new page is never changed, archived or redirected. After Apply the box says **This page was not changed. Delete or archive it yourself once the other page holds everything.**",
                "The merge takes the text of your new page. Its images, mentions and embeds are not carried over; the other page keeps its own.",
                "The proposal is also kept in your history in Ask Kee, for 7 days.",
            ]),
            SHOT("kee-duplicates-applied.png", "The proposal applied: the change is in the page's draft, and this page was not changed"),
            P("For administrators: the **Title and label suggestions** and **Duplicate page warning** switches are on **Settings → Kee → Features and access** ([Features and permissions](kee-access.html))."),
        ])),

    # -------------------------------------------------------------- kee-images
    ("kee-images", dict(
        label="Images and Kee", title="Images and Kee", icon="presentation",
        desc="Let Kee propose alt text and a caption for an image, and add images to a question in Ask Kee",
        keywords=["kee", "ai", "images", "image", "alt text", "alternative text", "caption", "describe with kee", "accessibility", "screenshot", "diagram", "ask about an image", "add an image", "picture"],
        blocks=[
            P("Kee can look at images: it proposes alternative text and a caption for an image in a page, and answers questions about images you add to Ask Kee. An image is sent to the model only when you ask, for that one request."),
            NOTE("Both need the **Images** feature, which an administrator turns on (it is off by default), and a model that reads images. If the model can't, Kee says so instead of offering the button."),
            H("Describe an image"),
            STEPS([
                "In the editor, select the image and open **Image settings**.",
                ("Under **Alternative text**, select **Describe with Kee**. Kee looks at the image and the text around it.", "page-edit.describe-image"),
                "Read the proposed **Alternative text** and **Caption**. Select **Use these** to fill them into the fields, or **Dismiss**.",
                "Change the text if you need to, then select **Apply** in the dialog. Publish the page as usual.",
            ], howto="describe-an-image-with-kee", task="Have Kee write alternative text and a caption for an image"),
            SHOT("kee-describe-image.png", "The image dialog: Describe with Kee, the proposed alternative text and caption, Dismiss and Use these"),
            UL([
                "Nothing changes until you select **Use these**, and nothing is saved until you apply the dialog and save the page.",
                "Alternative text is at most 150 characters and a caption at most 120: a longer answer is shortened to whole sentences, or at a word with \"…\".",
                "When the image looks decorative, Kee says so and proposes no alternative text.",
                "Kee never names the people in an image.",
                "You need to be able to edit the page. Page locks apply.",
                "If the model can't read images, the dialog says **… can't look at images**: ask your administrator for a model that does.",
                "Each description counts as one request against your daily limit.",
            ]),
            H("Ask Kee about an image"),
            STEPS([
                ("Open **Ask Kee** from the top bar, on the page with the image if it is in a page.", "header.ask"),
                ("Select **Add an image**. Pick one of the images under **On this page**, or **From your device**.", "ask.add-image"),
                ("Type your question and send it. The image goes with that question only.", "ask.input"),
            ], howto="ask-kee-about-an-image", task="Ask Kee a question about an image or a screenshot"),
            SHOT("kee-ask-images-picker.png", "Add an image in Ask Kee: the images on this page, From your device, and that images go with this question only and are not stored"),
            UL([
                "Up to four images a question: images attached to the page you opened Ask Kee on (read with your access), or one picture from your device (PNG, JPEG, GIF or WebP, up to 5 MB).",
                "Images are never stored. Your question keeps only their names (**With …** under it), and follow-up questions don't send them again.",
                "When the chosen model can't read images, the panel says so and you can't send. With an agent that always uses its own model, the server decides.",
                "The image is made smaller and its hidden details (camera, place, time) are removed before it is sent.",
                "Asking with images counts like any question.",
            ]),
            SHOT("kee-ask-image-answer.png", "An answer about the release pipeline diagram added to the question, with the page as its source"),
            H("Spreadsheets attached to pages"),
            P("Ask Kee also reads Excel workbooks (`.xlsx`) attached to pages, like PDF and Word files: every sheet, row by row. See [What Kee can read](ask-kee.html#what-kee-can-read)."),
        ])),

    # ------------------------------------------------------ kee-import-cleanup
    ("kee-import-cleanup", dict(
        label="Tidy imported pages", title="Tidy imported pages with Kee", icon="file",
        desc="After a Confluence import, Kee finds pages with blocks that did not come across, empty layout, uneven headings and links that had no target, and proposes a tidy-up for each page that you review and apply",
        keywords=["kee", "ai", "import", "confluence", "import cleanup", "tidy", "tidy the imported pages", "imported blocks", "macros", "headings", "missing links", "restore links", "prepare all", "review queue", "proposal", "apply"],
        blocks=[
            P("An import from Confluence brings pages across as well as it can, but some things are left behind: blocks of the other wiki that have no match here, empty layout, headings that skip levels, and links to pages that weren't imported yet. Under a finished import, Kee can find those pages and propose a tidied version of each. Nothing changes until you apply a proposal."),
            NOTE("You need the permission to import into the space (the space's **Import** tab) and to edit each page. Kee must be on for you and in the space, and the **Import cleanup** and **Ask Kee** features must be on. Only imports run since this feature arrived (2026-11-23) can be tidied: older imports did not keep the list of pages they made. Mirror syncs are not included."),
            H("What Kee looks for"),
            P("Finding the pages costs nothing: no text is sent to the model and nothing counts against your limit. Each page shows what was found:"),
            TABLE(["Shown as", "What it means"], [
                ["**Imported blocks**", "Confluence macros that were kept as imported blocks, with their names. Kee writes their text into the page in plain Wiki content where it can"],
                ["**Layout problems**", "Runs of empty paragraphs and headings with no words"],
                ["**Headings to fix**", "Top-level headings inside the page, headings that skip a level, and a first heading that repeats the page's title"],
                ["**Links to restore**", "Text that was a link in Confluence whose target was missing at import time, and which now exists and you can read (in the same space, or in a space imported later)"],
            ]),
            P("A page Kee can't tidy for you says why: you can't edit it, it is locked, it has changes that are not published yet, or it is too long."),
            SHOT("kee-import-cleanup-found.png", "Tidy the imported pages: two pages could be tidied, Deploying the API with two imported blocks, three headings to fix and a link to restore, and Service owners with two headings to fix"),
            H("Tidy the pages"),
            STEPS([
                ("Open the space and select **Space settings** in its sidebar, then the **Import** tab.", "space-rail.settings"),
                ("Under a finished import, in **Tidy the imported pages**, select **Find pages to tidy**. Kee lists the pages it made that could be tidied, with what was found on each.", "space-import.cleanup-find"),
                ("Select **Prepare N proposals** to have Kee prepare a tidy-up for every page, one after another, or **Propose a tidy-up** under one page. **Stop** stops preparing after the page in progress.", "space-import.cleanup-all"),
                ("Select **Review N proposals**. Each proposal shows the tidied page (**Result**) and what changes (**Changes**).", "space-import.cleanup-review"),
                "Select **Apply** to publish the tidied page as a new version, **Open the editor** to change it first, or **Discard**. The next proposal follows; **Back to the list** returns to the pages.",
            ], howto="tidy-imported-pages-with-kee", task="Tidy the pages a Confluence import made with Kee, and apply the proposals"),
            SHOT("kee-import-cleanup-proposed.png", "After preparing: Review 1 proposal, Deploying the API waiting for review, and Service owners still to propose"),
            SHOT("kee-import-cleanup-review.png", "The review queue: proposal 1 of 1 for Deploying the API, the tidied page with its restored links, and Apply, Open the editor and Discard"),
            H("Good to know"),
            UL([
                "Applying publishes the page: imported pages are published pages, so the tidied text becomes their next version, under your name, marked as made with Kee. **Page history** can show or restore the version before.",
                "A proposal is checked again when you apply it: if someone changed the page since, it shows **Out of date** and nothing is written. Prepare it again.",
                "Your proposals are yours: other people who may import see their own list and their own proposals.",
                "Each prepared proposal counts as one request against your [daily limit](kee.html#your-daily-limit). **Prepare N proposals** stops when your limit or the installation's budget is reached, or when the provider is down.",
                "Kee only tidies: it keeps the page's facts and wording, and doesn't change pages you didn't ask about. Links are restored only to pages you can read.",
                "A page that has been tidied and applied leaves the list.",
            ]),
        ])),
]

KEE_R3_SHARED = [
    # --------------------------------------------------------- kee-space-digest
    ("kee-space-digest", dict(
        label="Space digest", title="The weekly space digest", icon="calendar",
        desc="Once a week Kee sums up what was new or changed in a space, with the decisions and open questions its pages record, on the space's overview",
        keywords=["kee", "ai", "digest", "space digest", "weekly digest", "this week in the space", "what changed", "decisions", "open questions", "overview", "scheduled help"],
        blocks=[
            P("The space digest is a short summary of the week in a space: the pages that were new or changed, what each one says, and the decisions and open questions they record. Kee writes it once a week, on its own, as part of [scheduled help](kee-scheduled-help.html). It is shown at the top of the space's overview as **This week in the space**."),
            SHOT("kee-space-digest.png", "This week in the space on a space's overview: a new page, a new style page with its decisions, and a changed runbook with what changed and what was decided"),
            H("Read the digest"),
            STEPS([
                "Open the space. The digest is on its overview.",
                ("Read **This week in the space**: each page is marked **New** or **Changed**, with a short summary, and **Decided** and **Open questions** where the page records them.", "space.digest"),
                "Select a page's title to open it and check what it really says.",
            ], howto="read-a-spaces-weekly-digest", task="Read the weekly digest of what changed in a space"),
            UL([
                "Each reader sees only the pages they can read now, with their current titles. A page locked or restricted since leaves no trace.",
                "Each item is written from that page alone: it says nothing about another page. Kee can be wrong; open the page before you rely on it.",
                "The digest covers the week before (Monday to Monday, UTC), and is made on Mondays. It is written in the language of the space admin who turned it on.",
                "Nothing of a page under a page lock is ever sent or shown. At most 30 pages a space and week.",
                "When nothing you can read changed, the digest says so.",
                "There is no mail: the digest is on the overview only.",
            ]),
            H("Turn it on for a space (space admins)"),
            P("An administrator first turns on **Space digest** in the **Scheduled help** card ([Scheduled help](kee-scheduled-help.html#turn-it-on-administrators)). Then:"),
            STEPS([
                ("Open the space and select **Space settings** in its sidebar.", "space-rail.settings"),
                ("Open the **Kee** tab.", "space-tabs.ai"),
                ("Under **Scheduled help**, tick **Make a weekly digest of what changed**. It is saved at once.", "space-ai.space-digest"),
            ], howto="turn-on-the-space-digest", task="Turn on the weekly digest for a space"),
            SHOT("kee-space-digest-switch.png", "A space's Kee tab, Scheduled help: Look for pages that are out of date, Suggest this space's pages for new questions, and Make a weekly digest of what changed"),
            P("Changing the switch raises `space.ai_help.update` (with `space_digest`), which a [policy](policies.html) can refuse, and is in the audit log. Unticking it stops a run before the next page."),
            H("What is sent"),
            P("The text of each page published in the week, one page per request, with the paragraphs that changed. Kee reads each page as the space, never pages under a page lock, and never anything of a space where Kee is off. Requests come from the scheduled help budget, not from anyone's daily limit."),
            H("For administrators"),
            TABLE(["What", "Details"], [
                ["Switch", "**Space digest** in the **Scheduled help** card on **Settings → Kee → Features and access**. Off by default"],
                ["Job", "`wiki-ai-space-digest`, Mondays at 07:00. Change its schedule or run it now under **Settings → Scheduler**; `wiki-ai-help-continue` carries the run on"],
                ["Budget", "The monthly budget for scheduled help. When it is spent, the digest waits until next month"],
                ["Kept", "26 weeks, then removed by `wiki-ai-help-cleanup`"],
                ["Event", "`space.ai_digest.create` when a space's digest for a week is done (no text, no titles)"],
            ]),
        ])),
]

KEE_R3_ADMIN = [
    # ---------------------------------------------------------------- kee-search
    ("kee-search", dict(
        label="Search & search by meaning", title="Search and search by meaning", icon="search",
        desc="The index of page text every search uses, and the optional search by meaning: what it needs (the vector extension, an embeddings model), its switch, model, progress, cost and what happens without it",
        keywords=["kee", "ai", "search", "search tab", "full text", "page text", "index", "search by meaning", "semantic search", "embeddings", "embeddings model", "vectors", "pgvector", "vector extension", "create extension"],
        blocks=[
            P("Every search of page text, by people in the search box and by Kee, uses an index of what published pages say. It is built and kept current on its own. On top of it, **search by meaning** lets Kee also find passages that say the same thing in other words. It is optional and needs a database extension and an embeddings model."),
            H("Where it is"),
            P("**Settings → Kee → Search** (**Manage Kee settings**, Pro). The tab shows the index of page text and, where the database offers it, search by meaning. It reads its numbers when you open it and on **Refresh**; it doesn't update by itself."),
            SHOT("kee-settings-search.png", "Settings → Kee → Search on a database server without the vector extension: the index of page text with all pages indexed, and the note that search by meaning needs the extension"),
            H("The index of page text"),
            UL([
                "It holds the text of the newest published version of every page, as Kee reads it (up to about 200,000 characters a page). Drafts and earlier versions aren't in it.",
                "It follows every change within about a minute, on every server. After an upgrade, the first pass fills it in the background: **Pages indexed** shows how far it is. A page not indexed yet is still found by its title.",
                "It is used by the search box (results **In page text**, see [Search](search.html)) and by Ask Kee, agents and outside AI apps (`search_pages`).",
                "Every search is filtered by the person's access before anything is ranked: spaces they can see, published pages, page locks.",
                "It needs nothing from you and no extension.",
            ]),
            H("Search by meaning"),
            P("With search by meaning on, each page is cut into passages (by headings, then paragraphs, up to 40 a page) and each passage gets a **vector** from an embeddings model at your provider. When Kee searches, it also finds the passages closest in meaning to the words it searched for, and mixes them with the word matches."),
            TABLE(["It needs", "Details"], [
                ["The `vector` extension in the database", "The PostgreSQL server must offer the `vector` extension (pgvector), and a database administrator must install it in the Wiki's database: `CREATE EXTENSION vector;`. The Wiki never installs it. The server checks whether it is offered when it starts: restart it after installing the extension's package on the database server"],
                ["An embeddings model", "Added under **Providers and models** with the kind **Embeddings**, from a provider that has an embeddings endpoint. See [Providers and models](kee-providers.html)"],
                ["Its switch", "**Search by meaning** on this tab (also in the **Scheduled help** card). Off by default"],
                ["A budget", "It runs as scheduled work: the monthly budget for scheduled help pays for it, not people's limits"],
                ["Licence", "**Pro**"],
            ]),
            STEPS([
                "Ask a database administrator to install the `vector` extension in the Wiki's database (`CREATE EXTENSION vector;`), then restart the Wiki's servers if the package was just added.",
                "Open **Settings → Kee → Providers and models** and add an embeddings model.",
                "Open the **Search** tab. Under **Search by meaning**, turn the switch on.",
                "Choose the **Embeddings model** and confirm with **Continue**: the text of every page that may have vectors is sent to that model's provider.",
                "Watch **Pages with vectors** grow, with **Refresh**. While it runs, searches use words and the vectors made so far.",
            ], howto="set-up-search-by-meaning", task="Set up search by meaning for Kee"),
            H("What the tab shows"),
            TABLE(["State", "Meaning"], [
                ["**Not available**", "The database server doesn't offer the vector extension. Searches use the words of page text"],
                ["The extension is offered, not installed", "The tab says a database administrator installs it. Until then searches use words"],
                ["**Off**", "The switch is off. Searches use words"],
                ["**No model chosen**", "Choose an embeddings model. Searches use words"],
                ["**Making vectors**", "Pages are being sent. Searches use words and the vectors made so far"],
                ["**Ready**", "Searches by Kee use words and meaning"],
                ["**Stopped for now**", "The tab says why: the scheduled budget is spent, the model is paused or gone, the provider didn't answer or refused, a policy refused it. It goes on by itself at the next run where it can"],
            ]),
            UL([
                "Also shown: pages with vectors and passages, the vector length, tokens sent so far and the estimated cost (from the model's input price).",
                "Choosing another model asks first: the old vectors are removed and every page is sent to the new model again. **None** stops search by meaning and removes the vectors.",
                "A model paused under **Providers and models** shows **Paused** and stops the work.",
            ]),
            H("Without it"),
            P("Nothing breaks. Whenever any part is missing (the extension, the model, the switch, the licence, the budget or the provider), Kee searches by the words of page text, the same as before it was set up, and nothing is sent."),
            H("What is sent"),
            UL([
                "The text of published pages, cut into passages: never pages under a page lock, and nothing of a space where Kee is off. Vectors of a page are removed when it is deleted, locked, or its space turns Kee off.",
                "The words of each search Kee makes, to find passages close to them. These count against the scheduled budget too.",
                "Nothing of what people type in the search box: it searches words only.",
            ]),
            H("Events, audit and jobs"),
            TABLE(["What", "Details"], [
                ["`wiki.search_settings.update`", "Raised before and after the switch or the model changes; a [policy](policies.html) can refuse it. Audit `wiki_search:update_settings`"],
                ["`wiki-page-search-index`", "Every minute: keeps the index of page text current and fills it after an upgrade. Run now under **Settings → Scheduler**"],
                ["`wiki-page-search-embed`", "Every minute: makes and removes vectors while search by meaning is on"],
            ]),
            H("Limits"),
            UL([
                "There is no approximate vector index: a search compares every passage the person can read, which is fine for most wikis.",
                "Kee's own searches use meaning; the search box uses words only.",
                "The switch here and the one in the Scheduled help card are the same setting; the other tab shows a change after you reload it.",
            ]),
        ])),
]
