"""Wiki doc pages (user_a): first steps, navigation, search, profile and
alerts, spaces, the page tree, the editor and blocks. See content.py.
Keep in step with apps/wiki and libs/platform-ui in the depotex repo."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, CODE, SHOT

USER_A = [
    # ------------------------------------------------------------------
    ("getting-started", dict(
        label="Getting started", title="Getting started with the Wiki", icon="rocket",
        desc="Sign in, find your spaces, read a page and write your first one",
        keywords=["getting started", "sign in", "first steps", "spaces", "pages", "reader", "editor", "guest"],
        blocks=[
            H("What the Wiki is"),
            P("The Wiki holds your organization's pages: runbooks, handbooks, decisions, plans. Pages live in **spaces**, one per team or project, and each space decides who can read and who can write. Inside a space, pages form a tree: a page can have pages under it, as many levels deep as you need."),
            P("Several people can edit a page at the same time. Readers see the last **published** version; what editors change stays a draft until someone publishes it. See [Drafts and publishing](drafts-and-publishing.html)."),

            H("Sign in"),
            P("Open the address your administrator gave you and sign in with your email and password, or with your organization's single sign-on button when one is set up. **Forgot password?** sends you a link to choose a new one."),
            SHOT("getting-started-sign-in.png", "The sign-in page"),
            P("If your administrator turned on anonymous access, people without an account can read **public** spaces without signing in. They see the reading view only: no editing, watching, copying or answering \"Was this page helpful?\". See [Anonymous access](anonymous-access.html)."),

            H("Your first ten minutes"),
            STEPS([
                "**Find your spaces.** After signing in you land on **Spaces**: every space you can see. **Yours** lists only the spaces where you have a role. See [Spaces](spaces.html).",
                "**Read a page.** Open a space, then a page in its tree on the left. The page shows its last published version, who changed it and when.",
                "**Watch what matters.** **Watch** on a page sends you an alert each time a new version is published. See [Profile and notifications](profile-and-notifications.html).",
                "**Write a page.** If you are an editor of the space, **New page** in the page tree creates a draft. Write it, then **Publish**. See [Pages and the page tree](pages-and-the-page-tree.html) and [The editor](editor.html).",
                "**Find anything later.** Press **Ctrl+K** (**⌘K** on a Mac) or **/** to search spaces, pages, labels and questions. See [Search](search.html).",
            ]),

            H("What you can do depends on your role"),
            P("Each space gives its members one of four roles. Your role in a space shows at the top of the space (**Your role: Editor**) and in the **Your role** column of the space list."),
            TABLE(["Role", "Can"], [
                ["Viewer", "Read pages"],
                ["Commenter", "Read pages and comment on them"],
                ["Editor", "Read, create, edit, move and delete pages"],
                ["Admin", "Everything, including members, settings and deleting the space"],
            ]),
            P("Spaces that are **internal** or **public** can be read by more people than their members; only members can edit them. Creating a new space is for super admins by default."),

            H("Where to go next"),
            UL([
                "[Home and navigation](home-and-navigation.html): the sidebar, the header and the **Create** button.",
                "[The editor](editor.html) and [Blocks and macros](macros.html): writing and formatting pages.",
                "[Comments](comments.html), [Reviews](reviews.html) and [Editing together](editing-together.html): working on a page with others.",
                "[Q&A](qna.html), [Calendar](calendar.html) and [Analytics](analytics.html).",
            ]),
        ])),

    # ------------------------------------------------------------------
    ("home-and-navigation", dict(
        label="Home and navigation", title="Home and navigation", icon="grid",
        desc="The sidebar, the header, the Create button, and how links to spaces and pages work",
        keywords=["navigation", "sidebar", "menu", "header", "create", "home", "dashboard", "breadcrumbs", "help", "profile menu", "phone"],
        blocks=[
            H("Overview"),
            P("Every screen of the Wiki has the same frame: a sidebar on the left and a header across the top. The Wiki's home is the **Spaces** list: opening the Wiki's address without a path takes you there."),
            SHOT("home-and-navigation-shell.png", "A space's overview with the sidebar on the left and the header at the top"),

            H("The sidebar"),
            TABLE(["Entry", "What it opens"], [
                ["**Dashboard**", "Your dashboard: the newest posts of the blogs you follow and of your spaces, and widgets from plugins."],
                ["**Spaces**", "Every space you can see. See [Spaces](spaces.html)."],
                ["**Blogs**", "Posts from every space's blog you can read. See [Space blogs](blogs.html#the-company-blogs-page)."],
                ["**Labels**", "Every label in use, and the pages that carry each one. See [Labels and feedback](labels-and-feedback.html)."],
                ["**Q&A**", "Questions and answers for your organization, when you may read them. See [Q&A](qna.html)."],
                ["**Calendar**", "Space calendars, scheduled publishes and review-by dates. See [Calendar](calendar.html)."],
                ["**Analytics**", "Who reads what. Shown only when your licence includes analytics. See [Analytics](analytics.html)."],
                ["**Org settings** / **Settings**", "At the bottom, for people who manage the installation. See [Settings reference](settings-reference.html)."],
            ]),
            P("Pages that installed [plugins](plugins.html) add are listed under **Plugins** in the sidebar. The button at the top left folds the sidebar. On a phone the sidebar opens from the menu button instead."),

            H("The header"),
            UL([
                "**Search** finds spaces, pages, labels and questions. **/** or **Ctrl+K** opens it from anywhere. See [Search](search.html).",
                "**Create** starts something new: a **Space** (if you may create spaces) or a **Question** (if you may ask). Each item shows only with its permission.",
                "The **?** button opens help.",
                "The bell shows your alerts, with the number of unread ones. See [Alerts](alerts.html).",
                "Your picture or initials open the profile menu: **Edit Profile**, theme, language and sign out. See [Profile and notifications](profile-and-notifications.html).",
            ]),
            SHOT("home-and-navigation-create.png", "The Create menu: a new space or a new question"),

            H("Inside a space"),
            P("A space has tabs across the top: **Overview** (its description and pages), **Members**, and for the right roles **Analytics**, **Settings**, **Trash** and **Import**. The page tree on the left lists the space's pages. On a page, the breadcrumbs above the title show where it sits in the tree; each part is a link."),

            H("Links"),
            P("Every space and page has its own address, so you can bookmark it or paste it in a chat. A space's address uses its key (`/spaces/eng`); a page's address uses a fixed id, so it keeps working when the page is renamed or moved within the space. People who can't see the space get a message that the page doesn't exist or can't be seen; nothing about it is shown."),
        ])),

    # ------------------------------------------------------------------
    ("search", dict(
        label="Search", title="Search", icon="search",
        desc="Find spaces, pages, labels and questions from the search box at the top of every screen",
        keywords=["search", "find", "palette", "ctrl+k", "cmd+k", "shortcut", "spaces", "pages", "posts", "labels", "questions", "api"],
        blocks=[
            H("Overview"),
            P("The search box at the top of every screen finds what you can open across the Wiki: spaces, pages, labels and questions, and for administrators settings, people and groups. Open it by clicking the box, with **Ctrl+K** (**⌘K** on a Mac), or with **/** when you aren't typing in a field. On a phone, tap the search button in the header; the search fills the screen."),
            SHOT("search-palette.png", "Search: spaces, pages and labels matching what was typed"),
            P("Results appear as you type, grouped by kind, with the first one highlighted. A page shows the space it is in; a question shows **Answered** when it has an accepted answer."),

            H("All results"),
            P("The box shows the first five results of each kind. **See all results** at the bottom (or **Enter** on it) opens the **Search** page: every kind under **All**, each with **Show more** when there are more, and a tab per kind that found something. A kind's tab lists its results 20 at a time with **Load more**. The address holds the words and the tab (`/search?q=failover&kind=pages`), so a search can be bookmarked or shared; others see only what they may open."),
            SHOT("search-results.png", "The Search page: every kind of result, with a tab per kind"),

            H("What it finds"),
            P("Only what you could open yourself is found: a space you can't see never appears, nor do its pages, even by name. Drafts, archived pages and pages in the trash aren't found."),
            TABLE(["Kind", "Matches", "Opens"], [
                ["Spaces", "Name and key", "The space's overview"],
                ["Pages", "Words of the page's title (published pages only)", "The page"],
                ["Labels", "Labels that start with what you typed, on pages you can read", "The label's list of pages"],
                ["Posts", "Words of a blog post's title (published posts only)", "The post. See [Space blogs](blogs.html)"],
                ["Questions", "Title and text of a question", "The question in [Q&A](qna.html)"],
                ["Settings", "A setting's label, tab or page", "For people who can open Settings"],
                ["People and groups", "Name, username, email", "For administrators who may see them"],
            ]),
            NOTE("Pages are found by their title, not yet by the words in their content. To find a page by its subject, give it a clear title and [labels](labels-and-feedback.html)."),
            P("While [anonymous access](anonymous-access.html) is on, visitors who aren't signed in find public spaces and their published pages."),

            H("How matching works"),
            P("Each word you type must start a word of the result: `fail run` finds **Payments failover runbook**, and so does `run`, but `book` doesn't. Dots, dashes, underscores and `@` separate words. Type at least two letters or digits. Case and order don't matter."),

            H("Using the keyboard"),
            UL([
                "**↑** and **↓** move through the results, **Enter** opens the highlighted one, **Esc** closes the search.",
                "With the box empty, your last five searches are offered. They are kept in this browser only; **Clear** forgets them.",
                "**Ctrl+K** opens the search even while you are typing in a page.",
            ]),

            H("Searching through the API"),
            P("`GET /api/search` takes the same words in `q` and answers with the kinds your [API token](api-tokens.html) allows; it never finds more than its owner could. Add `kind` (`spaces`, `pages`, `labels` or `questions`) for one kind, 20 a page, and pass each group's `next` back as `cursor` for the next page."),
            CODE('curl -H "Authorization: Bearer $WIKI_TOKEN" "https://wiki.example.com/api/search?q=failover&kind=pages"'),
        ])),

    # ------------------------------------------------------------------
    ("profile-and-notifications", dict(
        label="Profile and notifications", title="Your profile and notifications", icon="users",
        desc="Your avatar, theme and language, watching pages, mentions, and which alerts you get",
        keywords=["profile", "avatar", "theme", "dark mode", "language", "notifications", "watch", "stop watching", "mention", "@", "preferences", "mute", "password", "sessions"],
        blocks=[
            H("Your profile settings"),
            P("Open your profile settings from the profile menu (your picture or initials, top right) with **Edit Profile**. The sections are in three groups: **Account** (Profile, Preferences, Notifications), **Sign-in** (Security, Active sessions) and **Access** (API tokens, Connected apps, and sections that installed plugins add). On a phone the sections are a row of tabs above the content."),
            UL([
                "**Profile**: change your avatar (a preset picture, or upload JPEG, PNG or WebP up to 2 MB) and see your name, email and role. An administrator changes your name and email.",
                "**Preferences**: the theme and language (below).",
                "**Notifications**: which alerts you get (below).",
                "**Security**: change your password, and **Download my data**.",
                "**Active sessions**: where you are signed in; sign out one session or all the others.",
                "**API tokens**: tokens for scripts and integrations. See [API tokens](api-tokens.html).",
                "**Connected apps**: applications you allowed to act for you. See [OAuth applications](oauth-applications.html).",
            ]),

            H("Theme and language"),
            P("Under **Preferences**, pick **Light**, **Dark** or **High contrast**; each card previews that theme. **Language** sets the language of menus, messages, numbers and dates: English or German (Deutsch). Both are saved for your account and follow you to other devices. The profile menu has the same two choices as a shortcut."),
            SHOT("profile-and-notifications-theme.png", "Profile settings → Preferences: the three themes and the language"),

            H("Watching a page"),
            P("**Watch** on a page sends you an alert each time a new version of it is published. **Stop watching** ends that. You watch a page automatically when you create it or publish a version of it; once you stop watching, the Wiki doesn't sign you up again."),
            SHOT("profile-and-notifications-watch.png", "The Stop watching button on a page you watch"),
            UL([
                "A version published as a **Minor change** doesn't alert watchers.",
                "You aren't alerted about your own publish.",
                "A new comment on a page you watch alerts you too. See [Comments](comments.html).",
                "You are only alerted while you can still read the page.",
            ]),
            NOTE("Watching a whole space or a label isn't available yet: watch the pages you care about."),

            H("Mentions"),
            P("Editors can mention someone in a page by typing **@** and part of their name, then picking them from the list. When the page is next published, each person it mentions gets an alert, once per page: being mentioned again in a later version of the same page doesn't alert them again. Mentions in [comments](comments.html) alert the person when the comment is posted."),
            UL([
                "The list offers active people of the space's organization, matched on their name (never their email). In a private space, only the space's members can be mentioned.",
                "Mentioning needs permission to see people's profiles; editors without it don't get the list.",
                "Readers who may not see people's profiles, and visitors who aren't signed in, see the name only.",
            ]),

            H("Choosing which alerts you get"),
            P("**Notifications** in your profile settings (also the settings icon in the bell panel, and **Preferences** on the notifications page) controls what reaches you:"),
            UL([
                "**Opt out of non-critical alerts** stops everything but critical alerts and the categories your administrator forces on everyone.",
                "Muted categories stop one kind of alert. Forced categories can't be muted and show a lock icon.",
                "A summary below says what you'll receive. Changes wait in a bar at the bottom until you **Save preferences** or **Discard** them.",
            ]),
            SHOT("profile-and-notifications-preferences.png", "Profile settings → Notifications: opt-out, muted and forced categories"),
            NOTE("The Wiki's alerts arrive in the bell and on the notifications page. Email and digest delivery of page alerts isn't available yet. To stop alerts about one page, use **Stop watching** on it."),
        ])),

    # ------------------------------------------------------------------
    ("alerts", dict(
        label="Alerts", title="Alerts and the notifications page", icon="bell",
        desc="The bell, what the Wiki alerts you about, and the notifications page",
        keywords=["alerts", "notifications", "bell", "unread", "mark read", "clear", "mention", "review", "comment", "watch"],
        blocks=[
            H("The bell"),
            P("The bell at the top right shows how many unread alerts you have (**99+** past 99). Click it to open the panel; on a phone it fills the screen. New alerts arrive while you work, with no need to reload."),
            SHOT("alerts-bell.png", "The bell's panel: unread alerts, newest first"),
            UL([
                "**Unread** and **All** tabs. Alerts are grouped by **Today**, **Yesterday** and **Earlier**.",
                "Click an alert, or the dot beside it, to mark it read; click the dot again to mark it unread.",
                "**Open the page** (or **Open the question**) goes to what the alert is about.",
                "**Mark all read** marks every alert read. The settings icon opens your [notification preferences](profile-and-notifications.html).",
                "**View all notifications** opens the notifications page.",
            ]),

            H("What the Wiki alerts you about"),
            TABLE(["Alert", "When"], [
                ["**<page> was updated**", "A new version of a page you watch was published (not for a minor change)"],
                ["**You were mentioned in <page>**", "A published version mentions you for the first time"],
                ["**New comment on <page>**", "Someone commented on a page you watch, or in a thread you took part in"],
                ["**You were mentioned in a comment on <page>**", "A comment mentions you"],
                ["**Review requested: <page>**", "Someone asked you to review a page. See [Reviews](reviews.html)"],
                ["**<page> was approved** / **Changes requested on <page>**", "A reviewer answered your request"],
                ["**A review of <page> is overdue**", "The date for a review you were asked for has passed"],
                ["**<page> is due for review**", "A page's review-by date has passed. See [Calendar](calendar.html)"],
                ["**A scheduled publish of <page> didn't happen**", "A publish you scheduled couldn't be made, or the draft changed after you scheduled it"],
                ["**New feedback on <page>**", "A reader answered \"Was this page helpful?\" with No and left a note. See [Labels and feedback](labels-and-feedback.html)"],
                ["Q&A alerts", "Answers, comments, accepted answers, mentions and new questions with a tag you follow. See [Q&A](qna.html)"],
            ]),
            P("Each alert is for you alone and names nobody else it went to. A newer alert about the same page and the same thing replaces the older one, so a busy page doesn't fill your bell."),

            H("The notifications page"),
            P("**View all notifications** (or the address `/alerts`) lists every alert you have. It opens on **Unread**."),
            SHOT("alerts-page.png", "Notifications: filters by state, severity and category, and every alert with its actions"),
            UL([
                "**Show**: Unread, All or Cleared, with how many each holds.",
                "**Severity** and **Category** narrow the list. The Wiki's own alerts are **info**.",
                "**Select several** to **Mark read** or **Clear** them together; on Cleared, **Restore** brings them back.",
                "Clearing only hides the alert for you. A cleared alert shows **Undo** for a moment.",
                "**Preferences** opens your notification preferences; **Load more** shows older alerts.",
            ]),
            NOTE("**Category** lists kinds of alert by name (Watched pages, Comments, Mentions in pages, Review requests, Answers…), each covering every page or question of that kind. To stop alerts about one page, use **Stop watching** on the page."),
        ])),

    # ------------------------------------------------------------------
    ("spaces", dict(
        label="Spaces", title="Spaces", icon="book",
        desc="What a space is, who can see it, roles and members, space settings, and creating one",
        keywords=["space", "spaces", "visibility", "private", "internal", "public", "members", "roles", "viewer", "commenter", "editor", "admin", "groups", "service accounts", "settings", "delete space", "templates", "key"],
        blocks=[
            H("What a space is"),
            P("A space holds a team's or a project's pages, and has its own members. Every page belongs to one space, and the space decides who can read it and who can write. Pages have no access rules of their own: everyone who can read the space can read all of its published pages."),

            H("The space list"),
            P("**Spaces** in the sidebar lists every space you can see, with its visibility, when it last changed and your role. **All** shows them all, **Yours** only those where you have a role. Filter by name with **Search spaces** or by visibility."),
            SHOT("spaces-list.png", "Spaces: every space you can see, with its visibility and your role"),

            P("Besides its pages, each space has a **Blog** tab for dated posts: updates, announcements and stories. See [Space blogs](blogs.html)."),

            H("Who can see a space"),
            TABLE(["Visibility", "Who can read", "Who can edit"], [
                ["**Private**", "Only members of the space", "Members with the Editor or Admin role"],
                ["**Internal**", "Everyone in your organization who can sign in", "Members with the Editor or Admin role"],
                ["**Public**", "Anyone, even without signing in", "Members with the Editor or Admin role"],
            ]),
            P("A space can only be made **public** while anonymous access is on, which a super admin turns on in Settings → Security. If anonymous access is turned off later, public spaces stay readable by signed-in people only until it is back on. See [Anonymous access](anonymous-access.html)."),

            H("Roles"),
            P("Each member of a space has one role. A person can be a member directly or through a group; everyone in a group gets the group's role, and the highest role a person has counts."),
            TABLE(["Can", "Viewer", "Commenter", "Editor", "Admin"], [
                ["Read pages", "Yes", "Yes", "Yes", "Yes"],
                ["Comment on pages", "No", "Yes", "Yes", "Yes"],
                ["Create, edit, move and delete pages", "No", "No", "Yes", "Yes"],
                ["Write blog posts and edit your own", "No", "If the space allows", "Yes", "Yes"],
                ["Edit anyone's blog post, manage the blog", "No", "No", "No", "Yes"],
                ["Manage members", "No", "No", "No", "Yes"],
                ["Change name, description and visibility", "No", "No", "No", "Yes"],
                ["Delete the space", "No", "No", "No", "Yes"],
            ]),

            H("Members"),
            P("The **Members** tab lists the people, service accounts and groups with a role in the space. **Compare roles** shows the table above. Filter by kind (People, Groups, Service accounts) or by name."),
            SHOT("spaces-members.png", "Members: each member's kind and role, with the role comparison open"),
            STEPS([
                "Open the space, then **Members**.",
                "**Add member**, search for a person, service account or group, pick a **Role** and **Add**.",
                "To change a role, pick another one next to the member. To take a member out, **Remove** and confirm. Roles they have through a group stay.",
            ]),
            P("Only the space's admins can add members or change roles. Only the space's members, and people allowed to view profiles, can see who has a role in it."),

            H("Creating a space"),
            P("**Create → Space** in the header, or **New space** on the space list, opens the form. By default only super admins may create spaces. Creating a space gives nobody a role in it: add members, and an admin, right after."),
            SHOT("spaces-new.png", "New space: name, key, description and visibility"),
            TABLE(["Field", "What to enter"], [
                ["**Name**", "What people call the space, such as **Engineering handbook**."],
                ["**Key**", "Used in links (`/spaces/eng`). 2–40 lowercase letters and digits, optionally separated by single hyphens. It can't be changed later."],
                ["**Description**", "What the space is for, shown on its overview."],
                ["**Visibility**", "Private, internal or public (above)."],
            ]),

            H("Space settings"),
            P("The space's admins see a **Settings** tab:"),
            UL([
                "**General**: the name, description and visibility. **Save** applies them. The key is fixed.",
                "**Page templates**: content new pages of this space can start with. See [Copies and templates](copies-and-templates.html).",
                "**Delete space**: removes the space, its pages and its members' roles for good. Type the space's key to confirm.",
            ]),
            SHOT("spaces-settings.png", "Space settings: General, Page templates and Delete space"),
            WARN("Deleting a space can't be undone. Its pages don't go to the trash."),

            H("Other tabs"),
            UL([
                "**Trash**: pages deleted in the space, for people who can edit pages. See [Pages and the page tree](pages-and-the-page-tree.html#deleting-and-the-trash).",
                "**Import**: bring in a Confluence space export or Markdown files (space admins, when imports are allowed). See [Import and export](import-and-export.html).",
                "**Analytics**: how the space's pages are read, when your licence includes analytics. See [Analytics](analytics.html).",
            ]),
        ])),

    # ------------------------------------------------------------------
    ("pages-and-the-page-tree", dict(
        label="Pages and the page tree", title="Pages and the page tree", icon="file",
        desc="Reading a page, creating pages, page status, moving pages and the trash",
        keywords=["page", "pages", "tree", "new page", "child page", "move", "reorder", "delete", "trash", "restore", "status", "draft", "published", "archived", "breadcrumbs"],
        blocks=[
            H("Reading a page"),
            P("Open a page from the space's page tree, a link or [search](search.html). Readers see the page's last published version: its title, when it last changed, the content, and at the bottom the pages under it, \"Was this page helpful?\", [labels](labels-and-feedback.html) and [comments](comments.html)."),
            SHOT("pages-reading-view.png", "A published page as a reader sees it"),
            P("At the top of the page, **Download** saves it as a Word document or PDF ([Import and export](import-and-export.html)), **Copy** makes a copy ([Copies and templates](copies-and-templates.html)) and **Watch** sends you alerts when it changes ([Profile and notifications](profile-and-notifications.html)). **Page history** shows its published versions ([Page history and versions](page-history-and-versions.html))."),

            H("The page tree"),
            P("The left side of a space lists its pages as a tree. The arrow next to a page shows or hides the pages under it. Readers see published pages only; editors see every page, with a badge for drafts and pages in review."),
            UL([
                "A page can be at most 100 levels deep.",
                "Titles are unique within a space: two pages can't share a title (case is ignored).",
                "Editors can move a page up or down among its neighbours with the buttons next to it in the tree.",
            ]),

            H("Creating a page"),
            STEPS([
                "In the space, choose **New page** above the tree (a top-level page), or **Add a page** on a page (a page under it).",
                "Enter the **Title**. Under **Start from**, keep **Blank page** or pick one of the space's templates.",
                "**Create page**. It opens in the [editor](editor.html).",
            ]),
            SHOT("pages-new-page.png", "New page: the title and the template to start from"),
            P("A new page starts as a draft: only people who can edit pages in the space see it until it is published. See [Drafts and publishing](drafts-and-publishing.html)."),

            H("Page status"),
            TABLE(["Status", "Who sees it"], [
                ["**Draft**", "Editors of the space only"],
                ["**In review**", "Editors of the space only; see [Reviews](reviews.html)"],
                ["**Published**", "Everyone who can read the space"],
                ["**Archived**", "Editors of the space only"],
            ]),
            P("Editors change it with **Status** in the page's side panel. So that readers never meet a page whose parent they can't see, a page can only be published under published pages, and a page with published pages under it can't be taken back to draft until they are."),

            H("Moving a page"),
            STEPS([
                "Open the page as an editor and choose **Move**.",
                "Pick the page to put it under, or **Top level of the space**.",
                "Under **Place it**, choose **First** or **Last** among its new neighbours, then **Move page**.",
            ]),
            SHOT("pages-move.png", "Move: choose the page to put it under and where among its neighbours"),
            P("The pages under it move with it. A page can't go under itself or one of its own pages, and a published page can only go under a published page. Its address stays the same."),

            H("Deleting and the trash"),
            P("**Delete** on a page moves it, and every page under it, to the space's trash. The **Trash** tab of the space lists them, with when they were deleted and when they will be removed for good."),
            SHOT("pages-trash.png", "Trash: deleted pages with Restore and Delete for good"),
            UL([
                "Pages stay in the trash for 30 days, then they are removed for good.",
                "**Restore** puts a page back under its old parent, or at the top level if that parent is gone or no longer published. It fails if another page took its title meanwhile: rename that page first.",
                "**Delete for good** removes it at once. It needs the space's Admin role and can't be undone.",
                "Only people who can edit pages in the space see its trash.",
            ]),
        ])),

    # ------------------------------------------------------------------
    ("editor", dict(
        label="The editor", title="The editor", icon="terminal",
        desc="Formatting, headings and heading numbers, lists, tables, images, the \"/\" menu, keyboard shortcuts and full screen",
        keywords=["editor", "edit", "format", "bold", "heading", "numbered headings", "list", "checklist", "table", "image", "video", "link", "slash", "/", "shortcut", "keyboard", "full screen", "table of contents", "mention", "figure"],
        blocks=[
            H("Overview"),
            P("Editors of a space open a page straight into the editor. Your changes are saved as you type (**All changes saved** at the top), and everyone editing the page sees them at once; see [Editing together](editing-together.html). Readers keep seeing the published version until someone chooses **Publish**; see [Drafts and publishing](drafts-and-publishing.html)."),
            SHOT("editor-workspace.png", "The editor: the toolbar, the page, and the side panel with status, reviews, plans and comments"),
            UL([
                "The top bar holds the breadcrumbs, the save state, who else is here, **Preview** (the draft as readers will see it) and **Publish**.",
                "The side panel holds the page's **Status**, [reviews](reviews.html), plans ([scheduled publishing and review-by dates](calendar.html)), versions, heading and figure numbers, comments, labels, the pages under this one, **Move** and **Delete**.",
                "If the connection drops, the editor says **Offline. Reconnecting…** and keeps your changes in the tab until it is back.",
            ]),

            H("The toolbar"),
            SHOT("editor-toolbar.png", "The formatting toolbar"),
            TABLE(["Group", "Tools"], [
                ["Text style", "**Text**, **Heading 1**, **Heading 2**, **Heading 3**, **Code block**"],
                ["History", "**Undo**, **Redo** (your own changes only, not other people's)"],
                ["Marks", "**Bold**, **Italic**, **Underline**, **Strikethrough**, **Code**"],
                ["Alignment", "**Align left**, **Center**, **Align right**, **Justify**"],
                ["Lists", "**Bulleted list**, **Numbered list**, **Checklist**, **Outdent**, **Indent**"],
                ["Blocks", "**Quote**, **Divider**"],
                ["Insert", "**Link**, **Insert image**, **Insert video**, **Insert table of contents**, **Insert table**"],
                ["Other", "**Comment on selection**, **Full screen**"],
            ]),
            P("When a table, image, video or block is selected, its own settings appear in the toolbar (**Table**, **Image settings**, **Video settings**, **Block settings**). On a phone, the toolbar scrolls sideways."),

            H("The \"/\" menu"),
            P("Type **/** at the start of a line or after a space to insert any block. Keep typing to narrow the list, use **↑** and **↓** to move, **Enter** to insert and **Esc** to close it."),
            SHOT("editor-slash-menu.png", "The \"/\" menu, listing the blocks you can insert"),
            P("It lists text styles and lists, **Quote**, **Code block**, **Divider**, **Table**, **Spreadsheet table**, **Image**, **Video**, **Table of contents**, and the blocks described in [Blocks and macros](macros.html): panels, expand, decision, status, anchor, excerpt, page properties, child pages, page tree, recently updated, include page, include excerpt, page properties report, and blocks from plugins."),

            H("Headings and heading numbers"),
            P("Use **Heading 1** to **Heading 3** to structure a page. Each heading gets an anchor from its words, so you can link to it with `#section-…` after the page's address, and a table of contents lists it."),
            P("**Heading numbers** in the side panel numbers a page's headings: **None**, **1, 1.1, 1.1.1** or **1., 1.1., a.**. Numbers are added when the page is shown; the text stays as you write it, so moving a section renumbers everything after it."),
            SHOT("editor-heading-numbers.png", "A page with numbered headings and a numbered table of contents"),
            P("**Insert table of contents** lists the page's headings where you put it. Its settings choose the **Headings to list** (top level only, two levels or three levels) and whether to **Number the entries**; when the page numbers its headings, the same numbers are used."),

            H("Lists and checklists"),
            P("**Bulleted list**, **Numbered list** and **Checklist** start a list; **Indent** and **Outdent** (or **Tab** and **Shift+Tab**) nest an item. Readers see checklist boxes as you left them."),

            H("Links and mentions"),
            P("Select text and choose **Link** to link it to a web address (`https://…`), an email (`mailto:…`) or a path in the Wiki (`/spaces/…`). Type **@** and part of a name to mention someone; see [Profile and notifications](profile-and-notifications.html#mentions)."),

            H("Tables"),
            P("**Insert table** adds a table with a header row. With the cursor in it, the **Table** tools add a row below or a column after, delete rows, columns or the table, turn the header row on or off, and merge or split cells. For sums and other calculations use a **Spreadsheet table**; see [Blocks and macros](macros.html#spreadsheet-tables)."),

            H("Images and videos"),
            P("**Insert image**, or paste or drop an image onto the page. **Image settings** sets the **Alternative text** (describe the image for people who can't see it), a **Caption**, the **Width** (a quarter, half, three quarters or full width) and the **Position**. With **Figure numbers** turned on in the side panel, captioned images are numbered Figure 1, Figure 2… in reading order."),
            P("Images can be PNG, JPEG, GIF or WebP up to 20 MB. For videos, files and limits see [Attachments and media](attachments-and-media.html) and [Blocks and macros](macros.html#video)."),

            H("Full screen"),
            P("**Full screen** at the right end of the toolbar hides the sidebar and header so only the page and toolbar remain. **Leave full screen**, or **Esc**, brings them back."),

            H("Keyboard shortcuts"),
            P("Use **Ctrl** on Windows and Linux, **⌘** on a Mac."),
            TABLE(["Shortcut", "Does"], [
                ["Ctrl+B / Ctrl+I / Ctrl+U", "Bold / italic / underline"],
                ["Ctrl+Shift+S", "Strikethrough"],
                ["Ctrl+E", "Code"],
                ["Ctrl+Alt+1, 2, 3", "Heading 1, 2, 3"],
                ["Ctrl+Alt+0", "Text"],
                ["Ctrl+Shift+8 / Ctrl+Shift+7 / Ctrl+Shift+9", "Bulleted list / numbered list / checklist"],
                ["Ctrl+Shift+B", "Quote"],
                ["Ctrl+Z / Ctrl+Shift+Z or Ctrl+Y", "Undo / redo your own changes"],
                ["Shift+Enter", "Line break inside a paragraph"],
                ["/", "The \"/\" menu"],
                ["@", "Mention someone"],
                ["Ctrl+K", "Search"],
                ["Esc", "Close a menu, leave full screen"],
            ]),
            P("Markdown-style typing works too: `# ` to `### ` at the start of a line make headings, `- ` or `* ` a bulleted list, `1. ` a numbered list, `[ ] ` a checklist item, `> ` a quote, three backticks a code block and `---` a divider. `**bold**`, `*italic*` and `` `code` `` format the text as you type."),
        ])),

    # ------------------------------------------------------------------
    ("macros", dict(
        label="Blocks and macros", title="Blocks and macros", icon="sliders",
        desc="Panels, expands, decisions, status, anchors, excerpts and includes, page properties, child pages, page trees, recently updated, video, spreadsheet tables and plugin blocks",
        keywords=["macro", "macros", "block", "panel", "info", "warning", "tip", "expand", "decision", "excerpt", "include", "page properties", "properties report", "status", "lozenge", "anchor", "child pages", "page tree", "recently updated", "video", "spreadsheet", "formula", "sum", "plugin block"],
        blocks=[
            H("Overview"),
            P("Besides text, a page can hold blocks: boxes that stand out, blocks that show other pages, videos, spreadsheet tables and blocks from plugins. Insert any of them from the **\"/\"** menu in the [editor](editor.html). To change one later, select it and choose **Block settings** in the toolbar. Pages imported from Confluence get these blocks for the macros they used; see [Import and export](import-and-export.html)."),

            H("Boxes: panels, expand, decision"),
            SHOT("macros-boxes.png", "An info panel, a note panel, a code block, a closed expand, a decision, an open question and a tip"),
            TABLE(["Block", "What it does", "Example"], [
                ["**Info panel** / **Warning panel**", "A coloured box around text. Its **Type** can be **Info**, **Note**, **Warning**, **Tip** or **Success**, with an optional **Title**.", "A **Before you start** info panel at the top of a runbook."],
                ["**Expand**", "A section readers click to open. Its title defaults to **Show more**; **Open by default** shows it open.", "**What the verify step checks**, with details most readers skip."],
                ["**Decision**", "Records a **Decision** or an **Open question**, each with its own colour.", "**Decision**: we fail over to the standby region rather than restoring from backup."],
            ]),
            P("**Remove box, keep content** in a box's settings takes the box away and leaves its text on the page."),

            H("Status"),
            P("A small coloured label inside a line of text. Enter its **Text** and pick a **Colour**: grey, blue, green, yellow, red or purple. Example: `APPROVED` in green next to **Current state**."),

            H("Anchor"),
            P("An invisible mark you can link to. Give it a **Name** (letters, digits, - and _, up to 64); link to it by adding `#` and the name to the page's address. Headings have anchors of their own already."),

            H("Code block"),
            P("Code in a fixed-width font. Its settings add a **File name** above it and **Line numbers**. Example: `failover.sh` with four numbered lines."),

            H("Excerpt and Include excerpt"),
            P("An **Excerpt** marks part of a page so other pages can show it. Give it an optional **Name** when a page has more than one. **Hide on this page** shows it only where it is included."),
            P("**Include excerpt** shows another page's excerpt: paste the page's **Page link** from the address bar and, if needed, the **Excerpt name**. It shows **Excerpt from <page>** and always shows the current published text. Example: the overview of a team's area quotes the first lines of its failover runbook."),
            NOTE("A hidden excerpt isn't private: it still shows where other pages include it, and in search and page history."),

            H("Include page"),
            P("Shows the whole published content of another page, by its **Page link**. A page can't include itself, and blocks that show other pages aren't shown inside an included page."),

            H("Page properties and Page properties report"),
            P("**Page properties** holds a two-column table of facts about the page (owner, tier, on-call). Give it an optional **Name** when a page has more than one."),
            P("**Page properties report** gathers those tables into one: for each published page in the space with a given **Label**, one row, with a column per property. Example: a **Services** report on the team's overview lists every page labelled `service` with its **Owner**, **Tier** and **On call**. A report shows up to 12 columns."),

            H("Child pages, Page tree, Recently updated"),
            SHOT("macros-other-pages.png", "Child pages two levels deep, an included excerpt, a page properties report and a recently updated list"),
            TABLE(["Block", "Shows", "Settings"], [
                ["**Child pages**", "The pages under this one", "**Levels**: 1 to 3 (default 1)"],
                ["**Page tree**", "The space's page tree", "**Levels** (default 2)"],
                ["**Recently updated**", "The space's most recently changed pages, with when", "**Pages to list**: 5, 10 or 20 (default 10)"],
            ]),
            P("These blocks show each reader only the pages they can see: what you see in the editor may be more than a reader sees. **Preview** the page to check it. **Not every page is listed** appears when a list is cut short."),

            H("Video"),
            P("**Video** adds a video from a file or a video site."),
            UL([
                "**Upload a file**: MP4 or WebM, up to 200 MB. A poster frame is taken from it. Add **Subtitles** as a WebVTT (.vtt) file up to 512 KB, with its **Language** (such as `en` or `pt-BR`).",
                "**Link from a video site**: paste the link. Only sites your administrator allows can be used (YouTube and Vimeo, or your organization's own video platform), set in Settings → Security → Video sites. If a site is taken off the list later, its videos stop playing.",
                "Both take a **Caption** and a **Start at** time (m:ss).",
            ]),
            SHOT("macros-video.png", "An uploaded video with its poster frame and caption"),

            H("Spreadsheet tables"),
            P("A **Spreadsheet table** is a table whose cells can hold formulas. Select a cell and type a value, or a formula starting with `=`, such as `=SUM(B2:B4)`, in the bar above the table. The bar also sets the cell's **Number format** (as typed, number, currency, percent or date), its **Decimal places** and, for currencies, the **Currency code**."),
            SHOT("macros-spreadsheet.png", "A spreadsheet table: amounts in euros with a total worked out by a formula"),
            UL([
                "References are A1-style within the same table: A1 is the first row's first cell. Another table can't be referenced.",
                "Values are worked out in the editor as you type and saved with the page, so readers see them at once. Hover over a cell to see its formula.",
                "Readers can sort a column and **Filter rows** for themselves, when the first row is headers and there are no merged cells.",
                "Numbers and dates show in each reader's language.",
                "Errors show in the cell: `#DIV/0!`, `#VALUE!`, `#REF!`, `#NAME?` (a function that isn't available), `#CIRCULAR!` (a formula that reads itself) or `#CALC!` (too slow to work out).",
            ]),
            P("Functions you can use:"),
            TABLE(["Kind", "Functions"], [
                ["Sums and counts", "SUM, AVERAGE, COUNT, COUNTA, COUNTBLANK, MIN, MAX, MEDIAN, PRODUCT, SUMIF, COUNTIF, AVERAGEIF"],
                ["Numbers", "ROUND, ROUNDUP, ROUNDDOWN, ABS, INT, MOD, POWER, SQRT, CEILING, FLOOR"],
                ["Logic", "IF, IFERROR, AND, OR, NOT, TRUE, FALSE, ISBLANK, ISNUMBER, ISTEXT, ISERROR"],
                ["Lookup", "VLOOKUP, HLOOKUP, INDEX"],
                ["Text", "CONCAT, CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM, TEXT, T"],
                ["Dates", "TODAY, DATE, DATEDIF, YEAR, MONTH, DAY, DAYS"],
            ]),
            NOTE("A table holds at most 2,000 formulas."),

            H("Plugin blocks"),
            P("[Plugins](plugins.html) can add their own blocks, such as a progress bar or a diagram. While such a plugin is active, its blocks are listed in the \"/\" menu under their own names; the block is drawn by the plugin, inside the page, and its settings are inside the block."),
            SHOT("macros-plugin-block.png", "A plugin block on a page: a progress bar from a sample plugin"),
            UL([
                "If the plugin is turned off or removed, or the licence is below Pro (plugins need Pro), readers see the block's short text description instead, and the block is kept on the page.",
                "Visitors who aren't signed in, and pages that include another page, see the text too.",
                "A page can hold up to 50 plugin blocks; the first 20 are drawn, the rest show their text.",
            ]),
            P("A macro from another wiki that an import couldn't convert shows as **Imported macro**, with **What it held**. You can leave it or replace it with a block."),
        ])),
]
