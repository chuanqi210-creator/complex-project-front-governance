# Terraform/GitOps 期望状态调和回归

current_as_of: 2026-06-22

本轮目的不是把 Terraform、Argo CD、Kubernetes 分别写成主协议目录，而是用它们共同暴露一个跨领域失败模式：声明式系统经常被误表述为“配置存在、plan 可运行、controller 会同步，所以长期安全可收敛”。真实风险恰恰在于 desired state 会被工具忠实执行，错误配置、错误目标、drift、import 身份绑定、destroy/prune/replace、并发写 state 和 operator handoff 都可能把一次成功 apply/sync 变成生产事故。

## 1. 官方来源角色表

| 来源 | 可支持主张 | 不能外推 |
| --- | --- | --- |
| HashiCorp Terraform state: https://developer.hashicorp.com/terraform/language/state | Terraform 通过 state 追踪真实对象与配置实例的关系，并用它决定后续变更 | state 是管理记录，不是业务健康证明；错误绑定会放大误操作 |
| HashiCorp Terraform plan/apply: https://developer.hashicorp.com/terraform/cli/commands/plan 与 https://developer.hashicorp.com/terraform/cli/commands/apply | plan 可预览变更，apply 执行计划；支持“先 diff，再执行”的治理门槛 | plan 是时间点证据，不保证 apply 时外部世界未改变 |
| HashiCorp Terraform locking/backend/import: https://developer.hashicorp.com/terraform/language/state/locking 与 https://developer.hashicorp.com/terraform/language/import | backend/locking 支撑并发 state 写保护；import 支撑既有资源纳入管理 | 锁不防错误配置，import 不证明配置完整正确 |
| Argo CD auto sync: https://argo-cd.readthedocs.io/en/latest/user-guide/auto_sync/ | Git 作为 desired state，sync/self-heal/prune 是显式策略能力 | Synced/Healthy 不等于业务可用；prune/self-heal 会忠实执行错误 desired state |
| Kubernetes controllers: https://kubernetes.io/docs/concepts/architecture/controller/ | controller loop 会把 current state 推近 desired state | 控制循环不等于事务一致、最终稳定或业务正确 |
| OpenAI Agents SDK: https://openai.github.io/openai-agents-python/ | handoff、guardrails、tracing 可作为子代理编排方法来源 | 不能证明当前 Codex 会话可调用这些能力或子代理结果可靠 |
| Anthropic effective agents: https://www.anthropic.com/engineering/building-effective-agents | routing、parallelization、orchestrator-workers、evaluator-optimizer 是可迁移编排模式 | 不能替代本地 skill 硬规则、工具探测和项目验收 |
| LangChain multi-agent docs: https://docs.langchain.com/oss/python/langchain/multi-agent | 主代理协调 subagents/handoffs，说明上下文工程和路由选择的重要性 | 不能证明本项目应采用该框架或需要并行 worker |

## 2. 小题执行证据

micro_task_execution_check:
  task: 用 Terraform/GitOps/Kubernetes 官方资料和两个只读子代理结果，判断现有协议是否足以覆盖 desired state -> observed state -> plan/diff -> apply/reconcile 风险，并用 TDD 把新字段纳入恢复链 verifier。
  actual_input:
    - `/Users/chuchenqidawang/Desktop/复杂项目启动前置治理协议_v3_核心版.md`
    - `/Users/chuchenqidawang/Documents/ai 科研/真实项目压力测试_跨域收束与低摩擦路由表_20260622.md`
    - `/Users/chuchenqidawang/Documents/ai 科研/tools/test_verify_governance_recovery.py`
    - `/Users/chuchenqidawang/Documents/ai 科研/tools/verify_governance_recovery.py`
  red_evidence: 新增 `test_preset_fails_when_desired_state_reconciliation_guard_missing` 后，旧 verifier 对删除 `desired_state_reconciliation_guard` 的 fixture 返回 `failure_count: 0`，测试退出 1。
  green_evidence: 将 `desired_state_reconciliation_guard` 纳入 preset required 后，`python3 tools/test_verify_governance_recovery.py` 输出 `ok`。
  observed_result: 现有 `external_state_write_guard`、`integration_lifecycle_gate`、`transactional_integration_consistency_guard` 和 `deployment_readiness_gate` 只能覆盖相邻问题，缺少声明式调和专门视角。
  pass_fail: pass
  remaining_gap: 未执行真实 `terraform apply`、`argocd sync` 或 Kubernetes 集群操作；本轮只支持 source-backed 方法晋升和恢复链字段覆盖。

## 3. 子代理结果整合

subagent_result_coverage_gate:
  contract_items:
    - 官方资料支持什么、不能支持什么
    - 现有协议字段能覆盖什么、漏掉什么
    - 是否值得晋升为主协议通用 guard
  returned_items:
    - Sartre 完成 Terraform/Argo CD/Kubernetes 官方来源审计，指出 state、plan、locking、import、prune/self-heal、controller loop 的可支撑范围和不可外推边界
    - Kierkegaard 完成现有协议缺口审计，判断值得晋升为抽象 guard，不能扩成具体工具目录
  unverified_items:
    - 未运行真实云账号、集群或 GitOps 控制器
    - 未验证任何特定生产环境配置
  out_of_scope_items:
    - Terraform/Argo/Kubernetes 教程
    - 云资源创建、删除或外部系统写入
  blocking_gaps_after_integration: none_for_protocol_writeback

main_agent_integration_review:
  adopted_claims:
    - 声明式系统需单独检查 desired state、observed state、plan/diff、drift、锁/单写者、破坏性动作、adoption/import、policy gate、rollback/forward fix 和 operator handoff
    - 官方机制只能证明控制面能力，不能证明业务可用、生产安全或长期一致
  rejected_or_downgraded_claims:
    - 不采用“Terraform/Argo/Kubernetes 三套模板”方案，避免主协议目录化
    - 不把子代理建议字段原样照搬，统一收束为 `desired_state_reconciliation_guard`
  final_claim_changed: 从“集成/交易/部署 guard 可能足够”改为“声明式期望状态调和需要独立通用 guard”

subagent_lifecycle_ledger:
  - agent_id: 019eee94-c934-7e12-9130-b6449e3c3455
    role: official_source_read_only_auditor
    previous_status_summary: completed
    close_attempted: true
    close_status: closed
    cleanup_decision: no_longer_needed
  - agent_id: 019eee95-0102-7e62-a433-0023c1c59614
    role: protocol_gap_read_only_auditor
    previous_status_summary: completed
    close_attempted: true
    repeated_close_result: first_attempt_wrong_id_not_found_then_correct_id_closed
    close_status: closed
    cleanup_decision: no_longer_needed

## 4. 晋升后的通用 guard

```yaml
desired_state_reconciliation_guard:
  trigger: declared_configuration_controls_external_resources_or_runtime_state
  desired_state_source:
  observed_state_source:
  target_scope:
  execution_model: plan_apply | controller_loop | manual_sync | auto_sync | other
  plan_or_diff_review:
  drift_detection:
  state_lock_or_concurrency_control:
  destructive_change_gate:
  adoption_or_import_rule:
  rollback_or_forward_fix_plan:
  policy_or_permission_gate:
  operator_handoff:
  downgrade_if_missing:
```

downgrade_rule:

1. 缺 `plan_or_diff_review` 或 `state_lock_or_concurrency_control`：只能写只读审计、source-backed 或 plan-only。
2. 缺 `destructive_change_gate`：不得执行或建议 apply/prune/destroy。
3. 缺 `drift_detection`：不得声称当前环境一致。
4. 缺 `adoption_or_import_rule`：不得声称既有资源可安全纳管。
5. 缺 `rollback_or_forward_fix_plan` 与 `operator_handoff`：不得声称 production ready、长期可收敛或可交接运行。

## 5. Agentic 编排能力补强

本轮也响应用户“通过网上方法、skill、插件提升子代理解决问题能力”的要求，但不新增框架目录。写回主协议的是更通用的 `method_source_role_map`：

```yaml
method_source_role_map:
  - source:
    role: local_hard_rule | official_pattern | framework_pattern | current_runtime_capability
    can_support:
    cannot_support:
    transferred_method:
    non_transfer_boundary:
```

可迁移方法：

1. 本地 Superpowers skill 提供硬约束：独立问题域、控制器准备上下文包、两阶段 review、生命周期清理。
2. OpenAI/Anthropic/LangChain 等在线方法提供模式：handoff、guardrail、tracing、routing、parallelization、orchestrator-workers、subagents/handoffs。
3. 当前 Codex 工具能力必须由 `tool_search` / `spawn_agent` / `wait_agent` / `close_agent` 的实际可用性证明；不能用框架名替代能力探测。
4. 主代理必须整合和裁决：子代理输出只能成为证据泳道或候选判断，不能直接成为最终结论。

## 6. 反膨胀判断

anti_protocol_bloat_gate:
  trigger_signal: 多个声明式真实工程系统共享 desired/observed/diff/reconcile/破坏性收敛风险
  observable_behavior: 项目声称可 apply/sync/self-heal/production ready 时，必须补字段并降级缺证主张
  evidence_or_check: 官方资料、子代理审计、TDD verifier 回归、协议/路由/发布链字段扫描
  route_back_if_failed: 回到 `desired_state_reconciliation_guard` 字段补全或降级 claim readiness
  user_friction_impact: 条件触发，不给普通支教、调研、文档或小型项目增加负担
  promotion_decision: promote_to_main_protocol_as_tool_guard

## 7. Claim readiness

claim_readiness_ladder:
  final_claim: 前置治理协议新增了声明式期望状态调和通用守卫，并增强子代理方法学习来源角色表
  current_level: small_loop_validated
  evidence:
    - 官方来源审计
    - 两个只读子代理结果
    - verifier 红绿回归
    - 协议、路由、发布包、变更清单写回
  cannot_claim:
    - 不证明任何具体 Terraform/Argo/Kubernetes 项目生产安全
    - 不证明真实云资源或集群已验证
    - 不证明未来所有子代理任务都会自动正确拆解
