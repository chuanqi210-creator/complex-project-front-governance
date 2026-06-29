# 第219轮外部 Skill 采用烟测记录 2026-06-23

本轮由用户指出 `mattpocock/skills` 中 34 个 skills 可能对本项目有价值而触发。仓库当前已经存在 `## 219. 当前机器看版` 与 `docs/continuous_optimization_real_project_training_round_219_20260623.md`，因此本记录不追加新的同号机器看版，不改主协议、README 或公开包；它补齐“外部 skill 库发现、试用、采用、拒绝”的项目化证据，并将轻量能力发现节奏写入仓库级 `AGENTS.md` 约定。

## Entry Gate

| item | result |
| --- | --- |
| latest_machine_board | `## 219. 当前机器看版` |
| existing_round_collision | 已存在第219轮真实项目训练记录；本轮作为第219外部 skill 采用辅助记录，不创建新当前入口 |
| valid_trigger | 用户明确要求按建议开展外部 skill 采用计划 |
| baseline_recovery_chain | `append_eof_section.py scan` 通过；综合 verifier `failure_count: 0` |
| selected_main_chain | 外部 skill adoption smoke test |
| proceed_decision | continue_without_new_machine_board |

## capability_discovery_cadence_gate

initial_scan:

| surface | candidates_considered | selected_now | rejected_now | reason |
| --- | --- | --- | --- | --- |
| external_skill_libraries | `mattpocock/skills` | 选用为本轮唯一外部 skill 库候选 | 其他外部库暂不扫描 | 用户点名该库；本轮要验证采用流程，不扩大候选池 |
| installed_skills | 本机 `/Users/chuchenqidawang/.codex/skills` 下 36 个 skill，其中包含上游 34 个 Matt skills | `diagnosing-bugs`, `tdd`, `grill-with-docs` | 全量 34 个一次性采用 | 已安装不等于已项目化采用；先小题验证 |
| callable_tools | `exec_command`, `apply_patch`, `append_eof_section.py`, `verify_governance_recovery.py`, `test_verify_governance_recovery.py` | 选用本地只读探测、写本记录和恢复链验证 | 无 | 本轮需要验证而非外部写入 |
| deferred_tools | `tool_search`, `multi_agent_v1` | 已用于候选发现与只读审计 | 无 | 外部 skill 候选与仓库接入点可并行审计 |
| plugins_connectors | GitHub / browser / Google Drive / automation 等 | 无 | 全部不选 | 不需要外部账号写入、UI 操作或长期自动化 |

periodic_reconsideration:

| trigger | action |
| --- | --- |
| new_user_requirement | 用户明确要求解释为什么没外部寻找 skill，并开展计划行动 |
| blocked_or_failing_verification | 旧工作目录不存在导致 shell 启动失败，进入 `diagnosing-bugs` 小题 |
| stage_transition | 每个 skill 小题结束后判断 `adopt_now | adapt_later | backlog | reject` |
| before_final_claim | 重新运行单测和恢复链 verifier 后才声明完成 |

lightweight_exception: 不全量安装或部署 34 个 skill；当前机器已安装 Matt skill 集，本轮验证的是项目适配、调用纪律和写回边界。

## External Source Record

| item | observed |
| --- | --- |
| source_url | https://github.com/mattpocock/skills |
| upstream_skill_count | 34 个 `skills/**/SKILL.md` |
| upstream_ref | `main` commit `6eeb81b5fcfe`, commit date `2026-06-18T08:41:33Z` |
| upstream_claim | README 将这些 skills 描述为 small、adaptable、composable，并建议 `npx skills@latest add mattpocock/skills` 后运行 `/setup-matt-pocock-skills` |
| local_install_state | 本机已有 36 个 `~/.codex/skills/*/SKILL.md`，包含上游 34 个 Matt skills 及本地扩展 |
| project_adoption_state | 仓库此前已有 capability / skill plugin gate，但没有独立记录“外部 skill 库 smoke test -> 项目采用/拒绝”的流程证据 |

## Smoke Test A: diagnosing-bugs

| field | value |
| --- | --- |
| source_url | https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md |
| skill_version_or_ref | local installed skill; upstream ref `6eeb81b5fcfe` |
| micro_task | 诊断为什么连续 `exec_command` 失败，避免把 cwd 迁移误判为 shell / tool 故障 |
| concrete_artifact_or_record_ref | 旧路径 `/Users/chuchenqidawang/Documents/日常/01_项目_Projects/complex-project-front-governance`；当前路径 `/Users/chuchenqidawang/Documents/complex-project-front-governance` |
| observed_benefit | 通过最小反馈环确认旧路径不存在、新路径存在且有 `.git`，将问题从“工具坏了”降级为“工作目录已迁移” |
| friction | 低；只需 2 条只读命令 |
| risk | 若机械套用完整六阶段，会把简单环境定位拉长 |
| decision | adopt_now |
| promotion_condition | 在 verifier 红灯、shell/路径/恢复链异常、测试失败时使用；不作为每个普通文档编辑的强制前置 |

diagnosis_loop_result:

```text
old_path_exists: False
new_path_exists: True
new_has_git: True
```

采用边界：`diagnosing-bugs` 的核心价值是先构造反馈环，再提出原因；本轮实际避免了一次“工具不可用”的错误结论。

## Smoke Test B: tdd

| field | value |
| --- | --- |
| source_url | https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md |
| skill_version_or_ref | local installed skill; upstream ref `6eeb81b5fcfe` |
| micro_task | 用临时目录构造缺少 `capability_discovery_cadence_gate` 的恢复链夹具，确认 verifier 能红 |
| concrete_artifact_or_record_ref | 临时拷贝的 protocol / route / release / changelog / long_log；未改仓库文件 |
| observed_benefit | 第一次替换为 `capability_discovery_cadence_gate_REMOVED` 仍被子串匹配误判通过；第二次替换为 `CAPABILITY_FIELD_ABSENT` 后 verifier 正确失败 |
| friction | 中低；需要临时夹具和一次红灯校准 |
| risk | 若把所有协议文档变化都强制 TDD，会制造维护负担；适合 verifier 字段、脚本和恢复链规则变化 |
| decision | adopt_now |
| promotion_condition | 进入 verifier required、脚本行为或恢复链约束前，先做最小红灯；纯叙述性经验库记录不强制 |

red_capable_loop_result:

```text
returncode: 1
failure_count: 5
failed_checks_sample:
- protocol_contains:capability_discovery_cadence_gate
- route_contains:capability_discovery_cadence_gate
- release_contains:capability_discovery_cadence_gate
- changelog_contains:capability_discovery_cadence_gate
- long_log_contains:capability_discovery_cadence_gate
```

采用边界：TDD skill 不只是“多写测试”，而是要求测试通过公共接口验证行为。本轮的公共接口是 `verify_governance_recovery.py --preset continuous-self-optimization`。

## Smoke Test C: grill-with-docs

| field | value |
| --- | --- |
| source_url | https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md |
| skill_version_or_ref | local installed skill; upstream ref `6eeb81b5fcfe` |
| micro_task | 检查“是否应把外部 skill 采用流程写进主协议或 verifier required”这一复杂治理问题能否被问清，同时避免文档膨胀 |
| concrete_artifact_or_record_ref | 本记录的 Entry Gate、External Source Record、三项 smoke test、Promotion Review |
| observed_benefit | 它强迫区分“外部 skill 已安装”“本项目已采用”“是否应进入主协议/AGENTS/verifier”三种状态 |
| friction | 中；完整 grilling 会打断已批准的执行计划，并可能默认生成 `CONTEXT.md` / ADR |
| risk | 若每轮连续优化都互动式 grilling，会增加用户摩擦；若自动写领域文档，会让轻量记录膨胀 |
| decision | adapt_later |
| promotion_condition | 用于新协议概念、术语冲突、硬规则晋升或跨角色误解明显时；本轮只记录关键问题与默认答案，不创建 `CONTEXT.md` 或 ADR |

dry_run_question:

```text
Q: 这次真实缺口是“缺少外部 skill”，还是“缺少外部 skill 采用证据链”？
Recommended answer: 后者。当前机器已安装 Matt skills；真正缺口是没有把外部 skill 库发现、小题验证、采用/拒绝和晋升条件写成项目记录。
```

采用边界：`grill-with-docs` 适合在协议概念尚未清晰时使用；本轮计划已足够明确，因此不进行完整用户访谈，不创建额外文档体系。

## Promotion Review

| candidate | decision | reason |
| --- | --- | --- |
| `diagnosing-bugs` for tool/verifier/recovery failures | adopt_now | 本轮实际减少误判，把旧 cwd 问题快速定位 |
| `tdd` for verifier/script changes | adopt_now | 本轮证明最小红灯能发现夹具子串陷阱 |
| `grill-with-docs` for ambiguous governance concepts | adapt_later | 有助于问清概念，但完整流程有用户摩擦和文档膨胀风险 |
| 全量部署 34 个 Matt skills 到项目流程 | reject | 本机已安装，不代表每个项目都应采用；全量采用会稀释选择证据 |
| 新增主协议硬字段 | reject | 本轮只证明采用流程需要显性记录，没有两个以上真实项目暴露同一新失败模式 |
| 新增 verifier required 字段 | reject | 外部 skill adoption 本身不适合用稳定字符串检查；先保留为训练记录 |
| `AGENTS.md` 轻量能力发现默认规则 | adopt_now | 用户明确要求以后无需主动提供 skill，也能在关键阶段自行搜寻相关 skill / tool / plugin / API / 外部方法 |
| 新增 `docs/agents/skill_usage.md` | backlog | 等 1-2 次后续真实任务再次证明该流程降低误判、摩擦或恢复链风险后再写稳定规则 |

## Answer To The Triggering Concern

为什么之前没有充分注意外部寻找、验证和部署这些 skill：

1. 项目独立化初期重心在恢复链、协议字段、发布包和开源适配，刻意避免把外部依赖当作主动依赖。
2. `capability_discovery_cadence_gate` 已要求考虑 local skills / tools / plugins / APIs，但示例扫描面没有把 `external_skill_libraries` 和 `installed_skills` 单独命名，导致“外部库 -> 小题验证 -> 采用/拒绝”的证据链不够显性。
3. 本机事实上已经安装 Matt skills；真正缺口不是下载部署，而是没有把它们在本项目中的项目适配、调用边界和晋升条件写成记录。

改进方式：后续凡是用户点名外部 skill 库、任务目标是提升 agent/tool/subagent 能力，或出现工具层误判时，先做轻量外部 skill adoption smoke；每轮最多 3 个候选，不全量采用。

## Exit Gate

| item | result |
| --- | --- |
| files_synced | `docs/continuous_optimization_external_skill_adoption_round_219_20260623.md` |
| machine_board_change | none |
| protocol_hard_field_change | none |
| verifier_required_change | none |
| AGENTS_or_README_change | `AGENTS.md` and `protocol/AGENTS.md` gained lightweight capability discovery defaults; README unchanged |
| next_round_decision | stop |
| may_start_next_round | false |
| verification_status | local_regression_test_green_and_recovery_scan_failure_count_0 |

next_route: keep_existing `continue_self_optimization_training_round_219_or_stop`
