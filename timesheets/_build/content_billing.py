"""Reporting and the billing chain."""
from engine import H, P, UL, OL, TABLE, NOTE, WARN, STEPS, SHOT

BILLING = [
    ("reports", dict(
        label="Reports & Exports", title="Reports & Exports", icon="table",
        desc="Team matrices, breakdowns and exports for projects you manage",
        keywords=["report", "matrix", "export", "excel", "pdf", "breakdown", "grouping"],
        blocks=[
            P("Reports answer *who logged what*, and *where did the time go*. They cover only projects you manage."),

            H("Who can see reports"),
            P("A person sees a project in reports if they are a **worklog approver** or a **project administrator** for it. Site administrators see everything they can browse."),
            P("Asking for a project outside that set does not silently return nothing — it is refused, so a report is never quietly narrower than you think."),

            H("The team matrix"),
            P("People down the side, days across the top, hours in the cells, with billable and non-billable split. It is the view for spotting a gap or an outlier in a week."),
            SHOT("timesheets-team-matrix.png", "The team matrix showing people down the side and days across, with hours in each cell"),

            H("Drilling into a cell"),
            P("Click a cell to see the entries behind it — project, cost centre, issue, description and status. This is where you check an unusual number before asking anybody about it."),
            SHOT("timesheets-matrix-cell-drilldown.png", "The drill-down panel for a matrix cell listing the individual entries behind the total"),

            H("Breakdown by cost centre, project or person"),
            P("The **Breakdown** view groups totals over one or two dimensions of your choosing — cost centre, project, person or client. Group by cost centre to see where effort actually went; add a second dimension to split it further."),
            SHOT("timesheets-breakdown-view.png", "The Breakdown view grouped by cost centre and person, showing hours, billable split and a proportion bar"),
            P("The largest hundred groups are shown; narrow the dates or projects to see the rest."),

            H("Unpriced billable time"),
            P("If billing is configured, the breakdown warns when billable work carries **no rate**. That figure is the difference between *we billed nothing* and *nobody set a price* — and the two look identical on a report that does not say."),
            P("Anyone who can see the report sees this warning, whether or not they can see money. Hours that are not being billed are an hours-level fact."),

            H("Amounts, and who can see them"),
            P("Amounts appear only for billing administrators. For everyone else the money columns are **absent**, not zeroed — an approver reading the report cannot tell what anybody bills at, because the figures were never sent to their browser."),
            P("Where several currencies are present, totals are shown per currency. There is deliberately no combined total: adding dollars to euros produces a perfectly ordinary-looking number that means nothing."),

            H("Excel export"),
            P("Exports the current report to a spreadsheet. The columns follow what the server sent you, so an export never contains a column you were not allowed to see on screen."),

            H("PDF export"),
            P("A printable version of the same data, for sending on or filing."),
            NOTE("Both files are generated **in your browser**. Nothing is uploaded anywhere to produce them."),
        ])),

    ("clients", dict(
        label="Clients", title="Clients", icon="briefcase",
        desc="The external party a project is billed to, and the currency it is billed in",
        keywords=["client", "customer", "billing", "currency", "invoice prefix", "payment terms"],
        blocks=[
            P("A client is who you send an invoice to. It is separate from a cost centre, which is how you classify work internally — a distinction worth keeping, because internal structure changes far more often than a customer relationship does."),
            NOTE("Clients are only needed if you intend to invoice. Time tracking, approvals and reporting all work without one."),

            H("What a client is"),
            P("A record of the party being billed: their name, address, tax identifier, billing email, payment terms and the currency you bill them in."),
            SHOT("timesheets-clients-list.png", "The Clients admin screen listing clients with their currency and payment terms"),

            H("Adding a client"),
            P("Under **Admin Settings → Clients**, add the client and fill in what you have. Name and currency are required; everything else can wait."),
            TABLE(["Field", "Notes"], [
                ["Name", "As it should appear on the invoice"],
                ["Code", "Optional short reference for your finance system"],
                ["Currency", "The currency this client is billed in. See the warning below"],
                ["Billing email", "Where invoices and billing correspondence go"],
                ["Address, Tax ID", "Printed on the invoice. TimeSheets does not calculate tax"],
                ["Payment terms", "Days added to the issue date to produce the due date"],
                ["Invoice prefix", "Starts this client's own numbering series, e.g. ACME-0001"],
            ]),

            H("Attaching a project to a client"),
            P("Set the client on a project under [Project Settings](project-settings.html). Work logged to that project is then attributable to that client for billing."),
            SHOT("timesheets-project-client-setting.png", "Project Settings showing the client selector with a client chosen"),
            P("A project with no client can still be tracked and reported on; it simply never reaches an invoice."),

            H("Currency, and why it cannot change later"),
            P("A client's currency pins everything downstream: which rates can apply, what an invoice is denominated in, and what a budget can be compared against."),
            WARN("Once a client has an invoice, treat the currency as fixed. Changing it would leave issued documents denominated in one currency and new work priced in another, with no exchange rate anywhere in the system to reconcile them. TimeSheets does not convert currencies and will not invent a rate."),
            P("Work priced in a currency other than the client's is reported as unbillable here rather than converted — see [Billing Health](billing-health.html)."),

            H("Payment terms and invoice prefix"),
            P("**Payment terms** are a number of days; the due date on an issued invoice is the issue date plus that number."),
            P("**Invoice prefix** gives a client their own numbering sequence. Leave it empty and they share the default `INV` series. Numbering is explained in [Invoices](invoices.html)."),
        ])),

    ("billing-rates", dict(
        label="Billing Rates", title="Billing Rates", icon="tag",
        desc="Hourly rates by person, project, cost centre or site default",
        keywords=["rate", "hourly", "price", "billing", "precedence", "effective date"],
        blocks=[
            P("A rate is what an hour of work is billed at. Rates are layered, so you can set a sensible default once and override it only where reality differs."),
            WARN("Everything on this screen is **billing-administrator only, including reading it**. A bill rate is salary-adjacent, and for a contractor it is very close to their pay rate."),

            H("How a rate is chosen"),
            P("For each entry, TimeSheets looks for the most specific rate that was in effect **on the date the work was done** — not the date it was approved or invoiced. That is what makes a re-run a year later produce the same numbers."),

            H("The precedence order"),
            TABLE(["Layer", "Use it for"], [
                ["Person on a project", "A named individual's rate on one engagement — the most specific, always wins"],
                ["Project", "Everything billed on one project at the same rate"],
                ["Cost centre", "A class of work. Walks up the cost centre's parents if no rate is set on it directly"],
                ["Site default", "The fallback for everything else"],
            ]),
            P("If no layer matches, the entry is captured **unpriced** rather than refused. Billing is not allowed to become a blocker on timekeeping."),
            SHOT("timesheets-rates-list.png", "The Billing Rates screen with rates grouped by scope, showing person, project, cost centre and site rates"),

            H("Effective dates"),
            P("Every rate has a start date and an optional end date. Leave the end empty for an open-ended rate."),
            P("A rate rise mid-period does not rewrite what came before: work before the change keeps the old rate, work after gets the new one, and an invoice shows them as two lines because a line may never mix two rates."),

            H("Adding a rate"),
            STEPS([
                "Choose what it applies to|person on a project, project, cost centre, or everything.",
                "Pick the target|as required by the scope you chose.",
                "Set the currency and amount|per hour.",
                "Set the effective dates|start is required, end is optional.",
                "Save|it applies to work dated inside its window from then on.",
            ]),
            SHOT("timesheets-add-rate-modal.png", "The Add billing rate dialog showing the scope selector, amount, currency and effective dates"),

            H("Ending a rate without replacing it"),
            P("**End** closes an open-ended rate at a date without creating a successor. Work after that date falls through to the next layer down — or becomes unpriced if there is none."),

            H("Previewing which rate would apply"),
            P("The **preview** tells you which rate would win for a given person, project, cost centre and date, and why. Use it before a change rather than discovering the answer on an invoice."),
            SHOT("timesheets-rate-preview.png", "The rate preview showing the winning rate for a person and date, with the layer that produced it"),

            H("Who can see rates"),
            P("Billing administrators, and nobody else. In particular, a person cannot see their own rate in their own timesheet — the timesheet screens never read the billing tables at all."),
        ])),

    ("invoices", dict(
        label="Invoices", title="Invoices", icon="file",
        desc="Turn approved, priced work into a numbered invoice",
        keywords=["invoice", "draft", "issue", "void", "numbering", "billing", "lines"],
        blocks=[
            P("An invoice turns a period of approved, priced work for one client into a numbered document. The lifecycle is deliberately narrow: **preview → draft → issued → void**, in one direction."),

            H("Preview before you commit"),
            P("A preview shows exactly what an invoice would contain and writes nothing. It uses the same code that produces the real document, so what you see is what gets billed."),
            SHOT("timesheets-invoice-preview.png", "The invoice preview showing lines, totals and a warning about unpriced work"),
            P("The preview also warns about two things worth catching early: **unpriced billable work**, which would otherwise be left off silently, and work priced in a **different currency** from the client, which cannot be billed here at all."),

            H("Creating a draft"),
            P("A draft claims the entries it covers, so a second draft for the same period will not bill them again. Drafts carry **no number** — abandoning one costs nothing, which is exactly why numbering waits."),
            P("Delete a draft and its entries return to the billable pool."),

            H("How work is grouped into lines"),
            P("Choose the grouping when you create the draft:"),
            TABLE(["Grouping", "Result"], [
                ["One line per person per project", "The default — most people's idea of a billing line"],
                ["One line per project", "Simpler documents for a client who does not need names"],
                ["One line per cost centre", "Where the classification is what the client cares about"],
                ["A single line", "One total for the engagement"],
            ]),
            P("Whatever you choose, **rate and currency are always part of the grouping**. Two different rates never share a line, because a line showing one rate and an amount derived from two would be quietly wrong."),
            NOTE("Rounding happens once per line. That way each line's amount follows exactly from its own hours and rate, and the invoice total is exactly the sum of its lines. Rounding per entry or only at the total breaks one of those two."),

            H("Issuing an invoice"),
            P("Issuing is the one-way door. In order, TimeSheets:"),
            OL([
                "checks the arithmetic, and refuses to issue anything whose lines do not add up;",
                "claims the next number in the client's series;",
                "marks the invoice issued and sets the issue and due dates;",
                "freezes the priced snapshot of every entry on it.",
            ]),
            SHOT("timesheets-invoice-issued.png", "An issued invoice showing its number, client details, lines and total"),

            H("Invoice numbering"),
            P("Numbers are assigned **at issue**, never at draft creation, so abandoned drafts do not leave holes. Each client with a prefix gets its own sequence."),
            P("Two people issuing at the same moment can never receive the same number. Gaps are a different matter: if an invocation fails between claiming a number and writing it, that number is spent. **Check for gaps** on the Invoices screen lists any such number, and reports voided invoices separately because a void keeps its number and is not a gap."),
            SHOT("timesheets-invoice-numbering-audit.png", "The numbering check showing the next number, issued and voided counts, and any gaps"),

            H("Voiding and re-issuing"),
            P("There is no *edit issued invoice*, on purpose: a document that changed after it was sent is not evidence of anything. The only correction path is **void → fix → raise a new one**."),
            P("Voiding requires a reason, keeps the number — numbers are never reused — and releases the work so it can be billed correctly on a new invoice."),
            SHOT("timesheets-invoice-void-dialog.png", "The void invoice dialog with the required reason field"),

            H("What happens to the time entries"),
            P("Once an invoice is issued, the entries behind it are frozen. Editing or deleting one is refused with a message saying it is on an issued invoice — and an unlock request will not help, because the constraint is the invoice, not the calendar."),
            P("Voiding the invoice releases them again."),
        ])),

    ("billing-health", dict(
        label="Billing Health", title="Billing Health", icon="activity",
        desc="Find approved work that carries no price, and re-price after a rate change",
        keywords=["billing health", "unpriced", "backfill", "recapture", "reprice", "capture"],
        blocks=[
            P("Prices are captured when work is approved. That timing is what makes an invoice stable — but it also means work approved before a rate existed carries no price, and nothing about that is obvious from a report showing zero revenue."),
            P("This screen exists to make it obvious."),

            H("Why work can end up unpriced"),
            UL([
                "It was approved **before** billing was set up, or before a rate covered it.",
                "No rate layer matched its date, person, project or cost centre.",
                "Its rate is in a **different currency** from the client, so it cannot be billed to them.",
                "It was edited after approval, so the recorded hours no longer match the entry.",
            ]),

            H("The four figures"),
            TABLE(["Figure", "What it means", "What to do"], [
                ["Approved entries", "Everything that could carry a price", "Nothing — this is the denominator"],
                ["Never captured", "Approved, but no price was ever recorded", "Run Price what is missing"],
                ["Billable, no rate", "Captured, but no rate applied on that date", "Add a rate, then re-price"],
                ["Hours changed since capture", "Edited after pricing, so the amount is stale", "Re-price the period"],
            ]),
            SHOT("timesheets-billing-health-card.png", "The Billing health card showing the four figures with two of them highlighted as needing attention"),

            H("Pricing what is missing"),
            P("**Price what is missing** fills gaps only. It never changes an amount that already exists, so it is always safe to run and safe to repeat."),

            H("Re-pricing a period"),
            P("**Re-price this range** recalculates from today's rates. Use it after correcting a rate that was wrong."),
            P("Both actions are deliberately manual. A job that silently rewrote money on a schedule would be worse than one somebody chose to run."),

            H("What re-pricing will not touch"),
            P("Work on an **issued invoice** keeps its original price, whatever the rates say now. The re-price reports how many entries it left alone for that reason — a silent skip would look identical to having nothing to do."),
            P("To correct an amount that has already been invoiced, void the invoice, fix the rate, re-price and raise a new one. See [Invoices](invoices.html)."),
        ])),
]
