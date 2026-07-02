# AGENTS.md

## Purpose

`protocol/` contains the current Complex protocol and current recovery state. Keep this directory concise.

## Active Files

- `core.md`: behavior rules for Complex.
- `current-state.md`: current recovery anchor and next route.

## Editing Rules

- Put durable behavior changes in `core.md`.
- Put only the latest recoverable state in `current-state.md`; do not append long historical logs.
- If a change is better taught by a filled example, put it in `docs/examples/` instead of expanding the core protocol.
- Do not add historical archives, migration notes, release packages, or dated machine-board chains to this directory.

## Verification

After protocol edits, run:

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
```
