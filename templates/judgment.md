# Judgment Template

Use this file when the agent needs to decide route, depth, tools, collaboration, convergence pace, or whether to ask the user. Keep it short; this is a recovery record, not a long essay.

## Judgment Context

- project_nature:
- convergence_status:
- current_basis:
- round_goal:
- decision to make:
- uncertainty_level: low / medium / high
- reversibility: reversible / partly_reversible / irreversible
- side_effect_level: none / local_write / external_read / external_write / account_or_permission / real_world_action

## Adaptive Judgment

- judgment_mode: fast / diagnostic / exploratory / strategic / critical
- autonomy_level: strong_autonomy_with_guardrails / ask_before_strategic_change / maximum_autonomy
- decision_right: ai_decide / ask_user / manual_action_required / blocked_until_authorized
- ask_user_needed: yes / no
- ask_user_necessity: necessary / unnecessary / manual_action_required
- unnecessary_user_intervention_reason:
- ai_can_continue_without_user: yes / no
- human_input_drift_risk: low / medium / high
- ai_decided_without_user_reason:
- user_boundary_respected:
- continuous_runtime_activation_decision:
- topology_auto_activation_decision:
- review_context_reset_decision:
- downstream_activation_reconciliation_decision:
- residual_auto_beat_decision:

## Route Choice

- selected_route:
- rejected_routes:
- why_selected:
- highest_misjudgment_risk:
- counterexample_or_hostile_case:
- rollback_or_recovery_route:

## Follow-Through

- state_update_needed:
- prompt_patch_needed:
- topology_or_capability_change:
- delivery_contract_change:
- next_route:
