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
        P("Lens is a Chrome extension that captures a region of any tab as a **PNG**, a **JPEG**, an animated **GIF** or an **MP4**, then files it into a folder on your own machine along with a metadata timeline. Nothing is uploaded — see [Privacy](../privacy.html)."),

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
            "Press **Capture Image**|the annotation editor opens with your capture loaded.",
            "Name it and save|the file lands in the project folder and appears in the popup timeline.",
        ]),
        SHOT("lens-region-selection.png", "A region selected on a web page, with the dimension pill above it and the Cancel / Record GIF / Capture Image toolbar below"),

        H("Where to go next"),
        UL([
            "[Capturing a region](capturing.html) — selection, annotation and saving in detail.",
            "[Recording GIF and MP4](recording.html) — the recorder, its controls and the two output formats.",
            "[Guides and Guide Mode](guides.html) \u2014 record a click-by-click walkthrough, share it, and play it back on the live page.",
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
        P("A still capture is a two-step flow: choose the region on the page, then annotate and name it in the editor."),

        H("Selecting the region"),
        P("Start a capture from the popup's **Capture region** button or the keyboard shortcut. The page dims, and the region you drag stays bright."),
        TABLE(["Action", "How"], [
            ["Draw a region", "Click and drag anywhere on the page"],
            ["Resize", "Drag any of the eight handles on the selection edge"],
            ["Move", "Drag from inside the selection"],
            ["Confirm", "Press **Capture Image**, or press Enter"],
            ["Cancel", "Press **Cancel**, or press Escape"],
        ]),
        P("The pill above the selection shows the size in CSS pixels and the native pixel size you will actually get — on a Retina display a 600x400 selection is captured at 1200x800."),

        H("Capturing a hover state or an open menu"),
        P("A hover, a dropdown and a pop-up menu all close the moment you click anywhere else \u2014 including on the **Capture Image** button \u2014 so on their own they can never be photographed. The delay beside that button solves it: choose **3s**, **5s**, **10s** or **30s** and Lens hands the page back to you for that long before the shutter fires."),
        STEPS([
            "Drag the region|over the area the menu or tooltip will appear in, not over the control that opens it.",
            "Pick a delay|from the clock menu on the left of the capture toolbar.",
            "Press **Capture Image**|the toolbar controls disappear, the region stays outlined, and the count starts.",
            "Set the page up|hover the control, open the menu, focus the field. Clicks, hovers and scrolling all reach the page normally.",
            "Wait|the capture is taken automatically when the count reaches zero.",
        ]),
        P("The count runs in the capture toolbar, in the place the delay was chosen. **Cancel** or **Escape** calls it off and gives you the selection back, still adjustable. Your choice is remembered for the rest of the session, so a run of captures that all need the same pause only needs setting once."),
        NOTE("Native dropdowns \u2014 a plain `<select>` \u2014 are drawn by the operating system rather than by the page, so Chrome cannot photograph them and they will not appear. Menus, tooltips, hover states and focus rings built in HTML and CSS, which is the great majority, all capture normally."),
        WARN("The region is fixed to the screen, not to the page. If you scroll during the delay, the capture takes whatever has moved under the box."),
        SHOT("lens-selection-handles.png", "A selection with its eight resize handles visible and the dimension pill reading both CSS and native pixel sizes"),

        H("Capture full tab"),
        P("**Full tab** skips the selection step and captures the whole visible area of the tab. It does not capture below the fold — only what is on screen."),

        H("Annotating"),
        P("After confirming, the editor opens with a toolbar above the image."),
        TABLE(["Tool", "What it does"], [
            ["Pen", "Freehand drawing"],
            ["Text", "Click to place a text label"],
            ["Rectangle", "Outline a box"],
            ["Ellipse", "Outline a circle or oval"],
            ["Arrow", "Point at something"],
            ["Blur", "Pixelate a region — applied to the image data, not drawn over it"],
            ["Undo", "Step back one annotation"],
            ["Reset", "Discard all annotations and start from the original capture"],
        ]),
        WARN("**Blur is irreversible and that is the point.** It rewrites the underlying pixels rather than covering them, so the original content cannot be recovered from the saved file by removing a layer. Use it for tokens, names and anything else that should not leave your machine — but check the result before saving, because Undo after a blur restores the pixels only within the current editing session."),
        SHOT("lens-annotation-editor.png", "The annotation editor with the toolbar visible and an arrow, a text label and a blurred region applied to a screenshot"),

        H("Naming and saving"),
        P("Below the image are the file name, an optional note, and the page title and URL that will be recorded alongside the capture."),
        UL([
            "The name is prefilled from your **file name pattern** — see [Settings](settings.html).",
            "The **note** is stored in `project_metadata.json` for that capture. Use it for context a file name cannot carry.",
            "Press **Save** to write the file. A toast confirms where it went.",
        ]),
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
            "**Timeline** — every capture across all projects, grouped by day.",
            "**Settings** — all preferences, plus your keyboard shortcuts.",
        ]),
        SHOT("lens-dashboard-projects.png", "The dashboard Projects tab showing project cards with folder, capture count, last capture and status badges"),

        H("Searching and filtering"),
        P("The master timeline's filter bar stays fixed as you scroll and combines three filters: free-text search across name, page title and URL; a project filter; and a type filter for PNG or GIF. The count on the right reflects what is currently shown."),
        SHOT("lens-dashboard-timeline.png", "The dashboard master timeline with the filter bar and capture cards grouped by day, each showing its captured size and type badge"),

        H("Exporting"),
        UL([
            "**Export timeline JSON** on the dashboard writes every capture across all projects to a single file.",
            "**JSON** in the popup, or **Export JSON** on a project card, writes that one project's `project_metadata.json`.",
        ]),

        H("Cached previews"),
        P("Thumbnails are held in extension storage so the timeline loads instantly. **Settings > Clear cached previews** empties that cache. Files already written to disk are untouched — only the thumbnails go, and the timeline then shows a placeholder icon in their place."),
    ],
)

PAGES["settings"] = dict(
    title="Settings",
    lede="Every preference, and exactly what it changes.",
    desc="Reference for every Lens setting: recording format, image format, file name pattern, clipboard, metadata, click markers and the shutter sound.",
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

        H("Open Lens after saving"),
        P("On by default. A capture that is written opens the Lens menu on its timeline with the new row picked out, so a save is seen rather than taken on trust from a toast. A saved guide opens the dashboard's Guides tab instead. Turn it off for a long run of captures."),

        H("Explain Smart Capture before it starts"),
        P("On by default. Shows how a walkthrough is recorded \u2014 when each screenshot is taken, how fast you can click, what does and does not become a step \u2014 with **Start recording** and **Cancel**, before anything is recorded. The dialog can also be dismissed for good from itself."),

        H("Watermark"),
        P("Lens draws a small mark in the corner of the images it saves, and tiles it faintly through exported documents \u2014 PDF and self-contained HTML \u2014 with a line at the foot of Markdown and clipboard copies."),
        P("A licence puts it under your control: your own wording and logo, or off entirely. Without one, the mark stays. Everything else Lens does is unaffected either way \u2014 see [the licence](../index.html)."),
        NOTE("Where a guide came from is recorded separately and is never removed: the source page, the date and the author are written into every export whatever the licence says. Only the visible mark is licensed."),

        H("Play shutter sound"),
        P("A short camera click when a capture completes. It is synthesised in the page, so nothing is downloaded and no audio file ships with the extension."),

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
        P("Lens registers three commands. Chrome owns the bindings, so they are changed in Chrome rather than in the extension."),
        TABLE(["Command", "macOS", "Windows / Linux", "What it does"], [
            ["Capture region", "⌘⇧S", "Alt+Shift+S", "Opens the region selector"],
            ["Record GIF region", "⌘⇧R", "Alt+Shift+R", "Opens the region selector ready to record"],
            ["Capture full tab", "⌘⇧F", "Alt+Shift+F", "Captures the visible tab with no selection step"],
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

        H("The MP4 I recorded is a WebM"),
        P("Your Chrome build cannot encode MP4. Lens falls back to WebM and names the file for what it actually wrote, rather than giving you an `.mp4` that is not one. The Settings page says which format your browser will produce. Updating Chrome usually resolves it."),

        H("Nothing happened when I pressed the shortcut"),
        P("See [Keyboard shortcuts](shortcuts.html) — the usual causes are a restricted page, a conflicting binding, or a page that has not finished loading."),

        H("Still stuck"),
        P("[Open a support ticket](../support.html) and include what you were capturing, which browser version you are on, and what the toast or tooltip said. No account is needed."),
    ],
)

# Sidebar order.
PAGES["guides"] = dict(
    title="Guides and Guide Mode",
    lede="Record a click-by-click walkthrough, edit it, share it, and play it back on the live page.",
    desc="Record a step-by-step guide with Lens Smart Capture, edit the steps, export it as HTML, Markdown or PDF, share it with a colleague, and replay it on the live page with Guide Mode.",
    icon="list",
    blocks=[
        P("A **guide** is a numbered sequence of steps, each with its own screenshot and the control it points at. Lens records one by watching your clicks \u2014 there is no region to drag and no video behind it."),

        H("Recording one"),
        P("Press **Smart Capture** in the popup, or its keyboard shortcut. A briefing appears first, explaining how the recorder behaves; nothing is recorded until you press **Start recording**, and **Cancel** leaves nothing behind."),
        STEPS([
            "Press Smart Capture|the briefing opens over the page.",
            "Read it and press Start recording|a small bar appears in the corner with the step count, Finish and discard.",
            "Work through your flow|at a normal, unhurried pace. Every click on a real control becomes a numbered step.",
            "Press Finish|the guide is assembled and offered for saving into the active project.",
        ]),
        P("Four things decide whether a guide comes out right, and the briefing says all four:"),
        TABLE(["Rule", "Why"], [
            ["Leave about a second between clicks", "Chrome allows a tab to be photographed about twice a second. Click faster and the step is still recorded, it just has no picture."],
            ["Pause after typing before clicking on", "What you type becomes one step, written down about a second and a half after you stop \u2014 not one step per key."],
            ["Keep the recorded tab in front", "A tab that is not the visible one cannot be photographed. Following a link into a new tab is fine; the walkthrough goes with it."],
            ["Press and release in one place", "A drag, or a press held longer than about a second and a half, is read as a text selection and dropped."],
        ]),
        NOTE("Clicking into a text box, or opening a dropdown, is deliberately **not** a step. The step is what you typed, or the option you picked \u2014 not the click that got you there. Recording stops at 60 steps."),
        P("The corner bar never appears in the pictures. Turn the briefing off for good from the dialog itself, or from **Dashboard \u2192 Settings \u2192 Explain Smart Capture before it starts**."),

        H("Editing a guide"),
        P("**Dashboard \u2192 Guides \u2192 Open editor**. Each step has its wording, its screenshot and its own controls: reorder, duplicate, split a run of clicks, add a note below the picture, or delete it. The header block carries the title, author, status, date, step count, how long the guide takes and a comments field \u2014 all of it editable, and all of it carried into every export."),
        P("The time is worked out from the steps unless you type your own figure, and the note beside it is yours to write: say *including approvals* and that is what the exports say."),
        P("**Markdown** at the top of the ribbon swaps the formatted view for the guide's raw Markdown. Edits made there \u2014 including in the header table and the comments \u2014 come back with you."),

        H("Exporting"),
        P("**Dashboard \u2192 Guides \u2192 Export** offers four destinations:"),
        TABLE(["Export", "What it is for"], [
            ["**Share bundle (.zip)**", "One file to send to a colleague. Downloads."],
            ["**Self-contained HTML**", "One `guide.html` with every picture inside it. Written into the project folder."],
            ["**Markdown**", "`guide.md` beside its screenshots, for a repo or a docs site."],
            ["**Copy to clipboard**", "Rich text for Confluence, Notion or a doc."],
        ]),
        P("**Export all guides**, beside the Import button, writes every guide into one archive."),

        H("Sharing a guide with a colleague"),
        P("**Share bundle** is the one to send. It holds the guide itself \u2014 the steps and the control each one points at \u2014 its screenshots, and readable HTML and Markdown copies for anyone who only wants to read it. Your colleague imports it from **Dashboard \u2192 Guides \u2192 Import**, and it arrives as a guide with a **Play** button, not a document about one."),
        P("Import also takes a link, so a bundle put on an internal share can be pulled in by address rather than by file."),
        WARN("A shared guide plays with rings only against the same screens. Guide Mode finds each step's control by a selector recorded against the page you captured on, so a colleague on the same app and version gets the rings in the right places, and one on a different build may not. The pictures and the words are unaffected either way."),

        H("Printing a guide, or saving it as PDF"),
        P("From the editor, **Export \u2192 Print / Save as PDF**. The guide prints on its own \u2014 no toolbars, no side panels, no per-step buttons \u2014 as one continuous strip sized to the document rather than sliced into A4 pages, so no screenshot is ever cut in half. A guide long enough to exceed a single PDF page breaks between steps, never through a picture."),

        H("Guide Mode \u2014 playing a guide back"),
        P("**Play** on any guide card runs it against the live page. Each step is shown in turn with its control ringed on the real page, so the reader follows along in the software rather than reading about it."),
        NOTE("A walkthrough recorded with **Interactive walkthrough** turned off records the screenshots and the words only, with nothing about the page's own markup. It reads and exports perfectly, and it does not play."),

        H("Where guides live"),
        P("Each guide is a folder inside its project, holding `guide.json` and its screenshots. A guide is listed because `project_metadata.json` names it \u2014 copying a folder in by hand achieves nothing on its own, which is what Import is for."),
    ],
)

ORDER = [
    "getting-started",
    "capturing",
    "recording",
    "guides",
    "projects",
    "timeline",
    "settings",
    "shortcuts",
    "troubleshooting",
]
