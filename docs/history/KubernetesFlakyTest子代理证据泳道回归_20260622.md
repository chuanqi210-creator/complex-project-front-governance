# Kubernetes Flaky Test 子代理证据泳道回归 2026-06-22

## 一、本轮真实项目样本

样本：Kubernetes issue #139417 `integration: TestDRA/all/PodGroup/gang-2-pods-mincount-2 flake`

来源：

1. GitHub issue：https://github.com/kubernetes/kubernetes/issues/139417
2. 关联修复 PR：https://github.com/kubernetes/kubernetes/pull/139418
3. 后续尝试 PR：https://github.com/kubernetes/kubernetes/pull/139602
4. Anthropic《Building effective agents》：https://www.anthropic.com/engineering/building-effective-agents
5. OpenAI Agents SDK Agent orchestration：https://openai.github.io/openai-agents-python/multi_agent/
6. AutoGen Teams：https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html
7. 本地 Superpowers skill：`dispatching-parallel-agents`、`subagent-driven-development`、`verification-before-completion`

## 二、小题目标

检验 `subagent_method_learning_trace` 在真实软件工程问题中是否能指导子代理分工，而不是只写“可以调用多个 agent”。本轮选择 Kubernetes flaky test，是因为它天然容易诱发错误并行：日志、issue triage、DRA/scheduler 假设、PR 修复和后续复发互相相关，但最终根因和修复路线高度耦合。

## 三、事实摘录

```yaml
source_role_map:
  github_issue_139417:
    role: bug_report_and_thread_timeline
    can_support_claims:
      - issue_state_open
      - labels_sig_scheduling_kind_flake_needs_triage
      - failing_test_and_initial_failure_text
      - maintainer_discussion_timeline
    cannot_support_claims:
      - final_root_cause_confirmed
      - all_flakes_fixed
      - release_inclusion
  pr_139418:
    role: merged_fix_attempt_and_code_change_scope
    can_support_claims:
      - merged_true_at_2026_06_02
      - changed_dynamicresources_go_and_test
      - described Reserve_PreBind_Unreserve accounting bug
    cannot_support_claims:
      - issue_fully_resolved_after_followup_comments
  followup_comment_2026_06_08:
    role: post_merge_residual_flake_evidence
    can_support_claims:
      - tests_still_flaking_for_different_reason
      - candidate_race_between_status_update_and_next_binding_attempt
      - three_candidate_fix_directions
    cannot_support_claims:
      - chosen_final_fix_merged
```

关键时间线：

1. 2026-06-01 issue 打开，Prow log 指向 `TestDRA/all/PodGroup/gang-2-pods-mincount-2` 超时，失败片段包括 PreBind plugin `DynamicResources` 和 claim “got allocated elsewhere in the meantime”。
2. 2026-06-01 维护者判断可能由 #138775 中的 commit 修复，并尝试复现。
3. 2026-06-02 PR #139418 创建并合入，文件范围为 `pkg/scheduler/framework/plugins/dynamicresources/dynamicresources.go` 与对应测试。
4. 2026-06-08 维护者说明测试仍 flaking，但“now for a different reason”，候选问题变成状态更新与下一次 binding attempt 的 race。
5. 2026-06-09 维护者尝试第一种路线，指向 PR #139602。

## 四、网上方法与本地 skill 抽象

```yaml
subagent_method_learning_trace:
  source_mix:
    local_skill_or_plugin:
      - Superpowers dispatching-parallel-agents: 独立问题才能并行，避免重复和共享状态冲突
      - Superpowers subagent-driven-development: 子任务必须有完整任务文本、上下文包、验收、review gate 和主代理整合
      - Superpowers verification-before-completion: 子代理返回后仍需主代理做 fresh verification
    online_or_official_method:
      - Anthropic Building effective agents: 优先简单、可组合 workflow；复杂度只在必要时增加；parallelization 适合可聚合的独立工作
      - OpenAI Agents SDK Agent orchestration: agents-as-tools 适合一个 manager 保留最终答案、整合 specialist 输出、集中 enforce guardrails
      - AutoGen Teams: 复杂任务才使用 team；简单任务先优化单 agent，team 需要更多 scaffolding 和可观察性
    codex_tool_capability:
      - multi_agent_v1.spawn_agent
      - multi_agent_v1.wait_agent
      - multi_agent_v1.close_agent
  method_synthesis:
    independent_domain_rule: 能并行的是证据来源和审计问题，不一定是最终根因或修复 worker
    context_isolation_rule: 每条 lane 只拿自己需要的 issue/PR/log/规则片段和禁止动作
    handoff_or_guardrail_rule: read_only evidence lane 禁止评论 issue、改 label、写 patch、宣布根因或选择修复
    review_and_integration_rule: 主代理把各 lane 的事实、候选假设和缺口合并进一个 integrated decision
  micro_task_used_to_validate: Kubernetes issue #139417 子代理分工设计
  adopted_into_subagent_contract: parallel_evidence_lane_trace
  rejected_or_backlogged_parts:
    - 不把 Kubernetes DRA/PodGroup/PreBind 写成主协议模板
    - 不把任何外部框架名写成规则本身
```

## 五、并行证据泳道设计

```yaml
parallel_evidence_lane_trace:
  case_type: flaky_test_or_incident_triage_with_shared_root_cause
  why_parallel_evidence_allowed: 日志复现、项目治理状态和代码/机制假设可独立读证据
  why_parallel_fix_forbidden: 最终根因、PR 路线和维护者动作高度耦合，任何一个 lane 单独下结论都容易误导
  evidence_lanes:
    - lane_id: prow_log_repro_lane
      role: read_only_audit
      output_contract:
        - job_run_test_name
        - failure_excerpt_and_time_anchor
        - single_or_repeated_signal
        - missing_repro_evidence
        - fact_inference_split
      forbidden_actions:
        - edit_code
        - trigger_prow
        - comment_issue
        - announce_root_cause
        - propose_final_fix
    - lane_id: ownership_triage_lane
      role: read_only_audit
      output_contract:
        - labels_and_SIG_WG_state
        - issue_PR_milestone_triage_state
        - likely_owner_areas
        - questions_for_maintainer_or_reviewer
      forbidden_actions:
        - change_labels
        - contact_maintainers
        - decide_priority
        - substitute_project_triage
    - lane_id: scheduler_dra_hypothesis_lane
      role: read_only_audit
      output_contract:
        - candidate_mechanisms
        - invariants_to_verify
        - evidence_that_would_discriminate_hypotheses
        - non_facts_and_uncertainties
      forbidden_actions:
        - write_patch
        - turn_hypothesis_into_fact
        - decide_root_cause
        - expand_into_unrelated_refactor
  shared_final_decision: main_agent_only
  integration_key:
    - issue_thread_time_order
    - PR_merge_state_and_followup_comments
    - fact_vs_hypothesis_vs_action_boundary
  merge_conflict_rule: 来源时间线和项目维护者语境优先；冲突未解时降级为候选假设，不能写成最终根因
```

## 六、暴露的协议缺口

现有 `subagent_problem_decomposition_builder` 字段足够承载这类分工，但原规则 `same_root_cause_likely` 容易被误读成“完全不能并行”。真实软件问题显示更精细的做法是：

1. 根因/修复高度耦合时，禁止并行 root-cause worker 或 fix worker。
2. 仍可并行只读 evidence lanes，但每条 lane 只交付事实、候选假设和缺口。
3. 最终根因裁决、修复路线选择、是否评论 issue/开 PR/改 triage，必须由主代理或真实项目维护者语境统一裁决。

## 七、规则晋升判断

```yaml
rule_promotion_mechanism:
  candidate_rule: parallel_evidence_lane_trace
  promotion_scope: main_protocol_tightening_rule
  evidence:
    - Kubernetes flaky test 小题
    - Banach read_only_audit 建议
    - Superpowers 子代理契约与 review 规则
    - OpenAI agents-as-tools manager pattern
    - Anthropic simple composable workflow and parallelization guidance
    - AutoGen team complexity warning
  anti_protocol_bloat_gate:
    trigger_signal: same_root_cause_likely 但存在多条可独立核验的信息源
    observable_behavior: 只并行 read_only evidence lanes，不并行最终 root-cause/fix worker
    check: 每条 lane 有 output_contract、forbidden_actions、write_scope none、integration_key
    route_back: 若 lane 试图裁决根因或写 patch，退回 single integrated decision
    user_friction_impact: 不增加用户问题数，只改善内部子代理调度
  decision: adopt_as_generic_tightening_rule
```

## 八、不能外推

本回归不证明 Kubernetes #139417 已完全解决，不评价 PR #139602 的最终状态，也不把 DRA/scheduler 细节写入主协议。它只证明：在真实软件工程 triage 中，子代理最佳分工经常不是“并行解决问题”，而是“并行读取不同证据，最后由主代理合并裁决”。
