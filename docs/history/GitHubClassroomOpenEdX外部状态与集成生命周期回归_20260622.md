# GitHub Classroom x Open edX 外部状态与集成生命周期回归

current_as_of: 2026-06-22

## 一、回归目标

第 192 节已经新增 `capability_type_and_side_effect_gate`、`claim_readiness_ladder` 和 `deployment_readiness_gate`。本轮用 GitHub Classroom + Open edX / LTI 1.3 / AGS 这个真实教育工程集成小题检验两个更细的共性缺口：

1. 只写 `external_write` 不足以管住外部写入，必须知道写向哪里、要什么权限、涉及什么敏感数据、子代理能不能碰连接器。
2. 两个产品各自支持同一标准，不能相加得出“组合已可用”；还必须检查端到端证据和维护/退役生命周期信号。

## 二、来源与角色

```yaml
source_role_map:
  - source_name: GitHub Docs - Register an LMS with GitHub Classroom
    source_url_or_path: https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/register-a-learning-management-system-with-github-classroom
    source_role: github_classroom_official_lti_feature_and_verified_lms_scope
    can_support_claims:
      - GitHub Classroom 官方文档说明支持 LTI 1.3 / LTI Advantage
      - 官方列出已测试或验证的 LMS 范围
    cannot_support_claims:
      - 不能证明 Open edX 这一具体组合已经端到端可用
  - source_name: Open edX LTI Advantage features
    source_url_or_path: https://docs.openedx.org/en/latest/educators/how-tos/course_development/exercise_tools/use_lti_advantage_features.html
    source_role: openedx_platform_lti_advantage_and_ags_feature_reference
    can_support_claims:
      - Open edX 平台侧可启用 LTI Advantage / AGS 等能力
    cannot_support_claims:
      - 不能证明 GitHub Classroom 与 Open edX 的特定组合已成功上线
  - source_name: 1EdTech LTI AGS
    source_url_or_path: https://www.imsglobal.org/spec/lti-ags/v2p0
    source_role: standard_capability_boundary
    can_support_claims:
      - AGS 标准涉及 gradebook column、score、result 等成绩服务边界
    cannot_support_claims:
      - 不能证明任意两个实现之间互通
  - source_name: GitHub Classroom official announcement
    source_url_or_path: https://github.com/orgs/community/discussions/196615
    source_role: product_lifecycle_signal
    can_support_claims:
      - GitHub Classroom 存在维护、迁移或退役类生命周期信号
    cannot_support_claims:
      - 不能单独证明 Open edX 技术链路失败
  - source_name: GitHub Community Open edX discussion
    source_url_or_path: https://github.com/orgs/community/discussions/194212
    source_role: issue_report_or_unresolved_user_report
    can_support_claims:
      - 有用户报告 GitHub Classroom + Open edX LTI 1.3 组合遇到阻断问题
    cannot_support_claims:
      - 不能证明官方根因、普遍故障率或修复状态
  - source_name: Open edX Discuss GitHub Classroom integration question
    source_url_or_path: https://discuss.openedx.org/t/integration-between-github-classroom-actions-and-openedx/15649
    source_role: community_request_signal
    can_support_claims:
      - Open edX 社区存在把 GitHub Classroom / Actions 成绩接入 Open edX 的需求
    cannot_support_claims:
      - 不能证明已有成熟生产方案
```

## 三、小题执行

```yaml
micro_task_execution_check:
  task: 用 GitHub Classroom + Open edX / LTI 1.3 / AGS 真实集成场景检验外部状态写入与集成生命周期闸门
  red_tests:
    - test_name: test_preset_fails_when_external_state_write_guard_missing
      observed_result: 旧 verifier 对缺少 external_state_write_guard 的恢复链 fixture 返回 failure_count 0
    - test_name: test_preset_fails_when_integration_lifecycle_gate_missing
      observed_result: 旧 verifier 对缺少 integration_lifecycle_gate 的恢复链 fixture 返回 failure_count 0
  green_test:
    command: python3 tools/test_verify_governance_recovery.py
    observed_result: ok
  pass_fail: pass
```

## 四、子代理只读审计

```yaml
subagents:
  lifecycle_ledger:
    - role: source_and_claim_readiness_auditor
      agent_id: 019eee76-de5d-7582-8051-c71446c8bd46
      return_status: done
      accepted_items:
        - 单边 LTI/LTI Advantage/AGS 能力不能证明组合可用
        - maintenance / sunset / deprecation / new-user freeze 等生命周期信号应阻断生产主张
        - GitHub Classroom + Open edX 目前只能形成 source_backed_compatibility_candidate
      integration_decision: adopted_as_integration_lifecycle_gate
    - role: side_effect_boundary_auditor
      agent_id: 019eee77-00cc-7501-a337-de20248ec025
      return_status: done
      accepted_items:
        - permission_scope_requested
        - external_state_target
        - sensitive_data_class
        - subagent_capability_boundary
      integration_decision: adopted_as_external_state_write_guard
```

## 五、外部状态写入守卫

```yaml
external_state_write_guard:
  trigger: capability_may_write_external_state_or_access_sensitive_course_data
  permission_scope_requested:
    options:
      - none
      - local_only
      - repo_read
      - repo_write
      - classroom_admin
      - lms_course_read
      - lms_course_write
      - gradebook_read
      - gradebook_write
      - roster_read
      - account_admin
  external_state_target:
    options:
      - none
      - github_repo
      - github_classroom
      - lms_course
      - lms_lti_registration
      - lms_gradebook
      - lms_roster
      - user_account
      - public_publication
  sensitive_data_class:
    options:
      - none
      - public_docs
      - course_config
      - student_identity
      - student_submission
      - roster
      - grades
      - credentials
      - security_keys
  subagent_capability_boundary:
    options:
      - read_only_no_tools
      - read_only_local_tools
      - web_source_only
      - connector_read_only
      - no_plugin_or_connector
      - explicit_user_authorization_required
  required_before_action:
    - explicit_user_authorization
    - sandbox_or_dry_run_evidence
    - rollback_or_reversal_plan
  downgrade_if_missing: only_read_only_analysis_or_manual_action_required
```

## 六、集成生命周期门

```yaml
integration_lifecycle_gate:
  trigger: claim_says_two_or_more_systems_can_integrate_interoperate_or_run_in_production
  component_capabilities:
    - GitHub Classroom supports LTI 1.3 / LTI Advantage according to official docs
    - Open edX supports LTI Advantage / AGS according to official docs and certification references
  composition_rule:
    single_component_capability_plus_single_component_capability: source_backed_compatibility_candidate_only
    required_for_locally_verified:
      - same_version
      - same_deployment
      - same_critical_flow
      - end_to_end_evidence
    required_for_pilot_ready:
      - small_real_user_or_course_context
      - permission_privacy_boundary
      - failure_reversal_path
      - support_owner
    production_blockers:
      - maintenance_mode
      - sunset
      - deprecation
      - new_user_freeze
      - partner_transition
      - retirement_or_data_deletion_date
      - unsupported_product_pair
  readiness_level_after_gate: source_backed_compatibility_candidate
  downgrade_rule: do_not_claim_pilot_ready_or_production_ready_without_end_to_end_and_lifecycle_evidence
```

## 七、规则晋升

```yaml
promotion_decision:
  promoted_to_protocol:
    - external_state_write_guard
    - integration_lifecycle_gate
  promoted_failure_modes:
    - external_state_write_blind_spot
    - component_capability_composition_gap
  non_transfer_boundary:
    - GitHub Classroom / Open edX 只是本轮敌意样例，不进入主协议场景目录
    - 具体 LTI 配置参数不写入主协议
  claim_readiness_ladder:
    final_claim: 协议现能区分外部写入风险与集成生命周期降级
    current_level: small_loop_validated
    evidence_required_for_next_level: 在另一个非教育集成项目中复用该 gate 并验证是否减少越权操作或越级生产主张
```
