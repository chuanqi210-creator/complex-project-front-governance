# AGENTS.md

## Workspace Purpose

This project is the current authoritative workspace for the Complex project continuous-governance protocol extracted from `ai 科研`.

## Defaults

- Treat `/Users/chuchenqidawang/Documents/ai 科研` as historical source material only; do not read from it as an active dependency unless a task explicitly asks for comparison or recovery.
- Keep current protocol, recovery, validation, iteration, and history work inside this repository.
- Keep protocol edits narrow and traceable.
- Put core protocol changes in `protocol/`.
- Put scripts and validation helpers in `tools/`.
- Put Runtime Kit templates in `templates/`.
- Put project-level Codex capability manifests and optional local skills in `.codex/`.
- Put new explanatory notes in `docs/`.
- Put copied historical regression records and evidence in `docs/history/`.
- Put migration notes in `docs/migration/`.
- If creating worktrees, use `.worktrees/` and keep it ignored.

## Capability Discovery

- At task start, stage changes, blockers, verification failures, subagent/tool boundaries, and before final claims, actively reconsider useful capabilities instead of waiting for the user to name them.
- Scan broadly but lightly: installed skills, external skill libraries when relevant, callable tools, deferred tools, plugins/connectors, APIs, libraries, scripts, and external methods.
- Use `.codex/shared-skills.json` as a project-level capability candidate list when helpful, but still verify what is actually callable in the current environment.
- Use `docs/runtime-skill-management.md` to decide whether a skill, tool, plugin, connector, API, browser path, or external method should be selected, rejected, backlogged, or delegated to manual user action.
- Prefer small smoke tests before adopting new capabilities. Do not install or route through large skill/plugin sets just because they exist; record selected, rejected, backlog, and why.
- If a user names external tools, skills, APIs, databases, accounts, browsers, Auto Research, or Complex, bind those words into an explicit capability list before executing; state what will be used, skipped, backlogged, or delegated to manual user action.
- If another project asks to read Complex or Auto Research, first spend visible effort understanding the relevant protocol components, dynamic loop, scoring/route-back rules, delivery boundaries, and tool boundaries; do not start the project work from a shallow protocol mention.
- When another project reads Complex, start from `complex_behavior_kernel`: restore true state, classify project nature, assign decision rights, pick one highest-leverage question, run the lightest useful validation/execution, deliver to the right audience, and leave next-route recovery. Mechanism names are implementation details.
- For a new agent or new project onboarding, prefer `docs/complex_new_agent_5_minute_quickstart_20260702.md` before the long protocol. Use it to reach the behavior kernel, project nature router, Runtime Kit examples, and transcript review path quickly.
- If a user only says "use Complex" or "按 Complex 推进", show or apply the `complex_setup_question_card`: delivery audience, capability permissions, collaboration topology, cadence, and manual-action boundaries.
- Show new users the `user_visible_trigger_guide` in plain language: "先设计提示词/prompt", "连续节拍", "多线程/子代理", "外部工具/账号/API", "完整扫描 Complex", "只要人看版", "模型发现型/先发散研究框架/不要早收敛", "先做问题-观点-论据图", "强自治+护栏", "让 AI 自行判断细节", "动态推进", "只在高风险时问我", and "AI 自己调路线，但保留理由" are available steering words.
- At Complex entry, classify `project_nature` as evidence_fill, model_discovery, mixed, or execution_delivery. If the model, formula, metric, research frame, or explanation path is unsettled, protect model discovery before evidence filling.
- For model_discovery or pre-convergence mixed work, keep candidate frameworks, issue/position/pro/con argument maps, discriminating probes, and convergence conditions visible; do not let a local evidence gap or tool path become the main goal too early.
- Apply `adaptive_judgment_controller` by default: use strong autonomy with guardrails for reversible, low-side-effect project details, and let the agent choose route depth, Loop probes, evidence depth, capability fit, temporary subagent splits, long-thread duty micro-adjustments, and divergence/convergence pacing. Ask the user before changing the main goal, authorizing accounts/APIs/payment/publishing/external writes, performing irreversible actions, changing the delivery/public voice, taking high-risk real-world action, or making strong public claims without enough evidence.
- For strategic or critical route changes, use `route_evaluator_reflection_gate`: record selected route, rejected route, reason, highest misjudgment risk, counterexample, and rollback or recovery route. Do not turn this into a table ritual for routine fast judgments.
- If the user asks to scan Complex and design a project prompt before execution, apply `complex_prompt_bootstrap_gate`: scan the relevant protocol, ask/default startup choices, output a copy-ready prompt, and wait for confirmation before business execution unless the user explicitly authorizes immediate execution.
- In continuous prompt-based projects, apply `round_prompt_rehydration_gate` before each new Plan/Loop: recover the master prompt or active_goal_summary, current state, and round_goal into a `round_execution_prompt` so the round plan does not drift away from the total plan.

## Runtime Kit

- Treat `templates/` as optional landing pads for new projects: state, evidence, decision, search, question, prompt, framing, argument, judgment, loop, and delivery records.
- Prefer the filled golden examples in `docs/examples/` when teaching a new project how Runtime Kit records should look. Do not make users infer usage from empty templates alone.
- After protocol behavior edits, run `python3 tools/check_behavior_regression_pack.py` and `python3 tools/review_behavior_transcript.py --validate-rules` in addition to recovery verification.
- Do not turn Runtime Kit templates into new mandatory protocol fields unless repeated real project failures justify promotion.
- When bootstrapping a new Complex project, prefer a small runtime skeleton over copying the full protocol into the project workspace.
- Do not ask users to choose ordinary vs major project modes. Complex always uses Goal/Plan/Loop, scoring, delivery alignment, and recovery; high-risk or high-rework work only raises internal evidence and validation intensity.
- In continuous cadence, review topology, capabilities, prompt, and goal freshness by event trigger first; 3 rounds is only a fallback cap. If no route, project nature, evidence path, version, delivery audience, external boundary, or subthread-fit event changed, record lightweight keep instead of rerunning the full review.
- Distinguish active_goal_summary, tool Goal, and round_goal; do not let a stale or completed round goal stop a still-active continuous route.
- Do not use one long Codex tool Goal to carry dozens of continuous-cadence rounds. Store continuity in state, master prompt, closure routing, and next_route; use a narrow per-round tool Goal when a tool Goal is useful.
- If an existing tool Goal is blocked or stale but current_basis shows the project can continue, treat it as a Goal lifecycle mismatch, not as project blockage; write protocol_round_goal / goal_migration_note and continue.
- Treat the confirmed copy-ready prompt as the master prompt; later rounds inherit and patch it instead of silently replacing it.

## Delivery Defaults

- When the user requests a human-readable deliverable, keep machine boards, YAML, verifier internals, and protocol jargon out of the user-facing output unless they directly affect a decision.
- Before delivering comments, teacher-facing notes, third-party explanations, or mixed human/machine artifacts, align the audience, purpose, granularity, tone, and internal-information boundary.

## Verification

After protocol edits, prefer lightweight structural checks first:

```bash
python3 tools/verify_governance_recovery.py
python3 tools/test_verify_governance_recovery.py
```

If a checker is not applicable, record why in the task notes.
