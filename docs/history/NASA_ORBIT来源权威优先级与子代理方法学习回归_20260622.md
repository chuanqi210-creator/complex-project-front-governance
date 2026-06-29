# NASA ORBIT 来源权威优先级与子代理方法学习回归

current_as_of: 2026-06-22

## 一、本轮问题

第 180 节之后，协议已经能记录 `source_role_map`，也能把 skill/plugin 学习绑定到真实项目。但 NASA ORBIT Challenge 2026 暴露了一个更细的共性缺口：

1. `source_role_map` 能说明“哪个来源能支撑什么”，但不能说明“多个来源冲突时谁优先”。
2. 子代理能力学习已经要求读 skill/plugin，但用户进一步要求学习网上方法、skill、插件来提升“构建子代理解决问题”的能力；协议需要把这些方法转为可执行分工规则，而不是只写参考名称。

本轮不新增 NASA 或竞赛专属模板，只晋升两个通用能力：`source_authority_precedence_trace` 和 `subagent_method_learning_trace`。

## 二、真实来源与来源角色

| 来源 | 链接 | 可支撑 | 不能支撑 |
| --- | --- | --- | --- |
| NASA 官方介绍页 | https://www.nasa.gov/directorates/stmd/prizes-challenges-crowdsourcing-program/center-of-excellence-for-collaborative-innovation-coeci/nasa-orbit-challenge-2026/ | NASA ORBIT 是 NASA 公布的学生挑战；页面记录奖金、报名开放/截止日期，并导向 nasaorbit.org | 不能替代详细规则、提交材料、评审、资格和程序要求 |
| NASA ORBIT rules page | https://nasaorbit.org/rules/ | 官方规则、资格、要求、截止日期、程序、提交材料、评审与 AI 使用披露要求 | 不能单独证明项目成果真实落地或某团队会获奖 |
| NASA ORBIT timeline/phases page | https://nasaorbit.org/timeline-phases/ | 时间线视图、阶段安排、报名和阶段提交日期 | 若与 rules page 冲突，只能作为补充线索，不能覆盖规则页 |
| NASA ORBIT project guide | https://nasaorbit.org/wp-content/uploads/2025/12/NASA-ORBIT-Project-Guide.pdf | 参赛准备、项目指南、交付物解释 | 不能覆盖规则页对资格、截止日期和程序的最终裁决 |

关键事实：NASA ORBIT rules page 明确把自身定位为比赛要求、资格、截止日期和程序的最高权威来源，并说明其他材料只作参考。该事实使本轮缺口不是“来源角色”问题，而是“来源权威优先级”问题。

## 三、source_authority_precedence_trace 小题

```yaml
source_authority_precedence_trace:
  trigger: source_self_claims_authority
  claim_scope: NASA ORBIT participation requirements, eligibility, deadlines, procedures, submissions, judging
  precedence_order:
    - source_url: https://nasaorbit.org/rules/
      authority_rank: 1
      governs: requirements, eligibility, deadlines, procedures, submission rules, judging, AI disclosure
      does_not_govern: outcome evidence, external adoption, public impact
      basis: rules page self-identifies as the official authoritative source for competition requirements and procedures
    - source_url: https://nasaorbit.org/timeline-phases/
      authority_rank: 2
      governs: timeline display and phase overview
      does_not_govern: overriding rules page in conflict
      basis: official challenge site, but function is timeline presentation
    - source_url: https://www.nasa.gov/directorates/stmd/prizes-challenges-crowdsourcing-program/center-of-excellence-for-collaborative-innovation-coeci/nasa-orbit-challenge-2026/
      authority_rank: 3
      governs: NASA public announcement, challenge overview, prize summary, referral to nasaorbit.org
      does_not_govern: detailed eligibility, submission and judging procedure
      basis: NASA overview page links out to the challenge site for more information
  conflict_rule: if deadline, eligibility or procedure differs, cite both and follow the rules page; if the rules page is unavailable or ambiguous, downgrade to user/manual confirmation.
  freshness_or_version_check: check canonical URLs and current_as_of date before using deadlines or active procedures.
  fallback_if_unresolved: write "以官方规则页为准，当前信息需复核"，do not present a final operational instruction.
```

### 前后差异

Before: NASA ORBIT 有 38 万美元奖金、报名截止日期、阶段安排，可以直接用 NASA 页面和 timeline 归纳参赛规则。

After: NASA 页面和 timeline 只能分别支撑“项目存在/公开概览”和“时间线视图”；涉及资格、要求、截止日期、程序、提交材料、评审和 AI 使用披露时，以 rules page 为最高优先。若来源冲突，结论降级，不装作已裁决。

## 四、子代理方法学习来源

本轮读取并归纳的本地与外部方法：

| 方法来源 | 链接或路径 | 可迁移约束 |
| --- | --- | --- |
| Superpowers dispatching-parallel-agents | `/Users/chuchenqidawang/.codex/plugins/cache/openai-curated-remote/superpowers/5.1.3/skills/dispatching-parallel-agents/SKILL.md` | 一个 agent 对应一个独立问题域；任务要自包含、边界明确、输出具体；返回后主代理审查和整合 |
| Superpowers subagent-driven-development | `/Users/chuchenqidawang/.codex/plugins/cache/openai-curated-remote/superpowers/5.1.3/skills/subagent-driven-development/SKILL.md` | 有计划、任务相对独立时可用 fresh subagent；实现后先 spec review，再 quality review；不要把最终判断外包 |
| Anthropic multi-agent research system | https://www.anthropic.com/engineering/multi-agent-research-system | 多代理适合开放研究和多方向并行探索；subagent 使用独立上下文压缩不同方向，再交给 lead agent 统合 |
| OpenAI Agents SDK handoffs / guardrails | https://openai.github.io/openai-agents-python/handoffs/ 与 https://openai.github.io/openai-agents-python/guardrails/ | handoff 要清楚移交对象和输入；guardrail 用于输入/输出检查与触发阻断，适合转化为子代理契约和 review gate |
| Google ADK workflows / multi-agent docs | https://google.github.io/adk-docs/agents/workflows/ | 多代理可用 workflow 组织顺序、并行和循环；适合转化为动态阶段控制器的 sequential / parallel / review 路由 |
| Codex 当前工具能力 | `multi_agent_v1.spawn_agent` / `wait_agent` / `close_agent` | 能真实调用、等待、关闭子代理；必须记录 tool_discovered、spawn_attempted、agent_return_status 和 close_status |

## 五、subagent_method_learning_trace

```yaml
subagent_method_learning_trace:
  source_mix:
    local_skill_or_plugin:
      - dispatching-parallel-agents
      - subagent-driven-development
    online_or_official_method:
      - Anthropic multi-agent research system
      - OpenAI Agents SDK handoffs and guardrails
      - Google ADK workflows
    codex_tool_capability:
      - multi_agent_v1.spawn_agent
      - multi_agent_v1.wait_agent
      - multi_agent_v1.close_agent
  method_synthesis:
    independent_domain_rule: only spawn when tasks are genuinely independent or have isolated write scopes
    context_isolation_rule: main agent prepares a compact context packet; subagent must not inherit an unbounded conversation dump
    handoff_or_guardrail_rule: every delegated task must include task boundary, forbidden actions, output contract and acceptance checks
    review_and_integration_rule: main agent reviews, accepts/rejects/conflicts, records lifecycle cleanup and keeps final judgment
  micro_task_used_to_validate: NASA ORBIT source-authority audit delegated to one read-only subagent, then integrated with local source checks
  adopted_into_subagent_contract:
    - add external_method_sources to skill_plugin_learning_loop
    - add subagent_method_learning_trace to problem decomposition builder
    - keep source_authority_precedence_trace as project-facing evidence arbitration
  rejected_or_backlogged_parts:
    - do not import whole external agent frameworks into the protocol
    - do not add vendor-specific agent templates
    - do not let subagents write final public claims without main-agent verification
```

## 六、子代理审计

```yaml
subagent_lifecycle_ledger:
  - contract_id: audit_source_authority_precedence_gap_20260622
    agent_id: 019eee34-0fd8-7a82-b9b3-6afc65495b01
    role: read_only_audit
    agent_return_status: done
    integration_decision: accepted
    accepted_items:
      - source_role_map is insufficient without authority precedence
      - verifier should fail when the new field is missing
      - keep field generic; avoid NASA/rules/timeline-specific templates
    close_status: closed
```

## 七、规则晋升判断

```yaml
rule_promotion_mechanism:
  candidate_rule_or_lens:
    - source_authority_precedence_trace
    - subagent_method_learning_trace
  source_experience_entries:
    - NASA_ORBIT来源权威优先级与子代理方法学习回归_20260622
    - 子代理问题拆解与来源角色回归_20260622
    - JenkinsGSoC项目适配学习闭环回归_20260622
  repeated_across_projects: yes
  abstracts_to_common_failure_mode: yes
  improves_new_domain_construction: yes
  reduces_or_preserves_user_friction: yes
  anti_protocol_bloat_gate:
    trigger_signal: multiple sources cover same claim or user asks to learn subagent methods
    observable_behavior: add one compact trace, not a new field per domain
    required_evidence_or_check: regression file + verifier required field + route table entry
    route_back_if_failed: downgrade to experience library only
    user_friction_impact: low; user does not need to name the field
  decision: write_to_protocol
```

## 八、新增失败模式

1. `source_authority_flattening_gap`：多个来源同时覆盖同一规则、日期、要求、程序或事实主张时，只标注来源角色，却没有记录冲突时谁优先。
2. `subagent_method_name_drop_gap`：学习网上方法、skill 或插件时，只写框架名称，没有抽取可执行子代理约束，也没有用当前项目小题验证。

