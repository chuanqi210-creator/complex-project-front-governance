# complex-project-continuous-governance

Complex is a compact runtime kit for pushing complex projects forward with:

**strong-autonomy continuous execution + evidence boundaries + anti-human/context-drift safeguards + an auditable recovery chain.**

This repository is the current authoritative version. Older material is intentionally not kept in the working tree; Git history is the recovery path.

## Current Entrypoints

- Core protocol: `protocol/core.md`
- Current state: `protocol/current-state.md`
- New-agent quickstart: `docs/quickstart.md`
- Runtime templates: `templates/`
- Filled runtime examples: `docs/examples/`
- Behavior regression pack: `docs/behavior-regression-cases.json`
- Transcript review rules: `docs/behavior-transcript-review-rules.json`
- Capability guide: `docs/runtime-skill-management.md`
- External method mapping: `docs/external-methods.md`

## How Complex Works

Complex starts from seven stable behaviors, not from a long menu of gates:

1. Restore the true current state.
2. Classify the project nature: `evidence_fill`, `model_discovery`, `mixed`, or `execution_delivery`.
3. Assign decision rights: AI handles reversible low-risk details; user confirmation is required for goals, authorization, irreversible actions, public voice, high-risk claims, accounts, payments, publishing, or external writes.
4. Pick the single highest-leverage question for this round.
5. Run the lightest useful validation or execution.
6. Deliver to the right audience in the right form.
7. Leave `next_route` and recovery notes.

The practical default is strong autonomy with guardrails: if the next step is clear, low-risk, reversible, and within existing authorization, AI should continue instead of asking whether to continue. If the user gives directories, files, links, or material locations, AI should read accessible materials before asking for manual summaries.

## Best Project Prompt

```text
请帮我扫描 Complex，并对我们的项目设计提示词。之后给出一个可复制的 prompt；我确认后，再根据这个 prompt 结合 Complex 推进项目。
```

If the project should move directly:

```text
这个项目按 Complex 推进。
目标是：……
已有材料在：……
我希望结果达到：……
采用强自治+护栏：可逆、低副作用的细节由 AI 自行判断；目标、授权、不可逆动作、外部写入、公开口径或高风险主张变化时再问我。
```

Useful steering words:

- `模型发现型 / 先发散研究框架 / 不要早收敛`
- `证据填充型 / 模型和指标已定`
- `连续节拍 / 总规划别丢 / 每轮 prompt 重水化`
- `少问我 / 能推进就继续 / 我给目录你自己读`
- `独立评审 / 客观审查 / 避免上下文污染`
- `外部工具 / 账号 / API / skill`
- `只要人看版`

## Runtime Kit

Use the filled examples before blank templates:

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/examples/independent_review_minimal_runtime/`

Use templates only as needed:

- `templates/state.md`: current state, basis, goals, route, and human-intervention boundary.
- `templates/evidence.md`: evidence levels, gaps, and claim boundaries.
- `templates/decision.md`: selected route, rejected routes, and re-evaluation conditions.
- `templates/search.md`: search and acquisition escalation.
- `templates/question.md`: defaultable startup questions.
- `templates/prompt.md`: project prompt bootstrap and round prompt rehydration.
- `templates/framing.md`: model discovery, candidate frameworks, and convergence.
- `templates/argument.md`: issue / position / pro / con map.
- `templates/judgment.md`: autonomy, ask-user necessity, and rollback route.
- `templates/loop.md`: 5-30 minute validation loop.
- `templates/delivery.md`: human-readable and machine-recovery delivery contracts.

## Verification

Run these after protocol, template, behavior-pack, or site changes:

```bash
python3 tools/check_behavior_regression_pack.py
python3 tools/review_behavior_transcript.py --validate-rules
python3 tools/test_verify_complex_integrity.py
python3 tools/verify_complex_integrity.py
pnpm -C docs/protocol_explainer_site build
```

Expected baseline:

- behavior pack: 11 cases and 11 transcript rules
- integrity verifier: `failure_count: 0`
- site build: Vite build succeeds

## Repository Shape

- `protocol/`: current protocol and state only.
- `docs/`: quickstart, external mapping, behavior review, examples, and explainer site source.
- `templates/`: optional runtime records for downstream projects.
- `.codex/`: project-level capability candidates and optional local skills.
- `tools/`: lightweight structural and behavior-review checks.

Do not add history archives, migration records, rendered outputs, or long machine-board logs back into the active tree. If old context is needed, use Git history.
