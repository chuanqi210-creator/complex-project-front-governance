# complex-project-front-governance

这是从 `/Users/chuchenqidawang/Documents/ai 科研` 拆出并独立化后的“复杂项目启动前置治理协议”项目。本仓库现在是当前权威工作区，旧 `ai 科研` 目录只作为历史来源。

## 项目目标

- 把复杂项目启动、低摩擦入口、真实项目压力测试、经验库和发布包放在一个小而清楚的项目里。
- 让 Codex 可以围绕该协议单独开工作树、迭代、测试和发布。
- 避免继续依赖或修改 `ai 科研` 大目录。

## 目录

- `protocol/`：协议核心文档、v3 主协议、发布包、自测记录、经验库索引。
- `docs/history/`：从旧目录同步来的历史回归记录、真实项目小题和治理样例。
- `docs/migration/`：独立化迁移清单和路径说明。
- `outputs/front_governance_protocol_v2/`：v2 版本 Markdown、DOCX、PDF 和渲染页。
- `tools/`：恢复链、链接扫描等辅助工具。
- `docs/`：后续新增说明和设计笔记。

## 推荐工作流

1. 改协议前先看 `protocol/前置治理协议发布包_20260622.md`。
2. 涉及历史恢复链时看 `protocol/持续优化变更清单_20260622.md`。
3. 修改后运行工具或结构检查，记录结果。
4. 需要并行探索时，从本项目创建 worktree，而不是从原 `ai 科研` 大目录创建。

## 来源

本项目源自 `/Users/chuchenqidawang/Documents/ai 科研`，相关历史记录已同步到 `docs/history/`。后续协议维护、验证和恢复默认只使用本仓库。
