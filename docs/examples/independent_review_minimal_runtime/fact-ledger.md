# Fact Ledger Example

Purpose: give a reviewer enough evidence to judge the work without inheriting the full chat history, social pressure, or the original assistant's preferences.

## Include

- artifact_under_review:
  - `docs/project_plan.md`
  - `templates/state.md`
  - latest delivery draft
- user_goal:
  - Improve Complex project execution quality while avoiding protocol bloat.
- current_claims_to_review:
  - The plan reduces unnecessary user intervention.
  - The plan preserves authorization and public-claim guardrails.
  - The plan is easier for a new agent to follow than the previous version.
- evidence_anchors:
  - behavior regression case ids
  - verification command outputs
  - linked source files and line-level anchors when available
- decisions_already_made:
  - Do not add a thick new gate if behavior cases and examples are enough.
  - Keep Runtime Kit templates optional.
- unresolved_questions:
  - Does the plan under-ask when authorization is ambiguous?
  - Does the fact ledger omit context needed to judge user intent?

## Exclude

- Full chat transcript unless directly needed.
- The original assistant's self-praise or confidence.
- User emotional tone unless it changes the goal, authorization, or delivery contract.
- Drafts that are not current basis.
- Hidden chain-of-thought or private tool logs.

## Reviewer Task

1. Check whether each major claim is supported by the included artifacts.
2. Identify missing evidence, overclaims, and authorization risks.
3. State whether the review was clean-context independent, separate-thread independent, read-only subagent audit, or same-session diagnostic.
4. Return only findings, residual risks, and recommended route-back points.
