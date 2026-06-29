# Repository Independence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make this repository the active, self-contained home for the complex-project front-governance protocol.

**Architecture:** Copy the missing authoritative protocol and historical regression records into local `protocol/` and `docs/history/`, then update tool defaults and current project documents to use repository-local paths. Preserve historical old-path mentions in logs when they describe past work.

**Tech Stack:** Markdown protocol documents, Python validation scripts, Git.

---

### Task 1: Add a Failing Default-Path Test

**Files:**
- Modify: `tools/test_verify_governance_recovery.py`

- [ ] Add a test that imports `tools/verify_governance_recovery.py` and asserts each default path is inside the repository.
- [ ] Run `python3 tools/test_verify_governance_recovery.py` and confirm it fails because defaults still point to `/Users/chuchenqidawang/Documents/ai 科研` and Desktop.

### Task 2: Copy Missing Local Sources

**Files:**
- Create: `protocol/复杂项目启动前置治理协议_v3_核心版.md`
- Create: `docs/history/*.md`
- Create: `docs/migration/独立化迁移清单_20260623.md`

- [ ] Copy the Desktop v3 protocol into `protocol/`.
- [ ] Copy front-governance regression and recovery records from `/Users/chuchenqidawang/Documents/ai 科研` into `docs/history/`.
- [ ] Write a migration manifest that maps each copied source to its local destination.

### Task 3: Switch Tool Defaults To This Repository

**Files:**
- Modify: `tools/verify_governance_recovery.py`

- [ ] Change default root discovery to resolve from the script location.
- [ ] Point default protocol, long log, release package, changelog, and route table at local repository files.
- [ ] Run the default-path test and confirm it passes.

### Task 4: Update Current Project Documentation

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `来源记录.md`
- Modify: `操作记录.md`
- Modify: `protocol/前置治理协议发布包_20260622.md`
- Modify: `protocol/持续优化变更清单_20260622.md`
- Modify: `protocol/真实项目压力测试_跨域收束与低摩擦路由表_20260622.md`
- Modify: `protocol/复杂项目启动_低摩擦用户入口_20260622.md`

- [ ] Replace current operating paths with this repository path.
- [ ] Mark `/Users/chuchenqidawang/Documents/ai 科研` as historical source only.
- [ ] Keep old absolute paths in historical logs unless they are part of a current recovery command.

### Task 5: Verify Self-Containment

**Commands:**
- `python3 tools/test_verify_governance_recovery.py`
- `python3 tools/append_eof_section.py scan protocol/前置治理协议_二十个跨渠道项目逆向校验实验.md --latest-heading "## 214. 当前机器看版"`
- `python3 tools/verify_governance_recovery.py --preset continuous-self-optimization --latest-heading "## 214. 当前机器看版" --expected-route continue_self_optimization_with_next_real_project_builder_or_software_delivery_state_boundary_regression`
- `rg -n 'DEFAULT_ROOT = Path\\(\"/Users/chuchenqidawang/Documents/ai 科研\"\\)|DEFAULT_PROTOCOL = Path\\(\"/Users/chuchenqidawang/Desktop' tools`

- [ ] Record command results in `操作记录.md`.
