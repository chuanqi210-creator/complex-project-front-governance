#!/usr/bin/env python3
"""Check the Complex behavior regression pack.

This is intentionally lightweight: it does not pretend to evaluate an LLM.
It validates that the project keeps a compact behavior-case bank and that
the expected trigger names still exist in the active docs/templates.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "docs" / "behavior_regression_cases_20260702.json"

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
    docs = load_docs()

    cases = pack.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("pack.cases must be a non-empty list")

    required_ids = set(pack.get("required_case_ids", []))
    if len(required_ids) < 8:
        fail("required_case_ids must cover at least 8 canonical cases")

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

    print(f"ok behavior_cases={len(cases)} required_cases={len(required_ids)}")


if __name__ == "__main__":
    main()
