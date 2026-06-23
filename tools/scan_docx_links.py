#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bounded DOCX text/link scanner.

This helper avoids dumping large OOXML files to the terminal. It scans the
relationship file and document body for literal patterns, then prints a compact
summary suitable for protocol post-change checks.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


PARTS = (
    "word/_rels/document.xml.rels",
    "word/document.xml",
)


def compact_xml_text(data: bytes) -> str:
    text = data.decode("utf-8", errors="replace")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def scan(docx: Path, patterns: list[str]) -> int:
    if not docx.exists():
        print(f"ERROR missing file: {docx}", file=sys.stderr)
        return 2

    total = 0
    with zipfile.ZipFile(docx) as zf:
        names = set(zf.namelist())
        for part in PARTS:
            if part not in names:
                continue
            raw = zf.read(part)
            body = raw.decode("utf-8", errors="replace")
            text = compact_xml_text(raw)
            for pattern in patterns:
                found = pattern in body or pattern in text
                if not found:
                    continue
                total += 1
                idx = text.find(pattern)
                if idx < 0:
                    idx = body.find(pattern)
                    snippet = body[max(0, idx - 80) : idx + len(pattern) + 80]
                else:
                    snippet = text[max(0, idx - 80) : idx + len(pattern) + 80]
                snippet = re.sub(r"\s+", " ", snippet).strip()
                print(f"MATCH\t{part}\t{pattern}\t{snippet}")

    if total == 0:
        print("NO_MATCH")
    else:
        print(f"TOTAL_MATCHES\t{total}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a DOCX for literal link/text patterns.")
    parser.add_argument("docx", type=Path)
    parser.add_argument("patterns", nargs="+")
    args = parser.parse_args()
    return scan(args.docx, args.patterns)


if __name__ == "__main__":
    raise SystemExit(main())
