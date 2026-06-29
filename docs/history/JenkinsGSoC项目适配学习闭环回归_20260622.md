# Jenkins GSoC 项目适配学习闭环回归

current_as_of：2026-06-22

## 一、本轮缺口

第 178 节新增 `skill_plugin_learning_loop` 后，协议已经能证明“读过 skill/plugin、做过小题、写回验证器”。但它仍可能脱离真实项目：工具学习本身很完整，项目主张、验收链和交付证据却没有变得更具体。

本轮用 Jenkins GSoC 2026 “AI Chatbot to Guide User Workflow” 做真实开源项目小题，检验 skill/plugin 学习是否真的改善项目构造。

新增失败模式：

`skill_plugin_detached_from_project_gap`：skill/plugin 学习闭环自洽，但没有绑定当前真实项目的主张、阶段缺口、验收链、协作方式或交付证据；结果是工具学习本身通过了，项目却没有更可执行、更可验证或更低摩擦。

## 二、真实来源与来源角色

| 来源 | 证据角色 | 可支撑内容 | 不可支撑内容 |
| --- | --- | --- | --- |
| https://www.jenkins.io/projects/gsoc/2026/project-ideas/ | 官方项目池 | Jenkins GSoC 2026 有 accepted project ideas；AI Chatbot 是 accepted idea，类别为 Plugins，列出技能方向和 mentors | 不能证明该项目已经交付或被 Jenkins 采纳 |
| https://www.jenkins.io/projects/gsoc/2026/project-ideas/ai-chatbot-to-guide-user-workflow/ | 项目目标与 quick-start | 项目目标是把 AI chatbot 集成进 Jenkins，帮助 workflow、documentation、troubleshooting；技能涉及 NLP、Python、JS/TS、LLM、UI/UX、Jenkins；quick-start 要熟悉 Jenkins、NLP/AI libraries、已有 chatbot、Jenkins plugin tutorial | 不能证明任意 chatbot 架构可行，也不能证明 LLM 回答准确 |
| https://www.jenkins.io/projects/gsoc/contributors/ | 贡献流程约束 | 申请流程要求 proposal template、熟悉 Jenkins、加入 Discourse/Gitter、公开讨论、推荐相关贡献；Jenkins 期望 public communication 和 first contributions | 不能替代 mentor 反馈、issue 认领、PR 和 CI 结果 |
| `superpowers:dispatching-parallel-agents` 与 `github:github` skill | 方法来源 | 把开源项目治理拆成 focused/self-contained 子任务；GitHub 工作需先解析 repo/issue/PR 上下文 | 不能凭 skill 本身证明项目达成 |

## 三、小题实测

```yaml
micro_task_execution_check:
  task: 将 Jenkins AI Chatbot 项目从泛化 AI 方案改造成开源项目验收链
  input_material:
    - Jenkins GSoC 2026 project ideas
    - AI Chatbot to Guide User Workflow project page
    - Jenkins GSoC contributors guide
    - superpowers dispatching-parallel-agents
    - github plugin skill
  action_taken:
    - 抽取项目目标、skills、quick-start 和 contributor application constraints
    - 构造 source_role_map，限制官方来源可支撑的范围
    - 把 skill/plugin 学习转成 skill_plugin_project_fit_trace
    - 形成一个开源项目验收链，而不是泛化 chatbot 描述
  actual_execution_evidence:
    - 官方项目页命中 AI Chatbot accepted idea、项目目标、skills、quick-start
    - contributor guide 命中 proposal template、Discourse/Gitter、public communication、first contributions
    - verifier 红灯测试曾放过缺少 skill_plugin_project_fit_trace 的夹具
    - verifier 绿灯测试要求新字段存在
  observed_result: 学习闭环从“读过 skill/plugin”升级为“项目适配前后差异可检查”
  pass_fail: pass
  remaining_gap: 内容质量仍需真实 mentor 反馈、issue/PR/CI 证据验证
```

## 四、skill_plugin_project_fit_trace

```yaml
skill_plugin_project_fit_trace:
  project_context: Jenkins GSoC 2026 AI Chatbot to Guide User Workflow
  primary_claim_or_stage_gap: 需要证明 proposal 能服务 Jenkins workflow / docs / troubleshooting，而不是泛化 AI chatbot demo
  pre_skill_gap:
    - 只有 AI chatbot、NLP、LLM、UI/UX 等宽泛技术关键词
    - 缺少 Jenkins contributor 公开沟通、proposal、first contribution、plugin integration 和验收证据链
  selected_skill_or_plugin:
    - superpowers:dispatching-parallel-agents
    - github:github
  transferred_method:
    - 把任务拆成 docs retrieval、workflow guidance、troubleshooting intent、plugin integration、community feedback 五个独立审计面
    - GitHub/开源上下文先解析 repo、issue、PR、CI 和维护者反馈，不把本地 demo 当成开源采纳
  micro_task_before_after:
    before: “做一个 Jenkins AI chatbot，能回答文档和排障问题”
    after: “proposal 需给出 Jenkins workflow/docs/troubleshooting 三类 query set、信息源索引边界、幻觉降级策略、plugin integration 路径、公开讨论链接、first contribution/issue/PR/CI/mentor feedback 证据链”
  acceptance_evidence:
    - project_goal_maps_to_query_sets: workflow guidance / documentation access / troubleshooting
    - quick_start_maps_to_prework: Jenkins familiarity / NLP libraries / existing chatbot / plugin tutorial
    - contributor_guide_maps_to_handoff: proposal template / Discourse or Gitter discussion / public communication / first contributions
    - downstream_hard_evidence_needed: issue link / PR link / CI result / mentor feedback / merged release note
  non_transfer_boundary:
    - 官方 idea page 只能证明项目目标和技能需求，不能证明实现可用
    - contributor guide 只能证明申请与协作流程，不能证明 proposal 会被接受
    - skill/plugin 学习只能改善治理方法，不能替代开源维护者反馈
  reuse_decision: reusable
```

## 五、写回判断

```yaml
anti_protocol_bloat_gate:
  new_rule_or_trace: skill_plugin_project_fit_trace
  trigger_signal: 已有 skill_plugin_learning_loop，但本轮需要证明学习结果改善真实项目
  observable_behavior: 记录 project_context、pre_skill_gap、micro_task_before_after、acceptance_evidence 和 non_transfer_boundary
  required_evidence_or_check: verify_governance_recovery_tool preset 缺字段会失败；真实项目记录包含 source_role_map
  route_back_if_failed: 回到真实项目构造器，而不是继续写 skill 学习总结
  user_friction_impact: 不增加用户输入负担，由 AI 在项目治理中自动填写
  replaces_or_tightens_existing_rule: 收紧 skill_plugin_learning_loop
  decision: write_to_protocol
```

## 六、下一轮约束

`skill_plugin_project_fit_trace` 不应变成 Jenkins 模板。后续只在用户明确触发 skill/plugin 学习，或 agent 自我优化声称学习了某种外部方法时使用；具体项目字段仍由 `new_domain_governance_builder` 临时生成。
