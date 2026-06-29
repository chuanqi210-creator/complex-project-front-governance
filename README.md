# complex-project-front-governance

这是从 `/Users/chuchenqidawang/Documents/ai 科研` 拆出并独立化后的“复杂项目启动前置治理协议”项目。本仓库现在是当前权威工作区，旧 `ai 科研` 目录只作为历史来源。

## 当前版本状态

- 当前主协议：`protocol/复杂项目启动前置治理协议_v3_核心版.md`
- 当前恢复入口：`protocol/前置治理协议_二十个跨渠道项目逆向校验实验.md` 的 `## 220. 当前机器看版`
- 当前 next route：`continue_self_optimization_with_skill_adoption_expansion_or_stop`
- 最近一次整合：仓库独立化、历史回归迁移、恢复链第 215-220 轮、外部 skill 采用扩展，以及新能源汽车项目复盘后的人看版交付/注意力绑定规则。
- GitHub 同步策略：本仓库保留完整工作区快照；公开轻量说明、可视化站点和 reusable protocol package 可以从该工作区继续整理发布。

## 项目目标

- 把复杂项目启动、低摩擦入口、真实项目压力测试、经验库和发布包放在一个小而清楚的项目里。
- 让 Codex 可以围绕该协议单独开工作树、迭代、测试和发布。
- 避免继续依赖或修改 `ai 科研` 大目录。

## 目录

- `protocol/`：协议核心文档、v3 主协议、发布包、自测记录、经验库索引。
- `protocol/复杂项目启动前置治理协议_v3_核心版.md`：当前权威主协议。
- `docs/history/`：从旧目录同步来的历史回归记录、真实项目小题和治理样例。
- `docs/migration/`：独立化迁移清单和路径说明。
- `docs/Complex协议复盘与优化人看版_20260629.md`：新能源汽车项目作为例子的 Complex 协议人看版复盘。
- `docs/protocol_explainer_site/`：协议解释站点源码。
- `outputs/front_governance_protocol_v2/`：v2 版本 Markdown、DOCX、PDF 和渲染页。
- `tools/`：恢复链、链接扫描等辅助工具。
- `docs/`：后续新增说明和设计笔记。

## 推荐工作流

1. 改协议前先看 `protocol/前置治理协议发布包_20260622.md`。
2. 涉及历史恢复链时看 `protocol/持续优化变更清单_20260622.md`。
3. 新项目要求读取 Complex 或 Auto Research 时，先理解核心入口、阶段流程、能力发现、子代理/线程和交付拆分规则，再开始业务执行。
4. 用户提到外部工具、skill、API、数据库、账号、浏览器、机构权限或 Auto Research 时，先建立能力候选清单，写清 selected / rejected / backlog / manual action。
5. 修改后运行工具或结构检查，记录结果。
6. 需要并行探索时，从本项目创建 worktree，而不是从原 `ai 科研` 大目录创建。

## 验证命令

协议或恢复链修改后，优先运行：

```bash
python3 tools/test_verify_governance_recovery.py
python3 tools/verify_governance_recovery.py --preset continuous-self-optimization --latest-heading '## 220. 当前机器看版' --expected-route continue_self_optimization_with_skill_adoption_expansion_or_stop
```

当前基线要求上述两条命令分别返回 `ok` 和 `failure_count: 0`。

## 来源

本项目源自 `/Users/chuchenqidawang/Documents/ai 科研`，相关历史记录已同步到 `docs/history/`。后续协议维护、验证和恢复默认只使用本仓库。
