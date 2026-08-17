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
        P("The pill above the selection shows the size in CSS pixels and the native pixel size you will actually get — on a Retina display a 600×400 selection is captured at 1200×800."),
        SHOT("lens-selection-handles.png", "A selection with its eight resize handles visible and the dimension pill reading both CSS and native pixel sizes"),

        H("Capture full tab"),
        P("**Full tab** skips the selection step and captures the whole visible area of the tab. It does not capture below the fold — only what is on screen."),

        H("The private-data check"),
        P("As the editor opens, Lens looks over the region it just captured for things that usually should not be shared, and shows a bar above the image listing what it found. Each one is outlined on the image so you can see exactly what would be covered."),
        P("It looks for password fields, fields named for a credential that have something in them, and text shaped like an API key, a JWT, a bearer token or a PEM private key. Unless you turn it off, it also flags email addresses and card numbers — card numbers are checksum-checked, so an order number is not mistaken for one."),
        UL([
            "Tick or untick anything in the list, then press **Blur all** to cover the ticked ones in a single step that a single **Undo** reverses.",
            "**Dismiss** hides the bar and changes nothing.",
            "High-confidence findings are ticked for you; the rest are listed but left unticked.",
        ]),
        NOTE("The check runs on the structure of the page in your own browser. It uses no AI and sends nothing anywhere, and it is on by default. If you have connected an AI provider you can additionally let a model sort real credentials from documentation examples — see [Settings](settings.html)."),
        WARN("Treat it as a safety net, not a guarantee. It recognises known shapes, so it will not catch a secret that does not look like one, or a name or figure that is sensitive only in context. Read the capture as well."),
        SHOT("lens-redaction-hints.png", "The annotation editor with an amber bar above the image listing two flagged regions, an API key and a password field, each outlined on the screenshot below"),

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
        P("If you have connected an AI provider, a **Suggest name & description** button appears above the name field. It reads the text inside the region you captured and fills in a file name and a one-line description of what the screenshot shows. The description is added to your note rather than replacing it, and everything it writes is yours to edit."),
        NOTE("This is the one feature that sends the captured region's text to your provider, because describing a screenshot is the task. It only ever runs when you press the button — never as part of saving. If your provider is the browser's built-in model or one on your own machine, that text does not leave the device either way."),
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

        H("Play shutter sound"),
        P("A short camera click when a capture completes. It is synthesised in the page, so nothing is downloaded and no audio file ships with the extension."),

        H("Flag private data in captures"),
        P("On by default. Checks each captured region for credentials before you save and offers to blur them — see [Capturing](capturing.html) for what the bar looks like and what it recognises. It reads the page structure in your browser: no AI, no network call, nothing sent anywhere."),

        H("Also flag emails and card numbers"),
        P("On by default, and only has an effect while the check above is on. Widens it past credentials to personal data. Card numbers are validated against their checksum, so order and reference numbers are not flagged."),

        H("AI provider"),
        P("**None** by default, which means every AI feature is off and Lens makes no network requests. Lens has no AI service of its own — you choose who does the work, and that choice decides whether anything leaves your machine."),
        TABLE(["Provider", "Runs", "Needs"], [
            ["None", "Nothing — AI features off", "—"],
            ["Your browser's built-in model", "On your device", "Edge or Chrome with the model available"],
            ["A local model", "On your device", "Ollama, LM Studio or similar, and the model name"],
            ["Claude", "Anthropic's servers", "An Anthropic API key"],
            ["OpenAI or compatible", "OpenAI's servers, or an endpoint you name", "An API key"],
        ]),
        P("Picking one that runs in the cloud asks you to confirm first, because it changes what the extension does with page text. **Test connection** tells you whether the provider is actually reachable before you rely on it."),
        NOTE("An API key is stored in this browser only, in its own storage area, and is read only by the extension's background worker — never by the code Lens injects into a page. The settings screen can tell you a key is saved but cannot show it back to you. Vectored never receives it; see the [privacy policy](../privacy.html#ai)."),

        P("Connecting a provider also puts two buttons on the save screens: **Suggest name & description** on a screenshot, and **Write steps from clicks** on a recording. Both are covered in [Capturing](capturing.html) and [Recording](recording.html). Neither runs on its own — you press them, per capture."),

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
ORDER = [
    "getting-started",
    "capturing",
    "recording",
    "projects",
    "timeline",
    "settings",
    "shortcuts",
    "troubleshooting",
]
