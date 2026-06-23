# Gate Reference

This reference explains the protocol gates in practical language.

## Always-Minimum Gates

| Gate | Use |
| --- | --- |
| `current_basis` | Prevent stale, historical, or generated materials from becoming facts. |
| `evidence_matrix` | Tie important judgments to sources and evidence roles. |
| `decision_log` | Make key tradeoffs recoverable. |
| `traceability_matrix` | Keep user requirements from disappearing during execution. |
| `new_domain_governance_builder` | Build a temporary governance lens for unfamiliar project types. |

## Capability Gates

| Gate | Use |
| --- | --- |
| `capability_discovery_cadence_gate` | Decide when to reconsider skills, tools, plugins, APIs, external methods, and subagents. |
| `skill_plugin_discovery_gate` | Record candidates, selected tools, rejected tools, instruction-read evidence, and call/skip decisions. |
| `capability_type_and_side_effect_gate` | Distinguish local read-only skills from plugins, connectors, external writes, installs, and authorization. |

Capability adoption uses a small smoke test before promotion. Record the source, version or reference, micro-task, observed benefit, friction, risk, and one of four decisions: `adopt_now`, `adapt_later`, `backlog`, or `reject`.

Do not promote a single successful tool or skill trial into a required protocol rule. Promote only after repeated cross-project value, and only make it verifier-required when the behavior can be checked reliably by script.

## Validation Gates

| Gate | Use |
| --- | --- |
| `micro_task_execution_check` | Run a small real task before expanding scope. |
| `claim_readiness_ladder` | Keep claims at the evidence level they actually reached. |
| `anti_protocol_bloat_gate` | Keep the core protocol from absorbing every single-case detail. |

## Risk Gates

| Gate | Use |
| --- | --- |
| `external_state_write_guard` | Require authorization, target, data boundary, dry-run evidence, and rollback plan before external writes. |
| `integration_lifecycle_gate` | Prevent standards compatibility from being overstated as end-to-end integration. |
| `transactional_integration_consistency_guard` | Check idempotency, retries, ordering, reconciliation, and live/test boundaries for transactions and events. |
| `data_artifact_lineage_freshness_guard` | Track data artifact identity, source snapshots, transformations, validation, freshness, and stale downgrade. |
| `software_delivery_state_boundary_guard` | Separate issue, PR, CI, merge, release, package, deployment, real usage, and monitoring evidence. |
| `security_incident_response_guard` | Separate vulnerability signals, scanner alerts, exploitation, compromise, remediation, and disclosure state. |

## Recovery Gates

| Gate | Use |
| --- | --- |
| `change_inventory` | Summarize touched files, purpose, validation, and recovery entry. |
| `latest_board_tail_check` | Ensure the latest machine board is actually the latest recovery point. |
| `verify_governance_recovery_tool` | Check route, required fields, stale entries, and recovery consistency. |
