# Agent Topology Selection 代理拓扑选择回归 2026-06-22

## 1. 本轮问题

用户要求：通过学习网上方法、skill、插件等，提升构建子代理解决问题的能力，并融入前置治理协议。

本轮不是新增一个具体领域 trace，而是修复一个跨项目失败模式：AI 知道很多多代理框架名，也知道“可以调用子代理”，但在真实任务里仍可能不会回答这些操作性问题：

1. 本轮是否真的需要子代理，还是主代理低成本 inline 即可？
2. 如果需要，是 agents_as_tools、handoff、parallel_evidence_lanes、orchestrator_workers、reviewer_loop、group_chat，还是 user_proxy？
3. 谁拥有最终答案，谁可以写文件或外部状态，谁只能只读？
4. 每个子代理拿到哪些上下文，哪些上下文必须排除？
5. 子代理返回后如何逐项核对 contract，而不是只写“已采纳”？

## 2. 来源与角色

| 来源 | 角色 | 可支持 | 不能支持 |
| --- | --- | --- | --- |
| `/Users/chuchenqidawang/.codex/plugins/cache/openai-curated-remote/superpowers/5.1.3/skills/dispatching-parallel-agents/SKILL.md` | local_hard_rule | 独立问题域、并行派工、结果集成和不要把相关问题拆散 | 不能证明当前项目一定需要并行 |
| `/Users/chuchenqidawang/.codex/plugins/cache/openai-curated-remote/superpowers/5.1.3/skills/subagent-driven-development/SKILL.md` | local_hard_rule | fresh subagent per task、spec review 先于 quality review、处理 DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED | 不能替代当前任务的 contract 和验收 |
| `/Users/chuchenqidawang/.codex/plugins/cache/openai-curated-remote/superpowers/5.1.3/skills/writing-plans/SKILL.md` | local_hard_rule | 计划必须自包含、文件边界清楚、步骤可执行 | 不能说明所有任务都应写大计划 |
| `multi_agent_v1.spawn_agent / wait_agent / close_agent` 当前工具表 | current_runtime_capability | 当前会话确有 explorer/worker 子代理能力，且支持 fork_context、agent_type 和 close 生命周期 | 不能证明任意插件或外部系统都可由子代理操作 |
| [OpenAI Agents SDK - Tools](https://openai.github.io/openai-agents-python/tools/) | official_pattern | agents_as_tools：主代理可把专业代理当工具调用并保留编排权 | 不能证明本地 Codex 子代理等同于 SDK Agent |
| [OpenAI Agents SDK - Handoffs](https://openai.github.io/openai-agents-python/handoffs/) | official_pattern | handoff 是控制权转交，需要明确何时交给另一个 agent | 不能把 handoff 当作普通只读审计 |
| [OpenAI Agents SDK - Guardrails](https://openai.github.io/openai-agents-python/guardrails/) | official_pattern | 输入/输出/工具 guardrails 可作为工作流边界和阻断条件 | 不能替代项目自身验收或人工授权 |
| [LangChain Multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent) | framework_pattern | 多代理价值来自工具过多、专门上下文、并行化、上下文工程和 handoffs/subagents 选择 | 不能证明某个 LangChain 模式可直接映射到本地工具 |
| [AutoGen AgentChat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html) 与 [Selector Group Chat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html) | framework_pattern | group chat/team 需要参与者、轮次/选择机制、状态管理和终止条件 | 不能把“多代理讨论”写成已验证结论 |

## 3. 小题执行

micro_task_execution_check:

```yaml
task: 判断本轮协议优化是否应该调用子代理，并实际派一个只读审计 agent。
input:
  local_skills_read:
    - dispatching-parallel-agents
    - subagent-driven-development
    - writing-plans
  online_sources_checked:
    - OpenAI Agents SDK tools / handoffs / guardrails
    - LangChain multi-agent overview
    - AutoGen AgentChat / SelectorGroupChat
  local_protocol_files_scanned:
    - /Users/chuchenqidawang/Desktop/复杂项目启动前置治理协议_v3_核心版.md
    - /Users/chuchenqidawang/Documents/ai 科研/真实项目压力测试_跨域收束与低摩擦路由表_20260622.md
    - /Users/chuchenqidawang/Documents/ai 科研/前置治理协议发布包_20260622.md
execution_evidence:
  subagent_spawned:
    agent_id: 019eeee9-cc47-7012-834a-57e42862a7cc
    role: read_only_auditor
    task_boundary: 审计主协议中子代理、Plan/Goal、阶段流程和动态调度字段的可执行缺口
  red_green_verifier:
    red: 添加缺少 agent_topology_selection_trace 的测试后，旧 verifier 输出 failure_count 0，证明恢复链未覆盖新字段
    green: 将 agent_topology_selection_trace 加入 continuous-self-optimization required 后，测试输出 ok
observed_result:
  - 现有协议已经有 agentic_orchestration_capability_builder 和 subagent_orchestration_pattern_router，但缺少一层明确的代理拓扑选择。
  - 子代理审计指出 subagent_task_contract 仍偏自由文本，缺 dispatch readiness、context_packet、output_contract_items、Plan 状态前后绑定和机器看版索引。
pass_fail: pass
remaining_gap:
  - 后续仍应在真实软件/工程交付任务中检验 worker 写文件、reviewer 审查和 close_agent 生命周期是否稳定。
```

## 4. agent_topology_selection_trace

本轮晋升字段：

```yaml
agent_topology_selection_trace:
  topology_options_considered:
    - topology: single_agent | agents_as_tools | handoff | parallel_evidence_lanes | orchestrator_workers | evaluator_optimizer | reviewer_loop | group_chat | user_proxy
      fit_signal:
      rejected_or_selected_reason:
      context_boundary:
      state_write_boundary:
      final_answer_owner:
      cost_or_latency_risk:
  selected_topology:
  control_plane:
    main_agent_owns_goal_and_final_claim: true
    subagent_can_write_external_state: false
    subagent_can_edit_files: no | listed_files_only | isolated_worktree_only
    human_or_user_proxy_owner:
  context_engineering:
    minimal_context_packet:
    excluded_context:
    allowed_extra_reads:
    exact_questions:
    output_schema:
  guardrails_and_review:
    pre_spawn_guardrails:
    tool_or_side_effect_guard:
    spec_review_required:
    quality_or_risk_review_required:
    coverage_gate_required:
  parallelism_and_state_safety:
    independent_lanes:
    shared_state_conflict:
    dependency_graph:
    batch_id:
  cost_benefit_and_downgrade:
    why_not_single_agent:
    expected_value_overhead_ratio:
    downgrade_to_inline_if:
    stop_or_user_proxy_if:
  source_backed_method_basis:
    local_skill_basis:
    official_or_primary_sources:
    current_runtime_tool_basis:
    non_transfer_boundary:
  minimum_application_test:
  topology_decision:
```

## 5. 三个调用决策回归

| 场景 | 应选拓扑 | 不选的路线 | 可观察证据 |
| --- | --- | --- | --- |
| 单文件小改：修正文档一处措辞或编号 | `single_agent` / `inline_fallback` | 不开子代理；不做 group chat | `no_spawn_reason: main_agent_low_cost_inline` |
| 行业资料核验：多个官方来源互相独立 | `parallel_evidence_lanes` 或 `read_only_audit` | 不让子代理写文件或做最终判断 | 每条 lane 只返回 source_role、可支撑主张、不能外推边界 |
| 多文件交付或协议变更后 QA | `agents_as_tools` + `reviewer_loop`，主代理保留最终答案 | 不用 handoff 把最终判断交出去 | spec review 先于 quality/risk review，返回后跑 verifier 和本地主检查 |

## 6. 规则晋升判断

anti_protocol_bloat_gate:

```yaml
new_rule: agent_topology_selection_trace
trigger_signal:
  - 用户要求学习网上方法、skill、插件或提升子代理能力
  - 任务出现多个可并行证据源、独立 worker、reviewer 或 user proxy
  - 主代理准备调用 spawn_agent / wait_agent / close_agent
observable_behavior:
  - 先选择代理拓扑，再写 subagent_task_contract
  - 记录 final_answer_owner、state_write_boundary、context_boundary、dependency_graph
  - 子代理返回后用 subagent_result_coverage_gate 和 main_agent_integration_review 收口
evidence_or_check:
  - verifier required 新增 agent_topology_selection_trace
  - 小题红绿回归通过
  - 机器看版新增 agent_topology_selection_trace 和 subagent_contract_index
route_back_if_failed:
  - 回到阶段 3 学习 skill/plugin/外部方法
  - 回到阶段 5.2 子代理编排梯
  - 降级为 inline_fallback 或 read_only_audit
user_friction_effect: 降低用户解释“怎么开子代理”的负担，只在登录、授权、付款、敏感上传或外部手动操作时要求用户代理执行。
promotion_decision: promote_to_protocol_core
```

## 7. 降级表述

本轮只能声明：

> 协议已把“学习多代理方法”压实为代理拓扑选择、上下文工程、派工契约、覆盖核对和生命周期清理；并通过一次只读子代理审计与 verifier 红绿回归验证了字段必要性。

不能声明：

> 所有未来子代理任务都会自动成功，或任意外部插件/多代理框架都能在当前 Codex 环境中安全调用。
