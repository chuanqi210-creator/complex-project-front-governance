# 持续优化元项目治理 Profile

current_as_of: 2026-06-23

## 定位

`continuous_optimization_meta_project_profile` 是把现有前置治理协议压缩应用到“持续优化协议本身”的运行形态。它不是新的大目录，也不是 verifier required 字段；它只回答本轮为什么继续、选哪个优化点、证据来自哪里、是否会让协议膨胀、何时停止。

## 阶段映射

| 现有阶段 | 元项目压缩用法 |
| --- | --- |
| iteration_quality_bar | 每轮进入、执行、退出的验收标准；不通过就 stop、ask_user 或 backlog |
| stage_0 | 恢复最新机器看版，确认继续优化理由和恢复链状态 |
| stage_1 | 登记 current_basis / not_current_basis，区分真实跨项目缺口、用户偏好、工具层惯性 |
| stage_2 | 列 2-3 个候选优化点，按真实项目价值、用户摩擦下降、误判风险降低、可验证性排序 |
| stage_4 | 只收束一个最高杠杆主链，其余进入 backlog 或经验库 |
| stage_7 | 用现有评分体系决定继续、停止或只入 backlog |
| stage_8 | 跑一个 5-30 分钟真实小题或恢复链小题 |
| stage_9 | 通过 anti_protocol_bloat_gate 后才允许改主协议 |

## 晋升规则

| 观察结果 | 处理 |
| --- | --- |
| 单一案例细节 | `add_to_experience_library` |
| 用户偏好但非跨项目失败模式 | `backlog` 或轻量 profile 说明 |
| 两个以上真实项目暴露同类失败模式 | 可考虑 `promote_to_protocol` |
| 能被 verifier 稳定结构化检查 | 才考虑进入 required 核心字段 |
| 只增加复杂度、不能降低误判或摩擦 | `reject` |

## 默认停止条件

连续 2 轮真实项目烟测没有暴露新的跨项目失败模式，或候选优化只能增加复杂度但不能降低误判、摩擦或恢复链风险时，停止连续优化；后续只保留 backlog，不继续加字段。

## 触发式续跑

默认不自动开启下一轮。只有出现以下触发信号，才允许从最新机器看版进入新一轮：

1. 用户明确指定继续某一轮或给出新优化主题。
2. 新真实项目暴露新的跨项目失败模式。
3. 恢复链、单测或综合 verifier 出现红灯。
4. 已有 backlog 被证明能降低误判、用户摩擦或恢复链风险。

无触发时，下一步只能写 `backlog` 或 `stop`，不得追加新机器看版。触发成立时，新一轮必须先完成 `capability_discovery_cadence_gate` 和 `iteration_quality_bar.entry_gate`，再决定是否进入执行。

## Iteration Quality Bar

每轮连续优化必须先填写本标准，再决定是否进入下一轮：

| gate | 必填项 | 不通过时 |
| --- | --- | --- |
| entry_gate | latest_machine_board、recovery_chain_failure_count、2-3 个候选、候选最低评分、capability_discovery_checked、proceed_decision | `stop`、`ask_user` 或 `backlog` |
| execution_gate | selected_candidate、one_main_chain_only、micro_task_or_noop_evidence、concrete_artifact_or_record_ref、source_url_present、primary_claim_bounded、state_or_field_evidence_status、downgrade_rule_present、claim_readiness_boundary、promotion_recommendation_present、user_friction_effect_stated、anti_protocol_bloat_decisions | 降级为 `source_backed_candidate`，不得 closed |
| exit_gate | files_synced、verification_commands、next_round_decision、may_start_next_round | 不得进入下一轮 |

最低小题质量：

1. 真实小题必须绑定具体对象，例如 issue / PR / release / package、官方数据集/API 记录、项目公告或交付物；只引用概念文档时必须写 no-op 或降级理由。
2. `primary_claim` 必须写成当前证据能支持的边界化主张。
3. 至少列出一个 `direct_observed` 状态或字段，以及一个 `unknown_or_not_verified` 状态或字段。
4. `downgrade_rule` 必须写明不能外推到什么层级，并给出 `claim_readiness_boundary`。
5. `promotion_recommendation` 只能是 `promote_to_protocol`、`add_to_experience_library`、`reject` 或 `backlog`。
6. `user_friction_effect` 必须说明该轮是否真正降低用户负担；若只是增加字段，不得进入下一轮。

## 能力发现节奏

本 profile 仍受 `capability_discovery_cadence_gate` 约束：

1. 启动时扫描 local_skills、callable_tools、deferred_tools、plugins_connectors、external_apis_methods。
2. 阶段切换、阻塞、验证失败、外部写入或最终主张前复盘是否需要新能力。
3. `skill-creator` 只在目标是创建或更新可复用 Codex skill 时选用；本轮只是项目协议整理，因此应记录为 rejected/backlog。
