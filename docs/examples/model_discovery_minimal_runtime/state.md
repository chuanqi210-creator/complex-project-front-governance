# State Example: Model Discovery

## Current State

- project_goal: Discover a strong explanation framework before evidence filling.
- project_nature: model_discovery
- convergence_status: pre_convergence
- current_basis:
  - User wants framework discovery before evidence table work.
  - Several plausible explanation paths exist.
  - No single model has been selected.
- not_current_basis:
  - Any first-pass framework treated as final.
  - Evidence rows that assume a model not yet chosen.

## Behavior Kernel

- restore true state: framework unsettled; evidence table not yet primary.
- classify nature: model_discovery.
- decision rights: AI may generate, merge, and reject candidate frameworks; ask before changing the project goal or delivery audience.
- highest-leverage question: which candidate framework best explains the project's core tension?
- lightest useful action: run a discriminating probe across candidate frameworks.
- delivery contract: interim human-readable explanation of options, not final proof.
- next-route recovery: converge only when conditions are met; otherwise keep candidate pool.

## Adaptive Judgment

- judgment_mode: exploratory
- autonomy_level: strong_autonomy_with_guardrails
- decision_right: ai_decide
- ask_user_needed: no
- ai_decided_without_user_reason: Candidate generation and probe design are reversible and directly serve the unsettled frame.
- rollback_or_recovery_route: If a chosen framework fails the probe, return to candidate pool and argument map.

## Goal State

- active_goal_summary: Find a project framing that can later be supported by evidence.
- round_goal: Produce 3-5 candidate frameworks and one discriminating probe.
- next_route: run_probe_then_decide_converge_or_continue_discovery
