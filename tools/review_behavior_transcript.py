#!/usr/bin/env python3
"""Review a real agent transcript against Complex behavior-case rules.

This tool is intentionally modest. It checks required/forbidden marker groups
and emits human-review questions. It does not claim to be a full LLM judge.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "docs" / "behavior_regression_cases_20260702.json"
RULES = ROOT / "docs" / "behavior_transcript_review_rules_20260702.json"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")
    if not isinstance(data, dict):
        fail(f"expected JSON object: {path}")
    return data


def known_case_ids() -> set[str]:
    pack = load_json(PACK)
    cases = pack.get("cases")
    if not isinstance(cases, list):
        fail("behavior pack cases must be a list")
    return {str(case.get("case_id")) for case in cases if isinstance(case, dict)}


def extract_text_from_json(data: Any) -> str:
    if isinstance(data, str):
        return data
    if isinstance(data, list):
        return "\n".join(extract_text_from_json(item) for item in data)
    if not isinstance(data, dict):
        return ""

    if isinstance(data.get("assistant_response"), str):
        return data["assistant_response"]
    if isinstance(data.get("transcript"), str):
        return data["transcript"]
    if isinstance(data.get("text"), str):
        return data["text"]

    messages = data.get("messages")
    if isinstance(messages, list):
        parts = []
        for message in messages:
            if not isinstance(message, dict):
                continue
            role = str(message.get("role", ""))
            content = message.get("content", "")
            if isinstance(content, str):
                parts.append(f"{role}: {content}")
        return "\n".join(parts)

    return "\n".join(extract_text_from_json(value) for value in data.values())


def load_transcript(args: argparse.Namespace) -> str:
    if args.text_file:
        return Path(args.text_file).read_text(encoding="utf-8")
    if args.json_file:
        return extract_text_from_json(load_json(Path(args.json_file)))
    if args.stdin:
        return sys.stdin.read()
    fail("provide --text-file, --json-file, or --stdin")


def marker_group_hit(text: str, group: dict[str, Any]) -> tuple[bool, list[str]]:
    markers = group.get("any")
    if not isinstance(markers, list) or not markers:
        fail(f"marker group missing non-empty any list: {group}")
    hits = [str(marker) for marker in markers if str(marker).lower() in text.lower()]
    return bool(hits), hits


def review(case_id: str, transcript: str) -> dict[str, Any]:
    rules_doc = load_json(RULES)
    rules_by_case = rules_doc.get("case_rules")
    if not isinstance(rules_by_case, dict):
        fail("rules file must contain case_rules object")

    case_ids = known_case_ids()
    if case_id not in case_ids:
        fail(f"unknown case_id: {case_id}")
    if case_id not in rules_by_case:
        fail(f"missing transcript review rules for case_id: {case_id}")

    rules = rules_by_case[case_id]
    required_groups = rules.get("required_marker_groups", [])
    forbidden_groups = rules.get("forbidden_marker_groups", [])
    minimum_required = int(rules.get("minimum_required_groups", len(required_groups)))

    required_results = []
    for group in required_groups:
        hit, hits = marker_group_hit(transcript, group)
        required_results.append(
            {
                "label": group.get("label", ""),
                "passed": hit,
                "hits": hits,
            }
        )

    forbidden_results = []
    for group in forbidden_groups:
        hit, hits = marker_group_hit(transcript, group)
        forbidden_results.append(
            {
                "label": group.get("label", ""),
                "failed": hit,
                "hits": hits,
            }
        )

    required_passed = sum(1 for item in required_results if item["passed"])
    forbidden_failed = [item for item in forbidden_results if item["failed"]]
    passed = required_passed >= minimum_required and not forbidden_failed

    return {
        "case_id": case_id,
        "passed": passed,
        "required_passed": required_passed,
        "required_total": len(required_results),
        "minimum_required_groups": minimum_required,
        "required_results": required_results,
        "forbidden_results": forbidden_results,
        "human_review_questions": rules.get("human_review_questions", []),
    }


def validate_rules() -> dict[str, Any]:
    rules_doc = load_json(RULES)
    rules_by_case = rules_doc.get("case_rules")
    if not isinstance(rules_by_case, dict):
        fail("rules file must contain case_rules object")

    case_ids = known_case_ids()
    rule_ids = set(rules_by_case)
    missing_rules = sorted(case_ids - rule_ids)
    extra_rules = sorted(rule_ids - case_ids)
    if missing_rules or extra_rules:
        fail(f"case/rule mismatch: missing={missing_rules}, extra={extra_rules}")

    for case_id, rules in rules_by_case.items():
        for key in ["required_marker_groups", "forbidden_marker_groups", "human_review_questions"]:
            value = rules.get(key)
            if not isinstance(value, list) or not value:
                fail(f"{case_id}.{key} must be a non-empty list")
        minimum_required = rules.get("minimum_required_groups")
        if not isinstance(minimum_required, int) or minimum_required < 1:
            fail(f"{case_id}.minimum_required_groups must be a positive integer")
        if minimum_required > len(rules["required_marker_groups"]):
            fail(f"{case_id}.minimum_required_groups exceeds required_marker_groups length")

    return {
        "passed": True,
        "case_count": len(case_ids),
        "rule_count": len(rule_ids),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-id")
    parser.add_argument("--text-file")
    parser.add_argument("--json-file")
    parser.add_argument("--stdin", action="store_true")
    parser.add_argument("--validate-rules", action="store_true")
    args = parser.parse_args()

    if args.validate_rules:
        print(json.dumps(validate_rules(), ensure_ascii=False, indent=2))
        return

    if not args.case_id:
        fail("--case-id is required unless --validate-rules is used")
    transcript = load_transcript(args)
    if not transcript.strip():
        fail("transcript is empty")

    result = review(args.case_id, transcript)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
