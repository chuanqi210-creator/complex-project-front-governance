# Subagent Method Transfer Matrix 子代理方法迁移矩阵回归

current_as_of: 2026-06-22

## 一、回归目标

本轮回应用户要求：“通过学习网上的方法、skill、插件等，提升自己构建子代理解决问题的能力，并且融入 MD 中”。

本轮不新增具体领域 trace，而是修复一个共性缺口：外部 agent 框架、skill、plugin 名称容易被写成装饰性引用，不能自动变成当前项目里的清晰子代理分工、上下文包、验收证据、review gate、集成裁决和生命周期清理。

最终主张降级边界：

1. 本轮可以主张：主协议已新增 `method_transfer_matrix`、`gate_activation_matrix`、`read_only_audit_subagent_contract`、`capability_resolution_order` 和 `schema_hygiene_gate` 等通用治理子结构。
2. 本轮不能主张：任何外部 agent 框架在当前会话都天然可调用，或任何子代理输出可以替代主代理最终判断。
3. 本轮不能主张：所有复杂项目都应该开启子代理；只有独立、边界清楚、可验收、可集成的工作包才适合拆分。

## 二、来源与角色

| 来源 | source_role | 可迁移方法 | 不能支持的主张 |
| --- | --- | --- | --- |
| 本地 Superpowers `dispatching-parallel-agents` skill | local_hard_rule | 一个独立问题域一个代理；上下文自包含；返回后主代理复核和整合 | 不能证明当前任务一定要并行，也不能替代当前工具能力探测 |
| 本地 Superpowers `subagent-driven-development` skill | local_hard_rule | fresh subagent per task；spec review 先于 quality review；实现子任务要有清晰文件边界 | 不能证明所有文档/研究任务都适合 worker 子代理 |
| 本地 Superpowers `writing-plans` skill | local_hard_rule | 计划必须给零上下文执行者完整任务、文件、命令、预期输出 | 不能替代主代理对用户目标和阶段深度的判断 |
| Anthropic `Building effective agents` | official_pattern | 先判断什么时候不用 agent；workflow 模式可抽象为 routing、parallelization、orchestrator-workers、evaluator-optimizer | 不能证明当前 Codex 会话已有这些工具或适合照搬实现 |
| Anthropic `How we built our multi-agent research system` | official_pattern | lead agent 协调多个专业子代理，适合宽广且可并行的研究证据收集 | 不能把研究型多代理系统外推为所有执行型项目都应多代理 |
| OpenAI Agents SDK `Agent orchestration` | official_pattern | 区分 LLM orchestration 与 code orchestration；handoff 与 agents-as-tools 是不同控制权结构 | 不能证明本地 Codex 的子代理就是 SDK agent，也不能授权外部写入 |
| LangChain `Multi-agent` | framework_pattern | supervisor/tool-calling 与 handoffs；context engineering 是多代理质量关键 | 不能证明框架模式比本项目的低摩擦单代理更合适 |
| Microsoft AutoGen `Selector Group Chat` | framework_pattern | group chat 需要参与者、选择逻辑和终止条件 | 不能在缺终止条件、状态 owner 和冲突处理时启用群聊式代理 |
| 当前 Codex `multi_agent_v1.spawn_agent / wait_agent / close_agent` | current_runtime_capability | 可实际 spawn 只读审计子代理，并通过 wait/close 管生命周期 | 不能证明子代理输出无需主代理覆盖检查 |

来源链接：

1. Anthropic: https://www.anthropic.com/engineering/building-effective-agents
2. Anthropic: https://www.anthropic.com/engineering/multi-agent-research-system
3. OpenAI Agents SDK: https://openai.github.io/openai-agents-python/multi_agent/
4. LangChain: https://docs.langchain.com/oss/python/langchain/multi-agent
5. Microsoft AutoGen: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html

## 三、method_transfer_matrix

| method_source | extracted_principle | solves_failure_mode | fit_signal | reject_signal | generated_work_unit | minimum_application_test | acceptance_evidence | non_transfer_boundary | downgrade_route |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Superpowers parallel agents | 按独立问题域拆分，给每个代理自包含上下文 | subagent_context_dumping_gap | 多个来源、模块或失败模式互相独立 | 同一根因、共享写状态、主代理低成本可完成 | read_only_audit 或 isolated worker | 本轮派 1 个只读审计子代理审协议缺口 | 子代理返回锚点、缺口和建议，主代理部分采纳 | 不适用于未拆清任务或强共享状态 | inline_fallback 或单代理梳理 |
| Superpowers subagent-driven development | worker 后接 spec review 与 quality/risk review | subagent_contract_coverage_gap | 有清晰实现计划、文件边界、验收命令 | 任务是价值判断、用户授权或高风险外部写入 | worker + reviewer_loop | 本轮未开写入 worker；仅迁移 review 顺序规则 | 主协议写入 spec-first review 规则和只读契约 | 不强迫所有文档任务走 worker | reviewer_only 或主代理本地验证 |
| OpenAI orchestration | agents-as-tools 与 handoff 控制权不同 | agent_topology_blind_spot | 需要专家子任务但主代理保留最终答案，或需要明确转交控制权 | 控制权、状态 owner、恢复入口不清 | topology selection trace | 本轮把 route_event / selected_topology / selected_pattern / strategy 区分 | 主协议要求四层语义边界 | SDK 概念不能证明本地工具可调度 | no_spawn_reason + main_agent owns final claim |
| Anthropic effective agents | 先判断不用 agent；用 routing/parallel/orchestrator/evaluator 等模式 | subagent_method_name_drop_gap | 单代理上下文不足、证据源可并行、输出可验收 | 为炫技开代理、没有验收证据 | pattern router | 本轮写入 method_transfer_matrix，要求每个方法有 fit/reject/test | 路由表和主协议均出现 `method_transfer_matrix` | 模式名不能替代项目契约 | method_candidate_only |
| LangChain multi-agent | context engineering 决定子代理质量 | subagent_context_dumping_gap | 子任务可用少量关键文件/链接/问题回答 | 需要完整会话、用户偏好或隐性判断 | controller_prepared_context_packet | 本轮只读审计 prompt 给出明确文件、范围和输出结构 | 子代理返回可集成结构而非泛泛总结 | 框架文档不能替代主代理读 skill | 补上下文后重派或 inline |
| AutoGen selector group chat | 群聊要有选择器、候选、终止条件 | agent_topology_blind_spot | 多角色轮流讨论且有明确终止条件 | 没有状态 owner、终止条件或冲突解决 | group_chat only as rare topology | 本轮拒绝 group_chat，选择 single read_only_audit | 记录 rejected pattern | 群聊不是默认并行化方案 | reviewer_loop 或 parallel_evidence_lanes |
| Codex current tool capability | 能 spawn/wait/close 才可写 available | subagent_capability_overclaim | tool_search 或当前工具表发现 spawn_agent，且已实际调用 | 只有环境列名、工具不可见或需用户代理 | capability_probe + lifecycle_ledger | 本轮实际 spawn 一个 explorer，wait 超时后收到完成通知 | agent_id、返回摘要、后续 close 记录 | 能调用不等于输出正确 | inline_fallback 或 user_proxy_required |

## 四、实际小题

小题：用只读审计子代理检查现有协议、路由表、发布包、变更清单和经验库中关于子代理、skill/plugin、Plan/Goal、动态阶段流程的缺口。

执行证据：

1. 调用 `multi_agent_v1.spawn_agent`，角色为 explorer，要求只读、禁止编辑。
2. 子代理返回：读到主协议 `dynamic_stage_controller`、`subagent_orchestration_ladder`、`subagent_task_contract`、路由表、发布包、变更清单和经验库索引。
3. 子代理指出 8 个缺口：gate 默认全跑与动态深度冲突、route_event/拓扑/策略边界混、只读子代理契约不足、Plan/Goal 混名、capability 解析顺序不清、机器看版 alias 过多、经验库调用方式缺动态前置、YAML/编号格式漂移。
4. 主代理采纳其中通用且低摩擦的部分：`gate_activation_matrix`、四层语义边界、`read_only_audit_subagent_contract`、`capability_resolution_order`、canonical alias 说明、经验库第 0 步、`schema_hygiene_gate`。
5. 主代理未采纳“再新增大量独立顶层 trace”的做法，避免协议继续目录化。

## 五、写回决策

| 写回项 | 写回位置 | 理由 | claim_readiness |
| --- | --- | --- | --- |
| `method_transfer_matrix` | 主协议 5.2、机器看版模板、路由表、经验库 | 防止框架名堆叠，要求外部方法落成 work unit 和最小应用测试 | small_loop_validated |
| `gate_activation_matrix` | 主协议 5.0、机器看版模板、路由表 | 解决“常驻检查默认全跑”与动态阶段深度冲突 | locally_verified |
| `read_only_audit_subagent_contract` | 主协议 5.3、路由表 | 防止只读审计子代理越界编辑、安装、外部写入或最终裁决 | small_loop_validated |
| `capability_resolution_order` | 主协议 5.2、路由表 | 区分 active skill/tool、tool discovery、installable、authorized 和 side effect | locally_verified |
| `schema_hygiene_gate` | 主协议 5.3、路由表扫描要求 | 防止 YAML 缩进、重复编号和 alias 漂移被后续代理复制 | locally_verified |

## 六、剩余边界

1. 本轮只使用了一个只读审计子代理，不证明并行 worker 群在所有项目中可靠。
2. 外部资料均作为方法来源，不作为当前 Codex 工具能力证明。
3. 若后续任务需要安装插件、登录连接器、写 GitHub/课程/账号等外部状态，仍必须先走 `capability_type_and_side_effect_gate` 与 `external_state_write_guard`。
4. 若子代理需要自行 tool discovery，必须由主代理先读必要 skill/plugin 指令并在契约里限定范围。
