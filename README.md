# complex-project-continuous-governance

Complex is a compact runtime kit for pushing complex projects forward with:

**strong-autonomy continuous execution + evidence boundaries + anti-human/context-drift safeguards + an auditable recovery chain.**

This repository is the current authoritative version. Older material is intentionally not kept in the working tree; Git history is the recovery path.

In this local Codex environment, the authoritative Complex workspace is:

`/Users/chuchenqidawang/Documents/complex-project-front-governance`

When a different project says "scan Complex", do not search only inside that target project. First resolve this authoritative Complex source, then read the target project separately. If the target repo has only `.git` or no `Complex` directory, that means there is no local copy inside the target repo; it does not mean Complex is unavailable.

## Install And Deploy

Complex is normally installed once as a separate local repository. Do not copy the whole Complex tree into every project. Keep one authoritative Complex workspace, then point each target project to it.

Recommended install:

```bash
mkdir -p ~/Documents
git clone https://github.com/chuanqi210-creator/complex-project-continuous-governance.git \
  ~/Documents/complex-project-front-governance
cd ~/Documents/complex-project-front-governance
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
```

Optional shell configuration:

```bash
export COMPLEX_HOME="$HOME/Documents/complex-project-front-governance"
```

Update an existing install:

```bash
cd "${COMPLEX_HOME:-$HOME/Documents/complex-project-front-governance}"
git pull --ff-only
python3 tools/verify_complex_integrity.py
```

Use Complex from another project by telling the agent where Complex is installed:

```text
请扫描 Complex 并为当前项目设计 prompt。
Complex 权威来源是：/absolute/path/to/complex-project-front-governance
目标项目是：/absolute/path/to/target-project
请分开读取 complex_source 和 target_project_source。
```

If `COMPLEX_HOME` is set, the agent may use it as the Complex source. If the target project has no `Complex` directory, the agent should still read the installed Complex workspace instead of declaring Complex missing.

## Current Entrypoints

- Core protocol: `protocol/core.md`
- Current state: `protocol/current-state.md`
- New-agent quickstart: `docs/quickstart.md`
- Runtime templates: `templates/`
- Filled runtime examples: `docs/examples/`
- Behavior regression pack: `docs/behavior-regression-cases.json`
- Transcript review rules: `docs/behavior-transcript-review-rules.json`
- Capability guide: `docs/runtime-skill-management.md`
- External method mapping: `docs/external-methods.md`

## How Complex Works

Complex starts from seven stable behaviors, not from a long menu of gates:

1. Restore the true current state.
2. Classify the project nature: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights: AI handles reversible low-risk details; user confirmation is required for goals, authorization, irreversible actions, public voice, high-risk claims, accounts, payments, publishing, or external writes.
4. Pick the single highest-leverage question for this round.
5. Run the lightest useful validation or execution.
6. Deliver to the right audience in the right form.
7. Leave `next_route` and recovery notes.

The practical default is strong autonomy with guardrails: if the next step is clear, low-risk, reversible, and within existing authorization, AI should continue instead of asking whether to continue. A queued `next_route` is an execution route, not a prompt for the user to say "continue" later. If a real turn or tool boundary stops the run, record the recovery route without making user continuation a permission gate. If the user gives directories, files, links, or material locations, AI should read accessible materials before asking for manual summaries.

When `连续节拍` is selected, it means runtime activation: each beat should create or record a narrow `round_goal`, run the Loop, route the result, and automatically start the next queued low-risk beat. It is not enough to write a plan that remembers the phrase. If temporary subagents, parallel review, or read-only audit are clearly useful and authorized, the agent should activate the available topology; independent review must use clean context or a fact-ledger packet each review beat.

When Complex is used inside another repository, local project rules can narrow steering words. The agent must reconcile requested steering words against that repo's `AGENTS.md`, `CONTEXT.md`, current state, manifests, stage boards, no-write boundaries, and manual-action records. If a true external-input boundary blocks the main route, the agent should still run allowed residual beats such as boundary contradiction repair, submission-friction reduction, non-expansion verification, or exact operator handoff before pausing.

Plan mode should produce an orchestration contract before execution when the user asks for continuous cadence, Goal mode, threads, subagents, automation, or independent review. The contract must distinguish user-visible long-running Codex threads from short-lived subagents, check whether Goal/thread/automation tools are available, define manager/worker responsibilities, and end each beat through a route such as `CONTINUE`, `SPAWN_SUBAGENT`, `CREATE_THREAD`, `CREATE_AUTOMATION`, `INTERRUPT_FOR_INPUT`, or `STOP_COMPLETE`.

## Best Project Prompt

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。

Complex 权威来源优先使用：/Users/chuchenqidawang/Documents/complex-project-front-governance。请把 Complex 协议源和目标项目材料分开读取：Complex 源读 README.md、protocol/current-state.md、docs/quickstart.md、protocol/core.md、templates、behavior cases 和 examples；目标项目再读它自己的 AGENTS.md、CONTEXT.md、状态文件、manifest、stage board 和代码。不要因为目标项目里没有 Complex 目录就说找不到 Complex；如果权威路径不可访问，再向我索要路径。

如果当前界面支持 Plan 模式，请先提醒我开启 Plan 模式完成协议扫描、项目判断和 prompt/plan 设计，再进入执行。
请在设计 prompt 前主动判断并显式使用这些 steering words，避免跑偏：
- 开启 Plan 模式 / 先规划再执行
- 模型发现型 / 先发散研究框架 / 不要早收敛
- 证据填充型 / 模型和指标已定
- 连续节拍 / 总规划别丢 / 每轮 prompt 重水化
- 每拍窄 Goal / 自动进入下一拍 / 不等我说继续
- 少问我 / 能推进就继续 / 我给目录你自己读
- 自动启用合适子代理 / 只读审核线程 / 每轮清上下文
- 独立评审 / 客观审查 / 避免上下文污染
- 外部工具 / 账号 / API / skill
- 只要人看版
```

If the project should move directly:

```text
这个项目按 Complex 推进。
目标是：……
已有材料在：……
我希望结果达到：……
采用强自治+护栏：可逆、低副作用的细节由 AI 自行判断；目标、授权、不可逆动作、外部写入、公开口径或高风险主张变化时再问我。
如果当前界面支持 Plan 模式，请先提醒我开启 Plan 模式完成扫描、判断和计划，再进入执行。
请显式判断这些 steering words 是否适用：开启 Plan 模式 / 先规划再执行；模型发现型 / 先发散研究框架 / 不要早收敛；证据填充型 / 模型和指标已定；连续节拍 / 总规划别丢 / 每轮 prompt 重水化；每拍窄 Goal / 自动进入下一拍 / 不等我说继续；少问我 / 能推进就继续 / 我给目录你自己读；自动启用合适子代理 / 只读审核线程 / 每轮清上下文；独立评审 / 客观审查 / 避免上下文污染；外部工具 / 账号 / API / skill；只要人看版。
如果 next_route / round_goal 已经给出清楚、低风险、可逆的下一步，不要以“下次你说继续”作为收尾；默认自动推进到下一拍。只有真实授权、外部写入、不可逆动作、高风险主张或回合/工具边界才暂停。
```

Useful steering words:

- `开启 Plan 模式 / 先规划再执行`
- `模型发现型 / 先发散研究框架 / 不要早收敛`
- `证据填充型 / 模型和指标已定`
- `连续节拍 / 总规划别丢 / 每轮 prompt 重水化`
- `每拍窄 Goal / 自动进入下一拍 / 不等我说继续`
- `少问我 / 能推进就继续 / 我给目录你自己读`
- `自动启用合适子代理 / 只读审核线程 / 每轮清上下文`
- `独立评审 / 客观审查 / 避免上下文污染`
- `外部工具 / 账号 / API / skill`
- `只要人看版`
- `目标仓库边界对账 / 真人工边界 / 剩余可自动小拍`
- `编排预检 / Goal mode / 长期线程 / automation / Beat Router / stop condition`

## Runtime Kit

Use the filled examples before blank templates:

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/examples/independent_review_minimal_runtime/`

Use templates only as needed:

- `templates/state.md`: current state, basis, goals, route, and human-intervention boundary.
- `templates/evidence.md`: evidence levels, gaps, and claim boundaries.
- `templates/decision.md`: selected route, rejected routes, and re-evaluation conditions.
- `templates/search.md`: search and acquisition escalation.
- `templates/question.md`: defaultable startup questions.
- `templates/prompt.md`: project prompt bootstrap and round prompt rehydration.
- `templates/framing.md`: model discovery, candidate frameworks, and convergence.
- `templates/argument.md`: issue / position / pro / con map.
- `templates/judgment.md`: autonomy, ask-user necessity, and rollback route.
- `templates/loop.md`: 5-30 minute validation loop.
- `templates/delivery.md`: human-readable and machine-recovery delivery contracts.

## Verification

Run these after protocol, template, behavior-pack, or site changes:

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
pnpm -C docs/protocol_explainer_site build
```

Expected baseline:

- behavior pack: 15 cases and 15 transcript rules
- integrity verifier: `failure_count: 0`
- site build: Vite build succeeds

## Repository Shape

- `protocol/`: current protocol and state only.
- `docs/`: quickstart, external mapping, behavior review, examples, and explainer site source.
- `templates/`: optional runtime records for downstream projects.
- `.codex/`: project-level capability candidates and optional local skills.
- `tools/`: lightweight structural and behavior-review checks.

Do not add history archives, migration records, rendered outputs, or long machine-board logs back into the active tree. If old context is needed, use Git history.
