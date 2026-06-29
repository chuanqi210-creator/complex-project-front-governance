#!/usr/bin/env python3
"""Regression tests for verify_governance_recovery.py."""

from __future__ import annotations

import ast
import json
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "verify_governance_recovery.py"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def remove_required_field_from_fixture(tmp: Path, field: str) -> None:
    for name in ("protocol.md", "route.md", "release.md", "changelog.md", "long_log.md"):
        path = tmp / name
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace(f"{field}\n", ""), encoding="utf-8")


def run_verifier(tmp: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--preset",
            "continuous-self-optimization",
            "--root",
            str(tmp),
            "--protocol",
            str(tmp / "protocol.md"),
            "--long-log",
            str(tmp / "long_log.md"),
            "--release",
            str(tmp / "release.md"),
            "--changelog",
            str(tmp / "changelog.md"),
            "--route-table",
            str(tmp / "route.md"),
            "--latest-heading",
            "## 2. 当前机器看版",
            "--expected-route",
            "next_route_value",
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def load_verifier_module():
    spec = importlib.util.spec_from_file_location("verify_governance_recovery", TOOL)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def continuous_required_assignment_value() -> ast.AST:
    tree = ast.parse(TOOL.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "CONTINUOUS_SELF_OPTIMIZATION_REQUIRED":
                return node.value
    raise AssertionError("CONTINUOUS_SELF_OPTIMIZATION_REQUIRED assignment not found")


def test_default_paths_resolve_inside_this_repository() -> None:
    verifier = load_verifier_module()
    defaults = [
        verifier.DEFAULT_ROOT,
        verifier.DEFAULT_PROTOCOL,
        verifier.DEFAULT_LONG_LOG,
        verifier.DEFAULT_RELEASE,
        verifier.DEFAULT_CHANGELOG,
        verifier.DEFAULT_ROUTE,
    ]

    for path in defaults:
        assert path.resolve().is_relative_to(ROOT), path


def test_continuous_required_core_fields_are_shared_across_scopes() -> None:
    verifier = load_verifier_module()
    core_required = verifier.CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED
    scope_extras = verifier.CONTINUOUS_SELF_OPTIMIZATION_SCOPE_REQUIRED_EXTRAS
    required = verifier.CONTINUOUS_SELF_OPTIMIZATION_REQUIRED

    expected_required = verifier.build_continuous_self_optimization_required(
        core_required,
        scope_extras,
    )
    assert required == expected_required

    assert "agent_topology_selection_trace" in core_required
    assert "capability_discovery_cadence_gate" in core_required
    for scope in ("protocol", "route", "release", "changelog", "long_log"):
        assert "agent_topology_selection_trace" in required[scope]
        assert "capability_discovery_cadence_gate" in required[scope]


def test_continuous_required_mapping_is_generated_by_builder() -> None:
    assignment_value = continuous_required_assignment_value()

    assert isinstance(assignment_value, ast.Call)
    assert isinstance(assignment_value.func, ast.Name)
    assert assignment_value.func.id == "build_continuous_self_optimization_required"
    assert len(assignment_value.args) == 2
    assert all(isinstance(arg, ast.Name) for arg in assignment_value.args)
    assert [arg.id for arg in assignment_value.args] == [
        "CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED",
        "CONTINUOUS_SELF_OPTIMIZATION_SCOPE_REQUIRED_EXTRAS",
    ]
    assert assignment_value.keywords == []


def test_continuous_required_scope_extras_match_spec() -> None:
    verifier = load_verifier_module()
    expected_extras = {
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

    assert verifier.CONTINUOUS_SELF_OPTIMIZATION_SCOPE_REQUIRED_EXTRAS == expected_extras
    core_fields = set(verifier.CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED)
    for scope, extras in expected_extras.items():
        actual_extras = [
            field
            for field in verifier.CONTINUOUS_SELF_OPTIMIZATION_REQUIRED[scope]
            if field not in core_fields
        ]
        assert actual_extras == extras


def test_continuous_required_builder_rejects_missing_scope_extras() -> None:
    verifier = load_verifier_module()
    scope_extras = dict(verifier.CONTINUOUS_SELF_OPTIMIZATION_SCOPE_REQUIRED_EXTRAS)
    scope_extras.pop("release")

    try:
        verifier.build_continuous_self_optimization_required(
            verifier.CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED,
            scope_extras,
        )
    except ValueError as exc:
        assert "missing" in str(exc)
        assert "release" in str(exc)
    else:
        raise AssertionError("missing scope extras should raise ValueError")


def test_continuous_required_builder_rejects_unexpected_scope_extras() -> None:
    verifier = load_verifier_module()
    scope_extras = dict(verifier.CONTINUOUS_SELF_OPTIMIZATION_SCOPE_REQUIRED_EXTRAS)
    scope_extras["archive"] = []

    try:
        verifier.build_continuous_self_optimization_required(
            verifier.CONTINUOUS_SELF_OPTIMIZATION_CORE_REQUIRED,
            scope_extras,
        )
    except ValueError as exc:
        assert "unexpected" in str(exc)
        assert "archive" in str(exc)
    else:
        raise AssertionError("unexpected scope extras should raise ValueError")


def minimal_fixture(tmp: Path) -> None:
    common = "verify_governance_recovery_tool\n"
    write(tmp / "protocol.md", common)
    write(tmp / "route.md", common)
    write(
        tmp / "release.md",
        common
        + "## 2. 当前机器看版\n"
        + "next_route_value\n"
        + "rendered_pass\n"
        + "render_pingchang_check\n"
        + "25 页\n"
        + "四川省平昌县第二中学支教.pdf\n",
    )
    write(tmp / "changelog.md", common + "## 2. 当前机器看版\nnext_route_value\n")
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\nverify_governance_recovery_tool\nnext_route_value\n",
    )


def test_preset_fails_when_subagent_coverage_fields_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        minimal_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:subagent_problem_decomposition_builder" in failed_names
        assert "route_contains:source_role_map" in failed_names
        assert "long_log_contains:subagent_lifecycle_ledger" in failed_names


def full_fixture(tmp: Path, latest_extra: str = "") -> None:
    required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "capability_discovery_cadence_gate",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
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
    )
    write(tmp / "protocol.md", required + "\nrecovery_verifier_to_run may be discussed as a failure mode.\n")
    write(
        tmp / "route.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "capability_discovery_cadence_gate\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "best_practice_learning_contract\n"
        "capability_type_and_side_effect_gate\n"
        "external_state_write_guard\n"
        "skill_plugin_discovery_gate\n"
        "integration_lifecycle_gate\n"
        "transactional_integration_consistency_guard\n"
        "agentic_orchestration_capability_builder\n"
        "agent_topology_selection_trace\n"
        "subagent_orchestration_pattern_router\n"
        "desired_state_reconciliation_guard\n"
        "stateful_data_migration_guard\n"
        "security_incident_response_guard\n"
        "data_artifact_lineage_freshness_guard\n"
        "field_evidence_status\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "subagent_result_coverage_gate\n"
        "main_agent_integration_review\n"
        "claim_readiness_ladder\n"
        "parallel_evidence_lane_trace\n"
        "claim_lane_binding\n"
        "deployment_readiness_gate\n"
        "software_delivery_state_boundary_guard\n"
    )
    write(
        tmp / "release.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "capability_discovery_cadence_gate\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "best_practice_learning_contract\n"
        "capability_type_and_side_effect_gate\n"
        "external_state_write_guard\n"
        "skill_plugin_discovery_gate\n"
        "integration_lifecycle_gate\n"
        "transactional_integration_consistency_guard\n"
        "agentic_orchestration_capability_builder\n"
        "agent_topology_selection_trace\n"
        "subagent_orchestration_pattern_router\n"
        "desired_state_reconciliation_guard\n"
        "stateful_data_migration_guard\n"
        "security_incident_response_guard\n"
        "data_artifact_lineage_freshness_guard\n"
        "field_evidence_status\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "subagent_result_coverage_gate\n"
        "main_agent_integration_review\n"
        "claim_readiness_ladder\n"
        "parallel_evidence_lane_trace\n"
        "claim_lane_binding\n"
        "deployment_readiness_gate\n"
        "software_delivery_state_boundary_guard\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n"
        "rendered_pass\n"
        "render_pingchang_check\n"
        "25 页\n"
        "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "capability_discovery_cadence_gate\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "best_practice_learning_contract\n"
        "capability_type_and_side_effect_gate\n"
        "external_state_write_guard\n"
        "skill_plugin_discovery_gate\n"
        "integration_lifecycle_gate\n"
        "transactional_integration_consistency_guard\n"
        "agentic_orchestration_capability_builder\n"
        "agent_topology_selection_trace\n"
        "subagent_orchestration_pattern_router\n"
        "desired_state_reconciliation_guard\n"
        "stateful_data_migration_guard\n"
        "security_incident_response_guard\n"
        "data_artifact_lineage_freshness_guard\n"
        "field_evidence_status\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "subagent_result_coverage_gate\n"
        "main_agent_integration_review\n"
        "claim_readiness_ladder\n"
        "parallel_evidence_lane_trace\n"
        "claim_lane_binding\n"
        "deployment_readiness_gate\n"
        "software_delivery_state_boundary_guard\n"
        "历史记录可描述 recovery_verifier_to_run 这个失败词。\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口，可提 recovery_verifier_to_run\n"
        "## 2. 当前机器看版\n"
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "capability_discovery_cadence_gate\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "best_practice_learning_contract\n"
        "capability_type_and_side_effect_gate\n"
        "external_state_write_guard\n"
        "skill_plugin_discovery_gate\n"
        "integration_lifecycle_gate\n"
        "transactional_integration_consistency_guard\n"
        "agentic_orchestration_capability_builder\n"
        "agent_topology_selection_trace\n"
        "subagent_orchestration_pattern_router\n"
        "desired_state_reconciliation_guard\n"
        "stateful_data_migration_guard\n"
        "security_incident_response_guard\n"
        "data_artifact_lineage_freshness_guard\n"
        "field_evidence_status\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "subagent_result_coverage_gate\n"
        "main_agent_integration_review\n"
        "claim_readiness_ladder\n"
        "parallel_evidence_lane_trace\n"
        "claim_lane_binding\n"
        "deployment_readiness_gate\n"
        "software_delivery_state_boundary_guard\n"
        "next_route_value\n"
        f"{latest_extra}\n",
    )


def test_recovery_verifier_to_run_is_only_forbidden_in_latest_board() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        full_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 0, payload

    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        full_fixture(tmp, "status: recovery_verifier_to_run")
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "latest_no_recovery_verifier_to_run" in failed_names


def skill_plugin_missing_fixture(tmp: Path) -> None:
    required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
        ]
    )
    write(tmp / "protocol.md", required + "\nskill_plugin_discovery_record\n")
    write(tmp / "route.md", "verify_governance_recovery_tool\nsubagent_problem_decomposition_builder\nsource_role_map\n")
    write(
        tmp / "release.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n"
        "rendered_pass\n"
        "render_pingchang_check\n"
        "25 页\n"
        "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "next_route_value\n",
    )


def test_preset_fails_when_skill_plugin_learning_loop_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        skill_plugin_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:skill_plugin_learning_loop" in failed_names
        assert "route_contains:skill_plugin_learning_loop" in failed_names
        assert "long_log_contains:skill_plugin_learning_loop" in failed_names


def skill_plugin_project_fit_missing_fixture(tmp: Path) -> None:
    required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
        ]
    )
    write(tmp / "protocol.md", required + "\n")
    write(
        tmp / "route.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n",
    )
    write(
        tmp / "release.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n"
        "rendered_pass\n"
        "render_pingchang_check\n"
        "25 页\n"
        "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "next_route_value\n",
    )


def test_preset_fails_when_skill_plugin_project_fit_trace_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        skill_plugin_project_fit_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:skill_plugin_project_fit_trace" in failed_names
        assert "route_contains:skill_plugin_project_fit_trace" in failed_names
        assert "long_log_contains:skill_plugin_project_fit_trace" in failed_names


def source_authority_precedence_missing_fixture(tmp: Path) -> None:
    required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "subagent_method_learning_trace",
        ]
    )
    write(tmp / "protocol.md", required + "\n")
    write(
        tmp / "route.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "subagent_method_learning_trace\n",
    )
    write(
        tmp / "release.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "subagent_method_learning_trace\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n"
        "rendered_pass\n"
        "render_pingchang_check\n"
        "25 页\n"
        "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "subagent_method_learning_trace\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "subagent_method_learning_trace\n"
        "next_route_value\n",
    )


def test_preset_fails_when_source_authority_precedence_trace_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        source_authority_precedence_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:source_authority_precedence_trace" in failed_names
        assert "route_contains:source_authority_precedence_trace" in failed_names
        assert "long_log_contains:source_authority_precedence_trace" in failed_names


def subagent_method_learning_missing_fixture(tmp: Path) -> None:
    required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "source_authority_precedence_trace",
        ]
    )
    write(tmp / "protocol.md", required + "\n")
    write(
        tmp / "route.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n",
    )
    write(
        tmp / "release.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n"
        "rendered_pass\n"
        "render_pingchang_check\n"
        "25 页\n"
        "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "next_route_value\n",
    )


def test_preset_fails_when_subagent_method_learning_trace_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        subagent_method_learning_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:subagent_method_learning_trace" in failed_names
        assert "route_contains:subagent_method_learning_trace" in failed_names
        assert "long_log_contains:subagent_method_learning_trace" in failed_names


def claim_lane_binding_missing_fixture(tmp: Path) -> None:
    required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "parallel_evidence_lane_trace",
        ]
    )
    write(tmp / "protocol.md", required + "\n")
    write(
        tmp / "route.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "parallel_evidence_lane_trace\n",
    )
    write(
        tmp / "release.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "parallel_evidence_lane_trace\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n"
        "rendered_pass\n"
        "render_pingchang_check\n"
        "25 页\n"
        "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "parallel_evidence_lane_trace\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "parallel_evidence_lane_trace\n"
        "next_route_value\n",
    )


def test_preset_fails_when_claim_lane_binding_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        claim_lane_binding_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:claim_lane_binding" in failed_names
        assert "route_contains:claim_lane_binding" in failed_names
        assert "long_log_contains:claim_lane_binding" in failed_names


def deployment_readiness_gate_missing_fixture(tmp: Path) -> None:
    required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
        ]
    )
    write(tmp / "protocol.md", required + "\n")
    write(
        tmp / "route.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "parallel_evidence_lane_trace\n"
        "claim_lane_binding\n",
    )
    write(
        tmp / "release.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "parallel_evidence_lane_trace\n"
        "claim_lane_binding\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n"
        "rendered_pass\n"
        "render_pingchang_check\n"
        "25 页\n"
        "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "parallel_evidence_lane_trace\n"
        "claim_lane_binding\n"
        "## 2. 当前机器看版\n"
        "next_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        "verify_governance_recovery_tool\n"
        "subagent_problem_decomposition_builder\n"
        "source_role_map\n"
        "subagent_lifecycle_ledger\n"
        "skill_plugin_learning_loop\n"
        "skill_plugin_project_fit_trace\n"
        "source_authority_precedence_trace\n"
        "subagent_method_learning_trace\n"
        "parallel_evidence_lane_trace\n"
        "claim_lane_binding\n"
        "next_route_value\n",
    )


def test_preset_fails_when_deployment_readiness_gate_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        deployment_readiness_gate_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:deployment_readiness_gate" in failed_names
        assert "route_contains:deployment_readiness_gate" in failed_names
        assert "long_log_contains:deployment_readiness_gate" in failed_names


def orchestration_method_application_missing_fixture(tmp: Path) -> None:
    old_required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    old_route_release = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    old_changelog_long = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    write(tmp / "protocol.md", old_required + "\n")
    write(tmp / "route.md", old_route_release + "\n")
    write(
        tmp / "release.md",
        old_route_release
        + "\n## 2. 当前机器看版\n"
        + "next_route_value\n"
        + "rendered_pass\n"
        + "render_pingchang_check\n"
        + "25 页\n"
        + "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        old_changelog_long + "\n## 2. 当前机器看版\nnext_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        + old_changelog_long
        + "\nnext_route_value\n",
    )


def test_preset_fails_when_orchestration_method_application_fields_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        orchestration_method_application_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:best_practice_learning_contract" in failed_names
        assert "route_contains:main_agent_integration_review" in failed_names
        assert "long_log_contains:claim_readiness_ladder" in failed_names


def external_state_write_guard_missing_fixture(tmp: Path) -> None:
    old_required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "best_practice_learning_contract",
            "capability_type_and_side_effect_gate",
            "skill_plugin_discovery_gate",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    old_route_release = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "best_practice_learning_contract",
            "capability_type_and_side_effect_gate",
            "skill_plugin_discovery_gate",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    old_changelog_long = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "best_practice_learning_contract",
            "capability_type_and_side_effect_gate",
            "skill_plugin_discovery_gate",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    write(tmp / "protocol.md", old_required + "\n")
    write(tmp / "route.md", old_route_release + "\n")
    write(
        tmp / "release.md",
        old_route_release
        + "\n## 2. 当前机器看版\n"
        + "next_route_value\n"
        + "rendered_pass\n"
        + "render_pingchang_check\n"
        + "25 页\n"
        + "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        old_changelog_long + "\n## 2. 当前机器看版\nnext_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        + old_changelog_long
        + "\nnext_route_value\n",
    )


def test_preset_fails_when_external_state_write_guard_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        external_state_write_guard_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:external_state_write_guard" in failed_names
        assert "route_contains:external_state_write_guard" in failed_names
        assert "long_log_contains:external_state_write_guard" in failed_names


def integration_lifecycle_gate_missing_fixture(tmp: Path) -> None:
    old_required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "best_practice_learning_contract",
            "capability_type_and_side_effect_gate",
            "external_state_write_guard",
            "skill_plugin_discovery_gate",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    old_route_release = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "best_practice_learning_contract",
            "capability_type_and_side_effect_gate",
            "external_state_write_guard",
            "skill_plugin_discovery_gate",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    old_changelog_long = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "best_practice_learning_contract",
            "capability_type_and_side_effect_gate",
            "external_state_write_guard",
            "skill_plugin_discovery_gate",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    write(tmp / "protocol.md", old_required + "\n")
    write(tmp / "route.md", old_route_release + "\n")
    write(
        tmp / "release.md",
        old_route_release
        + "\n## 2. 当前机器看版\n"
        + "next_route_value\n"
        + "rendered_pass\n"
        + "render_pingchang_check\n"
        + "25 页\n"
        + "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        old_changelog_long + "\n## 2. 当前机器看版\nnext_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        + old_changelog_long
        + "\nnext_route_value\n",
    )


def test_preset_fails_when_integration_lifecycle_gate_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        integration_lifecycle_gate_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:integration_lifecycle_gate" in failed_names
        assert "route_contains:integration_lifecycle_gate" in failed_names
        assert "long_log_contains:integration_lifecycle_gate" in failed_names


def transactional_integration_consistency_guard_missing_fixture(tmp: Path) -> None:
    old_required = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "spawn_preflight",
            "agent_return_status",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "best_practice_learning_contract",
            "capability_type_and_side_effect_gate",
            "external_state_write_guard",
            "skill_plugin_discovery_gate",
            "integration_lifecycle_gate",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    old_route_release = "\n".join(
        [
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
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    old_changelog_long = "\n".join(
        [
            "verify_governance_recovery_tool",
            "subagent_problem_decomposition_builder",
            "source_role_map",
            "subagent_lifecycle_ledger",
            "skill_plugin_learning_loop",
            "skill_plugin_project_fit_trace",
            "best_practice_learning_contract",
            "capability_type_and_side_effect_gate",
            "external_state_write_guard",
            "skill_plugin_discovery_gate",
            "integration_lifecycle_gate",
            "source_authority_precedence_trace",
            "subagent_method_learning_trace",
            "subagent_result_coverage_gate",
            "main_agent_integration_review",
            "claim_readiness_ladder",
            "parallel_evidence_lane_trace",
            "claim_lane_binding",
            "deployment_readiness_gate",
        ]
    )
    write(tmp / "protocol.md", old_required + "\n")
    write(tmp / "route.md", old_route_release + "\n")
    write(
        tmp / "release.md",
        old_route_release
        + "\n## 2. 当前机器看版\n"
        + "next_route_value\n"
        + "rendered_pass\n"
        + "render_pingchang_check\n"
        + "25 页\n"
        + "四川省平昌县第二中学支教.pdf\n",
    )
    write(
        tmp / "changelog.md",
        old_changelog_long + "\n## 2. 当前机器看版\nnext_route_value\n",
    )
    write(
        tmp / "long_log.md",
        "## 1. 当前机器看版\n历史记录，不再作为当前入口\n"
        "## 2. 当前机器看版\n"
        + old_changelog_long
        + "\nnext_route_value\n",
    )


def test_preset_fails_when_transactional_integration_consistency_guard_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        transactional_integration_consistency_guard_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:transactional_integration_consistency_guard" in failed_names
        assert "route_contains:transactional_integration_consistency_guard" in failed_names
        assert "long_log_contains:transactional_integration_consistency_guard" in failed_names


def agentic_orchestration_capability_builder_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "agentic_orchestration_capability_builder")


def test_preset_fails_when_agentic_orchestration_capability_builder_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        agentic_orchestration_capability_builder_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:agentic_orchestration_capability_builder" in failed_names
        assert "route_contains:agentic_orchestration_capability_builder" in failed_names
        assert "long_log_contains:agentic_orchestration_capability_builder" in failed_names


def agent_topology_selection_trace_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "agent_topology_selection_trace")


def test_preset_fails_when_agent_topology_selection_trace_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        agent_topology_selection_trace_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:agent_topology_selection_trace" in failed_names
        assert "route_contains:agent_topology_selection_trace" in failed_names
        assert "long_log_contains:agent_topology_selection_trace" in failed_names


def subagent_orchestration_pattern_router_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "subagent_orchestration_pattern_router")


def test_preset_fails_when_subagent_orchestration_pattern_router_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        subagent_orchestration_pattern_router_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:subagent_orchestration_pattern_router" in failed_names
        assert "route_contains:subagent_orchestration_pattern_router" in failed_names
        assert "long_log_contains:subagent_orchestration_pattern_router" in failed_names


def desired_state_reconciliation_guard_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "desired_state_reconciliation_guard")


def test_preset_fails_when_desired_state_reconciliation_guard_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        desired_state_reconciliation_guard_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:desired_state_reconciliation_guard" in failed_names
        assert "route_contains:desired_state_reconciliation_guard" in failed_names
        assert "long_log_contains:desired_state_reconciliation_guard" in failed_names


def stateful_data_migration_guard_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "stateful_data_migration_guard")


def test_preset_fails_when_stateful_data_migration_guard_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        stateful_data_migration_guard_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:stateful_data_migration_guard" in failed_names
        assert "route_contains:stateful_data_migration_guard" in failed_names
        assert "long_log_contains:stateful_data_migration_guard" in failed_names


def security_incident_response_guard_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "security_incident_response_guard")


def test_preset_fails_when_security_incident_response_guard_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        security_incident_response_guard_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:security_incident_response_guard" in failed_names
        assert "route_contains:security_incident_response_guard" in failed_names
        assert "long_log_contains:security_incident_response_guard" in failed_names


def data_artifact_lineage_freshness_guard_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "data_artifact_lineage_freshness_guard")


def test_preset_fails_when_data_artifact_lineage_freshness_guard_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        data_artifact_lineage_freshness_guard_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:data_artifact_lineage_freshness_guard" in failed_names
        assert "route_contains:data_artifact_lineage_freshness_guard" in failed_names
        assert "long_log_contains:data_artifact_lineage_freshness_guard" in failed_names


def field_evidence_status_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "field_evidence_status")


def test_preset_fails_when_field_evidence_status_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        field_evidence_status_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:field_evidence_status" in failed_names
        assert "route_contains:field_evidence_status" in failed_names
        assert "long_log_contains:field_evidence_status" in failed_names


def software_delivery_state_boundary_guard_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "software_delivery_state_boundary_guard")


def test_preset_fails_when_software_delivery_state_boundary_guard_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        software_delivery_state_boundary_guard_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:software_delivery_state_boundary_guard" in failed_names
        assert "route_contains:software_delivery_state_boundary_guard" in failed_names
        assert "long_log_contains:software_delivery_state_boundary_guard" in failed_names


def capability_discovery_cadence_gate_missing_fixture(tmp: Path) -> None:
    full_fixture(tmp)
    remove_required_field_from_fixture(tmp, "capability_discovery_cadence_gate")


def test_preset_fails_when_capability_discovery_cadence_gate_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        capability_discovery_cadence_gate_missing_fixture(tmp)
        result = run_verifier(tmp)
        payload = json.loads(result.stdout)
        assert result.returncode == 1, payload
        failed_names = {item["name"] for item in payload["failures"]}
        assert "protocol_contains:capability_discovery_cadence_gate" in failed_names
        assert "route_contains:capability_discovery_cadence_gate" in failed_names
        assert "long_log_contains:capability_discovery_cadence_gate" in failed_names


if __name__ == "__main__":
    test_default_paths_resolve_inside_this_repository()
    test_continuous_required_core_fields_are_shared_across_scopes()
    test_continuous_required_mapping_is_generated_by_builder()
    test_continuous_required_scope_extras_match_spec()
    test_continuous_required_builder_rejects_missing_scope_extras()
    test_continuous_required_builder_rejects_unexpected_scope_extras()
    test_preset_fails_when_subagent_coverage_fields_missing()
    test_recovery_verifier_to_run_is_only_forbidden_in_latest_board()
    test_preset_fails_when_skill_plugin_learning_loop_missing()
    test_preset_fails_when_skill_plugin_project_fit_trace_missing()
    test_preset_fails_when_source_authority_precedence_trace_missing()
    test_preset_fails_when_subagent_method_learning_trace_missing()
    test_preset_fails_when_claim_lane_binding_missing()
    test_preset_fails_when_deployment_readiness_gate_missing()
    test_preset_fails_when_orchestration_method_application_fields_missing()
    test_preset_fails_when_external_state_write_guard_missing()
    test_preset_fails_when_integration_lifecycle_gate_missing()
    test_preset_fails_when_transactional_integration_consistency_guard_missing()
    test_preset_fails_when_agentic_orchestration_capability_builder_missing()
    test_preset_fails_when_agent_topology_selection_trace_missing()
    test_preset_fails_when_subagent_orchestration_pattern_router_missing()
    test_preset_fails_when_desired_state_reconciliation_guard_missing()
    test_preset_fails_when_stateful_data_migration_guard_missing()
    test_preset_fails_when_security_incident_response_guard_missing()
    test_preset_fails_when_data_artifact_lineage_freshness_guard_missing()
    test_preset_fails_when_field_evidence_status_missing()
    test_preset_fails_when_software_delivery_state_boundary_guard_missing()
    test_preset_fails_when_capability_discovery_cadence_gate_missing()
    print("ok")
