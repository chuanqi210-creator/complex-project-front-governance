#!/usr/bin/env python3
"""Append long-log sections only at real EOF, then verify headings.

This helper exists to avoid repeated apply-patch anchor drift in long
append-only governance logs. It intentionally does one narrow thing:
append a provided Markdown block to the physical end of a file and rescan
headings outside fenced code blocks.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def headings_outside_fences(text: str) -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    inside = False
    headings: list[tuple[int, str]] = []
    pseudo: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            inside = not inside
        if line.startswith("## "):
            target = pseudo if inside else headings
            target.append((lineno, line))
    return headings, pseudo


def read_block(args: argparse.Namespace) -> str:
    if args.block_file:
        return Path(args.block_file).read_text(encoding="utf-8")
    if args.stdin:
        return sys.stdin.read()
    raise SystemExit("Either --block-file or --stdin is required for append.")


def scan(path: Path, latest_heading: str | None = None) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    headings, pseudo = headings_outside_fences(text)
    result: dict[str, object] = {
        "path": str(path),
        "heading_count": len(headings),
        "last_heading": headings[-1] if headings else None,
        "pseudo_heading_count": len(pseudo),
        "pseudo_headings": pseudo[:10],
    }
    if latest_heading:
        latest_start = text.rfind("\n" + latest_heading)
        latest = text[latest_start:] if latest_start != -1 else ""
        result["latest_heading_found"] = latest_start != -1
        result["latest_pending_count"] = latest.lower().count("pending")
    return result


def append(args: argparse.Namespace) -> dict[str, object]:
    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    headings, pseudo = headings_outside_fences(text)
    old_last = headings[-1][1] if headings else None

    if args.expect_old_tail and old_last != args.expect_old_tail:
        raise SystemExit(
            f"Old tail mismatch: expected {args.expect_old_tail!r}, got {old_last!r}"
        )
    if pseudo:
        raise SystemExit(f"Refusing to append while pseudo headings exist: {pseudo[:5]!r}")

    block = read_block(args).strip()
    if not block:
        raise SystemExit("Block is empty.")
    if not block.startswith("## "):
        raise SystemExit("Block must start with a level-2 Markdown heading.")

    for heading in args.expect_new_heading:
        if text.count(heading) != 0:
            raise SystemExit(f"New heading already exists before append: {heading!r}")

    new_text = text.rstrip() + "\n\n" + block + "\n"
    path.write_text(new_text, encoding="utf-8")

    new_headings, new_pseudo = headings_outside_fences(new_text)
    new_last = new_headings[-1][1] if new_headings else None
    if args.expect_new_tail and new_last != args.expect_new_tail:
        raise SystemExit(
            f"New tail mismatch: expected {args.expect_new_tail!r}, got {new_last!r}"
        )
    if new_pseudo:
        raise SystemExit(f"Pseudo headings after append: {new_pseudo[:5]!r}")

    counts = {
        heading: sum(1 for _, found in new_headings if found == heading)
        for heading in args.expect_new_heading
    }
    bad_counts = {heading: count for heading, count in counts.items() if count != 1}
    if bad_counts:
        raise SystemExit(f"Expected new headings exactly once: {bad_counts!r}")

    latest = ""
    if args.expect_new_tail:
        latest_start = new_text.rfind("\n" + args.expect_new_tail)
        latest = new_text[latest_start:] if latest_start != -1 else ""

    return {
        "path": str(path),
        "old_tail": old_last,
        "new_tail": new_last,
        "new_heading_counts": counts,
        "pseudo_heading_count": len(new_pseudo),
        "latest_pending_count": latest.lower().count("pending") if latest else None,
        "append_method": "append_eof_section_tool",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    scan_p = sub.add_parser("scan")
    scan_p.add_argument("path")
    scan_p.add_argument("--latest-heading")

    append_p = sub.add_parser("append")
    append_p.add_argument("path")
    append_p.add_argument("--block-file")
    append_p.add_argument("--stdin", action="store_true")
    append_p.add_argument("--expect-old-tail")
    append_p.add_argument("--expect-new-tail")
    append_p.add_argument("--expect-new-heading", action="append", default=[])

    args = parser.parse_args()
    if args.command == "scan":
        result = scan(Path(args.path), args.latest_heading)
    else:
        result = append(args)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
