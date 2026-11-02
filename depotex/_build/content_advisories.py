"""Security advisories page (docs/security-advisories.html) and its RSS feed
(depotex/advisories.xml, written by build.py from ADVISORIES).

Add an advisory at the top of ADVISORIES when a fix ships. Never list one
before the fixed release is available. Each entry:

    dict(id="DPX-SA-2026-001", date="YYYY-MM-DD", severity="High",
         title="Short title", affected="< 1.4.2", fixed="1.4.2",
         cve="CVE-2026-12345" or "", summary="What an attacker could do and who is exposed.",
         action="Upgrade to 1.4.2. Workaround until then: …")

Notices (kind="Notice") announce things about the feed or the process itself.
"""

import datetime
import html

from engine import H, P, UL, TABLE, NOTE, STEPS, CODE

SITE = "https://docs.vectored.dev/depotex"
FEED = "advisories.xml"

ADVISORIES = [
    dict(kind="Notice", id="DPX-NOTICE-2026-001", date="2026-11-02", severity="",
         title="Security advisory feed opened",
         summary="Depotex security advisories are now published on this page and in an RSS feed. No advisories have been issued so far.",
         action="Subscribe to the feed to hear about future advisories."),
]


def _rows():
    rows = []
    for a in ADVISORIES:
        if a.get("kind") == "Notice":
            continue
        rows.append([f"[{a['id']}](#{a['id'].lower()})", a["date"], a["severity"], a["title"],
                     f"`{a['affected']}`", f"`{a['fixed']}`", a.get("cve") or "—"])
    return rows


def _details():
    out = []
    for a in ADVISORIES:
        out.append(H(a["id"]))
        facts = [f"**Published:** {a['date']}"]
        if a.get("kind") != "Notice":
            facts += [f"**Severity:** {a['severity']}", f"**Affected versions:** `{a['affected']}`",
                      f"**Fixed in:** `{a['fixed']}`"]
            if a.get("cve"):
                facts.append(f"**CVE:** {a['cve']}")
        out.append(P(f"**{a['title']}**"))
        out.append(UL(facts))
        out.append(P(a["summary"]))
        out.append(P(f"**What to do:** {a['action']}"))
    return out


_table = _rows()

ADVISORIES_PAGE = [
    ("security-advisories", dict(
        label="Security advisories", title="Security advisories", icon="alert",
        desc="Security fixes in Depotex, what they affect and what to do, with an RSS feed to subscribe to",
        keywords=["security", "advisory", "advisories", "cve", "vulnerability", "rss", "feed", "subscribe", "disclosure", "report", "patch"],
        feed=("../" + FEED, "Depotex security advisories"),
        blocks=[
            P("When a release of Depotex fixes a security problem, it is announced here, with the versions affected, the version that fixes it and what to do until you can upgrade. Administrators should subscribe to the feed; everyone else can check here when asked to upgrade."),

            H("Subscribe"),
            P("Add this address to your feed reader, Slack or Microsoft Teams RSS app, or monitoring tool:"),
            CODE(f"{SITE}/{FEED}"),
            P("[Open the RSS feed](../advisories.xml). Each item links to its advisory below. Most browsers and feed readers also find the feed on their own from this page."),
            P("To get advisories by email as well, write to [support@vectored.dev](mailto:support@vectored.dev) with the address to send them to and your licensee name."),

            H("Advisories"),
            *([TABLE(["Advisory", "Published", "Severity", "Title", "Affected", "Fixed in", "CVE"], _table)] if _table else
              [NOTE("No security advisories have been issued for Depotex.")]),
            *_details(),

            H("Severity"),
            P("Each advisory has a CVSS score and one of these ratings, which say how soon to act:"),
            TABLE(["Rating", "CVSS", "Means", "Act"], [
                ["**Critical**", "9.0–10.0", "Exploitable from the network without an account, or leads to a full takeover", "Upgrade at once, or apply the workaround now"],
                ["**High**", "7.0–8.9", "Serious, but needs an account, a particular setting or a step from someone", "Upgrade in your next maintenance window, within days"],
                ["**Medium**", "4.0–6.9", "Limited impact or hard to exploit", "Upgrade with your regular updates"],
                ["**Low**", "0.1–3.9", "Minor, defense in depth", "Upgrade with your regular updates"],
            ]),

            H("What an advisory contains"),
            UL([
                "An ID (`DPX-SA-<year>-<number>`) and, where one is assigned, the CVE.",
                "What could happen and who is exposed: which features, settings, license tiers or deployment modes are affected.",
                "Affected versions and the version that fixes it. Fixes ship in a new release of the server image and the web app image together.",
                "A workaround or mitigation when there is one, and how to tell whether you were affected (audit log entries, log lines).",
                "Credit to the person who reported it, if they want it.",
            ]),
            P("Problems in components Depotex is built with (Go, Next.js, PostgreSQL client libraries and others) get an advisory when they affect Depotex as shipped. Upgrading to the latest release always brings their fixes; see [Upgrades](upgrades.html)."),

            H("Check your version"),
            P("The footer of every page, and **? → About**, show the version and build of the server that answered. In a cluster check each server: **Settings → Clustering** lists every server's version. From a script, `GET /api/health` answers with the version without signing in."),

            H("Report a vulnerability"),
            P("Found a security problem in Depotex? Please tell us privately, not in a public issue or forum, so we can fix it before it's widely known."),
            STEPS([
                "Write to us|Email [security@vectored.dev](mailto:security@vectored.dev) with the version, how to reproduce it, and what an attacker could do. Don't include real customer data, credentials or keys.",
                "We confirm|We acknowledge your report, confirm whether it's a vulnerability, and keep you informed while we fix it.",
                "We fix and publish|The fix ships in a release, then the advisory is published here and in the feed, crediting you if you wish.",
            ]),
            P("Please give us reasonable time to release a fix before you disclose it, test only against installations you own, and don't access or change other people's data. We won't take action against research done in good faith under these terms."),
            NOTE("For help with your own installation (configuration, an error you see) use [Support](support.html) instead."),
        ])),
]


def _rfc822(day):
    d = datetime.datetime.strptime(day, "%Y-%m-%d").replace(hour=9, tzinfo=datetime.timezone.utc)
    return d.strftime("%a, %d %b %Y %H:%M:%S +0000")


def rss():
    """The RSS 2.0 feed, newest first."""
    esc = html.escape
    page = f"{SITE}/docs/security-advisories.html"
    items = []
    for a in ADVISORIES:
        title = a["title"] if a.get("kind") == "Notice" else f"[{a['severity']}] {a['id']}: {a['title']}"
        desc = a["summary"] + " " + a["action"]
        if a.get("kind") != "Notice":
            desc = f"Affected: {a['affected']}. Fixed in: {a['fixed']}. " + desc
        items.append(f"""    <item>
      <title>{esc(title)}</title>
      <link>{page}#{a['id'].lower()}</link>
      <guid isPermaLink="false">{esc(a['id'])}</guid>
      <pubDate>{_rfc822(a['date'])}</pubDate>
      <category>{esc(a.get('kind') or 'Advisory')}</category>
      <description>{esc(desc)}</description>
    </item>""")
    newest = _rfc822(ADVISORIES[0]["date"]) if ADVISORIES else _rfc822("2026-11-02")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Depotex security advisories</title>
    <link>{page}</link>
    <atom:link href="{SITE}/{FEED}" rel="self" type="application/rss+xml"/>
    <description>Security fixes in Depotex: what they affect and what to do.</description>
    <language>en</language>
    <lastBuildDate>{newest}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""
