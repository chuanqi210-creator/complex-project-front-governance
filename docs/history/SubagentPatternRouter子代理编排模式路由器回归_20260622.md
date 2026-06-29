# Subagent Pattern Router 子代理编排模式路由器回归

current_as_of: 2026-06-22

## 一、回归目标

本轮检验一个流程级缺口：学习网上 agent/subagent、skill、plugin 或多代理框架方法后，协议已经能记录来源、能力边界和生命周期，但仍可能只写下 routing、handoff、orchestrator-workers、group chat 等模式名，没有证明这些方法如何转成当前项目可执行、可隔离、可验收的 work unit。

本轮不新增外部框架目录；新增的是 `subagent_orchestration_pattern_router`，作为 `agentic_orchestration_capability_builder` 和 `subagent_problem_decomposition_builder` 之间的模式选择层。

## 二、来源角色表

| 来源 | 角色 | 可支持 | 不能支持 |
| --- | --- | --- | --- |
| Codex manual: Agent Skills, Plugins, Subagents | 官方本地手册来源 | skill 是可复用工作流，plugin 可打包 skill/app/MCP，subagents 适合并行、读重、探索、测试和日志分析 | 不能证明当前项目一定需要 spawn，也不能证明子代理输出正确 |
| Superpowers `dispatching-parallel-agents` | 本地硬约束 | 独立问题域、聚焦 prompt、自包含上下文、并行后主代理整合 | 不替代当前项目的任务拆解证据 |
| Superpowers `subagent-driven-development` | 本地硬约束 | 每个任务后做 spec compliance 与 quality review，子代理不能继承混乱上下文 | 不要求所有任务都开 worker |
| Superpowers `writing-skills` | 本地方法论 | 文档/skill 改造也要 RED-GREEN-REFACTOR，先看失败再写规则 | 不证明本轮新增字段自动有效 |
| OpenAI Agents SDK / Codex subagents | 官方方法来源 | handoff、guardrail、tracing、主线程保留决策、子线程隔离噪音 | SDK API 不等于当前 Codex 桌面可调用能力 |
| Anthropic Building Effective Agents | 外部方法来源 | routing、parallelization、orchestrator-workers、evaluator-optimizer 等模式只在任务形态适配时使用 | 不能迁移具体产品性能或模型配置主张 |
| LangChain / LangGraph multi-agent docs | 外部方法来源 | multi-agent 核心是 context engineering、subagents、handoffs、router 和 custom workflow | 不等于当前环境安装了 LangGraph |
| Microsoft AutoGen / Agent Framework docs | 外部方法来源 | sequential、concurrent、handoff、group chat 等模式提示“编排模式需要按任务形态选择” | 不建议把 AutoGen 当新增生产依赖；只迁移模式判断 |

## 三、子代理只读审计

subagent_lifecycle_ledger:
  - agent_id: 019eeeaf-7d55-7122-b71f-3f6139b1ab8c
    role: external_method_auditor
    agent_return_status: done
    close_status: closed
    integration_decision: partially_accepted
    accepted_items:
      - 先判定是否真的需要多代理
      - 主代理保留控制权，子代理处理边界清楚的工作包
      - 编排模式必须按任务形态选择，不能把框架名当方法
      - 上下文工程、trace、guardrail 和人工闸门进入证据链
    rejected_items:
      - 新增大量框架专属字段
      - 把 SDK tracing、LangGraph state graph 或 AutoGen 能力写成当前 Codex 能力
  - agent_id: 019eeeaf-9fc6-7cc3-b13c-f9e9e14cb815
    role: protocol_gap_auditor
    agent_return_status: done
    close_status: closed
    integration_decision: accepted
    accepted_items:
      - 现有 builder 足够作为闸门，但缺少从方法原则到 work unit 的映射证据
      - 新增字段应收敛到 method_to_work_unit_mapping、rejected_decomposition_options、role_selection_reason
    rejected_items:
      - 独立大型 subagent 学习协议
      - 新增复杂评分表或更多角色枚举

## 四、最小小题

micro_task_execution_check:
  task: verifier required field drift regression for subagent_orchestration_pattern_router
  red_evidence:
    command: python3 tools/test_verify_governance_recovery.py
    observed_result: 新增缺字段测试后，旧 verifier 对缺少 subagent_orchestration_pattern_router 的 fixture 返回 failure_count 0，测试退出 1
  green_evidence:
    command: python3 tools/test_verify_governance_recovery.py
    observed_result: 将 subagent_orchestration_pattern_router 纳入 preset required 后输出 ok
  pass_fail: pass
  remaining_gap: 真实项目中仍需按具体任务填写 mapping；本轮只证明恢复链能守住该字段

## 五、写回字段

```yaml
subagent_orchestration_pattern_router:
  single_agent_sufficiency_gate:
    single_agent_sufficient:
    reason:
    cost_conflict_context_risk:
  candidate_patterns:
    - pattern: single_agent | routing | parallel_evidence_lanes | orchestrator_workers | evaluator_optimizer | handoff | reviewer_loop | group_chat | code_or_rule_router
      fit_signal:
      expected_benefit:
      cost_or_conflict_risk:
      context_packet_requirement:
      acceptance_evidence:
  selected_pattern:
  rejected_patterns:
    - pattern:
      rejection_reason:
  method_to_work_unit_mapping:
    - source_method:
      independent_work_unit_ref:
      context_isolation_rule:
      role_selection_reason:
      acceptance_check:
  context_packet_completeness:
    task_full_text:
    relevant_files_or_urls:
    excluded_context:
    forbidden_actions:
    output_contract:
    acceptance_checks:
  minimum_application_test:
  downgrade_if_missing:
```

## 六、反膨胀判断

anti_protocol_bloat_gate:
  trigger_signal: 用户明确要求学习网上方法、skill、插件以提升子代理解决问题能力
  observable_behavior: 先判断单代理是否足够，再选择编排模式，并把方法原则映射为 work unit、角色理由、上下文包和验收项
  evidence_or_check: verifier preset required 覆盖；缺字段必须红灯
  route_back_if_failed: 回到 agentic_orchestration_capability_builder 和 subagent_problem_decomposition_builder，补 mapping 或降级为方法候选
  user_friction_impact: 对用户仍保持低摩擦；字段由 AI 在治理文件中填写
  decision: promote_as_tool_router

## 七、失败模式

agent_failure_mode:
  id: subagent_pattern_name_drop_gap
  description: 学习网上 agent/subagent 方法时只记录模式名，没有说明为什么选择或拒绝某种编排，也没有把原则落到可独立验收的 work unit。
  correction: 使用 subagent_orchestration_pattern_router，并在机器看版与恢复链中保留 selected_pattern、rejected_patterns、method_to_work_unit_mapping、role_selection_reason、context_packet_completeness 和 minimum_application_test。

## 八、主张成熟度

claim_readiness_ladder:
  final_claim: 协议已能强制记录“外部子代理编排方法如何转成当前任务的 work unit 映射”
  current_level: small_loop_validated
  evidence_required_for_next_level: 在真实工程、社会实践和研究数据项目各运行一次模式路由器，并比较是否减少返工或上下文污染
  downgrade_rule: 若没有 mapping 或小题，只能写 source_backed_method_candidate
