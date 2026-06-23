# Startup Handoff Template

Use this template at the end of a front-governance pass.

```yaml
project:
  objective: ""
  primary_claim: ""
  claim_readiness: idea_or_candidate

current_basis:
  included: []
  excluded: []
  unknown: []

selected_lenses:
  - claim_ladder
  - evidence_contract
  - execution_validation
  - transfer_boundary

capability_discovery:
  selected_now: []
  rejected_now: []
  backlog: []
  next_reconsideration_trigger:
    - stage_transition
    - blocked_verification
    - before_final_claim

micro_validation:
  task: ""
  concrete_artifact_or_record: ""
  direct_observed: []
  unknown_or_not_verified: []
  result: ""
  downgrade_rule: ""

risk_boundary:
  high_risk_tags: []
  external_write: none
  manual_action_required: []
  cannot_conclude: []

decisions:
  - decision: ""
    reason: ""
    alternatives_rejected: []

next_route:
  action: ""
  why_next: ""
  stop_condition: ""
```

## Filled Example

This example is fictional. It shows the expected level of detail without requiring a heavy form.

```yaml
project:
  objective: "Launch a small open-source dashboard that summarizes public transit delay data."
  primary_claim: "The dashboard can reproduce one agency-published delay metric for a recent sample day."
  claim_readiness: small_loop_validated

current_basis:
  included:
    - "Official public CSV export for the selected sample day"
    - "Repository README and local build instructions"
  excluded:
    - "Old design mockups"
    - "Social media claims about service quality"
  unknown:
    - "Whether the same metric is stable across a full month"
    - "Whether the dashboard is accessible enough for public use"

selected_lenses:
  - evidence_contract
  - data_artifact_lineage_freshness_guard
  - software_delivery_state_boundary_guard
  - claim_readiness_ladder

capability_discovery:
  selected_now:
    - "local test runner"
    - "CSV parser"
    - "review skill for public README changes"
  rejected_now:
    - "browser automation: not needed until the dashboard UI exists"
    - "deployment connector: no deployment claim in this round"
  backlog:
    - "accessibility checker before public launch"
    - "scheduled data refresh after the metric is stable"
  next_reconsideration_trigger:
    - stage_transition
    - blocked_verification
    - before_final_claim

micro_validation:
  task: "Load one sample-day CSV and reproduce the agency's total-delay count."
  concrete_artifact_or_record: "sample_day_delays.csv"
  direct_observed:
    - "CSV downloaded from official portal"
    - "Local script produced the same total-delay count for the sample day"
  unknown_or_not_verified:
    - "Monthly stability"
    - "Production deployment"
    - "Real user adoption"
  result: "pass"
  downgrade_rule: "Can claim sample-day metric reproduction only; cannot claim production readiness or public impact."

risk_boundary:
  high_risk_tags: []
  external_write: none
  manual_action_required:
    - "Confirm data license before publishing screenshots"
  cannot_conclude:
    - "The dashboard is reliable for every day"
    - "The dashboard is deployed"
    - "The dashboard improves transit operations"

decisions:
  - decision: "Use one sample-day validation before building more charts."
    reason: "It tests the core evidence and parsing path with low cost."
    alternatives_rejected:
      - "Build the full dashboard first"
      - "Claim live monitoring before a refresh strategy exists"

next_route:
  action: "Implement the smallest dashboard view around the validated metric."
  why_next: "The source, parser, and claim boundary are now clear."
  stop_condition: "Stop if the metric cannot be reproduced on a second sample day."
```
