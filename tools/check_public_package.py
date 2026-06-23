#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "protocol/core_protocol.md",
    "protocol/gate_reference.md",
    "examples/startup_handoff_template.md",
    "docs/protocol_explainer_site/package.json",
    "docs/protocol_explainer_site/src/App.jsx",
]

FORBIDDEN_PATTERNS = [
    re.compile(r"/Users/"),
    re.compile(r"Documents/"),
    re.compile(r"Desktop/"),
    re.compile(r"ai 科研"),
    re.compile(r"chuchenqidawang/Documents"),
    re.compile(r"password\\s*[:=]", re.IGNORECASE),
    re.compile(r"api[_-]?key\\s*[:=]", re.IGNORECASE),
    re.compile(r"token\\s*[:=]", re.IGNORECASE),
    re.compile(r"secret\\s*[:=]", re.IGNORECASE),
]

SKIP_DIRS = {".git", "node_modules", "dist"}
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".js",
    ".jsx",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".html",
    ".css",
    ".mjs",
}


def iter_text_files() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path == pathlib.Path(__file__).resolve():
            continue
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            files.append(path)
    return files


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required file: {rel}")

    for path in iter_text_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                failures.append(f"forbidden pattern {pattern.pattern!r} in {rel}")

    if failures:
        print("public package check failed")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("public package check passed")
    print(f"checked files: {len(iter_text_files())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
