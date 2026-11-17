"""Wiki doc pages (user guide, part B): publishing, reviews, history,
comments, editing together, copies and templates, images and videos, labels,
import and export, Q&A, calendar, analytics and phones.

Keep in step with apps/wiki in the depotex repo (internal/pages, collab,
attachments, imports, exports, qna, calendar, analytics and the frontend).
"""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, CODE, SHOT

USER_B = [
    ("drafts-and-publishing", dict(
        label="Drafts &amp; publishing", title="Drafts and Publishing", icon="send",
        desc="Page status, saving as you type, the draft's history, publishing a version and publishing later",
        keywords=["draft", "publish", "status", "in review", "archived", "autosave", "save", "version", "minor change",
                  "schedule", "scheduled publish", "draft history", "snapshot", "preview"],
        blocks=[
            H("Overview"),
            P("Every page has a **draft** that the people who edit it change together, and **versions** that readers see. "
              "Editing never changes what readers see: the draft becomes the next version only when someone publishes it. "
              "Opening a page you may edit (the space's Editor and Admin roles) opens it in the editor; everyone else gets the reading view."),
            SHOT("drafts-and-publishing-editor.png", "A page in the editor: the save state and Publish at the top, and the page's status in Page details"),

            H("Status"),
            P("**Page details**, beside the page (under it on a phone), shows the page's status. Pick another one to change it:"),
            TABLE(["Status", "Who sees the page"], [
                ["**Draft**", "Only people who can edit pages in the space. New pages start here."],
                ["**In review**", "The same as a draft: a sign for the other editors that the page is waiting to be checked. See [Reviews](reviews.html)."],
                ["**Published**", "Everyone who can read the space, at the latest version."],
                ["**Archived**", "Only people who can edit pages, like a draft: the page is kept, out of readers' way."],
            ]),
            P("Picking **Published** opens the publish dialog, because publishing always makes a version. "
              "Under the status a line says what readers see now: nothing until the page is published, or the version they get until you publish again."),

            H("Saving as you type"),
            P("There is no Save button. Every change is saved within moments, and the top of the editor says where it stands:"),
            TABLE(["It says", "Meaning"], [
                ["**All changes saved**", "The server has stored every change you made."],
                ["**Saving…**", "Changes are on their way."],
                ["**Offline. Your changes are kept in this tab and saved when the connection returns.**", "You can keep typing; nothing is lost while the tab stays open."],
                ["**Editing stopped**", "The page can't be edited from this tab any more (it was deleted, your access changed or your session ended). The message says what to do."],
            ]),
            P("If you leave the page before everything is saved, the Wiki keeps sending your changes in the background and warns you before you close the site. "
              "See [Editing together](editing-together.html) for working on a page with other people."),

            H("Preview"),
            P("**Preview** at the top shows the draft as readers will see it once you publish, with heading and figure numbers. **Edit** goes back to the editor."),

            H("Publish a version"),
            STEPS([
                "Select **Publish**|At the top of the editor, or **Published** under the status.",
                "Say what changed (optional)|A short note, such as \"Fixed the escalation steps\", shown with the version in the page's history.",
                "Tick **Minor change, such as a typo** if it is one|People watching the page aren't told about a minor change.",
                "Select **Publish**|The draft becomes the page's next version: version 1, 2, 3 and so on. The dialog waits until your latest changes are saved first.",
            ]),
            SHOT("drafts-and-publishing-publish.png", "The publish dialog: a note about what changed and the minor change box"),
            UL([
                "A page can only be published under published pages: publish the page above it first.",
                "If nothing changed since the last version, there is nothing to publish and the Wiki says so.",
                "Publishing tells the people who watch the page (unless it was minor) and the people the new version mentions for the first time. See [Profile & notifications](profile-and-notifications.html).",
                "Your administrators can set a [policy](policies.html) that a page needs an approved review before it is published.",
            ]),

            H("Publish later"),
            P("Under **Plans** in Page details, **Schedule a publish** publishes the draft as it is now at a time you pick, from a minute to a year ahead, as you, with an optional note and minor change box. "
              "Only members of the space who edit pages can schedule one, and only in the browser."),
            WARN("Any edit to the page after you schedule it, by you or anyone else, cancels the publish: the Wiki publishes exactly the draft you scheduled or nothing. Schedule once the draft is final. If the draft changed, Plans says so and offers **Schedule again**, and you get an alert at the time it would have published."),
            P("**Change time** moves the publish and **Cancel publish** drops it. A page has one scheduled publish at a time. "
              "Scheduled publishes show on the [calendar](calendar.html). They are dropped when you sign out of your other sessions or change your password, and you get an alert when one couldn't be made."),
            SHOT("drafts-and-publishing-plans.png", "Plans in Page details: a page scheduled to publish"),

            H("Draft history"),
            P("Between versions, the Wiki keeps snapshots of the draft: a couple of minutes after people stop editing, and every ten minutes while they keep going. "
              "**Draft history** in Page details lists the newest five, each with **Open**, **Compare** (with the snapshot before) and **Restore**; **All draft snapshots** opens the full list on the page's history page."),
            UL([
                "Each snapshot names who edited since the one before (when you may see people in the space).",
                "**Restore** replaces the draft for everyone editing the page. The draft as it was is kept in the history first, and readers see nothing new until someone publishes.",
                "Snapshots are kept for 30 days, at most 200 per page, and only people who can edit the page see them.",
            ]),
            P("Published versions have their own history, which readers can open too: see [Page history & versions](page-history-and-versions.html)."),
        ])),

    ("reviews", dict(
        label="Reviews", title="Reviews and Review-by Dates", icon="check",
        desc="Ask people to review a draft, approve or ask for changes, and keep pages from going stale",
        keywords=["review", "review request", "approve", "approval", "ask for changes", "reviewer", "due date", "overdue",
                  "review by", "stale", "reminder"],
        blocks=[
            H("Overview"),
            P("A review request asks people who edit the space to read a page's draft and approve it or ask for changes. "
              "Reviews live in **Reviews**, in the editor's Page details: only people who can edit pages in the space see and answer them."),
            SHOT("reviews-section.png", "Reviews in Page details: one reviewer approved, one was asked and the request is due on a date"),

            H("Ask for a review"),
            STEPS([
                "Open the page and find **Reviews**|In Page details, beside the page.",
                "Select **Ask for review**|Search people who edit this space and pick up to 10. You can't ask yourself.",
                "Add a note and a date (both optional)|What the reviewer should look at, and **Review by**: a day up to a year ahead.",
                "Select **Send request**|Each reviewer gets an alert now, and another if the date passes before they answer.",
            ]),
            SHOT("reviews-request.png", "The Ask for a review dialog with a reviewer picked, a note and a date"),
            P("Asking for a review needs permission to see people in the space, because it names them. You can't ask the same person twice while their request is open; "
              "**Cancel request** withdraws one (nobody is told)."),

            H("Answer a request"),
            P("When you are asked, open the page from the alert. Your request shows **Approve** and **Ask for changes**:"),
            UL([
                "**Approve** with an optional note.",
                "**Ask for changes** with a note that says what should change.",
            ]),
            P("The person who asked gets an alert either way. Requests show **Waiting**, **Approved**, **Changes requested** or **Cancelled**, with **Due** or **Overdue since** and a date. "
              "An answer given before the page was last published is marked **Given before the last publish**: it was about an earlier draft."),
            NOTE("Your administrators can require an approval before a page is published, with a [policy](policies.html). Each reviewer counts once, by their latest answer since the last publish."),

            H("On the calendar"),
            P("Open requests show on the [calendar](calendar.html) on the day they are due, as **Review due**."),

            H("Review-by dates"),
            P("A review-by date is a reminder that a page should be checked again by a certain day, so it doesn't go stale. "
              "Under **Plans** in Page details, **Set a review-by date** picks a day up to five years ahead; **Change the date** and **Remove the date** change it. "
              "When the day comes, the person who set it gets an alert. Review-by dates show on the calendar too, and readers see a published page's date there."),
            P("Pages nobody has published in 180 days also show in [content health](analytics.html#content-health)."),
        ])),

    ("page-history-and-versions", dict(
        label="Page history &amp; versions", title="Page History and Versions", icon="history",
        desc="Every published version of a page, compared side by side, and restoring an old one",
        keywords=["history", "versions", "compare", "diff", "difference", "restore", "roll back", "revert", "old version",
                  "changes"],
        blocks=[
            H("Overview"),
            P("Each time a page is published, the Wiki keeps that version for good: its title and content, who published it and when, the note about what changed, and whether it was minor. "
              "Versions are numbered 1, 2, 3 and so on. Readers always see the latest one."),

            H("Versions in the editor"),
            P("**Versions** in Page details lists the newest versions, with **Older versions** for the rest. Each one has:"),
            TABLE(["Button", "What it does"], [
                ["**Open**", "Shows that version as readers saw it."],
                ["**Compare**", "Compares it with the version before."],
                ["**Restore**", "Replaces the draft with that version, for everyone editing the page, and opens the publish dialog. Readers see it once you publish."],
            ]),
            P("Restoring changes only the draft: you can still edit before you publish, or undo it. A version published from a restore says which version it restores, as long as the draft wasn't changed in between."),

            H("Compare two versions"),
            P("**Page history** under the title of a published page (once it has more than one version), or **Page history and comparison** in the editor, opens the page's history. "
              "Readers of the space can open it for published pages; people who edit pages can for every page."),
            SHOT("page-history-and-versions-compare.png", "Page history comparing two versions side by side, with an added and a changed block"),
            UL([
                "Pick the two versions in **Compare** and **With**: by default the newest against the one before.",
                "**Inline** shows the changes in one column, **Side by side** in two (on wider screens).",
                "Added and removed words are marked inside each block, and a change the text doesn't show (an image's caption, a table cell, a box's settings) is named under it.",
                "Unchanged parts are folded; select **Show … unchanged blocks** to see them.",
            ]),
            P("People who edit the page can switch **Show** to **Draft history** to compare snapshots of the draft the same way. See [Drafts & publishing](drafts-and-publishing.html#draft-history)."),

            H("Deleted pages"),
            P("Deleting a page moves it, with the pages under it, to the space's trash, where people who can edit pages can restore it with all its versions until it is removed for good. "
              "See [Pages & the page tree](pages-and-the-page-tree.html)."),
        ])),

    ("comments", dict(
        label="Comments", title="Comments", icon="list",
        desc="Comment on a page or on part of it, reply, mention people and resolve threads",
        keywords=["comment", "comments", "reply", "thread", "inline comment", "resolve", "reopen", "mention", "@"],
        blocks=[
            H("Overview"),
            P("People signed in who can read a page see its comments under it. Anyone with the space's Commenter, Editor or Admin role can comment and reply; Viewers read them."),
            SHOT("comments-threads.png", "Comments under a page: a thread with a reply, and a resolved thread"),

            H("Comment and reply"),
            UL([
                "Write in **Add a comment…** under the page and select **Comment**.",
                "**Reply** answers a thread. Replies go one level deep, up to 50 per thread.",
                "Type **@** to mention someone (when you may see people in the space): they get an alert. Mentions reach only people the space allows.",
                "A comment is plain text, up to 5,000 characters.",
            ]),

            H("Comment on part of a page"),
            P("People who edit the page can comment on text in the editor: select the text, then use the comment button in the toolbar. "
              "The thread shows the text it is about (**On part of the page**), and **Show in the page** finds it. If that text is later removed, the thread says so and stays."),

            H("Resolve, edit and delete"),
            TABLE(["Action", "Who"], [
                ["**Resolve** and **Reopen** a thread", "The person who started it, and anyone who can edit pages in the space"],
                ["**Edit comment**", "The person who wrote it"],
                ["**Delete**", "The person who wrote it, and the space's admins. Deleting a thread's first comment deletes its replies."],
            ]),
            P("**Show comments** switches between **Open**, **Resolved** and **All** threads."),

            H("Alerts"),
            P("A new comment tells the people it mentions, and otherwise the earlier people in the thread and the page's watchers, each once and never the writer. "
              "Editing a comment tells only people newly mentioned in it. See [Alerts](alerts.html)."),
        ])),

    ("editing-together", dict(
        label="Editing together", title="Editing Together", icon="users",
        desc="Several people in one page at once: cursors, who is editing, and what happens offline",
        keywords=["collaboration", "real time", "live", "co-editing", "together", "presence", "cursor", "offline", "connection",
                  "reconnect", "websocket"],
        blocks=[
            H("Overview"),
            P("Everyone who edits a page works on the same draft at the same time. Changes appear for the others as you type, each person's cursor shows with their name, "
              "and nothing anyone writes overwrites someone else's work: changes made at the same moment are merged."),
            SHOT("editing-together-presence.png", "Two people in one page: the other person's cursor with their name, and Editing now in Page details"),
            UL([
                "The faces at the top of the editor, and **Editing now** in Page details, show who else has the page open.",
                "Undo takes back your own changes, not other people's.",
                "Restoring a version or a draft snapshot changes the draft for everyone, as one change.",
            ]),

            H("Who can join"),
            P("People with the space's Editor or Admin role, signed in in the browser. Readers never see the live draft: they see the published version until the next publish. "
              "If your access changes or your session ends while a page is open, editing stops within half a minute and the editor says why."),

            H("When the connection drops"),
            P("You can keep typing. The editor says **Offline. Your changes are kept in this tab and saved when the connection returns.** "
              "When it returns, your changes are sent and merged with what others wrote meanwhile. Keep the tab open until it says **All changes saved**: changes not yet saved live only in that tab."),
            NOTE("If the editor says live editing can't connect, the server's reverse proxy may not pass live connections on. Tell your administrator: the [install guide](install.html) has the setting."),

            H("Limits"),
            P("A page's draft can hold a lot of content, but a single very large change, or a page that has reached its size limit, is refused: the editor stops and asks you to undo the last change or split the content into more pages."),
        ])),

    ("copies-and-templates", dict(
        label="Copies &amp; templates", title="Copies and Templates", icon="file",
        desc="Copy a page into any space you write in, and start new pages from a space's templates",
        keywords=["copy", "duplicate page", "template", "templates", "page template", "save as template", "start from"],
        blocks=[
            H("Copy a page"),
            P("**Copy** in the reading view (or Page details in the editor) makes a new page with this page's content and images:"),
            STEPS([
                "Select **Copy**|Signed in, you can copy any page you can read.",
                "Pick the title, space and place|The title starts as \"… (copy)\". **Space** lists the spaces where you can add pages, and **Put it under** picks a page there or the top level.",
                "Select **Copy page**|The copy starts as a draft.",
            ]),
            UL([
                "If you edit the page, the copy takes its current draft; otherwise the latest published version.",
                "Pages under it aren't copied.",
                "Up to 100 images (256 MB together) are copied with it; the Wiki tells you if some weren't.",
            ]),
            SHOT("copies-and-templates-copy.png", "The Copy dialog: title, space and where the copy goes"),

            H("Start from a template"),
            P("When you create a page, **Start from** lists the space's templates beside **Blank page**. The new page starts with the template's content, which you then edit like any draft. "
              "A page keeps its content when the template changes later."),

            H("Make a template"),
            P("Space admins make templates from a page: **Save as template** in Page details saves the page's draft as it is now, without its images, as a **New template** with a name and an optional description, or replaces an existing one (**Replace one** keeps its name and description)."),
            SHOT("copies-and-templates-save.png", "Save as template: a new template's name and description"),
            P("**Page templates** in the space's Settings tab lists them, with **Edit** (name and description) and **Delete**. A space holds up to 100 templates, with names unique in the space. Deleting one doesn't change pages made from it."),
        ])),

    ("attachments-and-media", dict(
        label="Images &amp; videos", title="Images and Videos", icon="grid",
        desc="Add images with captions and videos (uploaded or from an allowed site) to a page",
        keywords=["image", "images", "picture", "upload", "paste", "drag", "caption", "alt text", "figure", "video", "youtube",
                  "vimeo", "subtitles", "attachment", "attachments", "file"],
        blocks=[
            H("Images"),
            P("Add an image with the image button in the editor's toolbar, by pasting it, or by dropping the file onto the page. PNG, JPEG, GIF and WebP images up to 20 MB are taken, at most 16,384 pixels a side and 50 million in all."),
            P("Select an image to open its settings:"),
            TABLE(["Setting", "What it does"], [
                ["**Alternative text**", "Describes the image for people who can't see it. Leave it empty only for a decorative image."],
                ["**Caption**", "One line under the image. With **Figure numbers** on in Page details, captioned images are numbered Figure 1, Figure 2, … for readers."],
                ["**Width**", "Small (a quarter), Medium (half), Large (three quarters) or Full width."],
                ["**Position**", "Left, Center or Right."],
            ]),
            SHOT("attachments-and-media-image.png", "The image settings dialog: alternative text, caption, width and position"),
            P("**Remove image** takes it out of the draft; readers keep seeing it in the versions that have it. Images pasted from other websites aren't taken: download and add the file."),

            H("Videos"),
            P("Add a video from the toolbar or the **/** menu. **Where the video comes from** is either:"),
            UL([
                "**Upload a file**: MP4 or WebM, up to 200 MB. A poster frame is taken from it when it's added. Add **Subtitles (optional)** as a WebVTT (.vtt) file up to 512 KB, with its language (such as `en` or `pt-BR`). Readers play it in the browser's own player; it plays where the browser supports its format (H.264 MP4 and VP9 WebM play nearly everywhere).",
                "**Link from a video site**: paste a link to a video on a site your administrator allows (YouTube and Vimeo when allowed, and others they add in Settings → Security → Video sites). A YouTube or Vimeo page link is turned into its player, keeping the start time.",
            ]),
            P("Both take a **Caption**, a **Start at** time (m:ss) and a width. In the editor a linked video shows as a card naming its site; readers get the site's player. If a site is taken off the list, its videos show a notice instead."),
            SHOT("attachments-and-media-video.png", "The Video dialog: upload a file or link from an allowed video site"),

            H("Limits"),
            TABLE(["Limit", "Value"], [
                ["Image", "20 MB, 16,384 pixels a side, 50 million pixels"],
                ["Video", "200 MB, MP4 or WebM"],
                ["Subtitles", "512 KB, WebVTT, one track per video"],
                ["Per page", "500 files and 1 GB together"],
            ]),
            NOTE("Only images, videos and subtitles can be added to pages so far. Other files, such as PDFs, come later."),

            H("Who sees them"),
            P("People who edit a page see every image and video in its draft. Readers see only those in a published version of the page."),
        ])),

    ("labels-and-feedback", dict(
        label="Labels &amp; feedback", title="Labels and \"Was this page helpful?\"", icon="tag",
        desc="Label pages across spaces, and tell a page's owner whether it helped",
        keywords=["label", "labels", "tag", "tags", "helpful", "was this page helpful", "like", "dislike", "feedback",
                  "rating", "vote"],
        blocks=[
            H("Labels"),
            P("Labels group pages across spaces, such as `runbook` or `onboarding`. They are shared by the whole Wiki: the same label in two spaces is one label."),
            UL([
                "People who edit a page add labels under **Labels** in Page details: type one and press Enter or a comma, or pick a suggestion. Up to 50 per page.",
                "A label is letters, digits, `-`, `_` or `.`, without spaces, up to 50 characters, and is kept in lower case.",
                "Labels show at the end of a published page. Signed in, select one to see every published page with it, in the spaces you can read.",
                "**Labels** (at `/labels`) finds a label by its first letters.",
            ]),
            SHOT("labels-and-feedback-label-page.png", "A label's page: published pages with the label, with their space"),
            P("Administrators who manage labels see every label there with its page count, and can **Rename** one on every page (renaming to a label that exists merges the two) or **Remove** it from every page."),

            H("Was this page helpful?"),
            P("Under a published page, signed-in readers answer **Was this page helpful?** with **Yes** or **No**, and can change or take back their answer."),
            UL([
                "After **No**, you can say **What’s missing or wrong?** in a note of up to 1,000 characters. The note goes to the page's creator and the space's admins **without your name**; the creator gets an alert.",
                "Everyone sees how many people found the page helpful. Names of people who liked it show to those who may see people in the space.",
                "In the editor, **Was it helpful?** in Page details shows the counts and, for the page's creator and the space's admins, the notes.",
            ]),
            SHOT("labels-and-feedback-helpful.png", "Was this page helpful? after a reader answered No, with the note field"),
            P("Pages marked unhelpful most often show in [content health](analytics.html#content-health)."),
        ])),

    ("import-and-export", dict(
        label="Import &amp; export", title="Import and Export", icon="briefcase",
        desc="Bring Markdown or a Confluence space into a space, and download a page as Word or PDF",
        keywords=["import", "export", "markdown", "md", "zip", "confluence", "word", "docx", "pdf", "download", "print"],
        blocks=[
            H("Download a page as Word or PDF"),
            P("**Download** above a published page offers **Word document (.docx)** or **PDF**. In the editor it is in Page details once the page has a version. "
              "Anyone who can read the page can download it, readers who aren't signed in too."),
            SHOT("import-and-export-download.png", "The Download menu above a page: Word document or PDF"),
            UL([
                "The file holds the published version you are looking at, never the draft: heading and figure numbers, tables of contents, lists, tables, code, boxes, images with captions, and the content of blocks that show other pages you may read.",
                "PNG, JPEG and GIF images are included; other images and videos become a note or a link.",
                "The Word file shows every language. The PDF draws Latin, Greek and Cyrillic text; other scripts and emoji don't show there yet, so use Word for them. Pages are A4.",
                "A very large page can take too long to turn into a file; try again later or download a smaller page. When many people export at once, the Wiki asks you to try again in a moment.",
            ]),

            H("Import Markdown"),
            P("A space's admins import Markdown on the space's **Import** tab: one `.md` file, or a `.zip` of a folder of `.md` files with their images."),
            UL([
                "Each folder becomes a page holding its files' pages; a folder's `index.md`, `README.md` or `_index.md` is that page's text.",
                "A file's title comes from its front matter `title`, else its first top-level heading, else its name. A leading number (`02-setup.md`) sets the order and is left out of the title.",
                "Tables, task lists, strikethrough, links between the files and the images they show are kept. HTML inside the Markdown is left out.",
                "Importing the same folder again into the same space updates the pages it made, except pages edited here since.",
            ]),
            P("The upload is checked first, and nothing is written until you start the import from its report. Each page gets one version."),
            SHOT("import-and-export-report.png", "The Import tab's report for a checked export, before the import starts"),

            H("Import from Confluence"),
            P("A Confluence space export (Space tools → Export, XML, full export, as a `.zip`) is imported the same way, with its page tree, versions, comments, labels, images and videos, and people matched by email. "
              "See [Import from Confluence](confluence-import.html) for the steps and what converts."),
            NOTE("Imports are for the space's admins, and your administrator can turn them off or limit the upload size."),
        ])),

    ("qna", dict(
        label="Q&amp;A", title="Q&amp;A", icon="help",
        desc="Ask your organization a question, answer, vote, accept the answer that worked, and follow topics",
        keywords=["q&a", "qna", "questions", "answers", "ask", "vote", "upvote", "accept", "accepted answer", "tags", "follow",
                  "reputation", "duplicate", "public question", "stack overflow"],
        blocks=[
            H("Overview"),
            P("**Q&A** in the left menu is a place for questions and answers across your organization, separate from spaces. "
              "Everyone in the organization reads, asks, answers and votes; the organization's admins moderate. Answers that help get votes, and the person who asked accepts the one that worked."),
            SHOT("qna-list.png", "The Q&A list: questions with their votes, answers and tags, and the tabs and order"),

            H("Find a question"),
            UL([
                "The tabs show **All**, **Unanswered**, **Mine** and **Following**; **Order** sorts by **Active**, **Newest** or **Most votes**.",
                "Select a tag to see its questions. Questions also come up in the Wiki's [search](search.html).",
            ]),

            H("Ask a question"),
            STEPS([
                "Select **Ask a question**|In Q&A, or **+ Create** at the top of the Wiki.",
                "Write a specific title|10 to 200 characters. While you type, **Questions that may already answer yours** lists similar ones.",
                "Add the details|What you expected, what happened, what you tried. The editor has headings, lists, quotes, code blocks, tables, links and images (paste or add them, up to 20 per post), and **@** mentions people in your organization.",
                "Add up to 5 tags|Lower-case words such as `backups`; suggestions show as you type.",
                "Select **Post question**|You follow it from now on.",
            ]),
            P("Under a published page, **Questions about this page** lists questions that link to it, and **Ask about this page** starts a question with a link to it. "
              "A question lists the **Wiki pages** it links to that you can read."),

            H("Answer, vote and accept"),
            UL([
                "Write in **Your answer** and select **Post answer**. Your answer is saved as a draft while you type and kept for 30 days; **Discard draft** throws it away. Answering follows the question.",
                "Vote a question or an answer up (**This is useful**) or down (**This isn't useful**). You can't vote on your own posts.",
                "The person who asked (or a moderator) selects **Accept this answer** on the one that worked; **Take back the accept** undoes it. One answer is accepted at a time.",
                "Comments under a question or an answer are short notes on one line, up to 600 characters and 30 per post.",
            ]),
            SHOT("qna-question.png", "A question with its votes, an accepted answer and comments"),

            H("Edit, history and delete"),
            P("You edit your own questions, answers and comments. **History** shows what a post said before each edit, to its author and moderators. "
              "You can delete your own question while it has no answers, and your own answers and comments."),

            H("Follow"),
            P("**Follow** on a question tells you about new answers; **Follow tag** on a tag tells you about new questions with it. The **Following** tab lists both. You also get an alert when someone comments on your post, accepts your answer or mentions you."),

            H("Reputation"),
            P("People earn points for posts others find useful: 10 for each vote up and 2 off for each vote down on their questions and answers, and 15 for each accepted answer (not on their own question). "
              "Points show next to names and are counted again every 15 minutes."),

            H("Moderation"),
            P("Moderators (the organization's admins) edit, **Close** and **Reopen**, and delete any post; **Mark as duplicate** points a question to an earlier one (it then takes no answers); **Lock comments**; and merge one tag into another. "
              "See [Q&A moderation](qna-moderation.html)."),

            H("Public questions"),
            P("When your administrators allow anonymous access and the moderators turn on **Allow public questions** in Q&A **Settings**, a question can be a **Public question**: anyone can read it and its answers, even without signing in, at the Wiki's **Public questions** list. People are shown there by name only."),
            UL([
                "The person who asked can make a question public before anyone answers or comments; moderators can at any time.",
                "Signed-out readers can't answer or vote: **Answer or vote in Q&A** sends them to sign in.",
                "Turning the setting off hides every public question again.",
            ]),
        ])),

    ("calendar", dict(
        label="Calendar", title="Calendar", icon="calendar",
        desc="Space calendars with events and leave, scheduled publishes and review dates, and a feed for your calendar app",
        keywords=["calendar", "event", "events", "leave", "holiday", "vacation", "out of office", "repeat", "recurring",
                  "ical", "ics", "subscribe", "outlook", "google calendar", "feed"],
        blocks=[
            H("Overview"),
            P("**Calendar** in the left menu shows what is planned in the spaces you read: events and leave people add, publishes someone scheduled, and reviews and review-by dates."),
            SHOT("calendar-month.png", "The calendar's month view with events, leave and a scheduled publish, and the selected day beside it"),
            UL([
                "**Month**, **Week** and **Agenda** (the next 30 days) change the view; the arrows and **Today** move through time.",
                "Show **All my spaces** or pick one space, and turn kinds of entries on or off.",
                "Select a day to see its entries beside the calendar, and an entry to see its details. On a keyboard, the arrow keys move between days, Home and End to the start and end of the week, and Page Up and Page Down by a month.",
            ]),

            H("What shows"),
            TABLE(["Kind", "Comes from", "Who sees it"], [
                ["**Event**", "People who edit pages in the space", "Everyone who reads the space"],
                ["**Leave**", "People who add leave for themselves", "Everyone who reads the space; who is on leave only to people who may see people in the space"],
                ["**Scheduled publish**", "A [publish someone scheduled](drafts-and-publishing.html#publish-later)", "People who edit pages in the space"],
                ["**Review due**", "An open [review request](reviews.html), on the day it is due", "People who edit pages in the space"],
                ["**Review-by date**", "A page's [review-by date](reviews.html#review-by-dates)", "Editors for every page; readers for published pages"],
            ]),

            H("Add an event or leave"),
            STEPS([
                "Select **New event**|In a space where you edit pages.",
                "Pick the space and **What it is**|An event, or **My leave**, which is always whole days.",
                "Set the dates|**All day** for whole days (up to a year), or a start and end time (up to 31 days). Times are in your browser's time zone, and the event repeats on that clock.",
                "Repeat it (optional)|Daily, weekly, monthly or yearly, every 1 to 99, until a date, a number of times, or never ending. A monthly event on the 31st skips months without one.",
                "Select **Add to the calendar**|",
            ]),
            SHOT("calendar-new-event.png", "The New event dialog: space, kind, dates and a weekly repeat"),
            P("People who edit pages in the space change and delete its events; deleting a repeating event deletes every time it repeats. A space holds up to 5,000 events."),

            H("Subscribe in a calendar app"),
            P("**Subscribe** gives you a calendar address for an app such as Outlook, Google Calendar or Apple Calendar, which then shows what this calendar shows you: the spaces you read and the entries in them."),
            STEPS([
                "Select **Subscribe**, then **Make an address**|",
                "Copy the address now|It is shown only once.",
                "Add it to your calendar app as a calendar from the internet (a subscription)|The app reads it every so often; how often is up to the app.",
            ]),
            WARN("Anyone who has the address can read your calendar, so keep it to yourself. Lost it or shared it by mistake? **Make a new address**: the old one stops working. **Stop the address** turns it off."),
            P("The dialog says when you made the address and when an app last read it. The address also stops when you sign out of your other sessions or change your password; make a new one then."),
            SHOT("calendar-subscribe.png", "The Subscribe dialog, before an address is made"),
        ])),

    ("analytics", dict(
        label="Analytics", title="Analytics", icon="activity",
        desc="How pages and spaces are read, who publishes, and which pages need looking after (Pro)",
        keywords=["analytics", "views", "readers", "statistics", "stats", "reading time", "popular pages", "content health",
                  "stale", "broken links", "search misses", "csv", "export", "pro"],
        blocks=[
            NOTE("Analytics needs a Pro or Enterprise licence. Without one, the Analytics entries don't show and no views are recorded. See [Licensing](licensing.html)."),
            H("Overview"),
            P("Analytics shows how the spaces you read are read and kept up. Numbers follow within a quarter of an hour. Pick the **Period**: 7 days, 30 days, 90 days or 12 months, each compared with the same length of time before it."),
            SHOT("analytics-overview.png", "Analytics: views, readers, pages published and editors, the views by day chart and the most viewed spaces"),
            TABLE(["Where", "What it shows"], [
                ["**Analytics** in the left menu", "Every space you can read: views, readers, pages published, editors and average reading time, views or readers by day, the most viewed pages and spaces, who published, and content health"],
                ["A space's **Analytics** tab", "The same for one space, with **People** (who read and who published) for the space's admins"],
                ["**Analytics** under a page's title", "One published page: its views, readers, reading time and **Was this page helpful?** answers"],
            ]),

            H("What is counted"),
            UL([
                "A view is a published page opened in the browser. The same person opening the same page again within 10 minutes is one view.",
                "Readers who aren't signed in count as views (shown apart), not as readers.",
                "Reading time is the time the page was on screen with the tab visible.",
                "Pages read through API tokens aren't counted, and drafts never are.",
                "Each view is kept 90 days, and who read what each day 25 months. Daily counts per page and space are kept as long as the page or space.",
            ]),
            P("Who read what is shown only to a space's admins. Everyone else sees counts. Names of people who published follow the space's rule for seeing people."),
            SHOT("analytics-page.png", "A page's analytics: views, readers, reading time and the helpful answers"),

            H("Content health"),
            P("**Content health** lists pages that need looking after, ten of each with a total:"),
            TABLE(["List", "Pages"], [
                ["**Not updated in 180 days**", "Published pages nobody has published a new version of in that time"],
                ["**Drafts left open**", "Drafts and pages in review nobody has changed for 30 days (in a space's analytics, for people who edit pages there)"],
                ["**Broken links**", "Pages that link to or include pages that are gone. Checked every hour."],
                ["**Least helpful**", "Pages readers marked as not helpful most often"],
                ["**Searches with no results**", "What people in your organization searched for at least twice and didn't find (in Analytics in the left menu, for administrators)"],
                ["**Questions and answers**", "Questions asked in the period, answered and with an accepted answer, and all still open (in Analytics in the left menu)"],
            ]),
            SHOT("analytics-health.png", "Content health: stale pages, drafts left open, broken links and searches with no results"),

            H("Export"),
            P("**Export CSV** downloads the most viewed published pages of the period (up to 10,000): space, page, title, views, views by readers not signed in, readers and average reading time, for the spaces in view."),
        ])),

    ("mobile", dict(
        label="On a phone", title="Using the Wiki on a Phone", icon="sun",
        desc="Reading, editing, Q&A and the calendar on a small screen",
        keywords=["mobile", "phone", "tablet", "small screen", "touch", "ios", "android", "responsive"],
        blocks=[
            H("Overview"),
            P("The Wiki works in the browser on a phone: nothing to install. Every screen fits the width of the phone, and buttons and links are large enough to tap."),
            SHOT("mobile-page.png", "A published page on a phone"),
            UL([
                "The left menu opens from the menu button in the header.",
                "Rows in lists and tables (spaces, analytics, content health) open wherever you tap them.",
                "Wide tables in a page scroll sideways inside the page.",
                "Videos play in the phone's own player.",
            ]),

            H("Editing"),
            P("People who edit a page can edit it on a phone, together with others, as on a computer. The formatting toolbar scrolls sideways, and **Page details** (status, reviews, plans, versions, comments) is under the page instead of beside it."),
            SHOT("mobile-editor.png", "The editor on a phone, with the toolbar above the page"),
            P("If the connection drops on the move, keep the tab open: your changes are saved when it returns. See [Editing together](editing-together.html)."),

            H("Calendar and Q&A"),
            P("On a phone the month view marks each day's entries with dots, and the whole day is the button: tap it to see that day's entries under the calendar. The agenda view lists the next 30 days. Q&A works in full: ask, answer, vote and comment."),
            SHOT("mobile-calendar.png", "The calendar's month view on a phone, with a day selected"),
            NOTE("On tablets, controls use their compact desktop size. Plugin screens that need a large screen say so on a phone."),
        ])),
]
