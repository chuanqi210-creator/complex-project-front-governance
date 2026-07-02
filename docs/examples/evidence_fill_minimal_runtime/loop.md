# Loop Example: Evidence Fill

## Loop Purpose

- round_goal: Validate the weakest fixed metric source path.
- project_nature: evidence_fill
- convergence_status: converged_model
- judgment_mode: fast
- loop_type: evidence_check
- main_uncertainty: Whether Metric C has enough independent support for a third-party-facing statement.
- what_a_small_test_can_prove: Whether the current source path is strong enough to continue filling the table.
- what_it_cannot_prove: It cannot prove real-world impact.

## Micro Task

- task: Check one independent source for Metric C.
- inputs: fixed rubric, current evidence table, public source candidate.
- tool_or_method: local file read or public web source if authorized.
- timebox: 15 minutes.
- stop_condition: source found, source rejected, or access path needs escalation.

## Result

- observed_result: pending
- new_gap: source authority for Metric C still unknown.

## Route

- continue: if primary or high-quality source confirms Metric C.
- route_back: if only weak secondary descriptions are found.
- ask_user: only if access requires account, payment, private database, or rubric change.
- next_round_goal: Fill remaining metrics using the validated evidence path.
