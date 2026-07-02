# Prompt Bootstrap Template

Use this file when a user wants the agent to scan Complex, design a project-specific prompt, and execute only after confirmation.

This prompt is an execution contract for one project. It does not replace the Complex protocol, the user's latest instruction, or authorization boundaries.

## High-Fit User Request

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。

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
- 目标仓库边界对账 / 真人工边界 / 剩余可自动小拍
- 编排预检 / Goal mode / 长期线程 / automation / Beat Router / stop condition
- 只要人看版
```

## Protocol Scan Summary

- Complex source resolution:
- complex_source files read:
- target_project_source files read:
- Complex files or sections read:
- Components adopted now:
- Components skipped now:
- Components backlogged:
- Manual actions or permissions needed:
- Biggest misread risk:

## Project Intake

- Project goal:
- Existing materials:
- User steering words:
- Plan mode reminder status:
- Current basis:
- Known constraints:
- High-risk or high-rework signals:
- Project nature: evidence_fill / model_discovery / mixed / execution_delivery
- Convergence status:
- Candidate frameworks or known fixed model:

## Startup Questions or Defaults

- Delivery audience and format:
- Capability permission:
- Collaboration topology:
- Cadence:
- Continuous runtime activation:
- Review context reset policy:
- Downstream activation reconciliation:
- Orchestration contract:
- Project nature and convergence preference:
- Autonomy and judgment boundary:
- Evidence, privacy, account, publishing, or manual-action boundary:

## Prompt Design Rationale

- Why this goal needs Complex:
- Why this project is evidence_fill / model_discovery / mixed / execution_delivery:
- What the agent may decide without asking:
- What must trigger user confirmation:
- Why these capabilities are selected or rejected:
- Why this collaboration topology fits:
- Why this cadence fits:
- What the first Loop should test:
- What prevents premature convergence:
- What would trigger route-back:

## Copy-Ready Prompt

```text
请按 Complex 项目持续治理协议推进以下项目。

Complex 权威来源：
- 默认安装路径：`$COMPLEX_HOME` 或 `~/Documents/complex-project-front-governance`
- 可迁移配置：如果环境变量 `COMPLEX_HOME` 存在，优先用它作为 Complex 安装路径。
- 如果用户另给 Complex 路径，以用户路径为准。
- 如果目标项目没有 Complex 目录，不要说 Complex 不存在；先尝试上述权威路径或同级 `complex-project-front-governance` / `complex-project-continuous-governance`。
- 如果仍不可访问，只说“Complex 权威源不可访问，需要用户提供路径”，不要编造协议内容。

上下文分离：
- complex_source：README.md、protocol/current-state.md、docs/quickstart.md、protocol/core.md、templates、behavior cases、examples。
- target_project_source：目标仓库的 AGENTS.md、CONTEXT.md、状态文件、manifest、stage board、代码和 outputs。
- 下游 adapter / manifest 只能作为目标项目已吸收 Complex 的证据，不能替代 Complex 权威源，除非权威源不可访问。

项目目标：

已有材料：

当前交付对象和交付形式：

能力边界：
- 可用：
- 暂不使用：
- 需要用户授权或人工操作：

协作拓扑：

推进节拍：

Plan 模式：
- 如果当前界面支持 Plan 模式：先提醒用户开启 Plan 模式完成协议扫描、项目判断和 prompt/plan 设计，再进入执行。
- 如果当前界面不支持 Plan 模式：仍先输出计划和 round_execution_prompt，不直接跳到业务执行。

自动推进默认：
- 如果 next_route / round_goal / state 已经给出清楚、低风险、可逆且已授权的下一步：直接进入下一拍，不要等待用户说“继续”。
- 禁止默认收尾话术：下次你说继续时、等你说继续、你确认继续后、是否继续、要不要继续。
- 如果受回合、工具或权限边界限制必须暂停：只记录 next_route 和暂停原因，不把用户说“继续”写成许可条件。

连续节拍运行契约：
- 如果选择“连续节拍”：它是执行契约，不是提示词装饰词。
- 每一拍必须先重水化 round_execution_prompt，再建立/记录一个窄 round_goal，执行 Loop、评分路由、关闭或迁移本拍，然后自动进入下一拍 queued 的低风险可逆任务。
- Codex 工具 Goal 如果可用，只用于当前一拍；完成后立刻创建/记录下一拍 protocol_round_goal。不要用一个长期工具 Goal 承载几十拍，也不要等用户再说继续才开启下一拍。

协作拓扑自动启用：
- 如果临时子代理、并行检查或只读审核能明显降低风险且不触发外部副作用：自动启用可用拓扑，而不是只建议用户以后开启。
- 若创建用户可见长期线程、新账号/API、外部写入或不可逆动作需要授权：记录 manual_action_required，再回问。
- 独立评审每一轮都必须清上下文、使用事实账本/只读审核线程/独立 reviewer；同 session 自评只能标为 diagnostic self-review。

目标仓库激活对账：
- 如果该 prompt 被复制到另一个仓库：先读取目标仓库的 AGENTS.md、CONTEXT.md、当前状态、stage board、manifest、no-write boundary 和 manual_action_required 记录。
- 对每个 steering word 标记：active_now / active_but_boundary_blocked / overridden_by_project_safety / not_needed_with_reason。
- 如果本地项目要求真实外部输入、账号、人工标注或 no-write 边界确认：不要把它误判成 Complex 失败，也不要绕过；先执行允许的剩余小拍，包括硬边界矛盾修复、提交摩擦降低、非扩张验证、精确 operator handoff，或在文件/env var 已出现后运行 preflight。
- 只有没有可逆低风险剩余小拍时才暂停，并给出具体文件、字段、env var、命令和不能替代的原因。

运行编排协议：
- 先做 capability_preflight：Goal/tool goal、左侧栏长期 Codex thread、worktree/background thread、automation/heartbeat、subagent、browser/API/account tools、项目本地脚本分别是否可用。
- 先做 resource_taxonomy：Codex thread 是用户可见长期线程；subagent 是短生命周期 worker；automation/heartbeat 是定时唤醒；per-round Goal 是当前一拍目标。不要把子代理叫成长线程。
- 明确 authorization_status：创建用户可见长期 thread、automation、账号/API、外部写入、发布或不可逆动作需要明确授权；用户已要求只读审核/子代理时，可在低副作用场景直接启用短生命周期子代理。
- 主线程是 manager，只维护 global_goal、beat_queue、current_basis/not_current_basis、open resources、stop conditions、next beat；worker 只做 bounded work 并回传摘要。
- 每拍结束必须执行 Beat Router：CONTINUE / SPAWN_SUBAGENT / CREATE_THREAD / CREATE_AUTOMATION / INTERRUPT_FOR_INPUT / STOP_COMPLETE。
- 只有 stop condition 可以停：目标完成、真实外部输入缺失、权限/账号/API 缺失、no-write/evidence boundary、预算/时间/安全限制、不可替代用户判断。

Steering words to preserve:
- 开启 Plan 模式 / 先规划再执行：
- 模型发现型 / 先发散研究框架 / 不要早收敛：
- 证据填充型 / 模型和指标已定：
- 连续节拍 / 总规划别丢 / 每轮 prompt 重水化：
- 每拍窄 Goal / 自动进入下一拍 / 不等我说继续：
- 少问我 / 能推进就继续 / 我给目录你自己读：
- 自动启用合适子代理 / 只读审核线程 / 每轮清上下文：
- 独立评审 / 客观审查 / 避免上下文污染：
- 外部工具 / 账号 / API / skill：
- 目标仓库边界对账 / 真人工边界 / 剩余可自动小拍：
- 编排预检 / Goal mode / 长期线程 / automation / Beat Router / stop condition：
- 只要人看版：

自适应判断边界：
- autonomy_level：strong_autonomy_with_guardrails
- AI 可自行判断：
- 必须回问用户：
- judgment_mode 初始默认：
- rollback_or_recovery_route：

项目性质与收敛状态：
- project_nature：
- convergence_status：
- 如果模型/研究框架未定：先保留候选框架、问题-观点-论据图和可区分探针，不直接进入证据填表。
- 如果模型/表格已定：记录 divergence_noop_reason，避免形式化发散。

目标与计划：
- active_goal_summary（长期方向，写入 state/master prompt，不等同于长期工具 Goal）：
- round_goal：
- Codex 工具 Goal 生命周期：本拍窄目标 / 不使用 / 迁移旧目标
- 本轮计划：

Loop 小循环：
- 最大不确定性：
- 本轮 loop_type：framework_probe / evidence_check / capability_trial / execution_check
- candidate_framework_or_evidence_path：
- discriminating_probe：
- 5-30 分钟验证动作：
- 通过标准：
- 失败后的 route-back：

评分与动态路由：
- 证据充分性：
- 风险/返工：
- 能力匹配：
- 用户确认需求：
- 下一步路由：

交付契约：
- 人看版：
- 机器恢复记录：
- 不应暴露的内部信息：

请先解析 Complex 来源：优先使用用户提供路径，其次查 `COMPLEX_HOME`，再使用 `~/Documents/complex-project-front-governance`，最后查同级 Complex 仓库；不要只在目标项目里找 Complex。请先恢复或建立 state/current_basis，再判断 project_nature 和 convergence_status，并逐项判断上述 steering words 是否适用。如果当前界面支持 Plan 模式，请先提醒用户开启 Plan 模式完成协议扫描、项目判断和 prompt/plan 设计，再执行本轮 round_goal；如果不支持，也要先输出计划和 round_execution_prompt，不直接跳到业务执行。若请求涉及连续节拍、Goal、长期线程、子代理、automation 或独立评审，先输出 Orchestration Contract：能力预检、资源术语消歧、授权状态、总控/worker 分工、Beat Router 和 stop condition。若在目标仓库中执行，先把上述 steering words 与目标仓库 AGENTS/CONTEXT/current status/stage board/manifest/no-write/manual_action_required 做激活对账，明确哪些 active_now、哪些被真实边界阻断、哪些被项目安全规则覆盖、哪些当前不需要。每轮结束时留下 next_route；如果启用连续节拍，每拍使用窄 round_goal，连续性由 state、master prompt 和 next_route 承接，并在本拍完成后自动进入下一拍 queued 的低风险可逆任务。若 next_route / round_goal 已经给出清楚、低风险、可逆且已授权的下一步，默认自动进入下一拍，不要写“下次你说继续时再推进”；若受回合、工具或权限边界限制必须暂停，只记录 next_route 和暂停原因。若本地项目处在真实外部输入门，先做硬边界矛盾修复、提交摩擦降低、非扩张验证或精确 operator handoff 等剩余可自动小拍；只有这些都不可用时才暂停，并给出具体文件、字段、env var 和命令。工具、子代理/线程职责和 goal 生命周期采用事件触发优先的复查；3 轮只是兜底上限，无触发时只写 lightweight keep。若临时子代理、并行检查或只读审核对本轮有明显收益且无外部副作用，自动启用可用拓扑；独立评审每轮必须使用清上下文/事实账本/只读审核线程，否则只能标为同 session diagnostic self-review。每拍必须通过 Beat Router 收口并执行非终止路由；除 INTERRUPT_FOR_INPUT 或 STOP_COMPLETE 外，不允许停在等待用户继续。
```

## Execution Bridge

- User confirmation status:
- First round_goal after confirmation:
- First Loop:
- First verification:
- First next_route:

## Round Prompt Rehydration

Use this section at the start of each continuous round, Plan-mode continuation, or `next_route` handoff.

- round_index:
- master_prompt_location:
- active_goal_summary:
- codex_goal_lifecycle_mode:
- continuous_runtime_activation_status:
- goal_handoff_carrier:
- latest state/current_basis:
- project_nature:
- convergence_status:
- judgment_mode:
- autonomy_level:
- decision_right:
- candidate_frameworks or fixed evidence model:
- inherited master constraints:
- previous-round status:
- new round judgment:
- prompt patch from user details:
- round_execution_prompt:
- plan_alignment_to_master_prompt:
- next_route this prompt should preserve:
- ask_user_needed:
- topology_auto_activation:
- review_context_reset_status:
- downstream_activation_reconciliation:
- residual_auto_beat:
- orchestration_contract:
- beat_router_decision:
- termination_condition:
- rollback_or_recovery_route:

Rules:

- Compress and inherit the confirmed master prompt; do not rewrite it unless the user explicitly changes the main goal.
- Treat user detail changes as prompt patches by default.
- Do not put the whole continuous cadence into one long Codex tool Goal; use a per-round narrow goal or protocol_round_goal.
- If continuous cadence is selected and the next route is low-risk and reversible, start the next beat automatically rather than waiting for a user "continue".
- If independent review is selected, reset reviewer context each review beat with a fact ledger or clean reviewer route.
- Generate the Plan and Loop from `round_execution_prompt`, not from the local task alone.
- If the round prompt cannot be reconstructed, route back to state recovery before execution.
