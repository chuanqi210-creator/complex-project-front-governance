# 数据库/数据结构迁移零停机与回滚边界回归

current_as_of: 2026-06-22

本轮目的不是新增 Rails、Django、PostgreSQL、GitLab 或 MySQL 工具目录，而是抽取一个跨软件工程项目的共性治理问题：数据库 schema、索引/约束、字段重命名、类型变更、数据回填和数据模型重构，会同时影响持久状态和线上读写路径。一次 migration 文件存在、测试库通过或 ORM 能生成 SQL，不能证明线上零停机、可回滚或数据一致。

## 1. 来源角色表

| 来源 | 可支持主张 | 不可外推 |
| --- | --- | --- |
| GitLab zero-downtime migrations: https://docs.gitlab.com/development/database/avoiding_downtime_in_migrations/ | 多发布 expand/contract、字段删除/重命名前后的代码兼容、post-deployment migration 与大表回填边界 | 不能证明所有项目都必须采用 GitLab 的具体 release 数量或 helper |
| GitLab batched background migrations: https://docs.gitlab.com/development/database/batched_background_migrations/ | 大表数据迁移需要批处理、幂等、可暂停、可重试和健康信号节流 | 不能把 batched background migration 当作所有 DDL 的通用方案 |
| GitLab database indexes: https://docs.gitlab.com/development/database/adding_database_indexes/ | 索引、唯一约束、并发创建、post-deploy migration 与长时间操作的风险 | 不能外推到所有数据库，尤其不能替代数据库官方锁语义 |
| PostgreSQL ALTER TABLE / CREATE INDEX: https://www.postgresql.org/docs/current/sql-altertable.html 与 https://www.postgresql.org/docs/current/sql-createindex.html | DDL 锁级别、ACCESS EXCLUSIVE、NOT VALID/VALIDATE CONSTRAINT、CREATE INDEX CONCURRENTLY、标准索引构建阻塞写入等语义 | 只证明 PostgreSQL 边界，不能外推到 MySQL、SQLite 或 ORM 抽象 |
| Rails Active Record migrations: https://guides.rubyonrails.org/active_record_migrations.html | reversible/irreversible migration、DDL transaction、数据迁移回滚复杂度 | Rails 指南不是完整生产零停机手册，缺少具体流量和锁策略 |
| Django migrations: https://docs.djangoproject.com/en/6.0/howto/writing-migrations/ 与 https://docs.djangoproject.com/en/6.0/ref/migration-operations/ | nullable/backfill/enforce 拆步、非原子大表迁移、migration state 与真实 DB 不一致的风险 | 主要是 Django ORM 风险模型，不能直接外推到其他框架 |
| Stripe online migrations: https://stripe.com/blog/online-migrations | dual-write、backfill、dual-read verification、逐步切换读写、最后清理旧路径 | 单个工程案例，不能证明所有场景都适合双写 |
| GitHub gh-ost: https://github.com/github/gh-ost 与 https://github.blog/news-insights/company-news/gh-ost-github-s-online-migration-tool-for-mysql/ | ghost table、binlog apply、throttle、pause、controlled cutover、auditing 等在线迁移工具思想 | MySQL/InnoDB/复制拓扑经验，不能外推到 PostgreSQL |

## 2. 小题执行证据

micro_task_execution_check:
  task: 判断现有协议是否足以覆盖数据库/数据结构迁移的零停机发布与回滚边界，并用 TDD 把新字段纳入恢复链 verifier。
  actual_input:
    - `/Users/chuchenqidawang/Desktop/复杂项目启动前置治理协议_v3_核心版.md`
    - `/Users/chuchenqidawang/Documents/ai 科研/真实项目压力测试_跨域收束与低摩擦路由表_20260622.md`
    - `/Users/chuchenqidawang/Documents/ai 科研/tools/test_verify_governance_recovery.py`
    - `/Users/chuchenqidawang/Documents/ai 科研/tools/verify_governance_recovery.py`
  red_evidence: 新增 `test_preset_fails_when_stateful_data_migration_guard_missing` 后，旧 verifier 对删除 `stateful_data_migration_guard` 的 fixture 返回 `failure_count: 0`，测试退出 1。
  green_evidence: 将 `stateful_data_migration_guard` 纳入 preset required 后，`python3 tools/test_verify_governance_recovery.py` 输出 `ok`。
  observed_result: 现有 deployment/integration/transactional/desired-state guards 只能覆盖相邻问题，缺少数据迁移专门视角。
  pass_fail: pass
  remaining_gap: 未执行真实数据库 DDL、回填或生产迁移；本轮只支持 source-backed 方法晋升和恢复链字段覆盖。

## 3. 子代理整合

subagent_result_coverage_gate:
  contract_items:
    - 一手资料中的迁移风险和方法
    - 现有协议覆盖和缺口
    - 是否值得晋升为抽象 guard
  returned_items:
    - Pasteur 完成来源审计，覆盖 GitLab、PostgreSQL、Rails、Django、Stripe、GitHub gh-ost 等资料
    - Carver 完成协议缺口审计，判断现有 guard 不足，建议条件触发的抽象通用 guard
  unverified_items:
    - 未运行真实数据库或迁移工具
    - 未验证任何具体项目的迁移脚本
  out_of_scope_items:
    - Rails/Django/PostgreSQL 教程
    - 生产库写入、外部系统操作或真实迁移执行
  blocking_gaps_after_integration: none_for_protocol_writeback

main_agent_integration_review:
  adopted_claims:
    - 数据/数据库迁移需要单独检查兼容窗口、expand/backfill/cutover/contract、在线 DDL、回填幂等与校验、回滚或前滚边界、观测暂停恢复和 owner runbook
    - 官方/一手资料只能证明方法和风险存在，不能证明具体生产迁移安全
  rejected_or_downgraded_claims:
    - 不采用 `online_data_migration_release_guard` 作为名称，改用更抽象的 `stateful_data_migration_guard`
    - 不复制 GitLab/Rails/PostgreSQL/Django 工具目录
  final_claim_changed: 从“deployment 或 desired-state guard 可能足够”改为“持久状态数据迁移需要独立通用 guard”

subagent_lifecycle_ledger:
  - agent_id: 019eeea3-afa7-7643-9a15-9d4a81b443e4
    role: official_and_engineering_source_read_only_auditor
    previous_status_summary: completed
    close_attempted: true
    close_status: closed
    cleanup_decision: no_longer_needed
  - agent_id: 019eeea3-d66e-7b11-a9e5-f34bb7f79f46
    role: protocol_gap_read_only_auditor
    previous_status_summary: completed
    close_attempted: true
    close_status: closed
    cleanup_decision: no_longer_needed

## 4. 晋升后的通用 guard

```yaml
stateful_data_migration_guard:
  trigger: persistent_data_or_schema_change_affects_live_read_write_paths
  migration_scope:
  expand_contract_or_compatibility_plan:
  old_new_code_read_write_overlap:
  backfill_or_batching_plan:
  lock_timeout_and_online_operation_check:
  constraint_index_validation_plan:
  data_correctness_verification:
  rollback_or_roll_forward_boundary:
  feature_flag_or_release_order:
  observability_and_pause_resume_plan:
  owner_runbook_handoff:
  downgrade_if_missing:
```

downgrade_rule:

1. 缺 `expand_contract_or_compatibility_plan` 或 `old_new_code_read_write_overlap`：不得声称 zero-downtime。
2. 缺 `lock_timeout_and_online_operation_check`：只能写 plan-only 或 maintenance-window-required。
3. 缺 `backfill_or_batching_plan` 与 `data_correctness_verification`：不得声称迁移正确或数据一致。
4. 缺 `rollback_or_roll_forward_boundary`：不得声称可安全回滚；只能写 roll-forward-only、backup/restore-required 或需要人工审批。
5. 缺 `observability_and_pause_resume_plan` 与 `owner_runbook_handoff`：不得声称 production ready 或可交接运行。

## 5. 反膨胀判断

anti_protocol_bloat_gate:
  trigger_signal: 多个真实软件工程生态都出现持久状态变更与线上读写兼容风险
  observable_behavior: 项目声称数据库迁移、零停机、可回滚、数据一致、在线索引或回填安全时，必须补字段并降级缺证主张
  evidence_or_check: GitLab/PostgreSQL/Rails/Django/Stripe/GitHub gh-ost 一手资料、两个只读子代理审计、TDD verifier 回归、协议/路由/发布链字段扫描
  route_back_if_failed: 回到 `stateful_data_migration_guard` 字段补全或降级 claim readiness
  user_friction_impact: 条件触发，不给教育、调研、普通文档或非持久状态项目增加负担
  promotion_decision: promote_to_main_protocol_as_tool_guard

## 6. Claim readiness

claim_readiness_ladder:
  final_claim: 前置治理协议新增了持久状态数据迁移通用守卫
  current_level: small_loop_validated
  evidence:
    - 官方/一手工程来源审计
    - 两个只读子代理结果
    - verifier 红绿回归
    - 协议、路由、发布包、变更清单写回
  cannot_claim:
    - 不证明任何具体数据库迁移生产安全
    - 不证明真实 DDL、回填或线上流量切换已验证
    - 不证明所有数据库生态使用相同工具或步骤
