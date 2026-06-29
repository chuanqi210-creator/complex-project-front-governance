# 动态阶段控制器真实项目回归：NASA Space Apps 2026

current_as_of: 2026-06-22

## 1. 真实来源

| source_id | source | source_kind | 可支撑范围 |
| --- | --- | --- | --- |
| NASA-SA-main | https://www.spaceappschallenge.org/ | 官方项目主页 | Space Apps 是使用 NASA 及合作航天机构开放数据解决真实挑战的全球 hackathon |
| NASA-SA-local | https://www.spaceappschallenge.org/host-an-event/ | 官方 Local Event 页面 | 2026 Local Lead 需要组织本地活动、招募参与者、支持团队提交、组织评审和社区动员 |

证据等级：E1 official_source。

## 2. 本轮小题

任务：不用新增 NASA / hackathon 具体 trace，测试 `dynamic_stage_controller` 能否对一个真实但容易被过度外推的项目做动态路由。

最终要证明的主张不是“Space Apps 项目能产生真实公共影响”，而是：

> 当前协议能否在真实项目启动时，动态判断治理深度、子代理策略和不能外推边界，并把这个判断留下可恢复证据。

## 3. 动态阶段控制器实测

```yaml
dynamic_stage_controller_regression:
  project: NASA International Space Apps Challenge 2026 Local Event / Challenge participation
  mode_selected: standard
  stage_depth_budget: deep
  route_event: deepen
  why_not_light:
    - 涉及真实组织、公众参与、开放数据、评审和对外展示，不能当作单文件小任务
  why_not_full_continuous:
    - 当前只是协议回归小题，不是接手实际组织 Space Apps 活动
  subagent_decision:
    strategy: read_only_audit
    reason: 官方来源核验和协议缺口审查可并行，只读即可
  selected_lenses:
    - claim_ladder
    - evidence_contract
    - execution_validation
    - transfer_boundary
    - deliverable_storyline
  micro_task_execution_evidence:
    - 官方主页与 Local Event 页面作为 current_basis
    - 完成一次 mode / depth / route_event / subagent_strategy 判断
    - 识别一个可迁移协议缺口：动态决策必须留下 alternatives-considered，而不能只给 selected route
  pass_fail: pass
```

## 4. 暴露的共性失败模式

failure_mode_id: `dynamic_route_arbitrariness_gap`

症状：协议允许 AI 动态选择 `light / standard / deep / continuous` 和 `advance / compress / deepen / spawn_subagent`，但如果只记录最终选择，不记录为什么没有选择其他路线，后续恢复者无法判断这是证据驱动、用户摩擦驱动，还是 AI 随手选的。

这个问题在 Space Apps 样例中很明显：

1. 它可以被误判为 `light`：只是做一次活动方案或报告。
2. 它也可以被误判为 `deep`：因为有 NASA、全球挑战、真实数据和公众参与。
3. 它还可能被误判为 `continuous`：因为有活动组织、长期社区和后续提交。

正确做法不是固定选某一档，而是要求 AI 留下 `routing_decision_log`：选了什么、没选什么、触发信号是什么、用户摩擦影响是什么、何时需要重评。

## 5. 写回建议

不新增 NASA / hackathon trace。只写回一个通用规则：

```yaml
routing_decision_log:
  decision:
  selected:
  alternatives_considered:
  rejected_reason:
  trigger_evidence:
  user_friction_effect:
  revisit_if:
```

写回位置：

1. 主协议 `dynamic_stage_controller` schema。
2. 阶段深度选择规则。
3. 执行前闸门 `must_pass`。
4. 机器看版模板。

最小结论：动态阶段控制器需要“动态选择的证据账本”，否则动态会退化成不可复盘的自由裁量。
