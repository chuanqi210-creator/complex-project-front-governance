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

## When To Reconsider Capabilities

Reconsider capabilities at these points:

- A new project starts.
- The project changes stage or route.
- The user names a tool, skill, API, database, account, browser, Auto Research, Complex, or external method.
- A search, verification, render, data, or delivery task is blocked.
- A subagent, long-running thread, or external write is being considered.
- A final claim is about to be made.

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
- `templates/loop.md` for small capability trials.
- `templates/delivery.md` if capability output affects the final artifact.

For protocol maintenance work, update the relevant protocol or release package only when the lesson is reusable across projects. A one-off case can stay in docs, history, or backlog.

## Anti-Bloat Rule

Runtime skill management should reduce friction. It should not become a ritual.

Do not add a new skill, template, gate, or required field unless it meets at least one of these tests:

- It prevents a repeated real failure.
- It lowers user correction cost.
- It improves evidence quality.
- It makes recovery easier for later work.
- It protects against unauthorized or high-impact side effects.

If the value is only local or uncertain, keep it as a project note or backlog item.
