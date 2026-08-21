"""Lens doc content. Edit here, not the generated HTML under lens/docs/."""
from engine import P, H, UL, OL, STEPS, TABLE, NOTE, WARN, SHOT

# Each page: slug -> dict(title, lede, desc, icon, blocks)

PAGES = {}

PAGES["getting-started"] = dict(
    title="Getting Started",
    lede="Install Lens, link a project folder, and take your first capture.",
    desc="Install the Lens Chrome extension, link a local project folder and take your first screenshot or recording.",
    icon="rocket",
    blocks=[
        P("Lens is a Chrome extension that captures a region of any tab as a **PNG**, a **JPEG**, an animated **GIF** or an **MP4**, then files it into a folder on your own machine along with a metadata timeline. It also turns a flow you click through into a [step-by-step guide](guides.html). Nothing is uploaded — see [Privacy](../privacy.html)."),

        H("Install and pin"),
        STEPS([
            "Install Lens from the Chrome Web Store|or load the unpacked folder via chrome://extensions with Developer mode on.",
            "Pin it to the toolbar|click the puzzle-piece icon in Chrome's toolbar and press the pin next to Lens. The toolbar icon is where recording status and capture errors are reported.",
            "Open the popup|click the Lens icon. This is where you pick the active project and start a capture.",
        ]),
        SHOT("lens-popup-first-run.png", "The Lens popup on first run, showing the default project, no folder linked, and the three capture actions"),

        H("Link a project folder"),
        P("A **project** is a name plus one folder on your computer. Captures for the active project are written straight into that folder, next to a `project_metadata.json` file that records what was captured, from which page, and when."),
        STEPS([
            "Open the popup and press **New project**|or press **Link** on the default project to give the existing one a folder.",
            "Name the project|for example, the documentation set or release you are capturing for.",
            "Choose a folder|Chrome asks you to pick it and to grant read/write access. Lens can only ever see the folder you pick.",
        ]),
        NOTE("Without a linked folder Lens still works — captures fall back to your **Downloads** folder, under `Lens-Captures/`. The popup says which mode you are in."),
        SHOT("lens-folder-linked.png", "The popup project row with a folder linked, showing the folder name and the Change button"),

        H("Take your first capture"),
        STEPS([
            "Press **Capture region**|or use the keyboard shortcut. The page dims and the cursor becomes a crosshair.",
            "Drag a rectangle|over the area you want. Drag the handles to resize, or drag from the middle to move it.",
            "Press **Capture Image**|the save screen opens with your capture loaded, its tools down the left and the file name on the right.",
            "Annotate if you want to, then name it and save|the file lands in the project folder and appears in the popup timeline.",
        ]),
        SHOT("lens-region-selection.png", "A region selected on a web page, with the dimension pill above it and the Cancel / Record GIF / Capture Image toolbar below"),

        H("Where to go next"),
        UL([
            "[Capturing a region](capturing.html) — selection, annotation and saving in detail.",
            "[Recording GIF and MP4](recording.html) — the recorder, its controls and the two output formats.",
            "[Step-by-step guides](guides.html) — click through a flow once and get a documented walkthrough out of it.",
            "[Projects and folders](projects.html) — multiple projects, switching, and reconnecting folder access.",
            "[Settings](settings.html) — every preference and what it changes.",
        ]),
    ],
)

PAGES["capturing"] = dict(
    title="Capturing a Region",
    lede="Select, annotate and save a still image from any tab.",
    desc="Select a region of a page, annotate it with shapes, text and blur, then save it into your project folder.",
    icon="crop",
    blocks=[
        P("A still capture is one screen after the selection: the picture, the tools that change it, and the name it will be saved under are all in front of you at once. Nothing is written until you press Save."),

        H("Selecting the region"),
        P("Start a capture from the popup's **Capture region** button or the keyboard shortcut. The page dims, and the region you drag stays bright."),
        TABLE(["Action", "How"], [
            ["Draw a region", "Click and drag anywhere on the page"],
            ["Resize", "Drag any of the eight handles on the selection edge"],
            ["Move", "Drag from inside the selection"],
            ["Confirm", "Press **Capture Image**, or press Enter"],
            ["Cancel", "Press **Cancel**, or press Escape"],
        ]),
        P("The pill above the selection shows the size in CSS pixels and the native pixel size you will actually get — on a Retina display a 600×400 selection is captured at 1200×800."),
        SHOT("lens-selection-handles.png", "A selection with its eight resize handles visible and the dimension pill reading both CSS and native pixel sizes"),

        H("Capture full tab"),
        P("**Full tab** skips the selection step and captures the whole visible area of the tab. It does not capture below the fold — only what is on screen."),

        H("The private-data check"),
        P("As the save screen opens, Lens looks over the region it just captured for things that usually should not be shared, and shows a bar above the image listing what it found. Each one is outlined on the image so you can see exactly what would be covered."),
        P("It looks for password fields, fields named for a credential that have something in them, and text shaped like an API key, a JWT, a bearer token or a PEM private key. Unless you turn it off, it also flags email addresses and card numbers — card numbers are checksum-checked, so an order number is not mistaken for one."),
        UL([
            "Tick or untick anything in the list, then press **Blur selected** to cover the ticked ones in a single step that a single **Undo** reverses.",
            "**Dismiss** hides the bar and changes nothing.",
            "High-confidence findings are ticked for you; the rest are listed but left unticked.",
        ]),
        NOTE("The check runs on the structure of the page in your own browser. It uses no AI and sends nothing anywhere, and it is on by default. If you have connected an AI provider you can additionally let a model sort real credentials from documentation examples — see [Settings](settings.html)."),
        WARN("Treat it as a safety net, not a guarantee. It recognises known shapes, so it will not catch a secret that does not look like one, or a name or figure that is sensitive only in context. Read the capture as well."),
        SHOT("lens-redaction-hints.png", "The save screen with an amber bar above the image listing two flagged regions, an API key and a password field, each outlined on the screenshot below"),

        H("The save screen"),
        P("Confirming the selection opens the editor and the save form as a single screen. Down the left is a rail of tools, in the middle the picture, and on the right the panel for whichever tool is selected — with the file name and notes below it."),
        P("The rail has two halves. Above the divider are **marks** you add on top of the picture; below it are changes to the **picture itself**."),
        TABLE(["Tool", "What it does"], [
            ["Pen", "Freehand drawing. Hold Shift to constrain the line"],
            ["Text", "Click where the label goes, then type"],
            ["Box", "Drag a rectangle. Shift keeps it square"],
            ["Circle", "Drag an ellipse. Shift keeps it round"],
            ["Arrow", "Drag from the tail to the point"],
            ["Blur", "Pixelate a region — rewritten into the image data, not drawn over it"],
            ["Crop", "Trim the picture to a region or a fixed ratio"],
            ["Adjust", "Brightness, contrast, saturation, exposure and warmth, plus Auto"],
            ["Turn", "Rotate left or right, flip across or down"],
        ]),
        P("**Style** — colour, size and font — sits in the panel and applies to the next mark you make. Everything you add is listed under **Marks** in the order you made it, with blurs tagged *permanent*, so three edits later you can still see at a glance that a blur is in place."),
        SHOT("lens-capture-saver.png", "The save screen with the tool rail on the left, an annotated screenshot in the middle, and the style panel, marks list and file name on the right"),

        H("Cropping, adjusting and turning"),
        UL([
            "**Crop** opens on the whole picture — easier to pull inward than an empty box is to place. Ratio chips offer Free, Original, 1:1, 16:9, 4:3 and 3:2, and the readout shows the real pixel size you will get. **Apply crop** commits it.",
            "**Adjust** previews live against the picture as it was when you opened the tool, so dragging a slider back to the middle returns the exact original pixels rather than an approximation. **Auto** stretches the histogram to use the full range.",
            "**Turn** applies immediately — each rotation or flip is one step that Undo reverses.",
        ]),
        NOTE("Cropping or turning retires the private-data bar, because the regions it flagged no longer line up with the picture. Anything still sensitive is covered with the blur tool instead."),

        H("Undoing"),
        P("**⌘Z** (**Ctrl+Z**), or the Undo button under the picture. It steps back through everything — marks, crops, rotations and adjustments alike — restoring the size of the picture as well as its pixels, and taking the mark back off the list."),
        P("**Escape** works inward-out. In Crop, Adjust or Turn it leaves that tool. On a picture you have not drawn on, it closes the save screen. It will not throw away work you have done: undo that first, deliberately."),
        WARN("**Blur is irreversible and that is the point.** It rewrites the underlying pixels rather than covering them, so the original cannot be recovered from the saved file by removing a layer. Undo reverses a blur only while the save screen is still open — once the file is written, what was covered is gone."),

        H("Naming and saving"),
        P("Below the tools are the file name, an optional note, and the page title and URL that will be recorded alongside the capture."),
        UL([
            "The name is prefilled from your **file name pattern** — see [Settings](settings.html).",
            "The **note** is stored in `project_metadata.json` for that capture. Use it for context a file name cannot carry.",
            "**Save to project** (**⌘S**) writes the file. The footer says which project it is going to before you press it, and a toast afterwards says where it actually landed.",
            "**Copy image** puts it on the clipboard instead of saving.",
        ]),
        P("If you have connected an AI provider, a **Suggest name** button appears above the name field. It reads the text inside the region you captured and fills in a file name and a one-line description of what the screenshot shows. The description is added to your note rather than replacing it, and everything it writes is yours to edit."),
        NOTE("This is the one still-capture feature that sends the region's text to your provider, because describing a screenshot is the task. It only ever runs when you press the button — never as part of saving. If your provider is the browser's built-in model or one on your own machine, that text does not leave the device either way."),
        NOTE("The toast tells you the truth about where the file landed. If it says *Downloaded to Downloads*, the project folder was unavailable and the reason is in the message — most often folder access needs reconnecting."),
    ],
)

PAGES["recording"] = dict(
    title="Recording GIF and MP4",
    lede="Record a region of a tab as an animated GIF or an MP4 video.",
    desc="Record part of a tab as an animated GIF or MP4, with click-through interaction, navigation support and a converter for GIF output.",
    icon="video",
    blocks=[
        P("Lens records the region you select, not the whole screen, and you keep using the page while it records — clicks and scrolling pass straight through."),

        H("Starting a recording"),
        STEPS([
            "Press **Record GIF** in the popup|or use the recording shortcut. The region selector opens exactly as it does for a still capture.",
            "Drag the region and press **Record GIF**|on the selection toolbar.",
            "Use the page normally|a dashed red frame marks the recorded area and a REC widget shows elapsed time.",
            "Press **Stop & Convert**|when you are done.",
        ]),
        NOTE("The dashed frame and the REC widget sit **outside** the recorded region, so neither appears in the output. If your selection covers the whole viewport there is nowhere to put the widget, and it will be captured."),
        SHOT("lens-recording-active.png", "A page being recorded, with the dashed red frame around the region and the REC widget showing elapsed time and a Stop & Convert button"),

        H("Choosing GIF or MP4"),
        P("Set the output under **Settings > Capture and recording > Recording format**."),
        TABLE(["", "GIF", "MP4"], [
            ["Best for", "Embedding anywhere, no player needed", "Anything longer than a few seconds"],
            ["File size", "Large — tens of MB is normal", "Typically a small fraction of the GIF"],
            ["Colours", "256 per file, chosen automatically", "Full colour"],
            ["Conversion step", "Yes — a converter opens after you stop", "No — the file is ready when you stop"],
        ]),
        WARN("MP4 recording depends on your Chrome build. Where Chrome cannot encode MP4, Lens records **WebM** instead and names the file accordingly, so the extension always matches the actual contents. The Settings page tells you which one your browser will produce before you record."),

        H("The GIF converter"),
        P("Stopping a GIF recording opens a converter with a player, so you can check the result before committing to an encode."),
        UL([
            "**Framerate** — 10, 15, 24 or 30 frames per second.",
            "**Playback speed** — 0.5× to 2×, applied to the output, not just the preview.",
            "**Quality / scale** — 100%, 75% or 50%. Halving the scale is the fastest way to cut file size.",
            "The header shows how many frames were captured, the captured pixel size, and the region you selected.",
        ]),
        P("Encoding runs in the page and locks the controls while it works. Progress is shown on the bar."),
        SHOT("lens-gif-converter.png", "The GIF converter with the player showing a captured frame, the framerate, speed and scale controls, and the frame count in the header"),

        H("You also get a guide"),
        P("If the recording had clicks in it, Lens builds a **step-by-step guide** from it as well: a screenshot taken at the moment of each click, cropped to the control, numbered and captioned. It appears for review under the file name on the save screen, and nothing is written until you approve it — you can untick individual steps, or untick the guide entirely and keep just the recording."),
        P("This is on by default and needs no AI. See [Guides](guides.html) for the review panel, the editor and exporting. If you want the walkthrough without the video, **Record steps** (⌘⇧E) captures one with no recording behind it and no time limit."),

        H("Writing steps from what you clicked"),
        P("While a recording runs, Lens notes the name of each control you click — the name a screen reader would announce, never anything you type into a field. On the save screen, **Write steps from clicks** turns that into a numbered list and adds it to your note."),
        P("This works with no AI provider at all: the click list alone produces usable steps. If you have a provider connected, it rewrites the list into better prose instead — merging actions that are really one step and dropping navigation noise. The toast tells you which of the two you got."),
        UL([
            "The log follows the recording across pages, so a walkthrough that navigates keeps its steps.",
            "Repeated clicks on the same control within a second are treated as one step.",
            "Steps are added to your note, never over the top of what you already wrote.",
        ]),
        NOTE("If the recording had no clicks in it, the button does not appear — there is nothing to write."),

        H("Recording across page navigation"),
        P("A recording belongs to the **tab**, not the page. If you click a link and navigate, recording continues and the controls are rebuilt on the new page with the timer intact."),
        UL([
            "Navigating to a page Chrome does not allow extensions on — `chrome://` pages, the Web Store — keeps the recording going, but the on-page controls cannot be shown. Stop it from the popup instead.",
            "Closing the tab ends the recording and discards it.",
        ]),

        H("Stopping from another tab"),
        P("If you switch tabs, the Lens popup shows a **Recording** banner with the elapsed time and which tab it belongs to. **Stop & convert** there brings that tab forward and opens the converter; the cross button discards the recording."),
        SHOT("lens-popup-recording-banner.png", "The popup showing the red recording banner with elapsed time, the source tab name, and Stop & convert and discard buttons"),

        H("Length limit"),
        P("Recordings stop automatically at the cap set under **Settings > Maximum GIF recording length** — one minute by default, up to ten. When the cap is reached the recording stops and the converter opens as though you had pressed stop."),
    ],
)

PAGES["guides"] = dict(
    title="Step-by-step Guides",
    lede="Click through a flow once. Lens writes the walkthrough.",
    desc="Capture a step-by-step guide from your clicks, review it before saving, edit it in the guide editor and export it as HTML, Markdown or rich text.",
    icon="book",
    blocks=[
        P("A **guide** is a walkthrough of a flow: one screenshot per click, cropped to the control you clicked, numbered, with a sentence under each. You click through the task once and Lens assembles the document, rather than asking you to screenshot each step and paste them together afterwards."),
        NOTE("**No AI is involved in building a guide.** Step sentences come from the accessible name of each control — the name a screen reader would announce. That is also why nothing you type into a field is ever read. A connected model can rewrite those sentences afterwards; it never writes them in the first place."),

        H("Two ways to capture one"),
        P("**Record steps** (⌘⇧E, Alt+Shift+E) is the light one: no region to drag, no video, and **no time limit** — nothing accumulates between clicks, so a walkthrough can take as long as the work does."),
        STEPS([
            "Press **Record steps** in the popup|or use the shortcut. A small widget appears in the corner of the page.",
            "Click through your flow as you normally would|every click on a real control becomes a step. Scrolling is free, and a page load becomes a step of its own so the guide does not read as though everything happened on one screen.",
            "Press **Record clip** for anything a still cannot carry|a drag, a hover menu, an animation. Drag a region, do the thing, press **Stop clip**, and it is dropped in as one animated step in the place you recorded it.",
            "Press **Finish**|the review panel opens. There is no file to name, because the guide is the whole result.",
        ]),
        P("**Record GIF** (⌘⇧R) produces a guide as well as the recording, as long as **Build a guide from each recording** is on — it is by default. The review panel appears under the file name on the save screen."),
        NOTE("The region you drag limits the *recording*, not the steps. Each step screenshot is a fresh capture of the whole tab, cropped around whatever you clicked, so steps stay readable even when the recorded region was small."),
        SHOT("lens-steps-widget.png", "The walkthrough widget in the corner of a page, showing a step count, a clip count, and the Record clip, Finish and discard buttons"),

        H("What does not become a step"),
        UL([
            "Clicks on Lens's own controls. Pressing **Finish** does not appear in the guide it finishes.",
            "Clicks on nothing — empty space, a page background.",
            "A repeated click on the same control within a second, which is counted once.",
            "A drag or a text selection, which is not a click at all.",
        ]),

        H("Reviewing before anything is written"),
        P("Nothing reaches your folder until you approve it. The review panel lists every step with its screenshot, and you can:"),
        UL([
            "Edit the guide title, and the text of any step.",
            "Untick steps you do not want. They are dropped, and the rest renumber.",
            "Untick the guide entirely and keep just the recording.",
            "**Rewrite with AI** — only if you have a model connected. It refuses any answer that changes the number of steps, so it can improve the words but cannot invent or lose a step.",
        ]),
        SHOT("lens-guide-review.png", "The review panel on the save screen listing numbered steps with their screenshots, each with a checkbox and an editable caption"),

        H("Where guides live afterwards"),
        P("**Dashboard > Guides.** One card per guide, newest first, each showing the site's own logo — or its favicon where there is no logo, or a coloured initial where there is neither — with the title, the site, the step count, the project and the day it was captured."),
        TABLE(["Action", "What it does"], [
            ["Open editor", "Opens the guide as a document in its own tab"],
            ["Export", "Self-contained HTML, Markdown, or the clipboard"],
            ["Delete", "Removes the guide's folder on disk and the entry pointing at it. Asks first"],
        ]),
        NOTE("Guides recorded while no folder was linked are held in the browser and listed below the others as **pending**. They are not lost — link a folder, make that project active, and write them from there."),
        SHOT("lens-guides-list.png", "The dashboard Guides tab with guide cards, each showing the site's logo, title, step count and the folder path it was written to"),

        H("The guide editor"),
        P("The editor opens in its own tab and reads as a document: the sheet is the width of the exported page, and the steps run down it in order."),
        P("Step text is **Markdown**, and the toolbar offers exactly what Markdown can carry — bold, italic, strikethrough, code, highlight, links, bullet and numbered lists, task lists, tables, code blocks, rules, callouts and headings. Nothing else is offered on purpose: a font size or a colour would be something one of the two exports could not represent, and the same text is written to `guide.md` and rendered into `guide.html`."),
        TABLE(["Key", "What it does"], [
            ["⌘B / ⌘I", "Bold, italic"],
            ["⌘K", "Link"],
            ["⌘S", "Save"],
            ["⌘click", "Open a link — a plain click inside editable text places the caret instead, as it does everywhere"],
        ]),
        SHOT("lens-guide-editor.png", "The guide editor showing the dark chrome around a white document sheet, with numbered steps, their screenshots and the formatting toolbar"),

        H("Working on a step"),
        P("Hover a step. On the step itself:"),
        TABLE(["Control", "What it does"], [
            ["Move up / Move down", "Reorder. Numbers are rewritten, but **file names never change** — anything already exported still points at the right picture"],
            ["Add step above / below", "An empty step to write by hand"],
            ["Duplicate", "A copy, for when two steps differ by a word"],
            ["Split into individual clicks", "Breaks an animated step back apart. Lossless — each click kept its own still"],
            ["Copy step", "Text and picture together, ready to paste"],
            ["Delete", "The step goes, and its picture is removed from the folder when you save"],
        ]),
        P("On the screenshot itself you get the same image tools as a still capture — crop, annotate, blur, colour and rotation — plus **Replace image**, which swaps in a different file while keeping its name."),
        NOTE("Nothing is written until you press **Save**. Closing with unsaved changes asks first, and undo covers everything, including a rewrite the assistant applied."),

        H("Exporting"),
        TABLE(["Format", "What you get"], [
            ["**Self-contained HTML**", "`guide.html` with every picture inlined and no scripts. One file you can email, and ⌘P > Save as PDF is the PDF route"],
            ["**Markdown**", "`guide.md` beside its screenshots, relative paths, ready for a repo or a docs site"],
            ["**Copy to clipboard**", "Rich text for pasting into Confluence, Notion or a document"],
        ]),
        NOTE("Animated steps print their poster frame. When pasting into a document, check the pictures survived — editors disagree about pasted images and some drop them."),

        H("The assistant"),
        P("The editor has a chat panel, and it stays shut until you have configured a model **and** a test has actually reached it. See [AI features](ai.html) for setting one up."),
        UL([
            "**Step** and **Guide** attach material to *this* message. A question with nothing attached sends only the question.",
            "**Media** additionally sends the screenshots of what you attached. Off by default — the files are not even read unless it is on.",
            "The **model switcher** picks which of your configured models answers, per message.",
            "**Auto** applies a proposed rewrite as it arrives rather than waiting for a click. Off by default, and undo reverses it.",
        ]),
        WARN("If a request fails, the panel says so and stops. It has no offline imitation of a model — inventing documentation for software it cannot see is the one thing a documentation tool must never do."),
    ],
)

PAGES["projects"] = dict(
    title="Projects and Folders",
    lede="Organise captures into named projects, each writing to its own local folder.",
    desc="Create projects, link local folders, switch the active project and reconnect folder access when Chrome drops it.",
    icon="folder",
    blocks=[
        P("Every capture goes into the **active project**. A project is a name and, optionally, a folder on your machine that Lens has been granted access to."),

        H("Creating a project"),
        STEPS([
            "Press **New project** in the popup, or **New project** on the dashboard|both open the same flow.",
            "Give it a name|this is what appears in the project dropdown and in `project_metadata.json`.",
            "Pick a folder|Chrome asks for read/write access to that one folder.",
        ]),

        H("What Lens writes into the folder"),
        UL([
            "The capture files themselves — `.png`, `.jpg`, `.gif`, `.mp4` or `.webm`.",
            "`project_metadata.json` — a timeline entry per capture recording the file name, page title, page URL, timestamp, the captured region and your note.",
        ]),
        P("The metadata file is plain JSON and is meant to be read by other tools. Every entry and the file itself carry `\"createdBy\": \"Lens by Vectored\"`."),
        SHOT("lens-project-folder.png", "A project folder in Finder showing captured PNG and GIF files alongside project_metadata.json"),

        H("Switching the active project"),
        P("Use the dropdown at the top of the popup. Only the active project receives new captures; the others keep their files and history untouched."),

        H("When folder access is lost"),
        P("Chrome does not keep folder permission forever. After a browser restart or an extension reload it can lapse, and the extension's background worker is not allowed to ask for it back on its own."),
        P("When that happens the popup shows **access lost** next to the folder name and the button changes to **Reconnect**. One click restores it. The dashboard shows the same state on the project card."),
        WARN("While access is lost, captures do not fail — they fall back to the **Downloads** folder under `Lens-Captures/`, and the save toast says so. They still appear in the timeline, so nothing is silently dropped, but they are not in your project folder until you move them."),
        SHOT("lens-folder-access-lost.png", "The popup folder row showing the amber access lost flag and the Reconnect button"),

        H("Deleting a project"),
        P("Delete a project from the dashboard's project card. This removes it from Lens only — **files already written to disk are left alone**. The default project is protected and cannot be deleted."),
    ],
)

PAGES["timeline"] = dict(
    title="Timeline and Dashboard",
    lede="Review, search and export everything you have captured.",
    desc="Browse captures in the popup timeline and the dashboard master timeline, search and filter them, and export the metadata as JSON.",
    icon="list",
    blocks=[
        P("Lens keeps two views of what you have captured: a compact timeline in the popup for the active project, and a master timeline on the dashboard covering every project."),

        H("The popup timeline"),
        P("Captures are grouped by day, newest first, with the time down the left. Each row shows a thumbnail, the file name, its type and the page title."),
        TABLE(["Control", "What it does"], [
            ["Thumbnail", "Opens a larger preview with the page URL and capture time"],
            ["Copy", "Puts the image on the clipboard"],
            ["Rename", "Renames the file on disk and in the metadata"],
            ["Delete", "Removes the entry from the timeline"],
            ["Search", "Filters by file name, page title or URL"],
            ["JSON", "Exports `project_metadata.json` for the active project"],
        ]),
        SHOT("lens-popup-timeline.png", "The popup timeline with captures grouped under Today and Yesterday, each row showing thumbnail, file name, type badge and page title"),

        H("The dashboard"),
        P("Open the dashboard from the arrow icon at the top right of the popup. It has three sections."),
        UL([
            "**Projects** — every project as a card with its folder, capture count, last capture and access state.",
            "**Timeline** — every capture across all projects, grouped by project.",
            "**Settings** — all preferences, plus your keyboard shortcuts.",
        ]),
        SHOT("lens-dashboard-projects.png", "The dashboard Projects tab showing project cards with folder, capture count, last capture and status badges"),

        H("Searching and filtering"),
        P("The master timeline's filter bar stays fixed as you scroll and combines free-text search across name, page title and URL, a project filter, and a type filter for PNG or GIF. The count on the right reflects what is currently shown."),

        H("Grouping"),
        P("The master timeline is grouped by **project** by default. Projects are ordered by their most recent capture, so whatever you are working on now is at the top, and captures stay newest-first inside each one."),
        P("**Group by day** in the filter bar switches to date headings instead — useful for answering \"what did I do yesterday\" rather than \"show me this project\". Each card shows whichever of the two the heading does not: the date inside a project group, the project name inside a day group."),
        NOTE("Your choice is remembered, so the timeline opens the way you left it."),
        SHOT("lens-dashboard-timeline.png", "The dashboard master timeline with the filter bar and capture cards grouped under project headings, each card showing its captured size and type badge"),

        H("Exporting"),
        UL([
            "**Export timeline JSON** on the dashboard writes every capture across all projects to a single file.",
            "**JSON** in the popup, or **Export JSON** on a project card, writes that one project's `project_metadata.json`.",
        ]),

        H("Cached previews"),
        P("Thumbnails are held in extension storage so the timeline loads instantly. **Settings > Clear cached previews** empties that cache. Files already written to disk are untouched — only the thumbnails go, and the timeline then shows a placeholder icon in their place."),
    ],
)

PAGES["ai"] = dict(
    title="AI Features",
    lede="Off by default. When you turn them on, you choose who does the work.",
    desc="Lens AI features, the providers you can connect, exactly what each feature sends, and how your API key is stored.",
    icon="sparkles",
    blocks=[
        NOTE("Every AI feature is off when you install Lens, and with no provider selected the extension makes no network requests at all. Nothing on this page happens until you choose one."),

        P("Lens has no AI service of its own. There is no Vectored model, no Vectored endpoint and no Vectored proxy — instead you pick who does the work, and that choice decides whether anything leaves your machine."),

        H("Choosing a provider"),
        TABLE(["Provider", "Where it runs", "What leaves your machine", "You need"], [
            ["**None** — the default", "Nowhere", "Nothing", "—"],
            ["**Your browser's built-in model**", "On your device", "Nothing", "Edge or Chrome with the model available"],
            ["**A local model**", "On your device", "Nothing", "Ollama, LM Studio or similar"],
            ["**Claude**", "Anthropic's servers", "The prompt for the feature you used", "An Anthropic API key"],
            ["**Gemini**", "Google's servers", "The prompt for the feature you used", "A Google AI API key"],
            ["**OpenAI or compatible**", "OpenAI, or an endpoint you name", "The prompt for the feature you used", "An API key"],
        ]),
        P("Choosing one that runs in the cloud asks you to confirm first, because it genuinely changes what the extension does with page text."),

        H("Configuring more than one"),
        P("You are not limited to a single choice. Settings holds as many models as you like — a local one for everyday work and a hosted one for the harder rewrites, say — each saved with its own key and its own model name."),
        UL([
            "**Test** is not optional. A model is marked usable only once a test has actually reached it, because a key that looks well-formed is not a model that answers. Until then, the features that depend on it stay shut.",
            "One is the **active** model, used by the buttons on the capture screens.",
            "In the guide editor's assistant you switch between them **per message**, so a question can go to a different model than the last one did.",
        ]),
        SHOT("lens-ai-profiles.png", "The AI assistance panel on the Settings page listing several configured models, each with its provider, model name and a verified badge"),
        SHOT("lens-ai-provider.png", "The AI assistance panel on the Settings page with the provider dropdown open, showing the built-in, local, Claude and OpenAI options"),

        H("What each feature sends"),
        P("Only what that feature needs. The amounts differ, so they are listed separately rather than summarised."),
        TABLE(["Feature", "How it runs", "What the prompt contains"], [
            ["Sharpen the private-data check", "Automatically, only if you switch it on", "The **type** of each flagged region — \"an AWS access key\", \"a password field\" — plus the page title and heading. Never the flagged text."],
            ["Suggest name", "A button you press, per capture", "The page title and heading, the names of controls in the region, and **the text inside the region you captured**."],
            ["Write steps from clicks", "A button you press, per recording", "The page title and the names of the controls you clicked. Never anything you typed into a field."],
            ["Rewrite a guide's steps", "A button you press, on the review panel", "The step sentences Lens already wrote. The answer is rejected outright if it changes the number of steps."],
            ["The guide editor's assistant", "A message you send, per message", "Your message, plus **whatever you attached to it** — a step, several steps, the whole guide, or a text selection — and nothing else. A question with nothing attached sends only the question."],
        ]),
        P("Images are sent in one case only: the assistant's **Media** switch, which is off by default. With it off the screenshots are not even read from disk. Everywhere else, captured images are never sent to any provider. Lens does not keep a copy of any prompt or response."),
        NOTE("**Write steps from clicks** works with no provider at all — the click list alone produces usable numbered steps, and a model only rewrites them into better prose. The toast tells you which of the two you got."),

        H("Setting up the browser's built-in model"),
        P("Edge and Chrome both expose an on-device model to extensions. Nothing is configured and nothing leaves the device, but the model has to be downloaded once and the hardware bar is real."),
        STEPS([
            "Open the Lens dashboard and go to Settings|then **AI assistance**.",
            "Choose **Browser's built-in model**|no key or address is needed.",
            "Press **Test connection**|it reports whether the model is present, unavailable, or not yet downloaded.",
            "Press **Download model** if it appears|the download is several gigabytes and reports its progress. Lens never starts it during a capture.",
        ]),
        WARN("On Microsoft Edge this currently requires the Canary or Dev channel with the **Prompt API for on-device language model** flag enabled, and a capable GPU. If your device does not meet the bar, use a local model or a hosted provider instead — the rest of Lens is unaffected."),
        NOTE("Edge's built-in model is text-only. That is why every Lens AI feature is built on page text and structure rather than on the image, and why it behaves the same in both browsers."),

        H("Setting up a local model"),
        P("A model running on your own machine keeps everything on the device while giving you a full-size model. Anything that speaks the OpenAI chat format works — Ollama, LM Studio, llama.cpp, vLLM."),
        STEPS([
            "Start your server|for Ollama that is `ollama serve`, and `ollama pull <model>` once for the model itself.",
            "Choose **Local model** in Settings|then enter the server address and the model name.",
            "Press **Test connection**|this actually contacts the server, so a wrong address or a stopped server is reported here rather than mid-capture.",
        ]),

        H("Setting up Claude, Gemini or OpenAI"),
        P("These run on the provider's servers. Lens sends the request straight from your browser using your key — there is no Vectored server in the path, and we never receive the key or the prompt."),
        STEPS([
            "Create an API key with that provider|Lens cannot create one for you.",
            "Choose the provider in Settings and confirm the prompt|it explains what changes before anything is saved.",
            "Paste the key and pick a model|the key is saved as soon as you leave the field.",
            "Press **Test connection**|then use a feature to confirm end to end.",
        ]),

        H("How your API key is stored"),
        UL([
            "In this browser only, in its own storage area, kept apart from your other settings.",
            "Read only by the extension's background worker — never by the code Lens puts into a page. Injected code shares a process with the page it is injected into, so a key is never placed there.",
            "The Settings page can tell you a key is saved but cannot show it back to you.",
            "Sent only to the provider it belongs to. Vectored never receives it, and there is nowhere for it to be sent to us.",
            "Removed when you clear the field, and when you uninstall the extension.",
        ]),
        WARN("Scope the key to the minimum the provider allows. Anything the key can do, a mistake can do."),

        H("What the model is allowed to change"),
        P("For the private-data check specifically, the model's influence is bounded on both sides. It can re-rank and relabel what the local rules already found. It cannot add a region, it cannot blur anything, and it cannot clear a high-confidence finding such as a password field or a key matching a known format."),
        P("That last limit exists because the page being captured is the same page whose title and headings go into the prompt. A hostile page could try to write something into the prompt to talk the model out of a finding — so on the findings that matter most, it is not able to."),

        H("When something does not work"),
        TABLE(["What you see", "What it means"], [
            ["The suggest button is not there", "No model is configured, or none has passed a test. Set one up in Settings."],
            ["The assistant will not open", "Same reason. It stays shut until a test has actually reached a model, rather than opening and failing on your first message."],
            ["\"That provider still needs an API key or a model name\"", "The configuration is incomplete."],
            ["\"still needs to download\"", "The built-in model has not been fetched. Use **Download model** on the Settings page."],
            ["\"did not answer in time\"", "The provider was too slow. Nothing was changed; try again or pick a faster model."],
            ["\"answer could not be read\"", "The model did not return usable JSON. Nothing was changed. A larger model usually fixes this."],
            ["Not available on this machine", "The built-in model is unsupported here — see the hardware note above."],
        ]),
        NOTE("Every one of these leaves your capture exactly as it was. No AI failure can lose work, block a capture, or change an image."),

        H("Where to read the rest"),
        P("The [privacy policy](../privacy.html#ai) sets out what each feature sends and whose terms apply to it. The [security page](../security.html#ai) covers key handling and why the request is made where it is."),
    ],
)

PAGES["settings"] = dict(
    title="Settings",
    lede="Every preference, and exactly what it changes.",
    desc="Reference for every Lens setting: recording and image format, guides, private-data flagging, AI models, file name pattern, clipboard, metadata and sounds.",
    icon="sliders",
    blocks=[
        P("Settings live on the dashboard under **Settings**, and apply to every project. A change takes effect on your next capture, not one already in progress."),

        H("Recording format"),
        P("**GIF** or **MP4**. See [Recording](recording.html) for the trade-off. The description under the control tells you whether your Chrome build can encode MP4, or will fall back to WebM."),

        H("Maximum GIF recording length"),
        P("One to ten minutes. A recording stops at the cap and opens the converter as though you had pressed stop. This exists because a long recording at 15 frames a second becomes a very large GIF."),

        H("Still image format"),
        P("**PNG** keeps text crisp and is the right default for documentation. **JPEG** produces much smaller files but softens text and adds artefacts around high-contrast edges. The file extension follows the setting."),

        H("Write metadata file"),
        P("On by default. When off, capture files are still written to the project folder but `project_metadata.json` is not updated — so those captures will not appear in the timeline read from that folder."),

        H("Copy to clipboard on capture"),
        P("Puts each capture on the clipboard as well as saving it. Because the clipboard only accepts PNG images, a JPEG capture is converted before copying. The save toast reports whether the copy succeeded."),

        H("Visualise clicks"),
        P("Draws a marker at each click while recording, so a walkthrough shows where you clicked. Markers are only drawn **inside** the recorded region — a marker outside it would never appear in the output."),
        SHOT("lens-click-marker.png", "A recording in progress with a red click marker expanding at the point of a click inside the recorded region"),

        H("Play shutter sound"),
        P("A short camera click when a capture completes. It is synthesised in the page, so nothing is downloaded and no audio file ships with the extension."),

        H("Flag private data in captures"),
        P("On by default. Checks each captured region for credentials before you save and offers to blur them — see [Capturing](capturing.html) for what the bar looks like and what it recognises. It reads the page structure in your browser: no AI, no network call, nothing sent anywhere."),

        H("Also flag emails and card numbers"),
        P("On by default, and only has an effect while the check above is on. Widens it past credentials to personal data. Card numbers are validated against their checksum, so order and reference numbers are not flagged."),

        H("Build a guide from each recording"),
        P("On by default. Any recording with clicks in it also produces a step-by-step guide, offered for review on the save screen — see [Guides](guides.html). Turn it off and recordings are just recordings."),

        H("Auto-blur guide steps"),
        P("**Off**, and deliberately so. When on, anything the private-data check flags in a step screenshot is blurred without asking."),
        WARN("This is the only place in Lens where blurring happens without a click, and blurring cannot be undone once saved. It exists because clicking through the findings on a forty-step guide is impractical — but it means a false positive is covered permanently, so leave it off unless you have a reason."),

        H("Guide marker colour"),
        P("The colour of the numbered callout drawn on each step screenshot. Red by default. Pick something that stands out against the product you are documenting."),

        H("Maximum steps per guide"),
        P("Sixty by default. A flow longer than that is usually two guides, and the cap stops a stray click storm from producing a document nobody will read."),

        H("Guide image format"),
        P("**JPEG** by default here, rather than PNG. A sixty-step guide is sixty screenshots, and JPEG is what keeps that folder to a sane size. Switch to PNG if your steps are mostly small text."),

        H("Merge clicks into animated steps"),
        P("Off by default. When several clicks happen on one screen with no scrolling between them, they can be saved as one short animated step instead of a run of near-identical stills."),
        P("The clip is cut from footage the recording already sampled, so nothing is captured twice. Three controls tune it: the longest gap between clicks that still counts as one run, the longest a merged step may be, and its frame rate. An animated step can always be split back into its individual clicks in the editor — each click kept its own still."),

        H("AI models"),
        P("**None configured** by default, which means every AI feature is off and Lens makes no network requests at all. Lens has no AI service of its own — you choose who does the work, and that choice decides whether anything leaves your machine."),
        TABLE(["Provider", "Runs", "Needs"], [
            ["Your browser's built-in model", "On your device", "Edge or Chrome with the model available"],
            ["A local model", "On your device", "Ollama, LM Studio or similar, and the model name"],
            ["Claude", "Anthropic's servers", "An Anthropic API key"],
            ["Gemini", "Google's servers", "A Google AI API key"],
            ["OpenAI or compatible", "OpenAI's servers, or an endpoint you name", "An API key"],
        ]),
        P("Add as many as you like. Each is saved with its own key and model name, one is marked active for the capture screens, and the guide editor's assistant lets you switch between them per message."),
        P("Picking one that runs in the cloud asks you to confirm first, because it changes what the extension does with page text. **Test** actually contacts the model, and a model that has not passed one is not offered anywhere — a key that looks well-formed is not a model that answers."),
        NOTE("An API key is stored in this browser only, in its own storage area, and is read only by the extension's background worker — never by the code Lens injects into a page. The settings screen can tell you a key is saved but cannot show it back to you. Vectored never receives it; see the [privacy policy](../privacy.html#ai)."),

        P("Connecting a model also puts buttons on the save screens — **Suggest name** on a screenshot, **Write steps from clicks** on a recording, **Rewrite with AI** on a guide — and opens the assistant in the guide editor. None of them runs on its own: you press them, per capture. See [Capturing](capturing.html), [Recording](recording.html) and [Guides](guides.html)."),

        H("Let the model sharpen redaction hints"),
        P("Off even when a provider is set. Lets the model re-rank what the check above found, so a key in a documentation example is not flagged as hard as one in a live console."),
        P("The model is told the **type** of each flagged region and the page title and heading — never the flagged text itself. Sending a key to a model to ask whether it is a key would defeat the feature. The model can only re-rank and relabel: it cannot add a region, and it cannot blur one."),

        H("File name pattern"),
        P("Controls the name each capture is given before you edit it. The extension is added automatically."),
        TABLE(["Token", "Expands to", "Example"], [
            ["`{name}`", "The capture type — `Lens` for stills, `LensRecord` for recordings", "Lens"],
            ["`{date}`", "Capture date", "2026-08-17"],
            ["`{time}`", "Capture time", "09-04-07"],
            ["`{index}`", "A counter that increments through the day and resets at midnight", "007"],
        ]),
        P("Anything else in the pattern is kept as written. Characters a file system rejects — `/ \\ : * ? \" < > |` — are replaced with a dash. The line under the field previews the name your next capture will get."),
        NOTE("Clear the field and it returns to the default, `{name}_{date}_{time}`."),

        H("Keyboard shortcuts"),
        P("The Settings page lists the shortcuts currently bound, read from Chrome rather than hardcoded, so it always reflects reality. See [Keyboard shortcuts](shortcuts.html) to change them."),
    ],
)

PAGES["shortcuts"] = dict(
    title="Keyboard Shortcuts",
    lede="The default bindings, and how to change them.",
    desc="Lens keyboard shortcuts for region capture, GIF recording and full-tab capture, and how to remap them in Chrome.",
    icon="keyboard",
    blocks=[
        P("Lens registers four commands. Chrome owns the bindings, so they are changed in Chrome rather than in the extension."),
        TABLE(["Command", "macOS", "Windows / Linux", "What it does"], [
            ["Capture region", "⌘⇧S", "Alt+Shift+S", "Opens the region selector"],
            ["Capture full tab", "⌘⇧F", "Alt+Shift+F", "Captures the visible tab with no selection step"],
            ["Record steps", "⌘⇧E", "Alt+Shift+E", "Starts a walkthrough — a screenshot per click, no video, no time limit"],
            ["Record GIF region", "⌘⇧R", "Alt+Shift+R", "Opens the region selector ready to record"],
        ]),

        H("Inside the save screen"),
        P("These are not Chrome commands and cannot be rebound — they belong to the editor that opens after a capture."),
        TABLE(["Key", "What it does"], [
            ["⌘S / Ctrl+S", "Save into the project folder"],
            ["⌘Z / Ctrl+Z", "Undo the last mark, crop, rotation or adjustment"],
            ["Escape", "Leave the tool you are in; on an unedited picture, close the save screen"],
            ["Shift", "Held while dragging, constrains a shape — a square, a circle, a straight line"],
            ["Enter", "In the file name field, saves"],
        ]),

        H("Changing a shortcut"),
        STEPS([
            "Open `chrome://extensions/shortcuts`|or follow the link at the top of the Settings page on the dashboard.",
            "Find Lens in the list|each command has its own row.",
            "Click the field and press the combination|Chrome refuses combinations already taken by the browser or another extension.",
        ]),
        NOTE("Chrome allows a limited number of *suggested* shortcuts per extension, and any command can be left unbound. An unbound command shows as **not set** on the Settings page; the popup buttons still work."),

        H("When a shortcut does nothing"),
        UL([
            "The tab is a page Chrome does not allow extensions on — `chrome://` pages, the Web Store, the PDF viewer. The toolbar icon shows a red **!** and its tooltip explains why.",
            "Another extension has claimed the same combination. Chrome gives it to whichever registered first; rebind one of them.",
            "The page has not finished loading. Wait for it and try again.",
        ]),
        P("See [Troubleshooting](troubleshooting.html) for the full list of pages capture cannot run on."),
    ],
)

PAGES["troubleshooting"] = dict(
    title="Troubleshooting",
    lede="What the errors mean and what to do about them.",
    desc="Diagnose blocked pages, blank recordings, lost folder access and captures missing from the timeline.",
    icon="life-buoy",
    blocks=[
        P("Lens reports failures where it can — an in-page toast when a content script can run, and the toolbar icon badge when one cannot."),

        H("This page cannot be captured"),
        P("Chrome forbids extensions from running on some pages, and no extension can work around it."),
        UL([
            "`chrome://` and `about:` pages, including New Tab and Settings",
            "The Chrome Web Store",
            "`devtools://` and `view-source:` pages",
            "Other extensions' pages",
            "The built-in PDF viewer",
            "`file://` URLs, unless you enable **Allow access to file URLs** for Lens on `chrome://extensions`",
        ]),
        P("On these pages the toolbar icon shows a red **!** with the reason in its tooltip, because a toast cannot be drawn."),

        H("The recording came out blank"),
        P("Tab capture succeeds on protected video but returns solid black — sites using DRM, such as YouTube and Netflix, are excluded from capture by design. Lens samples the recorded frames and warns you when they look blank, but still opens the converter so you can judge for yourself."),
        P("If a whole page records black, the page is blocking capture. If only a video player area is black, that player is protected and the rest of the page is fine."),

        H("Captures are going to Downloads instead of my folder"),
        P("Folder access has lapsed. Open the popup: the folder row shows **access lost** and a **Reconnect** button. One click fixes it."),
        P("This happens because re-granting folder access requires a click, and the extension's background worker never has one — so it cannot recover on its own. See [Projects and folders](projects.html)."),

        H("A capture saved but is not in the timeline"),
        P("The file was written but `project_metadata.json` could not be updated. The save toast says so explicitly. Two causes:"),
        UL([
            "**Write metadata file** is switched off in Settings — turn it back on.",
            "The metadata file could not be written, usually a permission problem on the folder. Reconnect the folder.",
        ]),
        NOTE("The timeline merges the folder's metadata with a local cache, so a capture that went to Downloads still appears — it is just not in your project folder."),

        H("\"No frames were captured\""),
        P("The recording produced nothing to encode. Usually the tab was hidden or minimised for the whole recording — tab capture samples what is being drawn, and a tab that is not being drawn produces nothing. Check the tab stayed visible and record again."),

        H("My guide is not in the folder"),
        P("A guide is written when you approve it on the save screen. If no folder was linked at that moment it is held in the browser instead and listed under **Dashboard > Guides** as **pending**. Link a folder, make that project active, and write it from there — nothing is lost in the meantime."),

        H("The MP4 I recorded is a WebM"),
        P("Your Chrome build cannot encode MP4. Lens falls back to WebM and names the file for what it actually wrote, rather than giving you an `.mp4` that is not one. The Settings page says which format your browser will produce. Updating Chrome usually resolves it."),

        H("Nothing happened when I pressed the shortcut"),
        P("See [Keyboard shortcuts](shortcuts.html) — the usual causes are a restricted page, a conflicting binding, or a page that has not finished loading."),

        H("Still stuck"),
        P("[Open a support ticket](../support.html) and include what you were capturing, which browser version you are on, and what the toast or tooltip said. No account is needed."),
    ],
)

# Sidebar order.
ORDER = [
    "getting-started",
    "capturing",
    "recording",
    "guides",
    "projects",
    "timeline",
    "settings",
    "ai",
    "shortcuts",
    "troubleshooting",
]
