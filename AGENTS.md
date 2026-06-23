# AGENTS.md

## Workspace Purpose

This project is a focused workspace for the complex-project front-governance protocol extracted from `ai 科研`.

## Defaults

- Preserve source materials in `/Users/chuchenqidawang/Documents/ai 科研`; do not mutate them unless explicitly asked.
- Keep protocol edits narrow and traceable.
- Put core protocol changes in `protocol/`.
- Put scripts and validation helpers in `tools/`.
- Put new explanatory notes in `docs/`.
- If creating worktrees, use `.worktrees/` and keep it ignored.

## Verification

After protocol edits, prefer lightweight structural checks first:

```bash
python3 tools/verify_governance_recovery.py
python3 tools/test_verify_governance_recovery.py
```

If a checker is not applicable, record why in the task notes.

