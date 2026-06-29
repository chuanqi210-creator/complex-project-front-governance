# SecurityIncidentResponse 安全事件响应与协调披露回归

current_as_of: 2026-06-22

## 1. 本轮问题

第 202 节的 next_route 要求继续选择真实项目或真实交付流程，验证子代理编排模式路由器能否减少框架名堆叠和无效 spawn。本轮选取“安全漏洞/安全事件/凭证泄露/协调披露”作为敌意样例，因为它跨软件、开源、企业交付、云资源、数据系统和插件/API，且特别容易发生证据越级：

- CTF/writeup 或 PoC 被写成真实系统已被利用。
- scanner alert 或 secret scanning alert 被写成已发生入侵或数据泄露。
- issue/PR 合并被写成漏洞已修复、已部署、已验证。
- advisory 草稿、CVE/GHSA 编号或未审核条目被写成已经公开披露、已通知用户、漏洞事实已被确认。

本轮目标不是新增安全领域目录，而是抽取一个跨领域的生命周期 guard：`security_incident_response_guard`。

## 2. source_role_map

| 来源 | URL | 能支持 | 不能支持 |
| --- | --- | --- | --- |
| NIST SP 800-61 Rev.3 | https://csrc.nist.gov/pubs/sp/800/61/r3/final | 事件响应应纳入 CSF 2.0 的治理、识别、保护、检测、响应和恢复活动；提供 incident response 的准备、检测、响应、恢复、报告和改进框架 | 不能证明某个具体项目已经发生 compromise、完成取证、完成修复或完成通知 |
| CISA Cybersecurity Incident & Vulnerability Response Playbooks | https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks | 事件响应和漏洞响应需要识别、协调、修复、恢复、跟踪缓解；实际流程含准备、检测分析、遏制、清除恢复、事后活动、协调与报告 | 不能直接证明非 FCEB 项目的法定义务，也不能替代具体组织的授权、日志和影响评估 |
| CERT/CC CVD Phases | https://certcc.github.io/CERT-Guide-to-CVD/topics/phases/ | 协调漏洞披露可抽象为 discovery、reporting、validation、prioritization、remediation、public awareness、deployment 等阶段，并涉及 finder/reporter、vendor、coordinator、deployer 等角色 | 不能替代具体平台的 advisory/CVE/GHSA 流程，也不能证明 public awareness 或 deployment 已发生 |
| SSVC | https://riskbasedprioritization.github.io/ssvc/SSVC/ | 漏洞优先级需要按利益相关方语境决策，并明确区分 PoC 与 active exploitation 等利用状态 | 不能直接给出某个漏洞的真实利用证据或组织处置结论 |
| FIRST 多方漏洞协调指南 | https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1 | 多供应商、多上下游、多协调者场景需要清晰角色、联系人、时间线、协调和公开节奏 | 不能替代具体 vendor 的确认、补丁和通知 |
| GitHub Repository Security Advisories | https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories | repository advisory 支持私下讨论、协作者、修复和后续发布；草稿状态与公开发布状态不同 | 不能证明草稿 advisory 已公开、用户已通知或 GHSA/CVE 已完成 |
| GitHub Secret Scanning | https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning | secret scanning alert 可作为凭证泄露线索，后续需验证、吊销、轮换和排查使用 | 不能单独证明凭证仍有效、已被使用、已造成未授权访问或数据外泄 |

## 3. subagent_orchestration_pattern_router

```yaml
subagent_orchestration_pattern_router:
  single_agent_sufficiency_gate:
    single_agent_sufficient: false
    reason: 安全事件响应有官方来源核验和协议缺口审计两个独立工作面；并行只读审计能减少主代理单点漏判。
  selected_pattern: parallel_read_only_evidence_lanes_plus_main_agent_integration
  rejected_patterns:
    - pattern: single_agent_only
      rejection_reason: 官方来源与本地协议缺口可独立核验，单代理容易把来源摘要和规则晋升混在一起。
    - pattern: parallel_worker
      rejection_reason: 文件写入共享且主代理必须承担最终判断，子代理不应并行改协议。
    - pattern: framework_directory
      rejection_reason: 本轮需要抽象 lifecycle guard，不需要新增 CTF/CVE/GitHub/CISA 平台目录。
  method_to_work_unit_mapping:
    - source_method: parallel_evidence_lanes
      independent_work_unit_ref: Maxwell_official_source_audit
      role_selection_reason: read_only_source_auditor
      acceptance_check: 共性阶段、必须证据、不能由线索外推的主张
    - source_method: protocol_gap_review
      independent_work_unit_ref: Huygens_existing_guard_gap_audit
      role_selection_reason: read_only_protocol_auditor
      acceptance_check: 现有 guard 覆盖边界、最小新增字段、应留在经验库的细节
  context_packet_completeness: task_scope_sources_forbidden_actions_output_contract_included
  minimum_application_test: verifier_missing_field_red_green_cycle
  downgrade_if_missing: source_backed_guard_candidate_only
```

## 4. subagent_lifecycle_ledger

```yaml
subagent_lifecycle_ledger:
  - agent_id: 019eeebe-73b7-78a0-85bd-3c0ba318ce07
    role: official_primary_source_auditor
    close_status: returned
    integration_status: adopted_as_source_audit
    adopted_points:
      - NIST Rev.3 采用 CSF 2.0 全流程模型
      - CISA playbooks 强调 identify_coordinate_remediate_recover_track
      - CERT/CC CVD 阶段可迁移为协调披露字段
      - PoC、scanner alert、issue/PR、advisory draft 只能支持有限主张
  - agent_id: 019eeebe-99c7-79d0-a31d-77ef944d24a4
    role: local_protocol_gap_auditor
    close_status: returned
    integration_status: adopted_as_protocol_gap_audit
    adopted_points:
      - 现有 high_risk、external_state_write、deployment 和 security_remediation_trace 只覆盖相邻风险
      - 漏洞/事件/凭证泄露/协调披露生命周期缺少字段级 guard
      - CTF、漏洞类型、具体平台流程和法规长模板应留在经验库
```

## 5. micro_task_execution_check

```yaml
micro_task_execution_check:
  task: verifier required field drift regression for security_incident_response_guard
  red_evidence:
    command: python3 tools/test_verify_governance_recovery.py
    observed_result: 新增缺字段测试后旧 verifier 对 missing security_incident_response_guard 的 fixture 返回 failure_count: 0，测试退出 1。
  green_evidence:
    command: python3 tools/test_verify_governance_recovery.py
    observed_result: 将 security_incident_response_guard 纳入 continuous-self-optimization preset required 后，测试输出 ok。
  pass_fail: pass
  remaining_gap: 只验证恢复链能发现字段缺失；真实 incident 的技术判断仍需在具体项目中由日志、授权、资产和影响证据支撑。
```

## 6. security_incident_response_guard

```yaml
security_incident_response_guard:
  trigger: vulnerability_incident_secret_leak_advisory_scanner_alert_or_security_fix_claim
  source_type: incident | vulnerability | secret_leak | advisory | scanner_alert | poc | ctf | issue_pr
  claim_type: exploitability | active_exploitation | compromise | data_access | data_exfiltration | affected_version | fixed_version | remediation_verified
  evidence_level: lead | plausible | validated | confirmed | published
  affected_asset_scope:
    required_before: 影响版本、资产、账号、系统、用户或数据范围主张
  authorization_and_contact_boundary:
    required_before: 探测、复现、披露、通知、外部报告或协调动作
  severity_or_priority_basis:
    examples: CVSS_or_SSVC_or_asset_criticality_or_active_exploitation_or_business_impact
  exploitation_or_compromise_state:
    allowed_values: none | poc | active | compromise_confirmed | unknown
    downgrade_rule: PoC 不能外推为 active exploitation；扫描告警不能外推为 compromise。
  containment_or_mitigation_status:
    required_before: 事件已控制、风险已降低或可恢复主张
  credential_rotation_or_secret_revocation:
    required_before: 凭证泄露已处置或未造成访问风险主张
  impact_scope:
    required_before: 用户、数据、业务、权限、完整性或可用性影响主张
  remediation_verification:
    required_before: 修复已部署、已验证或漏洞已关闭主张
  coordination_or_disclosure_state:
    allowed_values: unreported | reported | acknowledged | coordinating | embargoed | published
  notification_requirements:
    required_before: 用户、客户、监管、社区或公众已通知主张
  monitoring_and_recurrence_check:
    required_before: 无新迹象、风险已恢复或长期受控主张
  post_incident_review_owner:
    required_before: 经验教训、根因改进、长期控制已承接主张
  cannot_conclude:
    must_list: 当前证据不能支持的更强主张
  downgrade_if_missing: lead_only_exploitability_candidate_patch_unverified_disclosure_not_ready_or_triage_only
```

## 7. anti_protocol_bloat_gate

```yaml
anti_protocol_bloat_gate:
  trigger_signal: 安全漏洞、事件、凭证泄露、PoC、扫描告警、issue/PR、advisory 或协调披露主张反复跨项目出现。
  observable_behavior: 协议必须要求证据层级、资产范围、授权联系人、遏制修复、凭证轮换、影响范围、披露通知和复盘 owner。
  evidence_or_check: 官方来源 + 两名只读子代理 + verifier 缺字段红绿回归。
  route_back_if_failed: 降级为 source-backed guard candidate；只写入经验库，不晋升主协议。
  user_friction_impact: 用户不用知道 CVD/SSVC/GHSA 细节；只要项目触发安全主张，AI 自动启用最小字段。
  promotion_decision: promote_minimal_guard_not_platform_directory
```

## 8. claim_readiness_ladder

```yaml
claim_readiness_ladder:
  source_backed:
    allowed_claim: 官方框架显示安全事件/漏洞响应需要生命周期管理和协调披露证据。
  locally_verified:
    allowed_claim: 本地协议、路由表、发布包、变更清单和 verifier 均包含 security_incident_response_guard。
  small_loop_validated:
    allowed_claim: 缺 guard 的 fixture 会触发 verifier 失败，恢复链不会误报通过。
  cannot_claim:
    - 本协议能判断任何具体漏洞是否已被利用
    - 某个扫描告警等同于真实入侵
    - 某个 PR 合并等同于修复已部署验证
    - advisory 草稿等同于公开披露和用户通知完成
```

## 9. 新增失败模式

`security_incident_response_gap`：CTF/writeup、PoC、扫描告警、secret scanning alert、issue/PR、advisory 草稿、CVE/GHSA 编号或补丁合并被直接写成真实系统已入侵、数据已外泄、漏洞已验证修复、用户已通知或披露已完成；缺少受影响资产、授权联系人、事件证据链、分级依据、遏制缓解、凭证吊销轮换、影响范围、修复部署验证、协调披露、通知要求、监控复发和复盘 owner。

## 10. 本轮不能迁移的细节

- 不把 CTF、靶场、flag、writeup 或具体漏洞类型写入主协议。
- 不把 CVSS、SSVC、EPSS、KEV、CVE、GHSA 的具体平台流程写成总规则字段；需要时在具体项目临时 trace 中展开。
- 不把 CISA 的 FCEB 报告时限外推为所有组织的法定义务。
- 不把 GitHub 的 advisory / secret scanning 文档外推到所有平台；只迁移“草稿不等于公开、告警不等于已利用、凭证泄露需要吊销轮换和使用排查”的共性方法。
