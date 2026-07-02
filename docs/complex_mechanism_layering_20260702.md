# Complex Mechanism Layering 2026-07-02

Purpose: reduce rule-density friction by telling future agents what to read first, what to treat as implementation detail, and what can be safely merged or demoted.

## Layer 0: Behavior Kernel

Read first. This is the stable contract:

1. Restore true state.
2. Classify project nature and convergence.
3. Assign decision rights and guardrails.
4. Pick one highest-leverage question.
5. Run the lightest useful validation or execution.
6. Deliver to the right audience.
7. Leave next-route recovery.

If an agent only remembers one part of Complex, it should remember this layer.

## Layer 1: Routers And Controllers

Use these to choose the route:

- `project_nature_router`
- `adaptive_judgment_controller`
- `dynamic_stage_controller`
- `continuous_cadence_refresh_gate`
- `round_prompt_rehydration_gate`
- `per_round_goal_lifecycle_gate`

These mechanisms should be visible in planning and recovery records, but they should not become a user-facing mode menu.

## Layer 2: Guards And Gates

Use these when a risk or event triggers them:

- Evidence and claim guards: `evidence_matrix`, `claim_readiness_ladder`, `source_authority_precedence_trace`.
- External-action guards: `capability_type_and_side_effect_gate`, `external_state_write_guard`.
- Collaboration guards: `agent_topology_selection_trace`, `subagent_result_coverage_gate`, `main_agent_integration_review`.
- Discovery guards: `anti_premature_convergence_gate`, `ibis_argument_map_gate`, `thought_search_gate`.

Do not run every guard on every task. Activate by project nature, uncertainty, reversibility, side effects, and delivery stakes.

## Layer 3: Runtime Kit Templates

Use these as landing pads, not as mandatory forms:

- Always useful for recovery: `state.md`, `loop.md`, `delivery.md`.
- Evidence-fill tasks: add `evidence.md`, `decision.md`, `search.md` as needed.
- Model-discovery tasks: add `framing.md`, `argument.md`, `judgment.md` as needed.
- Prompt-based continuous work: add `prompt.md`.

Templates are allowed to be partial. A short filled record that keeps the next agent moving is better than a complete empty form.

## Layer 4: Examples And Behavior Regression

Use these to teach behavior:

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/behavior_regression_cases_20260702.json`
- `docs/behavior_transcript_review_rules_20260702.json`
- `docs/behavior_review_result_template_20260702.md`
- `docs/real_project_pressure_test_result_template_20260702.md`
- `tools/check_behavior_regression_pack.py`
- `tools/review_behavior_transcript.py`

When a real project exposes a repeated failure, first add or update a behavior case, transcript review rule, or golden example. Promote to the core protocol only if the pattern repeats and cannot be handled by examples or transcript review.

## Layer 5: History, Release, And Verifier

Use these for maintenance, not for normal project onboarding:

- `protocol/持续治理协议_二十个跨渠道项目逆向校验实验.md`
- `protocol/持续优化变更清单_20260622.md`
- `protocol/持续治理协议发布包_20260622.md`
- `docs/history/`
- `tools/verify_governance_recovery.py`
- `tools/test_verify_governance_recovery.py`

These keep the project recoverable. They should not be copied into new project workspaces unless the task is protocol maintenance or regression debugging.

## Merge And Delete Rules

- If two mechanisms trigger at the same point and produce the same decision, merge their user-facing explanation.
- If a mechanism is only a historical alias, keep it in compatibility notes rather than in the entry path.
- If a mechanism is useful only for one domain, move it to history or examples.
- If a mechanism improves no behavior-kernel step, delete or backlog it.
- If a mechanism is useful but heavy, make it event-triggered and provide a lightweight keep path.

## New Project Read Order

1. `docs/complex_new_agent_5_minute_quickstart_20260702.md`.
2. README recommended entry.
3. Behavior kernel in the main protocol.
4. Setup question card and user-visible triggers.
5. Project-nature router and adaptive judgment boundary.
6. Runtime Kit template subset for the task.
7. Examples matching the project profile.
8. Detailed gates only when the route actually triggers them.
