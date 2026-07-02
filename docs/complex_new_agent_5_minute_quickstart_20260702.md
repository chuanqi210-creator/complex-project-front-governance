# Complex New Agent 5-Minute Quickstart

Audience: a new Codex/agent thread asked to "use Complex" or "scan Complex and continue this project."

Goal: get useful behavior quickly without reading every historical gate.

One-sentence model: Complex is strong-autonomy continuous execution with evidence boundaries, anti-human/context-drift safeguards, and an auditable recovery chain.

## Minute 0-1: Recover The Current Anchor

Read:

- `README.md`
- latest recovery anchor: `protocol/持续治理协议_二十个跨渠道项目逆向校验实验.md` -> `## 224. 当前机器看版`

Remember:

- `## 224` is the latest recovery state.
- `complex_behavior_kernel` is the execution spine.
- Historical sections such as `## 220` are useful context, not the current entry.

## Minute 1-2: Use The Seven-Step Behavior Kernel

Before planning, compress the task into these seven behaviors:

1. Restore true state.
2. Classify project nature and convergence.
3. Assign decision rights and guardrails.
4. Pick one highest-leverage question.
5. Run the lightest useful validation or execution.
6. Deliver to the right audience.
7. Leave next-route recovery.

If a gate name competes with these behaviors, the behavior kernel wins.

Decision rights are two-sided: prevent unsafe AI overreach, but also prevent unnecessary human intervention. If the next step is clear, low-risk, reversible, and inside existing authorization, continue and record why the user was not asked. If the user gives paths, files, links, or material locations, read accessible materials yourself before asking for manual cleanup or summaries.

## Minute 2-3: Classify The Project

Choose one:

- `evidence_fill`: model, formula, metric, or framework is fixed; fill evidence and delivery boundary.
- `model_discovery`: framework, explanation path, metric, or research model is unsettled; protect candidate frames.
- `mixed`: start with model discovery, then switch to evidence fill when convergence conditions are met.
- `execution_delivery`: the main job is implementation, delivery, or packaging.

If unsure, default to `mixed` and make the uncertainty explicit.

## Minute 3-4: Pick The Runtime Shape

Use filled examples before blank templates:

- `docs/examples/evidence_fill_minimal_runtime/`
- `docs/examples/model_discovery_minimal_runtime/`
- `docs/examples/independent_review_minimal_runtime/`

Minimum records:

- `state.md`: current state, goal, authority, next route.
- `loop.md`: one small validation or explicit no-op.
- `delivery.md`: audience and output boundary.

Add only what the task needs:

- Evidence-fill: `evidence.md`, `decision.md`, `search.md`.
- Model-discovery: `framing.md`, `argument.md`, `judgment.md`.
- Independent review: `fact-ledger.md`, `judgment.md`, `decision.md`.
- Prompt-based continuity: `prompt.md`.

## Minute 4-5: Start Low-Friction Execution

If the user only says "按 Complex 推进", give short defaults instead of a mode menu:

- delivery audience:
- capability permission:
- topology:
- cadence:
- autonomy boundary:
- manual-action boundary:

Then make a narrow `round_goal` and execute the lightest useful next action.

If the user asks for "independent review" inside the same session, do not claim roleplay is independent. Either route to clean context, separate reviewer/thread, read-only audit subagent, or a fact-ledger-only packet; if you stay in the same session, label it as diagnostic self-review.

Use `docs/examples/independent_review_minimal_runtime/fact-ledger.md` as the shape for clean-context review: include artifacts, claims, evidence anchors, decisions, and unresolved questions; exclude full chat momentum, stale drafts, and the prior assistant's confidence unless needed for user-intent evidence.

## When Something Feels Wrong

Do not immediately add a new protocol rule.

1. Map the failure to one of the canonical behavior cases in `docs/behavior_regression_cases_20260702.json`.
2. Run transcript review:

```bash
python3 tools/review_behavior_transcript.py --case-id <case_id> --text-file <response.txt>
```

3. Record the result with `docs/behavior_review_result_template_20260702.md`.
4. If the failure repeats, update the transcript rule, behavior case, or golden example before promoting a new core protocol rule.

## Best Default Prompt

```text
请先按 Complex 恢复当前状态，并用 7 步行为内核压缩本轮行动。
先判断本项目是 evidence_fill、model_discovery、mixed 还是 execution_delivery。
如果缺少我的确认，请给出少量可默认的问题；可逆、低副作用的细节由你自行判断，高风险、授权、外部写入、不可逆动作和公开口径变化再问我。
如果下一步已由 next_route / round_goal / 可访问材料说明清楚，请直接推进并说明为什么不需要回问；如果我给了目录、文件或链接，请优先自行读取。
本轮只抓一个最高杠杆问题，用最轻有效动作推进，最后给出适合交付对象的人看版，并留下 next_route。
```
