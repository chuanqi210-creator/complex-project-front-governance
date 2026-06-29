# Repository Independence Design

Date: 2026-06-23

## Purpose

Make this repository the only active source for the complex-project front-governance protocol. The previous `/Users/chuchenqidawang/Documents/ai 科研` directory and Desktop protocol file become historical sources only, not runtime dependencies.

## Scope

This migration keeps the old source directory untouched. It copies the governance protocol material needed for recovery, validation, and future iteration into this repository, then updates current project docs and tools so the default paths point here.

## Authoritative Files

- `protocol/复杂项目启动前置治理协议_v3_核心版.md` becomes the local v3 core protocol.
- `protocol/前置治理协议_二十个跨渠道项目逆向校验实验.md` remains the long recovery log.
- `protocol/前置治理协议发布包_20260622.md` remains the current release package.
- `protocol/持续优化变更清单_20260622.md` remains the change inventory.
- `protocol/真实项目压力测试_跨域收束与低摩擦路由表_20260622.md` remains the route table.
- `docs/history/` stores copied historical regression records that were previously only in `ai 科研`.
- `docs/migration/` stores the migration map and notes.

## Path Policy

Current instructions, tool defaults, and recovery commands should use this repository path. Historical logs may retain old absolute paths where they describe past work; new current-state sections should identify those paths as historical source references.

## Validation

The migration is considered usable when:

1. `python3 tools/test_verify_governance_recovery.py` passes.
2. `python3 tools/verify_governance_recovery.py --preset continuous-self-optimization --latest-heading "## 214. 当前机器看版" --expected-route continue_self_optimization_with_next_real_project_builder_or_software_delivery_state_boundary_regression` reads this repository by default.
3. The latest recovery log tail scan still finds `## 214. 当前机器看版` at EOF with no pseudo headings or pending markers.
4. `rg` confirms active tool defaults no longer point to `/Users/chuchenqidawang/Documents/ai 科研` or Desktop protocol paths.

## Out Of Scope

This task does not delete, archive, or mutate `/Users/chuchenqidawang/Documents/ai 科研`. Any cleanup of that directory should happen only after this repository verifies as self-contained.
