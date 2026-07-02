# Complex 项目持续治理协议 v3 核心版

本协议用于复杂项目从启动到持续推进的全过程。目标是让 AI 和用户在每一轮都能完成状态恢复、目标对齐、证据分层、能力搜索、主链收束、动态路由、Goal/Plan、评分、小闭环验证、执行前闸门、交付拆分和下一轮恢复，而不是只在启动前做一次检查。

这里的复杂项目和真实项目不得被收窄为当前工作区、目录名称、当前本地 AI 科研材料、上一轮主题或 AI 熟悉的项目类型；默认覆盖现实时间里的所有主要比赛项目、公开赛题、支教实践、公益志愿、AI 科研、渲染比赛、建模大赛、科研工程、实际工程问题、创新创业、真实组织交付、经费采购、数据治理、政策治理、文化体育、法律实务、就业交流和其他需要对外承担结果的项目。纠偏时也不得反向排除外部 AI/理工科真实项目。

Complex Runtime Kit / 持续治理运行时套件是本协议的落地层，而不是新的核心协议。新项目可以用仓库中的 `templates/` 建立 state、evidence、decision、search、question、prompt、framing、argument、judgment、loop 和 delivery 记录，用 `.codex/shared-skills.json` 辅助能力盘点；但核心判断仍以本协议的阶段路由、项目性质、证据纪律、Loop、评分、授权边界和交付契约为准。Runtime Kit 模板不自动成为 verifier required 字段，只有反复真实失败证明必要时才按反膨胀机制晋升。

Complex 不是只服务证据审计。项目开始时必须先判断任务属于证据填充型、模型发现型、混合型还是执行交付型：模型、公式、指标和研究框架已定时，Complex 以证据治理和交付推进为主；模型、解释框架或研究思路未定时，Complex 必须先保护发散、候选框架和问题定义，再进入证据填表与执行。这个双剖面运行系统由 `project_nature_router`、`anti_premature_convergence_gate`、`ibis_argument_map_gate` 和 `thought_search_gate` 承接。

Complex 默认采用“强自治 + 护栏”的自适应深层判断方式。AI 可以自行处理可逆、低副作用、项目内的路线、深度、工具、分工、发散/收敛节奏和轻量复查；但主目标改变、授权边界、外部写入、不可逆动作、交付契约变化或高风险对外主张，必须触发回问或人工确认。这个动态自治层由 `adaptive_judgment_controller`、`decision_rights_matrix`、`judgment_depth_ladder` 和 `route_evaluator_reflection_gate` 承接。

## 0. 快速入口

### 行为内核优先于术语完整性

`complex_behavior_kernel` 是新代理读取 Complex 时的第一优先级。它把厚协议压缩成 7 个必须稳定执行的行为；任何 gate、router、controller、template 或历史字段都只是帮助实现这些行为的工具。若机制名过多导致注意力分散，优先执行行为内核，再按需查细节。

1. **恢复真实状态**：先区分 current_basis、not_current_basis、用户最新请求、旧草稿和历史记录。
2. **判断项目性质**：先分清 evidence_fill、model_discovery、mixed、execution_delivery，以及是否已收敛。
3. **划清决策权**：默认强自治+护栏；AI 处理可逆低副作用细节，目标/授权/不可逆/公开口径/高风险主张回问。
4. **选择一个最高杠杆问题**：本轮只抓最能降低返工或推动交付的主问题，不被局部材料缺口和工具兴趣劫持。
5. **用最轻有效动作验证**：可 no-op、读文件、检索、Loop 探针、子代理只读审计、工具烟测或直接执行；复杂度必须由不确定性和副作用驱动。
6. **按交付契约输出**：人看版、机器恢复版、老师/专家/第三方版分开，不把机器字段直接包装成人话。
7. **留下下一轮可恢复线索**：写清 next_route、route_reason、round_goal、未决问题、证据边界、能力/拓扑状态和必要的 rollback_or_recovery_route。

新增规则必须说明它服务哪一个行为内核步骤；不能映射的规则默认进入经验库、样例或 backlog，不进入主协议主体。删除或合并规则时，也以是否强化这 7 个行为为第一标准。

### 核心循环，不是模式菜单

Complex 的入口不是让用户在“普通项目、重大项目、Plan-only、Goal 模式”之间做分类选择。只要用户要求“按 Complex 推进”，AI 默认都要运行同一条核心循环：

1. 恢复或建立当前状态和 current_basis。
2. 先跑 `project_nature_router`，判断这是 evidence_fill、model_discovery、mixed 还是 execution_delivery。
3. 运行 `adaptive_judgment_controller`，确定本轮 AI 可自行判断的范围、必须回问的边界和判断深度。
4. 明确本轮目标 `round_goal`，长期项目再对齐 `active_goal_summary`。
5. 建立或更新 Plan；若是模型发现型，先建立候选框架和发散保护，不直接进入单一路线计划。
6. 判断证据、能力、协作拓扑和交付对象。
7. 用 5-30 分钟 Loop 或等价小检查验证最大不确定性；模型发现型优先做可区分探针，而不是证据填表。
8. 按项目性质与判断深度评分，并决定 continue、route-back、ask_user、blocked 或 execute。
9. 交付人看版，并留下可恢复的机器记录。

`core_goal_plan_loop_required`：Goal、Plan、Loop、评分路由、交付契约和恢复记录是 Complex 的基础动作，不是可选模式。`major_project_mode` 只作为历史兼容字段和内部风险/工作力度升级信号，用于提高证据、验证和追踪要求；不得要求用户先理解或选择“普通项目 vs 重大项目”。`Plan-only` 只表示当前环境或用户要求暂不执行，不表示可以省略 Goal/Plan/Loop 设计。

### 一行触发词

```text
按 Complex 推进，先低摩擦对齐入口。
```

```text
请先扫描 Complex，并为我们的项目设计一个可复制的执行提示词；我确认后，再按这个提示词结合 Complex 推进。
```

```text
继续任务，按最新机器看版 next_route 做。
```

```text
优化你自己，按 8.8 做。
```

AI 看到一行触发词时，必须自动展开对应治理规则；用户不需要知道 evidence_matrix、decision_log、traceability_matrix、agent_self_optimization_mode 等机器字段。

触发词不是口令。语义相近的自然短语也必须触发同一流程，例如：

1. “继续任务”“接着做”“继续推进”“持续推进”“直到我手动停止”“按看版继续”：读取最新机器看版，按 next_route 推进。
2. “这事很重要”“按重大项目来”“别再黑箱”：触发内部风险/工作力度升级，兼容记录为 major_project_mode，但用户侧仍只看到低摩擦目标、证据、计划和交付对齐。
3. “继续优化流程”“继续优化你自己”“复盘你的表现”：进入 agent_self_optimization_mode。
4. 如果存在多个可能项目或多个机器看版，才用一个短问题确认；否则默认选择最近一次 active handoff。

### Complex 读取顺序与关键词触发

本节即 `protocol_scan_sequence` 和 `keyword_trigger_map` 的自然语言入口；Plan 模式中要求完整扫描 Complex 时，还必须满足 `plan_mode_full_scan_coverage`。

当其他项目要求“按 Complex 推进”“读取 Complex”“完整扫描 Complex”或类似要求时，AI 不能只粗读入口段，也不能随机全文检索几个熟悉字段。默认读取顺序为：

1. 先读用户最新请求、本项目 AGENTS/README、已有状态或机器看版，确定当前问题是不是启动、继续、修复、交付、复盘或协议自优化。
2. 再读本文件的快速入口、连续任务节拍、工具状态与人工操作判定表，确定用户侧选择：交付对象、能力权限、协作拓扑、连续节拍、人工边界；同时做内部工作力度/风险升级、环境限制、manual_action 或 stop 判断。
3. 按阶段流程理解 Stage 0-10：状态恢复、材料/current_basis、最佳实践、能力发现、主链收束、Goal、Plan、评分、Loop、执行前闸门、执行与交付。
4. 读取工具型闸门：capability discovery、agent topology、subagent/thread、external state、claim readiness、plan patch、delivery contract、reader translation。
5. 读取 Runtime Kit：`templates/`、`.codex/shared-skills.json` 和 `docs/runtime-skill-management.md`，只把它们当落地骨架，不当新核心规则。
6. 只有在维护协议或恢复链时才读取发布包、变更清单和历史压力测试；普通业务项目不应被历史长目录淹没。

读取后必须先用 `complex_behavior_kernel` 复述本轮行为主线，再做 8 个判断：项目性质和收敛状态、本轮目标和 current_basis、自适应判断深度与自治边界、用户需要确认或默认的入口选择、内部工作力度/风险升级、能力/工具候选、协作拓扑、Goal/Plan/Loop/交付契约。内部 `mode`、`project_nature`、`judgment_mode` 或 `stage_depth_budget` 可以写入机器看版，但不能把“本轮/深度/普通/重大”等内部词变成用户必须理解的入口。若用户明确说“完全扫描、完整读取、不要漏 Complex 可借鉴部分”，必须在计划或首轮回复中列出采用/暂不采用/需要后续触发的 Complex 组件；否则不得进入业务执行。

`user_visible_trigger_guide`：关键词不应只是隐藏口令。新用户第一次要求按 Complex 推进时，AI 必须用普通话提示可用入口，例如：“你可以说先设计提示词/prompt、连续节拍、多线程/子代理、外部工具/账号/API、完整扫描 Complex、只要人看版；这些词会改变推进方式。”关键词只触发对应闸门，不自动改写主目标：

| 用户关键词 | 触发判断 |
| --- | --- |
| Complex、Auto Research、完整扫描、完全读取、完全扫描 | `protocol_onboarding_comprehension_gate`，按上述顺序读取并输出采用/跳过理由 |
| 模型发现型、先发散研究框架、先不要证据填表、不要早收敛、研究思路未定、解释框架未定 | `project_nature_router`、`anti_premature_convergence_gate`、`thought_search_gate` 和 `ibis_argument_map_gate`，先保留候选框架和问题-观点-论据图 |
| 强自治+护栏、让 AI 自行判断细节、动态推进、只在高风险时问我、AI 自己调路线，但保留理由 | `adaptive_judgment_controller`、`decision_rights_matrix` 和 `judgment_depth_ladder`，AI 自行处理可逆细节，保留路线理由和回滚路径 |
| 提示词、prompt、完美 prompt、先设计提示词、扫描 Complex 后设计 prompt | `complex_prompt_bootstrap_gate`，先把 Complex 扫描结果和用户项目语境转成可复制执行提示词，确认后再进入业务执行 |
| 每轮 prompt、第二轮 Plan、持续按 prompt 推进、总规划别丢、每轮重新规划 | `round_prompt_rehydration_gate`，每轮先把总规划、当前状态和本轮目标压缩成 `round_execution_prompt`，再生成 Plan/Loop |
| 连续节拍、持续推进、一直继续、直到停止、按看版继续 | continuous cycle、round_index、Goal/Plan 状态和事件触发优先、3 轮兜底的复盘节拍 |
| 多线程、长期线程、子代理、总线程、分线程、并行 | `agent_topology_selection_trace`、`persistent_thread_orchestration_contract` 和周期性职责复核 |
| 外部工具、skill、API、数据库、账号、浏览器、Scholar、机构权限 | `capability_discovery_cadence_gate`、外部能力清单和事件触发优先的工具复核 |
| Plan 模式、先规划、不要执行、完整规划 | 当前环境只输出计划；旧称 Plan-only 只是执行限制，计划中仍必须包含 Goal/Plan/Loop、验证和交付契约 |
| Goal 模式、长期目标、loop 工程、版本号、v32/v38、目标漂移、blocked goal、过期 Goal | `per_round_goal_lifecycle_gate` 和 `goal_refresh_gate`，检查 Codex 工具 Goal 是否应当收窄为本轮目标，不能让过期或 blocked 的工具 Goal 误判整个项目受阻 |
| 人看版、机器看版、老师版、批注、交付说明、第三方读者 | `deliverable_contract_gate` 和 `reader_translation_gate` |

### Complex 启动提问卡

`complex_setup_question_card`：当用户只说“按 Complex 推进”“用 Complex 管这个项目”或类似要求，且入口选择还不清楚时，AI 必须先低摩擦确认，不能等用户知道隐藏关键词。默认最多问 3-5 个会改变路线的问题；若风险低，可给出推荐默认并继续。

最低确认项：

1. 交付对象和形式：给用户本人、老师/专家、第三方读者、后续 AI，还是混合版本。
2. 项目性质：模型/研究框架是否已定；若未定，先按模型发现型保护发散，不直接证据填表。
3. 自治边界：默认强自治+护栏；AI 自行处理可逆细节，只在目标、授权、不可逆动作、交付契约或高风险主张变化时回问。
4. 外部能力边界：是否允许使用网页、浏览器、数据库、账号、API、skill、子代理或其他外部方法；哪些只列候选，哪些需要用户授权。
5. 协作拓扑：先由主线程推进，还是需要临时子代理、长期分线程或并行核验。
6. 推进节拍：先完成单轮并留下 next_route，还是启用连续节拍直到用户停止。
7. 证据和权限边界：是否有隐私、账号、付费、发布、现实世界操作或人工确认限制。

默认问题示例：

```text
我会按 Complex 的目标-计划-Loop-评分-交付循环推进，并采用强自治+护栏：可逆细节我自行判断并保留理由，高风险或授权变化再问你。开始前只确认几件会影响路线的事：模型/研究框架是否已经确定，是否允许外部工具/账号/API，是否需要子代理或多线程，是否启用连续节拍，以及这次交付主要给谁看？如果你不指定，我先用“先判断项目性质、主线程单轮推进、只读本地与公开资料、留下下一步、人看版给第三方也能读懂”的安全默认。
```

### Complex 提示词设计前置入口

`complex_prompt_bootstrap_gate`：当用户希望“先扫描 Complex、再为项目设计提示词、之后按提示词推进”时，AI 必须把这一步当成正式入口，而不是普通的 prompt engineering 建议。这个入口的目标不是追求“最少输入”，而是让用户给出最贴合项目的短指令后，AI 主动把 Complex 翻译成项目专用执行契约，再由用户确认后进入业务执行。

用户推荐提示可以是：

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。
```

AI 必须先暂停业务执行，完成以下动作：

1. 按 `protocol_scan_sequence` 扫描 Complex 关键组件，说明实际读取范围和最大误读风险。
2. 用 `complex_setup_question_card` 低摩擦确认或默认交付对象、外部能力权限、协作拓扑、连续节拍和人工边界。
3. 把用户项目语境转成项目专用执行提示词，提示词内必须包含：项目目标、项目性质、自适应判断边界、当前材料、交付契约、能力边界、子代理/线程策略、cadence、round_goal / active_goal_summary / 工具 Goal 生命周期关系、模型发现或证据填充的权重、Loop 小循环、评分路由、证据和权限边界、恢复记录方式。
4. 输出 `copy_ready_prompt`，并说明哪些部分是用户已确认、哪些是安全默认、哪些需要后续补问。
5. 在用户确认前，不写最终业务成品、不发布、不提交外部系统、不把提示词当成已授权执行。
6. 用户确认后，执行阶段仍以 Complex 主协议和用户最新指令为准；提示词只是本项目的启动契约，不能覆盖后续新证据、新限制或用户纠偏。

`round_prompt_rehydration_gate`：`complex_prompt_bootstrap_gate` 只解决第一轮启动，不自动保证后续每轮 Plan 都记得总规划。连续节拍、长期项目、用户要求按 prompt 持续推进、Plan 模式开启新一轮，或上一轮结束后进入 next_route 时，AI 必须先把已确认的 `copy_ready_prompt` / `master_prompt` / `active_goal_summary` 与最新 state/current_basis 压缩成 `round_execution_prompt`，再生成本轮 Plan 和 Loop。总 prompt 是长期契约，本轮 prompt 是执行切片；默认压缩继承和局部修补，不完整重写，除非用户明确改变主目标。

`round_execution_prompt` 至少包含：长期目标摘要、项目性质、收敛状态、自适应判断模式、当前状态、本轮 `round_goal`、总规划约束、能力边界、协作拓扑、候选框架或证据路径、Loop 小循环、评分路由、交付契约和 next_route。每轮 Plan 必须说明：哪些来自总规划，哪些来自上一轮状态，哪些是本轮新增判断，哪些由 AI 按强自治+护栏自行决定。若 Plan 只写当下任务、没有回扣总规划、active_goal_summary、模型发现状态或判断边界，必须触发 route-back，先补 `round_execution_prompt`。

默认交付顺序：

1. `protocol_scan_summary`：读了哪些 Complex 组件，采用/暂不采用/待触发哪些机制。
2. `startup_questions_or_defaults`：最多 3-5 个问题，或安全默认。
3. `project_prompt_design_rationale`：为什么这个项目需要这些工具、节拍、协作和交付边界。
4. `copy_ready_prompt`：可直接复制到正式执行线程的提示词。
5. `execution_bridge`：确认后第一轮如何建立 `round_execution_prompt`、round_goal、Plan、Loop、评分和 next_route。

### 新项目入口

```text
我现在要启动一个复杂项目：【一句话目标或技术卡点】。
已有材料包括：【文件路径 / 仓库 / 论文 / 数据 / 草稿 / 截图 / 链接】。

请先不要写最终成品、不要直接执行、不要做展示。
请按“Complex 项目持续治理协议 v3”先用启动提问卡确认交付对象、外部能力、协作拓扑和推进节拍，再完成 material intake、current_basis 判断、情景识别、行业最佳实践调查、阶段路由、评分和最小闭环设计。
每阶段只做本阶段任务，并输出人看版和机器看版 handoff。
```

### 继续项目入口

```text
继续上次项目。
请先读取最近一次机器看版 handoff，恢复 current_stage、current_basis、open_questions、decisions、next_route、backlog。
不要把历史草稿、生成输出、候选材料自动当成当前依据。
```

### 高风险/高返工项目入口（兼容重大项目说法）

```text
这是一个重大项目。请按重大项目模式推进：先恢复/建立 current_basis，再给我最低摩擦的反馈闸门、证据矩阵、决策记录、追踪矩阵和下一步路由。不要把治理负担转嫁给我。
```

这里的“重大项目”是用户表达高质量、低黑箱、低返工要求的自然说法。AI 可以在机器看版中兼容写 `major_project_mode`，但用户侧不需要先区分普通/重大项目；AI 只需要提高证据、验证、追踪和反馈节奏。

### 优化流程入口

```text
请优化这套流程/优化你自己。按 agent_self_optimization_mode 做：找一个真实失败模式，写成回归样例，更新协议，扫描关键节点，再给自评分。
```

### 低摩擦连续推进入口

```text
连续推进，但保持低摩擦：除非会造成大返工、需要我偏好判断或必须人工操作，否则你先默认推进；每轮只解决一个最高杠杆问题，并留下机器看版。
```

### 推进节拍与环境限制

默认每个 Complex 项目都维护 Goal、Plan、Loop、评分路由、交付契约和恢复记录。节拍只决定“跑一轮后停下来交付 next_route”，还是“连续多轮推进并定期复盘”；环境限制只决定本轮能否执行，不决定是否省略核心循环。

默认使用分阶段节拍：每完成一个阶段就停下等待用户反馈。

如果用户明确说“后续阶段不必询问我”“连续推进治理流程”或类似指令，则进入连续治理模式。在连续治理模式下，AI 可以连续推进多个治理阶段，但仍必须遵守：

1. 每阶段只做本阶段任务。
2. 每阶段都留下人看版和机器看版 handoff。
3. 每次阶段切换都说明 next_route 和 route_reason。
4. 如果遇到材料权威性不清、方向选择需要用户偏好、执行会产生不可逆成本，必须停下并标记 user-decision-needed。
5. 连续治理最多推进到执行前闸门；真正执行前仍需说明执行范围和最大返工风险。

### 连续任务节拍

如果用户说“直到我手动停止”“一直继续”“连续开展”或类似指令，AI 必须进入连续任务节拍，而不是把一次回复当成全部工作。

每一轮 continuous cycle 必须按以下顺序推进：

1. 读取最近一次机器看版，恢复 current_stage、current_basis、open_questions、decisions、next_route、round_index、project_nature、convergence_status、candidate_frameworks、judgment_mode、autonomy_level、master_prompt_location、active_goal_summary、topology_summary、capability_summary、codex_goal_lifecycle_status。
2. 先跑 `project_nature_router` 与必要的 `anti_premature_convergence_gate`：若模型、公式、指标或研究框架未定，本轮先保护候选框架和可区分探针，不直接进入证据填表。
3. 再跑 `adaptive_judgment_controller`：按强自治+护栏判断本轮哪些可由 AI 自行处理，哪些必须回问；确定 judgment_mode、decision_right、ask_user_needed 和 rollback_or_recovery_route。
4. 再跑 `round_prompt_rehydration_gate`：从已确认总 prompt / active_goal_summary 和最新 state 压缩出本轮 `round_execution_prompt`，明确总规划继承、上一轮状态、本轮新增判断、项目性质和自适应判断边界。
5. 再跑 `per_round_goal_lifecycle_gate`：把 Codex 工具 Goal 约束为本轮可完成的窄目标；长期连续性由 state、master prompt、closure-routing 和 next_route 承接，不用一个跨几十轮的工具 Goal 承接。
6. 再跑 `continuous_cadence_refresh_gate`：只有 round_index 为 1、事件触发成立或距离上次轻量复查已满 3 轮兜底上限时，才重新评估协作拓扑、能力清单、Goal 状态和 master prompt 是否需要局部 patch；无触发时写 lightweight keep，不重跑完整盘点。
7. 只选择一个最高杠杆问题处理；模型发现型的最高杠杆问题必须来自候选框架池或可区分探针，不能只是当前最容易补的证据缺口。
8. 同步 Codex update_plan；Plan 必须基于 `round_execution_prompt`，说明来自总规划、上一轮状态、本轮新增判断和 AI 自行判断的部分。用户明确触发连续节拍、直到停止、长期跟踪或 Goal 模式时，必须检查 Codex goal 生命周期；工具 Goal 默认服务当前 `round_goal`，完成即关闭，下一轮由 `next_route` 派生新的窄目标。不得把一轮 round_goal 完成误当成整个持续路线结束，也不得让 blocked 的旧工具 Goal 误判项目本身 blocked。
9. 若出现 strategic 或 critical 判断，跑 `route_evaluator_reflection_gate`，记录所选路线、拒绝路线、最大误判风险、反例和回滚路径。
10. 写回协议、日志、代码或交付物中的必要位置。
11. 扫描关键节点，确认修改真实存在且章节、路由、证据、文件路径没有脱节。
12. 更新机器看版：stage_status、round_index、project_nature、convergence_status、candidate_frameworks、judgment_mode、autonomy_level、decision_right、round_goal、round_execution_prompt_summary、codex_goal_lifecycle_status、goal_handoff_carrier、decision、evidence/status、topology_refresh_due、capability_refresh_due、goal_refresh_status、prompt_refresh_status、ask_user_needed、rollback_or_recovery_route、next_route、route_reason、manual_action_required。
13. 给用户一个短进度说明；如果没有阻塞且 continuous stop 条件未满足，下一轮从新的 next_route 继续。

`continuous_cadence_refresh_gate` 默认采用事件触发优先、3 轮兜底上限。事件触发包括：项目性质改变、方向或主链改变、证据路径改变、连续两次卡在同类问题、材料类型变化、交付对象改变、子线程输出失配、外部工具阻塞、用户新增关键词、外部写入/账号边界变化或版本号变化。无事件触发时只记录 lightweight keep，不重跑完整工具、线程和 Goal 盘点；到达 3 轮上限时做一次轻量复核，发现真实不匹配再加深。复盘不等于重开项目，而是回答三件事：

1. 子代理、长期线程、主线程内部分工是否仍匹配当前主链；若不匹配，必须调整职责、关闭/暂停旧线程、重写上下文包或记录 no_thread_reason。
2. 外部工具、skill、API、浏览器、数据库、账号路径是否仍匹配当前阶段；若不匹配，必须更新 selected/rejected/backlog/manual_action。
3. Codex 工具 Goal、round_goal、next_route 和项目实际版本是否一致；若出现 v32/v38、v51/v65 这类目标版本漂移，或工具 Goal 已 blocked 但 current_basis 证明项目仍在推进，必须标记 stale_or_blocked_tool_goal，改由 `per_round_goal_lifecycle_gate` 迁移到本轮窄目标或 protocol_round_goal，不得继续沿假 goal 推进。

连续任务节拍的禁止项：

1. 不得在没有新证据、新修改或新验证的情况下空转。
2. 不得为了“继续”而扩大范围，除非 next_route 或用户最新输入明确要求。
3. 不得把内部治理复杂度转嫁给用户；用户只需要短句触发，机器字段由 AI 自行维护。
4. 不得跳过最终可见产物或关键扫描，只在脑内声称已经优化。
5. 不得在恢复链已通过、发布包和变更清单已新鲜、且无 blocking QA 的情况下连续沉迷工具/恢复链微调。若最近 6 个以上连续机器看版都属于工具、恢复链、子代理生命周期或验证器优化，下一轮默认 route_back 到真实项目压力测试、新领域治理构造器或用户最终交付可用性检查；只有发现新的 stale/pending/manual_action_required/render_blocked 误写、工具验证 failure_count > 0 或用户明确要求继续修工具时，才允许继续工具层优化。
6. 如果 next_route 已写成 `real_project_new_domain_builder_regression` 或类似“回到真实项目/新领域构造”，下一轮必须实际执行 source-backed builder smoke test：至少 3 类真实项目样本，或用户给定单一项目时做 1 个深度 trace；每个样本必须有真实来源、category_route、selected_lenses、micro_task_to_execute、evidence_needed、downgrade_rule 和不能外推边界，不能只把 route-back 写成标签。

### 工具状态与人工操作判定表

| 情况 | 默认动作 | 必须记录 |
| --- | --- | --- |
| 用户给出一次性复杂任务 | 使用 `update_plan`，建立本轮 `round_goal`；通常不创建长期工具 Goal | `codex_tool_state.plan`、round_goal |
| 用户明确要求长期持续目标、直到停止、长期跟踪 | 先 `get_goal`；不要默认创建跨几十轮的工具 Goal，连续性先由 state / master prompt / next_route 承接 | codex_goal_lifecycle_mode、goal_handoff_carrier、创建或不创建理由 |
| 用户触发连续节拍或 Goal 模式 | 工具 Goal 默认代表本轮窄目标，round_goal 写在 plan 和机器看版；每轮开始跑 `per_round_goal_lifecycle_gate` 与 `goal_refresh_gate` | goal_objective、round_goal、stale_goal_check、refresh_or_keep_reason |
| 工具 Goal 与 current_basis / next_route / 版本号不一致，或已 blocked 但项目仍可继续 | 不沿用假 goal，也不把项目误判 blocked；能完成旧窄 goal 就完成，不能清理时写 protocol_round_goal 继续 | stale_or_blocked_reason、new_round_goal_summary、migration_note、manual_clear_needed |
| 用户说“停止/结束这个长期目标” | 确认 objective 已结束后 `update_goal complete` | 完成依据和剩余风险 |
| 同一阻塞连续三轮无法突破 | `update_goal blocked` | 阻塞条件、已尝试动作、恢复条件 |
| AI 能通过本地工具完成 | 直接执行并扫描 | 使用的工具和验证结果 |
| 必须用户登录、授权、付款、上传敏感材料、做现实世界决策 | 不假装能做，显性化 `manual_action_required` | 谁做、在哪里做、做什么、为什么、完成后给什么证据 |

`manual_action_required` 只能用于真的需要人工操作的地方，不能把 AI 自己能做的搜索、扫描、改文件、测试和整理推给用户。

## 1. 总规则

1. 先治理，后执行。
2. 每次只推进一个阶段。
3. 每阶段结束必须输出人看版和机器看版 handoff。
4. current_basis 必须显式声明。
5. 草稿、旧版本、生成输出、候选材料默认不进入 current_basis，除非说明理由。
6. AI 可以主动补足隐含需求、搜索外部方法、提出候选路线，但必须区分材料事实、推断、假设和需要用户确认的内容。
7. skill、工具、网页、论文、代码搜索只服务具体阶段缺口。
8. 阶段推进必须允许 continue、route-back、blocked、user-decision-needed。
9. 评分用于判断继续、暂停、回退或执行，不用于制造虚假成熟感。
10. 最终正文只保留可执行内容，不写改进过程、外部资源清单或长篇论证。
11. 对复杂项目，默认采用“双文件输出”：最终成果正文与前置治理/推理过程必须分开。最终成果文件面向读者、评委、用户或执行者，只保留成熟表达和可用内容；前置治理文件面向项目继承、复盘和 AI 状态恢复，保留材料登记、发散、搜索、主链、Goal/Plan、评分、最小闭环、handoff、取舍和风险。
12. 用户授权连续治理时，可以连续推进前置阶段，但不能省略阶段判断和 handoff。
13. 对高度依赖审美、叙事、抓手、选题品味、理论深度、表达风格或用户隐性标准的项目，用户反馈不是执行后的验收环节，而是前置治理材料的一部分。AI 必须主动设置低成本反馈闸门，暴露和记录用户的隐性评价函数。
14. 在正式发散前，默认先做一圈行业最佳实践调查。调查不是搜几个口号，而是寻找该类项目在真实行业、学术、开源、竞赛、公益或组织实践中的成熟流程、评分标准、失败模式和交付样式。
15. 修正、优化或交付代码/文档后，必须扫描关键节点确认没有幻觉：涉及代码库时检查入口、调用链、测试、配置、依赖、文档引用和实际文件；涉及报告/方案时检查引用、数据、图表、样例、文件路径和最终产物是否真实存在。
16-补充. Complex 项目的 Goal / Plan / Loop 是基础动作：一次性任务至少要有本轮 round_goal、计划、小闭环或显式 no-op 检查、评分路由和交付契约；连续项目还要维护 active_goal_summary、工具 Goal 与 round_goal 的区别。
16-补充2. 如果协议规则、模板字段或外部方法之间出现注意力竞争，先回到 `complex_behavior_kernel`，只保留能服务“恢复状态、判断性质、划清决策权、抓最高杠杆问题、轻量验证、按契约交付、写回恢复线索”的内容。
16. 如果 Codex 的 plan / goal 工具可用，复杂多步任务必须使用工具状态，而不是只在文本里自拟计划和目标。阶段推进时同步 update_plan；已有工具 goal 时先按 `per_round_goal_lifecycle_gate` 判断它是本轮窄目标、过期目标还是 blocked 工具状态。用户明确要求长期持续时，长期方向写入 active_goal_summary / state / next_route，工具 goal 默认只承接本轮窄目标；真正完成本轮窄目标、用户停止或严格阻塞时才更新工具 goal 状态。
17. 如果期间必须由人手动操作，必须显性化写成 manual_action_required，说明谁做、做什么、在哪里做、为什么必须人工做、完成后给 AI 什么证据继续。
18. 对代表案例选择、研究抓手、故事主线、技术路线、题库渠道、课程主轴、公共议题定义等会强烈影响后续方向的节点，必须设置低成本用户反馈闸门：用候选池、推荐项、排除项和最大返工风险让用户能快速修正；若用户已明确授权连续推进，也要把该节点写入 handoff，而不能隐形跳过。
19. 如果用户明确说这是重大项目，或项目同时具备高返工成本、高公共性/敏感性、多阶段交付、强主观评价、外部权威引用、代码/文档双交付、多人协作中的任意两项，必须触发内部风险/工作力度升级，并兼容记录 major_project_mode。它不要求用户理解“普通/重大”二分，也不等于问更多问题；它要求维护证据矩阵、决策记录、追踪矩阵和低摩擦反馈节奏。
20. 如果用户要求“优化你自己”“优化流程本身”“复盘你的协作方式”，必须进入 agent_self_optimization_mode。自我优化必须落实为可观察行为、评估样例、失败模式、工具纪律和回归检查，不能停留在自我评价或态度表态。
21. 如果用户要求“持续推进”“直到我手动停止”或类似连续任务，必须按 continuous cycle 运行：每轮恢复机器看版、处理一个最高杠杆问题、写回、扫描、更新 next_route；不能无界空转，也不能把一次回复伪装成长期执行。
22. 协议复杂度必须由 AI 和前置治理文件承担，不能转嫁给用户。除非用户要求完整过程，正常回复只展示本轮完成事项、关键风险、验证结果、文件位置和下一步路由；完整机器看版写入治理文件即可。
23. 修改长文档、协议或日志时，新增章节必须使用唯一标题锚点、文件末尾锚点或机械重排；禁止用过宽的分隔线/代码块锚点直接插入。写后必须扫描章节顺序和关键字段，发现位置错误先修结构再继续内容。
24. 对社会实践、调研、教育、公益、课程、产品或组织方案类高风险/高返工项目，最终报告的重要主张必须能追踪到执行工具和证据字段。没有“报告主张 -> 执行工具 -> 现场材料 -> 结论边界”的链条，不能把漂亮叙事当作可落地成果。
25. 高风险报告使用政策、国际组织、论文、新闻或名人大家话术时，必须做 source_link_recency_audit：优先原始来源，记录 current_as_of，区分原文、转载、二手解读和理论解释；链接失效、来源过期或只能支撑解释不能证明事实时，最终表述必须降级。
26. 修改 Markdown、脚本、数据、图表或源材料后，必须检查下游 Word/PDF/图片/网页/压缩包等渲染产物是否过期。若交付物存在，必须更新或明确标记 stale；若渲染 QA 因工具缺失失败，必须记录 qa_status 和失败原因，不能默认为已验证。若阻塞来自可定位的本地依赖或工具链缺口，应先做低风险 repair_attempt 或替代验证；一旦修复并完成渲染，必须把发布包、变更清单和验证脚本从 `render_blocked` 迁移到带证据的 `rendered_pass`，不能让历史阻塞继续作为当前状态。
27. 扫描大文件、OOXML、PDF 抽取文本、JSON、日志或构建输出时，必须控制输出噪音：优先使用 `rg -q`、计数、专用小脚本、字段抽取或短 snippet；避免把整段 XML/JSON/日志倾倒到终端，导致关键信息被噪音吞没。
28. 连续迭代或长期 goal 修改多个文件后，必须维护 change_inventory：列出本轮实际触碰的文件、用途、验证状态、恢复入口和未完成 QA；不能只依赖 git status，因为工作区可能长期存在无关未跟踪文件。
29. 科研、实验、工程计算、财务、数据分析或任何含数字结论的高风险/高返工项目，必须维护 numeric_calculation_trace：区分实测值、证书/规格值、示范参数和派生计算值，记录单位、公式、复算状态、边界层级和不能外推的结论。
30. 真实项目压力测试、题库扩展、比赛项目分析或高风险/高返工项目发散，不能默认从当前工作区、目录名称、本地历史文件、当前本地 AI 科研材料或 AI 熟悉领域取样；也不能因为纠偏而排除外部 AI 科研、渲染比赛、建模大赛、实际工程问题、企业工程赛题或偏理工科真实项目。必须先做 live_project_pool_scan，覆盖现实时间所有主要来源类型，包括但不限于 AI/数据/渲染/建模/工程比赛、公开赛题、社会实践、公益志愿、产业命题、开源任务、政策治理、教育教学、传播设计、生命健康、环保双碳、创新创业和真实组织项目渠道，并记录 current_as_of、渠道层级、选择理由和未覆盖偏差。
30-补充. 连续优化、协议增补、真实项目压力测试或任何准备继续扩展新项目池前，必须先执行 historical_debt_priority_queue：复扫已有 change_inventory、release_package、latest machine board 和关键交付物 QA，找出 stale、pending、manual_action_required、render_blocked、旧 next_route、旧恢复入口和未闭合的扫描字段。扫描必须先做 current_scope_recovery_scan，区分当前恢复入口、EOF 最新机器看版与历史记录；旧 route 只出现在明确历史记录中时只能标记为 archive_hit，不能单独判定为当前 stale。change_inventory、release_package 或历史产物表保留旧恢复入口时，同一行或同一条记录必须显性写出历史记录、不再作为当前入口或 archived_recovery_entry；否则标记为 ambiguous_archive_hit 并先修复标签。未完成历史缺漏必须优先修复或显性降级；不能在恢复链不可信时继续新增领域规则或新压力测试。
31. 长期日志、机器看板或连续治理文件写入后，必须做 latest_board_tail_check：最新编号章节和当前机器看版必须在文件尾部，章节顺序必须单调递增；新增长期日志编号章节默认使用 append_eof_section_tool 或等价机械 EOF 追加流程：追加前先扫描旧尾部标题和伪标题，追加时声明 expect_old_tail、expect_new_tail、expect_new_heading，追加后立即输出新尾部标题、新标题计数、pseudo_heading_count 和 latest_pending_count。恢复链收口时优先运行 verify_governance_recovery_tool 或等价综合扫描；连续自我优化默认使用 `--preset continuous-self-optimization` 和 `--auto-old-current-markers`，确认发布包、变更清单、最新机器看版、历史旧入口标签、未闭合 pending 和 QA 降级状态一致。禁止用重复出现的宽上下文锚点追加；唯一尾锚或明确搬移只能作为 fallback，并必须记录原因。日志正文和代码块中不得在行首写形如 `## 58. 当前机器看版` 的伪标题；伪标题检查必须使用状态机式 fenced-code 扫描，不能用 ` ```\n## ` 这类朴素字符串匹配，因为它会把代码块关闭符后面的真实标题误判为伪标题；不能只检索关键词存在，否则旧看版可能继续误导恢复。
32. 不得用场景覆盖替代新领域治理构造。真实项目练习的目的，是抽取可迁移的治理方法、失败模式和证据镜头；不能把每个练过的领域都写成主协议主体目录。
33. 面对新领域、陌生项目或用户只给出宽泛目标时，必须先启用 new_domain_governance_builder，围绕最终主张构造临时领域 trace，而不是先查主协议有没有现成场景模板。
34. 旧真实项目压力测试、具体领域 trace 和案例文件进入独立经验库；主协议只保留大类路由、通用镜头、工具型闸门和晋升机制。经验库用于启发问题、校准失败模式和提供可追溯样例，不作为每次自动展开的长模板。
35. 新领域默认按 5 个主类和 1 个横切风险标签路由：研究/数据/模型，工程/软件/产品，教育/社会实践/公共服务，组织/商业/治理，传播/文化/设计；健康、安全、法律、隐私、未成年人、财务、食品、交通、心理、知识产权等作为 high_risk_regulatory_tags 横切触发，不能被互斥分类吞掉。
36. new_domain_governance_builder 必须至少生成 8 个通用镜头：claim_ladder、evidence_contract、stakeholder_context、execution_validation、risk_ethics_permission、operation_handoff、transfer_boundary、deliverable_storyline。具体字段由项目现场生成，不从主协议复制长目录。
37. 新项目的核心检查不是“属于哪个旧 trace”，而是识别常见误判：把输出当效果、把一次通过当长期可靠、把制度名单备案当治理有效、把样本发现外推总体、把公益善意替代授权、把竞赛/模拟/样机转译为现实能力、把权威来源误当现场证据、把回归样例写成愿望清单。
38. 工具型 trace 必须保留在主协议主体，因为它们跨领域服务治理过程：current_basis、resource_boundary、project_nature_router、anti_premature_convergence_gate、ibis_argument_map_gate、thought_search_gate、adaptive_judgment_controller、decision_rights_matrix、judgment_depth_ladder、route_evaluator_reflection_gate、evidence_matrix、decision_log、traceability_matrix、deliverable_execution_trace、live_project_pool_scan、real_project_pressure_test_gate、micro_task_execution_check、capability_discovery_cadence_gate、event_triggered_capability_refresh、continuous_optimization_meta_project_profile、best_practice_learning_contract、capability_type_and_side_effect_gate、external_state_write_guard、skill_plugin_discovery_gate、integration_lifecycle_gate、transactional_integration_consistency_guard、agentic_orchestration_capability_builder、agent_topology_selection_trace、subagent_orchestration_pattern_router、desired_state_reconciliation_guard、stateful_data_migration_guard、security_incident_response_guard、data_artifact_lineage_freshness_guard、software_delivery_state_boundary_guard、source_link_recency_audit、rendered_artifact_freshness、numeric_calculation_trace、append_only_eof_guard、append_eof_section_tool、verify_governance_recovery_tool、latest_board_tail_check、release_package_freshness、change_inventory、current_scope_recovery_scan、subagent_capability_probe、subagent_result_coverage_gate、subagent_lifecycle_cleanup、main_agent_integration_review、claim_readiness_ladder、anti_protocol_bloat_gate。子代理方法学习相关的 `method_transfer_matrix`、`capability_resolution_order`、`read_only_audit_subagent_contract`、`gate_activation_matrix` 和 `schema_hygiene_gate` 默认作为这些工具型 trace 的子结构存在，不再为每个框架单独新增主协议目录。
39. 追踪模板必须经 trace_module_router 选择后启用：按项目类型、最终要证明的主张、风险标签和经验库索引只启用必要镜头；禁止把经验库条目或历史 trace 全量套给用户或项目。
40. 每次新增规则、字段或经验库条目，都必须先过 anti_protocol_bloat_gate：有触发信号、可观察行为、证据/检查、失败 route-back、用户摩擦影响，并说明是合并、收紧、替代还是进入 backlog。
41. 规则晋升必须从经验库回到方法论：只有跨多个真实项目反复出现、能抽象为通用失败模式、能降低用户摩擦或提升新领域构造能力的内容，才能写回主协议；单一领域细节只进入经验库。
42. 真实项目做题检验、协议自测、跨项目压力测试或用户要求“按真实项目优化协议”时，必须启用 real_project_pressure_test_gate：先完成 historical_debt_priority_queue，再从现实项目池中至少选择 3 个不同类型样本，其中至少 1 个为工程、软件、企业交付、开源维护或真实运行流程类敌意样例；每个样例必须写明真实来源、最终主张、启用镜头、小题执行证据、失败模式、降级表述和不能外推的结论。只写“可参考这些项目”或只列链接，不能算通过。
43. Agent 自我优化、协议优化、流程复盘或任何声称“修复了一个失败模式”的轮次，必须启用 micro_task_execution_check：至少实际完成 1 个 5-30 分钟的小任务，例如拆一个赛题验收链、审一个开源 issue、跑一个项目文件扫描、写一个小型 trace 样例、复算一个数字或核对一个交付物 QA。回归样例必须记录实际输入、执行证据、观察结果、pass/fail 和 remaining_gap；只写 expected_behavior 不能标记为 resolved。
44. 复杂项目出现多领域并行、真实项目池核验、独立审计、代码/文档多文件交付、互不冲突的实现子任务或大范围 QA 时，必须评估 superpower_subagent_orchestration：能调用 subagent/spawn_agent 时，主代理负责任务拆解、角色边界、集成和最终判断；子代理只承担边界清楚的只读审计、领域核验、独立实现或验证任务。调用前必须先跑 `subagent_problem_decomposition_builder`：判断任务是否可拆、是否共享状态冲突、每个子任务输入上下文是否足够、是否有验收证据、是否需要两阶段 review、是否需要 skill/plugin/tool_discovery。单文件小修、问题尚未拆清、共享状态冲突或主代理能低成本完成时，不为炫技开启子代理。记录 `subagents.capability: available` 前必须先做 `subagent_capability_probe`，区分 environment_listed、tool_discovered、spawn_attempted、agent_returned 和 result_integrated；不能只凭环境里出现子代理名称就声称可调度。spawn 后如果子代理已返回、超时、阻塞或不再需要，必须做 `subagent_lifecycle_cleanup`：记录 close_attempted、close_status、previous_status_summary、repeated_close_result 和 cleanup_decision。无法调用子代理时记录 inline_fallback；只有确实需要用户在外部环境代理执行时才写 manual_action_required。
45. 当连续自我优化从工具/恢复链 route_back 到真实项目时，必须执行 source-backed real_project_builder_smoke_test：至少覆盖软件/工程、教育/公共服务、研究/数据三类中的 3 类样本，或对用户给定项目做 1 个深度样本；每个样本都要生成临时 `new_domain_governance_builder`，并含 source_url、primary_claim_to_prove、selected_lenses、micro_task_to_execute、evidence_needed、downgrade_rule 和 failure_mode_exposed。只写“下一轮回到真实项目”不能算完成 route-back。
46. 用户要求学习网上方法、skill、插件、子代理或 AI 工作流时，必须把学习结果落到 `best_practice_learning_contract` 和 `subagent_method_learning_trace`：说明当前阶段缺口、采用了哪个方法、能解决什么、不能迁移什么、最小应用测试是什么。只列 OpenAI、LangChain、Anthropic、AutoGen、Superpowers 等名称，不算方法学习。
46.1. 每个新任务、连续优化轮次或重大阶段切换，必须先补 `capability_discovery_cadence_gate`：在 `dynamic_stage_controller` 和 `project_nature_router` 后、进入执行前，显性记录是否完成初始能力盘点；盘点面至少覆盖 local_skills、callable_tools、deferred_tools、plugins_connectors、external_apis_methods，并写清 selected_now、rejected_now、backlog 和下一次重评点。后续复盘采用 `event_triggered_capability_refresh`：阶段切换、项目性质改变、方向/主链改变、证据路径改变、连续两次卡同类问题、材料类型变化、用户新增要求、阻塞/验证失败、外部写入或子代理边界、交付对象变化、最终主张前，必须重新考虑是否需要新 skill/tool/plugin/API/外部方法。连续节拍中 3 轮只是兜底上限：无触发时写 lightweight keep，不重跑完整能力发现；若发现不匹配，必须改写 selected/rejected/backlog/manual_action 和下一轮重评点。小型本地任务可写 `intentionally_skipped`，但必须说明已有本地工具足够；不强制每次联网或调用 `tool_search`。`skill-creator` 只有在目标是创建或更新可复用 Codex skill 时才选用，否则写入 rejected/backlog。
46.1-补充. `project_nature_router`：Complex 入口必须先判断项目性质，避免把所有复杂项目都压成证据审计。取值为 `evidence_fill`、`model_discovery`、`mixed`、`execution_delivery`。若模型/公式/指标/评价表/研究框架已定，走 evidence_fill，重点是证据、来源、数据、验证和交付；若研究问题、解释框架、模型假设、变量关系或故事主线未定，走 model_discovery，先做发散保护、候选框架和可区分探针；若先要建模再填证据，走 mixed，收敛前按 model_discovery，收敛后切回 evidence_fill；若目标只是实现已定义方案，走 execution_delivery。若用户明确说“先不要证据填表、模型未定、研究思路未定、不要早收敛”，默认进入 model_discovery，除非 current_basis 反证模型已经稳定。
46.1-补充. `anti_premature_convergence_gate`：模型发现型或混合型未收敛前，不得把一个局部证据缺口、一个工具路径或一个容易完成的小 Loop 当成主目标。最低要求是保留 3-5 个候选框架，每个框架写核心假设、能解释什么、解释不了什么、支持理由、反对理由、可区分证据、最小探针和淘汰/保留条件。若候选少于 3 个，必须说明为什么问题空间已足够窄；否则 route_back 到阶段 2 或 `thought_search_gate`。
46.1-补充. `ibis_argument_map_gate`：开放式研究、理论建构、论文思路、项目主线或价值判断未定时，先建立 issue / position / pro / con / unresolved question 图。它解决“问题如何被定义”，不是替代 evidence_matrix。只有当至少一个 position 能转成可验证假设、可区分证据和下一轮探针时，才进入证据填充或执行。若只堆材料而没有 issue/position，触发 `argument_map_missing_gap`。
46.1-补充. `thought_search_gate`：借鉴 Tree/Graph of Thoughts 的多路径搜索思想，模型发现型任务的“最高杠杆问题”必须从候选路径池中选出，而不是沿第一条看似可行路径贪心推进。路径池可包含保留、合并、回退、淘汰四类操作；每个路径至少记录核心问题、假设、预期收益、最大反例、下一步探针和停止条件。若新证据推翻当前路径，允许回到候选池重排，而不是继续把当前路径做深。
46.1-补充. `adaptive_judgment_controller`：Complex 的动态性上层控制器。输入包括 `project_nature`、`convergence_status`、`current_basis`、uncertainty、reversibility、side_effect_level、user_boundary、evidence_status、capability_state、collaboration_topology 和 delivery_contract；输出包括 `judgment_mode`、`autonomy_level`、`decision_right`、`route_event`、`confidence_state`、`ask_user_needed` 和 `rollback_or_recovery_route`。默认自治边界为 `strong_autonomy_with_guardrails`：AI 可以自行加深、压缩、route_back、跳过机械复查、调整工具、微调子线程职责、切换模型发现/证据填充权重；但触发 `decision_rights_matrix.must_ask_user` 时必须回问。
46.1-补充. `decision_rights_matrix`：把用户授权、AI 自主判断和必须回问分开。AI 可自行决定 plan 细节、Loop 探针、能力候选取舍、证据深度、临时子代理分工、长期线程职责微调、发散/收敛节奏、是否 lightweight keep 和可逆的本地文件内组织调整；必须回问主目标改变、交付对象或公开口径改变、账号/API/付款/发布/外部写入、不可逆文件操作、高风险现实行动、隐私/安全/法律边界变化、证据不足却要对外强主张。若不确定是否必须回问，按副作用和可逆性保守升级。
46.1-补充. `judgment_depth_ladder`：自适应判断不应每次同等重量。`fast` 用于常规执行，只记录简短理由；`diagnostic` 用于卡住、冲突、验证失败或同类问题重复；`exploratory` 用于模型发现、框架未定或候选路径池；`strategic` 用于主链、项目性质、协作拓扑、能力组合或交付方向变化；`critical` 用于高风险、外部副作用、正式交付前或对外强主张。只有 `strategic` 和 `critical` 默认触发 `route_evaluator_reflection_gate`。
46.1-补充. `route_evaluator_reflection_gate`：重要动态决策后的轻量自评，不是每轮表格。最低记录 selected_route、rejected_routes、why_selected、highest_misjudgment_risk、counterexample_or_hostile_case、rollback_or_recovery_route 和 user_visible_summary_needed。它借鉴 evaluator-optimizer、tracing 和 Reflexion 的思想，用来让后续 AI 知道“为什么当时这么判断”，而不是重新猜一遍。
46.1-补充. `core_goal_plan_loop_required`：Complex 不把 Goal、Plan 和 Loop 当作可选模式。任何 Complex 任务都要至少记录本轮 round_goal、当前计划、一个 5-30 分钟 Loop 或明确 no-op 检查、评分路由、交付契约和恢复入口；连续项目再额外维护 active_goal_summary 和工具 Goal 生命周期。Codex `create_goal` 只在本轮窄目标确实需要工具承接时使用；一次性任务不创建长期 goal，但不能因此没有本轮目标。
46.1-补充. `complex_setup_question_card`：用户要求“按 Complex 推进”但没有说明工具权限、协作方式、推进节拍或交付对象时，AI 必须主动提一个短问题组或给出安全默认。问题只覆盖会改变路线的事项：交付对象、外部工具/账号/API/skill 权限、是否需要子代理/长期线程、是否启用连续节拍、证据/隐私/人工操作边界。若用户不回答，默认主线程单轮推进、只读本地与公开资料、留下 next_route、人看版给第三方也能读懂，并把默认写入 state 或 handoff。
46.1-补充. `user_visible_trigger_guide`：新用户不应靠猜关键词使用 Complex。入口阶段必须用普通话提示可用触发词及影响：先设计提示词/prompt 会先生成项目专用执行契约；连续节拍会改变推进节奏；多线程/子代理会改变协作拓扑；外部工具/账号/API 会改变能力边界；完整扫描 Complex 会先做协议理解；只要人看版会改变交付边界。触发词只改变对应闸门和默认选项，不得自动改写主目标。
46.1-补充. `scheduled_topology_capability_review`：连续节拍、长期线程、子代理协作或长期 Goal 运行时，必须建立 round_index、review_interval 和 event_triggered_review_status。默认事件触发优先，3 轮只是兜底上限。出现阶段切换、项目性质改变、主链变化、证据路径变化、子线程输出偏离、工具阻塞、用户新增关键词、交付对象变化、版本号变化或外部写入/账号边界变化时，主线程必须重新评估 agent_topology、subagent/thread 职责、外部能力组合和 goal_refresh_status。无触发时只写 lightweight keep；长期分线程不能永久沿用最初职责，若职责不匹配，必须给出 adjust_scope、pause_or_close、new_context_packet 或 no_longer_needed。
46.1-补充. `capability_attention_binding`：用户只要提到“外部工具、skill、API、数据库、账号、浏览器、Chrome、Scholar、机构权限、清华账号、Auto Research、Complex、等外部方法”，就不能只写“会考虑”。必须把这些词转成能力候选清单，逐项说明 selected_now、rejected_now、backlog、manual_action_required 和用户可如何帮助补齐证据。若用户点名某个能力方向，模型必须在进入执行前回应它；不能因为当前默认路径顺手，就把用户给出的能力信号漏掉。
46.1-补充. `research_access_escalation_ladder`：研究、论文、政策、数据或资料获取卡住时，“找不到”只能作为当前状态，不能作为终点。公开搜索、DOI、出版社页、学术搜索、浏览器、机构数据库、用户代登录、用户上传 PDF/截图/导出引用信息，必须按低风险到高权限逐级考虑。涉及账号、付费、认证或敏感权限时，AI 不处理密码、不绕过授权，只写清需要用户在哪个页面操作、完成后返回什么证据。用户补齐材料后，必须回到 evidence/state/decisions 更新旧判断，不能沿用 access_exhausted。
46.1-补充. `protocol_onboarding_comprehension_gate`：新项目要求读取 Complex、Auto Research、Complex 项目持续治理协议或类似强约束方法时，必须先安排协议理解时间，再开始业务产出。最低要求是按“Complex 读取顺序与关键词触发”完成扫描：本项目状态和 AGENTS/README、快速入口、Complex 启动提问卡、用户可见触发词、连续任务节拍、Stage 0-10、能力发现、子代理/线程、Loop/评分、Plan/Goal、交付拆分、人看版规则、Runtime Kit 模板。输出必须包含 protocol_scan_order、user_visible_trigger_guide、adopt_now、skip_now、backlog、manual_action 和最大误读风险。若用户说“完全扫描、完整读取、不要漏”，Plan 模式也不能只给泛泛计划；必须先完成上述覆盖检查，再给业务计划。若协议较长或项目高风险，可以让只读子代理专门做协议理解和标题/知识图谱式权重分配；但最终采用与取舍必须由主代理决定。
46.1-补充. `complex_prompt_bootstrap_gate`：用户要求“扫描 Complex 后设计提示词”“给一个完美 prompt 后再推进”或类似低摩擦入口时，必须先完成协议理解和项目提示词设计，不能直接进入业务产出。输出至少包含 protocol_scan_summary、startup_questions_or_defaults、project_prompt_design_rationale、copy_ready_prompt 和 execution_bridge。`copy_ready_prompt` 必须把本项目目标、材料、交付对象、能力边界、子代理/线程、连续节拍、round_goal/active_goal_summary/工具 Goal 生命周期、Loop、评分路由、证据边界、权限边界和恢复记录写成可复制执行契约。用户确认前只做提示词和流程设计；确认后执行仍受 Complex 主协议、最新用户指令和副作用授权约束，不能把旧 prompt 当成永久目标或免确认授权。
46.1-补充. `round_prompt_rehydration_gate`：连续节拍、长期项目、按 prompt 持续推进、Plan 模式新一轮或 next_route 接续时，必须先从 `copy_ready_prompt` / `master_prompt_location` / `active_goal_summary` 恢复总规划，再结合最新 state/current_basis 生成本轮 `round_execution_prompt`。该 prompt 是执行切片，不是总 prompt 重写；用户补充细节时默认走 `plan_patch_alignment_gate`，作为 prompt patch 写入本轮，而不是改写主目标。每轮 Plan 必须包含 `plan_alignment_to_master_prompt`：总规划继承、上一轮状态、本轮新增判断。缺少 `round_execution_prompt` 或缺少 master prompt 对齐时，不得直接进入业务计划。
46.1-补充. `per_round_goal_lifecycle_gate`：Codex 工具里的 Goal 默认承接一个可验收、可关闭的本轮窄目标，不承接“连续节拍直到用户停止”本身。长期连续性必须写在 state、master prompt、closure-routing、next_route 和机器恢复记录中；工具 Goal 只是当前拍的执行容器。触发条件包括连续节拍、Goal 模式、Plan 模式新一轮、版本号跃迁、已有工具 Goal 过期、工具 Goal blocked、用户指出“项目没卡住但 Goal 卡住”。执行顺序：
1. 读取当前工具 Goal 状态、objective、round_index、项目版本、current_basis、next_route 和上一轮交付状态。
2. 判断工具 Goal 是本轮窄目标、长期容器、过期目标、blocked 目标，还是不可用/不适合使用。
3. 若工具 Goal 是跨多轮长期容器、目标文本停在旧版本，或已 blocked 但 current_basis 证明项目仍在推进，标记 `stale_or_blocked_tool_goal`；这不是项目 blocked，只是 Goal 工具生命周期失配。
4. 若旧工具 Goal 的本轮 objective 已完成，可以 `update_goal complete`；若工具不允许清理或已 blocked 无法恢复，不得停工，改在机器看版写 `protocol_round_goal`、`goal_migration_note` 和必要的 `manual_clear_needed`。
5. 新一轮只创建或记录一个窄 `round_goal`，例如“完成 v65 架构蓝图的小循环验证和交付”，完成后关闭；下一轮从 `next_route` 派生新的窄目标。
6. 只有连续三轮都是真实项目条件阻塞，且 state、证据、工具和用户协助路径均无法推进时，才能把项目路线标记 blocked；不得因为旧工具 Goal blocked 就宣布项目受阻。
46.1-补充. `goal_refresh_gate`：连续节拍中必须区分长期方向摘要、工具 Goal、round_goal 和 next_route。`active_goal_summary` 服务长期会话和总规划，工具 Goal 默认服务本轮 Loop；每轮都要有清晰 round_goal，一轮完成只结束本轮窄目标，不自动结束 continuous route。每轮开始检查目标摘要和工具 Goal 是否仍匹配 current_basis、next_route、版本号、交付对象和最高杠杆问题；若出现目标文本停留在旧版本、旧需求或旧交付物，例如目标写 v32/v51 而项目已到 v38/v65，必须标记 stale_goal，并交给 `per_round_goal_lifecycle_gate` 迁移或写 protocol_round_goal。若工具不支持修改 goal 文本，则在机器看版写 protocol_round_goal 和 goal_migration_note，不能继续沿假 goal 执行。
46.2. 当任务本身是“持续优化项目治理协议”时，必须把它当成一个真实项目，但只能使用 `continuous_optimization_meta_project_profile` 这种压缩形态治理：先恢复最新机器看版，区分真实缺口、用户偏好和工具层惯性，列出 2-3 个候选优化点，只收束一个最高杠杆主链，用现有评分体系判断是否继续，并至少跑一个 5-30 分钟真实小题或恢复链小题。该 profile 不是新的大目录，也不自动进入 verifier required。单一案例细节进入经验库；两个以上真实项目暴露同类失败模式，才考虑晋升为主协议规则；只有能被 verifier 稳定检查的通用规则，才考虑进入 required 核心字段。候选优化点必须标注 `promote_to_protocol`、`add_to_experience_library`、`reject` 或 `backlog`。
46.3. 连续优化不得无门槛自动进入下一轮。每轮必须在 `continuous_optimization_meta_project_profile.iteration_quality_bar` 中记录 entry、execution 和 exit 三个标准：entry 确认最新恢复链、候选优化点、能力发现和 proceed_decision；execution 确认只处理一个主链、有真实小题或明确 no-op 证据、每个候选有反膨胀决策；exit 确认协议/路由/docs/发布包/变更清单/机器看版同步、验证命令通过、next_round_decision 明确。只有 `may_start_next_round: true` 时才允许进入下一轮；若连续两轮没有新跨项目失败模式，或候选只能增加复杂度不能降低误判、摩擦或恢复链风险，必须 `stop` 或只保留 backlog。
46.4. 持续优化默认采用触发式续跑，不因“还能继续优化”自动开启下一节机器看版。有效触发仅包括：用户明确指定继续某一轮、新真实项目暴露新失败模式、恢复链或验证红灯、已有 backlog 被证明能降低误判/摩擦/恢复链风险。无触发时不得创建新轮次，只能保留 backlog；若触发成立，新一轮必须从最新机器看版恢复，先完成 `capability_discovery_cadence_gate` 和 `iteration_quality_bar.entry_gate`，再决定是否进入 execution。
47. skill、plugin、connector、local_tool、web_source 和 external_method 必须通过 `capability_type_and_side_effect_gate` 分开记录。plugin/connector 或任何会安装、授权、登录、写外部系统、上传敏感材料的能力，必须写 operation_mode、side_effect_level、权限边界和 manual_action_required 或用户授权证据；不得把有副作用的插件当成本地只读 skill 处理。
48. 使用子代理后必须做 `subagent_result_coverage_gate` 和 `main_agent_integration_review`：逐项核对子代理返回是否覆盖 contract，列出未验证项、越界项、冲突项、主代理补查项和最终主张变化。子代理输出可以被采纳、部分采纳、拒收或触发 route-back，但不能绕过主代理裁决。
49. 项目结论必须绑定 `claim_readiness_ladder`。默认层级为 idea_or_candidate、source_backed、locally_verified、small_loop_validated、pilot_ready、production_or_public_claim_ready；缺少对应证据时，最终表述必须停在当前层级，不能把“方法学到”“测试通过”“子代理同意”写成公开可用或真实影响已成立。
50. 任何 plugin、connector、CLI、浏览器自动化、API 或子代理动作只要可能写入外部系统、改变账号/课程/仓库/成绩/名单/发布状态，必须补 `external_state_write_guard`。该 guard 至少记录 permission_scope_requested、external_state_target、sensitive_data_class、subagent_capability_boundary、sandbox_or_dry_run_evidence、rollback_or_reversal_plan 和 explicit_user_authorization。缺任一关键项时，只能做只读分析或写 `manual_action_required`，不能代为执行、授权、发布、同步、评分、评论、打标签或改配置。
51. 任何集成、互通、标准兼容、平台连接或生产部署主张，必须补 `integration_lifecycle_gate`。A 产品支持某标准、B 产品支持同一标准，只能证明 source_backed compatibility candidate；必须有同一版本、同一部署、同一关键流程的端到端证据，才能上升到 locally_verified 或 small_loop_validated。若出现 maintenance mode、sunset、deprecation、new-user freeze、partner transition、退役日期、数据删除日期或支持路线图改变，必须阻断 production_or_public_claim_ready，并降级为待验证、试点受限、不建议新增生产依赖或需迁移方案。
52. 任何支付、退款、订阅、物流履约、云资源创建、IoT 控制、工单状态流转、外部库存或异步 webhook / event / callback 集成，必须补 `transactional_integration_consistency_guard`。该 guard 至少记录 idempotency_key_or_dedup_strategy、duplicate_event_handling、retry_and_replay_policy、event_ordering_assumption、source_of_truth、reconciliation_or_audit_log、test_vs_live_mode_boundary、high_impact_action_compensation_plan。缺任一关键项时，只能声明 sandbox/test/source-backed 或 small-loop 验证，不能写 production ready、自动履约可靠、不会重复扣款/发货/创建资源或状态一致。
53. 当用户要求学习网上方法、skill、插件、connector 或提升子代理解决问题能力，或本轮出现多领域并行、独立审计、worker/reviewer 分工、恢复链/交付物 QA 等代理编排需求时，必须先补 `agentic_orchestration_capability_builder` 和 `agent_topology_selection_trace`。前者判断能力缺口、来源组合、可调用工具、任务拆解、上下文包、验收证据、review gate、主代理集成责任和生命周期清理；后者决定本轮是 single_agent、agents_as_tools、handoff、parallel_evidence_lanes、orchestrator_workers、reviewer_loop 还是 user_proxy，并写明最终答案控制权、状态写入权、上下文边界、并行安全、成本收益和降级路线。不得把外部框架名、skill 名或环境中列出的 agent 名称直接写成可调度能力。学习到的方法必须落成独立 work unit、`subagent_instruction_packet`、规格先行的审查链和可关闭的生命周期账本；缺 ID 绑定、上下文包、验收项、拓扑选择或超时降级时，只能写成方法候选。
53.1. `persistent_thread_orchestration_contract`：用户提到“多线程、长期线程、子代理协作、loop 工程、goal 模式、总控线程、分线程”时，必须先确定协作架构，再开始执行。最低要区分三类：临时子代理适合短期只读核验、审稿、QA；长期 Codex 线程适合跨多轮持续维护状态和领域职责；主线程内部分工适合轻量任务。若选择长期线程，必须登记线程身份、职责边界、状态写回位置、主线程整合责任、唤醒条件和停止条件；若不创建长期线程，必须写明 no_thread_reason，避免把用户要求的长期协作误降级为一次性清单。长期线程不是一次登记永久有效；连续节拍默认事件触发优先、3 轮兜底上限运行 topology_revalidation。主链、项目性质、证据路径、交付对象、版本号、外部工具边界或子线程输出偏离时立即复核；无事件触发时只写 lightweight keep，不机械重发上下文包。
54. 任何 Terraform / Pulumi / CloudFormation、GitOps、Argo CD / Flux、Kubernetes controller / operator、Helm / Kustomize、配置管理、云资源编排、环境同步或“声明式配置会被工具持续 apply / reconcile 到真实资源”的系统，必须补 `desired_state_reconciliation_guard`。该 guard 至少区分 desired_state_source、observed_state_source、plan_or_diff_review、drift_detection、state_lock_or_concurrency_control、destructive_change_gate、adoption_or_import_rule、rollback_or_forward_fix_plan、policy_or_permission_gate 和 operator_handoff。缺 plan/diff 或并发控制时只能做只读审计或 plan-only；缺 destructive gate 时不得 apply/prune/destroy；缺 drift 检测不得声称当前一致；缺 rollback/handoff 不得声称 production ready 或长期可收敛。
55. 任何数据库 schema 变更、索引/约束变更、字段重命名、类型变更、数据回填、批处理迁移、数据模型重构或其他会影响持久状态和线上读写路径的数据迁移，都必须补 `stateful_data_migration_guard`。该 guard 至少记录 migration_scope、expand_contract_or_compatibility_plan、old_new_code_read_write_overlap、backfill_or_batching_plan、lock_timeout_and_online_operation_check、constraint_index_validation_plan、data_correctness_verification、rollback_or_roll_forward_boundary、feature_flag_or_release_order、observability_and_pause_resume_plan 和 owner_runbook_handoff。缺兼容计划时不得零停机发布；缺锁/超时评估时不得在热路径执行；缺回填幂等与校验时不得声称数据正确；缺回滚/前滚边界时不得声称可安全回退。
56. 当用户要求学习网上方法、skill、插件或提升子代理解决问题能力时，必须补 `subagent_orchestration_pattern_router`。该 router 先判断单代理是否足够，再在 routing、agents_as_tools、parallel_evidence_lanes、orchestrator_workers、evaluator_optimizer、handoff、reviewer_loop、group_chat、code_or_rule_router 等可迁移模式中选择，并记录 rejected_patterns、method_to_work_unit_mapping、role_selection_reason、context_packet_completeness、minimum_application_test 和 downgrade_if_missing。缺这些映射时，只能写成方法候选；不得把 OpenAI、Anthropic、LangGraph、AutoGen、Superpowers 等外部名称直接等同于当前项目的有效子代理分工。默认原则是单代理不足才拆分、契约先于调用、按独立问题域拆分、只读证据泳道可并行、写入 worker 默认串行或隔离、handoff 只用于明确转交控制权且有人类/主代理可追踪恢复的场景、agents_as_tools 用于主代理保留最终答案但调用专业子任务、spec/requirement review 先于 quality/risk review，任何子代理“同意”都不能替代主代理对文件、来源或测试的核验。
57. 任何安全漏洞、疑似入侵、凭证或密钥暴露、扫描告警、PoC、CTF/靶场复现、issue/PR 修复、CVE/GHSA/advisory、协调披露或真实系统安全事件主张，都必须先补 `security_incident_response_guard`。该 guard 至少区分 source_type、claim_type、evidence_level、affected_asset_scope、authorization_and_contact_boundary、severity_or_priority_basis、exploitation_or_compromise_state、containment_or_mitigation_status、credential_rotation_or_secret_revocation、impact_scope、remediation_verification、coordination_or_disclosure_state、notification_requirements、monitoring_and_recurrence_check、post_incident_review_owner 和 cannot_conclude。缺少事件证据链时只能写线索或可利用性候选；PoC 不能外推为 active exploitation，扫描告警不能外推为数据泄露，PR 合并不能外推为修复已部署验证，advisory 草稿不能外推为已公开披露或已通知受影响方。
58. 任何数据集、报表、图表、模型、表格、分析输出、BI 看板、指标包或其他 data/artifact 会支撑结论、被下游引用、用于决策、发布复用或需要刷新时，必须补 `data_artifact_lineage_freshness_guard`。该 guard 至少记录 artifact_id、artifact_type、owner、status、version、artifact_path_or_uri、source_assets、input_versions_or_hashes、source_current_as_of、produced_at_or_refreshed_at、code_ref、run_id、parameters_ref、environment_ref、transformation_logic、lineage_ref、freshness_policy、freshness_checked_at、freshness_status、validation_suite_ref、validation_checked_at、validation_status、artifact_checksum、reproduction_recipe_ref、downstream_references、intended_use、known_caveats、previous_or_superseded_version 和 downgrade_if_stale。每个关键字段还必须补 `field_evidence_status`，区分 direct_observed、derived_from_metadata、inferred、unknown、not_applicable，并记录 evidence_uri_or_hash、extracted_value 和 gap_action；不能把字段存在、空值或推断当成已验证。静态文档、README、catalog、lineage 图、BI last refreshed、报表截图、PDF、文件修改时间、单次 DAG 成功、模型 registry 版本或 DOI/canonical link 都不能单独证明当前有效、可复现或可用于决策；缺复现配方、来源快照、质量检查或 stale 降级时必须降低 claim readiness。
58.1. 任何开源 PR、CI、review、merge、release、package、deployment、production readiness 或真实用户可用性主张，必须补 `software_delivery_state_boundary_guard`。该 guard 至少记录 issue_state、pr_state、ci_state、review_state、merge_state、release_state、package_state、deployment_state、usage_state、rollback_or_monitoring_state、claim_readiness 和 cannot_conclude；缺同版本 release、部署、真实使用或监控证据时，只能写到已验证的软件交付状态，不能把 PR 合并、CI 通过、包发布或示例运行外推为生产可用、用户采用或长期稳定。
59. 当用户要求学习网上方法、skill、插件或提升子代理解决问题能力时，外部方法必须先进入 `method_transfer_matrix`，再决定是否写回协议。矩阵至少把每个来源映射到：source_role、可迁移方法、解决的失败模式、适用信号、拒绝信号、生成的 work unit、最小应用测试、验收证据、不能外推边界和降级路线。只有能转成 `subagent_task_contract`、`review_gate`、`integration_gate` 或 `lifecycle_gate` 的方法才可采纳；框架名称、平台宣传、子代理数量、模型名或“网上说法”不能单独晋升。只读审计子代理必须使用 `read_only_audit_subagent_contract`，禁止编辑、安装、认证、外部写入、Plan/Goal 操作和最终裁决；输出固定为读到的锚点、证据缺口、不能支持的主张、建议补法和主代理需补查项。

### 1.1 用户低摩擦入口 compressed_user_entry

用户可以只说：

```text
这是一个重大项目。
目标是：……
已有材料在：……
我希望结果达到：……
请按 Complex 项目持续治理协议推进，但不要把流程负担转嫁给我。
```

如果用户没有写全，AI 也应自动补齐：恢复目标、识别项目类型、做真实项目/行业最佳实践扫描、启用必要 trace、记录 assumption，并只在显著降低返工时问 1-2 个问题。用户可见回复只展示项目识别、启用检查、真实来源方向、最大风险和下一步动作；完整 YAML、机器看版、失败模式和执行闸门写入治理文件。

## 2. 材料治理

阶段 1 必须先建立材料登记表。

| 字段 | 含义 |
| --- | --- |
| id | 材料编号 |
| source | 路径、链接、截图、仓库或用户描述 |
| type | paper / dataset / draft / note / code / output / screenshot / other |
| role | authoritative input / background / draft / generated output / candidate / historical |
| authority | authoritative / provisional / superseded / uncertain |
| supports_stage | intake / divergence / search / goal / plan / validation / execution / manuscript |
| current_basis | yes / no / partial |
| reason | 进入或不进入 current_basis 的理由 |

判断规则：

1. authoritative input 可以进入 current_basis。
2. background 只能作为背景，不能直接支撑结论。
3. draft 需要确认是否为最新版。
4. generated output 只能作为候选材料，不能当作事实。
5. historical 默认不进入 current_basis。
6. uncertain 必须停在 intake-open，先澄清材料权威性。

### 2.1 资源边界表

除 current_basis / not_current_basis 外，复杂项目必须显式记录 resource_boundary。它来自真实项目逆向校验 P01（DrivenData Pump it Up）、P02（DrivenData DengAI）、P03（DrivenData Power Laws）、P04（Open Cities AI Challenge）、P05（STAC Overflow）、P06（Mars Spectrometry）、P07（NASA Airathon）、P08（Water Supply Forecast Rodeo）、P09（Kelp Wanted）和 P10（Youth Mental Health Narratives）的经验：题面不只说明“可以用什么”，也可能明确“禁止用什么”；边界也不只来自外部材料，还可能来自未来标签、测试标签、时间泄漏、预测时可用信息、运行时可用信息、补充材料分布差异、隐私、伦理、评审规则、数据访问入口、模型冻结策略、预训练模型条件、人工标注边界、敏感数据处理、第三方 API 数据保留或真实部署条件。如果不记录禁止项，AI 容易在后续搜索或执行中越界。

| 字段 | 含义 |
| --- | --- |
| allowed_basis | 允许作为依据的数据、材料、工具、规则、历史版本 |
| forbidden_basis | 明确禁止使用的数据、外部材料、工具、模型、路线或表达方式 |
| official_supplementary_basis | 题面、用户或组织明确允许但有使用边界的补充材料、静态资源、预训练模型或官方工具 |
| gray_zone | 题面未明确、需要用户确认的材料或能力 |
| boundary_reason | 边界来自规则、伦理、成本、时间、隐私、评审要求还是用户偏好 |
| distribution_warning | 官方补充材料、外部背景或新增样本是否与主材料存在场景、仪器、学校、群体、时间或采集方式差异 |
| approved_access_or_permission | 官方允许材料是否还绑定指定下载入口、账号权限、生成延迟、现场许可或组织授权 |
| external_model_or_tool_policy | 预训练模型、外部工具、AI 工具或第三方服务是否允许；是否要求公开、通用、非专门针对隐藏目标训练 |
| manual_annotation_or_human_labeling_policy | 是否允许人工补标、人工审阅、众包、访谈追问、支队成员主观判读；训练/准备/现场/测试阶段边界分别是什么 |

如果 forbidden_basis 不为空，必须进入执行前闸门检查。

外部材料不能只做二元判断。必须区分：

1. forbidden external：明确禁止或会造成越界的外部数据、答案、工具和结论。
2. official supplementary：题面、用户或组织明确允许的补充材料，但只能在规定边界内使用；如果材料绑定 approved access location、账号、下载窗口、现场授权或数据生成延迟，也要记录。
3. background-only：只能帮助理解语境，不能支撑关键结论。
4. training-only / inference-only：只允许在训练、准备、现场执行或复盘中的某个阶段使用。
5. external model / human annotation：外部模型、AI 工具、人工补标和人工审阅必须单独记录允许条件；公开可得不等于可用，人工看过不等于可作为测试或评估依据。
6. sensitive / restricted data：敏感文本、未成年人、医疗、心理健康、学校、隐私、暴力或可再识别材料，必须记录可运行环境、禁止传输对象、保留/删除规则、发布抑制规则和免责声明。

## 3. 证据与问题标注

所有关键判断必须标注依据类型：

| 标注 | 含义 |
| --- | --- |
| material_fact | 当前材料直接支持 |
| inference | AI 基于材料做出的推断 |
| assumption | 暂时假设，尚未验证 |
| user_confirm_needed | 需要用户确认 |
| external_method | 来自外部方法或高质量项目 |
| synthetic | AI 模拟、样例或模板，不是真实结论 |

复杂问题必须区分四层：

1. 世界问题：现实中到底发生了什么。
2. 经验规格：什么结果算好、算坏、算够用。
3. 操作问题：下一步具体怎么做。
4. 表达问题：如何写成方案、论文、报告、代码或展示。

如果问题层级不清，不能写 Goal 或 Plan。

### 3.1 双指标规则

复杂项目必须区分两类成功标准：

1. **正式指标**：排行榜分数、评分表、验收测试、论文指标、评奖标准、交付格式、用户显性要求。
2. **真实效用指标**：现实世界中是否真的有用、是否被人采用、是否降低成本、是否改善理解、是否能被现场承接。

如果正式指标和真实效用指标不一致，Plan 必须写明当前优先级和取舍。例如数据竞赛中排行榜准确率可能高于真实运营可解释性；社会实践中评奖叙事可能不同于现场长期影响。

### 3.2 验证切分、场景异质性与目标形态规则

本规则来自真实项目逆向校验 P02（DrivenData DengAI）、P03（DrivenData Power Laws）、P04（Open Cities AI Challenge）、P05（STAC Overflow）、P06（Mars Spectrometry）和 P09（Kelp Wanted）的经验：同一个“做预测/做方案/做报告”的表层任务，真正决定方法质量的往往是验证切分、适用场景、输出目标形态、标签来源和样本相关结构。如果这些没有在前置阶段显式化，后续很容易得到一个形式上完整、现实上无效的方案。

在写 Goal 和 Plan 前，必须补充以下三项：

| 字段 | 必答问题 | 常见取值 |
| --- | --- | --- |
| validation_semantics | 当前验证方式到底模拟什么真实部署？ | 随机同分布、严格未来、跨地区、跨学校、跨用户群、跨设备、跨 AOI/地点、人工评审、现场试点 |
| segment_or_context | 任务是否存在不可忽略的群体/场景异质性？ | 城市、学校、年级、地区、人群、平台、组织、时期、设备、数据来源、云量、边界、样本难度 |
| target_form | 最终输出到底是什么形态？ | 分类、计数、连续值、排名、文本、图像分割、结构化行动建议、课程、报告、工具包 |
| metric_structure | 指标或验收标准如何加权、归一化、聚合和惩罚错误？ | 加权误差、平均分、IoU/Jaccard、最低项卡线、人工评分表、分组均值、长期采用率、忽略区域 |
| evidence_or_label_quality | 依据、标签、访谈、问卷或 ground truth 是否质量一致？ | 高质量/低质量标签、噪声标签、标注来源差异、空间/时间配准误差、缺失群体、样本偏差、旧材料、二手转述 |
| correlated_or_duplicate_units | 是否存在近重复、同源、同地点、同用户、同学校、同批次或强相关样本？ | AOI group、同一学校/班级、同一访谈链、同一传感器轨道、同一病例/家庭、同一数据来源、隐藏 group |

判断规则：

1. 如果真实部署是未来预测，随机切分不能证明未来可用；如果真实部署是跨地区/跨学校，单地区随机验证不能证明迁移可用。
2. 如果任务天然包含不同群体或场景，必须判断采用统一方案、分组方案还是分层方案；不能默认“一个总方案”覆盖所有人。
3. 目标形态决定 baseline 和验收方式。计数目标不能只按普通连续回归处理；行动建议不能只按文本好看验收；社会实践项目不能只按汇报叙事验收。
4. 指标结构决定优化方向。不能只写“提高准确率”“降低误差”“评委喜欢”，必须拆解指标如何计算；如果存在 ignored region / valid region / 排除样本 / 不计分项，必须显式记录；如果用代理指标，必须说明它不能证明什么。
5. 证据和标签不默认同质。高质量标签、低质量标签、样本偏差、访谈噪声、人工标注来源、空间/时间配准误差和历史材料都要分层记录。
6. 如果样本可能近重复、同源或强相关，必须使用 group-aware validation；如果显式 group label 被移除，也要寻找合法 proxy，例如元数据、时间、学校/班级、设备、DEM/图像 embedding 或材料来源，但不得越过资源边界。
7. 这些项若无法确定，Plan 必须记录 assumption 或 user_confirm_needed，不能伪装成已经验证。

最小记录模板：

```yaml
validation_semantics:
segment_or_context:
target_form:
metric_structure:
ignored_or_valid_region:
evidence_or_label_quality:
correlated_or_duplicate_units:
chosen_strategy:
why_this_strategy:
what_this_validation_can_prove:
what_this_validation_cannot_prove:
```

### 3.3 预测时可用信息、执行契约与复现成本规则

本规则来自真实项目逆向校验 P03（DrivenData Power Laws）、P04（Open Cities AI Challenge）、P05（STAC Overflow）、P06（Mars Spectrometry）、P07（NASA Airathon）、P08（Water Supply Forecast Rodeo）和 P09（Kelp Wanted）的经验：高质量方案不仅要“能做”，还要证明它在真实执行时没有偷用未来信息，并且能在资源预算和运行环境内复现。尤其是预测、推荐、调度、干预、社会实践、调研和代码交付项目，必须把“行动发生时能知道什么”“同批次信息能否共享”“模型或方案是否允许更新”和“最终在哪里以什么契约运行”前置写清。

凡项目涉及未来预测、现场行动、用户推荐、政策建议、教学干预或长期跟踪，必须补充：

```yaml
prediction_time_contract:
  actor:
  action_time:
  visible_information:
  invisible_information:
  allowed_proxy:
  data_availability_ledger:
    generated_at:
    accessible_at:
    timezone_or_local_context:
    access_permission:
    latency_or_delay:
    as_of_replay_rule:
  leakage_or_overclaim_risk:
case_context_contract:
  unit_of_prediction_or_action:
  same_batch_visible_information:
  cross_case_allowed:
  cross_case_forbidden:
  future_or_hidden_information:
  correlated_or_duplicate_unit_policy:
rolling_evaluation_contract:
  model_freeze_or_update_policy:
  scheduled_runs_or_followups:
  interim_feedback_status:
  final_ground_truth_delay:
  failure_repair_scope:
reproduction_budget:
  compute_or_labor:
  time:
  permission_or_data_access:
  cost:
  low_cost_proxy_loop:
execution_contract:
  runtime_or_site:
  input_paths_or_materials:
  output_format:
  dependency_or_tooling:
  network_or_permission:
  time_memory_compute_limits:
  independence_or_no_cross_case_rule:
  batch_or_context_scope:
  local_validation_command:
```

判断规则：

1. 任何特征、证据、访谈结论或行动建议，都要问“在真实行动时是否已经可见”。如果事后才知道，不能伪装成事前依据。
2. 对预测任务，必须区分训练时可用、验证时可用、部署时可用；对社会实践和调研任务，必须区分前期假设、现场可观察事实和事后复盘结论。
3. “当天的数据”“现场听到的话”“同组同学已经知道的信息”不自动等于行动时可用。必须记录 generated_at、accessible_at、timezone_or_local_context、access_permission、latency_or_delay 和 as_of_replay_rule。
4. 不要默认所有样本、班级、访谈对象、学校、地区或测试案例必须独立，也不要默认可以互相借用。必须记录 case_context_contract，说明同批次可共享信息和禁止共享信息。
5. 如果项目成果会被未来多次运行、复测、回访或评估，必须记录 rolling_evaluation_contract。要说明模型/方案何时冻结、何时允许更新、临时反馈是否只是 diagnostic、最终真值何时出现，以及失败时能修什么不能修什么。
6. 如果公开答案、候选路线或理想方案需要高算力、长时间、特殊权限、组织协作或敏感数据，Plan 必须设计低成本代理闭环，不能直接把高成本路线当成当前可执行计划。
7. 复现成本不是执行阶段才考虑的工程细节，而是 Goal 和 Plan 是否成立的一部分。
8. 如果交付物要在指定容器、学校现场、评审系统、问卷平台、课堂时间、访谈场域或组织流程中运行，必须记录 execution_contract；路径、格式、权限、依赖、时限、人工角色和失败回退都属于前置治理。
9. 如果规则要求样本、班级、访谈对象、测试案例、学校或地区之间独立处理，必须记录 independence_or_no_cross_case_rule；如果规则允许同批次、同课堂、同日期或同地区信息共享，也必须记录 batch_or_context_scope，不能把一个项目里的跨样本技巧无脑迁移到另一个项目。
10. 如果样本存在近重复或同源结构，必须说明这种相关性属于验证切分问题、同批上下文问题还是资源越界问题；不能用“题面没给 group label”作为忽略相关样本的理由。

### 3.4 下游使用、公共伤害与竞赛技巧标注规则

本规则来自真实项目逆向校验 P04（Open Cities AI Challenge）、P05（STAC Overflow）、P06（Mars Spectrometry）、P08（Water Supply Forecast Rodeo）、P09（Kelp Wanted）和 P10（Youth Mental Health Narratives）的经验：公共性项目的“好”不能只由模型指标、报告好看或短期评奖决定。如果项目输出会进入教育、公共治理、医疗、灾害、心理健康、资源分配、人群判断、水资源管理、生态监测或科学任务决策，必须把下游使用者、受益者、可能受损者、不确定性沟通、数据安全和执行者安全放在前置治理阶段。

必须补充：

```yaml
downstream_use:
  decision_maker:
  direct_users:
  affected_groups:
  intended_benefit:
  potential_harms:
  uncertainty_communication:
  human_oversight:
  participation_or_feedback:
communication_output_contract:
  audience:
  decision_questions:
  reproducible_outputs:
  narrative_scope:
  judging_rubric_or_success_criteria:
sensitive_data_handling_contract:
  data_sensitivity:
  allowed_environment:
  prohibited_transfer_or_tool:
  retention_or_deletion_rule:
  publication_suppression_or_disclaimer:
operator_wellbeing_or_safety:
  exposure_risk:
  exposure_limit:
  support_resource:
  opt_out_or_rotation:
expert_review_contract:
  expert_role:
  review_sample:
  adjudication_or_consensus:
  disagreement_or_bias_handling:
evidence_or_label_quality:
  evidence_layers:
  known_noise:
  missing_groups:
  bias_risk:
  verification_plan:
technique_status:
  baseline:
  competition_only:
  deployment_safe:
  research_only:
```

判断规则：

1. 量化指标不能自动证明公共效用。像素 IoU、准确率、点击率、评委分数或问卷均值，只能证明它们对应的窄指标。
2. 如果输出会影响真实人群，必须说明谁会使用、谁会受益、谁可能被误伤、谁负责复核，以及如何表达不确定性。
3. 如果依据本身有质量分层，例如高质量/低质量标签、城市/学校/地区样本不均、访谈对象偏差、问卷样本偏差，Plan 必须记录并设计分层验证。
4. 竞赛中有效的技巧不自动适合真实部署。依赖测试集分布、leaderboard feedback、伪标签、过度集成、题面特例或评奖口味的做法，必须标注为 competition_only 或 presentation_only，不能直接写成 deployment_safe。
5. 面向非技术决策者的解释、汇报、forecast summary、课堂反馈或政策摘要，如果会影响真实行动，就是交付物，不是最终报告装饰。必须定义 audience、decision_questions、reproducible_outputs 和 narrative_scope。
6. 敏感数据不能只靠“不要泄露”四个字处理。必须写清数据敏感性、允许运行环境、禁止上传/转发的工具、保留和删除规则、公开发布时的小样本抑制或免责声明。
7. 如果材料涉及创伤、暴力、心理健康、未成年人、医疗或沉重个案，执行者安全也是项目边界。必须记录 exposure_limit、support_resource、opt_out_or_rotation。
8. 如果结论会进入专业领域判断，必须定义 expert_review_contract。专家不是最终润色者，而是判断变量、结论、风险和偏差能否成立的证据来源。
9. 伦理、责任和公平不是最终报告的装饰段，而是判断主链是否成立的前置条件。

### 3.5 研究结论边界、概率校准与领域预处理规则

本规则来自真实项目逆向校验 P06（Mars Spectrometry）、P07（NASA Airathon）、P08（Water Supply Forecast Rodeo）和 P09（Kelp Wanted）的经验：很多复杂项目真正危险的地方，不是模型、调研或报告做不出来，而是把代理目标误写成真实结论，把可观测信号误写成潜在事实，把概率/置信度误写成确定判断，把数据预处理误当成中性清洗，或把目标的已知部分和未知部分混在一起。科研、社会实践、教育调研、公共议题、医学健康、生态监测、政策建议和 AI 项目尤其需要在前置阶段建立“结论边界”。

必须补充：

```yaml
claim_ladder:
  world_question:
  measurable_proxy:
  model_or_project_output:
  allowable_claim:
  forbidden_overclaim:
observable_proxy_boundary:
  observed_signal:
  latent_construct:
  unobserved_parts:
  confounders_or_occlusions:
  claim_limit:
probability_or_score_contract:
  output_meaning:
  calibration_need:
  threshold_or_decision_rule:
  interval_or_quantile_meaning:
  coverage_or_reliability_check:
  coherence_constraints:
  overconfidence_risk:
  uncertainty_expression:
target_decomposition:
  known_component:
  residual_or_unknown_component:
  final_target:
  transformation_or_addback_rule:
open_world_or_sparse_class_risk:
  missing_labels_or_groups:
  rare_or_unseen_cases:
  safe_default:
  human_review_or_followup:
label_or_measurement_quality_contract:
  source_or_annotator:
  measurement_or_annotation_process:
  noise_modes:
  alignment_or_registration:
  correlated_or_duplicate_units:
  curation_or_exclusion_rule:
novel_variable_or_construct_contract:
  proposed_name:
  definition:
  gap_from_existing_variables_or_frames:
  theory_or_literature_basis:
  extractability_or_observability:
  validation_plan:
  action_or_research_value:
  communication_form:
domain_preprocessing_assumptions:
  transformed_or_removed_materials:
  normalization_or_coding_rule:
  missingness_or_imputation_rule:
  background_or_noise_policy:
  information_loss:
  why_domain_valid:
secondary_evaluation_or_priority_subset:
  priority_subset:
  secondary_metric_or_judges:
  tradeoff_with_main_metric:
```

判断规则：

1. 代理目标不等于真实结论。模型预测、问卷反馈、访谈样本、课堂表现、评委分数或短期结果，只能支持它们实际测量到的范围。
2. 如果输出是概率、风险分数、置信度、推荐强度或“可能性”，Plan 必须包含校准、阈值、过度自信风险和不确定性表达；不能只追求排序或命中率。
3. 如果输出是区间、上下界、分位数或风险带，必须记录 interval_or_quantile_meaning、coverage_or_reliability_check 和 coherence_constraints。例如上下界不能交叉，预测区间的含义必须能被使用者理解。
4. 如果目标由已知部分和未知部分组成，必须记录 target_decomposition。不能把 residual、增量、代理量或局部量误写成 final_target。
5. 如果训练材料、访谈对象、样本学校、历史案例或标签中缺少某些类别/群体，不能默认它们不存在。必须记录 open_world_or_sparse_class_risk，并设计安全默认值、人工复核或“不知道”的表达。
6. 如果输出来自可观测代理，例如遥感 canopy、问卷答案、课堂表现、访谈片段、日志行为、模型分数或短期反馈，必须记录 observable_proxy_boundary：它观测到了什么、没观测到什么、被什么遮挡或混淆、最多能支撑到哪一层结论。
7. 标签、测量和人工材料必须有质量契约。必须记录 source_or_annotator、measurement_or_annotation_process、noise_modes、alignment_or_registration、correlated_or_duplicate_units 和 curation_or_exclusion_rule；不能把“有人标过”“有人说过”“材料里写了”当成同等可靠事实。
8. 如果项目要提出“新变量”“新公共议题”“新研究抓手”“新评价维度”或“新故事主线”，必须写 novel_variable_or_construct_contract。它至少要满足 definition、gap_from_existing_variables_or_frames、theory_or_literature_basis、extractability_or_observability、validation_plan、action_or_research_value 和 communication_form。
9. 预处理不是中性动作。删样本、归一化、合并类别、背景扣除、缺失值插补、线性插值、问卷编码、访谈摘要、案例改写、材料筛选、mask 后处理、LLM 生成样例和权威话术融合，只要会改变结论，都必须记录为领域假设。
10. 如果项目存在 bonus prize、专家评审、关键学校、关键群体、重点场景、底线指标或组织偏好，必须单列 secondary_evaluation_or_priority_subset。总分高不等于关键子场景可用。

### 3.6 跨目标形态契约选择规则

本规则来自真实项目逆向校验 P11-P20 的新增经验：复杂项目不能只问“做什么”，还要问“它到底是哪一种目标形态”。事件检测、语义分割、科学 benchmark、隐私合成数据、强化学习、机器人仿真、社会创新、开放创新和开源 RFC 的成功条件完全不同。如果目标形态识别错，后续 Plan、指标、证据和结论都会偏。

前置阶段必须先选择适用契约。可以多选，但不能空缺。

```yaml
contract_selector:
  target_form:
  primary_contracts:
  secondary_contracts:
  why_selected:
  why_not_selected:
  required_minimum_evidence:
  user_feedback_gate_needed:
```

新增常用契约：

```yaml
multi_representation_contract:
  representation_source:
  information_loss:
  why_domain_valid:
  model_or_method_role:
  fusion_rule:
soft_label_or_consensus_target:
  voters_or_annotators:
  agreement_or_vote_count:
  disagreement_meaning:
  training_or_analysis_use:
  low_consensus_policy:
event_detection_contract:
  event_unit:
  tolerance_window:
  duplicate_policy:
  score_meaning:
  peak_selection_rule:
  final_event_format:
intermediate_target_contract:
  intermediate_target:
  final_target:
  transformation_rule:
  information_loss:
  validation_for_each_stage:
post_processing_contract:
  thresholds:
  distance_or_nms_or_wbf_rule:
  business_or_domain_filters:
  ablation:
  reproducibility_entry:
segmentation_contract:
  object_geometry:
  empty_case_policy:
  threshold_rule:
  resolution:
  alignment:
  visual_audit:
external_data_and_pseudolabel_contract:
  source:
  license_or_permission:
  leakage_risk:
  generation_model:
  use_stage:
  ablation:
public_action_chain:
  model_or_project_output:
  decision_action:
  impact_mechanism:
  cost_or_side_effect:
  evidence_level:
scientific_proxy_contract:
  reference_method:
  target_quantity:
  downstream_decision:
  known_error_floor:
  practical_threshold:
  missing_experiment:
privacy_contract:
  privacy_unit:
  adjacency:
  epsilon_delta:
  composition:
  data_access_ledger:
  proof_artifact:
workload_or_query_contract:
  intended_workload:
  non_goals:
  utility_metrics:
  unsupported_downstream_tasks:
trainable_submission_contract:
  training_entrypoint:
  from_scratch_condition:
  data_access_during_training:
  runtime_budget:
  evaluator_semantics:
environment_contract:
  simulator_or_runtime:
  version:
  seed_space:
  observation_action_or_interface:
  sample_or_time_budget:
  exploit_prohibition:
simulation_to_reality_contract:
  simulator_scope:
  known_gaps:
  validated_capability:
  unvalidated_real_world_factors:
  transfer_claim_limit:
system_integration_contract:
  modules:
  interfaces:
  failure_modes:
  recovery_actions:
  logs_or_evidence:
multi_agent_coordination_contract:
  role_set:
  allocation_policy:
  communication_assumptions:
  conflict_resolution:
  redundancy:
impact_pathway_contract:
  beneficiary:
  pain_point:
  mechanism:
  evidence:
  scaling_path:
community_fit_contract:
  local_language_or_context:
  cultural_relevance:
  low_resource_constraints:
  trusted_intermediaries:
  co_creation_evidence:
co_creation_contract:
  participants:
  methods:
  consent_or_safeguarding:
  feedback_loop:
  decision_power:
prototype_contract:
  fidelity:
  tested_assumption:
  participant:
  feedback:
  iteration:
digital_wellbeing_contract:
  positive_wellbeing_goal:
  agency:
  belonging:
  safety:
  data_minimization:
  escalation_path:
lifecycle_state_contract:
  proposal_status:
  accepted_status:
  implementation_status:
  support_status:
  default_status:
  deprecation_or_rollback_status:
ecosystem_migration_contract:
  affected_parties:
  compatibility_matrix:
  migration_guide:
  tooling_or_packaging_status:
  adoption_evidence:
versioned_claim_contract:
  current_as_of:
  version_or_stage:
  claim:
  may_change_when:
```

判断规则：

1. 如果输出是点事件，例如 onset、wakeup、故障、风险峰值、政策节点、行动节点，必须启用 event_detection_contract，并把 tolerance、去重、score 和最终事件格式写清。
2. 如果建模或研究中有中间目标，例如 sleep state、mask、latent score、问卷编码、课堂观察等级、故事主题簇，必须启用 intermediate_target_contract，说明它如何转成最终目标。
3. 如果输出是 mask、边界、区域、地图或空间覆盖率，必须启用 segmentation_contract，并做视觉抽检。
4. 如果方案靠阈值、距离约束、NMS/WBF、人工规则、业务过滤或故事化筛选成形，必须启用 post_processing_contract。后处理是方案的一部分，不是附注。
5. 如果使用外部数据、预训练、伪标签、权威话术库或旧项目样本，必须启用 external_data_and_pseudolabel_contract，说明许可、泄漏风险和消融。
6. 公共性、教育、医疗、气候、治理项目必须启用 public_action_chain 或 impact_pathway_contract，不能把代理指标直接写成公共成效。
7. 科学 benchmark 或工程代理项目必须启用 scientific_proxy_contract，并写 practical_accuracy_gap：榜单进步不等于可实用。
8. 隐私、安全和数据发布项目必须启用 privacy_contract 与 workload_or_query_contract；没有形式化证明或访问账本，不能声称安全。
9. RL、仿真、机器人、游戏和控制项目必须启用 trainable_submission_contract 与 environment_contract；离线准确率不能替代在线环境表现。
10. 仿真、数字孪生和机器人项目必须启用 simulation_to_reality_contract；仿真成功不能直接写成真实部署成功。
11. 社会创新、支教、教育调研、公益和社区项目必须启用 beneficiary、community_fit、impact_pathway、co_creation 和 prototype 相关契约；没有受益者声音和原型反馈，主张必须降级。
12. 青少年、AI、互联网、游戏和心理健康项目必须启用 digital_wellbeing_contract 与 safeguarding 相关检查，特别处理未成年人隐私、心理安全、成年人控制边界和求助升级。
13. 开源 RFC、政策、标准、法规、模型能力和产品路线图必须启用 lifecycle_state_contract、ecosystem_migration_contract 和 versioned_claim_contract；accepted、experimental、supported、default 是不同状态。
14. 如果 AI 在路线选择、代表案例选择或故事抓手上不确定，必须触发 user_feedback_gate_needed，给用户 2-4 个候选方向和推荐理由，不能写完整套后再等待返工。

## 4. 机器看版 handoff

每阶段结束必须输出稳定、可继承的机器看版。

机器看版可以保留 `dynamic_stage_controller.mode`、`stage_depth_budget`、`major_project_mode` 等历史兼容字段，但这些是内部路由和工作力度记录，不是让用户选择“普通/重大项目”的入口。用户可见层只说明本轮目标、采用的能力、协作方式、风险升级原因、交付对象和下一步。

```yaml
current_stage:
stage_status: open | closed | blocked
dynamic_stage_controller:
  mode:
  stage_depth_budget:
  current_stage:
  route_event:
  routing_decision_log:
    - decision:
      selected:
      alternatives_considered:
      rejected_reason:
      trigger_evidence:
      user_friction_effect:
      revisit_if:
  confidence_state:
  friction_budget:
  gate_activation_matrix:
  subagent_decision:
capability_discovery_cadence_gate:
  initial_scan:
    status:
    scanned_surfaces:
    candidates_considered:
    selected_now:
    rejected_now:
    backlog:
    skip_reason:
  event_triggered_capability_refresh:
    required_triggers:
    trigger_event:
    last_checked_at_stage:
    result: refresh | lightweight_keep | defer_until_probe_or_evidence_path
    next_check:
  periodic_reconsideration_legacy_alias:
    status: superseded_by_event_triggered_capability_refresh
  lightweight_exception:
current_basis:
not_current_basis:
open_questions:
decisions:
next_route:
route_reason:
backlog:
risk_register:
major_project_mode:
evidence_matrix_status:
decision_log_status:
traceability_status:
agent_self_optimization_mode:
agent_eval_status:
agent_failure_modes:
agent_regression_cases:
continuous_optimization_meta_project_profile:
  continuation_policy:
    default_mode: trigger_based
    valid_triggers: [explicit_user_request, new_real_project_gap, verification_red, high_value_backlog_item]
    no_trigger_behavior: backlog_only_no_new_machine_board
    next_round_entry: latest_machine_board_plus_capability_discovery_cadence_gate_plus_iteration_quality_bar_entry_gate
  iteration_quality_bar:
    round_id:
    entry_gate:
      latest_machine_board:
      recovery_chain_failure_count:
      candidate_count:
      candidate_minimum_score:
      capability_discovery_checked:
      proceed_decision: continue | stop | ask_user
    execution_gate:
      selected_candidate:
      one_main_chain_only:
      micro_task_or_noop_evidence:
      concrete_artifact_or_record_ref:
      source_url_present:
      primary_claim_bounded:
      state_or_field_evidence_status:
        direct_observed:
        unknown_or_not_verified:
      downgrade_rule_present:
      claim_readiness_boundary:
      promotion_recommendation_present:
      user_friction_effect_stated:
      anti_protocol_bloat_decisions:
    exit_gate:
      files_synced:
      verification_commands:
      next_round_decision: continue | stop | ask_user
      may_start_next_round:
  stage_0:
    latest_machine_board:
    continue_reason:
  stage_1:
    current_basis:
    not_current_basis:
    gap_type: real_gap | user_preference | tool_inertia
  stage_2:
    candidate_optimizations:
      - candidate:
        value_score:
        friction_reduction:
        overclaim_risk_reduction:
        verifiability:
        decision: promote_to_protocol | add_to_experience_library | reject | backlog
  stage_4:
    selected_main_chain:
    rejected_chains:
  stage_7:
    continue_score:
    stop_condition:
  stage_8:
    micro_task:
    observed_gap:
    downgrade_rule:
  stage_9:
    anti_protocol_bloat_gate:
    protocol_change_allowed:
contract_selector:
user_feedback_gate:
changed_since_last_stage:
codex_tool_state:
  goal:
  plan:
  subagents:
    capability:
    strategy:
    capability_probe:
      environment_listed:
      tool_discovered:
      discovery_method:
      callable_tool:
      spawn_attempted:
      agent_ids:
      wait_status:
      integration_decision:
      integration_reason:
      main_agent_local_checks:
      adopted_from_subagent:
      rejected_or_superseded_from_subagent:
    lifecycle_cleanup:
      close_attempted:
      closed_agent_ids:
      close_status:
      previous_status_summary:
      repeated_close_result:
      cleanup_decision:
      open_agent_cleanup_required:
    spawn_reason:
    no_spawn_reason:
    roles:
    integration_status:
    review_gates:
    problem_decomposition:
      spawn_preflight:
      dependency_boundary_check:
      controller_prepared_context_packet_ready:
      plan_subagent_binding:
      capability_discovery_cadence_gate:
      best_practice_learning_contract:
      skill_plugin_discovery_gate:
      capability_type_and_side_effect_gate:
      external_state_write_guard:
      integration_lifecycle_gate:
      skill_plugin_learning_loop:
      skill_plugin_project_fit_trace:
      subagent_method_learning_trace:
      agent_topology_selection_trace:
      subagent_orchestration_pattern_router:
      security_incident_response_guard:
      data_artifact_lineage_freshness_guard:
      subagent_result_coverage_gate:
      main_agent_integration_review:
      claim_readiness_ladder:
    best_practice_learning_contract:
      stage_gap:
      practice_pattern_extracted:
      project_stage_gap_addressed:
      minimum_application_test:
      downgrade_if_not_tested:
    skill_plugin_discovery_gate:
      discovery_basis:
      candidate_list:
      selected:
      call_or_skip_decision:
    capability_type_and_side_effect_gate:
      capability_type:
      operation_mode:
      side_effect_level:
      permission_or_manual_action_required:
    external_state_write_guard:
      permission_scope_requested:
      external_state_target:
      sensitive_data_class:
      subagent_capability_boundary:
      sandbox_or_dry_run_evidence:
      rollback_or_reversal_plan:
      explicit_user_authorization:
    integration_lifecycle_gate:
      integration_claim:
      component_capabilities:
      same_version_deployment_evidence:
      end_to_end_flow_evidence:
      maintenance_or_sunset_signal:
      support_or_migration_plan:
      readiness_level_after_gate:
      downgrade_rule:
    transactional_integration_consistency_guard:
      idempotency_key_or_dedup_strategy:
      duplicate_event_handling:
      retry_and_replay_policy:
      event_ordering_assumption:
      source_of_truth:
      reconciliation_or_audit_log:
      test_vs_live_mode_boundary:
      high_impact_action_compensation_plan:
    desired_state_reconciliation_guard:
      desired_state_source:
      observed_state_source:
      target_scope:
      execution_model:
      plan_or_diff_review:
      drift_detection:
      state_lock_or_concurrency_control:
      destructive_change_gate:
      adoption_or_import_rule:
      rollback_or_forward_fix_plan:
      policy_or_permission_gate:
      operator_handoff:
      downgrade_if_missing:
    stateful_data_migration_guard:
      migration_scope:
      expand_contract_or_compatibility_plan:
      old_new_code_read_write_overlap:
      backfill_or_batching_plan:
      lock_timeout_and_online_operation_check:
      constraint_index_validation_plan:
      data_correctness_verification:
      rollback_or_roll_forward_boundary:
      feature_flag_or_release_order:
      observability_and_pause_resume_plan:
      owner_runbook_handoff:
      downgrade_if_missing:
    security_incident_response_guard:
      source_type:
      claim_type:
      evidence_level:
      affected_asset_scope:
      authorization_and_contact_boundary:
      severity_or_priority_basis:
      exploitation_or_compromise_state:
      containment_or_mitigation_status:
      credential_rotation_or_secret_revocation:
      impact_scope:
      remediation_verification:
      coordination_or_disclosure_state:
      notification_requirements:
      monitoring_and_recurrence_check:
      post_incident_review_owner:
      cannot_conclude:
      downgrade_if_missing:
    data_artifact_lineage_freshness_guard:
      artifact_id:
      artifact_type:
      owner:
      status:
      version:
      artifact_path_or_uri:
      source_assets:
      input_versions_or_hashes:
      source_current_as_of:
      produced_at_or_refreshed_at:
      code_ref:
      run_id:
      parameters_ref:
      environment_ref:
      transformation_logic:
      lineage_ref:
      freshness_policy:
      freshness_checked_at:
      freshness_status:
      validation_suite_ref:
      validation_checked_at:
      validation_status:
      artifact_checksum:
      reproduction_recipe_ref:
      downstream_references:
      intended_use:
      known_caveats:
      previous_or_superseded_version:
      downgrade_if_stale:
      field_evidence_status:
        - field_name:
          evidence_status: direct_observed | derived_from_metadata | inferred | unknown | not_applicable
          evidence_uri_or_hash:
          extracted_value:
          gap_action:
    skill_plugin_learning_loop:
      discovery_question:
      selected_skill_or_plugin:
      instruction_source:
      instruction_read_status:
      key_constraints_extracted:
      practice_micro_task_ref:
      practice_result:
      adoption_decision:
      protocol_writeback_ref:
      verifier_requirement_ref:
      recovery_chain_ref:
    skill_plugin_project_fit_trace:
      project_context:
      primary_claim_or_stage_gap:
      pre_skill_gap:
      transferred_method:
      micro_task_before_after:
      acceptance_evidence:
      non_transfer_boundary:
      reuse_decision:
    subagent_method_learning_trace:
      source_mix:
      method_synthesis:
      micro_task_used_to_validate:
      adopted_into_subagent_contract:
      method_transfer_matrix:
      capability_resolution_order:
    agent_topology_selection_trace:
      selected_topology:
      final_answer_owner:
      state_write_boundary:
      context_boundary:
      dependency_graph:
      downgrade_to_inline_if:
    subagent_orchestration_pattern_router:
      selected_pattern:
      rejected_patterns:
      method_to_work_unit_mapping:
      role_selection_reason:
      context_packet_completeness:
      minimum_application_test:
    agentic_orchestration_capability_builder:
      capability_gap:
      method_source_mix:
      method_transfer_matrix:
      controller_prepared_context_packet:
      spawn_or_inline_decision:
      review_gate:
      main_agent_integration_responsibility:
      lifecycle_cleanup_plan:
    subagent_result_coverage_gate:
      contract_items:
      returned_items:
      unverified_items:
      blocking_gaps_after_integration:
    main_agent_integration_review:
      conflicts_found:
      adopted_claims:
      rejected_claims:
      final_claim_changed:
      integration_decision:
    claim_readiness_ladder:
      final_claim:
      current_level:
      downgrade_rule:
    review_pipeline:
      spec_review_status:
      quality_or_risk_review_status:
      open_findings_by_severity:
      re_review_required:
    lifecycle_ledger:
      - contract_id:
        agent_id:
        role:
        agent_return_status:
        integration_decision:
        close_status:
  scan_aliases:
    - subagents.capability
    - subagents.capability_probe
    - subagents.lifecycle_cleanup
    - subagents.strategy
    - subagents.roles
    - subagents.integration_status
    - subagents.review_gates
    - subagents.problem_decomposition
    - subagents.lifecycle_ledger
manual_action_required:
```

最低要求：

1. 后续 AI 只读 handoff 也能恢复项目状态。
2. current_basis 和 not_current_basis 必须分开。
3. decisions 记录关闭、回退、阻塞、范围变化和用户选择。
4. next_route 必须说明继续、回退、阻塞或等待用户的原因。
5. 如果启用了 `dynamic_stage_controller`，handoff 必须记录 mode、stage_depth_budget、route_event、routing_decision_log、subagent_decision 和 route_reason；同时说明这些是内部动态路由/工作力度，不得把“普通/重大/本轮深度”包装成用户必须理解的模式菜单。
6. 如果用了 Codex plan / goal 工具，handoff 必须记录工具状态和文档内 Goal/Plan 的对应关系。
7. 如果需要人工操作，handoff 必须记录 manual_action_required 和恢复条件。
8. 如果本阶段选择了重大路线、案例、故事抓手或目标形态，handoff 必须记录 contract_selector 和 user_feedback_gate 的处理状态。
9. 如果处于 major_project_mode，handoff 必须记录 evidence_matrix_status、decision_log_status 和 traceability_status；不能只说“已参考资料”或“已考虑风险”。
10. 如果处于 agent_self_optimization_mode，handoff 必须记录 agent_eval_status、agent_failure_modes 和 agent_regression_cases；不能只写“我会改进”。
11. 如果调用了 superpower / subagent / spawn_agent 类能力，handoff 必须记录子代理角色、任务边界、返回状态、集成结论和未采纳原因；如果子代理超时但不是关键路径，记录 `subagents.strategy: audit_timeout_non_blocking`，继续由主代理按本地证据推进；如果当前环境无法调用子代理，记录 `inline_fallback`，只有确实需要用户在外部环境代为执行时才写 manual_action_required。

#### Superpower 子代理编排 superpower_subagent_orchestration

本字段是第 5 节 `subagent_orchestration_ladder` 在机器看版中的兼容记录名。实际是否调用子代理，先按第 5 节的梯子判断；本处只负责记录能力、策略、角色、边界、返回状态和集成结论。

规范字段优先级：后续机器看版优先写 `codex_tool_state.subagents`、`subagent_contract_index`、`subagent_result_coverage_gate`、`main_agent_integration_review` 和 `subagent_lifecycle_ledger`。`superpower_subagent_orchestration` 只作为历史兼容 alias；同一子代理必须用同一个 `contract_id` 串起 task contract、coverage、integration 和 cleanup，不能让输出成为 orphan record。

```yaml
superpower_subagent_orchestration:
  capability: available | unavailable | not_needed
  strategy: not_needed | parallel_domains | subagent_driven_plan | sequential_worker | inline_fallback | user_proxy_required | audit_timeout_non_blocking
  capability_probe:
    environment_listed:
    tool_discovered:
    discovery_method:
    callable_tool:
    spawn_attempted:
    agent_ids:
    wait_status: not_started | running | returned | timed_out | blocked | failed
    integration_decision: not_needed | accepted | rejected | conflict_recorded | partially_adopted | audit_timeout_non_blocking | inline_fallback
    integration_reason:
    main_agent_local_checks:
    adopted_from_subagent:
    rejected_or_superseded_from_subagent:
  lifecycle_cleanup:
    close_attempted:
    closed_agent_ids:
    close_status: not_needed | closed | already_closed_or_not_resumable | keep_open_with_reason | cleanup_unresolved
    previous_status_summary:
    repeated_close_result:
    cleanup_decision:
    open_agent_cleanup_required:
  spawn_decision:
    reason:
    no_spawn_reason:
  roles:
    - role: source_verifier | domain_reviewer | worker | quality_reviewer | integration_reviewer
      scope:
      write_scope:
      expected_output:
      status: pending | running | returned | accepted | rejected | timed_out | blocked
      output_summary:
  integration_status:
  manual_proxy_needed:
```

1. 子代理适合处理并行、独立、可验收的任务；不适合处理尚未拆清的问题、共享文件强冲突或需要主代理连续判断的任务。
2. 主代理不能把目标、最终取舍、用户偏好判断或高风险人工操作甩给子代理；主代理必须集成和复核子代理输出。
3. 子代理超时且不是关键路径时，记录 `audit_timeout_non_blocking`，继续推进；子代理输出与本地证据冲突时，必须写 integration_status 和取舍理由。
4. `capability: available` 必须有 `tool_discovered` 或 `spawn_attempted` 证据；仅有环境子代理名单只能写 `environment_listed`，不能直接写可调度。
5. 子代理返回后，主代理必须写 `integration_reason`、`main_agent_local_checks`、`adopted_from_subagent` 和 `rejected_or_superseded_from_subagent`；不能只写 returned 或 accepted。
6. 子代理不再需要后必须记录 `lifecycle_cleanup`；如果调用 close_agent，记录 close_status 和 previous_status_summary；如果重复关闭返回 not found，只能结合 prior_close_evidence 判定为 already_closed_or_not_resumable，不能把 not found 单独当成成功关闭。
7. 当前环境没有 subagent 能力时，先 inline_fallback；只有必须由用户在外部环境代理执行时，才把任务写入 manual_action_required，并说明完成后应返回的证据。

## 5. 阶段流程

本节不是一条必须从 0 跑到 10 的流水线，而是一个动态阶段控制器。阶段编号保留，是为了让人和机器能恢复状态；真正的推进方式由当前证据、风险、用户摩擦、可验证性和工具能力共同决定。

默认原则：先判断本轮应该停在哪个阶段，再决定该阶段要轻跑、标准跑、深跑、并行跑还是回退。用户不需要知道这些字段；当用户只说“这事重要”“继续任务”“优化你自己”时，AI 应自动选择合适工作力度，并把判断写入机器看版。

### 5.0 动态阶段控制器 dynamic_stage_controller

每轮开始、阶段切换、发现重大新证据或准备执行前，先填写或更新本控制器。

```yaml
dynamic_stage_controller:
  mode: light | standard | deep | continuous
  stage_depth_budget: light | standard | deep
  project_nature: evidence_fill | model_discovery | mixed | execution_delivery
  convergence_status: divergent | candidate_pool_ready | provisionally_converged | evidence_fill_ready | execution_ready
  adaptive_judgment_controller:
    judgment_mode: fast | diagnostic | exploratory | strategic | critical
    autonomy_level: strong_autonomy_with_guardrails | ask_before_strategic_change | maximum_autonomy
    decision_right: ai_decide | ask_user | manual_action_required | blocked_until_authorized
    ask_user_needed:
    rollback_or_recovery_route:
  current_stage: 0 | 1 | 1.5 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
  route_event: advance | skip_with_reason | compress | deepen | route_back | fork_parallel | spawn_subagent | ask_user | blocked | execute
  routing_decision_log:
    - decision: mode_selection | depth_change | route_event_selection | subagent_strategy | user_feedback_gate
      selected:
      alternatives_considered:
      rejected_reason:
      trigger_evidence:
      user_friction_effect:
      revisit_if:
  confidence_state:
    problem_definition_confidence: low | medium | high
    framework_confidence: low | medium | high
    judgment_confidence: low | medium | high
    material_confidence: low | medium | high
    claim_confidence: low | medium | high
    execution_confidence: low | medium | high
    evidence_gap:
      - gap:
        route_back_if_unresolved:
  friction_budget:
    user_questions_remaining: 0 | 1 | 2
    ask_user_only_if: irreversible_choice | hidden_preference | authority_missing | cost_or_risk_shift | external_manual_action
  gate_activation_matrix:
    always_minimum:
      - current_basis
      - primary_claim
      - next_route_or_close_condition
    risk_based:
      - gate:
        activation_predicate:
        minimum_by_mode: light | standard | deep | continuous
        skip_record_required:
    continuous_only:
      - machine_board
      - recovery_chain_scan
      - latest_route
    recovery_only:
      - latest_board_tail_check
      - release_package_freshness
  subagent_decision:
    strategy: not_needed | read_only_audit | parallel_exploration | sequential_worker | reviewer | inline_fallback | user_proxy_required | audit_timeout_non_blocking
    reason:
  subagent_dispatch_readiness:
    batch_id:
    contract_ids:
    selected_pattern:
    parallel_safe:
    dependency_graph:
    learning_preflight_status: pass | fail | not_needed
    capability_probe_status: unavailable | environment_listed | tool_discovered | spawn_attempted
    no_spawn_reason:
  next_stage:
  next_route:
  route_reason:
```

路由事件含义：

| route_event | 触发信号 | 可观察动作 |
| --- | --- | --- |
| `advance` | 当前阶段关闭条件满足 | 进入下一阶段，并写明证据依据 |
| `skip_with_reason` | 低风险、材料充分、阶段产物已被前文覆盖 | 记录跳过理由和不能跳过的后续闸门 |
| `compress` | 用户摩擦预算低或任务很小 | 只保留本阶段最低输出，不展开完整表格 |
| `deepen` | 公共性、高风险、跨领域、长期交付、证据冲突 | 补行业最佳实践、证据矩阵、最小闭环或用户反馈点 |
| `route_back` | 主张、材料、证据、验收或权限不稳 | 回到能修复问题的最早阶段，不继续装作推进 |
| `fork_parallel` | 多个独立来源、领域或失败模式可并行核验 | 调用或计划子代理并行审计，主代理保留最终取舍 |
| `spawn_subagent` | 任务边界清晰、可验收、互不冲突 | 写 `subagent_task_contract` 后分派 |
| `ask_user` | 只有用户能决定价值偏好、授权、成本或外部行动 | 只问 1-2 个高杠杆问题，并说明不问的风险 |
| `blocked` | 缺少权限、材料、环境或连续三轮同一阻塞 | 写明阻塞证据、解除条件和恢复入口 |
| `execute` | 执行前闸门通过 | 进入阶段 10，但仍保持单任务推进和状态写回 |

动态不等于自由裁量。凡是选择 `compress`、`deepen`、`fork_parallel`、`spawn_subagent`、`ask_user`、`blocked`，或在 light / standard / deep / continuous 之间切换，必须写 `routing_decision_log`：说明选了什么、没有选什么、触发证据是什么、对用户摩擦的影响是什么、何时需要重评。

`gate_activation_matrix` 负责把高风险/高返工项目的常驻检查转成动态执行，而不是把所有 guard 全量硬跑。任何 gate 都必须先归类为 always_minimum、risk_based、continuous_only 或 recovery_only；risk_based gate 必须有 activation_predicate 和 minimum_by_mode，跳过时必须写 skip_record_required。若路由表写“默认做”，本控制器仍要说明在当前 mode 下最低做到了哪一层，防止 low friction 被误用为跳过证据，也防止 deep/continuous 自动膨胀成目录式清单。

选择 `fork_parallel` 或 `spawn_subagent` 前，必须先让 `subagent_dispatch_readiness` 通过：至少有 `batch_id`、`contract_ids`、`selected_pattern`、并行安全判断、依赖图、学习前置状态和能力探测状态。若 `learning_preflight_status: fail`、`parallel_safe: false` 且没有隔离方案、或 capability 只停在 `environment_listed`，不得 spawn；应改为 `inline_fallback`、`read_only_audit` 降级、缩小任务或回到阶段 3 补 skill/plugin/外部方法学习。

### 5.0.1 持续优化元项目 profile continuous_optimization_meta_project_profile

当用户要求继续优化本协议、流程或 AI 协作方式时，不另起一套完整协议，而是把现有阶段压缩为一个元项目 profile。该 profile 只规定“本轮为何继续、选哪个问题、怎么证实、何时停止”，细节证据写入 docs 或经验库。

```yaml
continuous_optimization_meta_project_profile:
  continuation_policy:
    default_mode: trigger_based
    valid_triggers: [explicit_user_request, new_real_project_gap, verification_red, high_value_backlog_item]
    no_trigger_behavior: backlog_only_no_new_machine_board
    next_round_entry: latest_machine_board_plus_capability_discovery_cadence_gate_plus_iteration_quality_bar_entry_gate
  iteration_quality_bar:
    round_id:
    entry_gate:
      latest_machine_board:
      recovery_chain_failure_count:
      candidate_count:
      candidate_minimum_score:
      capability_discovery_checked:
      proceed_decision: continue | stop | ask_user
    execution_gate:
      selected_candidate:
      one_main_chain_only:
      micro_task_or_noop_evidence:
      concrete_artifact_or_record_ref:
      source_url_present:
      primary_claim_bounded:
      state_or_field_evidence_status:
        direct_observed:
        unknown_or_not_verified:
      downgrade_rule_present:
      claim_readiness_boundary:
      promotion_recommendation_present:
      user_friction_effect_stated:
      anti_protocol_bloat_decisions:
    exit_gate:
      files_synced:
      verification_commands:
      next_round_decision: continue | stop | ask_user
      may_start_next_round:
  stage_0:
    latest_machine_board:
    continue_reason:
    recovery_chain_status:
  stage_1:
    current_basis:
    not_current_basis:
    gap_classification:
      real_cross_project_gap:
      user_preference:
      tool_layer_inertia:
  stage_2:
    candidate_optimizations:
      - candidate:
        value_for_real_projects: high | medium | low
        user_friction_reduction: high | medium | low
        overclaim_or_misroute_risk_reduction: high | medium | low
        verifiability: high | medium | low
        decision: promote_to_protocol | add_to_experience_library | reject | backlog
        decision_reason:
  stage_4:
    selected_main_chain:
    why_only_one_chain:
  stage_7:
    continue_decision: continue | stop_after_this_round | backlog_only
    stop_condition:
  stage_8:
    smoke_tests:
      - source_url:
        primary_claim:
        selected_lenses:
        micro_task:
        observed_gap:
        downgrade_rule:
  stage_9:
    anti_protocol_bloat_gate:
      protocol_change_allowed:
      verifier_required_allowed:
      experience_library_update:
```

映射关系：

1. `stage_0` 只做恢复：读取最新机器看版，确认本轮为什么还值得继续优化。
2. `stage_1` 只分清依据类型：真实缺口、用户偏好和工具层惯性不得混写。
3. `stage_2` 只列 2-3 个候选优化点，并按真实项目价值、用户摩擦下降、误判风险降低和可验证性排序。
4. `stage_4` 只收束一个最高杠杆主链；其他候选进入 backlog 或经验库。
5. `stage_7` 使用现有评分体系判断是否继续。连续 2 轮真实项目烟测没有暴露新的跨项目失败模式，或候选优化只能增加复杂度但不能降低误判/摩擦时，默认停止连续优化。
6. `stage_8` 必须跑一个 5-30 分钟真实小题或恢复链小题；只写“应该优化”不能作为证据。
7. `stage_9` 必须过 `anti_protocol_bloat_gate` 后才允许改主协议；单一案例细节进入经验库，两个以上真实项目暴露同类失败模式才考虑主协议规则，能被 verifier 稳定检查时才考虑 required 字段。
8. `iteration_quality_bar` 是每轮连续优化的进入/执行/退出标准，不是 verifier required。它必须至少记录 source_url、边界化 primary_claim、micro_task 或 no-op 证据、具体 artifact/record 引用、至少一个 direct_observed 状态或字段、至少一个 unknown/not_verified 状态或字段、downgrade_rule、claim_readiness_boundary、promotion_recommendation 和 user_friction_effect；缺任一项时，本轮只能降级为 source_backed_candidate 或 backlog，不能标记为可进入下一轮。
9. `continuation_policy` 是触发式续跑规则，不是 verifier required。默认 `trigger_based`：只有用户明确指定、新真实项目缺口、验证红灯或高价值 backlog 项成立时才允许新一轮；无触发时不得创建新机器看版，只保留 backlog。

### 5.1 阶段深度梯 stage_depth_ladder

```yaml
stage_depth_ladder:
  light:
    use_when: 低风险、小修小补、单文件说明、用户只要快速判断
    minimum_outputs:
      - current_basis
      - primary_claim_or_task
      - one_route_reason
      - next_route
    forbidden_overhead:
      - 不为小任务强制写完整十阶段报告
      - 不为了仪式感调用子代理或创建 Goal
  standard:
    use_when: 标准复杂项目、需要交付方案、报告、代码或多步骤执行
    minimum_outputs:
      - current_basis
      - best_practice_implications
      - main_chain
      - plan_with_acceptance
      - minimum_loop
      - pre_execution_gate
  deep:
    use_when: 公共性、高风险、跨领域、未成年人、隐私、财务、法律、安全、长期承接、正式发布或用户明确重视质量
    minimum_outputs:
      - industry_best_practice_scan
      - evidence_matrix
      - decision_log
      - traceability_matrix
      - micro_task_execution_check
      - risk_ethics_permission
      - artifact_or_code_key_node_scan
      - recovery_chain_update
  continuous:
    use_when: 用户说继续任务、持续推进、优化你自己、直到我手动停止
    minimum_outputs:
      - latest_machine_board_read
      - one_highest_leverage_task
      - post_change_scan
      - new_machine_board
      - next_route
```

深度选择规则：

1. 默认从 `standard` 起步；任务很小才降到 `light`，公共性或高风险才升到 `deep`。
2. `continuous` 不是无限扩写；每轮只能处理一个最高杠杆问题，结束时必须留下可恢复状态。
3. 深度可以动态变化：发现证据冲突、权限问题、外部依赖或用户隐性标准时立即 `deepen` 或 `route_back`。
4. 深度降低必须记录理由；不能用“低摩擦”逃避必要证据、授权或验收。
5. 深度选择必须记录 alternatives_considered；尤其当项目同时像小任务、高风险/高返工项目和长期项目时，要说明为什么没有选择其他深度。

### 5.1.1 项目性质剖面 project_nature_profiles

`stage_depth_ladder` 决定投入深度，`project_nature_profiles` 决定治理重心。二者必须同时判断：一个项目可以是轻量但模型发现型，也可以是深度但证据填充型。不得把所有复杂项目都当成“证据审计 + 工具选择 + 小 Loop”。

```yaml
project_nature_profiles:
  evidence_fill:
    use_when: 模型、公式、评价表、研究框架、变量口径或交付结构已经稳定
    priority:
      - current_basis
      - evidence_matrix
      - source_authority
      - verification
      - delivery_contract
    divergence_requirement: 可轻量记录 divergence_noop_reason，不强制展开候选框架池
    forbidden:
      - 为了显得发散而重复拆分已稳定模型
      - 每轮机械重跑完整外部能力盘点
  model_discovery:
    use_when: 研究问题、解释框架、模型假设、变量关系、叙事主线或方法路线尚未确定
    priority:
      - problem_definition_quality
      - candidate_frameworks
      - ibis_argument_map
      - thought_search_pool
      - discriminating_probe
      - convergence_conditions
    minimum_outputs:
      - 3-5 个候选框架；少于 3 个必须说明问题空间为什么已足够窄
      - 每个框架的核心假设、支持理由、反对理由、可解释边界、最小探针和淘汰/保留条件
      - 至少一个能区分候选框架的探针，而不是只补最容易找到的材料
    forbidden:
      - 在问题定义未稳时直接进入 evidence_matrix 主导
      - 把局部资料缺口、工具缺口或可快速完成的小任务当成主目标
  mixed:
    use_when: 先要发现模型或研究主线，再进入资料、数据、证据填充和交付
    rule: 收敛前按 model_discovery；满足 convergence_switch_conditions 后切回 evidence_fill
  execution_delivery:
    use_when: 方案和验收标准已经定义，任务主要是实现、整理、发布前检查或交付
    priority:
      - acceptance_criteria
      - implementation_plan
      - verification
      - side_effect_boundary
      - delivery_contract
    divergence_requirement: 只记录执行路线的关键替代方案和拒绝理由
convergence_switch_conditions:
  - 选定或暂定一个主框架
  - 至少记录两个被拒绝或降级的替代框架及理由
  - 写清可区分探针、探针结果或为何暂时不能执行
  - 证据路径和资料类型已经清楚
  - 用户可理解的主问题表述稳定
  - 下一轮 route 从“探索框架”转为“填证据 / 执行 / 交付”有明确理由
```

### 5.1.2 自适应深层判断层 adaptive_judgment_layer

自适应深层判断层回答一个问题：哪些细节应该交给项目现场的 AI 判断，哪些边界必须回到用户或人工授权。默认采用 `strong_autonomy_with_guardrails`，即 AI 不因可逆细节频繁打扰用户，但必须把关键判断理由和回滚路径留给后续恢复。

```yaml
adaptive_judgment_controller:
  inputs:
    project_nature:
    convergence_status:
    current_basis:
    uncertainty_level: low | medium | high
    reversibility: reversible | partly_reversible | irreversible
    side_effect_level: none | local_write | external_read | external_write | account_or_permission | real_world_action
    user_boundary:
    evidence_status:
    capability_state:
    collaboration_topology:
    delivery_contract:
  outputs:
    judgment_mode: fast | diagnostic | exploratory | strategic | critical
    autonomy_level: strong_autonomy_with_guardrails
    decision_right: ai_decide | ask_user | manual_action_required | blocked_until_authorized
    route_event: advance | compress | deepen | route_back | ask_user | blocked | execute
    confidence_state:
    ask_user_needed:
    ai_decided_without_user_reason:
    rollback_or_recovery_route:
decision_rights_matrix:
  ai_can_decide:
    - plan_detail_order
    - loop_probe_shape
    - capability_candidate_selection_or_rejection
    - evidence_depth_within_existing_boundary
    - temporary_subagent_assignment
    - long_running_thread_scope_micro_adjustment
    - divergence_or_convergence_pacing
    - lightweight_keep_when_no_refresh_event
    - reversible_local_organization_change
  must_ask_user:
    - main_goal_change
    - delivery_audience_or_public_claim_change
    - account_api_payment_publish_or_external_write
    - irreversible_file_operation
    - high_risk_real_world_action
    - privacy_security_legal_boundary_change
    - insufficient_evidence_but_external_strong_claim_requested
judgment_depth_ladder:
  fast:
    use_when: routine_low_risk_reversible_execution
    record: one_sentence_reason
  diagnostic:
    use_when: blocked_conflict_validation_failure_or_repeated_same_gap
    record: failure_signal_root_suspect_next_probe
  exploratory:
    use_when: model_discovery_or_framework_unsettled
    record: candidate_pool_discriminating_probe_convergence_risk
  strategic:
    use_when: main_chain_project_nature_topology_capability_or_delivery_direction_changes
    record: selected_route_rejected_routes_misjudgment_risk_recovery_route
  critical:
    use_when: high_risk_external_side_effect_formal_delivery_or_public_claim
    record: authorization_evidence_guardrail_manual_action_or_blocked_reason
route_evaluator_reflection_gate:
  trigger: judgment_mode in [strategic, critical]
  minimum_record:
    selected_route:
    rejected_routes:
    why_selected:
    highest_misjudgment_risk:
    counterexample_or_hostile_case:
    rollback_or_recovery_route:
    user_visible_summary_needed:
```

### 5.2 子代理编排梯 subagent_orchestration_ladder

子代理是降低盲区和并行核验的工具，不是替主代理承担判断的借口。每次调用前先判断是否真的有独立任务、清晰边界和可验收输出。

#### 代理编排能力构造器 agentic_orchestration_capability_builder

当用户要求学习网上方法、skill、插件或提升子代理解决问题能力时，先运行本构造器，再进入具体 `subagent_problem_decomposition_builder`。本构造器只吸收可迁移的方法，不复制外部框架目录；可参考本地 Superpowers skill 的独立问题域/两阶段 review 规则、OpenAI Agents SDK 的 handoff/guardrail/tracing 思路、Anthropic effective agents 的 routing/parallelization/orchestrator-workers/evaluator-optimizer 模式、LangChain/LangGraph 的 supervisor-subagents / handoffs / context engineering 思路，以及当前 Codex 实际可调用的 spawn/wait/close 工具能力。外部方法只能证明“可用模式”，不能证明当前会话可调用、当前项目适配或子代理输出正确。

```yaml
agentic_orchestration_capability_builder:
  capability_gap:
    current_project_gap:
    why_single_agent_is_insufficient:
    why_subagent_may_help:
    why_subagent_may_hurt:
  method_source_mix:
    local_skill_or_plugin_rules:
    external_method_sources:
    method_transfer_matrix:
      - method_source:
        source_role: local_hard_rule | official_pattern | framework_pattern | current_runtime_capability
        extracted_principle:
        solves_failure_mode:
        fit_signal:
        reject_signal:
        generated_work_unit:
        context_packet_requirement:
        review_or_guardrail:
        minimum_application_test:
        acceptance_evidence:
        non_transfer_boundary:
        downgrade_route:
    method_source_role_map:
      - source:
        role: local_hard_rule | official_pattern | framework_pattern | current_runtime_capability
        can_support:
        cannot_support:
        transferred_method:
        non_transfer_boundary:
    codex_tool_capability_probe:
      environment_listed:
      tool_discovered:
      callable_tools:
      spawn_attempted:
      agent_returned:
      result_integrated:
      capability_status: unavailable | available | inline_fallback
  subagent_orchestration_pattern_router:
    single_agent_sufficiency_gate:
      single_agent_sufficient:
      reason:
      cost_conflict_context_risk:
    candidate_patterns:
      - pattern: single_agent | agents_as_tools | routing | parallel_evidence_lanes | orchestrator_workers | evaluator_optimizer | handoff | reviewer_loop | group_chat | code_or_rule_router
        fit_signal:
        expected_benefit:
        cost_or_conflict_risk:
        context_packet_requirement:
        acceptance_evidence:
    selected_pattern:
    rejected_patterns:
      - pattern:
        rejection_reason:
    method_to_work_unit_mapping:
      - source_method:
        independent_work_unit_ref:
        context_isolation_rule:
        role_selection_reason:
        acceptance_check:
    context_packet_completeness:
      task_full_text:
      relevant_files_or_urls:
      excluded_context:
      forbidden_actions:
      output_contract:
      acceptance_checks:
    minimum_application_test:
    downgrade_if_missing:
  agent_topology_selection_trace:
    topology_options_considered:
      - topology: single_agent | agents_as_tools | handoff | parallel_evidence_lanes | orchestrator_workers | evaluator_optimizer | reviewer_loop | group_chat | user_proxy
        fit_signal:
        rejected_or_selected_reason:
        context_boundary:
        state_write_boundary:
        final_answer_owner:
        cost_or_latency_risk:
    selected_topology:
    control_plane:
      main_agent_owns_goal_and_final_claim: true
      subagent_can_write_external_state: false
      subagent_can_edit_files: no | listed_files_only | isolated_worktree_only
      human_or_user_proxy_owner:
    context_engineering:
      minimal_context_packet:
      excluded_context:
      allowed_extra_reads:
      exact_questions:
      output_schema:
    guardrails_and_review:
      pre_spawn_guardrails:
      tool_or_side_effect_guard:
      spec_review_required:
      quality_or_risk_review_required:
      coverage_gate_required:
    parallelism_and_state_safety:
      independent_lanes:
      shared_state_conflict:
      dependency_graph:
      batch_id:
    cost_benefit_and_downgrade:
      why_not_single_agent:
      expected_value_overhead_ratio:
      downgrade_to_inline_if:
      stop_or_user_proxy_if:
    source_backed_method_basis:
      local_skill_basis:
      official_or_primary_sources:
      current_runtime_tool_basis:
      non_transfer_boundary:
    minimum_application_test:
    topology_decision:
  decomposition_gate:
    independent_work_units_ready:
    rejected_decomposition_options:
    controller_prepared_context_packet:
    acceptance_evidence_ready:
    shared_state_conflict:
    main_agent_low_cost_inline:
    high_risk_or_user_judgment_required:
    decision: no_spawn | read_only_audit | parallel_exploration | worker | reviewer | inline_fallback | user_proxy_required
  task_contract_shape:
    contract_id:
    plan_item_id:
    claim_lane_id_optional:
    role: read_only_auditor | worker | spec_reviewer | quality_reviewer | integration_reviewer
    role_selection_reason:
    scope:
    controller_prepared_context_packet_quality:
      task_full_text_included:
      exact_questions_included:
      relevant_files_or_urls_included:
      excluded_context_declared:
      acceptance_checks_included:
    subagent_instruction_packet:
      skill_or_plugin_constraints_read_by_main_agent:
      external_method_constraints:
      allowed_tool_discovery:
      forbidden_actions:
      source_paths_or_urls:
    write_scope: none | listed_files_only | isolated_worktree
    allowed_actions:
    forbidden_actions:
    expected_output:
    review_gate: none | spec_review | quality_review | two_stage_review
  integration_gate:
    coverage_checked:
    conflicts_found:
    adopted_from_method:
    rejected_or_not_transferable:
    integration_decision: accepted | partially_accepted | rejected | conflicted | timeout_non_blocking
    main_agent_final_decision_required: true
  lifecycle_gate:
    agent_return_status: not_started | running | returned | timed_out | blocked | failed | done_with_concerns | needs_context
    timeout_policy_detail:
      critical_path:
      deadline_or_check_interval:
      fallback_action:
      what_was_not_verified:
      reopen_condition:
    close_status: not_needed | closed | keep_open_with_reason | cleanup_unresolved
```

判断规则：

1. 学习 skill/plugin/外部方法时，必须先做 `method_source_role_map`：本地 skill/plugin 只能证明本环境的硬规则，官方/公司文档只能证明可迁移模式，当前工具发现只能证明本会话能力；三者不能互相替代。学习结果必须转成 `controller_prepared_context_packet`、`task_contract_shape`、`review_gate`、`integration_gate` 或 `lifecycle_gate` 之一；只写“参考 OpenAI / LangGraph / AutoGen / CrewAI / Anthropic / Superpowers”不能晋升。
   补充：`method_transfer_matrix` 是方法迁移闸门。每个外部方法、skill 或插件必须写清 fit_signal、reject_signal、generated_work_unit、minimum_application_test、acceptance_evidence 和 non_transfer_boundary；缺任一项时只能进入经验库候选，不能写成主协议能力。`capability_resolution_order` 必须先区分 active_local_skill_or_tool、tool_discovered、installable、authorized 和 side_effect_level；environment_listed != callable，installable != authorized。
2. `subagent_orchestration_pattern_router` 是方法落地闸门：先判断单代理是否足够，再选择 routing、agents_as_tools、parallel_evidence_lanes、orchestrator_workers、evaluator_optimizer、handoff、reviewer_loop、group_chat 或 code_or_rule_router。必须写 `rejected_patterns` 和 `method_to_work_unit_mapping`，说明外部原则如何生成具体 work unit、上下文隔离规则、角色选择理由和验收项；缺映射时只能停在方法候选。
3. `agent_topology_selection_trace` 是派工前的拓扑闸门：OpenAI Agents SDK 中 agents-as-tools 保留主代理控制，handoff 转交控制权；LangChain/LangGraph 强调 subagents、handoffs 和 context engineering；Superpowers 强调独立问题域、上下文隔离、两阶段 review；AutoGen 类 group chat 需要参与者、终止条件和状态管理。这些只能抽象为当前项目的拓扑选择，不能直接替代当前会话的能力探测、上下文包、验收证据和主代理集成。缺 `final_answer_owner`、`state_write_boundary`、`context_boundary`、`dependency_graph` 或 `downgrade_to_inline_if` 时，不得 spawn。
4. `capability_status: available` 必须有 `tool_discovered` 或 `spawn_attempted` 证据；只有环境列出子代理名时，最多写 `environment_listed`。
5. read_only_audit 可并行；worker 默认串行。只有写入范围隔离、计划清楚、验收命令明确、集成 owner 明确时，才考虑并行 worker。
6. 两阶段 review 的顺序是 spec/requirements compliance 先于 quality/risk review；前者未通过时，不进入后者。
7. `done_with_concerns` 先审 concerns；`needs_context` 补上下文；`blocked` 必须缩小任务、换策略/模型或修计划；不得用同一 prompt 原样重试。
8. 主代理保留最终判断：目标解释、用户偏好、是否调用子代理、证据等级、claim readiness、Plan/Goal 更新、外部写入授权、高风险操作和最终交付表述，都不能下放给子代理。

#### 子代理问题拆解构造器 subagent_problem_decomposition_builder

先拆问题，再调用子代理。外部多代理框架、Superpowers skill 和 Codex subagent 工具的共性不是“多开几个 agent”，而是把任务拆成边界清楚、上下文隔离、可验收、可集成的工作包。

```yaml
subagent_problem_decomposition_builder:
  problem_summary:
  decomposition_decision: spawn | no_spawn | inline_fallback | user_proxy_required
  why_now:
  spawn_preflight:
    bounded_work_unit_ready:
    context_packet_ready:
    acceptance_ready:
    shared_state_conflict:
    main_agent_low_cost_inline:
    user_judgment_required:
    decision:
  dependency_boundary_check:
    same_root_cause_likely:
    shared_files_or_state:
    ordering_dependency:
    one_fix_may_resolve_others:
    parallel_safe:
    decision:
  parallel_evidence_lane_trace:
    trigger: same_root_cause_likely_but_evidence_sources_are_independently_auditable
    claim_lane_binding:
      primary_claim_ladder_level:
      lane_supported_claim_level:
      evidence_contract_ref:
      can_support_claims:
      cannot_support_claims:
      impact_inference_guard:
      deployment_readiness_gate:
        trigger: claim_reaches_real_world_use_or_deployment
        external_validity_evidence:
        workflow_or_user_evidence:
        risk_safety_permission_evidence:
        regulatory_or_policy_boundary:
        monitoring_and_handoff_plan:
        downgrade_if_missing:
    evidence_lanes:
      - lane_id:
        role: read_only_audit
        claim_lane_binding:
          claim_ladder_level: output | process | quality | uptake | outcome | long_term_impact
          can_support_claims:
          cannot_support_claims:
        output_contract:
        forbidden_actions:
        write_scope: none
    shared_final_decision: main_agent_only
    integration_key:
    merge_conflict_rule:
  independent_work_units:
    - role:
      task_boundary:
      controller_prepared_context_packet:
        task_full_text:
        files_or_urls:
        relevant_snippets_with_line_refs:
        known_errors_or_questions:
        constraints:
        acceptance_checks:
        excluded_context:
        allowed_extra_reads:
      input_context_packet:
        files_or_urls:
        exact_questions:
        relevant_constraints:
        excluded_context:
      output_contract:
      acceptance_evidence:
      write_scope: none | listed_files_only | isolated_worktree
      conflict_risk: low | medium | high
      review_gate: none | spec_review | quality_review | two_stage_review
      skill_or_plugin_to_use:
      timeout_policy:
        critical_path:
        deadline_or_check_interval:
        fallback_action:
        what_was_not_verified:
        reopen_condition:
      plan_subagent_binding:
        goal_id_optional:
        plan_item_id:
        contract_id:
        review_gate:
        main_agent_updates_plan_only: true
      subagent_instruction_packet:
        instruction_sources_read_by_main_agent:
        hard_constraints:
        allowed_actions:
        forbidden_actions:
        allow_subagent_tool_discovery:
        excluded_context:
  coordination_model: llm_orchestrated | code_or_rule_orchestrated | hybrid
  context_isolation_rule:
  main_agent_integration_plan:
  best_practice_learning_contract:
    trigger_source: user_request | stage_gap | high_risk | unfamiliar_domain | subagent_method_gap
    stage_gap:
    source_role_map:
    practice_pattern_extracted:
    failure_mode_learned:
    project_stage_gap_addressed:
    non_transfer_boundary:
    minimum_application_test:
    downgrade_if_not_tested:
  capability_discovery_cadence_gate:
    initial_scan:
      status: done | intentionally_skipped
      scanned_surfaces: [local_skills, callable_tools, deferred_tools, plugins_connectors, external_apis_methods]
      candidates_considered: []
      selected_now: []
      rejected_now: []
      backlog: []
      skip_reason:
    event_triggered_capability_refresh:
      required_triggers: [stage_transition, project_nature_change, main_chain_change, evidence_path_change, new_user_requirement, blocked_or_failing_verification, external_write_or_subagent_boundary, delivery_audience_change, before_final_claim]
      trigger_event:
      last_checked_at_stage:
      result: refresh | lightweight_keep | defer_until_probe_or_evidence_path
      next_check:
    periodic_reconsideration_legacy_alias:
      status: superseded_by_event_triggered_capability_refresh
    lightweight_exception:
  skill_plugin_discovery_gate:
    discovery_basis:
    capability_resolution_order:
      - active_local_skill_or_tool
      - tool_search_or_current_tool_table
      - read_required_instructions
      - side_effect_gate
      - explicit_install_or_auth_or_external_write_authorization
    candidate_list:
      - capability_name:
        capability_type: skill | plugin | connector | local_tool | web_source | external_method
        selection_reason:
        rejection_reason:
    selected:
    instruction_read_evidence:
    call_or_skip_decision:
  capability_type_and_side_effect_gate:
    capability_type: skill | plugin | connector | local_tool | web_source | external_method
    operation_mode: read_instructions | call_tool | install | authenticate | write_external_state
    side_effect_level: none | local_read | local_write | external_read | external_write | account_or_permission
    permission_or_manual_action_required:
    sensitive_data_boundary:
    external_state_write_allowed:
  external_state_write_guard:
    permission_scope_requested: none | local_only | repo_read | repo_write | classroom_admin | lms_course_read | lms_course_write | gradebook_read | gradebook_write | roster_read | account_admin
    external_state_target: none | github_repo | github_classroom | lms_course | lms_lti_registration | lms_gradebook | lms_roster | user_account | public_publication
    sensitive_data_class: none | public_docs | course_config | student_identity | student_submission | roster | grades | credentials | security_keys
    subagent_capability_boundary: read_only_no_tools | read_only_local_tools | web_source_only | connector_read_only | no_plugin_or_connector | explicit_user_authorization_required
    sandbox_or_dry_run_evidence:
    rollback_or_reversal_plan:
    explicit_user_authorization:
    manual_action_required_if_missing:
  integration_lifecycle_gate:
    integration_claim:
    component_capabilities:
      - component:
        claimed_standard_or_api:
        source_role_map_ref:
        cannot_imply_end_to_end_success:
    same_version_deployment_evidence:
    end_to_end_flow_evidence:
    lifecycle_signals:
      maintenance_mode:
      sunset_or_deprecation:
      new_user_freeze:
      partner_transition:
      retirement_or_data_deletion_date:
      support_policy_change:
    readiness_level_after_gate: source_backed_compatibility_candidate | locally_verified | small_loop_validated | pilot_ready | production_or_public_claim_ready_blocked
    downgrade_rule:
  transactional_integration_consistency_guard:
    trigger: external_state_change_depends_on_async_events_or_retriable_requests
    idempotency_key_or_dedup_strategy:
    duplicate_event_handling:
    retry_and_replay_policy:
    event_ordering_assumption:
    source_of_truth:
    reconciliation_or_audit_log:
    test_vs_live_mode_boundary:
    high_impact_action_compensation_plan:
    downgrade_if_missing: source_backed_or_sandbox_validated_only
  desired_state_reconciliation_guard:
    trigger: declared_configuration_controls_external_resources_or_runtime_state
    desired_state_source:
    observed_state_source:
    target_scope:
    execution_model: plan_apply | controller_loop | manual_sync | auto_sync | other
    plan_or_diff_review:
    drift_detection:
    state_lock_or_concurrency_control:
    destructive_change_gate:
    adoption_or_import_rule:
    rollback_or_forward_fix_plan:
    policy_or_permission_gate:
    operator_handoff:
    downgrade_if_missing:
  stateful_data_migration_guard:
    trigger: persistent_data_or_schema_change_affects_live_read_write_paths
    migration_scope:
    expand_contract_or_compatibility_plan:
    old_new_code_read_write_overlap:
    backfill_or_batching_plan:
    lock_timeout_and_online_operation_check:
    constraint_index_validation_plan:
    data_correctness_verification:
    rollback_or_roll_forward_boundary:
    feature_flag_or_release_order:
    observability_and_pause_resume_plan:
    owner_runbook_handoff:
    downgrade_if_missing:
  security_incident_response_guard:
    trigger: vulnerability_incident_secret_leak_advisory_scanner_alert_or_security_fix_claim
    source_type: incident | vulnerability | secret_leak | advisory | scanner_alert | poc | ctf | issue_pr
    claim_type: exploitability | active_exploitation | compromise | data_access | data_exfiltration | affected_version | fixed_version | remediation_verified
    evidence_level: lead | plausible | validated | confirmed | published
    affected_asset_scope:
    authorization_and_contact_boundary:
    severity_or_priority_basis:
    exploitation_or_compromise_state: none | poc | active | compromise_confirmed | unknown
    containment_or_mitigation_status:
    credential_rotation_or_secret_revocation:
    impact_scope:
    remediation_verification:
    coordination_or_disclosure_state: unreported | reported | acknowledged | coordinating | embargoed | published
    notification_requirements:
    monitoring_and_recurrence_check:
    post_incident_review_owner:
    cannot_conclude:
    downgrade_if_missing:
  data_artifact_lineage_freshness_guard:
    trigger: data_report_model_table_figure_metric_or_analysis_artifact_supports_claim_or_downstream_decision
    artifact_id:
    artifact_type: dataset | report | model | figure | table | metric | dashboard | analysis_output | other
    owner:
    status: draft | active | deprecated | superseded | unknown
    version:
    artifact_path_or_uri:
    source_assets:
    input_versions_or_hashes:
    source_current_as_of:
    produced_at_or_refreshed_at:
    code_ref:
    run_id:
    parameters_ref:
    environment_ref:
    transformation_logic:
    lineage_ref:
    freshness_policy:
    freshness_checked_at:
    freshness_status: fresh | stale | unknown | blocked
    validation_suite_ref:
    validation_checked_at:
    validation_status: pass | fail | unknown | blocked
    artifact_checksum:
    reproduction_recipe_ref:
    downstream_references:
    intended_use:
    known_caveats:
    previous_or_superseded_version:
    downgrade_if_stale:
    field_evidence_status:
      - field_name:
        evidence_status: direct_observed | derived_from_metadata | inferred | unknown | not_applicable
        evidence_uri_or_hash:
        extracted_value:
        gap_action:
  skill_plugin_learning_loop:
    trigger:
    discovery_question:
    selected_skill_or_plugin:
    instruction_source:
    instruction_read_status: not_needed | read_complete | read_blocked
    external_method_sources:
      - source_name:
        source_url_or_path:
        method_claim:
        usable_constraint:
        cannot_prove:
    key_constraints_extracted:
    practice_micro_task_ref:
    practice_result: not_needed | pass | fail | blocked
    adoption_decision: adopt | partially_adopt | reject | backlog
    protocol_writeback_ref:
    verifier_requirement_ref:
    recovery_chain_ref:
  skill_plugin_project_fit_trace:
    project_context:
    primary_claim_or_stage_gap:
    pre_skill_gap:
    selected_skill_or_plugin:
    transferred_method:
    micro_task_before_after:
    acceptance_evidence:
    non_transfer_boundary:
    reuse_decision: reusable | project_only | reject | backlog
  subagent_method_learning_trace:
    source_mix:
      local_skill_or_plugin:
      online_or_official_method:
      codex_tool_capability:
    method_synthesis:
      independent_domain_rule:
      context_isolation_rule:
      handoff_or_guardrail_rule:
      review_and_integration_rule:
      tool_discovery_permission_rule:
      method_to_work_unit_mapping:
    micro_task_used_to_validate:
    adopted_into_subagent_contract:
    rejected_or_backlogged_parts:
  subagent_orchestration_pattern_router:
    single_agent_sufficiency_gate:
    selected_pattern:
    rejected_patterns:
    method_to_work_unit_mapping:
    role_selection_reason:
    context_packet_completeness:
    minimum_application_test:
    downgrade_if_missing:
  agentic_orchestration_capability_builder:
    capability_gap:
    method_source_mix:
    subagent_orchestration_pattern_router:
    controller_prepared_context_packet:
    spawn_or_inline_decision:
    task_contract_shape:
    integration_gate:
    lifecycle_gate:
  subagent_result_coverage_gate:
    contract_items:
    returned_items:
    unverified_items:
    out_of_scope_items:
    blocking_gaps_after_integration:
    main_agent_followup_checks:
  main_agent_integration_review:
    subagent_outputs_received:
    conflicts_found:
    integration_decision:
    adopted_claims:
    rejected_claims:
    final_claim_changed:
    reason_for_rejection_or_downgrade:
  claim_readiness_ladder:
    final_claim:
    current_level: idea_or_candidate | source_backed | locally_verified | small_loop_validated | pilot_ready | production_or_public_claim_ready
    evidence_required_for_next_level:
    downgrade_rule:
  review_pipeline:
    spec_review_status: not_needed | pending | pass | issues_found
    quality_or_risk_review_status: not_needed | pending | pass | issues_found
    open_findings_by_severity:
    fix_owner:
    re_review_required:
  subagent_lifecycle_ledger:
    - contract_id:
      agent_id:
      role:
      agent_return_status: done | done_with_concerns | needs_context | blocked | failed | timed_out
      summary:
      accepted_items:
      rejected_items:
      conflict_items:
      main_agent_local_checks:
      integration_decision:
      close_status:
      cleanup_decision:
  no_spawn_reason:
  lifecycle_cleanup_plan:
```

判断规则：

1. `spawn_preflight` 是硬闸门：`bounded_work_unit_ready`、`context_packet_ready`、`acceptance_ready` 任一不成立，或 `shared_state_conflict`、`main_agent_low_cost_inline`、`user_judgment_required` 任一成立且无法隔离时，必须 `decomposition_decision: no_spawn | inline_fallback`。
2. 多个问题不等于可并行；先做 `dependency_boundary_check`。若 `same_root_cause_likely`、`ordering_dependency` 或 `one_fix_may_resolve_others` 为 true，先由主代理或单一 agent 收敛根因。

并行证据泳道例外：当最终根因、修复方案或维护者动作高度耦合时，禁止并行 root-cause worker 或 fix worker；但如果日志、来源、权限、triage、代码阅读或评审标准可以独立核验，可以开启 `parallel_evidence_lane_trace`。每条 lane 必须是 `read_only_audit`、`write_scope: none`，只交付可核验证据、候选假设和缺口，并显式禁止最终根因裁决、修复选择、评论外部 issue、改标签、开 PR 或执行高风险动作。最终判断必须由主代理在 `main_agent_integration_plan` / `integration_decision` 中完成。

证据泳道必须绑定主张层级：每条 lane 必须填写 `claim_lane_binding`，说明它能支撑 `claim_ladder` 中的哪一层主张，不能支撑哪一层主张。活动量、参与人数、任务完成数、代码提交、地图覆盖、问卷样本或模型指标只能支撑相应的输出/过程/质量主张；不能直接证明真实使用、受益者结果、公共影响或长期改变。若最终报告需要 outcome / impact 主张，必须另有使用者、利益相关方、现场反馈、独立评估、长期追踪或反事实比较等证据；缺失时按最弱证据泳道降级表述。

部署/真实使用证据门：当主张从 benchmark、demo、竞赛、样机、论文指标、离线评估或内部验收上升到真实使用、临床/教育/工程部署、用户决策、公共服务运行或商业交付时，必须补 `deployment_readiness_gate`。最低要求包括外部有效性或真实场景验证、工作流/使用者证据、风险安全与授权边界、监管/政策/合规边界、运维监控与责任承接。缺任一关键证据时，只能表述为“在给定测试/数据/场景下表现良好”或“具备进一步验证潜力”，不能写成“可部署”“已改善决策/诊疗/学习/生产”。

3. 如果任务不能写出 `independent_work_units`，说明问题尚未拆清，先 inline 梳理，不 spawn。
4. 子代理上下文必须是主代理整理出的 `controller_prepared_context_packet`，包括完整任务文本、关键文件/链接、行号片段、已知问题、约束、验收检查、排除项和允许额外读取范围；不能把整段会话、整份计划或大目录扔给子代理后让其自己猜重点。若子代理返回 `needs_context`，主代理补包后重派，不能原 prompt 重试。
5. 能用规则或代码路由的任务优先 `code_or_rule_orchestrated`，例如分类后选择固定 reviewer；需要开放探索、来源核验或领域判断时才使用 `llm_orchestrated` 或 `hybrid`。
6. `read_only_audit` 可以并行；`worker` 默认串行。只有 isolated_worktree、无共享状态、明确 merge owner、明确验证命令和 review gate 时，才允许并行写入型 worker。
7. worker 子代理必须有写入范围和验收命令；read_only_audit 子代理必须禁止编辑和最终裁决。
8. 重大代码、协议、报告或交付物变更后，优先使用两阶段审查：先 spec/requirement compliance，再 quality/risk review；Critical/Important finding 未修复或未证据化拒收前不得关闭。
9. 子代理输出只是一种证据，必须进入 `subagent_lifecycle_ledger` 和 `main_agent_integration_plan`，记录 accepted、partially_accepted、rejected 或 conflict；主代理保留最终判断。
10. 子代理返回状态必须使用 `agent_return_status`。`done_with_concerns` 先审 concerns；`needs_context` 补上下文；`blocked` 要缩小任务、换模型/策略或修计划；不得用相同 prompt 原样重试。
11. Plan/Goal 与子代理契约必须通过 `plan_subagent_binding` 绑定；子代理永不创建、完成或改写 Goal，只有主代理在集成和 review 后更新 Plan。
12. skill/plugin 发现默认由主代理完成。主代理必须读取必要 skill/plugin 指令，并把相关摘取成 `subagent_instruction_packet`；只有 `subagent_task_contract` 明确允许、side_effect_level 为 none 或 local_read、且 `subagent_tool_discovery_permission_gate` 已限定范围时，才允许子代理自行 tool discovery。
13. 新任务启动、连续优化轮次恢复或重大阶段切换后，必须先补 `capability_discovery_cadence_gate`，记录 initial_scan 是否覆盖 local_skills、callable_tools、deferred_tools、plugins_connectors、external_apis_methods，并写明 selected_now、rejected_now、backlog、last_checked_at_stage 和 next_check；后续复盘采用事件触发优先，遇到 stage_transition、project_nature_change、main_chain_change、evidence_path_change、new_user_requirement、blocked_or_failing_verification、external_write_or_subagent_boundary、delivery_audience_change 或 before_final_claim 时必须复盘。连续节拍中 3 轮只是兜底上限；无触发时写 lightweight keep，不重跑完整能力发现。小型本地任务可写 intentionally_skipped，但必须说明已有本地工具足够，不强制联网或 tool_search。
14. 如果用户明确提到 skill/plugin，或当前任务显然适配一个现有 skill/plugin，或本轮目标是提升 agent/tool/subagent 能力，必须先补 `skill_plugin_discovery_gate` 和 `capability_type_and_side_effect_gate`，再补 `skill_plugin_learning_loop`。闭环至少说明候选集、选择/拒绝理由、指令是否读完、抽取的硬约束、小题或实际试用证据、采纳/拒收决定、写回协议位置、验证器覆盖项和恢复链引用。只写“已学习/已参考”不算闭环。
15. 外部最佳实践、官方方法或网上 agent 编排资料必须进入 `best_practice_learning_contract`：记录 stage_gap、source_role_map、practice_pattern_extracted、failure_mode_learned、project_stage_gap_addressed、non_transfer_boundary 和 minimum_application_test。没有最小应用测试时，只能写成候选方法，不能晋升为主规则。
16. 凡 `capability_type_and_side_effect_gate.operation_mode` 是 install / authenticate / write_external_state，或 side_effect_level 是 external_write / account_or_permission，必须补 `external_state_write_guard`。如果 permission_scope_requested、external_state_target、sensitive_data_class、subagent_capability_boundary、sandbox_or_dry_run_evidence、rollback_or_reversal_plan 或 explicit_user_authorization 任一缺失，主代理只能继续只读分析、写 `manual_action_required` 或改走沙盒/模拟路径；不得让子代理、浏览器、CLI、plugin 或 connector 尝试外部写入。
17. 凡项目主张涉及“两个或多个系统能互通/兼容/集成/上线/长期承接”，必须补 `integration_lifecycle_gate`。单边标准能力或认证只能给出 source_backed_compatibility_candidate；同一版本、同一部署、同一关键流程的端到端证据才能上升到 locally_verified 或 small_loop_validated；维护模式、退役、停止新用户、迁移伙伴、数据删除日、SLA/支持变化等生命周期信号自动阻断 production_or_public_claim_ready。
18. `skill_plugin_learning_loop` 必须同时补 `skill_plugin_project_fit_trace`：说明该 skill/plugin 改善了当前真实项目的哪条主张、阶段缺口、验收链、协作方式或交付证据；记录学习前缺口、迁移的方法、小题前后差异、验收证据、不能迁移的边界和复用决定。若只是工具学习而没有项目价值增量，必须写 `reuse_decision: backlog | reject`，不能晋升为主规则。
19. 当用户要求“学习网上的方法、skill、插件来提升子代理能力”，或当前子代理分工质量不足时，必须补 `subagent_method_learning_trace`。最低来源组合是：一个本地 skill/plugin 规则、一个可核验的外部/官方方法来源、一个当前 Codex 可调用工具能力；若网络不可用或工具不可用，记录 `read_blocked` / `inline_fallback`。最终只吸收可触发、可验收、可写入 contract 的方法，例如独立问题域、上下文隔离、handoff/guardrail、两阶段 review、结果覆盖检查和主代理集成裁决；不得把外部框架名、模型名或平台宣传写成规则。被采纳的方法必须能生成 `contract_id`、`plan_item_id`、`subagent_instruction_packet`、timeout fallback 和 integration review；缺这些字段时停在经验库候选。
20. `agentic_orchestration_capability_builder` 必须把学习结果转成可执行能力：method_source_mix 说明本地 skill、外部方法和 Codex 工具各自能支撑什么；`controller_prepared_context_packet` 说明主代理准备给子代理的最小上下文；`spawn_or_inline_decision` 说明为什么开或不开；`integration_gate` 说明主代理如何接受、拒收或降级；`lifecycle_gate` 说明返回、超时、阻塞和关闭处理。缺这些字段时，只能写成方法候选，不能作为已提升的子代理能力。
21. `subagent_orchestration_pattern_router` 必须把外部方法转成当前任务的编排模式选择：先记录 single_agent_sufficiency_gate，再记录 selected_pattern、rejected_patterns、method_to_work_unit_mapping、role_selection_reason、context_packet_completeness 和 minimum_application_test。若无法说明“为什么不是单代理、为什么不是并行 worker、为什么这个 work unit 能独立验收”，不得 spawn；若只需要主代理低成本完成，写 no_spawn_reason。
22. 子代理返回后必须补 `subagent_result_coverage_gate` 和 `main_agent_integration_review`，逐项核对 contract_items、returned_items、unverified_items、out_of_scope_items、conflicts_found、final_claim_changed 和 reason_for_rejection_or_downgrade。若 blocking_gaps_after_integration 仍存在，必须 route_back、降级主张或补主代理检查。
23. 所有由子代理、skill/plugin 或外部方法支撑的结论，必须绑定 `claim_readiness_ladder`；证据不足时停在 idea_or_candidate、source_backed、locally_verified、small_loop_validated 或 pilot_ready，不得跳到 production_or_public_claim_ready。
24. 若子代理不再需要，`lifecycle_cleanup_plan` 和 `subagent_lifecycle_ledger` 必须说明 close/keep_open/timeout 处理；不能让已完成 agent 长期占用并发槽或让后续恢复者继续等待。子代理输出、ledger、coverage gate 和 integration review 必须引用同一个 `contract_id`；不能留下 orphan subagent output。超时策略必须写 critical_path、deadline_or_check_interval、fallback_action、what_was_not_verified 和 reopen_condition；非关键只读审计可以继续主线，关键路径超时必须 route_back、inline_fallback 或缩小任务。
25. 对 Terraform/GitOps/Kubernetes controller 等声明式调和系统，`integration_lifecycle_gate` 和 `transactional_integration_consistency_guard` 只能作为相邻约束，不能替代 `desired_state_reconciliation_guard`。主代理必须分别检查配置真源、实际观测源、plan/diff、drift、锁/单写者、破坏性动作、import/adoption、rollback/roll-forward、policy gate 和 operator handoff；任何一项缺失都要降低 claim readiness，而不是用“官方机制存在”兜底。
26. 对数据库/数据结构/持久状态迁移，`desired_state_reconciliation_guard` 只能覆盖“配置驱动资源收敛”，不能替代 `stateful_data_migration_guard`。主代理必须分别检查 expand-contract 兼容、旧新代码并行读写、批量回填幂等与节流、DDL 锁与超时、索引/约束在线验证、数据正确性校验、回滚或前滚边界、feature flag/发布顺序、暂停恢复与 owner runbook；任何一项缺失都要降低 claim readiness，不能把“migration 文件存在”或“测试库通过”写成线上零停机安全。
27. 对安全漏洞、凭证泄露、疑似入侵、协调披露或安全修复主张，`external_state_write_guard`、`integration_lifecycle_gate`、`deployment_readiness_gate` 和 `security_remediation_trace` 只能覆盖相邻权限、部署或历史经验，不能替代 `security_incident_response_guard`。主代理必须分别检查触发来源、主张类型、证据等级、受影响资产、授权与联系人、分级依据、利用/入侵状态、遏制缓解、凭证吊销轮换、影响范围、修复验证、披露/通知、监控复发和复盘 owner；任何一项缺失都要降低 claim readiness，不能把 PoC、扫描告警、issue/PR、advisory 草稿或 CTF/writeup 直接写成真实事件已确认、数据已外泄、用户已通知或修复已部署验证。
28. 对数据集、报表、模型、图表、表格、指标或分析输出，`numeric_calculation_trace`、`rendered_artifact_freshness`、`source_authority_precedence_trace`、`stateful_data_migration_guard` 和 `deployment_readiness_gate` 只能覆盖相邻数值、渲染、来源冲突、迁移或部署风险，不能替代 `data_artifact_lineage_freshness_guard`。主代理必须分别检查产物身份、版本/路径、来源快照、输入 hash、生成/刷新时间、转换逻辑、run/job、代码/参数/环境、lineage、freshness policy、质量检查、checksum、复现配方、下游引用、用途限制和 stale 降级；任何一项缺失都要降低 claim readiness，不能把 README/catalog、lineage 图、BI last refreshed、报表截图、文件修改时间、单次 DAG 成功、模型 registry 版本或 DOI 当成当前、可复现、可决策的充分证据。guard 的通过条件按字段证据强度计算；`unknown`、空字段、从摘要推断或只来自二手说明的字段必须写 gap_action，不能因为 guard 模板已填满而提升结论层级。

调用前先跑轻量 `subagent_capability_probe`：如果只看到环境列出子代理名称，记录 `environment_listed`；如果通过 tool_search 或当前工具表发现 `spawn_agent` / `wait_agent`，记录 `tool_discovered`；如果实际调用，记录 `spawn_attempted`、agent_id、wait_status 和 integration_decision。没有这些证据时，不得把 `capability` 写成 available。

调用后必须补 `subagent_lifecycle_cleanup`：子代理已返回、超时、阻塞、被拒收或不再需要时，关闭或记录保留理由；机器看版必须留下 close_attempted、close_status、previous_status_summary、repeated_close_result 和 cleanup_decision。`spawn_attempted: true` 但没有 lifecycle_cleanup，视为恢复链未闭合。

```yaml
subagent_orchestration_ladder:
  not_needed:
    use_when:
      - 单文件小改
      - 问题尚未拆清
      - 需要主代理连续理解用户偏好
      - 子代理会编辑同一文件造成冲突
    required_record: no_spawn_reason
  read_only_audit:
    use_when:
      - 行业最佳实践核验
      - 来源与时效审查
      - 历史债务或恢复链扫描
      - 经验库归类
      - 根因耦合但证据源可独立核验的 parallel_evidence_lane_trace
    allowed_actions: read_search_summarize
    forbidden_actions: edit_files_or_make_final_decision
  parallel_exploration:
    use_when:
      - 多个领域、多个来源、多个失败模式互相独立
      - 主代理可以同时推进非重叠任务
    required_record: roles_boundaries_expected_outputs
  sequential_worker:
    use_when:
      - Plan 已清楚
      - 写入边界互不冲突
      - 有明确验收命令或检查
    required_record: ownership_write_scope_review_gate
  reviewer:
    use_when:
      - 最终报告、协议变更、代码改动或交付物需要独立 QA
      - 主代理需要检查遗漏、幻觉、过度主张或恢复链漂移
    required_record: accepted_rejected_or_conflict_reason
  inline_fallback:
    use_when:
      - 当前环境没有可调用子代理
      - 子代理不可用但主代理可完成同等只读检查
      - 仅有 environment_listed 但没有 tool_discovered 或 spawn_attempted 证据
    required_record: fallback_reason_and_manual_action_required_none
  user_proxy_required:
    use_when:
      - 需要登录、授权、付款、上传敏感材料、线下确认或外部系统手动操作
    required_record: operator_action_location_reason_completion_evidence
  audit_timeout_non_blocking:
    use_when:
      - 子代理超时但不在关键路径
    required_record: timed_out_role_what_was_not_verified_how_to_recover
```

### 5.3 子代理任务契约 subagent_task_contract

所有子代理任务必须先有契约，再有调用；没有契约的调用视为工具冲动。

```yaml
subagent_task_contract:
  contract_id:
  plan_item_id:
  claim_lane_id_optional:
  goal_ref:
  plan_item_status_before:
  batch_id:
  role: source_verifier | domain_reviewer | read_only_auditor | evidence_lane_auditor | worker | quality_reviewer | integration_reviewer
  stage:
  task_boundary:
  input_scope:
  dispatch_readiness:
    bounded_work_unit_ready:
    context_packet_ready:
    acceptance_ready:
    learning_preflight_passed:
    topology_trace_passed:
    side_effect_gate_passed:
    shared_state_conflict:
    main_agent_low_cost_inline:
  context_packet:
    task_full_text:
    exact_questions:
    files_or_urls:
    relevant_snippets_with_line_refs:
    excluded_context:
    allowed_extra_reads:
  subagent_instruction_packet:
    instruction_sources_read_by_main_agent:
    hard_constraints:
    allowed_actions:
    forbidden_actions:
    allow_subagent_tool_discovery:
    excluded_context:
    learning_preflight:
      trigger_source: user_request | obvious_skill_match | unfamiliar_domain | new_plugin_or_connector | online_method_needed | subagent_quality_gap | not_needed
      skill_plugin_discovery_gate_ref:
      instruction_read_status:
      key_constraints_extracted:
      best_practice_learning_contract_ref:
      subagent_method_learning_trace_ref:
      agent_topology_selection_trace_ref:
      minimum_application_test_status:
      block_spawn_if_failed: true
  allowed_actions: read_only | edit_listed_files | test | browser | external_search
  output_contract_items:
    - item_id:
      required_evidence:
      cannot_claim:
  acceptance_evidence:
  return_schema:
  subagent_tool_discovery_permission_gate:
    allow_subagent_tool_discovery: false
    allowed_capability_types:
    forbidden_capability_types:
    max_discovery_scope:
    must_return_before_calling:
    main_agent_approval_required:
  forbidden_actions:
    - 不得扩大范围
    - 不得替主代理做最终取舍
    - 不得修改未授权文件
    - 不得把未经核验材料写成事实
  timeout_policy:
    mode: wait_on_critical_path | audit_timeout_non_blocking
    critical_path:
    deadline_or_check_interval:
    fallback_action:
    what_was_not_verified:
    reopen_condition:
  integration_decision: pending | accepted | partially_accepted | rejected | conflicted
  integration_gate:
    contract_items:
    main_agent_local_checks_required:
    claim_readiness_effect:
  integration_reason:
  plan_item_status_after:
```

只读审计子代理的最小契约：

```yaml
read_only_audit_subagent_contract:
  role: read_only_auditor
  write_scope: none
  allowed_actions:
    - read_named_files_or_urls
    - search_within_declared_scope
    - report_evidence_gaps
  forbidden_actions:
    - edit_files
    - install_or_authenticate_plugins
    - write_external_state
    - update_plan_or_goal
    - decide_final_claim
    - expand_scope_without_returning_for_approval
  required_output:
    anchors_read:
    evidence_gaps:
    claims_not_supported:
    recommended_fixes:
    main_agent_followup_checks:
  integration_requirement:
    main_agent_must_review: true
    result_coverage_gate_required: true
    lifecycle_cleanup_required: true
```

集成规则：

1. 主代理必须阅读并整合子代理输出，写明接受、拒绝或冲突原因。
2. 子代理结论不能自动覆盖 current_basis；只有被主代理纳入证据矩阵或决策记录后才成为依据。
3. 子代理输出如果互相冲突，优先回到证据等级、来源权威、时效和项目语境，而不是少数服从多数。
4. 子代理不能创建或完成 Codex Goal，不能决定用户价值偏好，不能执行高风险人工操作。
5. 需要登录、授权、付款、敏感材料上传、现实判断或外部系统写入的任务，不能包装成普通子代理任务；必须先写 `user_proxy_required` 或 `manual_action_required`，并说明用户完成后应返还的证据。
6. `schema_hygiene_gate`：面向复制复用的 YAML / 表格 / 编号清单必须避免 tab 缩进、重复编号和同名字段漂移；若只是示意结构，必须标注 schematic_only。发现格式漂移时先修模板，再让后续代理或用户复用。

### 5.4 阶段卡通用格式

以下 0-10 阶段保留原编号，但每阶段都按阶段卡运行。阶段卡中的 `dynamic_shortcuts` 允许压缩或跳过，`route_back_triggers` 决定回退，`subagent_fit` 决定是否并行。

#### 阶段 0：总控启动

```yaml
stage_card:
  purpose: 建立工作姿态、触发模式、阶段深度和状态入口。
  entry_triggers:
    - 用户提出新项目、继续任务、高要求/高返工任务、复盘优化或执行计划
    - 机器看版缺失、过期或与当前请求冲突
  required_outputs:
    - 项目触发信息
    - 初始 current_basis 候选
    - mode 和 stage_depth_budget
    - handoff 与机器看版位置
    - Codex tool_state: goal / plan / subagents
  dynamic_shortcuts:
    - 小任务可直接进入阶段 1 或阶段 6，但必须保留 current_basis 和 next_route
    - 连续任务先读取最新机器看版，再决定是否恢复或改道
  route_back_triggers:
    - 无法确认当前请求是否延续旧任务
    - 发现最新用户输入推翻旧 next_route
  subagent_fit: 通常不调用；除非需要只读审计最新机器看版或历史债务
  close_condition: 已知道本轮为何启动、用什么深度、从哪个状态继续、下一步去哪一阶段
```

#### 阶段 1：材料 Intake 与情景识别

```yaml
stage_card:
  purpose: 登记材料、区分事实/草稿/假设，形成 current_basis。
  entry_triggers:
    - 新材料出现
    - 用户补充隐性诉求
    - 执行中发现材料与叙述不一致
  required_outputs:
    - material_register
    - current_basis / not_current_basis
    - 主类、次类和 high_risk_regulatory 标签
    - 最大不确定性
    - 现在最不该急着做什么
    - 必须澄清的问题或 assumption
  dynamic_shortcuts:
    - 材料少且低风险时只列依据、缺口和下一阶段
    - 材料多或相互冲突时先做证据分层，再进入发散
  route_back_triggers:
    - 来源权威性不清
    - 文件路径、版本、时间或用户最新意图不一致
    - 把样例、旧稿、生成物误当 current_basis
  subagent_fit: read_only_audit 可核对文件路径、版本、来源时效和历史状态
  close_condition: 后续阶段知道哪些材料可用、哪些不可用、哪些只是待验证假设
```

#### 阶段 1.5：行业最佳实践调查

```yaml
stage_card:
  purpose: 在发散前校准该类项目的成熟做法、优秀案例、失败模式和验收样式。
  entry_triggers:
    - 高风险、高返工或用户明确重视质量
    - 陌生领域
    - 用户要求高质量、专业、可落地或有权威来源
    - 涉及真实项目、比赛项目、项目复盘或跨项目压力测试
  required_outputs:
    - best_practice_sources
    - best_practice_learning_contract
    - best_practice_patterns
    - anti_patterns
    - project_specific_implications
    - forbidden_or_low_relevance_patterns
    - live_project_pool_scan（必要时）
  dynamic_shortcuts:
    - 熟悉且低风险领域可只做 3 条关键启发
    - 高风险或时效敏感领域必须查原始来源和 current_as_of
    - 真实项目压力测试必须包含 hostile_case_reason 和 protocol_failure_risk_to_probe
  route_back_triggers:
    - 没有外部来源却声称行业共识
    - 只选友好案例
    - 只从当前目录或上一轮主题选项目池
    - 只列框架/平台/插件名称，没有说明 stage_gap、minimum_application_test 或 non_transfer_boundary
  subagent_fit: read_only_audit 或 parallel_exploration 适合核验来源、优秀案例、失败模式和经验库条目
  close_condition: 至少形成 3 条会改变当前项目发散方向、验收标准或风险边界的具体启发，并能写入 best_practice_learning_contract
```

#### 阶段 2：高质量发散

```yaml
stage_card:
  purpose: 在 current_basis、最佳实践约束和 project_nature 下生成多个可比较方向；模型发现型任务先保护问题定义和候选框架，不急于证据填表。
  entry_triggers:
    - 问题空间未收束
    - 用户还在表达愿景、偏好或新增想法
    - 现有方案缺抓手、故事性或落地性
    - 研究问题、模型、公式、解释框架或评价口径尚未确定
  required_outputs:
    - project_nature
    - convergence_status
    - candidate_directions
    - 每个方向的核心问题、价值、资源、风险、验证方式和证据等级
    - model_discovery 时的 candidate_frameworks、thought_search_pool、ibis_argument_map、divergence_budget、discriminating_probe 和 convergence_conditions
    - 不采用方向及其理由
  dynamic_shortcuts:
    - 小任务可只给 2-3 个方向
    - 高风险或高返工项目至少覆盖保守、创新、敌意样例和低成本落地路径
    - 用户临时加想法时先纳入候选或 backlog，再判断是否改主链
    - evidence_fill 可写 divergence_noop_reason，避免为已稳定模型制造形式化发散
    - model_discovery 默认保留 3-5 个候选框架；少于 3 个必须说明问题空间已经被 current_basis 收窄
  route_back_triggers:
    - 候选方向只是同义改写
    - 发散脱离 current_basis
    - 没有验证方式或资源约束
    - 模型未定却只剩单一路线
    - 先做 evidence_matrix 而没有 issue / position / pro / con
    - 没有可区分候选框架的最小探针
  subagent_fit: parallel_exploration 可让不同代理分别找案例、失败模式、工具路线，但主代理负责收束
  close_condition: 候选足够多样，且每个候选都能说明依据、风险、最小验证和收敛条件
```

#### 阶段 3：Skill / 工具 / 外部方法搜索

```yaml
stage_card:
  purpose: 针对阶段缺口寻找外部能力，而不是堆工具。
  entry_triggers:
    - 需要技能、插件、论文、网页、代码、数据、渲染、文档或浏览器验证
    - 项目依赖最新信息、官方规则、行业方法或特定工具
  required_outputs:
    - 当前缺口
    - capability_discovery_cadence_gate.initial_scan
    - event_triggered_capability_refresh 或 lightweight_keep_reason
    - 候选 skill / 工具 / 方法
    - 适用阶段、风险、是否安装、是否只借鉴
    - 推荐调用顺序
    - skill_plugin_learning_loop：读完状态、小题试用、采纳决定、写回和验证器引用
    - skill_plugin_project_fit_trace：项目语境、前后差异、验收证据和不能迁移边界
  dynamic_shortcuts:
    - 本地文件可解决时不强制联网
    - 有官方或一手来源时优先使用一手来源
    - 工具不可用时写 inline_fallback 或 manual_action_required
    - model_discovery 且尚未形成具体证据路径时，先记录 capability_posture: defer_until_probe_or_evidence_path，不重跑完整工具盘点
    - 无事件触发时只写 lightweight keep；3 轮兜底只是上限，不是机械全量复盘
  route_back_triggers:
    - 工具选择替代了项目主链
    - 找到的材料不能支撑当前主张
    - 缺少权限、依赖或环境
    - 把工具可用性误当成研究框架已经收敛
  subagent_fit: read_only_audit 适合并行查工具/来源；worker 只能在 Plan 边界明确后执行
  close_condition: 外部能力服务明确阶段缺口，并知道不用哪些工具
```

#### 阶段 4：主链收束与阶段路由

```yaml
stage_card:
  purpose: 把发散方向压成可执行主链，并决定下一步阶段或回退点。
  entry_triggers:
    - 候选方向已足够
    - 用户需要报告主线、项目抓手或执行路线
    - 发散开始分叉且需要收束
  required_outputs:
    - 一句话主链
    - 通俗版解释
    - 专业版解释
    - 保留范围
    - backlog
    - 边界
    - next_route
    - route_reason
  dynamic_shortcuts:
    - 如果主链已经由用户明确给出，可压缩为确认和风险校正
    - 如果主链依赖用户偏好，设置 ask_user，而不是替用户定审美或价值排序
  route_back_triggers:
    - 主链缺对象、约束、核心矛盾、解决机制或验证方式
    - backlog 没有边界，导致继续扩散
    - next_route 只是“继续优化”而不可执行
  subagent_fit: reviewer 可审主链是否过度主张、是否遗漏证据或利益相关者
  close_condition: 主链稳定，backlog 有理由，next_route 和 route_reason 明确
```

#### 阶段 5：Goal

```yaml
stage_card:
  purpose: 把主链升级为长期使命、第一性原理和不可变约束。
  entry_triggers:
    - 用户明确要求长期目标、持续迭代或高风险/高返工承接
    - 项目会跨多轮、多人、多个交付物或长期维护
  required_outputs:
    - 系统使命
    - 第一性原理
    - 核心主链
    - 不变量
    - 边界
    - 证据等级
    - 评价维度
    - 阶段门
    - 终止条件
    - 自我纠偏规则
    - Codex goal 对齐状态
  dynamic_shortcuts:
    - 单轮交付不创建长期 Goal，只在文档中写本轮目标
    - 已有长期方向摘要时先对齐，但 Codex 工具 Goal 默认仍收窄到本轮可完成目标
  route_back_triggers:
    - Goal 变成任务清单
    - Goal 与用户最新意图或 current_basis 冲突
    - 终止条件不可审计
  subagent_fit: 不允许子代理拥有或更新主目标；reviewer 只能审 Goal 是否一致和可验收
  close_condition: 长期方向能约束项目，且工具 Goal 生命周期、文档状态和 next_route 一致
```

工具规则：

1. 连续项目的长期方向优先写入 state、master prompt、closure-routing 和 next_route；Codex goal 工具默认只创建当前拍窄目标。
2. 不得因为阶段产物完成、预算接近或自己想停下就把长期路线标记 complete；只有本轮窄目标完成时才 update_goal complete，本轮完成不等于 continuous route 结束。
3. 子代理不得创建、更新、完成或阻塞主 Goal。
4. 若历史工具 Goal 已 blocked 或停在旧版本，但 current_basis 证明项目仍可继续，按 `per_round_goal_lifecycle_gate` 迁移到 protocol_round_goal 或新一轮窄目标。

#### 阶段 6：Plan

```yaml
stage_card:
  purpose: 把 Goal 或本轮主链转成当前阶段可执行任务。
  entry_triggers:
    - 需要多步骤执行
    - 用户要求 implement/开展/继续做
    - 已经有明确主链但缺任务分解
  required_outputs:
    - task_list
    - 每个任务的 why、input、output、acceptance、dependency、risk、stop_condition
    - 人看产物和机器看产物
    - Codex update_plan 状态
    - subagent_orchestration_ladder 判断
  dynamic_shortcuts:
    - 小任务可以只有 2-3 个任务项，但仍要有验收标准
    - 多步骤任务必须同步 update_plan，最多一个 in_progress
    - 能并行的只读审计或独立实现要评估子代理；不开则写 no_spawn_reason
  route_back_triggers:
    - 任务没有验收标准
    - 任务混入未来阶段或无边界扩写
    - manual_action_required 被藏在自然语言里
  subagent_fit: sequential_worker 适合清晰、独立、可验收的执行任务；reviewer 适合验收前检查
  close_condition: Plan 只管当前阶段，每个任务可验收，工具状态同步，知道现在不做什么
```

`plan_patch_alignment_gate`：Plan 模式或执行前计划中，用户补充细节时，默认视为对当前计划的补丁，而不是自动重写整个任务。模型必须先判断该修改属于交付风格、受众、颗粒度、证据要求、范围变化还是任务目标变化；只有明确属于任务目标变化时，才改写主目标。若只是风格、受众、颗粒度或证据要求，应明确说“主目标不变，只调整这一处”，并把修改写回原 plan 的对应项，避免局部细节劫持主线。

#### 阶段 7：评分体系与终止条件

```yaml
stage_card:
  purpose: 用评分和阈值决定继续、压缩、加深、回退或执行。
  entry_triggers:
    - 高风险或高返工项目进入执行前
    - 用户要求自评、复盘或判断流程质量
    - 证据、计划和主链之间存在不确定性
  required_outputs:
    - scoring_rubric
    - 每项权重、0 分定义、1 分定义、当前证据等级、缺失证据、阶段门
    - pass / partial / route_back / blocked 判断
  dynamic_shortcuts:
    - 小任务可用三档判断：可执行 / 需补证据 / 阻塞
    - 深度项目保留完整权重表和低分项下一轮 route
  route_back_triggers:
    - 分数没有证据来源
    - 低分项不形成修复任务
    - 用总分掩盖底线风险
  subagent_fit: reviewer 可独立审评分是否自洽、是否遗漏硬闸门
  close_condition: 分数能改变行动，而不是装饰性自评
```

默认评价维度：

| 维度 | 权重 |
| --- | --- |
| 材料治理能力 | 0.14 |
| 状态恢复能力 | 0.14 |
| 阶段路由能力 | 0.14 |
| AI 主动性与边界平衡 | 0.10 |
| skill/工具搜索质量 | 0.08 |
| 最小闭环能力 | 0.10 |
| 用户入口简洁度 | 0.12 |
| 最终正文克制度 | 0.10 |
| 可迁移性 | 0.08 |
| 可验证性 | 0.10 |

阈值：低于 0.55 必须 `route_back`；0.55-0.70 只允许局部最小闭环；0.70-0.85 可进入执行前闸门；高于 0.85 可执行但仍保留回退机制。

项目性质评分剖面：

```yaml
project_nature_scoring_profiles:
  evidence_fill:
    use_when: 模型、指标或表格已定，主要风险是证据硬度和交付准确性
    emphasize:
      evidence_strength: 0.25
      current_basis_integrity: 0.20
      source_authority_and_access: 0.15
      validation_and_reproducibility: 0.15
      delivery_contract: 0.15
      capability_fit: 0.10
  model_discovery:
    use_when: 模型、研究框架或解释路径尚未稳定
    emphasize:
      problem_definition_quality: 0.20
      candidate_framework_diversity: 0.20
      discriminating_probe_quality: 0.15
      adversarial_or_counterexample_coverage: 0.15
      convergence_discipline: 0.15
      evidence_boundary_honesty: 0.10
      delivery_clarity: 0.05
    route_back_if:
      - 候选框架不足且无窄化理由
      - 只有支持证据没有反对理由或敌意样例
      - 没有能区分候选路线的探针
      - 总分较高但问题定义仍不稳定
  mixed:
    rule: convergence_status 进入 evidence_fill_ready 前使用 model_discovery 权重；之后切换到 evidence_fill 权重，并记录 switch_reason
  execution_delivery:
    emphasize:
      acceptance_criteria_clarity: 0.25
      implementation_or_delivery_plan: 0.20
      verification: 0.20
      side_effect_boundary: 0.15
      recovery_and_handoff: 0.10
      user_visible_delivery_quality: 0.10
```

#### 阶段 8：最小闭环

```yaml
stage_card:
  purpose: 用最低成本验证主链中最关键的不确定性。
  entry_triggers:
    - 主链和 Plan 已形成但尚未证明可行
    - 项目涉及真实效果、工程运行、调研结论、教育成效、公共议题或正式交付
  required_outputs:
    - micro_task_execution_check
    - baseline_first_loop
    - validation_semantics
    - execution_or_artifact_contract
    - what_it_can_prove
    - what_it_cannot_prove
    - next_route_after_loop
  dynamic_shortcuts:
    - 文档类任务做低成本样张或结构扫描
    - 代码/系统任务先跑 dummy/baseline 或最小测试
    - 社会实践/教育任务先做问卷/访谈/课堂材料小样和受众视角抽检
    - 高风险项目必须补 risk_ethics_permission 和 downstream_use
  route_back_triggers:
    - 闭环不能验证主链
    - 只写期望行为，没有 actual_execution_evidence
    - 代理验证与真实部署差距未说明
  subagent_fit: worker 可执行独立小题；reviewer 可审闭环是否真的证明主张
  close_condition: 已完成一个 5-30 分钟可复核小题，记录输入、执行证据、观察结果、pass/fail 和 remaining_gap
```

最小闭环必须优先检查：

1. `claim_ladder`：世界问题、代理目标、当前输出、可主张结论和禁止夸大结论。
2. `evidence_contract`：来源、权限、版本、时效、证据等级和可支撑范围。
3. `execution_validation`：输入输出、目标环境、验收标准、失败样例和复现方式。
4. `transfer_boundary`：从竞赛、样机、demo、调研、活动、证书、新闻到真实效果之间缺哪层证据。
5. `operation_handoff`：资源、维护、培训、责任、申诉、整改和长期承接。

#### 阶段 9：执行前闸门

```yaml
stage_card:
  purpose: 在执行或交付前检查底线条件，防止带着幻觉、旧状态或未授权风险进入正式产出。
  entry_triggers:
    - 准备写最终报告、改文件、生成 Word/PPT/PDF、提交代码、发布结论或进入现场行动
    - 阶段 7 评分达到执行阈值
    - 阶段 8 最小闭环通过或已明确降级
  required_outputs:
    - pre_execution_gate_result
    - route_event: execute | route_back | ask_user | blocked
    - failed_gate_to_fix
    - next_route
  dynamic_shortcuts:
    - 小任务只跑 must_pass
    - 高风险或高返工项目跑 must_pass + risk_based_checks + artifact_freshness_checks + manual_decision_gates
    - 执行前闸门失败时不继续补内容，先 route_back
  route_back_triggers:
    - 任一 must_pass 失败
    - 高风险授权、隐私、安全或未成年人保护不清
    - 交付物源稿和渲染物不一致
    - 最新机器看版或发布包指向旧状态
  subagent_fit: reviewer 或 read_only_audit 适合做最终 QA、来源复核、恢复链扫描和反幻觉检查
  close_condition: 可以明确说 execute、route_back、ask_user 或 blocked，而不是含糊继续优化
```

执行前闸门采用四组动态检查，不再维护几百条固定清单：

```yaml
pre_execution_gate:
  must_pass:
    - current_basis 已更新，not_current_basis 不会被误用
    - primary_claim / main_chain / next_route 一致
    - evidence_matrix 或最低证据清单能支撑核心判断
    - Plan 有验收标准，manual_action_required 显性化
    - micro_task_execution_check 有 actual_execution_evidence 或明确降级
    - subagent 输出已集成，或记录 no_spawn_reason / inline_fallback
    - routing_decision_log 已记录关键动态选择和未选路线
  risk_based_checks:
    - high_risk_regulatory 标签已触发 risk_ethics_permission
    - stakeholder_context 明确受益者、使用者、风险承担者和复核者
    - downstream_use 和 harm scenario 至少各有一个
    - transfer_boundary 写清不能外推到真实效果的层级
    - rule_promotion_mechanism 和 anti_protocol_bloat_gate 已处理新增规则
  artifact_freshness_checks:
    - 代码、报告、Word、PPT、PDF、图表、问卷、课程材料或发布包与源稿一致
    - rendered_artifact_freshness 标明 rendered_pass / structural_scan_pass / render_blocked / not_checked
    - release_package_freshness 指向最新机器看版和当前 next_route
    - append_only_eof_guard 确认最新机器看版在 EOF 且无伪标题误判
  manual_decision_gates:
    - 价值偏好、路线取舍、授权、付款、登录、敏感材料上传或外部手动操作只由用户决定
    - 若必须等待用户，写 ask_user 或 user_proxy_required，不伪装成 blocked
```

#### 阶段 10：执行

```yaml
stage_card:
  purpose: 进入执行，但每轮仍受 Goal、Plan、评分、闸门和阶段路由约束。
  entry_triggers:
    - 阶段 9 输出 route_event: execute
    - 用户明确要求执行已通过闸门的计划
  required_outputs:
    - 本轮最高优先级任务
    - 服务的 Goal / main_chain 部分
    - 实际改动或产物
    - 验收证据
    - post_change_key_node_scan 或 artifact_key_node_scan
    - 更新后的人看版和机器看版
  dynamic_shortcuts:
    - 每轮只推进一个最高杠杆任务
    - 新想法先进 backlog，除非暴露硬性方向错误
    - 发现 current_basis 变化立即回阶段 1 或 4
  route_back_triggers:
    - 执行中发现目标、材料、权限、验收或交付物与计划不一致
    - 扫描发现实际文件和叙述不一致
    - 子代理或工具输出与本地证据冲突且无法解释
  subagent_fit: worker 只处理边界清楚且写入范围独立的任务；reviewer 做完成前验证
  close_condition: 当前执行任务完成验收，状态可继承，下一步路由明确
```

执行规则：

1. 每次只推进一个最高优先级任务。
2. 执行前说明它服务 Goal 或主链的哪一部分。
3. 发现偏离主链时主动暂停或 route-back。
4. 新想法先进入 backlog，除非暴露硬性方向错误。
5. 每轮结束更新人看版和机器看版。
6. 如果 current_basis 变化，必须更新 state。
7. 阶段关闭、回退、阻塞或用户决策，必须写入 decisions。
8. 不把 synthetic、sample、template 当真实结论。
9. 如果执行中修正、优化或新增代码，完成后必须做 post_change_key_node_scan。
10. 如果执行中修正、优化或新增报告、Word、PPT、问卷、课程材料或其他交付物，完成后必须做 artifact_key_node_scan。
11. 如果扫描发现实际代码库或文件与叙述不一致，必须先修正事实或降级表述。

## 6. 路由规则

| 情况 | 路由 |
| --- | --- |
| 材料权威性不清 | 回到阶段 1 |
| 缺少行业最佳实践调查 | 回到阶段 1.5 |
| 问题层级不清 | 回到阶段 1 或补做问题契约 |
| 候选方向不足 | 回到阶段 2 |
| 外部方法不足 | 回到阶段 3 |
| 主链不稳 | 回到阶段 4 |
| Goal 不稳 | 回到阶段 5 |
| Plan 无验收标准 | 回到阶段 6 |
| 评分不足 | 回到阶段 7 |
| 最小闭环不能验证主链 | 回到阶段 8 |
| 目标形态或 primary_contracts 不清 | 回到阶段 3.6 或阶段 4 |
| 重大路线需要用户品味/偏好但未设置反馈闸门 | user-decision-needed |
| 契约选择正确但缺少最小验证模块 | 回到阶段 8 |
| major_project_mode 已触发但缺少证据矩阵、决策记录或追踪矩阵 | 回到阶段 8.7 |
| 核心判断证据等级不足但被写成确定结论 | 回到阶段 8.7 或阶段 8 |
| agent_self_optimization_mode 已触发但没有失败模式、回归样例或工具纪律检查 | 回到阶段 8.8 |
| route_event = compress | 记录压缩理由和保留的最低输出后继续 |
| route_event = deepen | 补行业最佳实践、证据矩阵、最小闭环或用户反馈点 |
| route_event = fork_parallel / spawn_subagent | 写 subagent_task_contract 后调用或记录 inline_fallback |
| route_event = ask_user | 只问不可替代的偏好、授权、成本或外部操作问题 |
| 执行前闸门不通过 | 按失败原因 route-back |
| 需要用户确认才能继续 | user-decision-needed |
| 无法继续且原因明确 | blocked |

## 7. 人看版输出要求

人看版必须解释：

1. 当前判断。
2. 使用了哪些依据。
3. 做了哪些取舍。
4. 主要风险。
5. 下一步为什么这样走。

不要只罗列表格。

`reader_translation_gate`：人看版默认给没有参与治理过程的第三方也能读懂。先讲问题和用户为什么会感觉摩擦，再讲协议或方案哪里要补；用普通语言解释，不依赖项目内部黑话、机器看版字段、trace 名称或长串工具名。真实项目可以作为例子，但不能让例子抢走主线；最终要沉淀为少量可复用范式，而不是一长串零散补丁。

`deliverable_contract_gate`：最终或阶段性交付前，必须先确认或记录交付对象、用途、粒度、语气和内部信息边界。若交付给老师、专家、第三方、评委、用户本人或后续 AI，表达方式必须不同；若用户使用“批注、老师版、交付说明、人看版、机器看版、最终版”等词，模型不能自行混用，必须明确该产物是批注新增内容、指出原文风险、解释修改理由、还是给后续 AI 恢复状态。不确定时要低摩擦确认，不能把内部治理记录包装成给人的最终说明。

### 用户可见压缩层

协议越复杂，用户可见输出越要短。除非用户要求查看完整治理过程，每轮回复只展示：

1. 本轮实际完成了什么。
2. 修改或产物在什么文件。
3. 关键验证是否通过，若未通过则说明阻塞。
4. 一个最高杠杆风险、反馈点或 next_route。
5. 如果需要人工操作，显性化 manual_action_required。

以下内容默认写入前置治理文件或机器看版，不在普通回复中整段展开：

1. 完整 evidence_matrix、decision_log、traceability_matrix。
2. 完整机器看版 YAML。
3. 长篇外部材料清单和逐条推理过程。
4. 已被废弃的候选方向，除非会影响用户决策。

压缩不等于隐藏关键风险。若存在高返工风险、事实不确定、人工操作、权限/工具限制或用户偏好节点，必须在用户可见层说明。

## 8. 机器看版输出要求

机器看版必须短、稳定、可继承。

推荐格式：

```yaml
current_stage:
stage_status:
dynamic_stage_controller:
  mode:
  stage_depth_budget:
  route_event:
  routing_decision_log:
    - decision:
      selected:
      alternatives_considered:
      rejected_reason:
      trigger_evidence:
      user_friction_effect:
      revisit_if:
  subagent_decision:
capability_discovery_cadence_gate:
  initial_scan:
    status:
    scanned_surfaces:
    candidates_considered:
    selected_now:
    rejected_now:
    backlog:
    skip_reason:
  event_triggered_capability_refresh:
    required_triggers:
    trigger_event:
    last_checked_at_stage:
    result: refresh | lightweight_keep | defer_until_probe_or_evidence_path
    next_check:
  periodic_reconsideration_legacy_alias:
    status: superseded_by_event_triggered_capability_refresh
  lightweight_exception:
current_basis:
not_current_basis:
open_questions:
decisions:
major_project_mode:
evidence_matrix_status:
decision_log_status:
traceability_status:
agent_self_optimization_mode:
agent_eval_status:
agent_failure_modes:
agent_regression_cases:
contract_selector:
user_feedback_gate:
score_snapshot:
next_route:
route_reason:
backlog:
codex_tool_state:
subagent_contract_index:
  - contract_id:
    batch_id:
    plan_item_id:
    role:
    status:
    agent_id:
    critical_path:
    timeout_policy:
    coverage_status:
    integration_decision:
    close_status:
learning_preflight_summary:
  required:
  passed:
  blocked_refs:
agent_topology_selection_trace:
  selected_topology:
  final_answer_owner:
  state_write_boundary:
  context_boundary:
  dependency_graph:
  downgrade_to_inline_if:
result_coverage_summary:
  contract_items_count:
  returned_items_count:
  unverified_items:
  out_of_scope_items:
  conflicts_found:
  claim_readiness_after_integration:
manual_action_required:
```

后续 AI 必须先读取机器看版，再决定是否继续、回退、阻塞或等待用户。

## 8.5 成果与治理分文件规则

复杂项目进入最终交付或阶段性交付时，必须优先拆成两个文件：

1. 最终成果文件：面向真实读者，只写最终方案、报告、正文、执行清单、展示稿或交付物。不写前置治理过程、长篇方法搜索、阶段 handoff、内部推理、废弃方向和版本演化，除非这些内容本身就是成果的一部分。
2. 前置治理文件：面向项目继承和复盘，保留 material intake、current_basis、not_current_basis、open_questions、decisions、发散方向、外部方法搜索、主链收束、Goal、Plan、评分、最小闭环、执行前闸门、风险和机器看版 handoff。

若用户只要求人看版交付，默认不展示机器看版、验证器细节或内部状态演化，只在必要时用一句话说明验证或阻塞。若同一项目需要老师版、第三方版、用户自用版和机器恢复版，必须分清受众：老师/第三方只看能理解、能判断、能行动的内容；机器恢复版才保留字段、状态、文件路径和内部取舍。

分文件命名建议：

```text
【项目名】_最终成果.md
【项目名】_前置治理与推理过程.md
```

如果最终成果需要故事化、案例化或对外展示，而现场材料尚未发生，必须把样例、模拟、模板明确标注为 synthetic / sample / 举例 / 模拟，不得写成事实。最终成果文件可以保留必要的样例，但必须清楚说明其性质；前置治理文件应记录这些样例为何被设计、需要哪些真实证据替换。

## 8.6 低摩擦共创与隐性诉求反馈规则

本规则用于防止复杂项目变成“AI 在黑箱里循环优化，用户只在成品后返工”。尤其适用于社会实践方案、研究选题、汇报叙事、课程设计、品牌表达、论文框架、产品设计等评价标准较隐性的项目。

### 方法来源

本规则不是凭空设想，主要借鉴以下成熟方法：

1. **Requirements Elicitation / Elicitation and Collaboration**：IIBA BABOK 将 elicitation and collaboration 拆成准备、开展、确认结果、沟通信息、管理协作等任务；对应本协议中的“问题契约闸门”和“确认用户隐性标准”。参考：https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/4-elicitation-and-collaboration/
2. **Double Diamond**：Design Council 的 Double Diamond 将复杂问题处理为 Discover、Define、Develop、Deliver 四个阶段，强调先理解问题、再定义挑战、再发散方案、再测试交付；对应本协议中的“发散-收束-执行前闸门”。参考：https://www.designcouncil.org.uk/resources/the-double-diamond/
3. **Human-Centered Design / Design Thinking**：IDEO 将设计思维定义为整合人的需要、技术可能性和组织可行性的以人为中心方法；对应本协议中的“用户反馈是前置治理材料的一部分”。参考：https://designthinking.ideo.com/
4. **Low-fidelity / Paper Prototyping**：Nielsen Norman Group 认为低保真原型可在极低成本下测试早期想法、尽早发现问题；对应本协议中的“方向样张闸门”和“10% 粗稿校准闸门”。参考：https://www.nngroup.com/articles/paper-prototyping/
5. **Co-design**：共创方法强调不是为人设计，而是和有真实经验的人一起设计；对应本协议中的“连续治理不是取消用户参与”。参考：https://aci.health.nsw.gov.au/projects/co-design
6. **本地可借鉴 skill**：当前 Codex 环境中没有专门面向所有复杂项目的“隐性诉求抽取 skill”。相邻的是 `product-design:get-context`，它要求在产品设计前先完成 brief gate，且规定上下文未确认前不得实施；本协议将其抽象为通用复杂项目的 brief / feedback gate。

### 核心判断

复杂项目失败常常不是因为 AI 不会完成任务，而是因为用户的真实标准没有在前置阶段被显化。用户一开始给出的目标通常只包含显性目标，例如“写一份报告”“做一个项目方案”；隐性标准可能要在看到粗糙版本后才会出现，例如：

1. 需要更强抓手，而不是泛泛而谈。
2. 需要故事性，而不是流程罗列。
3. 需要权威话术和可溯源依据，而不是自说自话。
4. 需要真落地、真有用，而不是宏大表达。
5. 需要用户本人参与判断方向，而不是 AI 独自跑完。

这些隐性标准一旦出现，必须进入 current_basis 或 decisions，不能被当作“用户临时改需求”的噪音。

### 反馈闸门

即使用户授权连续治理，只要项目具有高度主观评价或高返工风险，AI 也必须至少设置以下低摩擦反馈闸门之一：

1. **问题契约闸门**：在正式写作前，用 5 到 8 行说清“我理解你要的不是 A，而是 B；评判好坏的标准是 C；最大返工风险是 D”。请用户确认或修正。
2. **方向样张闸门**：在高质量发散后，不直接写长文，而是给出 2 到 3 个候选抓手、标题或故事主线，让用户选择“最像我想要的方向”。
3. **粗稿校准闸门**：先交付一个低成本、可推翻的 10% 粗稿或目录样张，明确说“这是用来暴露偏好的，不是最终稿”。
4. **执行前验收闸门**：进入最终写作、PPT、Word、代码实现或对外交付前，列出最终验收标准和可能牺牲的内容。

如果用户明确说“不要中途问我，直接完成”，AI 可以跳过反馈闸门，但必须记录：

```yaml
feedback_gate_skipped: true
skip_reason: user_explicitly_requested_no_interruption
max_rework_risk:
```

### 低摩擦提问模板

反馈问题必须短，避免把治理成本转嫁给用户。优先问能改变方向的问题，而不是泛泛收集偏好。

```text
我先不继续写长稿。请你只判断方向：
1. 这个抓手是否太泛？
2. 你更想要“项目评奖叙事”“真实落地工具包”还是“社会学研究问题”？
3. 哪一句最接近你想让评委记住的核心表达？
```

```text
这是 10% 粗稿，用来暴露隐性标准，不是最终稿。
如果你觉得不对，请优先指出：
抓手不对 / 深度不够 / 太空泛 / 不够落地 / 不够故事化 / 权威依据不足 / 受众不对。
```

### 用户“临时加想法”的处理

用户在过程中新增想法，不默认视为范围蔓延。先判断它属于哪一类：

1. **隐性标准显化**：例如“要更有故事性”“要权威话术”“要横向比较”。这类应立即进入 current_basis，并回退到相关阶段。
2. **新材料进入**：例如新增文件、政策、案例。回到材料治理。
3. **范围扩张**：例如从报告变成 PPT、Word、工具包。进入 backlog 或新阶段。
4. **方向纠偏**：例如从泛支教改为 AI 之于县中教育。回到主链收束。

只有第 3 类才默认视为 scope expansion；第 1 类和第 4 类通常说明前置治理还不充分。

如果用户的临时想法发生在 Plan 模式或执行计划已形成之后，必须同步触发 `plan_patch_alignment_gate`：先判断它是补风格、补受众、补颗粒度、补证据、改范围还是改目标。除非用户明确改目标，否则主目标不变，只把新细节补进对应任务、交付标准或风险说明。模型不得因为用户补了一个局部细节，就把整轮注意力转向那个细节而忘记原本要交付的东西。

如果临时想法涉及“批注、老师版、给第三方看、人看版、交付说明、不要术语、说人话”等表达，必须同步触发 `deliverable_contract_gate` 和 `reader_translation_gate`，先对齐受众和表达颗粒度，再继续产出。

### 连续治理下的特殊规则

连续治理不是取消用户参与，而是减少等待次数。若项目出现以下信号，AI 必须暂停并请求反馈：

1. 用户评价中出现“空泛”“没有抓手”“不够落地”“不够故事性”“不是我想要的”“还差点意思”。
2. AI 正在选择多个同样合理但风格差异很大的方向。
3. 最终成果依赖用户所在组织的真实审美、评奖标准、汇报场景或隐性人情境。
4. 继续写作会把一个可轻松调整的方向错误放大成大规模返工。

如果不暂停，AI 至少必须输出一个“反馈采样点”，让用户可以用一句话改变方向。

## 8.7 工作力度/风险升级与重大项目兼容记录

本规则用于把高风险、高返工或高公共性的复杂项目升级为可审计、可继承、可复盘的工作力度。历史字段仍可写作 `major_project_mode`，但它不是用户侧“普通项目 vs 重大项目”的模式菜单；用户只需要表达“这事重要、别黑箱、要系统推进”，AI 负责在内部提高证据、验证、追踪和反馈要求。

它借鉴三类成熟做法：需求追踪强调需求、证据和验收之间可追溯；Stage-Gate / 技术评审强调每个阶段必须有进入/退出条件；Architecture Decision Records 强调重大取舍必须记录上下文、选项、决定和后果；系统工程评审强调结论要能回到证据和验证。

### 触发条件

出现任一条件，默认触发工作力度/风险升级，并在机器看版中兼容记录 `major_project_mode`：

1. 用户明确说“重大项目”“重要项目”“不能再黑箱”“要系统复盘”“长期协议”等。
2. 项目会影响真实人群、未成年人、学校、医疗、心理健康、隐私、政策、公共议题或组织协作。
3. 项目需要最终成果和前置治理双文件，或同时修改协议、报告、Word、PPT、代码、问卷、课程材料等多个交付物。
4. 项目涉及权威引用、公共判断、故事主线、研究抓手、课程主轴或评奖汇报。
5. 用户已经在过程中多次补充“不是这个意思”“太空泛”“还可以优化”“缺少抓手”“要更落地”。
6. AI 需要连续推进多个阶段，且用户不一定在每一步实时反馈。

`major_project_mode` 不是要求每一步都停下来问用户，也不是让用户先选择项目类别。它要求每一步的关键判断可追踪、可降级、可被用户低成本改方向。

### 风险升级最小治理包（兼容 major_project_mode）

```yaml
major_project_mode:
  trigger:
  scope:
  friction_budget:
  feedback_cadence:
  evidence_matrix_required: true
  decision_log_required: true
  traceability_matrix_required: true
  post_change_key_node_scan_required: true
```

#### 证据矩阵 evidence_matrix

所有支撑核心结论、规则、方案主张、权威表述、技术状态、案例选择和公共意义的证据，必须进入证据矩阵。

```yaml
evidence_matrix:
  - claim_id:
    claim:
    claim_type: material_fact | external_method | benchmark_result | user_preference | inference | assumption
    source_id:
    source_link_or_path:
    source_kind: primary | official | peer_reviewed | first_party | secondary | user_input | generated
    authority_level: high | medium | low | uncertain
    current_as_of:
    supports_what:
    counterevidence_or_limits:
    evidence_level: E0 | E1 | E2 | E3 | E4
    used_in_deliverable:
    verification_status: unchecked | checked | contradicted | outdated | needs_user_confirmation
```

证据等级：

1. **E0 unsupported**：只有直觉、草稿、生成内容或未查证说法。
2. **E1 single-source**：有一个可追溯来源，但尚未交叉验证。
3. **E2 corroborated**：有多个独立来源，或一个官方/一手来源加可解释推断。
4. **E3 operationally verified**：已在代码、文件、指标、渲染、样例、现场小闭环或用户材料中验证。
5. **E4 stakeholder-validated**：已被用户、专家、现场对象、评审标准或真实结果确认。

判断规则：

1. 最终报告中的核心判断原则上不能低于 E1；重大公共性判断原则上不能低于 E2。
2. 如果只能达到 E0/E1，必须在最终成果中降级为“假设、待验证、举例、初步判断”。
3. 来源不能只贴链接。必须说明它支持哪一句判断，也要记录它不能证明什么。
4. 网页、软件状态、政策法规、模型能力、组织人物、竞赛状态等会变化的信息必须填 current_as_of。

#### 决策记录 decision_log

重大路线选择、案例选择、规则写回、文件命名、是否暂停问用户、是否跳过某些材料、是否降级表述，必须有轻量决策记录。

```yaml
decision_log:
  - decision_id:
    date:
    status: proposed | accepted | superseded | rejected
    context:
    options_considered:
    decision:
    why_now:
    tradeoffs:
    evidence_ids:
    user_feedback:
    consequences:
    review_trigger:
    superseded_by:
```

判断规则：

1. 决策记录不是复述结论，而是保留“为什么不选其他路线”。
2. 如果用户后续纠偏，旧 decision 不删除，改为 superseded，并写明新依据。
3. 如果 AI 连续推进没有暂停问用户，必须在 decision_log 记录 skip_reason 和 max_rework_risk。

#### 追踪矩阵 traceability_matrix

高风险或高返工项目必须能从用户诉求追踪到最终交付物，不允许“中间看起来很努力，最终不知道服务了哪个要求”。

```yaml
traceability_matrix:
  - user_need_or_risk:
    requirement_or_gate:
    selected_contract:
    evidence_ids:
    decision_ids:
    deliverable_location:
    validation_or_scan:
    status: open | satisfied | partial | dropped | user_confirm_needed
```

判断规则：

1. 用户明确提出的痛点，例如“太空泛”“没抓手”“要权威”“要可落地”“要横向比较”，必须进入 traceability_matrix。
2. 每个最终成果的重要章节，都应该至少追踪到一个用户诉求或项目目标。
3. 如果某个用户诉求被放弃，必须写 dropped_reason，不能默默消失。

#### 成果到执行追踪矩阵 deliverable_execution_trace

如果项目最终成果包含报告主张、公共议题、课程方案、组织行动、政策建议、实践工具包或评奖叙事，还必须建立成果到执行追踪矩阵。

```yaml
deliverable_execution_trace:
  - final_claim:
    required_field_evidence:
    execution_tool_or_template:
    minimum_pass_standard:
    conclusion_boundary:
    downgrade_rule:
    owner_or_collection_time:
```

判断规则：

1. 每条重要主张必须对应一个现场工具、数据字段、访谈问题、课堂产物、测试记录或用户行为证据。
2. 如果只能追踪到“团队印象”或“表达需要”，主张必须降级为假设、故事素材或待验证问题。
3. 对外报告中的“可持续、可承接、可复制、公共性、认知改变、能力提升”等词，必须有执行证据和最低通过标准。
4. 对于支教和社会实践项目，至少追踪学生材料、教师/伙伴材料、团队复盘材料和横向比较材料中的两类；否则不能写成公共结论。

#### 现实项目池扫描 live_project_pool_scan

涉及真实项目、比赛项目、题库扩展、跨项目压力测试、行业最佳实践调查或高风险/高返工项目发散时，必须先建立现实时间项目池，不能默认从当前工作区、目录名称、当前本地 AI 科研材料、上一轮主题或 AI 熟悉领域取样，也不能把“避免只看 AI 科研”误解成“排除外部 AI/理工真实项目”。

```yaml
live_project_pool_scan:
  current_as_of:
  scan_purpose:
  historical_debt_priority_queue:
    change_inventory_checked:
    release_package_checked:
    latest_machine_board_checked:
    current_scope_recovery_scan:
      current_scope_checked:
      historical_record_scope_checked:
      archive_hits:
      ambiguous_archive_hits:
      current_stale_hits:
      decision_rule: current_scope_hit_required_for_stale
    stale_or_pending_items:
    manual_action_required_items:
    decision_before_new_expansion: proceed | repair_first | downgrade_and_proceed
  channel_coverage:
    - channel_type: national_or_official_competition | discipline_competition | data_ai_platform | social_practice | volunteer_public_service | innovation_entrepreneurship | open_source | industry_or_government_task | school_or_local_project
      source_name:
      source_url_or_path:
      authority_level: A_original_official | B_platform | C_school_or_org | D_aggregator_or_media
      current_signal:
      candidate_project_examples:
      verification_needed:
  selection_rule:
  selected_pressure_test_case:
  pressure_test_mix:
  hostile_case_reason:
  protocol_failure_risk_to_probe:
  real_project_pressure_test_gate:
    sample_count:
    hostile_case_included:
    engineering_or_software_or_delivery_case:
    micro_task_execution_check:
    pressure_test_status: pass | insufficient | blocked
  why_not_local_only:
  uncovered_bias:
  refresh_rule:
```

判断规则：

1. “真实项目”必须优先理解为现实时间仍能被外部渠道核验的项目、赛题、组织需求或公开任务，而不是当前目录里恰好存在的文件；外部 AI 科研、渲染比赛、建模大赛、实际工程问题、企业工程赛题和偏理工科竞赛，只要可被真实渠道核验，同样属于真实项目池。
2. 至少覆盖 5 类渠道；如果只覆盖单一领域，必须写明 `uncovered_bias`，不能把局部样本说成全域样本。
3. 对活跃比赛、报名通知、赛题、项目招募和政策类信息，必须记录 `current_as_of`；超过 30 天未复查的当前事实必须重新核验。
4. 聚合网站、新闻和公众号只能作线索，不能直接替代原始官方通知、赛事官网、学校官网或主办方页面。
5. 如果最终仍选择本地项目作为压力测试，必须写明它比外部现实项目更适合本轮暴露协议缺口的理由；否则触发 `local_project_pool_bias`。
6. 新增真实项目、比赛项目或领域 trace 前，必须先关闭或显性降级 historical_debt_priority_queue 中的历史缺漏；如果最新机器看版仍有 pending、发布包仍指向旧 route、交付物 QA 仍被误写为通过，不能进入新压力测试。
7. 跨项目压力测试不得只选友好样例；至少包含 1 个工程、软件、企业交付、开源维护或真实运行流程类项目，并说明 hostile_case_reason 和 protocol_failure_risk_to_probe。缺少这类敌意样例时，pressure_test_status 只能写 insufficient，不能声称协议已通过真实项目压力测试。

#### 真实项目压力测试闸门 real_project_pressure_test_gate

真实项目压力测试不是“找几个案例佐证协议”，而是用现实项目反过来挑战协议。

```yaml
real_project_pressure_test_gate:
  current_as_of:
  source_set:
    - source_id:
      source_url_or_path:
      source_kind: official | platform | school_or_org | repository | local_artifact
      authority_level:
      link_status:
  selected_cases:
    - case_name:
      case_type: engineering_practice | software_or_open_source | enterprise_delivery | social_practice | policy_or_org | other
      final_claim_to_test:
      trace_modules_enabled:
      micro_task_to_execute:
      actual_execution_evidence:
      observed_result:
      failure_mode_exposed:
      downgraded_expression:
  sample_mix_check:
    at_least_three_types:
    hostile_engineering_or_software_case_included:
    local_project_pool_bias_avoided:
  pressure_test_status: pass | insufficient | blocked
```

1. 至少选择 3 个不同类型真实项目；至少 1 个必须是工程、软件、企业交付、开源维护或真实运行流程类敌意样例。
2. 每个样例都必须实际完成一个小题检验；不能只列项目名、链接或优秀案例。
3. 小题产物可以很小，但必须可检查，例如验收链表、issue 证据链、trace 摘要、文件扫描结果、降级表述对照。
4. 如果某个项目只能支持“竞赛作品、演示原型、报名通知、平台活动、候选线索”，必须写 downgraded_expression，不能把它外推成真实部署、工程可用、业务价值或公共成效。

#### 新领域治理构造器 new_domain_governance_builder

面对新领域时，AI 先构造临时领域 trace，而不是查主协议是否已经覆盖该领域。构造器只服务本轮项目主张；如果后续发现它跨项目反复有效，再通过规则晋升机制写回主协议或经验库。

```yaml
new_domain_governance_builder:
  domain_hypothesis:
  primary_claim_to_prove:
  category_route:
    primary_library: research_data_model | engineering_software_product | education_practice_public_service | organization_business_governance | communication_culture_design
    high_risk_regulatory_tags:
      - health | safety | law | privacy | minors | finance | food | transport | mental_health | intellectual_property | other
    why_this_route:
  selected_lenses:
    - claim_ladder
    - evidence_contract
    - stakeholder_context
    - execution_validation
    - risk_ethics_permission
    - operation_handoff
    - transfer_boundary
    - deliverable_storyline
	  source_role_map:
	    - source_url:
	      source_owner:
	      source_role: project_existence | rules_or_requirements | task_definition | authority_background | benchmark_data | implementation_evidence | outcome_evidence | media_report | secondary_interpretation
	      can_support_claims:
	      cannot_support_claims:
	  source_authority_precedence_trace:
	    trigger: multiple_sources_same_claim | source_self_claims_authority | date_or_rule_conflict | high_risk_claim
	    claim_scope:
	    precedence_order:
	      - source_url:
	        authority_rank:
	        governs:
	        does_not_govern:
	        basis:
	    conflict_rule:
	    freshness_or_version_check:
	    fallback_if_unresolved:
	  domain_specific_questions:
	    - question:
	      why_it_matters:
	      evidence_needed:
  micro_task_to_execute:
  evidence_needed:
  downgrade_rule:
  promotion_decision: use_once | add_to_experience_library | propose_protocol_rule | reject_as_too_specific
```

通用镜头定义：

| 镜头 | 要回答的问题 |
| --- | --- |
| `claim_ladder` | 最终想证明什么；哪些只是活动输出、过程材料、代理指标、样例或假设；哪些结论不能外推。 |
| `evidence_contract` | 需要哪些来源、现场材料、数据、权威依据、版本和时效；每个证据能支撑到哪一句。 |
| `stakeholder_context` | 谁是使用者、受益者、风险承担者、执行者、复核者和承接者；是否存在弱势群体或被影响公众。 |
| `execution_validation` | 最小闭环是什么；如何验收、复现、测试、抽样、访谈、观察或运行；失败样例如何记录。 |
| `risk_ethics_permission` | 是否涉及授权、隐私、安全、伦理、未成年人、健康、法律、财务、知识产权或监管边界。 |
| `operation_handoff` | 谁负责资源、时间、维护、培训、转交、申诉、整改、长期承接和退出。 |
| `transfer_boundary` | 从竞赛、样机、demo、调研、活动、证书、备案、评分、PR、新闻或专家意见到真实效果，中间缺哪层证据。 |
| `deliverable_storyline` | 最终成果如何讲清“问题 -> 证据 -> 行动 -> 边界 -> 下一步”，而不是只堆过程和好词。 |

判断规则：

1. 每个新项目先写 `primary_claim_to_prove`，再选镜头；没有主张就不能套模板。
2. 一轮默认只展开 3-5 个最高杠杆镜头，其余记录为不展开原因。
3. 若触发 high_risk_regulatory_tags，必须至少展开 `risk_ethics_permission` 和 `stakeholder_context`。
4. 如果旧经验库有相近案例，只引用其失败模式和可迁移问题，不复制旧领域长字段。
	5. 构造出的临时 trace 必须包含降级规则；没有降级规则，说明主张边界还没想清楚。
	6. 外部来源必须先进入 `source_role_map`。项目官网、比赛页、通知、论文、新闻、排行榜、PR、评审结果和现场材料的证据角色不同；不能把“项目存在/规则明确/任务定义”外推为“效果已经发生/真实场景已经改善”。
	7. 当多个来源覆盖同一类规则、日期、要求、程序、API 行为、报价、许可、医疗/安全判断或事实主张，或任一来源自称 official / authoritative / sole source 时，必须补 `source_authority_precedence_trace`。`source_role_map` 只说明“各来源能支撑什么”，不能替代“冲突时谁优先”。若权威优先级无法确认，结论必须降级为“待核验/以官方规则为准/需人工确认”，不得把二手摘要、宣传页、时间线视图或邮件材料写成最终裁决。

#### 六类经验库路由 category_experience_router

旧真实项目练习沉淀为经验库，而不是主协议主体目录。经验库条目至少保留 `trace_id`、`source_pressure_test_file`、`failure_mode_id`、`regression_case_id`、`current_as_of`、`primary_library`、`risk_tags`，保证新领域能回查来源。

```yaml
category_experience_router:
  project_summary:
  primary_library:
  high_risk_regulatory_tags:
  experience_library_entries:
    - trace_id:
      source_pressure_test_file:
      failure_mode_id:
      reusable_method:
      non_transferable_detail:
  common_failure_modes_to_check:
  generated_lenses:
  not_using_legacy_directory_reason:
```

大类路由：

| 大类 | 典型主张 | 优先镜头 |
| --- | --- | --- |
| 研究/数据/模型 | 结论可靠、预测有效、样本代表、实验真实、指标可解释 | `claim_ladder`、`evidence_contract`、`execution_validation`、`transfer_boundary` |
| 工程/软件/产品 | 原型可靠、系统可用、开源采纳、产品交付、工程可部署 | `execution_validation`、`operation_handoff`、`transfer_boundary`、`risk_ethics_permission` |
| 教育/社会实践/公共服务 | 学生学会、服务有效、公共问题改善、对象受益、长期承接 | `stakeholder_context`、`execution_validation`、`risk_ethics_permission`、`deliverable_storyline` |
| 组织/商业/治理 | 组织运行、市场验证、政策采纳、程序公平、资源配置有效 | `evidence_contract`、`stakeholder_context`、`operation_handoff`、`transfer_boundary` |
| 传播/文化/设计 | 认知改变、传播有效、文化理解、审美/科学/品牌影响 | `claim_ladder`、`stakeholder_context`、`execution_validation`、`deliverable_storyline` |
| 高风险监管标签 | 健康、安全、法律、隐私、未成年人、财务、食品、交通、心理、知识产权等 | 横切触发 `risk_ethics_permission`、`stakeholder_context`、`operation_handoff`，不得被主类覆盖。 |

#### 追踪模块路由 trace_module_router

高风险或高返工项目追踪必须先路由后启用，避免把所有经验库条目套给每个项目。

```yaml
trace_module_router:
  project_type:
  primary_claim_to_prove:
  category_route:
  high_risk_regulatory_tags:
  always_on_modules:
    - current_basis
    - evidence_matrix
    - decision_log
    - traceability_matrix
  selected_lenses:
    - lens:
      trigger_signal:
      reason:
  experience_library_references:
    - trace_id:
      source_pressure_test_file:
      failure_mode_id:
      reusable_method:
  explicitly_not_expanded:
    - lens_or_experience:
      reason:
  max_user_visible_questions:
  compression_rule:
```

判断规则：

1. 先判断最终要证明的主张，再判断大类和风险标签。
2. 经验库只提供问题意识和失败模式，不把历史模板原样复制进当前项目。
3. 除非项目确实跨域，否则一轮只展开 3-5 个最高杠杆镜头。
4. 未展开的镜头记录为不适用或本轮不展开，不得隐形丢弃。
5. 用户可见回复只说明启用哪些镜头和原因，完整字段写入前置治理文件。

#### 规则晋升机制 rule_promotion_mechanism

```yaml
rule_promotion_mechanism:
  candidate_rule_or_lens:
  source_experience_entries:
  repeated_across_projects:
  abstracts_to_common_failure_mode:
  improves_new_domain_construction:
  reduces_or_preserves_user_friction:
  anti_protocol_bloat_gate:
    trigger_signal:
    observable_behavior:
    required_evidence_or_check:
    route_back_if_failed:
    user_friction_impact:
  decision: write_to_protocol | add_to_experience_library | merge_with_existing | backlog | reject
```

1. 单一领域字段默认进入经验库，不进入主协议。
2. 能跨项目迁移的不是领域名，而是失败模式、证据缺口、降级规则和小题验证方法。
3. 如果新增规则让用户入口变重，必须同时压缩用户可见入口或拒绝写入。
4. 旧规则被压缩或替代时，必须在经验库索引保留可追溯路径。

#### 经验库索引 legacy_experience_library_reference

经验库索引位置：`/Users/chuchenqidawang/Documents/complex-project-front-governance/protocol/持续治理协议_真实项目经验库索引_20260622.md`。

经验库用途：

1. 回查旧压力测试如何暴露失败模式。
2. 为新领域生成 `domain_specific_questions`。
3. 提供降级表述、不能外推边界和小题实测样例。
4. 支撑规则晋升或拒绝新增规则的证据。
5. 保证主协议不再靠场景目录扩张来获得深度。

经验库不做：

1. 不替代新项目的行业最佳实践调查。
2. 不自动展开所有旧 trace。
3. 不把历史案例当成当前事实。
4. 不让用户阅读长目录后自行选择。
#### EOF 追加护栏 append_only_eof_guard

长期日志或机器看版新增编号章节时，必须防止新章节进入历史中部。

```yaml
append_only_eof_guard:
  target_file:
  old_tail_heading:
  append_method: append_eof_section_tool | equivalent_mechanical_eof_append | explicit_tail_anchor_fallback
  tool_path:
  expect_old_tail:
  expect_new_tail:
  expect_new_headings:
  heading_scan_method: stateful_fenced_block_scan
  new_section_headings:
  latest_heading_after_append:
  pseudo_heading_in_code_count:
  latest_pending_count:
  moved_from_middle_to_tail: yes | no
  next_route_after_append:
```

判断规则：

1. 新增编号章节默认通过 EOF 机械追加；不得用宽上下文锚点匹配旧机器看版。
2. 追加前记录旧尾部标题；追加后扫描真实标题和代码块伪标题；伪标题计数必须基于 fenced-code 状态机，不能把代码块关闭符后面紧跟的真实标题误判为伪标题。
3. 最新机器看版必须是文件尾部最后一个二级标题。
4. 如果新章节被插到中部，必须立即机械搬移到尾部，并把这次修复写入机器看版。

#### 来源链接与时效性抽检 source_link_recency_audit

重大报告中所有关键权威来源，至少抽检核心来源并记录来源层级和时效边界。

```yaml
source_link_recency_audit:
  - source_id:
    claim_supported:
    source_level: primary | official_reprint | secondary | theory_reference | news_background
    link:
    current_as_of:
    link_status: checked | unstable | broken | not_checked
    preferred_citation:
    supports_only:
    cannot_support:
    required_report_change:
```

判断规则：

1. 政策文件优先使用原始发布机构；转载页只能作为备份或补充。
2. 国际组织报告必须记录标题、机构、年份、链接或文档编号。
3. 新闻来源只能支撑背景事件，不替代政策、研究或现场证据。
4. 社会科学理论可以支撑解释框架，不能直接证明项目现场事实。
5. 含“最新、当前、已经、普遍、证明”等高强度表述时，必须确认来源时效与证据等级匹配。

#### 渲染产物新鲜度检查 rendered_artifact_freshness

如果项目存在 Markdown/脚本源稿与 Word、PDF、图片、网页、压缩包等下游产物，必须记录产物是否和源稿同步。

```yaml
rendered_artifact_freshness:
  - source_file:
    rendered_artifact:
    source_modified_at:
    artifact_modified_at:
    freshness_status: fresh | stale | unknown | not_applicable
    sync_action:
    qa_status: rendered_pass | structural_scan_pass | render_blocked | not_checked
    qa_blocker:
    repair_attempted:
    repair_result:
    render_evidence:
      output_dir:
      page_count:
      pdf_path:
      sampled_pages:
      warnings:
    qa_state_transition: unchanged | blocked_to_pass | pass_to_stale | stale_to_pass
    user_visible_note:
```

判断规则：

1. 如果源稿比交付物新，交付物默认 stale，不能继续称为最终版。
2. 如果只做了结构扫描，没有视觉渲染，qa_status 必须写 `structural_scan_pass`，不能写 `rendered_pass`。
3. 如果渲染失败是环境依赖问题，记录 `render_blocked` 和具体失败原因；不要把工具失败误判为文档通过。
4. 如果渲染失败可定位到本地工具链依赖，优先尝试低风险修复、复用已存在的捆绑依赖或换用等价渲染路径；不能只因第一次失败就永久留下 `render_blocked`。
5. 如果阻塞被修复，必须记录 `qa_state_transition: blocked_to_pass`、输出目录、页数、PDF 或图片证据、抽检页和残留 warning；同时更新发布包、变更清单和恢复链验证工具，避免旧 blocked 状态继续误导后续恢复。
6. 对用户最终交付时，必须说明哪个文件是最新可用版本。

#### 当前恢复入口作用域扫描 current_scope_recovery_scan

恢复链扫描必须先定作用域，再判断 stale。全文 `rg` 只能发现候选命中，不能单独证明当前恢复入口过期。

```yaml
current_scope_recovery_scan:
  current_scope:
    release_package_recovery_entry:
    change_inventory_current_recovery_entry:
    latest_machine_board_eof:
  historical_record_scope:
    historical_changelog_rows:
    old_machine_board_sections:
    failure_mode_examples:
    archived_routes:
  scan_result:
    current_scope_hits:
    archive_hits:
    ambiguous_archive_hits:
    stale_status: fresh | stale | unclear
    decision_basis:
```

判断规则：

1. 只有 current_scope 中出现旧恢复入口、旧 next_route、未闭合 pending 或错误 QA 状态，才判定当前 stale。
2. historical_record_scope 中出现旧恢复入口或旧 route，只能标记为 `archive_hit`；除非它被当前恢复入口引用，不能要求删除。
3. change_inventory、release_package 或历史产物表保留旧恢复入口时，同一行或同一条记录必须显性写出“历史记录”“不再作为当前入口”或 `archived_recovery_entry`；没有标签的旧入口标为 `ambiguous_archive_hit`，先修复标签再继续扩展。
4. 如果一个文件同时包含当前入口和历史记录，必须优先解析“当前恢复入口”段、发布包恢复入口段和 EOF 最新机器看版。
5. 如果没有明确 current_scope，先修复恢复入口结构，再继续做真实项目压力测试或协议扩展。

#### 综合恢复链验证 verify_governance_recovery_tool

本工具用于把 post-change scan 从一次性内联脚本升级为可复用验证。凡是连续优化、发布包更新、变更清单更新、机器看版推进或历史入口修复后，都应优先运行该工具或等价综合扫描。

```yaml
verify_governance_recovery_tool:
  tool_path:
  preset: continuous-self-optimization | custom | none
  latest_heading:
  expected_route:
  auto_old_current_markers: yes | no
  required_files:
    protocol:
    long_log:
    release_package:
    change_inventory:
    route_table:
	  checks:
	    tail_matches_latest_heading:
	    latest_heading_count:
	    pseudo_heading_count:
	    latest_pending_count:
	    release_points_latest_heading:
	    changelog_points_latest_heading:
	    old_current_markers_historical:
	    render_qa_state_consistent:
	    subagent_field_coverage:
	    capability_discovery_cadence_gate_field_coverage:
	    skill_plugin_learning_field_coverage:
	    skill_plugin_project_fit_field_coverage:
	    best_practice_learning_contract_field_coverage:
	    capability_type_and_side_effect_gate_field_coverage:
		    external_state_write_guard_field_coverage:
		    skill_plugin_discovery_gate_field_coverage:
		    integration_lifecycle_gate_field_coverage:
		    transactional_integration_consistency_guard_field_coverage:
		    agentic_orchestration_capability_builder_field_coverage:
		    subagent_orchestration_pattern_router_field_coverage:
	    source_authority_precedence_field_coverage:
	    subagent_method_learning_field_coverage:
	    desired_state_reconciliation_guard_field_coverage:
	    stateful_data_migration_guard_field_coverage:
	    security_incident_response_guard_field_coverage:
	    data_artifact_lineage_freshness_guard_field_coverage:
	    subagent_result_coverage_gate_field_coverage:
	    main_agent_integration_review_field_coverage:
	    claim_readiness_ladder_field_coverage:
	    parallel_evidence_lane_field_coverage:
	    claim_lane_binding_field_coverage:
	    deployment_readiness_gate_field_coverage:
		    forbidden_terms_absent:
		    preset_requirements_applied:
  failure_count:
  accepted_as_current_basis: yes | no
  reroute_if_failed:
```

判断规则：

1. 工具必须使用 fenced-code 状态机识别真实二级标题，避免把正常标题、代码块关闭符后的标题或历史示例误判为伪标题。
2. 恢复链验证不能只证明“关键词存在”；必须同时证明最新机器看版在 EOF、发布包和变更清单指向同一 latest_heading 和 expected_route。
3. 旧机器看版、旧 route 和旧恢复入口允许存在于历史记录中，但必须被识别为 historical/archive scope；无法判定作用域时标记 ambiguous_archive_hit，而不是直接删除。
4. 未完成 QA 必须保持降级状态，例如 `render_blocked`；综合扫描不得把依赖缺失伪装成视觉通过。若 QA 已被重新渲染并抽检通过，综合扫描必须改为检查 `rendered_pass` 与页数、输出目录、PDF/图片证据是否同时存在，不能继续强制保留旧阻塞。
		5. 连续自我优化默认使用 `--preset continuous-self-optimization`，由工具自动填充常驻 forbid、required 和 `--auto-old-current-markers`；除非本轮有明确不同的恢复链范围，否则不得手写一长串易漂移参数替代 preset。preset 必须覆盖近期晋升的核心字段；新增 `subagent_problem_decomposition_builder`、`source_role_map`、`spawn_preflight`、`agent_return_status`、`subagent_lifecycle_ledger`、`capability_discovery_cadence_gate`、`skill_plugin_learning_loop`、`skill_plugin_project_fit_trace`、`best_practice_learning_contract`、`capability_type_and_side_effect_gate`、`external_state_write_guard`、`skill_plugin_discovery_gate`、`integration_lifecycle_gate`、`transactional_integration_consistency_guard`、`agentic_orchestration_capability_builder`、`subagent_orchestration_pattern_router`、`desired_state_reconciliation_guard`、`stateful_data_migration_guard`、`security_incident_response_guard`、`data_artifact_lineage_freshness_guard`、`software_delivery_state_boundary_guard`、`source_authority_precedence_trace`、`subagent_method_learning_trace`、`subagent_result_coverage_gate`、`main_agent_integration_review`、`claim_readiness_ladder` 等字段后，恢复链验证必须能在缺字段时失败。
6. 如果工具输出 failure_count > 0，本轮不能宣称恢复链已收口；应先修复失败项或在机器看版中显性降级并写 reroute。
7. 机器看版中的验证状态必须和实际命令一致；若已运行恢复链验证，不得继续保留 `recovery_verifier_to_run` 一类待运行状态。

#### 数值计算追踪 numeric_calculation_trace

如果项目包含实验浓度、稀释倍数、不确定度、财务测算、统计指标、工程参数、单位换算或任何带数字的结论，必须建立数值计算追踪。

```yaml
numeric_calculation_trace:
  - numeric_claim:
    value:
    value_identity: measured | certificate_or_spec | demonstrative_parameter | derived_calculation
    source_file_or_record:
    inputs_with_units:
    formula:
    recalculation_status: checked | not_checked | blocked
    boundary_or_scope:
    cannot_support:
    replacement_condition:
```

判断规则：

1. 示范参数必须显式标注，不能写成真实测量结果。
2. 派生计算值必须能回到输入量、单位和公式。
3. 单位换算必须写清，例如 `ug/L`、`mg/L`、`mg/kg`、`g/L`、质量比和体积比不能混用。
4. 不确定度、概率、浓度、收益、减排、节约比例等数字必须说明边界；局部计算不能外推成系统结论。
5. 如果复算未完成，结论必须降级为待验证，不得以精确数字制造可靠性幻觉。

### 低摩擦反馈节奏

高风险或高返工项目默认设置四个低摩擦反馈点：

1. **方向前**：给 2-4 个候选抓手/案例/路线，并标推荐项。
2. **收束前**：用 5 行说明当前主链、牺牲项和最大返工风险。
3. **长文前**：给目录样张或 10% 粗稿。
4. **交付前**：列最终验收标准、证据等级不足项和用户可一票否决项。

如果用户明确授权连续推进，可不逐一等待，但必须在 handoff 中写：

```yaml
feedback_gate:
  planned_points:
  skipped_points:
  skip_reason:
  max_rework_risk:
  next_user_can_still_change:
```

### 高风险/高返工项目自评分

高风险或高返工项目每轮阶段性交付后，必须给出自评分，至少包含：

| 维度 | 含义 |
| --- | --- |
| 状态恢复 | 只读 handoff 能否恢复 |
| 用户反馈摩擦 | 用户是否能用很少反馈改变方向 |
| 证据硬度 | 核心判断是否有证据矩阵支撑 |
| 决策透明度 | 重大取舍是否有 decision_log |
| 追踪完整度 | 用户诉求是否能追到交付物 |
| 幻觉防护 | 是否做 post_change_key_node_scan |
| 交付可用性 | 最终成果是否能被真实读者使用 |

自评分不能只给总分。低于 0.80 的维度必须进入下一轮 backlog。

## 8.8 Agent 自我优化模式

本规则用于处理用户要求“优化你自己”“优化协作流程”“复盘 AI 工作方式”的情况。Agent 自我优化不是人格化自夸，也不是写一段“我会更努力”；它必须把失败模式转成可触发的规则、可检查的行为、可复用的评估样例和可回归测试的任务。

### 方法来源

本规则借鉴以下成熟做法：

1. **LLM / agent evals**：把抽象能力拆成代表性任务、期望行为、失败类型和可重复评分。参考 OpenAI Evals（https://github.com/openai/evals）和 Anthropic agent evals（https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents）。
2. **ReAct / tool-using agents**：复杂任务中推理、行动、观察和修正必须交替发生，不能只在脑内规划。参考 ReAct paper（https://arxiv.org/abs/2210.03629）。
3. **Reflexion / verbal self-reflection**：反思只有在写成下一轮可用的策略或记忆时才有价值。参考 Reflexion paper（https://arxiv.org/abs/2303.11366）。
4. **Effective agent patterns**：优先采用简单、可组合、可观察的 agent/workflow 模式，而不是堆复杂框架。参考 Anthropic Building Effective Agents（https://www.anthropic.com/research/building-effective-agents）。
5. **Regression testing**：修复过的失败必须进入回归样例，防止下次以不同形式复发。
6. **Human-in-the-loop evaluation**：主观、高风险或用户品味相关任务，必须用低成本反馈采样校准，而不是等待终稿验收。

### 触发条件

出现任一条件，默认进入 agent_self_optimization_mode：

1. 用户要求优化 AI 自己、优化流程、优化协作方式、降低摩擦或复盘失败。
2. 同一类失败连续出现，例如空泛、幻觉、忘记状态、没有搜索最佳实践、没有同步 plan、没有显性化人工操作、交付物与事实不一致。
3. 自评分低于 0.80 的维度需要进入下一轮 backlog。
4. 协议已经变长但用户入口没有变简单，存在“治理复杂度转嫁给用户”的风险。

### 自我优化最小包

```yaml
agent_self_optimization_mode:
  trigger:
  target_behavior:
  failure_modes:
  regression_cases:
  eval_rubric:
  tool_discipline:
  user_friction_budget:
  next_behavior_change:
```

#### 失败模式库 agent_failure_modes

每次复盘至少记录一个失败模式。失败模式必须可观察、可触发、可修正。

```yaml
agent_failure_modes:
  - failure_id:
    symptom:
    root_cause:
    trigger_signal:
    bad_default_behavior:
    corrected_behavior:
    detection_check:
    regression_case:
    status: open | mitigated | resolved | recurring
```

常见失败模式：

1. **premature_completion**：还没有完成验证就收尾。
2. **hidden_assumption**：把用户未说出的标准当作已知。
3. **low_specificity**：输出宏大但不可执行。
4. **source_blending**：把权威来源、二手材料、推断和样例混在一起。
5. **tool_state_drift**：文档里有 Plan/Goal，但 Codex 工具状态不同步。
6. **handoff_decay**：机器看版不足以恢复状态。
7. **feedback_gate_skip**：重大路线选择前没有给用户低成本反馈入口。
8. **post_change_scan_skip**：修改后没有做关键节点扫描。
9. **over_protocolization**：协议越来越长，但用户入口没有更简单。
10. **continuous_cycle_drift**：用户要求持续推进时，AI 要么过早收尾，要么无边界空转，没有按机器看版逐轮推进。
11. **user_visible_bloat**：把证据矩阵、机器看版和内部字段整段展示给用户，导致治理负担从 AI 转嫁给用户。
12. **append_anchor_drift**：新增章节时使用非唯一锚点，导致内容插入到历史章节中间，破坏日志顺序或状态恢复。
13. **goal_boundary_miss**：用户明确给出长期持续目标时仍不创建 goal，或用户只给普通一次性任务时擅自创建 goal。
14. **deliverable_execution_gap**：最终报告主张漂亮，但没有追踪到执行工具、现场证据字段和降级规则。
15. **authority_link_decay**：最终报告引用了权威来源，但没有抽检原始链接、转载关系、时效性和来源能支撑到的结论边界。
16. **rendered_artifact_stale**：源稿已经修改，但 Word/PDF/图片等下游交付物仍是旧版本，或视觉渲染 QA 失败却未显性记录。
17. **scan_output_bloat**：扫描命令有效但输出过大，整段 XML/JSON/日志淹没真正的检查结果，降低状态恢复和用户可见压缩质量。
18. **change_inventory_gap**：连续迭代修改多个产物后，没有清单说明哪些文件被改、为什么改、如何验证、从哪里恢复。
19. **numeric_trace_gap**：数字结论看起来精确，但没有说明数值身份、单位换算、公式、复算状态和适用边界。
20. **local_project_pool_bias**：把“真实项目/比赛项目/题库渠道”误收窄为当前工作区、目录名称、本地历史文件、当前本地 AI 科研材料、AI 熟悉领域或上一轮主题，没有先扫描现实时间外部项目渠道。
21. **machine_board_tail_drift**：新增章节或机器看版存在于文件中部，文件尾部仍是旧看版；后续恢复若只读 tail，会沿着过期 next_route 继续工作。
22. **output_effect_confusion**：把照片、PPT、作品、demo、活动场次、证书、推文、播放量、评分、合格、备案或新闻，当成真实效果或公共价值。
23. **one_pass_reliability_gap**：把一次通过、一次演示、一次验收、一次无事故、一次 PR 合并或一次比赛完成，当成长期可靠、真实运行稳定或可规模复制。
24. **governance_document_reality_gap**：把制度、名单、公示、协议、备案、流程图、职责表或承诺书，当成治理已经有效、合规已经闭环或责任已经落实。
25. **sample_to_population_gap**：把问卷、访谈、样本、个案、显著性检验、课堂反馈或平台数据，外推成总体事实、因果解释或长期趋势。
26. **goodwill_permission_gap**：把公益善意、学校安排、组织同意、服务时长、儿童笑脸、感谢信或满意度，当成知情同意、权益保护、隐私授权或安全转介已经完成。
27. **simulation_competition_reality_gap**：把竞赛、模拟、样机、仿真、CTF、模拟法庭、建模、渲染、企业赛题或 demo 结果，直接转译成真实部署、真实服务、工程可靠或实际治理能力。
28. **authority_source_overclaim**：把政策、通知、新闻、专家意见、转载、论文背景或平台介绍，当成项目现场证据、因果证明或当前可用事实。
29. **domain_directory_sprawl**：把每次真实项目练习都写成新的主协议场景模板，导致协议越来越像领域目录，而不是更会面对新领域。
30. **experience_library_traceability_loss**：宏观重构时只保留 6 类名称，丢失旧 trace_id、压力测试文件、失败模式、回归样例和 current_as_of，导致经验库不可追溯。
31. **expectation_only_regression_gap**：自我优化或协议优化只写 user_prompt_pattern、expected_behavior、forbidden_behavior 和 pass_condition，却没有实际做一个小题、跑一次扫描、核一个来源、填一个 trace 或产出可检查证据。
32. **friendly_case_pressure_test_gap**：真实项目压力测试只选择容易解释、适合协议现有结构的友好样例，或只列优秀案例和链接，没有纳入工程、软件、企业交付、开源维护、真实运行流程等敌意样例。
33. **subagent_orchestration_gap**：复杂项目具备并行核验、领域审查、独立 QA 或多文件交付机会时，没有评估 superpower/subagent；或者开了子代理但没有清晰边界、集成审查和超时/拒收记录。
34. **protocol_bloat_gate_skip**：新增规则、镜头或模板时没有先过 anti_protocol_bloat_gate，缺少触发信号、可观察行为、必需证据、route-back 或用户摩擦影响。
35. **append_only_middle_insertion_gap**：新增章节或机器看版存在，但不在文件尾，导致恢复入口仍沿旧机器看版继续。
36. **dynamic_route_arbitrariness_gap**：动态阶段控制器只记录最终 mode、route_event 或 subagent_strategy，没有记录其他可选路线、拒绝理由、触发证据、用户摩擦影响和重评条件，导致后续恢复者无法判断这是证据驱动还是随意选择。
37. **current_historical_scope_confusion**：恢复链扫描把历史记录、旧机器看版、失败模式案例或 archive route 中的旧入口误判为当前 stale；没有先区分 current_scope 和 historical_record_scope，导致 AI 修错地方或删除合法历史证据。
38. **ambiguous_archive_recovery_row**：change_inventory、release_package 或历史产物表中保留旧恢复入口、旧机器看版或旧 next_route，却没有在同一条记录显性标明历史记录、不再作为当前入口或 archived_recovery_entry，导致后续扫描必须靠上下文猜测其身份。
39. **subagent_capability_overclaim**：机器看版或计划写 `subagents.capability: available`，但没有记录 tool_search/tool 表发现、spawn_agent 尝试、agent_id、wait_status 和 integration_decision；把环境中列出子代理名称误当成可调度、已返回或已集成。
40. **subagent_lifecycle_cleanup_gap**：子代理已经返回、超时、阻塞、被拒收或不再需要，但没有记录 close_agent/close_status/previous_status_summary/repeated_close_result/cleanup_decision，导致后续恢复者不知道代理是否仍占用并发槽、是否还要等待或是否已经关闭。
41. **append_eof_tool_missing**：长期日志新增编号章节时没有使用 append_eof_section_tool 或等价机械 EOF 追加流程，也没有记录 expect_old_tail、expect_new_tail、新标题唯一性、pseudo_heading_count 和 latest_pending_count，导致新章节仍可能靠宽上下文锚点误插历史中部。
42. **ad_hoc_recovery_scan_drift**：恢复链收口依赖每轮临时手写脚本或零散 `rg`，导致正则误判、检查口径漂移、发布包/变更清单/机器看版未按同一 expected_route 校验，或把历史入口、未完成 QA 和当前恢复入口混在一起。
43. **recovery_verifier_invocation_drift**：虽然已有 verify_governance_recovery_tool，但每轮仍手写很长的 `--require`、`--forbid` 和 `--old-current-marker` 参数，导致漏填历史入口、漏填 forbid 项或忘记 QA 降级检查；连续自我优化应使用标准 preset 和自动旧入口推导。
44. **meta_tooling_loop_drift**：连续自我优化在恢复链已干净后仍连续修工具、机器看版、子代理生命周期或验证器细节，导致协议优化脱离真实项目、新领域构造和最终交付可用性；需要用最近章节类型扫描把 next_route 拉回真实项目压力测试或真实交付检查。
45. **route_back_label_without_real_project_trace**：机器看版写了“回到真实项目/新领域构造”，但下一轮没有 source_url、category_route、selected_lenses、micro_task_to_execute、evidence_needed 和 downgrade_rule；route-back 只停留在标签，未真正检验协议面对新项目的构造能力。
46. **render_qa_state_stale_after_repair**：交付物视觉渲染曾因工具链依赖阻塞，后来已修复并生成页图/PDF/抽检证据，但发布包、变更清单或恢复链验证器仍强制保留 `render_blocked`，导致后续恢复者误以为交付物仍不可视觉验证。
47. **subagent_context_dumping_gap**：主代理没有先拆出独立工作包、输入上下文包、验收证据和集成计划，就把整段会话、整份计划或一堆文件丢给子代理，导致子代理重复探索、误解边界、越权修改或输出难以集成。
48. **source_role_overclaim_gap**：外部来源只证明项目存在、规则、任务定义、权威背景或媒体报道，却被写成现场效果、因果改进、可推广能力或长期价值证据。
	49. **verifier_required_field_drift**：主协议新增了核心治理字段或失败模式，但 `verify_governance_recovery_tool --preset continuous-self-optimization` 没有同步 required/forbid 检查，导致关键字段被删除、遗漏或机器看版保留待运行状态时恢复链仍误报通过。验证器内部不得把同一批核心 required 字段在多个 scope 手写复制；应维护 `core_required + scope_required_extras` 这类单一核心源，生成各 scope required，并用测试锁住生成方式、scope extras 精确匹配和缺失/多余 scope 的失败行为，防止 `verifier_required_core_source_drift`。
	49.1. **capability_discovery_cadence_gap**：新任务或连续优化轮次没有在进入执行前显性盘点 local_skills、callable_tools、deferred_tools、plugins/connectors、external APIs/methods，或阶段切换、用户新增要求、阻塞/验证失败、外部写入/子代理边界、最终主张前没有重新考虑能力组合，导致错过可用工具、误用不适配 skill、把 tool_search 当成永不需要或每次机械联网。
	50. **skill_plugin_learning_loop_gap**：用户明确要求学习网上方法、skill 或插件，或任务明显触发某个 skill/plugin，但协议只记录了发现名称，没有证明主代理读完指令、抽取硬约束、完成小题试用、写回规则、同步验证器和恢复链引用，导致“学过”无法迁移成下一次可执行能力。
	51. **skill_plugin_detached_from_project_gap**：skill/plugin 学习闭环自洽，但没有绑定当前真实项目的主张、阶段缺口、验收链、协作方式或交付证据；结果是工具学习本身通过了，项目却没有更可执行、更可验证或更低摩擦。
52. **source_authority_flattening_gap**：多个来源同时覆盖同一规则、日期、要求、程序或事实主张时，只标注 source_role_map，却没有记录权威优先级和冲突裁决；结果是摘要页、宣传材料、时间线视图、邮件或二手报道可能覆盖真正的规则、标准、合同、API 文档、许可证或监管文件。
53. **subagent_method_name_drop_gap**：用户要求学习网上方法、skill 或插件来提升子代理能力时，只把 Anthropic/OpenAI/Google/Superpowers 等名称写进文档，没有抽取独立问题域、上下文隔离、handoff/guardrail、review/integration 等可执行约束，也没有用当前项目小题验证，导致“学习方法”变成装饰性引用。
54. **impact_inference_lane_mismatch_gap**：证据泳道已经拆开，但没有把每条 lane 绑定到 claim_ladder；结果是活动量、制品产出、地图覆盖、代码提交、课程场次或问卷样本被误用来证明真实使用、公共效果、学生改变、受益者结果或长期影响。
55. **benchmark_to_deployment_overclaim_gap**：研究、数据、模型、竞赛、离线评测或工程验收只证明特定数据集、评分函数、测试环境或样机条件下的性能，却被写成真实部署、临床/教育/生产决策改善、安全有效或长期效果；缺少外部有效性、真实工作流、权限合规、风险监控和承接责任证据。
56. **best_practice_name_drop_gap**：用户要求学习网上方法或行业最佳实践时，只列平台、框架、名人、机构或案例名称，没有写出 stage_gap、practice_pattern_extracted、minimum_application_test 和 non_transfer_boundary，导致“参考了先进方法”不能改善当前项目。
57. **capability_side_effect_blind_spot**：把 skill、plugin、connector、local_tool、web_source 和 external_method 混为一谈，未记录 operation_mode、side_effect_level、权限边界或外部写入风险，导致本该人工授权或降级的插件/连接器被当作本地只读资料使用。
58. **skill_plugin_discovery_bias_gap**：任务触发 skill/plugin/tool 时，只凭记忆或习惯选择一个能力，没有记录候选集、拒绝理由、instruction_read_evidence 和 call_or_skip_decision，导致“显然适配”无法被复盘。
59. **subagent_contract_coverage_gap**：子代理返回后只记录 accepted/rejected，没有逐项核对 contract_items、returned_items、unverified_items 和 out_of_scope_items，导致未覆盖风险被主代理误认为已审计。
60. **claim_readiness_jump_gap**：结论没有绑定 claim_readiness_ladder，把 source-backed、locally verified 或 small-loop validated 的结果写成 pilot ready、production ready 或 public impact ready。
61. **external_state_write_blind_spot**：只记录 external_read / external_write 或 plugin/connector 名称，没有记录 permission_scope_requested、external_state_target、sensitive_data_class、subagent_capability_boundary、sandbox_or_dry_run_evidence、rollback_or_reversal_plan 和 explicit_user_authorization，导致 AI 可能越权写入仓库、课程、名单、成绩、公开发布或账号配置。
62. **component_capability_composition_gap**：A 系统支持某标准、B 系统支持同一标准，就被外推出二者组合可互通、可试点或可生产上线；缺少同一版本/部署/关键流程端到端证据，也没有检查 maintenance mode、sunset、deprecation、new-user freeze、partner transition、退役日期或支持路线图变化。
63. **transactional_event_consistency_gap**：外部写入和集成生命周期已经检查，但异步交易、webhook、消息、回调或可重试请求缺少幂等键、重复事件处理、重试/重放策略、乱序假设、权威状态源、对账日志、test/live 边界和高影响动作补偿方案，导致重复扣款/发货/创建资源或状态不一致被误写成生产可用。
64. **agentic_orchestration_capability_shell_gap**：用户要求学习网上方法、skill 或插件来提升子代理能力时，只新增字段或引用框架名，没有形成 `agentic_orchestration_capability_builder` 所要求的能力缺口、来源组合、上下文包、验收证据、review gate、主代理集成和生命周期清理，导致“多代理能力提升”仍停留在口号。
65. **desired_state_reconciliation_gap**：Terraform/GitOps/Kubernetes controller 等声明式系统只验证“配置存在、工具支持、plan 可运行或 controller 会同步”，却没有区分 desired_state_source、observed_state_source、plan/diff、drift、锁/单写者、destroy/prune/replace、import/adoption、policy gate、rollback/forward fix 和 operator handoff，导致误把一次 apply/sync、Synced/Healthy 或官方机制写成长期生产安全。
66. **zero_downtime_data_migration_rollback_gap**：数据库 schema、索引、约束、字段重命名、类型变更、回填或数据模型重构只验证 migration 文件、测试库通过或 ORM 能生成 SQL，却没有检查旧新代码与旧新 schema 的兼容窗口、expand/backfill/cutover/contract 顺序、在线 DDL 锁/表重写/索引构建、回填幂等与校验、双写/双读切换、不可逆步骤、备份/恢复或前滚边界、暂停恢复和 owner handoff，导致零停机、可回滚或数据一致性主张越级。
67. **subagent_pattern_name_drop_gap**：用户要求学习网上方法、skill、插件或提升子代理能力时，只记录 routing、agents-as-tools、handoff、orchestrator-workers、group chat、Agents SDK、LangGraph、AutoGen、Superpowers 等模式名，没有先判断单代理是否足够，没有写 rejected_patterns、method_to_work_unit_mapping、role_selection_reason、context_packet_completeness 或 minimum_application_test，导致“多代理编排”仍无法生成可独立验收的 work unit。
68. **agent_topology_blind_spot**：主代理学到了多代理框架、skill 或插件，但没有决定本轮到底是 single_agent、agents_as_tools、handoff、parallel_evidence_lanes、orchestrator_workers、reviewer_loop 还是 user_proxy；也没有写最终答案控制权、状态写入边界、上下文包、并行依赖图、成本收益和降级路线，导致子代理被当作万能劳力或外包最终判断。
68. **security_incident_response_gap**：CTF/writeup、PoC、扫描告警、secret scanning alert、issue/PR、advisory 草稿、CVE/GHSA 编号或补丁合并被直接写成真实系统已入侵、数据已外泄、漏洞已验证修复、用户已通知或披露已完成；缺少受影响资产、授权联系人、事件证据链、分级依据、遏制缓解、凭证吊销轮换、影响范围、修复部署验证、协调披露、通知要求、监控复发和复盘 owner。
69. **data_artifact_lineage_freshness_gap**：数据集、报表、图表、模型、指标、表格或分析输出只凭 README/catalog 描述、lineage 图、BI last refreshed、报表截图、PDF、文件修改时间、单次 DAG 成功、模型 registry 版本或 DOI/canonical link，就被写成当前有效、可复现、可用于决策或可被下游安全引用；缺少 artifact 身份、版本、来源快照、输入 hash、生成/刷新时间、转换逻辑、run/job、代码/参数/环境、质量检查、freshness 检查、checksum、复现配方、下游引用、用途限制和 stale 降级。
70. **data_artifact_guard_checkbox_gap**：已经启用 `data_artifact_lineage_freshness_guard`，但只是把字段名逐项填满，没有标注 direct_observed、derived_from_metadata、inferred、unknown 或 not_applicable，也没有 evidence_uri_or_hash、extracted_value 和 gap_action；结果是未知证据被包装成已验证证据，guard 本身反而制造可决策幻觉。
71. **software_delivery_state_boundary_gap**：issue triage、PR 打开、CI 通过、review approved、merge、release、package 发布、部署、真实用户使用、回滚和监控被压成“交付完成”一个状态；结果是 PR 合并或包发布被误写成生产可用、用户已采用或长期稳定，缺少同版本 release/deployment/usage/monitoring 证据和 claim readiness 降级。
72. **capability_attention_binding_gap**：用户已经点名外部工具、skill、API、账号、数据库、浏览器、Auto Research 或 Complex，但模型没有把这些词转成显式能力候选清单，导致后续仍沿默认路径推进。
73. **research_access_dead_end_gap**：资料、文献或全文找不到时，模型停在 access_exhausted，没有主动升级到 DOI、出版社页、Scholar、浏览器、机构权限、用户代登录或用户上传证据，也没有说明用户可以怎样帮助补齐。
74. **persistent_thread_architecture_gap**：用户提到多线程、长期线程、子代理、Goal 或 Loop 时，模型只做临时任务分组，没有先判断临时子代理、长期 Codex 线程和主线程内部分工的区别，也没有登记职责、状态写回和主线程整合方式。
75. **plan_patch_amplification_drift**：用户在 Plan 模式中补充风格、颗粒度、受众或局部交付细节后，模型把局部补丁放大成新主线，导致原任务目标、验收标准或重点交付物被稀释。
76. **deliverable_contract_ambiguity_gap**：模型没有在交付前确认人看版、老师版、批注版、交付说明、机器看版或第三方版本的受众和边界，把内部治理记录、机器状态或项目术语直接写进给人的成果里。
77. **protocol_onboarding_underread_gap**：新项目要求读取 Complex、Auto Research 或 Complex 项目持续治理协议时，模型没有先理解核心入口、阶段流程、动态路由、能力发现、子代理/线程、Loop/评分和交付拆分规则，就直接开始业务执行，导致“按协议推进”只停留在口头。
78. **protocol_scan_order_ambiguity_gap**：用户要求按 Complex 或完整扫描 Complex 推进时，模型没有说明读取顺序和决策点，导致只读熟悉片段、漏掉 Runtime Kit、连续节拍、Plan/Goal 或交付契约。
79. **scheduled_topology_refresh_gap**：连续节拍开始时评估过多线程/子代理，但后续没有按轮次或主链变化复盘，长期分线程职责滞后于总线程要求，仍按旧上下文输出。
80. **scheduled_capability_refresh_gap**：初始阶段建立过外部工具/skill/API 清单，但后续任务阶段变化后没有定期重评，导致继续使用已经不适配的工具组合，或漏掉后来才变得关键的能力。
81. **plan_mode_full_scan_undercoverage_gap**：用户在 Plan 模式中明确要求完整读取 Complex，但计划没有覆盖协议可借鉴组件、关键词触发、阶段流程、Loop/评分、协作拓扑和 Runtime Kit，只给出普通任务计划。
82. **fake_goal_drift_gap**：Codex goal 或文本目标停留在旧版本、旧需求或旧 next_route，例如 goal 仍写 v32 但项目已推进到 v38；模型没有刷新 goal，却继续让假 goal 驱动实际项目，造成 Loop 停止或目标漂移。
83. **hidden_trigger_vocab_gap**：Complex 把“连续节拍、多线程、外部工具、完整扫描、人看版”等能力藏成内部关键词，没有在入口阶段告诉新用户可以怎样触发，导致用户只能靠反复纠偏发现规则。
84. **major_project_user_mode_confusion_gap**：模型把“普通项目/重大项目”当成用户必须选择的模式，而不是内部工作力度/风险升级判断，造成入口重复、解释负担和错误路由。
85. **optional_goal_plan_loop_gap**：模型把 Plan、Goal 或 Loop 当成某些模式才需要的动作，一次性任务或 Plan 模式中缺少 round_goal、小循环、评分路由或交付契约。
86. **setup_question_missing_gap**：用户只说“按 Complex 推进”时，模型没有先用启动提问卡确认外部能力、子代理/多线程、连续节拍和交付对象，也没有给出安全默认。
87. **prompt_bootstrap_missing_gap**：用户希望先扫描 Complex、设计项目提示词、确认后再执行时，模型直接开工或只给泛泛 prompt，未把协议扫描、启动问题、能力边界、协作拓扑、Goal/Loop、评分路由和交付契约固化成可复制执行提示词。
88. **round_plan_attention_drift_gap**：第二轮或后续 Plan 只关注当下任务，未说明来自总规划、上一轮状态和本轮新增判断的关系，导致总 prompt 退化成背景口号。
89. **master_prompt_decay_gap**：第一轮 `copy_ready_prompt` 没有进入 state、handoff 或后续恢复链，长期目标、交付契约和能力边界逐轮淡化。
90. **round_prompt_missing_gap**：连续节拍新一轮没有先生成 `round_execution_prompt`，就直接进入业务计划或执行，导致 Plan 与 master prompt、active_goal_summary、next_route 脱节。
91. **long_lived_goal_blocked_gap**：模型把“连续节拍直到停止”塞进一个跨几十轮的 Codex 工具 Goal，导致工具 objective 停在旧版本或被判 blocked 后，项目明明可以继续却被误判为受阻。
92. **blocked_goal_false_project_block_gap**：当前工具 Goal 已 blocked，但模型没有回到 current_basis、state、closure-routing 和 next_route 判断项目真实状态，直接把工具状态包装成项目状态。
93. **round_goal_tool_lifecycle_drift_gap**：每轮 round_goal 已完成或版本已迁移，但工具 Goal 没有 complete、迁移或降级为 protocol_round_goal，造成后续 Plan/Loop 被旧目标牵引。
94. **premature_convergence_greedy_gap**：模型、研究框架或解释路径尚未确定时，模型沿第一条容易推进的路线贪心深入，把局部证据缺口、工具路径或小任务当成主目标，过早放弃候选框架池。
95. **evidence_audit_overrouting_gap**：任务本质是模型发现或混合型，但 Complex 流程过早进入 evidence_matrix、资料审计和填表，导致问题定义、候选解释和反例没有被治理。
96. **model_discovery_underprotected_gap**：用户已经说明“研究思路未定、先发散、不要早收敛”，模型仍没有保留 3-5 个候选框架、IBIS 问题-观点-论据图、可区分探针和收敛条件。
97. **mechanical_cadence_overhead_gap**：连续节拍中没有事件触发，却机械重跑完整工具、子代理、Goal 或 prompt 盘点，打断主线并稀释注意力；3 轮兜底被误用成强制全量复盘。
98. **argument_map_missing_gap**：开放式研究、理论建构或价值判断任务只堆材料和证据表，没有先记录 issue / position / pro / con / unresolved question，导致“问题如何被定义”不可复盘。
99. **adaptive_judgment_absent_gap**：项目现场需要动态判断路线、深度、工具、分工或发散/收敛节奏时，模型仍按固定流程执行，没有记录 judgment_mode、decision_right、ask_user_needed 或 recovery_route。
100. **over_asking_user_for_reversible_detail_gap**：用户已授权强自治+护栏，但模型把可逆、低副作用、项目内细节频繁转嫁给用户确认，导致连续推进摩擦上升。
101. **unsafe_autonomy_without_guardrail_gap**：模型把“自主判断”误解成可越过授权边界，对主目标、交付口径、账号/API、外部写入、不可逆文件操作或高风险现实行动自行决策。
102. **route_reflection_missing_gap**：发生战略或关键路线切换后，模型没有记录所选路线、拒绝路线、误判风险、反例和回滚路径，后续恢复者无法判断为什么调路由。
103. **mechanical_deep_judgment_gap**：所有轮次都套用完整深层判断表，未按 fast / diagnostic / exploratory / strategic / critical 分级，导致自适应层反而变成新的流程负担。
104. **rule_density_attention_overload_gap**：协议机制名过密时，模型把注意力放在列举 gate/router/controller 上，而没有先执行 `complex_behavior_kernel` 的 7 个稳定行为。
105. **behavior_regression_missing_gap**：新增或修改协议行为后，没有更新行为回归用例，导致结构验证通过但真实入口触发仍可能漂移。
106. **golden_example_missing_gap**：Runtime Kit 只有空模板或字段说明，没有填好的 evidence_fill / model_discovery 等黄金样例，新项目无法快速模仿低摩擦运行现场。

#### 回归样例 agent_regression_cases

每个被修复的失败，都要形成回归样例。

```yaml
agent_regression_cases:
  - case_id:
    user_prompt_pattern:
    expected_behavior:
    forbidden_behavior:
    required_tools_or_checks:
    micro_task_to_execute:
    actual_execution_evidence:
    observed_result:
    pass_fail:
    remaining_gap:
    pass_condition:
    last_tested:
```

#### 小题实测回归 micro_task_execution_check

回归样例不能只写“期望行为”。每轮自我优化至少实际解决 1 个 5-30 分钟可完成的小任务，留下可检查证据。

```yaml
micro_task_execution_check:
  task:
  input_material:
  action_taken:
  actual_execution_evidence:
  observed_result:
  pass_fail:
  remaining_gap:
  next_regression_trigger:
```

1. 小题必须服务本轮要修复的失败模式，而不是随便做一个容易任务。
2. 小题证据可以是文件扫描结果、真实来源核验、trace 样例、验收链拆解、代码测试、链接抽检、文档渲染状态或人工代理证据。
3. 如果环境或权限导致不能执行，pass_fail 必须写 blocked，remaining_gap 必须写清楚；不能把 blocked 任务标成 resolved。

示例：

```yaml
- case_id: R-feedback-gate-01
  user_prompt_pattern: 用户说“这个版本还是空泛/没有抓手/不是我想要的”
  expected_behavior: 暂停长文，回到问题契约或方向样张闸门，给 2-4 个候选抓手
  forbidden_behavior: 继续在原方向上扩写完整报告
  required_tools_or_checks: update_plan, current_basis update, user_feedback_gate
  pass_condition: 用户能用一句话改变方向
```

#### Agent 评估表 agent_eval_rubric

自我优化轮次必须按以下维度打分：

| 维度 | 高分标准 |
| --- | --- |
| 任务保持 | 始终服务用户最新请求，不被旧任务幽灵带偏 |
| 状态恢复 | handoff 足以让下一轮继续 |
| 证据纪律 | 核心判断能追到 evidence_matrix |
| 工具纪律 | plan/goal、搜索、apply_patch、扫描等工具使用符合规则 |
| 用户摩擦 | 问题少而准，用户能低成本纠偏 |
| 具体性 | 输出能落地到文件、表格、步骤、检查项或行为改变 |
| 幻觉防护 | 修改后扫描，信息不确定时降级 |
| 适应性 | 用户新增隐性标准时能回退阶段，而不是硬凑 |

低于 0.80 的维度必须生成一个 failure_mode 和 regression_case。

#### 工具纪律 tool_discipline

自我优化必须检查以下工具纪律：

1. 多步骤任务是否使用 update_plan，且最多一个 in_progress。
2. 用户未明确要求 create_goal 时，是否没有擅自创建 goal。
3. 需要最新资料、最佳实践、权威引用或当前软件状态时，是否搜索并优先使用官方/一手来源。
4. 文件修改是否使用 apply_patch。
5. 修改后是否执行 post_change_key_node_scan。
6. 如果需要人工操作，是否写成 manual_action_required。
7. 如果已触发工作力度/风险升级，是否维护 evidence_matrix、decision_log、traceability_matrix。

#### 用户摩擦预算

自我优化不能通过频繁询问把负担转嫁给用户。每轮最多提出 1 个高杠杆问题；如果能合理默认，就先推进并在 handoff 中记录 assumption。只有以下情况必须停下：

1. 继续会产生大规模返工。
2. 用户偏好无法从材料推断。
3. 会发生不可逆操作或高成本操作。
4. 需要用户身份、账号、许可、现场材料或人工判断。

#### 协议反膨胀闸门 anti_protocol_bloat_gate

新增规则、trace 或模板前，必须先过反膨胀闸门。

```yaml
anti_protocol_bloat_gate:
  new_rule_or_trace:
  trigger_signal:
  observable_behavior:
  required_evidence_or_check:
  route_back_if_failed:
  user_friction_impact:
  replaces_or_tightens_existing_rule:
  decision: write_to_protocol | merge_with_existing | backlog | reject
```

1. 缺少触发信号、可观察行为、必需证据或检查、失败后的 route-back、用户摩擦影响中的任一项，不得写入总规则或 trace 模板。
2. 每新增一条规则，必须说明它替代、合并或收紧了哪条旧规则；如果只是增加抽象口号，必须拒绝写入或进入 backlog。
3. 如果规则会让用户入口变重，必须同时补 compressed_user_entry 或路由表，保证复杂度由 AI 承担。

### 自我优化输出格式

每轮自我优化至少输出：

1. 本轮要改变的一个核心行为。
2. 一个新增或更新的 failure_mode。
3. 一个新增或更新的 regression_case。
4. 一个写回协议的规则、检查项，或一个明确拒绝/降级写回的 `continuous_optimization_meta_project_profile` 决策。
5. 一次 post_change_key_node_scan。
6. 一个自评分变化说明。

## 9. 自我纠偏

1. 如果开始写最终成品，回到当前阶段边界。
2. 如果开始做 Word、PDF、UI 或展示，检查它是否属于当前最高优先级。
3. 如果开始堆工具，回到阶段缺口。
4. 如果开始写长篇理论，压缩为可执行规则。
5. 如果过度简化，检查是否丢失 intake、state、routing、decision、scorecard。
6. 如果协议变难用，优先压缩用户入口，不删除机器治理规则。
7. 如果用户多次在成品后补充“其实我想要的是……”，说明前置阶段没有充分暴露隐性诉求；应回到 8.6 设置反馈闸门，而不是继续在黑箱里加速产出。
8. 如果项目已触发工作力度/风险升级或兼容记录为 major_project_mode，但没有证据矩阵、决策记录或追踪矩阵，说明只是口头上重大，流程上仍是黑箱；必须回到 8.7 补齐最小治理包。
9. 如果用户要求优化 AI 自己，但输出没有形成 failure_mode、regression_case、eval_rubric 或 tool_discipline 检查，说明仍是口头自省；必须回到 8.8。
10. 如果入口阶段让用户先理解“普通/重大项目、Plan-only、Goal 模式”等模式菜单，说明把内部路由暴露成了用户负担；必须回到快速入口，改成启动提问卡和用户可见触发词。
11. 如果 Complex 任务没有 round_goal、Plan、Loop 或评分路由，说明触发了 optional_goal_plan_loop_gap；必须先补核心循环再执行。
