# Runtime State Template

Use this file to make a Complex project resumable. Keep it short enough that a later agent can recover the project without rereading every artifact.

## Project Snapshot

- Project:
- Current objective:
- Current stage:
- Current route:
- round_index:
- review_interval:
- current project version or milestone:
- Last updated:
- Owner or main thread:

## Project Nature

- project_nature: evidence_fill / model_discovery / mixed / execution_delivery
- convergence_status: divergent / candidate_pool_ready / provisionally_converged / evidence_fill_ready / execution_ready
- project_nature_router_status: pending / complete / route_back
- anti_premature_convergence_status: not_needed / active / passed / route_back
- candidate_frameworks:
- divergence_budget:
- discriminating_probe:
- convergence_switch_conditions:
- current scoring profile:

## Adaptive Judgment

- judgment_mode: fast / diagnostic / exploratory / strategic / critical
- autonomy_level: strong_autonomy_with_guardrails / ask_before_strategic_change / maximum_autonomy
- decision_right: ai_decide / ask_user / manual_action_required / blocked_until_authorized
- ask_user_needed: yes / no
- ask_user_necessity: necessary / unnecessary / manual_action_required
- ai_can_continue_without_user: yes / no
- human_input_drift_risk: low / medium / high
- ai_decided_without_user_reason:
- rollback_or_recovery_route:
- route_evaluator_reflection_status: not_needed / pending / complete
- last_strategic_or_critical_judgment:

## Human Intervention Boundary

- ai_auto_continue_allowed:
- known_next_step_auto_execute_rule: applicable / not_applicable / blocked_by_risk_or_authorization
- unnecessary_user_intervention_reason:
- must_ask_user_for:
- manual_action_required_for:
- context_pointers_user_provided:
- materials_ai_should_read_itself:
- user_input_classification: fact / preference / authorization / local_correction / goal_change / noise_or_possible_misleading
- independent_review_context_separation: not_needed / required / degraded_to_same_session_diagnostic
- downstream_activation_reconciliation: not_needed / pending / complete
- local_boundary_effect_on_steering_words:
- residual_auto_beat_available: yes / no
- residual_auto_beat_type: boundary_contradiction_repair / submission_friction_reduction / non_expansion_verification / exact_operator_handoff / preflight_after_env_var / none
- orchestration_contract_status: not_needed / pending / complete / degraded
- complex_source_resolution_status: explicit_user_path / local_authoritative_path / sibling_repo / target_adapter_only / unavailable_need_user_path
- complex_source:
- target_project_source:
- capability_preflight:
- resource_taxonomy_decision:
- authorization_status:
- beat_router_decision: CONTINUE / SPAWN_SUBAGENT / CREATE_THREAD / CREATE_AUTOMATION / INTERRUPT_FOR_INPUT / STOP_COMPLETE
- termination_condition:

## User Choices

- setup_question_card_status: asked / defaulted / not_needed
- prompt_bootstrap_status: not_requested / designing / awaiting_confirmation / confirmed / superseded
- prompt_bootstrap_location:
- master_prompt_location:
- round_prompt_status: not_needed / needs_rehydration / rehydrated / route_back_to_state_recovery
- last_prompt_refresh_round:
- delivery audience and format:
- capability permission: local_only / public_web_ok / browser_ok / account_required / API_ok / manual_action_required
- collaboration choice: main_thread / temporary_subagent / long_running_threads / parallel_review / undecided
- cadence choice: single_round_then_next_route / continuous_until_stopped
- continuous_runtime_activation_status: inactive / active / paused_by_boundary / degraded
- project nature preference or trigger words:
- autonomy preference or trigger words:
- evidence or privacy boundary:
- user_visible_trigger_guide_shown: yes / no

## Goal State

- active_goal_summary:
- round_goal:
- core_goal_plan_loop_status:
- codex_goal_lifecycle_mode: none / per_round_narrow_goal / long_goal_legacy / tool_unavailable
- next_beat_auto_start: yes / no / blocked_by_boundary
- current_tool_goal_status: not_used / active / complete / blocked / stale / unknown
- goal_handoff_carrier: state_next_route / closure_routing / master_prompt / codex_tool_goal / mixed
- protocol_round_goal:
- goal_refresh_status:
- stale_goal_check:
- goal_migration_note:
- manual_clear_needed:

## Collaboration Topology

- main thread responsibility:
- subagents or long-running threads:
- topology_auto_activation: not_needed / activated / recommended_only / blocked_by_authorization_or_tooling
- review_context_reset_each_round: not_needed / active / degraded_to_diagnostic
- current fit:
- next topology review:
- adjustment needed:

## Capability State

- selected now:
- rejected now:
- backlog:
- manual action:
- event_triggered_capability_refresh: due / lightweight_keep / completed / blocked
- refresh trigger:
- next capability review or fallback cap:

## Current Basis

Accepted as current basis:

-

Not current basis:

-

Unknown or stale:

-

## Open Questions

-

## Current Decisions

-

## Next Route

- next_route:
- route_reason:
- topology_refresh_due:
- capability_refresh_due:
- manual_action_required:
- next review trigger:

## Recovery Notes

- Files or links to read first:
- Files or links to ignore unless doing history comparison:
- Recent validation or QA evidence:
