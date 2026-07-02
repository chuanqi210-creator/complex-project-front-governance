# Complex Usage Friction Fix 2026-07-01

本轮来源：用户在其他项目中使用 Complex 时反馈，模型仍会漏读协议、连续节拍中不复盘长期分工和外部工具、Plan 模式没有完整吸收 Complex、Goal 模式出现粗糙目标或旧版本目标漂移。后续追加反馈指出：Complex 对证据填充/审计型任务较强，但对模型、研究框架和解释路径未定的任务容易过早收敛；再进一步的问题是，协议虽然有动态路由，但 AI 还不够会自行判断路线、深度、工具、分工、发散/收敛节奏和何时回问用户。

## 修复判断

这些问题不是“Complex 没有相关思想”，而是缺少更明确的运行触发、项目性质判断、反早收敛保护和自适应深层判断层。尤其是连续节拍中，初始选择的子代理、长期线程、工具和 Goal 很容易随着项目阶段变化而过期；但机械固定复盘也会打断思考，所以当前做法改为事件触发优先、3 轮兜底上限，并默认采用“强自治 + 护栏”：可逆、低副作用、项目内的细节由 AI 自行判断，高风险或授权边界才回问用户。

## 写回内容

- 主协议新增 Complex 读取顺序与关键词触发表。
- 主协议新增 `complex_behavior_kernel`，把厚协议压缩成 7 个稳定行为，作为新代理读取 Complex 的第一优先级。
- 连续任务节拍新增 `continuous_cadence_refresh_gate`，采用事件触发优先、3 轮兜底上限的拓扑、能力和 Goal 复查。
- `capability_discovery_cadence_gate` 增加 `event_triggered_capability_refresh`，避免无事件时机械打断。
- 主协议新增 `project_nature_router`、`anti_premature_convergence_gate`、`ibis_argument_map_gate` 和 `thought_search_gate`，把证据填充型、模型发现型、混合型和执行交付型分开治理。
- 主协议新增 `adaptive_judgment_controller`、`decision_rights_matrix`、`judgment_depth_ladder` 和 `route_evaluator_reflection_gate`，让 AI 能自行处理可逆细节、动态调路线，并在战略或关键判断时留下误判风险和回滚路线。
- `persistent_thread_orchestration_contract` 增加长期线程职责复核。
- `protocol_onboarding_comprehension_gate` 增加 Plan 模式完整扫描要求。
- 新增 `goal_refresh_gate`，区分 active_goal_summary、工具 Goal、round_goal 和 next_route。
- 失败模式库新增 protocol scan、scheduled topology/capability refresh、Plan full scan undercoverage 和 fake goal drift。
- Runtime Kit 状态、Prompt、Loop 与新增 Judgment 模板增加 round_index、event-triggered refresh、project_nature、convergence_status、candidate_frameworks、discriminating_probe、judgment_mode、autonomy_level、decision_right、ask_user_needed 和 recovery_route 字段。
- 新增行为回归包和两个黄金样例，优先验证入口行为和运行现场，而不是继续增加空字段。
- 发布包同步新增相关能力项。

## 本轮不做

- 不新增 verifier required 字段。
- 不新开长期机器看版。
- 不把 3 轮兜底变成用户负担或机械全量复盘；无事件触发时只写 lightweight keep。
- 不把模型发现层变成每个任务的新表格负担；证据填充型任务可以写明 `divergence_noop_reason` 后保持轻量推进。
- 不把自适应判断层变成每轮大表格；只有战略或关键判断才需要 `route_evaluator_reflection_gate`，常规 fast 判断保留简短理由即可。

## 验证

模拟记录见 `docs/complex_runtime_cadence_simulation_20260701.md`。
