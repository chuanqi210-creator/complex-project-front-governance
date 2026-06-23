#!/usr/bin/env python3
"""Verify governance protocol recovery-chain consistency.

This helper turns the recurring post-change scan into a reusable check:
latest machine-board tail, fenced-code pseudo headings, current recovery
entry freshness, stale pending markers, and historically downgraded old
machine-board entries.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Iterable


DEFAULT_ROOT = Path("/Users/chuchenqidawang/Documents/ai 科研")
DEFAULT_PROTOCOL = Path("/Users/chuchenqidawang/Desktop/复杂项目启动前置治理协议_v3_核心版.md")
DEFAULT_LONG_LOG = DEFAULT_ROOT / "前置治理协议_二十个跨渠道项目逆向校验实验.md"
DEFAULT_RELEASE = DEFAULT_ROOT / "前置治理协议发布包_20260622.md"
DEFAULT_CHANGELOG = DEFAULT_ROOT / "持续优化变更清单_20260622.md"
DEFAULT_ROUTE = DEFAULT_ROOT / "真实项目压力测试_跨域收束与低摩擦路由表_20260622.md"
CONTINUOUS_SELF_OPTIMIZATION_FORBIDS = [
    "pending_post_change_scan",
    "pending_stateful_fenced_block_scan",
    "post_change_scan_pending",
    "post_change_scan_in_progress",
    "final_scan_to_run",
    "final_post_change_scan_needed",
    "final_tool_scan_to_run",
    "final_preset_scan_to_run",
    "final_meta_tooling_scan_to_run",
    "待最终扫描",
]
CONTINUOUS_SELF_OPTIMIZATION_SCOPES = (
    "protocol",
    "route",
    "release",
    "changelog",
    "long_log",
)
CONTINUOUS_SELF_OPTIMIZATION_SCOPE_EXTRA_ANCHOR = "source_role_map"
CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED = [
    "verify_governance_recovery_tool",
    "subagent_problem_decomposition_builder",
    "source_role_map",
    "skill_plugin_learning_loop",
    "skill_plugin_project_fit_trace",
    "best_practice_learning_contract",
    "capability_type_and_side_effect_gate",
    "external_state_write_guard",
    "skill_plugin_discovery_gate",
    "integration_lifecycle_gate",
    "transactional_integration_consistency_guard",
    "agentic_orchestration_capability_builder",
    "agent_topology_selection_trace",
    "subagent_orchestration_pattern_router",
    "desired_state_reconciliation_guard",
    "stateful_data_migration_guard",
    "security_incident_response_guard",
    "data_artifact_lineage_freshness_guard",
    "field_evidence_status",
    "source_authority_precedence_trace",
    "subagent_method_learning_trace",
    "subagent_result_coverage_gate",
    "main_agent_integration_review",
    "claim_readiness_ladder",
    "parallel_evidence_lane_trace",
    "claim_lane_binding",
    "deployment_readiness_gate",
    "software_delivery_state_boundary_guard",
]
CONTINUOUS_SELF_OPTIMIZATION_SCOPE_REQUIRED_EXTRAS = {
    "protocol": [
        "spawn_preflight",
        "agent_return_status",
        "subagent_lifecycle_ledger",
    ],
    "route": [],
    "release": [],
    "changelog": [
        "subagent_lifecycle_ledger",
    ],
    "long_log": [
        "subagent_lifecycle_ledger",
    ],
}


def build_continuous_self_optimization_required(
    core_required: Iterable[str],
    scope_required_extras: dict[str, Iterable[str]],
) -> dict[str, list[str]]:
    expected_scopes = set(CONTINUOUS_SELF_OPTIMIZATION_SCOPES)
    actual_scopes = set(scope_required_extras)
    missing = sorted(expected_scopes - actual_scopes)
    unexpected = sorted(actual_scopes - expected_scopes)
    if missing or unexpected:
        details = []
        if missing:
            details.append(f"missing scope extras: {missing}")
        if unexpected:
            details.append(f"unexpected scope extras: {unexpected}")
        raise ValueError("; ".join(details))

    core_fields = list(core_required)
    insert_at = core_fields.index(CONTINUOUS_SELF_OPTIMIZATION_SCOPE_EXTRA_ANCHOR) + 1
    required: dict[str, list[str]] = {}
    for scope in CONTINUOUS_SELF_OPTIMIZATION_SCOPES:
        fields = list(core_fields)
        fields[insert_at:insert_at] = list(scope_required_extras[scope])
        required[scope] = fields
    return required


CONTINUOUS_SELF_OPTIMIZATION_REQUIRED = build_continuous_self_optimization_required(
    CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED,
    CONTINUOUS_SELF_OPTIMIZATION_SCOPE_REQUIRED_EXTRAS,
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def headings_outside_fences(text: str) -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    inside = False
    headings: list[tuple[int, str]] = []
    pseudo: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            inside = not inside
            continue
        if line.startswith("## "):
            target = pseudo if inside else headings
            target.append((lineno, line))
    return headings, pseudo


def latest_section(text: str, headings: list[tuple[int, str]], latest_heading: str) -> str:
    for lineno, heading in reversed(headings):
        if heading == latest_heading:
            lines = text.splitlines()
            return "\n".join(lines[lineno - 1 :])
    return ""


def heading_count(headings: Iterable[tuple[int, str]], heading: str) -> int:
    return sum(1 for _, found in headings if found == heading)


def unique_append(values: list[str], additions: Iterable[str]) -> None:
    seen = set(values)
    for addition in additions:
        if addition not in seen:
            values.append(addition)
            seen.add(addition)


def check(result: list[dict[str, object]], name: str, ok: bool, detail: object = "") -> None:
    result.append({"name": name, "ok": bool(ok), "detail": detail})


def historical_marker_scan(texts: dict[str, str], markers: list[str]) -> list[dict[str, str]]:
    ambiguous: list[dict[str, str]] = []
    historical_terms = ("历史", "不再作为当前入口", "历史恢复点", "historical")
    for marker in markers:
        for file_key in ("release", "changelog"):
            text = texts[file_key]
            start = 0
            while True:
                idx = text.find(marker, start)
                if idx == -1:
                    break
                window = text[max(0, idx - 120) : idx + 240]
                if not any(term in window for term in historical_terms):
                    ambiguous.append(
                        {
                            "file": file_key,
                            "marker": marker,
                            "context": window.replace("\n", " ")[:260],
                        }
                    )
                start = idx + len(marker)
    return ambiguous


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--preset",
        choices=["continuous-self-optimization"],
        help="Apply the standard checks used by the continuous governance loop.",
    )
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    parser.add_argument("--protocol", default=str(DEFAULT_PROTOCOL))
    parser.add_argument("--long-log", default=str(DEFAULT_LONG_LOG))
    parser.add_argument("--release", default=str(DEFAULT_RELEASE))
    parser.add_argument("--changelog", default=str(DEFAULT_CHANGELOG))
    parser.add_argument("--route-table", default=str(DEFAULT_ROUTE))
    parser.add_argument("--latest-heading", required=True)
    parser.add_argument("--expected-route", required=True)
    parser.add_argument("--require-protocol", action="append", default=[])
    parser.add_argument("--require-route", action="append", default=[])
    parser.add_argument("--require-release", action="append", default=[])
    parser.add_argument("--require-changelog", action="append", default=[])
    parser.add_argument("--require-long-log", action="append", default=[])
    parser.add_argument("--forbid", action="append", default=[])
    parser.add_argument("--old-current-marker", action="append", default=[])
    parser.add_argument(
        "--auto-old-current-markers",
        action="store_true",
        help="Derive old machine-board headings from the long log, excluding --latest-heading.",
    )
    parser.add_argument(
        "--check-render-blocked",
        action="store_true",
        help=(
            "Check rendered artifact QA consistency. Kept for backwards "
            "compatibility: unresolved blockers must not claim visual pass; "
            "resolved states must include render evidence."
        ),
    )
    return parser.parse_args()


def apply_preset(args: argparse.Namespace) -> None:
    if args.preset != "continuous-self-optimization":
        return
    unique_append(args.require_protocol, CONTINUOUS_SELF_OPTIMIZATION_REQUIRED["protocol"])
    unique_append(args.require_route, CONTINUOUS_SELF_OPTIMIZATION_REQUIRED["route"])
    unique_append(args.require_release, CONTINUOUS_SELF_OPTIMIZATION_REQUIRED["release"])
    unique_append(args.require_changelog, CONTINUOUS_SELF_OPTIMIZATION_REQUIRED["changelog"])
    unique_append(args.require_long_log, CONTINUOUS_SELF_OPTIMIZATION_REQUIRED["long_log"])
    unique_append(args.forbid, CONTINUOUS_SELF_OPTIMIZATION_FORBIDS)
    args.auto_old_current_markers = True
    args.check_render_blocked = True


def main() -> None:
    args = parse_args()
    apply_preset(args)
    paths = {
        "root": Path(args.root),
        "protocol": Path(args.protocol),
        "long_log": Path(args.long_log),
        "release": Path(args.release),
        "changelog": Path(args.changelog),
        "route": Path(args.route_table),
    }

    checks: list[dict[str, object]] = []
    for key, path in paths.items():
        if key == "root":
            check(checks, "root_exists", path.exists() and path.is_dir(), str(path))
        else:
            check(checks, f"{key}_exists", path.exists(), str(path))

    if any(not item["ok"] for item in checks):
        print(json.dumps({"checks": checks, "failure_count": 1}, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    texts = {
        "protocol": read_text(paths["protocol"]),
        "long_log": read_text(paths["long_log"]),
        "release": read_text(paths["release"]),
        "changelog": read_text(paths["changelog"]),
        "route": read_text(paths["route"]),
    }

    headings, pseudo = headings_outside_fences(texts["long_log"])
    if args.auto_old_current_markers:
        old_markers = [
            heading
            for _, heading in headings
            if heading.endswith("当前机器看版") and heading != args.latest_heading
        ]
        unique_append(args.old_current_marker, old_markers)
    latest = latest_section(texts["long_log"], headings, args.latest_heading)
    last_heading = headings[-1] if headings else None

    check(checks, "long_log_tail_matches_latest_heading", bool(last_heading and last_heading[1] == args.latest_heading), last_heading)
    check(checks, "latest_heading_count_1", heading_count(headings, args.latest_heading) == 1, heading_count(headings, args.latest_heading))
    check(checks, "pseudo_heading_count_0", len(pseudo) == 0, pseudo[:10])
    check(checks, "latest_section_found", bool(latest))
    check(checks, "latest_pending_count_0", "pending" not in latest.lower(), re.findall(r"(?i)pending", latest)[:10])
    check(
        checks,
        "latest_no_recovery_verifier_to_run",
        "recovery_verifier_to_run" not in latest,
        re.findall(r"recovery_verifier_to_run", latest),
    )
    check(checks, "latest_has_expected_route", args.expected_route in latest)
    check(checks, "release_points_latest_heading", args.latest_heading in texts["release"])
    check(checks, "changelog_points_latest_heading", args.latest_heading in texts["changelog"])
    check(checks, "release_has_expected_route", args.expected_route in texts["release"])
    check(checks, "changelog_has_expected_route", args.expected_route in texts["changelog"])

    for file_key, needles in (
        ("protocol", args.require_protocol),
        ("route", args.require_route),
        ("release", args.require_release),
        ("changelog", args.require_changelog),
        ("long_log", args.require_long_log),
    ):
        for needle in needles:
            check(checks, f"{file_key}_contains:{needle}", needle in texts[file_key])

    for forbidden in args.forbid:
        found = {key: text.count(forbidden) for key, text in texts.items() if forbidden in text}
        check(checks, f"forbid:{forbidden}", not found, found)

    if args.old_current_marker:
        ambiguous = historical_marker_scan(texts, args.old_current_marker)
        check(checks, "old_current_markers_historical", not ambiguous, ambiguous)

    if args.check_render_blocked:
        release = texts["release"]
        has_blocked = "render_blocked" in release
        has_pass = any(
            marker in release
            for marker in (
                "rendered_pass",
                "visual_render_pass",
                "视觉渲染 QA 通过",
                "视觉渲染抽检通过",
            )
        )
        has_render_evidence = all(
            marker in release
            for marker in (
                "render_pingchang_check",
                "25 页",
                "四川省平昌县第二中学支教.pdf",
            )
        )
        if has_blocked:
            check(
                checks,
                "render_qa_state_consistent",
                not has_pass,
                "blocked_state_must_not_claim_visual_pass",
            )
        else:
            check(
                checks,
                "render_qa_state_consistent",
                has_pass and has_render_evidence,
                {
                    "has_pass": has_pass,
                    "has_render_evidence": has_render_evidence,
                },
            )

    failures = [item for item in checks if not item["ok"]]
    output = {
        "latest_heading": args.latest_heading,
        "expected_route": args.expected_route,
        "preset": args.preset,
        "auto_old_current_marker_count": len(args.old_current_marker),
        "heading_count": len(headings),
        "last_heading": last_heading,
        "failure_count": len(failures),
        "failures": failures,
        "checks": checks,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
