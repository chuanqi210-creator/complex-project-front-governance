# 复杂项目启动前置治理协议 v2.0

Auto-Research 增强版：把提示词链升级为可恢复、可路由、可执行的前置治理系统。

## v2.0 核心改进

- 增加 material intake：登记材料路径、类型、角色、权威性和 current_basis。
- 增加 state recovery：后续 AI 先读当前状态，不重读所有历史。
- 增加 question contract：区分世界问题、经验规格、操作问题、操作定义和范围边界。
- 增加 decisions：记录关闭、回退、阻塞、范围变化和用户决策。
- 增加 closure routing：用未关闭的不确定性决定下一阶段，不从材料直接跳到成品。

## 阶段列表

### 阶段 0：总控启动

- 阶段目的：建立 AI 的工作姿态、阶段边界和文件化继承规则。
- 输入：用户的零散想法、文件路径、截图、目标、限制、已有仓库或已有成果。
- 判断门：AI 是否明确承诺先治理后执行，并知道要先建立材料和状态入口。
- 机器看版最低字段：project_trigger、known_materials、initial_constraints、stage_order、handoff_rule。

```text
现在进入阶段 0：总控启动。

阶段目的：建立 AI 的工作姿态、阶段边界和文件化继承规则。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

你现在扮演“项目前置治理架构师”，不是执行者。

我会给你一个新项目的零散想法、材料、目标或问题。请你先不要写成品、不要写代码、不要做展示、不要急着进入实现。

你的任务是按阶段完成前置治理：材料接收、情景识别、高质量发散、外部 skill/工具/方法搜索、主链收束、Goal 设定、Plan 设计、评分体系、最小闭环、执行前闸门、执行启动。

请先确认工作方式，并告诉我你将如何建立材料登记、状态恢复、阶段路由和人/机器双输出。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 1：项目情景识别与材料 Intake

- 阶段目的：判断项目类型，同时登记材料、角色、权威性和当前依据，防止旧稿或生成物污染判断。
- 输入：原始想法、材料清单、文件路径、仓库、论文、数据、代码、草稿、截图、用户目标。
- 判断门：是否形成 current_basis；若材料权威性不清，必须停在 intake-open。
- 机器看版最低字段：intake_registry、material_authority、current_basis、not_current_basis、project_type、uncertainty。

```text
现在进入阶段 1：项目情景识别与材料 Intake。

阶段目的：判断项目类型，同时登记材料、角色、权威性和当前依据。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请基于我给出的材料，先做材料 intake，再做项目情景识别。

材料 intake 请输出：
1. 每个材料的来源或路径；
2. 材料类型：paper / dataset / draft / notes / code / output / other；
3. 材料角色：authoritative input / background / draft / generated output / candidate / historical；
4. 权威性：authoritative / provisional / superseded / uncertain；
5. 能支持的阶段：intake / novelty / feasibility / execution / manuscript；
6. 是否允许进入 current_basis。

情景识别请判断：
1. 主类型和副类型；
2. 当前最大不确定性；
3. 现在最不该急着做什么；
4. 前置阶段必须完成哪些工作；
5. 本项目更适合怎样的对话流程；
6. 我没说清楚但可能关键的隐含需求。

本阶段不要写方案、不要定 Goal、不要定 Plan。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 2：高质量发散

- 阶段目的：开放生成高潜力方向，但每个方向都绑定依据、资源、风险和可验证性。
- 输入：阶段 1 的项目类型、current_basis、open_questions、材料权威性。
- 判断门：候选方向是否足够多样，且没有把未检查材料当作事实。
- 机器看版最低字段：candidate_routes、basis_used、risks、evidence_gap、backlog_seed。

```text
现在进入阶段 2：高质量发散。

阶段目的：开放生成高潜力方向，但每个方向都绑定依据、资源、风险和可验证性。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请基于阶段 1 的 handoff 和 current_basis 发散可能方向。要求不是穷举，而是找到高潜力方向。

每个方向请说明：
1. 核心问题；
2. 为什么值得做；
3. 可能创新点或价值点；
4. 资源需求；
5. 最大风险；
6. 适合的交付形式；
7. 与我的原始意图有什么关系；
8. 哪些依据来自材料，哪些是你的推断；
9. 需要后续搜索或验证的关键缺口。

本阶段不要收束成唯一方案，不要写 Goal，不要写执行 Plan。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 3：Skill / 工具 / 外部方法搜索

- 阶段目的：让 AI 主动寻找可用能力，但搜索必须服务阶段缺口，不做无边界工具堆叠。
- 输入：候选方向、证据缺口、能力缺口、当前环境可用 skill/plugin/MCP/GitHub/论文工具。
- 判断门：工具矩阵是否说明用途、阶段、风险、是否安装或仅借鉴。
- 机器看版最低字段：skill_matrix、search_purpose、selected_tools、tool_risks、calling_order。

```text
现在进入阶段 3：Skill / 工具 / 外部方法搜索。

阶段目的：让 AI 主动寻找可用能力，但搜索必须服务阶段缺口。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请根据阶段 1-2 的结果，判断本项目需要哪些外部能力，包括但不限于：文献综述、知识图谱、代码图谱、模型验证、不确定性评估、专利检索、产品发现、用户研究、数据分析、仿真建模、写作结构化、可视化、测试自动化。

请执行：
1. 先列出需要搜索的 skill/工具/方法类别，以及对应的阶段缺口；
2. 如果当前环境有 skill/plugin/MCP，请先检查可用项；
3. 如果需要 GitHub、网页或论文搜索，请先说明搜索目的，再搜索高匹配、维护活跃、说明清楚的项目或方法；
4. 每个候选项说明用途、适合阶段、是否安装、是否只借鉴、风险；
5. 不要盲装，除非它对前置质量有明显提升；
6. 最后给出推荐组合和调用顺序。

搜索是支持活动，不是独立阶段；不要让工具选择替代项目主链。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 4：主链收束与阶段路由

- 阶段目的：把发散方向压成一个可执行主链，并决定下一步属于哪个阶段门。
- 输入：候选方向、工具矩阵、材料 current_basis、开放问题、用户意图。
- 判断门：是否得到稳定主链句；backlog 是否说明保留原因；next_route 是否明确。
- 机器看版最低字段：mainline_sentence、kept_scope、backlog、boundaries、next_route、route_reason。

```text
现在进入阶段 4：主链收束与阶段路由。

阶段目的：把发散方向压成一个可执行主链，并决定下一步属于哪个阶段门。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请基于前面发散和 skill/工具搜索结果，收束项目主链。

要求：
1. 用一句话说明项目真正解决什么问题；
2. 这句话包含对象、约束、核心矛盾、解决机制、验证方式；
3. 给出通俗版、专业版、可放入 Goal 的版本；
4. 明确哪些想法保留，哪些进入 backlog；
5. backlog 的原因不是“不重要”，而是暂时不属于当前主链；
6. 指出我可能还没表达出来但应进入主链的关键点；
7. 判断下一步应进入 intake-open、novelty-iteration、feasibility-closure、research-execution、manuscript-realization、blocked 或 user-decision-needed。

本阶段不要写完整 Goal，也不要写执行 Plan。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 5：Goal 模式文本

- 阶段目的：把主链升级为长期使命、第一性原理、边界和不变量，而不是任务清单。
- 输入：主链句、边界、backlog、阶段路由、证据等级、用户长期意图。
- 判断门：Goal 是否能长期约束项目；是否自然语言可读，且包含可验证边界。
- 机器看版最低字段：goal_text、first_principles、invariants、boundaries、evidence_levels、stage_gates。

```text
现在进入阶段 5：Goal 模式文本。

阶段目的：把主链升级为长期使命、第一性原理、边界和不变量。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请基于阶段 4 的主链，为这个项目生成可复制进 Goal 模式的自然语言文本。Goal 不是任务清单，而是长期使命和第一性原理。

请包含：
1. 系统使命；
2. 第一性原理；
3. 核心主链；
4. 不变量；
5. 边界；
6. 证据等级；
7. 评价维度；
8. 阶段门；
9. 终止条件；
10. 自我纠偏规则；
11. 人看产物与机器看产物的要求；
12. 允许 AI 在理解我意图基础上拓展，但不能偏离主链。

请根据项目类型动态改写，不要套工程模板。科研、产品、写作、学习、商业、专利等场景都应有不同强调。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 6：Plan 模式

- 阶段目的：把长期 Goal 转为当前阶段的 5-8 个任务，并明确验收、依赖、停止条件。
- 输入：Goal 文本、当前阶段、next_route、current_basis、可用 skill、评分维度。
- 判断门：Plan 是否只管当前阶段；每个任务是否可验收；是否说明现在不做什么。
- 机器看版最低字段：task_list、priority、dependencies、acceptance_gates、stop_conditions、backlog_updates。

```text
现在进入阶段 6：Plan 模式。

阶段目的：把长期 Goal 转为当前阶段的任务、顺序和验收。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请基于 Goal，设计当前阶段 Plan。注意：Plan 只管当前阶段，不替代 Goal。

请先判断当前阶段属于：探索期、架构期、原型期、验证期、扩展期、收束期，或 auto-research 的 intake-open / novelty-iteration / feasibility-closure / research-execution / manuscript-realization。

然后输出 5-8 个任务，每个任务包括：
1. 为什么做；
2. 输入；
3. 输出；
4. 验收标准；
5. 依赖；
6. 风险；
7. 停止条件；
8. 与 Goal 的关系；
9. 人看产物；
10. 机器看产物；
11. 需要调用的 skill/工具。

请明确哪些事现在不做，哪些进入 backlog。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 7：评分体系与终止条件

- 阶段目的：用评分服务决策：继续、暂停、收束、等待资源或回退，而不是制造虚假成熟感。
- 输入：Goal、Plan、阶段门、证据等级、材料权威性、项目类型。
- 判断门：每个指标是否有 0-1 定义、权重、阈值、证据等级和终止条件。
- 机器看版最低字段：scorecard、weights、thresholds、evidence_levels、continue_pause_close_rules。

```text
现在进入阶段 7：评分体系与终止条件。

阶段目的：用评分服务决策，而不是制造虚假成熟感。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请为本项目设计可计算、可复盘的成熟度评分。指标应根据项目类型动态生成，包括但不限于：问题清晰度、架构完整度、证据强度、可验证性、可执行性、创新性、工程化成熟度、可复用性、风险可控性、表达成熟度。

要求：
1. 每个指标给 0-1 分定义；
2. 给权重；
3. 给阶段门；
4. 给继续/暂停/收束/等待外部资源/回到上一阶段的条件；
5. 区分 idea、synthetic、literature、field、human-reviewed 等证据；
6. 明确分数是为决策服务，不是为了制造虚假成熟感；
7. 如果当前材料不足以评分，请标记 missing evidence，而不是猜分。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 8：最小闭环

- 阶段目的：设计第一轮最低成本验证路径，只证明主链中最关键的不确定性。
- 输入：Goal、Plan、评分表、current_basis、next_route、资源约束。
- 判断门：闭环是否足够小；是否说明能证明什么、不能证明什么。
- 机器看版最低字段：loop_modules、interfaces、validation_table、failure_boundary、backlog_updates。

```text
现在进入阶段 8：最小闭环。

阶段目的：设计第一轮最低成本验证路径，只证明主链中最关键的不确定性。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请基于 Goal、Plan 和评分体系，设计第一轮最小闭环。

要求：
1. 只保留能验证主链的最小路径；
2. 不追求完整，不追求好看，不追求一次做完；
3. 每个模块说明输入、输出、验证方式、失败边界；
4. 明确人看产物和机器看产物；
5. 明确哪些内容进入 backlog；
6. 说明完成后能证明什么、不能证明什么；
7. 给出第一轮执行顺序；
8. 如果是科研项目，区分“方案可行性闭环”和“真实结果闭环”，不要把设计稿当结果。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 9：执行前闸门

- 阶段目的：最后检查 Goal、Plan、材料、评分、路由和最小闭环是否足以支撑执行。
- 输入：全部 handoff、Goal、Plan、评分表、最小闭环、材料 registry、closure-routing。
- 判断门：通过则输出“可以进入执行”；不通过必须指出回到哪个阶段。
- 机器看版最低字段：gate_result、risk_register、route_back_stage、required_fix、execution_ready_basis。

```text
现在进入阶段 9：执行前闸门。

阶段目的：最后检查是否可以进入执行。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

请检查：
1. Goal 是否清楚；
2. Plan 是否服务 Goal；
3. 当前任务是否最高边际价值；
4. 是否提前做了下一阶段的事；
5. 是否存在过早展示、过早工程化、过早复杂化、过早堆模块等风险；
6. 是否已定义人看产物和机器看产物；
7. 是否已定义评分和停止条件；
8. 是否需要先调用某个 skill/工具；
9. 材料 current_basis 是否清楚，旧稿、候选材料、生成输出是否被正确隔离；
10. 如果现在执行，最大返工风险是什么；
11. 你在理解我意图后，还有什么必须提醒我的地方。

如果通过，请输出：可以进入执行。
如果不通过，请说明应该回到哪个阶段修正。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```

### 阶段 10：执行启动

- 阶段目的：进入执行，但每轮仍受 Goal、Plan、评分和阶段路由约束。
- 输入：通过闸门的 Goal、Plan、最小闭环、current_basis、task priority。
- 判断门：每轮是否只推进一个最高优先级任务，并更新状态。
- 机器看版最低字段：current_status、manifest、changed_files、score_update、decisions_update、next_action。

```text
现在进入阶段 10：执行启动。

阶段目的：进入执行，但每轮仍受 Goal、Plan、评分和阶段路由约束。

请先读取上一阶段的机器看版 handoff；如果已有项目文件，请优先读取 state.md、intake.md、question.md、decisions.md、closure-routing.md。不要把历史草稿、未检查材料、生成输出自动当成当前依据。

请按本阶段边界工作，只输出本阶段需要的判断和 handoff。允许你在理解我真实意图的基础上主动补足隐含需求，但必须说明哪些是原始材料支持，哪些是你的推断，哪些需要我确认。

现在开始执行当前 Plan。

执行规则：
1. 每次只推进一个最高优先级任务；
2. 执行前说明它服务 Goal 的哪一部分；
3. 执行中如发现偏离主链，主动暂停并说明；
4. 新想法先进入 backlog，不打断当前闭环，除非它暴露硬性方向错误；
5. 每轮结束更新人看版总结和机器看版状态；
6. 机器看版必须可被后续 AI 继续读取，包括 current_status、manifest、评分表、接口表、验证表、必要时的 CodeGraph；
7. 不把 synthetic/sample/template 当作真实结论；
8. 不为了产物数量牺牲主链清晰度；
9. 阶段关闭、回退、阻塞或用户决策，必须写入 decisions；
10. 如果当前 basis 变化，必须更新 state。

输出必须包含：
1. 人看版：解释判断、取舍、风险和下一步；
2. 机器看版 handoff：用稳定结构保存 current_stage、current_basis、open_questions、decisions、next_route、backlog；
3. 如当前阶段不能关闭，明确 route-back、blocked 或 user-decision-needed 的原因。
```
