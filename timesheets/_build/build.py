#!/usr/bin/env python3
"""Assemble the TimeSheets docs in reading order and build them."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import engine
from engine import H, P, UL, SHOT, NOTE
from content_core import CORE
from content_approvals import APPROVALS
from content_leave import LEAVE
from content_billing import BILLING
from content_admin import ADMIN
from content_settings import SETTINGS

BY_SLUG = {}
for group in (CORE, APPROVALS, LEAVE, BILLING, ADMIN, SETTINGS):
    for slug, page in group:
        if slug in BY_SLUG:
            raise SystemExit(f"duplicate page: {slug}")
        BY_SLUG[slug] = page

# Reading order: learn it, use it, run it, govern it.
ORDER = [
    "getting-started", "logging-time", "templates", "cost-centers",
    "approvals", "weekly-submission", "delegation", "approval-history",
    "leave", "leave-auto-decision", "holidays", "locking",
    "dashboard", "calendar", "summary",
    "reports", "scheduled-reports",
    "clients", "billing-rates", "invoices", "billing-health",
    "project-settings", "worklog-sync", "email", "scheduler",
    "personal-settings", "admin-settings",
    "data-requests", "permissions", "privacy-security",
]

# Hand-written; body preserved, nav refreshed.
HANDWRITTEN = {"privacy-security"}

# The hand-written page still needs an entry so it appears in nav and search.
BY_SLUG["privacy-security"] = dict(
    label="Privacy &amp; Data Handling", title="Privacy &amp; Data Handling", icon="lock",
    desc="What TimeSheets stores, what leaves Atlassian, and how erasure, export and retention work",
    keywords=["privacy", "gdpr", "security", "data", "residency", "ses", "article 9",
              "retention", "erasure", "export", "subprocessor", "forge"],
    blocks=[H(h) for h in [
        "Where your data lives", "What TimeSheets stores", "What leaves Atlassian",
        "Jira permissions the app asks for", "Special-category data", "Retention",
        "Erasing one person", "Why some data survives erasure",
        "Giving someone a copy of their data", "Who can see what",
        "What you still need to decide",
    ]],
)

missing = [s for s in ORDER if s not in BY_SLUG]
extra = [s for s in BY_SLUG if s not in ORDER]
if missing or extra:
    raise SystemExit(f"order mismatch — missing: {missing}, unplaced: {extra}")

PAGES = [(s, BY_SLUG[s]) for s in ORDER]

INTRO = [
    P("TimeSheets is time tracking, approvals, leave and billing for Jira Cloud. It runs entirely on Atlassian Forge — nothing to host, and no data leaves your Atlassian site except email."),
    H("What it does"),
    UL([
        "**Log time** against projects and cost centres, with or without a Jira issue.",
        "**Approve** it per entry or per week, with delegation for when an approver is away.",
        "**Book leave**, with balances, half-days and per-project approval.",
        "**Report** on teams and cost centres, and export to Excel or PDF.",
        "**Bill** approved work: clients, layered rates, and immutable numbered invoices.",
        "**Govern** it: retention windows, personal-data export, and erasure.",
    ]),
    NOTE("New here? Start with [Getting Started](docs/getting-started.html). Evaluating the app for a security or privacy review? Go straight to [Privacy & Data Handling](docs/privacy-security.html)."),
]

if __name__ == "__main__":
    pages, shots, tocs = engine.build(PAGES, INTRO, handwritten=HANDWRITTEN)
    print(f"pages: {pages}")
    print(f"screenshot slots: {shots}")
    print(f"pages with on-this-page nav: {tocs}")
    print(f"manifest: {engine.ROOT / 'SCREENSHOTS.md'}")
