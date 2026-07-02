# Complex Quickstart

Audience: a new agent asked to use Complex on a project.

Goal: start useful work in five minutes without reading a historical log.

## Minute 0-1: Read The Current Entrypoints

Read, in order:

1. `README.md`
2. `protocol/current-state.md`
3. this file
4. the first part of `protocol/core.md`

Remember the one-sentence model:

> Complex = strong-autonomy continuous execution with evidence boundaries, anti-human/context-drift safeguards, and an auditable recovery chain.

If you are inside a downstream target project, resolve the Complex source before scanning the project. Prefer an explicit user path, then `COMPLEX_HOME`, then `/Users/chuchenqidawang/Documents/complex-project-front-governance`. If those paths are unavailable, look for sibling repos named `complex-project-front-governance` or `complex-project-continuous-governance`, then ask the user for the path. A target repo without a `Complex` directory only lacks a local copy; it does not prove Complex is unavailable.

## Minute 1-2: Use The Behavior Kernel

Before planning, compress the project into seven actions:

1. Restore true state.
2. Classify project nature and convergence.
3. Assign decision rights and ask-user necessity.
4. Pick one highest-leverage question.
5. Run the lightest useful validation or execution.
6. Deliver to the right audience.
7. Leave `next_route`.

If a mechanism name competes with these behaviors, the behavior kernel wins.

## Minute 2-3: Classify The Project

Choose one:

- `evidence_fill`: model, formula, metric, or framework is fixed; fill evidence and delivery boundary.
- `model_discovery`: framework, explanation path, metric, or research model is unsettled; protect candidate frames.
- `mixed`: start with model discovery, then switch to evidence fill when convergence conditions are met.
- `execution_delivery`: the main job is implementation, packaging, or delivery.

If unsure, default to `mixed` and make the uncertainty explicit.

## Minute 3-4: Pick A Runtime Shape

Use filled examples before blank templates:

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/examples/independent_review_minimal_runtime/`

Minimum records for a new project:

- `state.md`: current basis, goal, decision rights, and next route.
- `loop.md`: one small validation or explicit no-op.
- `delivery.md`: audience and output boundary.

Add only what the task needs:

- Evidence fill: `evidence.md`, `decision.md`, `search.md`.
- Model discovery: `framing.md`, `argument.md`, `judgment.md`.
- Independent review: `fact-ledger.md`, `judgment.md`, `decision.md`.
- Prompt-based continuity: `prompt.md`.

## Minute 4-5: Start Low-Friction Execution

If the user only says "按 Complex 推进", give short defaults instead of a mode menu:

- delivery audience:
- capability permission:
- topology:
- cadence:
- autonomy boundary:
- manual-action boundary:

Then make a narrow `round_goal` and execute the lightest useful next action.

Decision rights are two-sided:

- Prevent unsafe AI overreach.
- Prevent unnecessary human intervention.

If the next step is clear, low-risk, reversible, and inside existing authorization, continue and record why the user was not asked. Do not write "next time you say continue" when `next_route` is already queued; either execute the next route now or, if a real turn/tool boundary stops the run, record the recovery route without making user continuation a permission condition. If `连续节拍` is selected, start each beat from a narrow `round_goal`, run the Loop, close or migrate the beat, then automatically enter the next queued low-risk beat until a real boundary appears. If the user gives paths, files, links, or material locations, read accessible materials yourself before asking for manual cleanup or summaries.

When Complex is applied to another repository, reconcile the user's steering words with that repository's local rules before executing. Read local `AGENTS.md`, `CONTEXT.md`, current state, stage boards, manifests, no-write boundaries, and manual-action records. Mark each major steering word as active, boundary-blocked, safety-overridden, or not needed with reason. If the main route is blocked by a true external-input boundary, continue only with allowed residual beats: boundary contradiction repair, submission-friction reduction, non-expansion verification, exact operator handoff, or preflight after the required file/env var appears.

When the request mentions Plan mode plus continuous cadence, Goal mode, threads, subagents, automation, or independent review, write an orchestration contract before the project plan:

- Which runtime resources are available: Goal/tool goal, user-visible Codex thread, worktree/background thread, automation/heartbeat, subagent, browser/API/account tools.
- Which resource is being used now and why.
- Which resource is unavailable or needs explicit authorization.
- Manager/worker split: main thread manages, workers do bounded work.
- Beat Router: `CONTINUE`, `SPAWN_SUBAGENT`, `CREATE_THREAD`, `CREATE_AUTOMATION`, `INTERRUPT_FOR_INPUT`, or `STOP_COMPLETE`.
- Stop conditions.

If the user asks for independent review inside the same session, do not claim roleplay is independent. Use clean context, a separate reviewer/thread, read-only audit subagent, or a fact-ledger packet when independence matters. Reset review context every independent review beat; if you stay in the same session, label it as diagnostic self-review.

## When Something Feels Wrong

Do not immediately add a new core rule.

1. Map the failure to a case in `docs/behavior-regression-cases.json`.
2. Run transcript review:

```bash
python3 tools/review_behavior_transcript.py --case-id <case_id> --text-file <response.txt>
```

3. Record the result in `docs/behavior-review.md`.
4. If the failure repeats, update a transcript rule, behavior case, or golden example before promoting a new core rule.

## Best Default Prompt

```text
请先按 Complex 恢复当前状态，并用 7 步行为内核压缩本轮行动。
Complex 权威来源优先使用我提供的路径；如果没有提供，先查 `COMPLEX_HOME`，再查 /Users/chuchenqidawang/Documents/complex-project-front-governance。请分开读取 Complex 协议源和目标项目材料：Complex 源读 README.md、protocol/current-state.md、docs/quickstart.md、protocol/core.md、templates、behavior cases 和 examples；目标项目再读它自己的 AGENTS.md、CONTEXT.md、状态文件、manifest、stage board 和代码。不要因为目标项目里没有 Complex 目录就说找不到 Complex；如果权威路径不可访问，再向我索要路径。
如果当前界面支持 Plan 模式，请先提醒我开启 Plan 模式完成扫描、判断和计划，再进入执行。
请先显式判断这些 steering words 是否适用，并把适用项写入本轮 prompt/plan：开启 Plan 模式 / 先规划再执行；模型发现型 / 先发散研究框架 / 不要早收敛；证据填充型 / 模型和指标已定；连续节拍 / 总规划别丢 / 每轮 prompt 重水化；每拍窄 Goal / 自动进入下一拍 / 不等我说继续；少问我 / 能推进就继续 / 我给目录你自己读；自动启用合适子代理 / 只读审核线程 / 每轮清上下文；独立评审 / 客观审查 / 避免上下文污染；外部工具 / 账号 / API / skill；目标仓库边界对账 / 真人工边界 / 剩余可自动小拍；编排预检 / Goal mode / 长期线程 / automation / Beat Router / stop condition；只要人看版。
先判断本项目是 evidence_fill、model_discovery、mixed 还是 execution_delivery。
如果缺少我的确认，请给出少量可默认的问题；可逆、低副作用的细节由你自行判断，高风险、授权、外部写入、不可逆动作和公开口径变化再问我。
如果下一步已由 next_route / round_goal / 可访问材料说明清楚，请直接推进并说明为什么不需要回问；如果我给了目录、文件或链接，请优先自行读取。
不要用“下次你说继续时再推进”作为默认收尾。若下一拍已 queued 且低风险可逆，默认自动进入下一拍；若受回合或工具边界限制必须暂停，只记录 next_route，不把用户说“继续”当成许可门。
如果启用连续节拍，每一拍都要建立/记录窄 round_goal，执行 Loop 后自动进入下一拍；若需要独立评审，每一轮审核用清上下文、事实账本或只读审核线程，不把同 session 自评说成独立评审。
如果目标仓库本地规则把某个 steering word 缩窄或阻断，请明确做边界对账：哪些 active_now，哪些 active_but_boundary_blocked，哪些 overridden_by_project_safety，哪些 not_needed_with_reason。遇到真实外部输入门时，先做剩余可自动小拍；只有确实没有低风险内部小拍时，才暂停并给出具体文件、字段、env var 和命令。
如果请求涉及连续节拍、Goal、长期线程、子代理或 automation，先输出 Orchestration Contract：能力预检、资源术语消歧、授权状态、总控/worker 分工、Beat Router 和 stop condition。不要把子代理说成左侧栏长期线程；如果需要长期线程或 automation，说明是否已被用户明确授权创建。
本轮只抓一个最高杠杆问题，用最轻有效动作推进，最后给出适合交付对象的人看版，并留下 next_route。
```
