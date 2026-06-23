# Core Protocol

This document is the public, reusable core of the complex-project front-governance protocol. It is intentionally compact: the protocol should improve project launch quality without turning every kickoff into a heavy form.

## Principle

Govern before execution.

For a complex project, do not start by producing the final artifact. First establish:

1. What the project is trying to prove.
2. What evidence is current and authoritative.
3. What capabilities should be used or rejected.
4. What small validation can reduce uncertainty.
5. What claims must be downgraded.
6. What handoff allows future recovery.

## Minimal Stages

### 0. Intake

Capture the user's goal, materials, expected result, constraints, and any obvious high-risk tags.

Output:

- project objective
- materials list
- open questions
- preliminary risk tags

### 1. Current Basis

Separate materials into:

- `current_basis`: can support current decisions
- `not_current_basis`: background, drafts, stale material, generated output, historical records, or uncertain sources
- `unknown`: needs confirmation or a small check

Why:

Starting from the wrong material is one of the fastest ways to make a complex project look mature while it is still fragile.

### 2. Primary Claim

Write the strongest claim the project wants to make, then bound it.

Examples:

- "This tool can be deployed in production" is too strong unless deployment, usage, monitoring, and rollback evidence exists.
- "This prototype passes a local validation task" is often a more honest launch-stage claim.

### 3. Evidence Map

For each important judgment, record:

- source
- source role
- what it can support
- what it cannot support
- freshness or version boundary
- missing evidence

### 4. Capability Discovery

Before execution and at key transitions, reconsider:

- local skills
- local tools
- deferred tools
- plugins or connectors
- APIs
- external methods
- subagents or review lanes

Record selected, rejected, and backlog capabilities. Do not install or authorize tools just because they exist.

### 5. Micro Validation

Run one small task that tests the riskiest or highest-leverage assumption.

A good micro-task has:

- a concrete object or record
- direct observed evidence
- unknown or unverified items
- a pass/fail or no-op result
- a downgrade rule

### 6. Risk Boundary

Before making final claims, check:

- external writes
- privacy or sensitive data
- safety, legal, financial, health, or minors-related risk
- deployment and production readiness
- data lineage and freshness
- software delivery state
- security incident claims

If evidence is missing, downgrade the claim rather than filling the gap with confidence.

### 7. Launch Handoff

End with a compact handoff:

- human summary
- current basis
- primary claim
- selected lenses
- decisions
- open risks
- next route
- validation status
- stop or continue condition

## Default Stop Rule

Stop expanding the protocol when a new rule would add complexity without reducing misunderstanding, user friction, verification risk, or recovery risk.
