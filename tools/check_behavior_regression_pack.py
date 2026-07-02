#!/usr/bin/env python3
"""Check the Complex behavior regression pack.

This is intentionally lightweight: it does not pretend to evaluate an LLM.
It validates that the project keeps a compact behavior-case bank, transcript
review rules, and trigger names that still exist in active docs/templates.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "docs" / "behavior_regression_cases_20260702.json"
TRANSCRIPT_RULES = ROOT / "docs" / "behavior_transcript_review_rules_20260702.json"

DOC_PATHS = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "protocol" / "AGENTS.md",
    ROOT / "protocol" / "Complex项目持续治理协议_v3_核心版.md",
    ROOT / "protocol" / "持续治理协议发布包_20260622.md",
    ROOT / "docs" / "runtime-skill-management.md",
    ROOT / "docs" / "complex_runtime_cadence_simulation_20260701.md",
]
DOC_PATHS.extend(sorted((ROOT / "templates").glob("*.md")))

REQUIRED_CASE_FIELDS = {
    "case_id",
    "user_prompt",
    "project_nature",
    "expected_triggers",
    "expected_behavior",
    "forbidden_behavior",
    "expected_runtime_records",
}

ALLOWED_PROJECT_NATURES = {
    "unknown_at_entry",
    "evidence_fill",
    "model_discovery",
    "mixed",
    "execution_delivery",
}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_pack() -> dict:
    if not PACK.exists():
        fail(f"missing behavior pack: {PACK}")
    try:
        return json.loads(PACK.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {PACK}: {exc}")


def load_transcript_rules() -> dict:
    if not TRANSCRIPT_RULES.exists():
        fail(f"missing transcript review rules: {TRANSCRIPT_RULES}")
    try:
        return json.loads(TRANSCRIPT_RULES.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {TRANSCRIPT_RULES}: {exc}")


def load_docs() -> str:
    parts: list[str] = []
    missing = [path for path in DOC_PATHS if not path.exists()]
    if missing:
        fail("missing checked docs: " + ", ".join(str(path) for path in missing))
    for path in DOC_PATHS:
        parts.append(path.read_text(encoding="utf-8"))
    return "\n".join(parts)


def main() -> None:
    pack = load_pack()
    transcript_rules = load_transcript_rules()
    docs = load_docs()

    cases = pack.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("pack.cases must be a non-empty list")

    required_ids = set(pack.get("required_case_ids", []))
    if len(required_ids) < 8:
        fail("required_case_ids must cover at least 8 canonical cases")

    transcript_case_rules = transcript_rules.get("case_rules")
    if not isinstance(transcript_case_rules, dict):
        fail("transcript rules must contain case_rules object")

    seen_ids: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            fail("each case must be an object")
        missing_fields = REQUIRED_CASE_FIELDS - set(case)
        if missing_fields:
            fail(f"{case.get('case_id', '<unknown>')} missing fields: {sorted(missing_fields)}")

        case_id = case["case_id"]
        if case_id in seen_ids:
            fail(f"duplicate case_id: {case_id}")
        seen_ids.add(case_id)

        project_nature = case["project_nature"]
        if project_nature not in ALLOWED_PROJECT_NATURES:
            fail(f"{case_id}.project_nature is not routable: {project_nature}")

        for key in ["expected_triggers", "expected_behavior", "forbidden_behavior", "expected_runtime_records"]:
            value = case[key]
            if not isinstance(value, list) or not value:
                fail(f"{case_id}.{key} must be a non-empty list")

        for trigger in case["expected_triggers"]:
            trigger_key = str(trigger).split(":", 1)[0].strip()
            if trigger_key and trigger_key not in docs:
                fail(f"{case_id} trigger not found in active docs/templates: {trigger_key}")

        for record in case["expected_runtime_records"]:
            if record.endswith(".md") and not (ROOT / "templates" / record).exists():
                fail(f"{case_id} references missing template: templates/{record}")

    missing_required = required_ids - seen_ids
    if missing_required:
        fail("missing required behavior cases: " + ", ".join(sorted(missing_required)))

    rule_ids = set(transcript_case_rules)
    missing_rules = seen_ids - rule_ids
    extra_rules = rule_ids - seen_ids
    if missing_rules or extra_rules:
        fail(
            "transcript rule mismatch: "
            + f"missing={sorted(missing_rules)}, extra={sorted(extra_rules)}"
        )

    for case_id, rule in transcript_case_rules.items():
        for key in ["required_marker_groups", "forbidden_marker_groups", "human_review_questions"]:
            value = rule.get(key)
            if not isinstance(value, list) or not value:
                fail(f"{case_id}.{key} must be a non-empty list")
        minimum_required = rule.get("minimum_required_groups")
        if not isinstance(minimum_required, int) or minimum_required < 1:
            fail(f"{case_id}.minimum_required_groups must be a positive integer")
        if minimum_required > len(rule["required_marker_groups"]):
            fail(f"{case_id}.minimum_required_groups exceeds required_marker_groups length")

    print(
        "ok "
        + f"behavior_cases={len(cases)} "
        + f"required_cases={len(required_ids)} "
        + f"transcript_rules={len(rule_ids)}"
    )


if __name__ == "__main__":
    main()
