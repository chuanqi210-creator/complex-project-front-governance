# Judgment Example: Diagnostic vs Independent Review

## Judgment Context

- project_nature: mixed
- convergence_status: provisionally_converged
- current_basis: reviewable artifacts and fact ledger are available.
- round_goal: choose the review route.
- decision to make: same-session diagnostic or independent review.
- uncertainty_level: medium
- reversibility: reversible
- side_effect_level: none

## Adaptive Judgment

- judgment_mode: diagnostic
- autonomy_level: strong_autonomy_with_guardrails
- decision_right: ai_decide
- ask_user_needed: no
- ask_user_necessity: unnecessary
- ai_can_continue_without_user: yes
- human_input_drift_risk: medium
- ai_decided_without_user_reason: The agent can label the review route and prepare a clean fact ledger without changing the project goal.
- user_boundary_respected: no external write, account action, publication, or irreversible file operation.

## Review Independence Decision

- same_session_diagnostic:
  - allowed_when: quick self-check, low stakes, no claim of independence.
  - must_label_as: diagnostic self-review.
  - cannot_claim: independent audit, fresh reviewer, context-free judgment.
- clean_context_independent_review:
  - use_when: user asks for independent review, high-stakes decision, repeated drift, or prior assistant confidence may bias judgment.
  - context_packet: fact-ledger.md plus artifacts under review.
  - exclude: full persuasion-heavy chat history unless a specific user intent dispute requires it.
- read_only_audit_subagent:
  - use_when: separate reviewer/subagent is available and the task is evidence or protocol conformance audit.
  - output_contract: findings, evidence gaps, unsupported claims, route-back recommendations.

## Route Choice

- selected_route: clean_context_independent_review_if_available_else_same_session_diagnostic_with_downgrade_label
- rejected_routes:
  - same_session_roleplay_as_independent: context contamination risk.
  - full_chat_dump_to_reviewer: transfers bias and makes review harder to reproduce.
- highest_misjudgment_risk: fact ledger may omit context that changes the goal or authorization boundary.
- rollback_or_recovery_route: add missing goal/authorization facts to fact ledger and rerun review.

## Follow-Through

- state_update_needed: yes
- prompt_patch_needed: no
- topology_or_capability_change: maybe read_only_audit_subagent
- delivery_contract_change: distinguish diagnostic vs independent review
- next_route: run_review_then_record_findings
