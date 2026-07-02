# AGENTS.md

## Workspace Purpose

This directory contains the current authoritative Complex project continuous-governance protocol files for this repository. Preserve traceability while keeping active protocol work local to this project.

## Operating Defaults

- Inspect project files, outputs, logs, and current app state before asking the user for information that can be discovered locally.
- Act directly on low-risk tasks such as file organization, document/image processing, rendering, export checks, and local diagnostics.
- Treat `/Users/chuchenqidawang/Documents/ai 科研` as historical source material, not an active dependency. Do not mutate it unless explicitly asked.
- Do not overwrite source materials. Create dated outputs, backups, or new versions for generated documents and transformed files.
- Ask before irreversible deletion, account/security/privacy changes, password entry, publishing/submitting, payments, or destructive commands.
- Verify outputs before reporting completion, especially rendered documents, generated images, archives, and converted files.
- At protocol task start, stage changes, blockers, verification failures, subagent/tool boundaries, and before final claims, actively reconsider useful skills, tools, plugins, connectors, APIs, libraries, scripts, and external methods; use small smoke tests before adopting anything new.
- For runtime capability work, use `.codex/shared-skills.json` as a candidate list only; still verify actual callable tools and side-effect boundaries in the current environment.
- When users mention external tools, skills, APIs, databases, browser access, accounts, Auto Research, or Complex, convert those hints into an explicit capability list with selected, rejected, backlog, and manual-action items before executing.
- When a new project asks to read Complex or Auto Research, first understand the relevant protocol components, tool boundaries, Loop/scoring rules, runtime templates, and delivery rules; shallow acknowledgment is not enough.
- When a new project reads Complex, start from `complex_behavior_kernel`: restore true state, classify project nature, assign decision rights, pick one highest-leverage question, run the lightest useful validation/execution, deliver to the right audience, and leave next-route recovery. Use mechanism names only after this behavior spine is clear.
- For a new agent or new project onboarding, prefer `docs/complex_new_agent_5_minute_quickstart_20260702.md` before the long protocol. Use it to reach the behavior kernel, project nature router, Runtime Kit examples, and transcript review path quickly.
- When a user only says "use Complex" or "按 Complex 推进", apply the `complex_setup_question_card`: delivery audience, external capability permission, collaboration topology, cadence, and manual-action boundaries. If unanswered and safe, record defaults instead of blocking.
- Show new users the `user_visible_trigger_guide` in ordinary language so they know "先设计提示词/prompt", "连续节拍", "多线程/子代理", "外部工具/账号/API", "完整扫描 Complex", "只要人看版", "模型发现型/先发散研究框架/不要早收敛", "先做问题-观点-论据图", "强自治+护栏", "让 AI 自行判断细节", "动态推进", "只在高风险时问我", and "AI 自己调路线，但保留理由" are available steering words.
- At Complex entry, classify `project_nature` as evidence_fill, model_discovery, mixed, or execution_delivery. If model, formula, metric, research frame, explanation path, or story line is unsettled, protect divergent model discovery before evidence filling.
- For model_discovery or pre-convergence mixed work, preserve candidate frameworks, issue/position/pro/con argument maps, discriminating probes, and convergence conditions; do not let an easy evidence gap or tool route become the main goal too early.
- Apply `adaptive_judgment_controller` by default. The agent may decide reversible, low-side-effect project details such as plan details, Loop probes, evidence depth, capability fit, temporary subagent splits, long-thread duty micro-adjustments, and divergence/convergence pacing. Ask before main-goal changes, accounts/APIs/payment/publishing/external writes, irreversible actions, delivery/public-voice changes, high-risk real-world action, or strong public claims without enough evidence.
- For strategic or critical route changes, use `route_evaluator_reflection_gate` to record selected route, rejected route, reason, highest misjudgment risk, counterexample, and rollback or recovery route; keep routine fast judgments lightweight.
- When the user asks to scan Complex and design a project prompt before execution, apply `complex_prompt_bootstrap_gate`: scan the relevant protocol, ask/default startup choices, output a copy-ready prompt, and wait for confirmation before business execution unless the user explicitly authorizes immediate execution.
- In continuous prompt-based projects, apply `round_prompt_rehydration_gate` before each new Plan/Loop so the round plan inherits the master prompt, current state, and round_goal instead of drifting into a local-only plan.
- Do not ask users to choose ordinary vs major project modes. Complex always has Goal/Plan/Loop, scoring, delivery alignment, and recovery; high-risk or high-rework signals only raise internal evidence and validation intensity.
- When users mention continuous cadence, long-running threads, subagents, Goal mode, Plan mode, or version drift, check round_index, topology fit, capability fit, and goal freshness before continuing. Use event-triggered refresh first; 3 rounds is a fallback cap, not a mechanical full review.
- Do not put a whole continuous cadence into one long Codex tool Goal. Continuity belongs in state, master prompt, closure routing, and next_route; Codex tool Goal should normally be one narrow round objective that can be completed at the end of that beat.
- If a tool Goal is blocked or stale while current_basis and next_route still show usable progress, record a goal lifecycle mismatch and continue via protocol_round_goal / goal_migration_note instead of declaring the project blocked.
- For human-readable deliverables, keep protocol jargon, machine board fields, and internal state out of the main explanation unless they are necessary for the reader's decision.
- For comments, teacher-facing notes, third-party summaries, or mixed human/machine outputs, align audience, purpose, granularity, tone, and internal-information boundary before final delivery.

## File Placement

- Keep protocol artifacts inside this repository when one is clear.
- Put Runtime Kit templates in `templates/` and runtime capability notes in `docs/runtime-skill-management.md`; model-discovery landing pads belong in `templates/framing.md` and `templates/argument.md`, and adaptive route/depth decisions belong in `templates/judgment.md`.
- Put filled Runtime Kit examples in `docs/examples/`; use them to reduce onboarding friction before adding more empty template fields.
- After protocol behavior edits, run `python3 tools/check_behavior_regression_pack.py` and `python3 tools/review_behavior_transcript.py --validate-rules` along with the recovery verifier.
- Put project-level capability manifests and optional local skills in `.codex/`.
- Put copied historical records in `docs/history/` and migration notes in `docs/migration/`.
- Use `/Users/chuchenqidawang/Documents/日常/03_产出_Deliverables/` for general final deliverables that do not belong to a specific research project.
- Use `/Users/chuchenqidawang/Documents/日常/00_入口_Inbox/Codex抓取待复核/` for uncertain captures or external materials pending review.
- Record important operation notes in the project folder or in `/Users/chuchenqidawang/Documents/日常/00_文件管理规则/`.

## Reference Protocol

Use repository-local protocol files as the active governance source. External file-management rules may provide background defaults, but this repository owns current continuous-governance protocol maintenance.
