#!/usr/bin/env python3
"""Write the Wiki docs index: the docs as data, for the product to embed.

    python3 wiki/_build/index.py --out <file>      write the index
    python3 wiki/_build/index.py --check <file>    exit 1 when <file> is stale

The Wiki answers "how do I..." questions from its own product docs. Each
build of the product embeds this index (pages, their sections as Markdown,
and the how-to `STEPS` blocks with the controls they point at), so the
answers match the running version and need no network.

The index is NOT part of the site: until the Wiki launches it is written
only into the product's source tree (the `--out` path), never under
`wiki/` here, the same way the Wiki stays out of the `llms` files.

The output is stable: the same content gives the same bytes, so the
product's check can compare files.
"""
import argparse
import hashlib
import html
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import engine
import guides
from content import PAGES

FORMAT = 1
SITE_URL = "https://docs.vectored.dev/wiki/"
# Pages that are lists of dated lines, not documentation to answer from.
SKIP = {"changelog"}


def page_url(slug, where, frag=""):
    return f"{SITE_URL}{where}/{slug}.html{frag}"


def md_inline(text, locations):
    """Content text is already Markdown-like (**bold**, `code`, [text](href));
    only links between pages need work: they become full addresses."""
    def link(m):
        label, href = m.group(1), m.group(2)
        pm = engine.PAGE_LINK.match(href)
        if pm and pm.group(1) in locations:
            href = page_url(pm.group(1), locations[pm.group(1)], pm.group(2) or "")
        return f"[{label}]({href})"
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)


def step_text(item):
    """A step as one sentence: "title|detail" reads "title: detail"."""
    if "|" not in item:
        return item
    title, detail = item.split("|", 1)
    return f"{title.rstrip('.:')}: {detail}"


def block_md(kind, val, locations):
    il = lambda t: md_inline(t, locations)
    if kind == "p":
        return il(val)
    if kind == "ul":
        return "\n".join(f"- {il(i)}" for i in val)
    if kind in ("ol", "steps"):
        return "\n".join(f"{n}. {il(step_text(i))}" for n, i in enumerate(val, 1))
    if kind == "table":
        headers, rows = val
        cell = lambda c: il(str(c)).replace("|", "\\|").replace("\n", " ")
        lines = ["| " + " | ".join(cell(h) for h in headers) + " |", "|" + "---|" * len(headers)]
        lines += ["| " + " | ".join(cell(c) for c in row) + " |" for row in rows]
        return "\n".join(lines)
    if kind == "note":
        return "> Note: " + il(val)
    if kind == "warn":
        return "> Warning: " + il(val)
    if kind == "code":
        return "```\n" + val.strip("\n") + "\n```"
    if kind == "shot":
        return ""           # a picture: nothing to read
    raise SystemExit(f"index: unknown block {kind}")


def sections(blocks, locations, seen_howtos, slug):
    out, seen = [], {}
    cur = {"id": "", "heading": "", "parts": [], "howtos": []}

    def close():
        text = "\n\n".join(p for p in cur["parts"] if p)
        if text or cur["howtos"]:
            s = {"id": cur["id"], "heading": cur["heading"], "text": text}
            if cur["howtos"]:
                s["howtos"] = cur["howtos"]
            out.append(s)

    for kind, val in blocks:
        if kind == "h":
            close()
            base = engine.slugify(val)
            seen[base] = seen.get(base, 0) + 1
            sid = base if seen[base] == 1 else f"{base}-{seen[base]}"
            cur = {"id": sid, "heading": html.unescape(re.sub(r"[*`]", "", val)), "parts": [], "howtos": []}
            continue
        cur["parts"].append(block_md(kind, val, locations))
        if kind == "steps" and isinstance(val, engine.HowTo):
            if val.howto in seen_howtos:
                raise SystemExit(f"index: how-to {val.howto!r} is on {seen_howtos[val.howto]} and {slug}")
            seen_howtos[val.howto] = slug
            steps = []
            for item, anchor in zip(val, val.anchors):
                st = {"text": md_inline(step_text(item), locations)}
                if anchor:
                    st["anchor"] = anchor
                steps.append(st)
            cur["howtos"].append({"id": val.howto, "task": val.task, "steps": steps})
    close()
    return out


def build_index():
    pages = guides.place(PAGES)
    locations = {slug: p.get("dir", "docs") for slug, p in pages}
    seen_howtos, out = {}, []
    for slug, p in pages:
        if slug in SKIP:
            continue
        where = p.get("dir", "docs")
        out.append({
            "slug": slug,
            "guide": p.get("guide", "user"),
            "title": html.unescape(p["title"]),
            "desc": html.unescape(p.get("desc", "")),
            "url": page_url(slug, where),
            "sections": sections(p["blocks"], locations, seen_howtos, slug),
        })
    return out


def render(pages):
    """One page per line, so a change to one page is a one-line diff."""
    lines = [json.dumps(p, ensure_ascii=False, separators=(",", ":")) for p in pages]
    revision = hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()[:12]
    head = json.dumps({"format": FORMAT, "product": "wiki", "site": SITE_URL, "revision": revision},
                      separators=(",", ":"))
    return head[:-1] + ',"pages":[\n' + ",\n".join(lines) + "\n]}\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--out", help="write the index to this file (in the product's source tree)")
    g.add_argument("--check", help="compare with this file; exit 1 when it is stale")
    args = ap.parse_args()
    text = render(build_index())
    if args.check:
        have = pathlib.Path(args.check)
        if not have.exists() or have.read_text(encoding="utf-8") != text:
            print(f"{args.check} is stale: run  python3 wiki/_build/index.py --out {args.check}", file=sys.stderr)
            sys.exit(1)
        print("docs index is current")
    else:
        target = pathlib.Path(args.out).resolve()
        site = engine.SITE.resolve()
        if site in target.parents:
            raise SystemExit("the index is not published: write it into the product's source tree, not into the docs site")
        target.write_text(text, encoding="utf-8")
        data = json.loads(text)
        n = sum(len(s.get("howtos", [])) for p in data["pages"] for s in p["sections"])
        print(f"docs index: {len(data['pages'])} pages, {sum(len(p['sections']) for p in data['pages'])} sections, "
              f"{n} how-tos, {len(text.encode('utf-8')) // 1024} KB, revision {data['revision']}")
