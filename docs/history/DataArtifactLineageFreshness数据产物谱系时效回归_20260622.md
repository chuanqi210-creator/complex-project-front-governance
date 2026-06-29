# DataArtifactLineageFreshness 数据产物谱系与时效回归

current_as_of: 2026-06-22

## 1. 本轮问题

本轮发现的共性缺口不是“数据工具不够多”，而是协议已有 `numeric_calculation_trace`、`rendered_artifact_freshness`、`source_authority_precedence_trace`、`stateful_data_migration_guard` 和 `deployment_readiness_gate`，但它们没有把一个数据/模型/报表产物从来源快照、输入版本、生成运行、转换逻辑、质量验证、freshness、checksum、复现配方到下游引用绑定成一条链。

这会导致一个常见越级：README、catalog、lineage 图、BI 刷新时间、报表截图、文件修改时间、单次 DAG 成功、模型 registry 版本或 DOI/canonical link 被写成“当前有效、可复现、可用于决策”。

## 2. 来源角色表 source_role_map

| 来源 | source_role | 能支持 | 不能支持 |
| --- | --- | --- | --- |
| W3C PROV overview / PROV-DM：`https://www.w3.org/TR/prov-overview/`、`https://www.w3.org/TR/prov-dm/` | provenance 概念基准 | 数据/事物的产生涉及实体、活动和人员，provenance 可用于评估质量、可靠性和可信度 | 不能证明某个具体项目产物的新鲜度、质量或复现成功 |
| W3C DCAT v3：`https://www.w3.org/TR/vocab-dcat-3/` | catalog/metadata 语义基准 | 数据集、数据服务、目录与分发等元数据描述需要明确 | catalog 存在不能证明底层数据已刷新或产物可决策 |
| OpenLineage Object Model：`https://openlineage.io/docs/spec/object-model/` | job / dataset / run event 谱系模型 | 区分 Job、Dataset、RunEvent、JobEvent、DatasetEvent，并把运行时事件和设计元数据分开 | lineage 事件不能替代质量检查和 freshness 判断 |
| dbt sources：`https://docs.getdbt.com/docs/build/sources` | source freshness 与依赖声明样例 | source 定义可用于 lineage、source tests 和 freshness | dbt 配置存在不能证明当前项目的具体 run、质量结果和下游引用安全 |
| Great Expectations docs：`https://docs.greatexpectations.io/docs/core/introduction/` | 数据质量验证样例 | expectations/checkpoint 一类质量验证可作为质量证据形式 | 不能替代来源快照、复现配方或下游用途限制 |
| MLflow Tracking docs：`https://mlflow.org/docs/latest/ml/tracking/` | 模型/实验运行追踪样例 | run 可记录参数、代码版本、指标、输出文件和 artifacts | registry/model version 不能单独证明训练数据、参数、环境和部署用途完整 |
| DVC docs：`https://doc.dvc.org/start` | 数据/流水线版本化样例 | 可版本化数据、捕获 pipeline 和 metrics、管理实验 | lock 文件或版本号不能替代语义质量检查和当前业务 freshness |
| 本地 Superpowers skills：`dispatching-parallel-agents`、`subagent-driven-development` | 子代理方法来源 | 独立问题域、上下文隔离、契约先行、两阶段 review、主代理集成 | 具体 prompt 模板和框架 API 细节不进入主协议硬规则 |

## 3. 子代理编排

```yaml
subagent_orchestration_pattern_router:
  single_agent_sufficiency_gate: false
  selected_pattern: parallel_read_only_audit_plus_main_agent_integration
  rejected_patterns:
    - parallel_worker: 数据产物 guard 与主协议补丁共享文件，worker 并行写入会增加冲突
    - group_chat: 本轮只需要两个独立审计问题，不需要多方对话
  method_to_work_unit_mapping:
    - role: official_method_auditor
      contract_id: data-lineage-method-source-audit
      output: 可迁移原则、不可迁移框架细节、幻觉风险
    - role: protocol_gap_auditor
      contract_id: data-lineage-local-gap-audit
      output: 现有协议字段覆盖/缺口和最小补丁落点
  context_packet_completeness: pass
  minimum_application_test: verifier red-green + 主协议字段落地 + 长日志恢复链验证
```

```yaml
subagent_result_coverage_gate:
  contract_items:
    - 数据/模型/报表 artifact lineage/freshness 共性方法
    - 本地协议相邻字段缺口
    - 子代理方法学习如何落地为 contract/instruction packet/timeout/integration
  returned_items:
    - W3C / OpenLineage / dbt / MLflow / DVC 方法候选
    - numeric/render/source/stateful/deployment 字段不能替代 artifact guard 的缺口
    - contract_id、subagent_instruction_packet、timeout fallback 和 user proxy 边界建议
  unverified_items:
    - 具体项目中的真实数据质量结果，需要未来项目现场执行
  out_of_scope_items:
    - 某一数据平台的 API 参数和 UI 操作
  main_agent_supplemental_checks:
    - 本地 verifier 红绿回归
    - 发布包、路由表、经验库、长日志恢复链扫描
```

```yaml
subagent_lifecycle_ledger:
  - contract_id: data-lineage-method-source-audit
    agent_id: 019eeed3-5ab0-7732-8a76-37bb135fe3a3
    role: read_only_audit
    status: returned
    integration_decision: partially_accepted
    adopted: 独立问题域、契约先行、上下文工程、两阶段 review、生命周期闭合
    rejected: 框架 API 细节、固定 prompt 原文、供应商 dashboard 细节
  - contract_id: data-lineage-local-gap-audit
    agent_id: 019eeed3-7716-7041-8bd0-a726ba71f23a
    role: read_only_audit
    status: returned
    integration_decision: accepted
    adopted: contract_id、plan_item_id、subagent_instruction_packet、timeout fallback、user proxy 统一边界
```

## 4. 小题执行证据 micro_task_execution_check

```yaml
micro_task_execution_check:
  task: 给 verify_governance_recovery_tool 新增 data_artifact_lineage_freshness_guard 必填字段回归
  red_step:
    command: python3 tools/test_verify_governance_recovery.py
    observation: 旧 verifier 对缺少 data_artifact_lineage_freshness_guard 的夹具返回 failure_count 0，测试失败
  green_step:
    change: 将 data_artifact_lineage_freshness_guard 加入 protocol/route/release/changelog/long_log required 列表
    command: python3 tools/test_verify_governance_recovery.py
    observation: ok
  pass_fail: pass
  remaining_gap: 需要把主协议、路由表、发布包、变更清单、经验库和长日志同步到第 206 节恢复入口
```

## 5. 晋升规则

```yaml
data_artifact_lineage_freshness_guard:
  trigger: data_report_model_table_figure_metric_or_analysis_artifact_supports_claim_or_downstream_decision
  required_chain:
    - artifact_id
    - artifact_type
    - owner
    - status
    - version
    - artifact_path_or_uri
    - source_assets
    - input_versions_or_hashes
    - source_current_as_of
    - produced_at_or_refreshed_at
    - code_ref
    - run_id
    - parameters_ref
    - environment_ref
    - transformation_logic
    - lineage_ref
    - freshness_policy
    - freshness_checked_at
    - freshness_status
    - validation_suite_ref
    - validation_checked_at
    - validation_status
    - artifact_checksum
    - reproduction_recipe_ref
    - downstream_references
    - intended_use
    - known_caveats
    - previous_or_superseded_version
    - downgrade_if_stale
  downgrade_rule: 缺来源快照、输入版本、质量检查、freshness 检查、复现配方或下游用途边界时，停在 source_backed 或 locally_verified，不能写 production_or_public_claim_ready。
```

## 6. 反膨胀闸门 anti_protocol_bloat_gate

```yaml
anti_protocol_bloat_gate:
  trigger_signal: 数据/模型/报表产物被用于支撑主张、下游引用或决策
  observable_behavior: 记录 artifact 身份、来源快照、刷新、转换、质量、复现和下游引用链
  evidence_or_check: verifier required 字段 + 主协议 guard + 路由表执行顺序 + 经验库索引
  route_back_if_failed: 降级主张，补数据产物谱系和 freshness 证据后再提升 readiness
  user_friction_impact: 不要求用户理解数据工程工具名；只要求 AI 在需要时补证据链
  promotion_decision: promote_to_protocol_tool_guard
```

## 7. 失败模式

`data_artifact_lineage_freshness_gap`：数据集、报表、图表、模型、指标、表格或分析输出只凭 README/catalog 描述、lineage 图、BI last refreshed、报表截图、PDF、文件修改时间、单次 DAG 成功、模型 registry 版本或 DOI/canonical link，就被写成当前有效、可复现、可用于决策或可被下游安全引用；缺少 artifact 身份、版本、来源快照、输入 hash、生成/刷新时间、转换逻辑、run/job、代码/参数/环境、质量检查、freshness 检查、checksum、复现配方、下游引用、用途限制和 stale 降级。

## 8. 不迁移细节

不把 dbt YAML、Great Expectations checkpoint、MLflow registry API、OpenLineage facets、DataHub/OpenMetadata UI、Airflow DAG 语法、DVC lock 文件格式或 DataCite relationType 写成主协议硬规则。它们只作为经验库中的方法样例；面对新项目时由 `new_domain_governance_builder` 生成临时领域 trace。
