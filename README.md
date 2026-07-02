# complex-project-continuous-governance

这是从 `/Users/chuchenqidawang/Documents/ai 科研` 拆出并独立化后的 **Complex 项目持续治理协议** 项目。本仓库现在是当前权威工作区，旧 `ai 科研` 目录只作为历史来源。

本项目名称从 “front governance / 启动前置治理” 调整为 “continuous governance / 持续治理”，因为协议已经不只覆盖复杂项目启动前的目标和证据对齐，也覆盖持续推进中的动态路由、Loop 小闭环、评分迭代、协作拓扑、恢复链和交付边界。

## 当前版本状态

- 当前主协议：`protocol/Complex项目持续治理协议_v3_核心版.md`
- 当前低摩擦入口：`protocol/Complex项目持续治理_低摩擦用户入口_20260622.md`
- 当前恢复入口：`protocol/持续治理协议_二十个跨渠道项目逆向校验实验.md` 的 `## 224. 当前机器看版`
- 当前 next route：`continue_self_optimization_with_behavior_transcript_review_real_project_pressure_or_stop`
- 最近一次整合：仓库独立化、历史回归迁移、恢复链第 215-224 轮、外部 skill 采用扩展、新能源汽车项目复盘后的人看版交付/注意力绑定规则、Runtime Kit 运行模板、提示词前置与每轮重水化、每拍窄 Goal 生命周期、模型发现与反早收敛、自适应判断、行为内核、反人工/上下文漂移约束、独立评审黄金样例、transcript 审查和真实样本结果记录格式。
- 当前重构方向：用 `complex_behavior_kernel` 把厚协议压缩成 7 个稳定行为，并用行为回归包和黄金样例验证新项目能落地，而不是继续堆规则名。
- GitHub 同步策略：本仓库保留当前权威协议和 Runtime Kit；公开说明、可视化站点、模板和 reusable protocol package 均从该工作区同步。

## 项目目标

- 把复杂项目的项目性质判断、目标对齐、问题框架发现、证据分层、能力发现、自适应深层判断、动态路由、Loop 小闭环、评分迭代、协作拓扑、恢复链和交付边界放在一个小而清楚的项目里。
- 让 Codex 可以围绕该协议单独开工作树、持续迭代、测试和发布。
- 提供 Complex Runtime Kit / 持续治理运行时套件，让新项目能直接建立状态、证据、决策、检索、提问、提示词、framing、argument、judgment、Loop 和交付记录。
- 避免继续依赖或修改 `ai 科研` 大目录。

## 三层结构

1. `protocol/`：Complex 持续治理核心规则，决定项目如何恢复、路由、评分、协作和交付。
2. `templates/`：Runtime Kit 运行模板，帮助新项目快速建立 state、evidence、decision、search、question、prompt、framing、argument、judgment、loop 和 delivery 记录。
3. `.codex/`：项目级能力发现入口，记录推荐能力候选和项目本地 skill 放置规则；它不替代实际环境中的工具探测。

## 目录

- `.codex/shared-skills.json`：项目级能力候选清单，用于启动能力盘点，不声称所有能力当前可调用。
- `.codex/skills/`：项目本地 skill 放置区；当前仅保留说明，未来新增 skill 必须绑定真实项目缺口和小题验证。
- `protocol/`：协议核心文档、v3 主协议、低摩擦入口、发布包、自测记录、经验库索引。
- `protocol/Complex项目持续治理协议_v3_核心版.md`：当前权威主协议。
- `templates/`：Runtime Kit 轻量模板，供新项目复制或引用。
- `templates/framing.md`：问题域、候选框架、发散预算、可区分探针和收敛条件。
- `templates/argument.md`：问题-观点-论据图，用于开放式研究和模型发现。
- `templates/judgment.md`：自适应判断记录，用于路线、深度、工具、协作、回问和回滚边界。
- `templates/prompt.md`：提示词设计前置模板，用于先扫描 Complex、设计项目专用执行 prompt、确认后再推进。
- `docs/runtime-skill-management.md`：运行时 skill / tool / plugin / API / 外部方法选择、拒绝、试用和写回规则。
- `docs/complex_mechanism_layering_20260702.md`：机制分层说明，帮助新代理区分行为内核、路由器、触发门、模板、历史和验证器。
- `docs/behavior_regression_cases_20260702.json`：11 个高风险入口行为回归用例。
- `docs/behavior_transcript_review_rules_20260702.json`：11 个行为案例的 transcript 审查规则，记录必需行为标记、禁忌标记和人工复核问题。
- `docs/behavior_transcript_review_guide_20260702.md`：行为回归从结构检查到真实对话 transcript 审查的使用说明。
- `docs/behavior_review_result_template_20260702.md`：真实回复审查结果记录格式，用于累计 8-12 条 transcript 样本。
- `docs/real_project_pressure_test_result_template_20260702.md`：端到端真实项目压力测试结果格式，用于 evidence_fill / model_discovery 样本。
- `docs/complex_new_agent_5_minute_quickstart_20260702.md`：新代理 5 分钟上手版，只保留恢复入口、7 步行为内核、项目性质和最小 Runtime Kit。
- `docs/examples/`：三个填好的 Runtime Kit 黄金样例，覆盖 evidence_fill、model_discovery 和 independent_review。
- `tools/check_behavior_regression_pack.py`：行为回归包结构检查。
- `tools/review_behavior_transcript.py`：针对真实 agent 回复或导出对话的行为 transcript 审查器。
- `docs/history/`：从旧目录同步来的历史回归记录、真实项目小题和治理样例。
- `docs/migration/`：独立化迁移清单和路径说明。
- `docs/Complex协议复盘与优化人看版_20260629.md`：新能源汽车项目作为例子的 Complex 协议人看版复盘。
- `docs/protocol_explainer_site/`：协议解释站点源码。
- `outputs/front_governance_protocol_v2/`：v2 版本 Markdown、DOCX、PDF 和渲染页。
- `tools/`：恢复链、链接扫描等辅助工具。
- `docs/`：后续新增说明和设计笔记。

## 使用说明

### 推荐最贴合入口

新项目最贴合的用法，是先让 Complex 扫描协议、理解项目性质，再设计项目专用提示词并确认执行：

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。
```

AI 应先触发 `complex_prompt_bootstrap_gate`，完成协议扫描、启动问题或安全默认、项目专用 `copy_ready_prompt` 和 `execution_bridge`。用户确认前不应进入业务执行、发布、提交外部系统或把 prompt 当成已授权操作。

新代理扫描 Complex 时，先抓 7 个行为内核，再读机制名：

1. 恢复真实状态。
2. 判断项目性质和收敛状态。
3. 划清 AI 自治与用户授权边界，并先判断人工介入是否真的必要。
4. 选择一个最高杠杆问题。
5. 用最轻有效动作验证或执行。
6. 按交付对象输出。
7. 留下 next_route 和恢复线索。

`## 224. 当前机器看版` 是恢复链的最新状态锚点；`complex_behavior_kernel` 是执行层的第一行为锚点。新代理恢复时先确认 224 的 current state 和 next_route，再用 7 步行为内核压缩本轮行动，而不是从第 220 轮 skill 同步记录或长 gate 名单开始。

如果是第一次接手 Complex，先读 `docs/complex_new_agent_5_minute_quickstart_20260702.md`，再按任务类型选择黄金样例或 Runtime Kit 模板。

如果你的任务不是“按既定模型填证据”，而是研究框架、解释路径、指标模型或故事主线还没定，可以直接加一句：

```text
这是模型发现型任务，先不要证据填表。请先发散研究框架，建立候选解释路径和问题-观点-论据图，再判断何时收敛。
```

如果你希望 AI 自己处理可逆、低副作用、项目内的路线细节，可以加一句：

```text
采用强自治+护栏：让 AI 自行判断细节、动态推进，只在高风险、授权、不可逆动作、主目标或交付公开口径变化时问我；AI 自己调路线，但保留理由。
```

### 直接推进入口

如果已经知道项目目标，也可以直接说：

```text
这个项目按 Complex 推进。
目标是：……
已有材料在：……
我希望结果达到：……
```

AI 应先用 `complex_setup_question_card` 确认或默认交付对象、外部能力权限、子代理/多线程、连续节拍、自治边界和人工边界。用户不需要区分普通项目和重大项目；高风险、高返工或高公共性的工作只会触发内部工作力度/风险升级。

AI 还应先判断 `project_nature`：证据填充型、模型发现型、混合型，还是执行交付型。模型、公式、指标或研究框架未定时，不应直接进入证据填表。

AI 还应启用 `adaptive_judgment_controller`：默认采用“强自治+护栏”，自行处理计划细节、Loop 探针、证据深度、工具取舍、临时分工、长期线程职责微调和发散/收敛节奏；只有主目标改变、账号/API/付款/发布/外部写入、不可逆动作、交付公开口径变化或证据不足却要对外强主张时，才回问用户。

同时启用 `human_intervention_drift_guard`：人工介入默认是成本和潜在漂移源。若 `next_route`、`round_goal`、state 或用户给出的材料位置已经指向明确、低风险、可逆的下一步，AI 应继续推进并记录理由，不应停在“是否继续”；若用户给出目录、文件或链接，AI 应优先自行读取和归纳，只有权限、隐私、账号、外部写入或现实责任边界才要求人工操作。

### 可选触发词

新用户不需要猜隐藏口令。可以直接说：

- `完整扫描 Complex`：先做协议理解，再给业务计划。
- `先设计提示词/prompt`：先生成项目专用执行 prompt，确认后再推进。
- `模型发现型 / 先发散研究框架 / 不要早收敛 / 先做问题-观点-论据图`：先保护候选框架、反例和可区分探针，再判断何时转入证据填充。
- `强自治+护栏 / 让 AI 自行判断细节 / 动态推进 / 只在高风险时问我 / AI 自己调路线，但保留理由`：AI 自行选择路线、深度、工具、分工和发散/收敛节奏，并在战略或关键判断时留下选择理由、误判风险和回滚路线。
- `少问我 / 能推进就继续 / 已知 next_route 就继续 / 我给目录你自己读`：先判断人工介入是否必要；低风险可逆且材料可读时，AI 自动推进并记录理由。
- `独立评审 / 客观审查 / 避免上下文污染`：同一 session 自评只能算 diagnostic；真正独立评审需要清上下文、新线程、只读审计子代理或事实账本输入。
- `连续节拍`：每轮先重构 `round_execution_prompt`，再生成 Plan、Loop、评分路由和 `next_route`；Codex 工具 Goal 默认每拍一个窄目标。工具、子代理/线程职责、goal 和 master prompt 采用事件触发优先的复查，3 轮只是兜底上限。
- `多线程/子代理`：先判断主线程、临时子代理或长期线程哪种拓扑合适，再执行。
- `外部工具/账号/API`：先建立能力候选清单，写清 selected / rejected / backlog / manual action。
- `只要人看版`：交付以第三方也能读懂的人看版为主，机器恢复记录另行保留或压缩。

### Runtime Kit 落地方式

需要让新项目可恢复时，复制或引用 `templates/` 中的轻量模板：

- `state.md`：当前状态、用户选择、goal、拓扑和能力刷新。
- `evidence.md`：证据层级、缺口和可声明边界。
- `decision.md`：关键取舍、拒绝路线和重评条件。
- `search.md`：资料检索、获取升级、账号/权限/用户协助边界。
- `question.md`：启动提问卡和高杠杆确认问题。
- `prompt.md`：先扫描 Complex、设计项目 prompt、确认后执行。
- `framing.md`：模型发现型任务的问题域、候选框架和收敛条件。
- `argument.md`：IBIS 风格的问题-观点-论据图。
- `judgment.md`：自适应判断、自治边界、回问条件、误判风险和回滚路线。
- `loop.md`：5-30 分钟小循环、评分和 route-back/execute 判断。
- `delivery.md`：人看版、机器恢复版、老师/专家/第三方版本的交付契约。

如果不知道怎么填，先看三个黄金样例：

- `docs/examples/evidence_fill_minimal_runtime/`：模型和指标已定，只补证据、验证和交付边界。
- `docs/examples/model_discovery_minimal_runtime/`：研究框架未定，先保留候选框架、论据图和可区分探针。
- `docs/examples/independent_review_minimal_runtime/`：需要客观审查时，用事实账本和清上下文评审区分同 session diagnostic 与真正 independent review。

### 连续节拍中的每轮 prompt

第一轮 `copy_ready_prompt` 是总规划，后续每轮不应把它降级成一句背景原则。连续项目每轮开始时，AI 应先触发 `round_prompt_rehydration_gate`：从总 prompt / active_goal_summary、最新状态和本轮最高杠杆问题压缩出 `round_execution_prompt`，再基于它生成 Plan 和 Loop。

本轮 Plan 应明确三件事：哪些继承自总规划，哪些来自上一轮状态，哪些是本轮新增判断。用户补充局部细节时，默认作为 prompt patch 写入本轮执行 prompt，不自动改写总目标。

### 连续节拍中的 Goal

连续项目不要把几十轮推进塞进一个长期 Codex 工具 Goal。Complex 的默认做法是：长期方向写在 state、master prompt、closure routing 和 `next_route` 里；Codex 工具 Goal 只承接当前拍的窄 `round_goal`，完成这一拍就关闭，下一拍再从 `next_route` 生成新的窄目标。

如果工具 Goal 已经 blocked 或停在旧版本，但项目材料和状态说明仍可继续，不能把项目本身判成 blocked。先记录 `goal_migration_note` 或 `protocol_round_goal`，继续按当前 state 推进；只有真实项目条件连续阻塞，才进入 blocked 路由。

### 维护者工作流

1. 改协议前先看 `protocol/持续治理协议发布包_20260622.md`。
2. 涉及历史恢复链时看 `protocol/持续优化变更清单_20260622.md`。
3. 新项目要求读取 Complex 或 Auto Research 时，先理解低摩擦入口、启动提问卡、阶段流程、动态路由、能力发现、子代理/线程、Goal/Plan/Loop、评分和交付拆分规则，再开始业务执行。
4. 修改后运行工具或结构检查，记录结果。
5. 需要并行探索时，从本项目创建 worktree，而不是从原 `ai 科研` 大目录创建。

## 验证命令

协议或恢复链修改后，优先运行：

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/test_verify_governance_recovery.py
python3 tools/verify_governance_recovery.py --preset continuous-self-optimization --latest-heading '## 224. 当前机器看版' --expected-route continue_self_optimization_with_behavior_transcript_review_real_project_pressure_or_stop
```

当前基线要求上述命令分别返回行为包 `ok`、transcript rules `passed: true`、治理测试 `ok` 和恢复验证 `failure_count: 0`。

真实行为样本的记录格式：

- 单条 agent 回复审查：`docs/behavior_review_result_template_20260702.md`
- 端到端真实项目压力测试：`docs/real_project_pressure_test_result_template_20260702.md`

## 来源

本项目源自 `/Users/chuchenqidawang/Documents/ai 科研`，相关历史记录已同步到 `docs/history/`。后续协议维护、验证和恢复默认只使用本仓库。
