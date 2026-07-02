# Behavior Review Result Template

Purpose: record the result of reviewing a real agent response against Complex behavior cases. Use this for the 8-12 real transcript samples recommended by the current project evaluation.

This template is for real observations only. Do not fill it with imagined transcripts.

## Metadata

- review_id:
- date:
- reviewer:
- source_project:
- transcript_location:
- case_id:
- project_nature:
- agent_surface:

## Input

- user_prompt:
- relevant_context_summary:
- expected_behavior_case:

## Marker Review

Command:

```bash
python3 tools/review_behavior_transcript.py --case-id <case_id> --text-file <agent_response.txt>
```

Result:

- marker_passed:
- required_passed:
- required_total:
- forbidden_hits:
- missing_required_groups:

## Human Review

Answer briefly, in ordinary language:

- Did the agent reduce user correction cost?
- Did it pick the right depth for the project?
- Did it preserve the main goal while handling local details?
- Did it avoid exposing Complex as visible process burden?
- Did it keep delivery audience and internal-information boundary clear?

Human score:

| Dimension | Score 1-5 | Note |
| --- | ---: | --- |
| Goal alignment |  |  |
| Behavior-kernel coverage |  |  |
| Evidence/tool boundary |  |  |
| Low-friction execution |  |  |
| Delivery fit |  |  |

Overall:

- human_passed:
- user_correction_count:
- main_failure_if_any:
- severity: low / medium / high

## Decision

Choose one:

- no_change_needed
- update_transcript_rule
- update_behavior_case
- add_or_update_golden_example
- update_quickstart_or_README
- promote_to_protocol_candidate
- backlog_for_real_project_pressure_test

Decision reason:

## Follow-Up

- owner:
- due_trigger:
- linked_commit_or_issue:
- next_review_case:
