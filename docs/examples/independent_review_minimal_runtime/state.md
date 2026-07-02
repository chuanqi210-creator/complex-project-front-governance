# State Example: Independent Review

## Current State

- project_goal: Review a Complex project plan without letting the prior chat steer the conclusion.
- project_nature: mixed
- convergence_status: provisionally_converged
- current_basis:
  - User wants an objective review of an existing plan.
  - The plan, evidence anchors, decisions, and unresolved questions can be separated from the conversation.
  - No external write, account action, or publication is authorized.
- not_current_basis:
  - The assistant's prior confidence in the plan.
  - User praise, frustration, or local corrections treated as proof.
  - Same-session roleplay treated as independent review.

## Behavior Kernel

- restore true state: distinguish reviewable artifacts from chat momentum.
- classify nature: mixed; review checks both reasoning frame and evidence boundary.
- decision rights: AI may prepare a fact ledger and run same-session diagnostic; true independent review needs clean context or read-only auditor.
- highest-leverage question: what is the smallest context packet that lets a reviewer judge the plan without inherited bias?
- lightest useful action: build a fact ledger and choose diagnostic vs independent route.
- delivery contract: separate diagnostic self-check from independent review result.
- next-route recovery: if independence is required, dispatch clean-context review; if not, deliver diagnostic with downgrade label.

## Adaptive Judgment

- judgment_mode: diagnostic
- autonomy_level: strong_autonomy_with_guardrails
- decision_right: ai_decide
- ask_user_needed: no
- ask_user_necessity: unnecessary
- ai_can_continue_without_user: yes
- human_input_drift_risk: medium
- ai_decided_without_user_reason: Preparing a fact ledger and labeling the review route are reversible and reduce context contamination.
- rollback_or_recovery_route: If user requires formal independence, route to clean-context reviewer or read-only audit subagent.

## Goal State

- active_goal_summary: Produce a review that separates facts, claims, evidence, and unresolved risks.
- round_goal: Build the fact ledger and decide whether this is diagnostic or independent review.
- next_route: run_clean_context_review_or_deliver_same_session_diagnostic
