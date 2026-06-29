# Subagent / Skill / Plugin 方法应用回归

current_as_of: 2026-06-22

## 一、回归目标

用户提出：可以通过学习网上的方法、skill、插件等，提升构建子代理解决问题的能力，并融入主协议。

本轮不扩展具体项目模板，而是检验一个共性失败：AI 学了外部 agent 方法、本地 skill 或插件后，是否真的能转化为当前项目可执行、可验证、可恢复的子代理编排能力。

## 二、来源与角色

```yaml
source_role_map:
  - source_name: OpenAI Codex Agent Skills
    source_url_or_path: https://developers.openai.com/codex/skills
    source_role: skill_authoring_and_progressive_disclosure_reference
    can_support_claims:
      - skill 是可复用工作流的指令/资源/脚本包
      - Codex 选择 skill 后需要读取完整 SKILL.md
    cannot_support_claims:
      - 不能证明某个具体项目已经因为 skill 而变好
  - source_name: OpenAI Codex Subagents
    source_url_or_path: https://developers.openai.com/codex/subagents
    source_role: codex_subagent_capability_reference
    can_support_claims:
      - Codex 支持 subagent / custom agent 这类能力形态
    cannot_support_claims:
      - 不能替代本地工具可用性探测和生命周期清理
  - source_name: OpenAI Agents SDK agent orchestration
    source_url_or_path: https://openai.github.io/openai-agents-python/multi_agent/
    source_role: orchestration_pattern_reference
    can_support_claims:
      - agent 编排可以通过 LLM、代码、handoff、agents-as-tools 等模式组织
    cannot_support_claims:
      - 不能直接证明 Codex 当前线程应该调用哪些子代理
  - source_name: LangChain multi-agent documentation
    source_url_or_path: https://docs.langchain.com/oss/python/langchain/multi-agent
    source_role: multi_agent_pattern_and_context_management_reference
    can_support_claims:
      - 多 agent 常见模式包括 handoffs、supervisor/tool-calling、skills/on-demand context
      - 上下文管理是多 agent 系统的重要设计问题
    cannot_support_claims:
      - 不能替代当前协议的证据矩阵和主代理裁决
  - source_name: Anthropic multi-agent research system
    source_url_or_path: https://www.anthropic.com/engineering/built-multi-agent-research-system
    source_role: empirical_multi_agent_research_engineering_case
    can_support_claims:
      - 多 agent 在重并行、信息量超过单上下文、多个工具接口的研究任务中有优势
      - lead agent 需要拆分任务、给出明确目标和输出格式，并管理并行复杂度
    cannot_support_claims:
      - 不能证明所有 coding / writing 任务都适合多 agent
  - source_name: local Superpowers skills
    source_url_or_path: /Users/chuchenqidawang/.codex/plugins/cache/openai-curated-remote/superpowers/5.1.3/skills
    source_role: local_operational_skill_rules
    can_support_claims:
      - 本地技能要求先读 SKILL.md、TDD 红绿、完成前验证、并行子代理只处理独立任务
    cannot_support_claims:
      - 不能替代当前项目实际小题验证
```

## 三、小题执行

```yaml
micro_task_execution_check:
  task: 构造缺少方法应用字段的临时恢复链 fixture
  expected_behavior: verify_governance_recovery_tool preset 必须失败
  red_test:
    command: python3 tools/test_verify_governance_recovery.py
    observed_result: 新增测试最初失败，因为旧 verifier 对缺少 best_practice_learning_contract / main_agent_integration_review / claim_readiness_ladder 的 fixture 返回 failure_count 0
  green_test:
    command: python3 tools/test_verify_governance_recovery.py
    observed_result: 更新 verifier required 与完整 fixture 后输出 ok
  pass_fail: pass
  remaining_gap: 仍需在后续真实项目中检验这些字段是否降低实际协作摩擦，而不仅是字段存在
```

## 四、两名只读子代理反馈

```yaml
subagents:
  capability_probe:
    tool_discovered: true
    callable_tool: multi_agent_v1.spawn_agent
    spawn_attempted: true
    agent_ids:
      - 019eee67-01c4-7251-bd4b-1bf5a6c836d2
      - 019eee67-1e8a-74c1-bbde-4417cd9873da
  lifecycle_ledger:
    - role: protocol_rule_auditor
      return_status: completed
      accepted_items:
        - 外部方法触发口径需要统一
        - skill 和 plugin/connector 的副作用等级需要区分
        - 子代理结果需要覆盖率闸门
      rejected_items:
        - 不把具体 autograder 场景写成主协议模板
    - role: unfamiliar_project_simulator
      return_status: completed
      accepted_items:
        - best_practice_learning_contract
        - main_agent_integration_review
        - claim_readiness_ladder
      rejected_items:
        - 不把高校作业平台模拟场景写成领域目录
  integration_decision: partially_adopted_as_generic_gates
```

## 五、方法综合

```yaml
best_practice_learning_contract:
  trigger_source: user_request
  stage_gap: 子代理方法学习容易停在“读过框架名”，没有转化为当前项目 contract、review 和降级规则
  practice_pattern_extracted:
    - lead_or_main_agent_keeps_final_judgment
    - subagents_need_specific_objective_context_output_contract
    - parallel_agents_fit_independent_information_domains
    - skills_are_on_demand_instruction_packages
    - handoff_or_tool_calling_requires_clear_control_boundary
  failure_mode_learned:
    - best_practice_name_drop_gap
    - capability_side_effect_blind_spot
    - skill_plugin_discovery_bias_gap
    - subagent_contract_coverage_gap
    - claim_readiness_jump_gap
  project_stage_gap_addressed: 连续自我优化中的子代理/skill/plugin 编排从“会调用”升级为“会选择、会授权、会验收、会整合、会降级”
  non_transfer_boundary:
    - Anthropic 搜索系统经验主要适合重并行研究，不自动迁移到所有 coding / writing 任务
    - LangChain / OpenAI SDK 的框架模式不能替代 Codex 当前工具可用性探测
    - plugin/connector 可能涉及外部账号或写入副作用，不能按本地 skill 处理
  minimum_application_test: verifier 新增缺字段红绿回归，并用两名只读子代理审计字段合理性
  downgrade_if_not_tested: 只能说“候选方法”，不能说“协议能力已晋升”

capability_type_and_side_effect_gate:
  capability_type_options:
    - skill
    - plugin
    - connector
    - local_tool
    - web_source
    - external_method
  operation_mode_options:
    - read_instructions
    - call_tool
    - install
    - authenticate
    - write_external_state
  side_effect_rule: plugin / connector / external_write / account_or_permission 必须进入授权边界或 manual_action_required

skill_plugin_discovery_gate:
  minimum_record:
    - discovery_basis
    - candidate_list
    - selected
    - rejected_candidates_with_reason
    - instruction_read_evidence
    - call_or_skip_decision

subagent_method_learning_trace:
  source_mix:
    local_skill_or_plugin: Superpowers subagent-driven-development, dispatching-parallel-agents, TDD, verification-before-completion
    online_or_official_method: OpenAI Codex skills/subagents, OpenAI Agents SDK orchestration, LangChain multi-agent, Anthropic multi-agent research system
    codex_tool_capability: multi_agent_v1.spawn_agent / wait_agent / close_agent
  method_synthesis:
    independent_domain_rule: 并行子代理只用于独立证据源、独立问题域或 disjoint write scope
    context_isolation_rule: 子代理接收主代理整理的 input packet，不继承整段混乱上下文
    handoff_or_guardrail_rule: 只有控制权或工具边界清楚时 handoff；高风险副作用先授权
    review_and_integration_rule: 主代理逐项核对 coverage，记录冲突、采纳、拒收和最终主张变化
    tool_discovery_permission_rule: 子代理默认不自行发现/调用插件；若允许，必须限定 capability_type、side_effect_level 和返回前置候选
  micro_task_used_to_validate: tools/test_verify_governance_recovery.py::test_preset_fails_when_orchestration_method_application_fields_missing
  adopted_into_subagent_contract:
    - best_practice_learning_contract
    - capability_type_and_side_effect_gate
    - skill_plugin_discovery_gate
    - subagent_result_coverage_gate
    - main_agent_integration_review
    - claim_readiness_ladder
  rejected_or_backlogged_parts:
    - 不把任何一个外部框架的术语完整搬进主协议
    - 不新增具体领域模板

claim_readiness_ladder:
  levels:
    - idea_or_candidate
    - source_backed
    - locally_verified
    - small_loop_validated
    - pilot_ready
    - production_or_public_claim_ready
  downgrade_rule: 当前轮只证明方法字段和恢复链可验证；不能证明所有后续项目都会自动高质量调用子代理
```

## 六、规则晋升

```yaml
promotion_decision:
  promoted_to_protocol:
    - best_practice_learning_contract
    - capability_type_and_side_effect_gate
    - skill_plugin_discovery_gate
    - subagent_result_coverage_gate
    - main_agent_integration_review
    - claim_readiness_ladder
  promoted_failure_modes:
    - best_practice_name_drop_gap
    - capability_side_effect_blind_spot
    - skill_plugin_discovery_bias_gap
    - subagent_contract_coverage_gap
    - claim_readiness_jump_gap
  anti_protocol_bloat_gate:
    trigger_signal: 用户要求学习网上方法、skill、插件并融入协议
    observable_behavior: 字段进入主协议、路由表、发布包、变更清单、长日志和 verifier preset
    route_back_if_failed: 回到字段覆盖测试或真实项目小题
    user_friction_impact: 用户不需要知道字段名，只说学习方法或提升子代理能力即可触发
```
