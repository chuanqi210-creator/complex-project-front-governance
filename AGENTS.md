# AGENTS.md

## Workspace Purpose

This project is the current authoritative workspace for the Complex project continuous-governance protocol extracted from `ai 科研`.

## Defaults

- Treat `/Users/chuchenqidawang/Documents/ai 科研` as historical source material only; do not read from it as an active dependency unless a task explicitly asks for comparison or recovery.
- Keep current protocol, recovery, validation, iteration, and history work inside this repository.
- Keep protocol edits narrow and traceable.
- Put core protocol changes in `protocol/`.
- Put scripts and validation helpers in `tools/`.
- Put Runtime Kit templates in `templates/`.
- Put project-level Codex capability manifests and optional local skills in `.codex/`.
- Put new explanatory notes in `docs/`.
- Put copied historical regression records and evidence in `docs/history/`.
- Put migration notes in `docs/migration/`.
- If creating worktrees, use `.worktrees/` and keep it ignored.

## Capability Discovery

- At task start, stage changes, blockers, verification failures, subagent/tool boundaries, and before final claims, actively reconsider useful capabilities instead of waiting for the user to name them.
- Scan broadly but lightly: installed skills, external skill libraries when relevant, callable tools, deferred tools, plugins/connectors, APIs, libraries, scripts, and external methods.
- Use `.codex/shared-skills.json` as a project-level capability candidate list when helpful, but still verify what is actually callable in the current environment.
- Use `docs/runtime-skill-management.md` to decide whether a skill, tool, plugin, connector, API, browser path, or external method should be selected, rejected, backlogged, or delegated to manual user action.
- Prefer small smoke tests before adopting new capabilities. Do not install or route through large skill/plugin sets just because they exist; record selected, rejected, backlog, and why.
- If a user names external tools, skills, APIs, databases, accounts, browsers, Auto Research, or Complex, bind those words into an explicit capability list before executing; state what will be used, skipped, backlogged, or delegated to manual user action.
- If another project asks to read Complex or Auto Research, first spend visible effort understanding the relevant protocol components, dynamic loop, scoring/route-back rules, delivery boundaries, and tool boundaries; do not start the project work from a shallow protocol mention.

## Runtime Kit

- Treat `templates/` as optional landing pads for new projects: state, evidence, decision, search, question, loop, and delivery records.
- Do not turn Runtime Kit templates into new mandatory protocol fields unless repeated real project failures justify promotion.
- When bootstrapping a new Complex project, prefer a small runtime skeleton over copying the full protocol into the project workspace.

## Delivery Defaults

- When the user requests a human-readable deliverable, keep machine boards, YAML, verifier internals, and protocol jargon out of the user-facing output unless they directly affect a decision.
- Before delivering comments, teacher-facing notes, third-party explanations, or mixed human/machine artifacts, align the audience, purpose, granularity, tone, and internal-information boundary.

## Verification

After protocol edits, prefer lightweight structural checks first:

```bash
python3 tools/verify_governance_recovery.py
python3 tools/test_verify_governance_recovery.py
```

If a checker is not applicable, record why in the task notes.
