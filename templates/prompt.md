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
- 少问我 / 能推进就继续 / 我给目录你自己读
- 独立评审 / 客观审查 / 避免上下文污染
- 外部工具 / 账号 / API / skill
- 只要人看版
```

## Protocol Scan Summary

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

Steering words to preserve:
- 开启 Plan 模式 / 先规划再执行：
- 模型发现型 / 先发散研究框架 / 不要早收敛：
- 证据填充型 / 模型和指标已定：
- 连续节拍 / 总规划别丢 / 每轮 prompt 重水化：
- 少问我 / 能推进就继续 / 我给目录你自己读：
- 独立评审 / 客观审查 / 避免上下文污染：
- 外部工具 / 账号 / API / skill：
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

请先恢复或建立 state/current_basis，再判断 project_nature 和 convergence_status，并逐项判断上述 steering words 是否适用。如果当前界面支持 Plan 模式，请先提醒用户开启 Plan 模式完成协议扫描、项目判断和 prompt/plan 设计，再执行本轮 round_goal；如果不支持，也要先输出计划和 round_execution_prompt，不直接跳到业务执行。每轮结束时留下 next_route；如果启用连续节拍，每拍使用窄 round_goal，连续性由 state、master prompt 和 next_route 承接。工具、子代理/线程职责和 goal 生命周期采用事件触发优先的复查；3 轮只是兜底上限，无触发时只写 lightweight keep。
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
- rollback_or_recovery_route:

Rules:

- Compress and inherit the confirmed master prompt; do not rewrite it unless the user explicitly changes the main goal.
- Treat user detail changes as prompt patches by default.
- Do not put the whole continuous cadence into one long Codex tool Goal; use a per-round narrow goal or protocol_round_goal.
- Generate the Plan and Loop from `round_execution_prompt`, not from the local task alone.
- If the round prompt cannot be reconstructed, route back to state recovery before execution.
