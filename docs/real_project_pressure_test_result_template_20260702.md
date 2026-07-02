# Real Project Pressure Test Result Template

Purpose: record an end-to-end Complex trial on a real project. Use this for the next two priority samples:

1. one `evidence_fill` project;
2. one `model_discovery` project.

The goal is not to prove Complex is perfect. The goal is to measure whether it reduces user correction, prevents premature convergence, improves evidence quality, and leaves a recoverable next route.

## Metadata

- test_id:
- date:
- reviewer:
- project_name:
- project_type: evidence_fill / model_discovery / mixed / execution_delivery
- agent_surface:
- starting_prompt:
- source_material_location:

## Setup

- master_prompt_or_entry:
- startup_choices:
- delivery_audience:
- capability_permissions:
- collaboration_topology:
- autonomy_boundary:

## Runtime Records

Required minimum:

- state_record:
- loop_record:
- delivery_record:

Add when relevant:

- evidence_record:
- framing_record:
- argument_record:
- judgment_record:
- search_record:
- decision_record:

## Behavior-Kernel Trace

| Step | Observed? | Evidence |
| --- | --- | --- |
| Restore true state |  |  |
| Classify project nature |  |  |
| Assign decision rights |  |  |
| Pick highest-leverage question |  |  |
| Run lightest useful action |  |  |
| Deliver to audience |  |  |
| Leave next-route recovery |  |  |

## Transcript Review

- transcript_location:
- behavior_case_id:
- review_command:
- marker_passed:
- human_passed:
- main_gap:

## Outcome Metrics

Use rough but consistent measurement:

| Metric | Value | Note |
| --- | ---: | --- |
| user_correction_count |  | Count explicit user corrections after Complex started |
| route_changes |  | Count meaningful route shifts |
| avoidable_rework_events |  | Count rework caused by agent drift |
| evidence_claim_boundary_score |  | 1-5 |
| delivery_fit_score |  | 1-5 |
| recovery_quality_score |  | 1-5 |
| overall_usefulness_score |  | 1-5 |

## Evaluation

- What improved because Complex was used?
- What still created friction?
- Did the agent over-govern the task?
- Did the agent under-govern a high-risk decision?
- Did model discovery stay open long enough?
- Did evidence filling avoid unnecessary divergence?

## Decision

Choose one:

- pass_no_protocol_change
- update_golden_example
- update_transcript_review_rule
- update_quickstart
- add_behavior_case
- promote_protocol_candidate
- reject_as_project_specific

Decision reason:

## Next Route

- next_route:
- next_trigger:
- recovery_note:
