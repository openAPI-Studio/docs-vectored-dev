"""Lens doc content. Edit here, not the generated HTML under lens/docs/."""
from engine import P, H, UL, OL, STEPS, TABLE, NOTE, WARN, SHOT

# Each page: slug -> dict(title, lede, desc, icon, blocks)

PAGES = {}

PAGES["getting-started"] = dict(
    title="Getting Started",
    lede="Install Lens, link a project folder, and take your first capture.",
    desc="Install the Lens Chrome extension, link a local project folder and take your first screenshot or recording. Works completely offline, with no account and no subscription.",
    icon="rocket",
    blocks=[
        P("Lens is a Chrome extension that captures a region of any tab as a **PNG**, a **JPEG**, a high-quality animated **GIF** or an **MP4**, then files it into a folder on your own machine along with a metadata timeline. It also turns a flow you click through into a [step-by-step guide](guides.html). Nothing is uploaded — see [Privacy](../privacy.html)."),
        NOTE("**Lens works completely offline, and there is no subscription.** No account, no sign-in and no licence check: install it and every feature on these pages works with the network switched off. The only thing that ever touches the network is a cloud [AI provider](ai.html) you connect yourself, which is off on install and optional."),

        H("Install and pin"),
        STEPS([
            "Install Lens from the Chrome Web Store|or load the unpacked folder via chrome://extensions with Developer mode on.",
            "Pin it to the toolbar|click the puzzle-piece icon in Chrome's toolbar and press the pin next to Lens. The toolbar icon is where recording status and capture errors are reported.",
            "Open the popup|click the Lens icon. This is where you pick the active project and start a capture.",
        ]),
        SHOT("lens-popup-first-run.png", "The Lens popup on first run, showing the default project, no folder linked, and the three capture actions"),

        H("What is in the popup"),
        P("Top to bottom: the header, the project, the capture actions, and this project's recent captures."),
        TABLE(["Where", "What it is"], [
            ["Header, right", "The arrow opens the full dashboard in a tab. **?** holds Docs, Support and Security. The gear goes straight to the dashboard's Settings"],
            ["Project", "The dropdown switches project; the row under it names the linked folder, with **Link**, **Change** or **Reconnect** beside it"],
            ["Capture region", "The full-width button, because it is the one most people reach for"],
            ["Steps, GIF, Full tab", "The row of three under it. Each shows its own keyboard shortcut"],
            ["Interactive walkthrough", "A switch. On, a walkthrough also records which control each step points at, so it can be [played back](guides.html) against the live page. Off records the screenshots and the words only"],
            ["Timeline", "This project's captures, newest first. See [Timeline and dashboard](timeline.html)"],
            ["Footer", "**License** states the built-in free licence, which covers every feature and needs no key. **Privacy** opens the policy"],
        ]),

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

        H("Capturing a hover state or an open menu"),
        P("A hover, a dropdown and a pop-up menu all close the moment you click anywhere else \u2014 including on the **Capture Image** button \u2014 so on their own they can never be photographed. The delay beside that button solves it: choose **3s**, **5s**, **10s** or **30s** and Lens hands the page back to you for that long before the shutter fires."),
        STEPS([
            "Drag the region|over the area the menu or tooltip will appear in, not over the control that opens it.",
            "Pick a delay|from the clock menu on the left of the capture toolbar.",
            "Press **Capture Image**|the toolbar controls disappear, the region stays outlined, and the count starts.",
            "Set the page up|hover the control, open the menu, focus the field. Clicks, hovers and scrolling all reach the page normally.",
            "Wait|the capture is taken automatically when the count reaches zero.",
        ]),
        P("The count runs in the capture toolbar, in the place the delay was chosen, so nothing new appears on the page to get in the way. **Cancel** or **Escape** calls it off and gives the selection back, still adjustable. The choice is remembered for the rest of the session, so a run of captures that all need the same pause only needs setting once."),
        NOTE("Native dropdowns \u2014 a plain `<select>` \u2014 are drawn by the operating system rather than by the page, so Chrome cannot photograph them and they will not appear. Menus, tooltips, hover states and focus rings built in HTML and CSS, which is the great majority, all capture normally."),
        WARN("The region is fixed to the screen, not to the page. If you scroll during the delay, the capture takes whatever has moved under the box."),

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
    lede="Record a region of a tab as a high-quality animated GIF or an MP4 video.",
    desc="Record part of a tab as a high-quality animated GIF or MP4, with click-through interaction, navigation support and a converter that controls GIF framerate, speed and scale. Runs entirely offline.",
    icon="video",
    blocks=[
        P("Lens records the region you select, not the whole screen, and you keep using the page while it records — clicks and scrolling pass straight through. GIFs are captured at the region's own pixel size and encode at up to 30 frames a second, so the output is as sharp as what was on screen."),
        NOTE("Recording and encoding both happen inside your browser. Nothing is uploaded, no account or subscription is involved, and the whole flow works offline."),

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
            ["Quality controls", "Framerate, speed and scale, set after you stop", "None — recorded as captured"],
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
        P("Encoding runs in the page and locks the controls while it works. Progress is shown on the bar. It is done entirely on your machine — there is no upload step and no service to sign up for, so the converter works with the network off."),

        H("Getting the highest-quality GIF"),
        P("The defaults favour a file you can attach to a ticket. When the GIF is going into documentation and detail matters more than size, push all three controls up:"),
        UL([
            "**Scale 100%** — the single biggest factor. At 100% each captured pixel becomes a GIF pixel, so text in the recording stays readable.",
            "**30 frames per second** — for cursor movement, drag-and-drop and anything animated. 10 or 15 is enough for a slow click-through and encodes far faster.",
            "**Playback speed 1×** — anything faster drops frames from the output, not just the preview.",
            "Select a **tight region**. A small region at full scale is both sharper and smaller than a big region scaled down.",
        ]),
        NOTE("A high-quality GIF is a large GIF — a full-scale 30fps recording of a wide region runs to tens of megabytes and takes noticeably longer to encode. If the result is too big to share, halve the scale before you drop the framerate: it costs less of what makes a recording readable."),
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
        P("A **guide** is a walkthrough of a flow: a screenshot per step with the control you used ringed and numbered, and a sentence under each. You click through the task once and Lens assembles the document, rather than asking you to screenshot each step and paste them together afterwards. A finished guide can also be played back against the live page, with each step's control highlighted on it — see **Guide Mode** below."),
        NOTE("**No AI is involved in building a guide.** Step sentences come from the accessible name of each control — the name a screen reader would announce. A connected model can rewrite those sentences afterwards; it never writes them in the first place."),

        H("Two ways to capture one"),
        P("**Record steps** (⌘⇧E, Alt+Shift+E) is the light one: no region to drag, no video, and **no time limit** — nothing accumulates between clicks, so a walkthrough can take as long as the work does."),
        STEPS([
            "Press **Record steps** in the popup|or use the shortcut. A small widget appears in the corner of the page.",
            "Click through your flow as you normally would|every click on a real control becomes a step, and a page load becomes a step of its own so the guide does not read as though everything happened on one screen.",
            "Type into fields as you normally would|a field is captured once you stop typing, not when you click into it, so the picture shows a filled box rather than an empty one. The step quotes what you entered — *Type \"ACME-1024\" into \"Order number\"*.",
            "Choose from dropdowns as you normally would|the step is the option that came out, not the click that opened it — *Select \"Germany\" from \"Country\"*.",
            "Scroll as you normally would|scrolling far enough to reach something becomes a step, named for the heading you land on. A nudge to bring something into view does not.",
            "Press **Record clip** for anything a still cannot carry|a drag, a hover menu, an animation. Drag a region, do the thing, press **Stop clip**, and it is dropped in as one animated step in the place you recorded it.",
            "Press **Finish**|the review panel opens. There is no file to name, because the guide is the whole result.",
        ]),
        P("A flow that opens a **new tab** — a payment provider, a consent screen, a document — carries on being recorded. Any tab the flow itself opens joins the walkthrough; a tab you open for something else does not. Closing the tab you started in does not end the walkthrough if the flow has moved on, and **Finish** is available in whichever tab you are standing in."),
        P("**Record GIF** (⌘⇧R) produces a guide as well as the recording, as long as **Build a guide from each recording** is on — it is by default. The review panel appears under the file name on the save screen."),
        NOTE("Only **Record steps** follows the flow into a new tab. A GIF recording is a capture stream bound to one tab, so it stays on the tab it started in."),
        NOTE("The region you drag limits the *recording*, not the steps. Each step screenshot is a fresh capture of the **whole tab**, with the control you used ringed on it — so steps stay readable even when the recorded region was small."),
        P("A step is the whole screen on purpose. A picture cropped tight around one button leaves out the part of the page a reader needs in order to know where they are, and a crop cannot be undone once it is saved. Lens works out where a tighter crop would go and offers it instead: open a step's crop tool in the editor and that box is already drawn, ready to accept or drag."),
        SHOT("lens-steps-widget.png", "The walkthrough widget in the corner of a page, showing a step count, a clip count, and the Record clip, Finish and discard buttons"),

        H("What does not become a step"),
        UL([
            "Clicks on Lens's own controls. Pressing **Finish** does not appear in the guide it finishes.",
            "Clicks on nothing — empty space, a page background.",
            "A repeated click on the same control within a second, which is counted once.",
            "A drag or a text selection, which is not a click at all.",
            "Clicking into a field and leaving it empty — the step arrives when you type something, not before.",
            "Pausing while you fill a field in. The step is written once the typing settles, and typing on into the same field extends that step rather than adding another; the picture is of the field as you leave it.",
            "The page load a click causes — said as part of that click (*Follow \"Support\" — opens docs.vectored.dev/support.html*) rather than as a step of its own with no picture. A redirect chain names where you end up; a page you open yourself is still a step.",
            "Clicking a dropdown open. The step is the option you choose from it. On most platforms the open list is drawn by the operating system and would not appear in a screenshot of the page anyway.",
            "A short scroll, or the jump a page makes in response to a click that was already recorded.",
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
            ["Play", "Runs the guide against the live page. See **Guide Mode** below"],
            ["Open editor", "Opens the guide as a document in its own tab"],
            ["Export", "Self-contained HTML, Markdown, or the clipboard"],
            ["Delete", "Removes the guide's folder on disk and the entry pointing at it. Asks first"],
        ]),
        P("Above the cards sit three actions that apply to the whole set: **Find guides on disk**, **Import guide** and **Export all guides**. The first two are covered under **Importing a guide** below, the third under **Exporting**."),
        NOTE("Guides recorded while no folder was linked are held in the browser and listed below the others as **pending**. They are not lost — link a folder, make that project active, and write them from there."),
        SHOT("lens-guides-list.png", "The dashboard Guides tab with guide cards, each showing the site's logo, title, step count and the folder path it was written to"),

        H("Guide Mode: playing a guide back"),
        P("An exported guide is something you read next to the work. **Guide Mode** puts it *on* the work: a small panel floats over the real page with the current step and its screenshot, and a ring is drawn around the control that step is about, on the page itself."),
        P("Start it from **Dashboard > Guides > Play**, or from **Guide Mode** in the editor's toolbar."),
        TABLE(["Control", "What it does"], [
            ["Drag the header", "Moves the panel. It remembers where you left it"],
            ["Drag the bottom corner", "Resizes it, both directions. The step text scrolls inside"],
            ["Minimise", "Collapses to a pill **in the same place**, so the walkthrough does not jump to another corner"],
            ["The step number", "Opens the list of every step, to jump straight to one"],
            ["Auto-advance", "On by default. Moves to the next step when you actually use the ringed control"],
            ["Expand the picture", "Opens the step's screenshot full size"],
        ]),
        P("The walkthrough follows you across pages: navigating mid-guide takes the panel with it and carries on at the right step. When a click takes you to a new page, the page-load step you have just performed is skipped, so you land on the step that is actually about the page in front of you."),
        SHOT("lens-guide-mode.png", "Guide Mode running on a live page: the companion panel with a step and its screenshot, and a blue ring drawn around the button that step refers to"),

        P("Where the recording caught what was typed — an order number, a search term, an option chosen from a dropdown — the panel carries a **Copy** button beside the instruction, so the value goes into the field without being read off a screenshot and retyped. Anything that looked like a credential was never written down, so those steps have nothing to copy."),

        H("Dropdowns wait for the choice"),
        P("Opening a dropdown is not the same as choosing from it, so a step about one does not move on when you click it. What happens next depends on where the list is drawn."),
        UL([
            "**A list drawn in the page** — a listbox, a menu, or a dropdown built out of `div`s — has the option itself ringed as soon as it appears, with the tag reading **Pick \"Overnight courier\"**. Click that option and the step is done.",
            "**A list drawn by the operating system**, which is what a plain `<select>` gets on macOS, is not part of the page and has nothing in it to ring. The tag names the option to choose instead.",
        ]),
        P("Choose something other than what the guide recorded and the step stays where it is, saying **Choose \"Asia Pacific\"** — better than carrying you forward from a choice you did not make."),

        H("When the control cannot be found"),
        P("Beside the step number the panel says which it is — **Ringed on the page**, or **Not on this page**. A step with no control to point at, such as a page load or a scroll, says nothing there and shows no ring; press **Next** when you have done it."),
        P("Lens looks for the control by the selector recorded at the time, then its id, then a test id, label or field name, then its position in the page, and finally by the words on it. A guide recorded before Guide Mode existed, or one recorded in Plain mode, still names the control each step is about — and that name alone is often enough to find it."),
        P("It also keeps looking. A page that fetches its content draws its controls after the page has loaded, and a control behind a menu does not exist until you open that menu; the ring goes on the moment the control appears, however long that takes."),
        NOTE("Guide Mode needs an ordinary website tab. Started from the dashboard or the editor — both extension pages, which Chrome does not allow any script into — it opens the page the guide starts on in a new tab."),

        H("What a guide says about itself"),
        P("Above the first step sits a table: **written by**, **email**, **status** (Draft, In review, Published), **date**, **steps**, **time needed** and **comments**. Every field is editable in the editor, and all of it is printed into `guide.html` and `guide.md` above step 1 — they are the questions a reader asks before starting, not after finishing."),
        P("The time needed is worked out from the steps themselves: a click reads quicker than a field to fill in, a clip counts for as long as it runs, and the words in each step count towards the reading. Type over it and your figure stands; clear it and the calculation comes back."),
        NOTE("The name and address are filled in for you — from Settings, or from the address this Chrome profile is signed in with when Settings is blank. A guide someone else wrote keeps their name when you open it, and nothing is sent anywhere: it goes into that guide's own file in your folder. See [Privacy](../privacy.html)."),

        H("The guide editor"),
        P("The editor opens in its own tab and reads as a document: the sheet is the width of the exported page, and the steps run down it in order."),
        P("Step text is **Markdown**, and the toolbar offers exactly what Markdown can carry — bold, italic, strikethrough, code, highlight, links with an optional tooltip, pictures, bullet and numbered lists, task lists, nesting a list item deeper or bringing it back out, a line break inside a paragraph, tables, code blocks, rules, callouts and headings. Nothing else is offered on purpose: a font size or a colour would be something one of the two exports could not represent, and the same text is written to `guide.md` and rendered into `guide.html`."),
        P("Typed by hand, the whole of the [basic syntax](https://www.markdownguide.org/basic-syntax/) works: headings, bold, italic and both at once, blockquotes, ordered and unordered lists (`-`, `*` and `+`) nested by indentation, code spans — including the doubled-backtick form that holds a backtick — fenced code blocks, horizontal rules, links with titles, autolinked addresses such as `<https://example.com>` and bare email addresses, pictures, two-space hard line breaks, and backslash escapes. On top of that: strikethrough, `==highlight==`, tables, task lists, GitHub-style callouts and `:emoji:` shortcodes."),
        P("Printed as written rather than rendered: setext headings, four-space indented code blocks, nested blockquotes, reference-style links, and raw HTML — the last of those deliberately."),
        P("**Enter** carries on what you are in the middle of: another bullet, another numbered item, another task with its own box, and any inline formatting you had switched on. An empty list item leaves the list, and Enter after a heading drops back to ordinary text."),
        P("**Insert a picture** opens the file picker and copies the file into the guide's own folder when you save, writing it into the text as `![alt](name.png)`. **Insert a table** opens a grid — drag across it to choose the size — and while the caret is inside a table, a small bar above it adds or removes rows and columns."),
        TABLE(["Key", "What it does"], [
            ["⌘B / ⌘I", "Bold, italic"],
            ["⌘K", "Link"],
            ["⌘S", "Save"],
            ["⌘⇧M", "Switch between formatted editing and the raw Markdown"],
            ["⌘⇧O", "Show or hide the outline down the left"],
            ["⌘click", "Open a link — a plain click inside editable text places the caret instead, as it does everywhere"],
        ]),
        P("The **outline** down the left jumps between steps. The button in its header collapses it, and a tab at the screen edge — or ⌘⇧O — brings it back. On a window narrower than about 1000px there is no room for it and it is not shown."),
        P("**Markdown** in the ribbon, or ⌘⇧M, replaces the sheet with the whole guide as one Markdown document — the same text `guide.md` is exported as, title and numbered steps and picture links and all. Retitle it, rewrite a step, reorder or delete items, or type a new numbered step at the end; the document is read back into the guide as you type."),
        P("The outline still works here: clicking a step scrolls the document to that step's numbered line and puts the caret on it."),
        P("Lines are numbered down the left, and a wrapped line stays one line however many rows it takes — each number is as tall as the line beside it. The **?** next to the toggle, which only exists in this view, lists every mark the editor understands and what it produces; clicking a row drops it in at the caret."),
        P("What the text does not carry is kept from the steps that were there: which control each step points at, what kind of step it is, the file behind each picture. Items are matched to their steps by the picture they name, so a step that moves takes its screenshot and its recorded control with it, and an item you type in becomes a plain step with no picture. While the mode is on the formatting controls are blurred and made inert rather than hidden — they have nothing to act on — and the title in the header is read-only, because the document's first line is the title. The mode is remembered between sessions."),
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
        P("The page a step happened on sits under it as a small pill, showing the host and the end of the path — `docs.vectored.dev/lens`, or `docs/getting-started.html` for a local file. A search address with forty parameters shortens to `google.com/search?…`, and the whole address is the tooltip. Clicking the pill changes the address, which is what you want when a guide was recorded against localhost; the arrow beside it opens the page in a new tab."),
        P("On the screenshot itself you get the same image tools as a still capture — crop, annotate, blur, colour and rotation — plus **Replace image**, which swaps in a different file while keeping its name. The crop tool opens with the crop the recording suggested already drawn, to accept or drag."),
        NOTE("Nothing is written until you press **Save**. Closing with unsaved changes asks first, and undo covers everything, including a rewrite the assistant applied."),

        H("Exporting"),
        TABLE(["Format", "What you get"], [
            ["**Share bundle (.zip)**", "One guide as one file, for sending to somebody. It downloads rather than being written into the project folder, because it exists to be sent"],
            ["**Print / Save as PDF**", "The guide alone \u2014 no toolbars, no side panels, no per-step buttons \u2014 as one continuous strip sized to the document rather than sliced into A4 pages, so no screenshot is cut in half"],
            ["**Self-contained HTML**", "`guide.html` with every picture inlined and no scripts. One file you can email. A recorded value prints on its own line, selectable in one click"],
            ["**Markdown**", "`guide.md` beside its screenshots, relative paths, ready for a repo or a docs site"],
            ["**Copy to clipboard**", "Rich text for pasting into Confluence, Notion or a document"],
        ]),
        P("From the **editor**, Markdown downloads as a `.zip` holding `guide.md` and every screenshot it points at, in one folder. On its own the Markdown is a document whose picture links lead nowhere; the archive keeps the two together. A guide with no screenshots downloads as a plain `.md`."),
        P("**Export all guides**, above the cards on the Guides tab, writes `Lens_Guides_<date>.zip`: one folder per guide, each holding `guide.html`, `guide.md`, the screenshots, and the `guide.json` they were built from — so the archive can be read back in, not only read. A guide that cannot be read, usually a folder needing reconnecting, is left out and counted rather than failing the whole archive."),
        NOTE("A guide longer than a single PDF page allows breaks between steps, never through a picture. Animated steps print their poster frame. When pasting into a document, check the pictures survived — editors disagree about pasted images and some drop them."),

        H("Sending a guide to a colleague"),
        P("**Share bundle** is the one to send. It holds the guide itself \u2014 the steps and the control each one points at \u2014 its screenshots, and readable HTML and Markdown copies for anyone who only wants to read it. The other end imports it from the same tab and gets a guide with a **Play** button, not a document about one."),
        P("Before this, sharing one guide meant sending the whole archive of every guide you had: **Export all guides** was the only route that produced something importable."),
        WARN("A shared guide plays with rings only against the same screens. Guide Mode finds each step's control by a selector recorded against the page you captured on, so a colleague on the same app and version gets the rings in the right places, and one on a different build may not. The pictures and the words are unaffected either way. A walkthrough recorded with **Interactive walkthrough** off has no selectors at all: it imports and reads perfectly, and it does not play."),

        H("Importing a guide"),
        P("A guide appears in the list because `project_metadata.json` names it. Copying a guide folder into a project achieves nothing on its own, and a metadata file that is lost or overwritten takes every guide in that project out of the list with all the files still sitting on disk. These two actions cover both."),
        TABLE(["Action", "What it does"], [
            ["**Import guide > From a file**", "A `.zip` written by either export, or a bare `guide.json`. One archive may hold many guides; all of them come in"],
            ["**Import guide > From a link**", "The same, fetched from an address you paste"],
            ["**Find guides on disk**", "Lists guide folders that are in a linked project folder but missing from its timeline"],
        ]),
        P("An import is always a **copy**: it is given a new id and its own folder, so importing the same bundle twice leaves two guides rather than quietly overwriting the first. Nothing already on disk is replaced. A `guide.json` that arrives without its screenshots imports anyway and says so — those steps keep their words and have no picture."),
        P("Imports land in the **active project**, which must have a folder linked. What kind of file it is is read from its first bytes rather than its name, so a bundle fetched from a link works whatever the address ends in."),
        NOTE("Importing from a link is the only time Lens reaches the network on its own. It downloads the address you paste and nothing else: no service in between, nothing of yours sent with the request, `http` and `https` only, and 50 MB or 30 seconds at the outside. See [Privacy](../privacy.html)."),
        P("**Find guides on disk** walks every linked project, keeps each guide's existing id, and adds only what is missing. Run it after copying a folder in, or to repair a metadata file. Running it twice adds nothing the second time."),

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
            ["Thumbnail", "Opens a larger preview with the page URL and capture time. The preview shows the real file, so a GIF plays"],
            ["Copy", "Puts the image on the clipboard"],
            ["Rename", "Renames the file on disk and in the metadata"],
            ["Delete", "Removes the entry from the timeline"],
            ["Search", "Filters by file name, page title or URL"],
            ["JSON", "Exports `project_metadata.json` for the active project"],
        ]),
        SHOT("lens-popup-timeline.png", "The popup timeline with captures grouped under Today and Yesterday, each row showing thumbnail, file name, type badge and page title"),

        H("The dashboard"),
        P("Open the dashboard from the arrow icon at the top right of the popup, or the gear beside it to land straight on Settings. It has four sections."),
        UL([
            "**Projects** — every project as a card with its folder, capture count, last capture and access state.",
            "**Timeline** — every capture across all projects, grouped by project.",
            "**Guides** — every step-by-step guide, with import and export for the whole set. See [Guides](guides.html).",
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

        H("Thumbnails, and the file behind them"),
        P("What the timeline shows beside each entry is a small JPEG of the **first frame**, held in extension storage so the list loads instantly. That is why a GIF sits still in the popup timeline and in the dashboard grid, and why a screenshot there is thumbnail-sized rather than full resolution."),
        P("Open one and the preview reads the actual file out of the project folder instead: full size, and a recording that plays. Where no folder is linked, or its access has lapsed, the stored thumbnail stays up rather than the preview failing."),
        P("**Settings > Clear cached previews** empties that cache. Files already written to disk are untouched — only the thumbnails go, and the timeline then shows a placeholder icon in their place until you open one."),
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

        H("GIF quality, framerate and scale"),
        P("These are not on the Settings page — they live in the converter that opens when you stop a GIF recording, so you set them per recording against a preview of the actual frames. Scale 100% at 30 frames a second gives the highest-quality output — see **Getting the highest-quality GIF** on the [Recording](recording.html) page."),

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

        H("Open Lens after saving"),
        P("On by default. A capture that is written opens the Lens menu on its timeline with the new row picked out, so a save is seen rather than taken on trust from a message that disappears. A saved guide opens the dashboard's Guides tab instead. Turn it off for a long run of captures."),

        H("Explain Smart Capture before it starts"),
        P("On by default. Before a walkthrough records anything, a short briefing explains how the recorder behaves \u2014 when each screenshot is taken, how fast you can click, what does and does not become a step \u2014 with **Start recording** and **Cancel**. Nothing is recorded until you press Start, and Cancel leaves nothing behind. The dialog carries its own **Don't show this again**."),

        H("Watermark"),
        P("Lens draws a small mark in the corner of the images it saves \u2014 screenshots, recordings and the step images in a guide \u2014 picking black or white to suit what is behind it. It also tiles faintly through exported documents, PDF and self-contained HTML, and closes Markdown and clipboard copies with a line."),
        P("A licence puts it under your control: your own wording and logo, or off entirely. Without one the mark stays. Nothing else Lens does is affected either way \u2014 see [the licence](../index.html)."),
        NOTE("Where a guide came from is recorded separately and is never removed: the source page, the date and the author go into every export whatever the licence says. Only the visible mark is licensed."),

        H("Flag private data in captures"),
        P("On by default. Checks each captured region for credentials before you save and offers to blur them — see [Capturing](capturing.html) for what the bar looks like and what it recognises. It reads the page structure in your browser: no AI, no network call, nothing sent anywhere."),

        H("Also flag emails and card numbers"),
        P("On by default, and only has an effect while the check above is on. Widens it past credentials to personal data. Card numbers are validated against their checksum, so order and reference numbers are not flagged."),

        H("Build a guide from each recording"),
        P("On by default. Any recording with clicks in it also produces a step-by-step guide, offered for review on the save screen — see [Guides](guides.html). Turn it off and recordings are just recordings."),

        H("Walkthrough mode"),
        P("**Interactive** by default. As well as the screenshots and the words, Lens notes which control each step points at — enough to find it again later, which is what lets a guide be [played back against the live page](guides.html). **Plain** records the screenshots and the words only, and writes nothing about the page's own markup."),
        P("The same setting sits under the **Record steps** button in the popup, as a checkbox. Both write the one value."),

        H("Quote what you typed"),
        P("On by default. A step for a field you filled in reads *Type \"ACME-1024\" into \"Order number\"* rather than *Type into \"Order number\"* — the difference between an instruction a reader can follow and one they cannot."),
        P("It is fenced in. Nothing is quoted from a password or payment field, from a field whose name suggests a secret, or from a value shaped like a key, a token, a card number or an email address. Those steps name the field and stop there. The rules are the same ones the private-data check uses. Turn the setting off and nothing you enter is written down at all."),
        P("The option you pick from a dropdown is held to the same bar, and is recorded whatever this setting says — it is a label on the page rather than something you entered. An option carrying a mail address or an account number names the field and stops there."),
        NOTE("The screenshot for such a step is taken *after* you have typed, so what you entered is visible in the picture whether or not it is quoted in the text. That is the point of the step. Blur it in the editor, or delete the step, before the guide is saved."),

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
    desc="Diagnose blocked pages, blank recordings, low-quality GIFs, lost folder access and captures missing from the timeline.",
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

        H("My guides have disappeared from the dashboard"),
        P("The files are almost certainly still there. A guide is listed because `project_metadata.json` names it, so a metadata file that was lost, replaced or hand-edited takes every guide in that project out of the list while the folders sit untouched on disk."),
        P("**Dashboard > Guides > Find guides on disk** walks every linked project and lists whatever is missing, keeping each guide's own id. The same action picks up a guide folder you copied in by hand, which is otherwise invisible for the same reason."),

        H("A dropdown step will not move on"),
        P("That is deliberate. Opening a dropdown is not choosing from it, so the step waits for the option the guide recorded — the panel names which one. Pick something else and the step stays put and tells you what to look for. Where the list is drawn in the page, the option itself is ringed; where the operating system draws it, as with a plain `<select>` on macOS, there is nothing in the page to ring and the tag names it instead."),
        P("**Next** moves on regardless, if you want to skip it."),

        H("Guide Mode is not highlighting anything"),
        P("Look at the label beside the step number in the panel."),
        UL([
            "**Not on this page** — the control could not be found. Either you are not on the page that step is about, or the page has changed since the guide was recorded. Lens keeps looking, so if the control is behind a menu, opening that menu will ring it.",
            "**Nothing at all** — that step has no control to point at. A page load and a scroll are instructions to follow, not things to click; press **Next** when you have done it.",
            "**Plain walkthrough** — the guide was recorded with **Walkthrough mode** set to Plain, so nothing was written down about the page's controls. Guides recorded that way show their words and pictures only. Re-record with Interactive to get the highlighting.",
        ]),

        H("My GIF came out blurry or soft"),
        P("The converter's **Quality / scale** control was below 100%. At 75% or 50% every captured pixel is resampled, which softens text first. Re-encode from the converter at 100%, and raise the framerate to 30 if motion also looked choppy — see **Getting the highest-quality GIF** on the [Recording](recording.html) page."),
        P("If the recording itself looked soft on screen, the region was captured on a scaled display. Recording at 100% scale keeps whatever the tab actually rendered; it cannot add detail that was never drawn."),

        H("Do I need an account or a subscription?"),
        P("No. Lens has no account, no sign-in and no subscription, and it does not check a licence at any point. Everything on these pages works offline. The one optional exception is a cloud [AI provider](ai.html) you connect with your own key — that is your account with that provider, not one with Vectored."),

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
