# AGENTS.md

## Workspace Purpose

This repository is the current authoritative Complex continuous-governance runtime kit. Keep it small, current, and directly useful for new projects.

## Defaults

- Start from `README.md`, `protocol/current-state.md`, `docs/quickstart.md`, and `protocol/core.md`.
- Do not reintroduce history archives, migration records, old rendered outputs, or long machine-board logs into the active tree.
- Put core behavior rules in `protocol/core.md`.
- Put current recovery state in `protocol/current-state.md`.
- Put Runtime Kit templates in `templates/`.
- Put filled examples in `docs/examples/`.
- Put lightweight docs in `docs/`.
- Put validation helpers in `tools/`.
- Put project-level capability manifests and optional local skills in `.codex/`.

## Complex Behavior

- Use `complex_behavior_kernel` first: restore true state, classify project nature, assign decision rights, pick one highest-leverage question, run the lightest useful action, deliver to the right audience, and leave next-route recovery.
- Classify `project_nature` as `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
- Protect model discovery when the model, metric, research frame, explanation path, or story line is unsettled.
- Use strong autonomy with guardrails: AI may decide reversible low-side-effect project details; ask before main-goal changes, accounts/APIs/payment/publishing/external writes, irreversible actions, public-voice changes, high-risk real-world action, or strong claims without enough evidence.
- Apply `human_intervention_drift_guard`: before asking the user, prove the issue truly needs user authority or judgment. If accessible state, `round_goal`, `next_route`, files, or links already define a clear low-risk next step, continue and record why user intervention was unnecessary.
- Use `context_pointer_first_intake`: when the user provides directories, files, links, exports, or material locations, read and summarize accessible materials yourself before asking for manual cleanup or summaries.
- Do not present same-session roleplay as independent review. Use clean context, a separate reviewer/thread, a read-only audit subagent, or a fact-ledger packet when independence matters; otherwise label it as same-session diagnostic self-review.
- In prompt-based continuous projects, use `round_prompt_rehydration_gate` before each new Plan/Loop so each round inherits the master prompt, current state, and `round_goal`.
- Do not use one long Codex tool Goal for many continuous rounds. Store continuity in state, master prompt, and `next_route`; use narrow per-round goals when tool Goals are useful.
- Treat selected `连续节拍` as an active runtime contract: each beat creates or records a narrow `round_goal`, runs the Loop, routes the result, and starts the next queued low-risk reversible beat until a real boundary appears.
- If temporary subagents, parallel review, or read-only audit are clearly useful and authorized, activate the available topology rather than only recommending it. Reset context for each independent review beat with a fact ledger, clean reviewer, or read-only audit lane.
- When applying Complex to another repository, reconcile steering words against that repository's local `AGENTS.md`, `CONTEXT.md`, current state, stage boards, manifests, no-write boundaries, and manual-action records. If a true external-input boundary blocks the main route, run allowed residual beats before pausing: boundary contradiction repair, submission-friction reduction, non-expansion verification, exact operator handoff, or preflight after the required file/env var appears.

## Runtime Kit

- Prefer filled examples before blank templates: evidence fill, model discovery, and independent review.
- Keep templates optional. Do not promote a new field to required status unless repeated real project failures justify it.
- Keep routine judgments lightweight. Use deeper route reflection only for strategic or critical route changes.

## Delivery Defaults

- Human-readable deliverables should avoid machine-board fields, YAML, verifier internals, and protocol jargon unless they affect the reader's decision.
- Align audience, purpose, granularity, tone, and internal-information boundary before teacher-facing, expert-facing, third-party, or mixed human/machine outputs.

## Verification

After protocol, template, behavior-pack, or site edits, run:

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
```

Run the explainer site build when site files changed:

```bash
pnpm -C docs/protocol_explainer_site build
```
