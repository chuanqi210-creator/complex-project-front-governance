# Runtime Skill Management

This note explains how Complex projects should manage skills, tools, plugins, connectors, APIs, browser access, and external methods at runtime. It is part of the Complex Runtime Kit: a landing layer for project execution, not a replacement for the core protocol.

## Purpose

Complex projects often fail because useful capabilities are not considered at the right time, or because a capability is adopted without proving it fits the current project gap.

Runtime skill management keeps capability use tied to project progress:

1. Discover what might help.
2. Choose what fits the current stage.
3. Reject or backlog what does not fit.
4. Test risky capabilities with a small task before relying on them.
5. Write the result back into state, evidence, decisions, loop checks, or delivery records.

Before copying blank templates, check whether a filled golden example is closer to the task:

- `docs/examples/evidence_fill_minimal_runtime/` for fixed-model evidence and delivery work.
- `docs/examples/model_discovery_minimal_runtime/` for unsettled framing and research-model discovery.

Examples are allowed to be copied, shortened, or adapted. Their purpose is to teach shape, not to become mandatory forms.

## Startup Choice Card

When a user starts a project by saying "use Complex", "按 Complex 推进", or similar, do not wait for the user to know hidden trigger words. Use the `complex_setup_question_card` from `templates/question.md`, or state safe defaults if the task is low risk.

Confirm or default these choices:

- Delivery audience and format.
- External capability permission: web, browser, database, account, API, skill, plugin, connector, or external method.
- Collaboration topology: main thread, temporary subagent, long-running thread, or parallel review.
- Cadence: one round with a next route, or continuous cadence.
- Project nature: evidence filling, model discovery, mixed discovery-to-evidence, or execution delivery.
- Autonomy boundary: default to strong autonomy with guardrails for reversible project details, unless the user asks for tighter confirmation.
- Evidence, privacy, account, payment, publishing, or manual-action boundary.

This card is not a new mandatory verifier field. It is a low-friction way to avoid hidden-trigger behavior and to keep capability use tied to user intent.

## Prompt Bootstrap

When a user wants to give a short but high-fit instruction such as "scan Complex and design a prompt for this project", use `complex_prompt_bootstrap_gate` and `templates/prompt.md`.

The agent should:

1. Scan the relevant Complex entry points before business execution.
2. Ask or default the same startup choices: delivery, capabilities, topology, cadence, and boundaries.
3. Produce a copy-ready project prompt that includes the selected capability policy, rejected/backlogged capabilities, manual-action boundaries, Loop, scoring route, and delivery contract.
4. Wait for user confirmation before executing, unless the user explicitly authorized "design and execute".
5. Treat the prompt as a project startup contract, not a replacement for Complex or for later user corrections.

This bootstrap is especially useful for new projects, new users, or handoff into another Codex thread where the receiving agent needs a compact but complete execution prompt.

For continuous prompt-based projects, rehydrate the prompt each round before planning. The round prompt should inherit the confirmed master prompt, current state, capability policy, topology, and delivery contract, then add only the current `round_goal` and prompt patches. Rehydration is not new authorization to use accounts, APIs, external writes, or subagents beyond the existing boundary.

## Adaptive Judgment Boundary

Capability work should not force the user to adjudicate every small tool, depth, or route choice. Complex defaults to `strong_autonomy_with_guardrails`: the agent may decide reversible, low-side-effect project details when the decision can be recovered from state.

The agent may usually decide:

- Whether to deepen, compress, route back, or keep a lightweight refresh.
- Which candidate capability to select, reject, backlog, or try with a small smoke test.
- Whether a temporary subagent split, read-only review, or main-thread-only path best fits the current gap.
- Whether model-discovery work should keep diverging or begin converging based on probes and argument quality.

The agent must ask or require manual action before:

- Changing the main goal or delivery/public voice.
- Using accounts, paid resources, APIs with side effects, browser sessions tied to private state, publishing, submitting, commenting, or external writes.
- Performing irreversible file or project operations.
- Taking high-risk real-world action or making strong public claims with insufficient evidence.

For strategic or critical decisions, record a short `route_evaluator_reflection_gate` note: selected route, rejected route, reason, highest misjudgment risk, counterexample, and rollback or recovery route. For routine fast decisions, a sentence is enough; do not create a table ritual.

## Per-Round Goal Lifecycle

Continuous cadence should not depend on one long Codex tool Goal that spans dozens of rounds. Use state, master prompt, closure routing, and `next_route` as the continuity carriers. When a tool Goal is useful, make it a narrow per-round objective that can be completed when that beat finishes.

If a current tool Goal is stale or blocked but the project state still shows a viable next route, treat the situation as a goal lifecycle mismatch, not a project blockage. Record a `protocol_round_goal` or `goal_migration_note`, continue from state, and only ask for manual cleanup if the tool state itself prevents the next round.

## When To Reconsider Capabilities

Reconsider capabilities at these points:

- A new project starts.
- A Complex startup choice card is asked or defaulted.
- A Complex prompt bootstrap is requested or confirmed.
- A continuous round rehydrates the project prompt for a new Plan/Loop.
- The adaptive judgment controller marks a route, depth, topology, or tool decision as strategic or critical.
- The project changes stage or route.
- The user names a tool, skill, API, database, account, browser, Auto Research, Complex, or external method.
- A search, verification, render, data, or delivery task is blocked.
- A subagent, long-running thread, or external write is being considered.
- A final claim is about to be made.

For continuous cadence, reconsider capabilities by event trigger first. Trigger a real refresh when the main chain, project nature, delivery audience, project version, evidence path, material type, subthread responsibility, account/API boundary, external write boundary, or repeated block changes. Three rounds is only a fallback cap: if no event has fired by then, do a lightweight fit check and deepen only when something is actually stale.

Small local tasks may intentionally skip broad discovery, but the skip reason should be clear.

## Capability Sources

Check only the sources relevant to the current gap:

- Local repository scripts and templates.
- Available Codex skills and callable tools.
- Deferred tools, plugins, connectors, and APIs.
- Browser, Scholar, publisher, database, or institutional access paths.
- User-provided files, screenshots, exports, accounts, or manual actions.
- External methods or best practices that can be translated into this project.

Environment-listed does not mean callable. Installable does not mean authorized. A public method does not automatically fit the current project.

## Selection Record

For each meaningful candidate, record:

| Field | Meaning |
| --- | --- |
| candidate | Skill, tool, plugin, connector, API, template, account path, or external method |
| type | skill / tool / plugin / connector / API / browser / template / external_method / manual_action |
| selected_now | Whether it will be used in this round |
| rejected_now | Why it is not useful or safe now |
| backlog | When it might be useful later |
| manual_action_required | What only the user can do |
| side_effect_boundary | Whether it can read, write, install, publish, authenticate, or change external state |
| verification_hint | What evidence will prove it helped |

This can live in a project state file, decision file, machine recovery note, or a short task note. It does not need to be a large table when a sentence is enough.

## Event-Triggered Refresh

Continuous projects need refresh because the best capability at round 1 may be wrong later. But a mechanical full review can also interrupt thinking, especially in model-discovery work. Use event triggers first and a 3-round fallback cap second.

At each refresh point, check:

- Which selected capabilities still match the current route.
- Which rejected or backlog capabilities have become relevant.
- Whether a long-running thread or subagent needs a new context packet.
- Whether an external account, browser path, database, or API now needs user authorization.
- Whether a previous manual action has been completed and should move into evidence.

Record one of these outcomes:

- keep: still fits the current round.
- lightweight_keep: no trigger fired; no full review needed.
- adjust: same capability, new role or boundary.
- replace: old capability no longer fits; use another one.
- pause: keep in backlog but do not use now.
- manual_action: user must operate or authorize outside the agent.
- retire: no longer relevant.

Do not treat this refresh as a full project restart. It is a correction loop.

For model-discovery work, defer broad capability refresh until there is a discriminating probe or evidence path. If the project is still comparing frames, record `capability_posture: defer_until_probe_or_evidence_path` rather than scattering attention across tools.

## Adoption Rules

Use a capability now when:

- It directly reduces the current highest-risk uncertainty.
- It can be tried with acceptable cost.
- Its output can be verified.
- Its side effects are understood.
- It improves the current project, not just the agent's tooling story.

Reject or defer a capability when:

- The current local tools are enough.
- It would require authorization the user has not granted.
- It would install, publish, comment, grade, submit, or modify external state without a clear boundary.
- It solves a general tooling curiosity but not the current project gap.
- It would create more process than clarity.

## Small Test Before Trust

Before relying on a new or uncertain capability, run a small test when possible:

- Read one file before indexing a whole repository.
- Render one page before claiming a document pipeline is healthy.
- Search one canonical source before broad literature expansion.
- Ask a read-only subagent to audit one claim before delegating a larger review.
- Try one template on the current project before making it standard.

Record what the test proves and what it cannot prove.

## User and Account Boundaries

The agent must not handle passwords, bypass authorization, or silently perform high-impact account actions.

When user help is needed, say exactly:

- Where the user should operate.
- What they should retrieve or confirm.
- Why AI cannot safely do it alone.
- What evidence should come back.

Examples include institutional database access, browser sessions tied to personal accounts, paid resources, private repositories, publishing, submissions, grading, and external system writes.

## Writing Back

After capability use, update the smallest useful record:

- `templates/state.md` for current status and next route.
- `templates/evidence.md` for what the capability proved.
- `templates/decision.md` for major adoption or rejection decisions.
- `templates/search.md` for external search and access escalation.
- `templates/framing.md` for model-discovery framing and convergence conditions.
- `templates/argument.md` for issue-position-argument maps.
- `templates/judgment.md` for strategic or critical route, autonomy, and recovery decisions.
- `templates/loop.md` for small capability trials.
- `templates/delivery.md` if capability output affects the final artifact.

For protocol maintenance work, update the relevant protocol or release package only when the lesson is reusable across projects. A one-off case can stay in docs, history, or backlog.

## Anti-Bloat Rule

Runtime skill management should reduce friction. It should not become a ritual.

Use the behavior kernel as the deletion test. If a proposed skill rule, capability field, or template addition does not improve state recovery, project-nature classification, decision rights, highest-leverage choice, light validation/execution, delivery contract, or next-route recovery, keep it out of the core path.

Do not add a new skill, template, gate, or required field unless it meets at least one of these tests:

- It prevents a repeated real failure.
- It lowers user correction cost.
- It improves evidence quality.
- It makes recovery easier for later work.
- It protects against unauthorized or high-impact side effects.

If the value is only local or uncertain, keep it as a project note or backlog item.
