# Missing Maps 公共服务证据泳道主张绑定回归 2026-06-22

## 一、本轮真实项目样本

样本：Missing Maps / Humanitarian OpenStreetMap Team / HOT Tasking Manager 这类公共服务与志愿开放地图项目。

来源：

1. Missing Maps 官网：https://www.missingmaps.org/
2. Missing Maps MapSwipe：https://www.missingmaps.org/mapswipe/
3. Missing Maps Field Mapping：https://www.missingmaps.org/field-mapping/
4. HOT Tasking Manager：https://tasks.hotosm.org/
5. HOT Activation Working Group 页面：https://wiki.openstreetmap.org/wiki/Humanitarian_OSM_Team/Working_groups/Activation
6. HOT Data Principles：https://www.hotosm.org/en/data-principles/
7. 本地 Superpowers skill：`dispatching-parallel-agents`

## 二、小题目标

第 186 节已经新增 `parallel_evidence_lane_trace`，解决“根因或最终判断耦合时，仍可并行只读证据泳道”的问题。本轮用公共服务项目检验它是否还有一个缺口：证据泳道虽然拆开了，但如果不绑定主张层级，活动量或制品证据仍可能被误用来证明公共效果。

## 三、事实摘录

```yaml
source_role_map:
  missing_maps_home:
    role: project_overview_and_intended_use_claim
    can_support_claims:
      - Missing Maps 是开放协作的人道制图项目
      - 远程志愿者把卫星影像描绘进 OpenStreetMap
      - 社区志愿者补充本地细节
      - 人道组织和本地社区使用地图来规划减灾和灾害响应
    cannot_support_claims:
      - 某个具体项目已经改善救援效率
      - 某地居民风险实际降低
      - 长期公共影响已经发生
  mapswipe_page:
    role: volunteer_mapping_tool_and_data_workflow
    can_support_claims:
      - MapSwipe 是开源移动和网页应用
      - 志愿者识别基础设施、环境变化或验证地图数据
      - MapSwipe 有多类项目以满足不同制图需求
    cannot_support_claims:
      - 识别结果已经被现场行动采用
      - 志愿者贡献自动等于公共服务效果
  field_mapping_page:
    role: local_knowledge_and_risk_boundary_source
    can_support_claims:
      - 本地知识用于补充街道名、地标、卫生设施、社区特定地点
      - 现场制图需要考虑隐私、身体安全和社区参与
    cannot_support_claims:
      - 外部团队可以不经本地伙伴直接采集敏感信息
      - 公开最小地图数据必然安全
  tasking_manager_page:
    role: coordination_tool_description
    can_support_claims:
      - Tasking Manager 是组织志愿者和小组在 OpenStreetMap 上制图的工具
      - 它服务于人道行动协作制图
    cannot_support_claims:
      - 某个 task 完成即证明人道响应成功
  hot_activation_working_group:
    role: activation_process_and_humanitarian_stakeholder_context
    can_support_claims:
      - HOT 灾害制图有工作组、流程、工具和协调语境
      - activation 需要连接人道利益相关方，使数据更有用、更易使用
    cannot_support_claims:
      - 任一地图项目已经完成所有现场使用闭环
```

## 四、并行证据泳道小题

```yaml
micro_task_execution_check:
  task: 为 Missing Maps / HOT 公共服务项目构造证据泳道，并检查每条 lane 是否绑定 claim_ladder
  observed_result:
    - 项目存在和任务组织证据可以独立核验
    - 地图数据贡献与质量证据可以独立核验
    - 本地使用、隐私安全、现场效果和长期影响证据需要另一条更强证据链
  exposed_gap: parallel_evidence_lane_trace_without_claim_lane_binding_can_still_overclaim_impact
  pass_fail: pass_after_rule_tightening
```

```yaml
parallel_evidence_lane_trace:
  case_type: public_service_mapping_project
  evidence_lanes:
    - lane_id: activity_and_coordination_lane
      role: read_only_audit
      claim_lane_binding:
        claim_ladder_level: output_process
        can_support_claims:
          - 项目存在
          - 志愿者协同制图流程存在
          - 工具用于组织任务
        cannot_support_claims:
          - 地图数据质量足够
          - 现场组织实际采用
          - 公共效果已经发生
    - lane_id: data_quality_and_local_detail_lane
      role: read_only_audit
      claim_lane_binding:
        claim_ladder_level: quality
        can_support_claims:
          - 有远程影像识别、OSM 绘制、现场本地细节补充等质量路径
          - 隐私、安全和社区参与是必要边界
        cannot_support_claims:
          - 数据已被人道组织有效使用
          - 受益者风险下降
    - lane_id: uptake_outcome_impact_lane
      role: read_only_audit
      claim_lane_binding:
        claim_ladder_level: uptake_outcome_or_impact
        can_support_claims:
          - 仅在有使用者证据、现场反馈、伙伴确认、响应记录或评估材料时支持效果主张
        cannot_support_claims:
          - 不能由 mapathon 数量、任务完成数或地图覆盖面积替代
  shared_final_decision: main_agent_only
  impact_inference_guard: 最终表述按最弱证据泳道降级；没有 uptake/outcome lane 证据时，只能说“为公共服务提供数据基础/潜在支持”，不能说“已经产生公共影响”
```

## 五、子代理生命周期

```yaml
subagent_lifecycle_ledger:
  - contract_id: audit_missing_maps_claim_lane_binding_20260622
    agent_id: 019eee52-461f-7690-b9e4-57f797c9ec3a
    role: read_only_audit
    agent_return_status: timed_out
    summary: 60 秒内未返回，随后关闭
    integration_decision: audit_timeout_non_blocking
    accepted_items: []
    rejected_items: []
    close_status: shutdown_after_close_request
    cleanup_decision: closed_without_result_not_on_critical_path
```

本轮不把超时子代理的结论当作依据；规则来自主代理对官方来源的小题核验和既有协议目标。

## 六、规则晋升判断

```yaml
rule_promotion_mechanism:
  candidate_rule: claim_lane_binding
  promotion_scope: main_protocol_tightening_rule
  evidence:
    - Kubernetes 回归证明同根因问题需要并行证据泳道
    - Missing Maps / HOT 回归证明公共服务项目中证据泳道还必须绑定主张层级
    - Field Mapping 页面显式提示隐私、安全和社区参与边界
  anti_protocol_bloat_gate:
    trigger_signal: 一条 lane 的证据只证明活动/产出/质量，却被用于证明 outcome 或 impact
    observable_behavior: 每条 evidence lane 写明 claim_ladder_level、can_support_claims、cannot_support_claims 和 impact_inference_guard
    check: 缺少 claim_lane_binding 时 verifier preset 红灯
    route_back: 如果最终报告出现公共影响主张但没有 uptake/outcome/impact lane 证据，降级为过程或潜在支持
    user_friction_impact: 不增加用户提问，只提高内部证据绑定质量
  decision: adopt_as_generic_tightening_rule
```

## 七、不能外推

本回归不评价 Missing Maps 或 HOT 某个具体项目的实际效果，不证明任何灾害响应已因地图改善，也不把开放地图、人道制图或公共服务写成主协议新目录。它只证明一条通用方法：证据泳道必须和主张层级绑定；否则并行证据会变成并行过度外推。
