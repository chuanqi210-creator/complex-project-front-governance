# Delivery Example: Review Output Boundary

## Same-Session Diagnostic Label

Use this label when the review stays in the same conversation:

```text
This is a same-session diagnostic self-review, not an independent audit. It can catch obvious inconsistencies, missing evidence, and overclaims, but it may inherit the prior conversation's framing.
```

## Independent Review Label

Use this label only when the reviewer had clean context, a separate thread/reviewer, or a read-only audit subagent with a fact-ledger packet:

```text
This review used a separated context packet: artifacts, claims, evidence anchors, decisions, and unresolved questions. It did not rely on the full prior chat except for explicitly listed current-basis facts.
```

## Human-Readable Findings Shape

- Findings first, ordered by severity.
- For each finding: claim, evidence status, why it matters, route-back.
- Residual risks: what the review could not judge from the fact ledger.
- Next route: continue, route back, ask user, or dispatch deeper independent audit.

## Machine Recovery Notes

- review_route: same_session_diagnostic / clean_context_independent / read_only_audit_subagent
- fact_ledger_location:
- artifacts_reviewed:
- excluded_context:
- unsupported_claims:
- next_route:
