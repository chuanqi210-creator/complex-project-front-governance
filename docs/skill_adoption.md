# Skill and Capability Adoption

This project treats skills, tools, plugins, APIs, connectors, subagents, libraries, and external methods as capabilities that must be discovered and adopted deliberately.

The goal is not to install every promising skill. The goal is to improve project launch quality while keeping the protocol lightweight, recoverable, and safe.

## Adoption Rhythm

Run a capability check at these points:

1. At project start, before execution begins.
2. At stage transitions, especially before a project moves from analysis to implementation.
3. When verification fails or the agent is blocked.
4. Before external writes, installs, authentication, deployment, or subagent delegation.
5. Before making the final claim that work is complete.

Small local tasks may record that existing local tools are sufficient. Larger or ambiguous tasks should scan local skills, callable tools, deferred tools, public APIs, libraries, external methods, and review lanes.

## Relevant-First Smoke Test

Use a small test before adopting a capability:

```yaml
capability_smoke_test:
  source_url: ""
  version_or_ref: ""
  micro_task: ""
  observed_benefit: ""
  friction: ""
  risk: ""
  decision: adopt_now | adapt_later | backlog | reject
  promotion_condition: ""
```

Decision meanings:

| Decision | Meaning |
| --- | --- |
| `adopt_now` | Use in the current workflow because it clearly reduces guesswork, friction, overclaiming, or recovery risk. |
| `adapt_later` | Useful, but only under a clearer trigger or after the project grows into that need. |
| `backlog` | Potentially useful after a prerequisite exists, such as issue tracker setup, a PRD, or a dedicated architecture round. |
| `reject` | Not suitable now because it is unavailable, unsafe, redundant, or expands scope without value. |

## Current Public Recommendations

These recommendations came from applying the adoption process to a public engineering-skills library and the needs of this repository.

| Capability | Recommendation | Why |
| --- | --- | --- |
| `diagnosing-bugs` | `adopt_now` | Use when verification or build commands fail, so fixes begin with diagnosis rather than guesswork. |
| `tdd` | `adopt_now` | Use before turning a protocol rule into a script-enforced required field. |
| `ask-matt` | `adopt_now` | Use as a lightweight router when deciding which engineering skill or flow fits the current stage. |
| `review` | `adopt_now` | Use before public sync, recovery-chain edits, or checker changes. |
| `handoff` | `adopt_now` | Use for recoverable context transfer and public-safe handoff examples. |
| `codebase-design` | `adopt_now` | Use when changing boundaries between protocol text, validators, public package checks, and explanatory sites. |
| `grill-with-docs` | `adapt_later` | Useful when a plan or domain vocabulary is unclear, but too heavy for a settled execution plan. |
| `setup-matt-pocock-skills` | `adapt_later` | Run when the public repository starts using GitHub Issues and agent docs as the main workflow. |
| `decision-mapping` | `adapt_later` | Useful when multiple continuation paths compete and the decision needs to be split into tickets. |
| `domain-modeling` | `adapt_later` | Useful when public readers need a glossary for protocol language. |
| `improve-codebase-architecture` | `adapt_later` | Useful for a dedicated architecture-health round, not for every public sync. |
| `to-prd` | `backlog` | Useful after issue tracker setup and a public roadmap exist. |
| `to-issues` | `backlog` | Useful after a PRD exists and work can be split into independent issues. |
| `codegraph` | `backlog` | Re-evaluate after the CLI or equivalent capability is installed and a health check succeeds. Do not claim adoption before then. |

## Promotion Rule

Do not promote a single successful smoke test directly into the core protocol.

- Single-case value goes into examples or this adoption guide.
- Repeated cross-project value may become a protocol rule.
- Only stable, script-checkable rules should become required verifier fields.

This keeps the protocol from becoming a catalog of tools while still letting it learn from good external methods.
