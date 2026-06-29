# 持续优化元项目 Profile 烟测

current_as_of: 2026-06-23
latest_machine_board_before_run: `## 215. 当前机器看版`
target_next_route: `continue_self_optimization_with_meta_project_profile_smoke`

## stage_0

continue_reason: 用户要求把“持续优化协议”本身也作为一个项目治理，并避免无界迭代或低边际收益。

recovery_chain_status: 第 215 节已记录 `capability_discovery_cadence_gate`，本轮不新增 verifier required 字段。

## stage_1

current_basis:

1. 用户计划要求新增轻量 `continuous_optimization_meta_project_profile`。
2. 用户明确要求第一轮先做真实项目烟测，不先改 verifier。
3. 当前协议已有 `capability_discovery_cadence_gate` 和 `anti_protocol_bloat_gate`。

not_current_basis:

1. 不回写 `/Users/chuchenqidawang/Documents/ai 科研`。
2. 不创建或更新 Codex skill，因此不使用 `skill-creator` 实施。
3. 不把单一烟测结果直接当成 required 核心字段。

gap_type:

1. real_cross_project_gap: 持续优化本身缺少低摩擦闭环和停止条件。
2. user_preference: 用户希望“持续优化但不低收益空转”。
3. tool_layer_inertia: 不能因为恢复链工具可改就继续改工具。

## capability_discovery_cadence_gate

initial_scan:

| surface | considered | selected_now | rejected_now | backlog |
| --- | --- | --- | --- | --- |
| local_skills | `superpowers:executing-plans`, `superpowers:verification-before-completion`, `skill-creator` | executing-plans, verification-before-completion | `skill-creator`：本轮不是创建或更新 reusable skill | `skill-creator` 可在未来创建专用 Codex skill 时使用 |
| callable_tools | `apply_patch`, `rg`, `python3 tools/test_verify_governance_recovery.py`, `python3 tools/verify_governance_recovery.py`, `curl` | 本地编辑、结构扫描、恢复链验证、只读来源探测 | 无外部写入工具 | 若后续做网页 UI 验证，可考虑 browser/node_repl |
| deferred_tools | `tool_search` 返回线程/Node REPL 能力 | `tool_search` 用于能力盘点 | 线程工具：用户未请求创建线程；Node REPL：本轮无浏览器自动化需求 | 需要并发审计或 UI 自动化时再启用 |
| plugins_connectors | 无需安装插件或连接器 | none | plugin-creator / skill-installer：不适用本轮 | 后续若用户要求发布 reusable skill/plugin 再评估 |
| external_apis_methods | GitHub Docs、Socrata API 文档、OWID API 文档 | 作为只读 source_url | 会写入外部系统的 API 全部拒绝 | 若下一轮要深测数据刷新，可补只读 API 抽样 |

periodic_reconsideration:

| trigger | last_checked_at_stage | decision |
| --- | --- | --- |
| stage_transition | stage_4 before documentation edits | 仍用本地编辑和只读来源，未启用 subagent |
| before_final_claim | planned after verification | 必须运行结构扫描和恢复链 verifier |

## stage_2

| candidate | value_for_real_projects | user_friction_reduction | overclaim_or_misroute_risk_reduction | verifiability | decision | decision_reason |
| --- | --- | --- | --- | --- | --- | --- |
| 新增 `continuous_optimization_meta_project_profile` | high | high | high | medium | promote_to_protocol | 它压缩引用现有阶段，直接解决持续优化空转和膨胀风险，但不作为 verifier required |
| 新增 `continuous_optimization_roi_gate` required 字段 | medium | low | medium | medium | reject | 现在会增加硬字段和工具负担，违背“先烟测再晋升” |
| 三类真实项目烟测记录 | high | medium | high | high | add_to_experience_library | 烟测细节用于校准 profile，不直接写成新主协议目录 |

## stage_4

selected_main_chain: 建立 profile + 做三类 source-backed smoke test + 更新恢复入口。

rejected_chains:

1. 直接改 verifier required：拒绝。
2. 新增完整“持续优化项目协议”大目录：拒绝。
3. 并行子代理审计：本轮没有用户明确委派，且改动耦合，降级为主代理本地执行。

## stage_7

continue_decision: continue_this_round_then_reassess

stop_condition: 若下一轮真实项目烟测没有暴露新的跨项目失败模式，或候选只能增加协议长度而不能降低误判/摩擦，停止连续优化并只维护 backlog。

## stage_8

### sample_1_software_open_source_delivery

source_url:

1. https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
2. https://docs.github.com/actions/managing-workflow-runs/viewing-workflow-run-history

primary_claim: 开源/软件交付项目不能把 PR、CI 或 release 页面直接外推为部署完成、真实用户采用或生产稳定。

selected_lenses:

1. `software_delivery_state_boundary_guard`
2. `claim_readiness_ladder`
3. `capability_discovery_cadence_gate`

micro_task: 用 GitHub release 与 workflow run 文档填一次最小状态边界：release 文档能支持“有发布机制/发布记录可查”，workflow run 文档能支持“运行状态可查”，但不能证明部署、真实使用或监控承接。

observed_gap: `software_delivery_state_boundary_guard` 已能覆盖本小题；本轮不需要新增 `release_deployment_usage_gate`。

downgrade_rule: 缺同版本部署、真实使用和监控证据时，主张只能停在 source-backed 或 locally verified 的交付状态，不能写 production ready 或 user adopted。

### sample_2_public_service_low_friction_start

source_url:

1. https://dev.socrata.com/foundry/data.cityofnewyork.us/erm2-nwe9
2. https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9

primary_claim: 公共服务类新项目可以低摩擦启动，但不能把公开数据可访问外推为服务改善、受益者满意或治理有效。

selected_lenses:

1. `claim_ladder`
2. `evidence_contract`
3. `stakeholder_context`
4. `public_action_chain`
5. `claim_readiness_ladder`

micro_task: 用 NYC 311 数据源构造一个 10 分钟项目入口：目标是“识别投诉类型和响应时间的分析小题”，不是“证明城市服务已改善”。

observed_gap: 低摩擦入口需要强制写 primary_claim 和 downgrade_rule；否则公共服务项目很容易从数据可得跳到公共成效主张。

downgrade_rule: 公开 API 或数据集只能支持数据分析候选，不能证明 agency workflow、居民受益、政策成效或长期治理结果。

### sample_3_research_data_claim_readiness

source_url:

1. https://docs.owid.io/projects/etl/api/

primary_claim: 研究/数据项目中，图表或 API 可访问只能证明数据入口存在；发表结论、决策建议或复用数据产品还需要字段证据、版本、时效和复现边界。

selected_lenses:

1. `data_artifact_lineage_freshness_guard`
2. `field_evidence_status`
3. `source_role_map`
4. `claim_readiness_ladder`

micro_task: 用 OWID API 文档设计一个最小数据产物 trace：记录 source_url、artifact type、metadata/freshness 待查、field evidence 状态和不能外推边界。

observed_gap: 现有数据产物 guard 足够覆盖本小题；profile 的作用是阻止“看到数据问题就继续加 required 字段”。

downgrade_rule: API 或图表存在只能支持 source-backed data candidate；缺字段证据、版本/刷新时间和复现配方时，不能写成可用于决策或已验证研究结论。

## stage_9

anti_protocol_bloat_gate:

| candidate | trigger_signal | observable_behavior | required_evidence_or_check | route_back_if_failed | user_friction_impact | decision |
| --- | --- | --- | --- | --- | --- | --- |
| `continuous_optimization_meta_project_profile` | 用户要求持续优化也按治理协议收束 | 机器看版可记录候选、烟测、停止条件和晋升边界 | 三类样本字段完整，恢复链验证通过 | 回到 stage_1 区分真实缺口和工具惯性 | 降低用户反复提醒成本 | promote_to_protocol |
| `continuous_optimization_roi_gate` hard field | 想量化 ROI | 新字段和 verifier 都会增加负担 | 目前只有本轮偏好，无跨项目失败证据 | 进入 backlog，等两轮烟测重复出现 | 增加用户和维护摩擦 | reject |
| 三类烟测细节 | 需要验证 profile 是否真能用 | 每个样本有 source_url / claim / lenses / micro_task / gap / downgrade | 文档结构扫描和恢复链验证 | 若样本缺字段，补 smoke doc 不改主协议 | 中等，仅在 docs 中承载 | add_to_experience_library |

verifier_required_allowed: false

experience_library_update: 本轮先保存在 `docs/continuous_optimization_meta_project_smoke_20260623.md`；若后续形成稳定失败模式，再同步经验库索引。

