# State Example: Evidence Fill

## Current State

- project_goal: Complete a source-backed evidence table for a fixed evaluation rubric.
- project_nature: evidence_fill
- convergence_status: converged_model
- current_basis:
  - The metric list is fixed by the user.
  - The output should support a human-readable summary.
  - Only local files and public sources are allowed in this round.
- not_current_basis:
  - Draft claims without source anchors.
  - Old candidate metrics not in the fixed rubric.

## Behavior Kernel

- restore true state: fixed rubric and current source set recovered.
- classify nature: evidence_fill; no model-discovery expansion.
- decision rights: AI may choose source order and verification depth; ask before external account/API/write actions.
- highest-leverage question: which fixed metric has the weakest source support?
- lightest useful action: verify one representative metric before filling the rest.
- delivery contract: third-party human-readable summary plus concise evidence boundary.
- next-route recovery: continue evidence checks if sample metric passes; route back if source authority is weak.

## Adaptive Judgment

- judgment_mode: fast
- autonomy_level: strong_autonomy_with_guardrails
- decision_right: ai_decide
- ask_user_needed: no
- ai_decided_without_user_reason: Source ordering and evidence-depth choices are reversible and inside the fixed rubric.
- rollback_or_recovery_route: If source authority is insufficient, route back to search/access escalation.

## Goal State

- active_goal_summary: Finish the fixed evidence table and delivery summary.
- round_goal: Validate one weak metric and decide whether the evidence path is adequate.
- next_route: evidence_check_then_fill_remaining_metrics
