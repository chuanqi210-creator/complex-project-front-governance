# Complex Runtime Cadence Simulation 2026-07-01

用途：用小模拟验证本轮修复是否覆盖用户在其他项目使用 Complex 时遇到的四类摩擦：完整扫描不足、提示词设计未前置、连续节拍中拓扑/工具不复盘、Goal 漂移或完成后自动停止。

本记录不是新的长期机器看版，不改变当前恢复入口；它只作为本轮协议修复的小题证据。

## Scenario 0: 新用户只说“按 Complex 推进”

用户提示：

```text
这个项目按 Complex 推进。
```

旧风险：

- 模型把用户带进“普通项目/重大项目/Plan-only/Goal 模式”的模式菜单，让用户理解内部路由。
- 模型等用户自己说出“连续节拍、多线程、外部工具、人看版”等触发词，新用户不知道这些入口。
- 一次性任务没有 round_goal、Loop 或评分路由，后续交付和恢复容易漂移。

新期望：

- 先运行 `complex_setup_question_card`，确认或默认交付对象、能力权限、协作拓扑、推进节拍和人工边界。
- 展示 `user_visible_trigger_guide`，告诉用户可以用“先设计提示词/prompt”“连续节拍”“多线程/子代理”“外部工具/账号/API”“完整扫描 Complex”“只要人看版”改变推进方式。
- 不让用户选择普通/重大项目；若有高风险、高返工或高公共性，只在内部做工作力度/风险升级并兼容记录 `major_project_mode`。
- 无论是否连续，都建立 round_goal、Plan、Loop/小检查、评分路由、交付契约和恢复记录。

模拟结论：

- 新协议可检查到 `hidden_trigger_vocab_gap`、`major_project_user_mode_confusion_gap`、`optional_goal_plan_loop_gap` 和 `setup_question_missing_gap`。
- Runtime Kit 由 `templates/question.md` 承接启动提问卡，`templates/state.md` 记录用户选择，`templates/loop.md` 记录本轮目标和 Loop 路由。

## Scenario 0.5: 用户只想先设计项目 prompt

用户提示：

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个完美 prompt，再根据这个 prompt 结合 Complex 推进项目。
```

旧风险：

- 模型直接开始做项目，跳过提示词设计前置。
- 模型只给普通 prompt 模板，没有说明实际扫描了哪些 Complex 组件。
- prompt 没有写进能力边界、子代理/多线程、连续节拍、Goal/Loop、评分路由和交付契约，后续线程仍然会漂移。

新期望：

- 先触发 `complex_prompt_bootstrap_gate`，业务执行暂停。
- 输出 `protocol_scan_summary`、`startup_questions_or_defaults`、`project_prompt_design_rationale`、`copy_ready_prompt` 和 `execution_bridge`。
- `copy_ready_prompt` 必须包含项目目标、材料、交付对象、能力边界、协作拓扑、cadence、round_goal/active_goal_summary/工具 Goal 生命周期、Loop、评分路由、证据/权限边界和恢复记录方式。
- 用户确认前不执行、发布或写外部系统；确认后仍以 Complex 主协议和用户最新指令为准。

模拟结论：

- 新协议可检查到 `prompt_bootstrap_missing_gap`。
- Runtime Kit 由 `templates/prompt.md` 承接可复制 prompt，`templates/question.md` 承接 Prompt Bootstrap Card，`templates/state.md` 记录 prompt_bootstrap_status。

## Scenario 0.6: 第二轮 Plan 忘记总 prompt

用户提示：

```text
根据上一轮设计好的 prompt，开启 Plan 模式继续推进下一轮。
```

旧风险：

- 第一轮 `copy_ready_prompt` 质量高，但第二轮 Plan 只关注当前任务，把总规划降级成一句“遵循前文”。
- 用户补充局部细节后，Plan 把细节放大成主线，长期目标、能力边界和交付契约逐渐淡化。
- 连续几轮后，`active_goal_summary`、`next_route` 和项目实际版本仍在推进，但 master prompt 没有进入恢复链。

新期望：

- 先触发 `round_prompt_rehydration_gate`，从 master prompt / active_goal_summary、最新 state 和本轮最高杠杆问题生成 `round_execution_prompt`。
- 第二轮 Plan 必须写明：来自总规划的约束、来自上一轮状态的变化、本轮新增判断。
- 用户补充局部细节时默认作为 prompt patch 写入本轮 prompt；除非用户明确改目标，否则总 prompt 不重写。
- 到第 3 轮或主链变化时，同时触发 prompt rehydration、goal refresh、工具/线程复查。

模拟结论：

- 新协议可检查到 `round_plan_attention_drift_gap`、`master_prompt_decay_gap` 和 `round_prompt_missing_gap`。
- Runtime Kit 由 `templates/prompt.md` 的 Round Prompt Rehydration、`templates/loop.md` 的 `round_execution_prompt` 和 `templates/state.md` 的 master prompt 字段承接。

## Scenario 0.7: 工具 Goal blocked 但项目没有 blocked

用户提示：

```text
连续节拍推进时，当前 Goal 显示 blocked，但项目实际已经从 v51 推进到 v65。
```

旧风险：

- 模型把“连续节拍直到停止”塞进一个长期 Codex 工具 Goal，几十轮后 objective 仍写旧版本。
- 工具 Goal 被判 blocked 后，模型把工具生命周期问题误判成项目研究卡死。
- 用户需要手动清理工具状态，否则下一拍无法自然接上。

新期望：

- 先触发 `per_round_goal_lifecycle_gate`，读取工具 Goal 状态、项目版本、current_basis 和 next_route。
- 若 current_basis 证明项目仍可继续，标记 `stale_or_blocked_tool_goal`，不把项目判成 blocked。
- 连续性由 state、master prompt、closure routing 和 `next_route` 承接；工具 Goal 只做本拍窄目标。
- 如果工具无法清理 blocked 状态，写 `protocol_round_goal`、`goal_migration_note` 和必要的 `manual_clear_needed`，继续按 state 推进。

模拟结论：

- 新协议可检查到 `long_lived_goal_blocked_gap`、`blocked_goal_false_project_block_gap` 和 `round_goal_tool_lifecycle_drift_gap`。
- Runtime Kit 由 `templates/state.md` 的 codex goal lifecycle 字段和 `templates/loop.md` 的 per-round goal lifecycle decision 承接。

## Scenario 1: Plan Mode 完整扫描 Complex

用户提示：

```text
请在 Plan 模式下完整扫描 Complex，再规划本项目。
```

旧风险：

- 模型只读取快速入口或几个熟悉字段。
- 计划只写普通任务步骤，没有覆盖 Complex 的可借鉴组件。

新期望：

- 先按 `protocol_scan_sequence` 读取：项目状态、快速入口、启动提问卡、用户可见触发词、连续节拍、Stage 0-10、能力发现、子代理/线程、Loop/评分、Plan/Goal、交付拆分、Runtime Kit。
- 输出 `user_visible_trigger_guide`，说明“Plan 模式”和“完整扫描”触发的是计划前的协议理解，而不是立即执行；旧称 Plan-only 只是当前环境限制。
- 计划中必须写 `adopt_now`、`skip_now`、`backlog` 和最大误读风险。
- 计划仍必须包含 round_goal、Loop 验证、评分路由和交付契约。

模拟结论：

- 新协议可检查到 `protocol_scan_order_ambiguity_gap` 和 `plan_mode_full_scan_undercoverage_gap`。
- Runtime Kit 由 `templates/state.md` 和 `templates/loop.md` 承接扫描结果与下一轮目标。

## Scenario 2: 连续节拍中的长期分线程和外部工具失配

用户提示：

```text
按 Complex 连续节拍推进，使用多线程和外部工具。
```

旧风险：

- round 1 建过子代理或长期线程，但 round 4 以后主链变化，分线程仍按旧职责输出。
- round 1 选过工具，但后期任务变成渲染、检索、交付或代码验证后，工具组合没有更新。

新期望：

- round 1 建立 `round_index: 1`、topology_summary、capability_summary 和 event_triggered_review_status。
- 主链、项目性质、证据路径、材料类型、交付对象、版本号、外部边界或子线程输出失配时触发 `continuous_cadence_refresh_gate`。
- 3 轮只是兜底上限；无事件触发时只写 lightweight keep，不重跑完整工具和线程盘点。
- 主线程必须给每个分线程一个结果：keep / adjust / pause / close / replace。
- 能力清单必须给每个工具一个结果：keep / adjust / replace / pause / manual_action / retire。

模拟结论：

- 新协议可检查到 `scheduled_topology_refresh_gap` 和 `scheduled_capability_refresh_gap`。
- `templates/state.md` 已有 topology/capability 复盘字段，`docs/runtime-skill-management.md` 已改为事件触发优先、3 轮兜底上限。

## Scenario 3: Goal 停在旧版本或一轮完成后停止

用户提示：

```text
连续节拍推进这个项目，当前已经从 v32 走到 v38。
```

旧风险：

- 长期目标摘要或工具 Goal 仍写 v32，实际工作已到 v38。
- round_goal 完成后，模型把整个长期目标标成 complete，导致 next_route 没有继续触发。

新期望：

- 每轮开始运行 `goal_refresh_gate`。
- 区分 active_goal_summary、工具 Goal、round_goal 和 next_route：长期方向服务持续会话，工具 Goal 默认服务本轮 Loop。
- 若目标摘要或工具 Goal 与 current_basis、版本号、next_route 或交付对象不一致，标记 `stale_goal`，迁移到新目标或写 `protocol_round_goal`。
- round_goal 完成只更新本轮，不自动结束 continuous route。

模拟结论：

- 新协议可检查到 `fake_goal_drift_gap`。
- `templates/state.md` 和 `templates/loop.md` 已增加 goal_refresh_status、stale_goal_check、round_goal 和 next refresh trigger。

## Scenario 4: 证据填充型任务不增加发散负担

用户提示：

```text
按 Complex 推进这个数据审计任务，模型和指标表已经确定，只需要补齐来源和验证。
```

旧风险：

- 新增模型发现机制后，模型为了“完整”强行展开 3-5 个研究框架，反而增加无效流程。

新期望：

- `project_nature_router` 判定为 `evidence_fill`。
- 记录 `divergence_noop_reason`：模型、指标和表格已定。
- 直接进入 current_basis、evidence_matrix、source_authority、validation 和 delivery_contract。

模拟结论：

- 模型发现层不会把证据填充型任务拖重。
- Runtime Kit 可只用 `state.md`、`evidence.md`、`loop.md` 和 `delivery.md`，不强制填写完整 `framing.md`。

## Scenario 5: 模型发现型任务不直接证据填表

用户提示：

```text
这是模型发现型任务，研究框架还没定。先不要证据填表，请先发散研究框架。
```

旧风险：

- 模型把“找资料”“补证据”“选工具”当成主线，过早进入熟悉的审计流程。

新期望：

- `project_nature_router` 判定为 `model_discovery`。
- 先运行 `anti_premature_convergence_gate`、`ibis_argument_map_gate` 和 `thought_search_gate`。
- 输出 3-5 个候选框架、核心假设、支持/反对理由、可区分证据和最小探针。
- 未形成候选池前，局部资料缺口不能成为主目标。

模拟结论：

- 新协议可检查到 `premature_convergence_greedy_gap`、`evidence_audit_overrouting_gap`、`model_discovery_underprotected_gap` 和 `argument_map_missing_gap`。
- Runtime Kit 由 `templates/framing.md` 和 `templates/argument.md` 承接。

## Scenario 6: 混合型任务先发散后切换证据审计

用户提示：

```text
我想先确定研究解释框架，再用文献和数据支撑它。
```

旧风险：

- 要么一直发散不落地，要么过早把第一个框架当成结论后开始填材料。

新期望：

- `project_nature_router` 判定为 `mixed`。
- 收敛前按 model_discovery 权重评分：问题定义、候选多样性、反例、可区分探针和延迟收敛质量。
- 满足 convergence_switch_conditions 后，记录 switch_reason，并切回 evidence_fill 权重。

模拟结论：

- Complex 可以在“发现模型”和“审计证据”之间切换，不把二者混成同一个贪心循环。

## Scenario 7: 无事件触发时能力复查不机械打断

用户提示：

```text
连续节拍继续，本轮仍是同一主链，没有新增工具或交付对象变化。
```

旧风险：

- 每到固定轮次就完整复查工具、线程和 Goal，稀释本轮任务注意力。

新期望：

- `event_triggered_capability_refresh` 检查是否出现项目性质、主链、证据路径、材料类型、外部边界、子线程职责或交付对象变化。
- 若无触发，记录 `lightweight_keep`。
- 3 轮兜底只做轻量 fit check；发现真实不匹配时才加深。

模拟结论：

- 新协议可检查到 `mechanical_cadence_overhead_gap`。
- 连续节拍保持可恢复，但不把复盘变成常规打断。

## Scenario 8: 用户只说“按 Complex 动态推进”

用户提示：

```text
按 Complex 动态推进，让 AI 自己判断细节。
```

旧风险：

- 模型把“动态推进”理解成完全自由发挥，或者反过来每个细节都回问用户。
- 路线、工具、分工和深度变化没有留下理由，后续恢复时只能看到结果，看不到判断边界。

新期望：

- 先启用 `adaptive_judgment_controller`，默认 `autonomy_level: strong_autonomy_with_guardrails`。
- 可逆、低副作用、项目内的计划细节、Loop 探针、证据深度、能力取舍和临时分工由 AI 自行决定。
- 若涉及主目标、授权、外部写入、不可逆动作、交付公开口径或高风险主张，触发 `ask_user_needed`。

模拟结论：

- 新协议可检查到 `adaptive_judgment_absent_gap`、`over_asking_user_for_reversible_detail_gap` 和 `unsafe_autonomy_without_guardrail_gap`。
- Runtime Kit 由 `templates/judgment.md`、`templates/state.md` 和 `templates/loop.md` 承接判断模式和回问边界。

## Scenario 9: 模型发现任务中 AI 自行延迟证据填表

用户提示：

```text
这个研究还没定框架，按 Complex 推进。
```

旧风险：

- 模型为了显得“有进展”，直接开始检索资料和补 evidence matrix。
- 用户没有明确说“不要早收敛”时，模型没有主动保护发散空间。

新期望：

- `project_nature_router` 判定为 `model_discovery` 或 pre-convergence `mixed`。
- `adaptive_judgment_controller` 选择 `judgment_mode: exploratory`。
- AI 自行延迟证据填表，先建立候选框架、问题-观点-论据图和可区分探针，并记录 `ai_decided_without_user_reason`。

模拟结论：

- 新协议可检查到 `model_discovery_underprotected_gap` 与 `evidence_audit_overrouting_gap`。
- “先发散”不依赖用户说出准确关键词，AI 可以根据项目性质自行判断。

## Scenario 10: 连续节拍无事件变化时 AI 自行 lightweight keep

用户提示：

```text
继续下一拍，当前路线没变。
```

旧风险：

- 固定轮次触发完整工具、线程和目标复查，导致本轮注意力被流程抢走。

新期望：

- `adaptive_judgment_controller` 检查 route_event、项目性质、证据路径、材料类型、外部边界、子线程职责和交付对象。
- 若无变化，AI 自行决定 `lightweight_keep`，只写短理由和 next refresh trigger。
- 不把 3 轮兜底误解成每 3 轮强制完整复盘。

模拟结论：

- 新协议可检查到 `mechanical_deep_judgment_gap` 和 `mechanical_cadence_overhead_gap`。
- 连续节拍保留恢复感，但不牺牲推进效率。

## Scenario 11: 长期分线程职责失配时 AI 微调职责

用户提示：

```text
继续多线程推进，主线已经从资料审计转到模型方案选择。
```

旧风险：

- 长期分线程仍按旧职责输出，主线程被迫手动纠偏。
- 模型认为任何线程职责变化都必须先问用户，造成不必要的等待。

新期望：

- `adaptive_judgment_controller` 判断这是可逆、低副作用的职责微调，而不是主目标改变。
- AI 可自行把旧“资料审计线程”调整为“候选框架反例审查线程”，同时写清 `ai_decided_without_user_reason` 和 `recovery_route`。
- 若线程需要外部账号、写入仓库、发布或不可逆操作，再触发用户授权。

模拟结论：

- 新协议把长期线程职责复查从机械流程改成事件触发的深层判断。
- `templates/judgment.md` 能记录 keep / adjust / pause / close / replace 的理由和回滚路线。

## Scenario 12: 账号/API/外部写入触发回问

用户提示：

```text
继续推进，必要时可以用外部 API 和发布平台。
```

旧风险：

- “强自治”被误解成可直接登录、写入、发布或产生费用。

新期望：

- `decision_rights_matrix` 把账号、API 写入、付款、发布、提交、评论和外部系统修改列为 `ask_user_needed` 或 `manual_action_required`。
- AI 可以先做只读分析、沙盒计划、dry-run 或需要用户操作的具体说明。
- 缺授权时不得越权执行。

模拟结论：

- 新协议可检查到 `unsafe_autonomy_without_guardrail_gap`。
- 强自治不是最大自治；它是“项目内细节自治 + 高风险边界回问”。

## Scenario 13: 重要路线切换后记录误判风险和回滚

用户提示：

```text
我们从证据审计切到模型发现，再决定是否回到数据验证。
```

旧风险：

- 模型切路线后只给新计划，不说明为什么拒绝旧路线，也没有恢复路径。

新期望：

- 这是 `judgment_mode: strategic`。
- 启用 `route_evaluator_reflection_gate`，记录 selected route、rejected route、why_selected、highest_misjudgment_risk、counterexample_or_hostile_case 和 rollback_or_recovery_route。
- 若新路线失败，可以回到旧证据路径或重新进入候选框架池。

模拟结论：

- 新协议可检查到 `route_reflection_missing_gap`。
- 重要动态判断既有自治，也有可恢复的判断证据。

## Scenario 14: 规则太密时先回到行为内核

用户提示：

```text
完整扫描 Complex 后推进，但不要被协议术语带偏。
```

旧风险：

- 模型列出大量 gate、router、controller 和模板字段，却没有形成可执行主线。
- 新项目代理知道“规则很多”，但本轮不知道先恢复状态、判断性质、划清决策权还是跑工具。

新期望：

- 先启用 `complex_behavior_kernel`，用 7 个行为压缩本轮主线。
- 机制名只作为实现细节：先行为内核，再 project_nature、adaptive judgment、Loop、交付和恢复。
- 若新增规则不能映射到行为内核，默认进入经验库、样例或 backlog，不进入主协议主体。

模拟结论：

- 新协议可检查到 `rule_density_attention_overload_gap`、`behavior_regression_missing_gap` 和 `golden_example_missing_gap`。
- `docs/behavior_regression_cases_20260702.json` 与两个黄金样例把“写进协议”推进到“能被新代理模仿和检查”。

## Overall Result

本轮修复把用户体验问题转成 25 个可触发机制：

1. `protocol_scan_sequence`
2. `complex_prompt_bootstrap_gate`
3. `round_prompt_rehydration_gate`
4. `continuous_cadence_refresh_gate`
5. `scheduled_topology_capability_review`
6. `goal_refresh_gate`
7. `per_round_goal_lifecycle_gate`
8. `plan_mode_full_scan_coverage`
9. `complex_setup_question_card`
10. `user_visible_trigger_guide`
11. `core_goal_plan_loop_required`
12. 内部工作力度/风险升级，替代用户侧普通/重大模式选择
13. `project_nature_router`
14. `anti_premature_convergence_gate`
15. `ibis_argument_map_gate`
16. `thought_search_gate`
17. `event_triggered_capability_refresh`
18. `adaptive_judgment_controller`
19. `decision_rights_matrix`
20. `judgment_depth_ladder`
21. `route_evaluator_reflection_gate`
22. `complex_behavior_kernel`
23. `behavior_regression_pack`
24. `golden_runtime_examples`
25. `mechanism_layering_map`

这些机制默认不新增 verifier required 字段；它们先作为主协议行为规则、Runtime Kit 模板字段和发布包能力项存在。若后续真实项目继续暴露同类问题，再考虑把其中稳定可检查的字段纳入恢复链验证器。
