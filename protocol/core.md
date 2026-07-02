# Complex Continuous Governance Core

Complex is a runtime protocol for complex projects. It is not a history log, a template dump, or a mode menu.

Core model:

> strong-autonomy continuous execution + evidence boundaries + anti-human/context-drift safeguards + auditable recovery.

## 1. Behavior Kernel

`complex_behavior_kernel` is the first execution spine. Every Complex round must do seven things:

1. Restore true state: identify `current_basis`, `not_current_basis`, latest user request, current materials, and prior decisions.
2. Classify project nature: run `project_nature_router` and choose `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights: run `adaptive_judgment_controller`, `decision_rights_matrix`, and `ask_user_necessity_gate`.
4. Pick one highest-leverage question.
5. Run the lightest useful validation or execution.
6. Deliver to the right audience.
7. Leave `next_route` and recovery notes.

If a mechanism name conflicts with these behaviors, the behavior kernel wins.

## 2. Project Nature

`project_nature_router` decides the operating profile:

- `evidence_fill`: the model, formula, metric, or framework is fixed. Use `evidence_matrix`, `claim_readiness_ladder`, and `delivery_contract`; record `divergence_noop_reason` when no model discovery is needed.
- `model_discovery`: the frame is unsettled. Use `anti_premature_convergence_gate`, `ibis_argument_map_gate`, `thought_search_gate`, and `judgment_mode: exploratory`.
- `mixed`: protect discovery until convergence conditions are met, then switch to evidence fill.
- `execution_delivery`: focus on implementation, packaging, delivery, and recovery.

Model discovery must keep candidate frameworks, issue / position / pro / con maps, counterexamples, convergence conditions, and discriminating probes visible. It must not let a local evidence gap become the main goal too early.

Evidence fill must not pay unnecessary divergence overhead. If the model is fixed, fill evidence, validate claims, and deliver.

## 3. Decision Rights

Complex defaults to strong autonomy with guardrails.

AI may decide:

- plan details
- Loop probes
- evidence depth
- tool/capability fit
- temporary subagent splits
- minor long-thread responsibility adjustments
- divergence/convergence pacing
- `lightweight_keep` when no refresh event exists

AI must ask before:

- changing the main goal
- using accounts, APIs, payment, publishing, or external writes
- irreversible file or system actions
- changing delivery/public voice
- taking high-risk real-world action
- making strong public claims without enough evidence

`manual_action_required` is for true access, permission, privacy, account, external-write, payment, publication, or real-world responsibility boundaries.

## 4. Anti-Human And Context Drift

`human_intervention_drift_guard` has two duties:

- prevent unsafe AI overreach
- prevent AI from offloading low-risk work back to the user

`known_next_step_auto_execute_rule`: if `next_route`, `round_goal`, state, or accessible materials already define a clear, low-risk, reversible next step, execute or validate it instead of asking "should I continue?"

Do not end a continuous-cadence response with "next time you say continue" or equivalent phrasing when the next route is already clear. If the environment or turn boundary truly prevents further work, record `next_route` as a recovery fact, not as a user-permission gate. The default is `auto_continue_until_boundary`, not `wait_for_user_continue`.

`context_pointer_first_intake`: if the user provides directories, files, links, exports, or material locations, read and summarize accessible materials before asking for manual cleanup, copy-paste, or summaries. Record `resource_boundary` only when access or authorization blocks intake.

`user_input_classification_gate`: classify new user input as fact, preference, authorization, local correction, goal change, or noise/possible misleading. Only goal changes and authorization boundaries rewrite the mainline.

## 5. Prompt And Continuous Cadence

`complex_prompt_bootstrap_gate` applies when the user asks to scan Complex and design a project prompt before execution.

`complex_source_resolution` runs before protocol scanning. Do not assume Complex lives inside the downstream target repository. Resolve sources in this order:

1. explicit user-provided Complex path or repository
2. current authoritative local workspace when available: `/Users/chuchenqidawang/Documents/complex-project-front-governance`
3. sibling/local repository names such as `complex-project-front-governance` or `complex-project-continuous-governance`
4. target-repository absorbed adapters/manifests only as downstream evidence, not as the authoritative Complex source
5. ask the user for the Complex path if none of the above is accessible

Keep two contexts separate:

- `complex_source`: the authoritative Complex Runtime Kit, normally `README.md`, `protocol/current-state.md`, `docs/quickstart.md`, `protocol/core.md`, templates, behavior cases, and examples.
- `target_project_source`: the repository being governed, such as its `AGENTS.md`, `CONTEXT.md`, status files, manifests, stage boards, code, and outputs.

If the target repository has no `Complex` directory, say that the target repo does not contain a local copy; then resolve the external Complex source. Do not treat unrelated candidate folders as target project material, and do not replace Complex scanning with downstream adapters unless the authoritative source is truly unavailable.

Output:

- `protocol_scan_sequence`
- startup questions or safe defaults
- project prompt rationale
- `copy_ready_prompt`
- `execution_bridge`

Do not execute business work before confirmation unless the user explicitly authorizes it.

`orchestration_contract`: when the user asks for Plan mode, continuous cadence, Goal mode, long-running threads, subagents, automation, or clean-context review, the Plan must design the runtime orchestration before business execution. This contract is not optional wording; it decides which runtime resources should be used, which are unavailable, and what the fallback is.

The contract must include:

- `capability_preflight`: check or state availability for Codex Goal/tool goals, user-visible Codex threads, worktree/background threads, automations/heartbeats, subagents, browser/API/account tools, and project-local scripts.
- `resource_taxonomy`: distinguish user-visible long-running Codex threads from short-lived subagents/workers, automations/heartbeats, and per-round tool Goals. Do not call a subagent a long-running thread.
- `authorization_status`: user-owned long threads, automations, account/API actions, external writes, publishing, and irreversible operations need explicit authorization. Short-lived read-only subagents may be used when the user requested subagents/review and the task is low-side-effect.
- `manager_worker_contract`: main thread is the manager; workers/subagents perform bounded work and return summaries. Workers do not complete the global goal or upgrade evidence.
- `beat_router`: every beat ends by selecting and executing or recording one route: `CONTINUE`, `SPAWN_SUBAGENT`, `CREATE_THREAD`, `CREATE_AUTOMATION`, `INTERRUPT_FOR_INPUT`, or `STOP_COMPLETE`.
- `termination_conditions`: goal complete, true external input missing, permission/account/API missing, no-write/evidence boundary, budget/time/safety limit, or user-only judgment.

`round_prompt_rehydration_gate` applies before each new Plan/Loop in a prompt-based or continuous project. Recover the master prompt or `active_goal_summary`, current state, and `round_goal` into `round_execution_prompt`.

Each round plan must say what comes from:

- master prompt
- prior state
- new judgment
- AI autonomous decision

`continuous_runtime_activation_contract`: when the user prompt or confirmed project prompt selects `连续节拍`, `continuous_until_stopped`, or equivalent wording, continuous cadence is an active execution contract, not a decorative steering word. Each beat must: rehydrate the round prompt, create or record a narrow `round_goal`, run the Loop, score/route, close or migrate the beat, and immediately enter the next low-risk reversible queued beat until a real boundary appears.

`downstream_activation_reconciliation`: when Complex is applied inside another repository, local `AGENTS.md`, `CONTEXT.md`, current state, stage boards, manifests, no-write boundaries, and manual-action records can narrow how steering words execute. Before concluding that cadence, subagents, review, or tools are active, reconcile each requested steering word with local project boundaries and mark it as `active_now`, `active_but_boundary_blocked`, `overridden_by_project_safety`, or `not_needed_with_reason`.

If the local project declares a true external-input or manual-action boundary, continuous cadence does not mean inventing evidence or bypassing the boundary. It means: execute any allowed residual beat first, such as hard-boundary contradiction repair, submission-friction reduction, non-expansion verification, exact operator handoff, or preflight once the required env var/file exists. Only after those are exhausted may the agent pause, and the pause must name the exact boundary, required file/env var, command, and why no further low-risk internal beat remains.

`per_round_goal_lifecycle_gate`: do not use one long tool Goal for many rounds. Use a narrow per-round goal. If an old tool Goal is stale or blocked while the project can continue, record `stale_or_blocked_tool_goal`, `goal_refresh_gate`, and `protocol_round_goal`; do not declare the whole project blocked.

If a Codex tool Goal is available and the user has requested continuous Complex execution, use it only for the current beat's narrow objective. When that beat completes and the next route is clear, create or record the next `protocol_round_goal` and continue. Do not wait for a new user message merely to start the next beat.

`continuous_cadence_refresh_gate`: refresh tools, topology, goals, and prompt by event trigger first. Three rounds is only a fallback cap.

## 6. Capability And Topology

`capability_discovery_cadence_gate` runs lightly at entry and when events justify it. Consider tools, skills, plugins, connectors, APIs, browsers, accounts, databases, and external methods.

Record capability choices as:

- selected
- rejected
- backlog
- `manual_action_required`

Use `capability_type_and_side_effect_gate` and `external_state_write_guard` for anything that can change external state.

Use `agent_topology_selection_trace` when work may need main-thread execution, temporary subagents, long-running threads, or review lanes. Use `read_only_audit_subagent_contract` for evidence or conformance review.

`topology_auto_activation_policy`: if the confirmed prompt authorizes strong-autonomy Complex execution and the work clearly benefits from temporary subagents, parallel review, or read-only audit, activate the available low-side-effect topology instead of merely recommending it. Ask the user only for user-owned long-thread creation, unavailable tools, account/API access, external writes, or other real authorization boundaries.

`independent_review_context_separation`: same-session roleplay is diagnostic only. True independent review requires clean context, a separate reviewer/thread, read-only audit subagent, different reviewer/model where available, or a fact-ledger-only packet. Track `human_input_drift_risk` when prior conversation may bias judgment.

`review_context_reset_each_round`: every independent review beat must start from a fresh fact-ledger packet or clean reviewer context. Reusing the full prior conversation is allowed only as same-session diagnostic review and must be labeled as such.

## 7. Delivery Contract

Run `deliverable_contract_gate` before output:

- audience
- purpose
- granularity
- tone
- internal-information boundary

Run `reader_translation_gate` for human-facing work. If the user says `只要人看版`, keep machine fields, YAML, verifier internals, and protocol jargon out of the main deliverable.

Keep human-readable delivery and machine recovery notes separate.

## 8. Setup Card And User-Visible Triggers

`complex_setup_question_card` applies when the user only says "use Complex" or "按 Complex 推进".

Ask or default only route-changing choices:

- delivery audience
- project nature
- capability permission
- collaboration topology
- cadence
- autonomy boundary
- manual-action boundary

`user_visible_trigger_guide` means steering words are visible to users, not hidden commands:

- `开启 Plan 模式 / 先规划再执行`
- `先设计提示词/prompt`
- `模型发现型 / 先发散研究框架 / 不要早收敛`
- `证据填充型 / 模型和指标已定`
- `连续节拍 / 总规划别丢 / 每轮 prompt 重水化`
- `多线程/子代理`
- `外部工具 / 账号 / API / skill`
- `少问我 / 能推进就继续 / 我给目录你自己读`
- `独立评审 / 客观审查 / 避免上下文污染`
- `只要人看版`

## 9. Runtime Kit And Evaluation

Runtime templates are optional landing pads, not required protocol fields.

Use filled examples before blank templates:

- evidence fill
- model discovery
- independent review

Behavior regression is the first line of protocol maintenance:

- `docs/behavior-regression-cases.json`
- `docs/behavior-transcript-review-rules.json`
- `tools/check_behavior_regression_pack.py`
- `tools/review_behavior_transcript.py`

Promotion rule:

1. Add or refine a behavior case.
2. Add or refine transcript review rules.
3. Add or refine a golden example.
4. Promote to this core protocol only when repeated/high-impact failures cannot be handled by the first three.

Do not add history archives, long machine-board logs, dated release packages, or one-off recovery records to the active protocol.
