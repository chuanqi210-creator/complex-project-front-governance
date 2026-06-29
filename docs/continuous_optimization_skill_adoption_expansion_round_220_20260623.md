# 第220轮 External Skill Adoption Expansion 记录

日期：2026-06-23

本轮目标：回应用户对 `mattpocock/skills` 外部技能库的提醒，按“相关优先烟测”而不是“全量机械安装”的方式，验证哪些 skill 能让复杂项目前置治理协议更好用，并把公开仓库同步限定为可开源的协议说明、能力发现规则、skill 采用结论和可视化站点。

## 1. Entry Gate

```yaml
round_id: 220
trigger:
  user_request: "审核未提交改动、扩展验证 Matt skills、形成不需用户主动提供也能在关键阶段搜寻技能/工具/API/方法的机制，并同步公开 GitHub 仓库。"
  latest_recovered_machine_board: "## 219. 当前机器看版"
  previous_route: continue_self_optimization_training_round_219_or_stop
  proceed_decision: continue
scope_boundary:
  private_workspace: "Only records and recovery-chain metadata are updated here."
  public_workspace: "/Users/chuchenqidawang/Documents/complex-project-front-governance-public"
  github_target: "chuanqi210-creator/complex-project-front-governance"
  excluded_from_public_sync:
    - docs/history raw evidence packages
    - long private recovery logs
    - rendered PDF/PNG history materials
    - private absolute paths
    - node_modules/dist/temp artifacts
capability_discovery_cadence_gate:
  initial_scan:
    status: done
    scanned_surfaces:
      - local_skills
      - installed_skills
      - callable_tools
      - deferred_tools
      - external_skill_libraries
      - public_github_repo
      - local_scripts
      - public_package_checker
    candidates_considered:
      - diagnosing-bugs
      - tdd
      - grill-with-docs
      - setup-matt-pocock-skills
      - ask-matt
      - decision-mapping
      - review
      - handoff
      - to-prd
      - to-issues
      - domain-modeling
      - codebase-design
      - codegraph
      - improve-codebase-architecture
      - superpowers:dispatching-parallel-agents
      - superpowers:subagent-driven-development
      - tool_search
      - multi_agent_v1
      - tools/check_public_package.py
    selected_now:
      - implement
      - superpowers:executing-plans
      - github:yeet_as_write_safety_reference
      - superpowers:verification-before-completion
      - superpowers:dispatching-parallel-agents
      - superpowers:subagent-driven-development
      - review_as_public_sync_review_lens
      - handoff_as_public_template_lens
      - codebase-design_as_tool_boundary_lens
    rejected_now:
      - skill-creator: "Not creating a reusable Codex skill in this round."
      - plugin-creator: "Not creating a Codex plugin in this round."
      - full_34_skill_install: "No value without proof; use relevant-priority smoke tests first."
    backlog:
      - "Run a dedicated setup-matt-pocock-skills onboarding when this repo starts using GitHub issues as the main work tracker."
      - "Try improve-codebase-architecture in a separate architecture-health round."
      - "Turn repeated effective skill rules into docs/agents/skill_usage.md only after repeated cross-project value."
      - "Install or expose codegraph CLI, then re-evaluate it after codegraph doctor succeeds."
  periodic_reconsideration:
    required_triggers:
      - stage_transition
      - new_user_requirement
      - blocked_or_failing_verification
      - external_write_or_subagent_boundary
      - before_final_claim
    checks_performed:
      - "tool_search was used to expose multi_agent_v1 before objective audit subagents were spawned."
      - "Public write boundary was checked before GitHub sync."
      - "Verification-before-completion will be run before claiming success."
    next_check: before_final_claim
  lightweight_exception: ""
iteration_quality_bar:
  entry_gate:
    latest_machine_board_exists: true
    candidate_count: 14
    high_value_candidate_present: true
    capability_discovery_checked: true
  execution_gate:
    selected_main_chain: external_skill_adoption_expansion_plus_public_sync
    one_main_chain_only: true
    micro_task_type: skill_smoke_and_public_package_sync
    promotion_policy: "single-round evidence goes to round record/public docs; main protocol or verifier required only after repeated cross-project failure or stable scriptability."
  exit_gate:
    expected_next_route: continue_self_optimization_with_skill_adoption_expansion_or_stop
```

## 2. Smoke-Test Method

每个 skill 的小题都使用同一判断口径：

```yaml
skill_smoke_template:
  source_url:
  skill_version_or_ref:
  micro_task:
  observed_benefit:
  friction:
  risk:
  decision: adopt_now | adapt_later | backlog | reject
  promotion_condition:
```

本轮的“用到”分三层：

1. `active_use`：本轮实际读完 skill 并用其约束当前执行。
2. `smoke_evaluated`：读完 skill，拿当前项目做小题判断，但不直接改变主协议。
3. `not_run_due_boundary`：相关但本轮不满足前置条件，写入 backlog 或 reject。

## 3. Skill Decisions

| skill | source_url | skill_version_or_ref | micro_task | observed_benefit | friction | risk | decision | promotion_condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `diagnosing-bugs` | `https://github.com/mattpocock/skills` | local installed skill | 恢复链/verifier 红灯时先诊断再修复 | 能减少猜测式补字段和反复改恢复链 | 对纯文档任务略重 | 若机械套用会拖慢轻量任务 | `adopt_now` | 验证失败、构建失败或 GitHub 反馈异常时默认启用 |
| `tdd` | `https://github.com/mattpocock/skills` | local installed skill | 新协议字段进入 verifier required 前先写最小红绿测试 | 把“规则想法”变成可验证行为 | 只适合可脚本检查的规则 | 不可脚本化规则强行测试会变形 | `adopt_now` | 新增 verifier required 或 public checker 规则时启用 |
| `grill-with-docs` | `https://github.com/mattpocock/skills` | local installed skill | 复杂治理问题先追问并生成 ADR/glossary | 能暴露术语歧义和设计前提 | 会生成额外文档，容易膨胀 | 对本轮已经有明确执行计划，不宜再开访谈 | `adapt_later` | 新项目目标模糊、术语不稳或需要 ADR 时再启用 |
| `setup-matt-pocock-skills` | `https://github.com/mattpocock/skills` | local installed skill | 检查当前仓库是否需要 Matt skills 的 issue tracker 和 agent docs 初始化 | 明确了 `to-prd`/`to-issues`/`review` 的前置依赖 | 会引入 issue tracker、labels 和 docs/agents 结构 | 本轮公开同步不应扩大为完整项目管理迁移 | `backlog` | 当公开仓库明确开始用 GitHub Issues、labels 和 docs/agents 承载路线图时执行一次 |
| `ask-matt` | `https://github.com/mattpocock/skills` | local installed skill | 在能力发现 gate 中作为 skill router，判断当前应走 review/handoff/to-prd/implement 等路线 | 能避免用户主动点名 skill 后才想起使用 | 需要先知道本地 skill 清单 | 若不记录选择理由，会退化为口头路由 | `adopt_now` | 每个较大阶段开始和阻塞时纳入 `capability_discovery_cadence_gate` |
| `decision-mapping` | `https://github.com/mattpocock/skills` | local installed skill | 把“持续优化是否继续”转成候选决策票据 | 适合多轮不确定目标，能收束分支 | 当前第220轮目标已经明确 | 过早使用会把简单执行变成决策文档 | `adapt_later` | 当连续优化出现 3 个以上互斥方向且收益难比较时使用 |
| `review` | `https://github.com/mattpocock/skills` | local installed skill | 审核公开仓库同步 diff 和私有未提交改动取舍 | 强制从 bug/regression/missing tests 视角看输出 | 完整模式需要固定基点和本地标准 | 在文档项目中容易只做风格评论 | `adopt_now` | public sync、恢复链变更、checker 变更前后使用 |
| `handoff` | `https://github.com/mattpocock/skills` | local installed skill | 为公开版 `examples/startup_handoff_template.md` 和长会话交接提炼模板 | 能把恢复上下文压缩成别人可接手的结构 | 不应复制私有长日志 | 可能泄漏内部上下文，必须 public-safe 重写 | `adopt_now` | 上下文压缩、交接模板、公开示例都使用 sanitized handoff |
| `to-prd` | `https://github.com/mattpocock/skills` | local installed skill | 把本协议公开化路线整理为 issue/PRD | 对开源路线图有价值 | 需要 issue tracker setup | 本轮不依赖 GitHub Issues，`gh` 认证也不稳定 | `backlog` | 公开仓库启用 issue tracker 后再转 PRD |
| `to-issues` | `https://github.com/mattpocock/skills` | local installed skill | 把未来协议优化拆成可并行 issue | 能把大优化拆成可认领小切片 | 需要 PRD 和 issue tracker setup | 过早拆分会制造维护负担 | `backlog` | 有公开 roadmap/PRD 后再使用 |
| `domain-modeling` | `https://github.com/mattpocock/skills` | local installed skill | 检查 public README 中的领域词：front-governance、capability discovery、claim readiness、handoff | 有利于稳定公开术语和 glossary | 创建 `CONTEXT.md` 对当前同步偏重 | 术语文档过早会膨胀 | `adapt_later` | 当公开读者反馈术语不清，或新增 glossary 时启用 |
| `codebase-design` | `https://github.com/mattpocock/skills` | local installed skill | 检查协议、gate reference、checker、site 的边界是否清楚 | 能帮助把 verifier、公版 package checker 和协议文档分层 | 对文档说明项目需要轻量使用 | 过度工程化会偏离协议可读性 | `adopt_now` | checker 或 public package 边界变化时用作设计 lens |
| `codegraph` | `https://github.com/mattpocock/skills` | local installed skill, CLI unavailable | 尝试用于仓库结构/依赖导航 | 理论上适合大代码库结构审计 | 当前 `codegraph` CLI 不可用 | 不能把不可调用能力写成已采用 | `backlog` | 本机安装并能 `codegraph doctor` 通过后再重新评估 |
| `improve-codebase-architecture` | `https://github.com/mattpocock/skills` | local installed skill | 生成架构健康 HTML 报告，找协议工具/公开站点改进点 | 适合专门的架构健康轮 | 本轮已有公开同步主链，不能再开大报告 | 容易把第220轮扩大为另一个项目 | `adapt_later` | 单独开启 codebase health round 且有明确验收标准时使用 |

## 4. What This Changes

```yaml
round_220_result:
  skills_actively_used:
    - implement
    - superpowers:executing-plans
    - superpowers:dispatching-parallel-agents
    - superpowers:subagent-driven-development
    - superpowers:verification-before-completion
    - github:yeet_as_write_safety_reference
    - review_as_diff_audit_lens
    - handoff_as_public_template_lens
    - codebase-design_as_boundary_lens
  matt_skills_smoke_evaluated_count: 14
  matt_skills_adopt_now:
    - diagnosing-bugs
    - tdd
    - ask-matt
    - review
    - handoff
    - codebase-design
  matt_skills_adapt_later:
    - grill-with-docs
    - decision-mapping
    - domain-modeling
    - improve-codebase-architecture
  matt_skills_backlog:
    - setup-matt-pocock-skills
    - to-prd
    - to-issues
    - codegraph
  matt_skills_reject: []
  main_protocol_change_allowed: false
  verifier_required_change_allowed: false
  public_docs_change_allowed: true
  public_github_sync_allowed: true
```

本轮没有把 `skill_adoption_expansion` 晋升为新的主协议硬字段，因为 `capability_discovery_cadence_gate`、`skill_plugin_discovery_gate`、`skill_plugin_learning_loop`、`skill_plugin_project_fit_trace` 和 `best_practice_learning_contract` 已覆盖“发现、试用、取舍、写回”的核心要求。需要补的是公开版说明和经验记录，而不是新 gate。

## 5. Public Sync Contract

```yaml
public_sync_contract:
  include:
    - README workflow map and capability discovery explanation
    - protocol/core_protocol.md lightweight skill adoption language
    - protocol/gate_reference.md capability and skill smoke rules
    - docs/skill_adoption.md public-safe adoption summary
    - docs/protocol_explainer_site source
    - examples/startup_handoff_template.md
  exclude:
    - private long recovery chain
    - docs/history raw evidence packages
    - private absolute paths
    - rendered history PDF/PNG artifacts
    - node_modules
    - dist
    - temporary tool caches
  public_checker:
    command: python3 tools/check_public_package.py
  build_checker:
    command: pnpm run build
```

## 6. Subagent Lifecycle Ledger

```yaml
subagent_lifecycle_ledger:
  spawned:
    - role: public_package_sanitization_auditor
      contract: read_only
      write_permission: false
      expected_output: "public-safe gaps before push"
    - role: skill_adoption_objective_auditor
      contract: read_only
      write_permission: false
      expected_output: "adopt/adapt/backlog/reject challenge"
  main_agent_integration_review:
    final_decision_owner: main_agent
    acceptance_rule: "accept only public-safe, evidence-backed, non-duplicative recommendations"
    conflict_rule: "if auditor suggests expansion without repeated cross-project value, downgrade to docs/backlog"
```

## 7. Anti-Expansion Decision

```yaml
anti_protocol_bloat_gate:
  promote_to_protocol: false
  add_to_experience_library: true
  add_to_public_docs: true
  reject_full_installation: true
  reason: "The repeated failure is not absence of a new gate; it is the operational habit of not scanning external capabilities early enough. Existing cadence and skill/plugin gates cover this, so the durable change is examples, public docs and a reusable adoption table."
next_round_decision: stop
may_start_next_round: false
next_route: continue_self_optimization_with_skill_adoption_expansion_or_stop
verification_status: to_be_filled_after_local_and_public_checks
```
