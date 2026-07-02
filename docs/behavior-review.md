# Complex Behavior Review

Purpose: check whether a real agent response followed the Complex behavior kernel, without turning the project back into a thick rule archive.

## Files

- `docs/behavior-regression-cases.json`: canonical behavior cases.
- `docs/behavior-transcript-review-rules.json`: marker groups and human-review questions.
- `tools/check_behavior_regression_pack.py`: validates the case/rule structure.
- `tools/review_behavior_transcript.py`: checks one real response or exported transcript against one case.

## Use

Validate rules:

```bash
python3 tools/review_behavior_transcript.py --validate-rules
```

Review a plain-text response:

```bash
python3 tools/review_behavior_transcript.py \
  --case-id setup_card_default \
  --text-file path/to/agent_response.txt
```

Review an exported JSON transcript:

```bash
python3 tools/review_behavior_transcript.py \
  --case-id model_discovery_protect_divergence \
  --json-file path/to/transcript.json
```

Accepted JSON shapes:

- `{ "assistant_response": "..." }`
- `{ "transcript": "..." }`
- `{ "text": "..." }`
- `{ "messages": [{ "role": "user", "content": "..." }, { "role": "assistant", "content": "..." }] }`

## How To Read Results

The script returns:

- `passed`: marker-level pass/fail.
- `required_passed`: how many required marker groups were found.
- `forbidden_results`: forbidden marker hits.
- `human_review_questions`: questions a reviewer should still answer.

Passing means "no obvious marker-level regression." It does not mean the response was excellent.

Human review still asks:

- Did the response reduce user correction cost?
- Did it choose the right depth for this project?
- Did it preserve the main goal while handling local details?
- Did it avoid asking the user to do low-risk work the agent could safely do itself?
- Did it avoid turning Complex into visible process burden?

## Result Record

Use this compact record for real replies:

```yaml
case_id:
transcript_location:
marker_passed:
human_passed:
user_correction_count:
main_failure_if_any:
decision: no_change / update_rule / update_case / update_example / promote_candidate
notes:
```

Use this compact record for end-to-end project samples:

```yaml
project_type: evidence_fill / model_discovery / mixed / execution_delivery
runtime_records:
behavior_kernel_trace:
transcript_review_case_ids:
user_correction_count:
final_delivery_quality:
remaining_gap:
decision: no_change / update_rule / update_case / update_example / promote_candidate
```

## Promotion Rule

If a real transcript fails and the failure is repeated or high-impact:

1. Add or refine a marker group in `docs/behavior-transcript-review-rules.json`.
2. Update the matching behavior case only if expected behavior changed.
3. Add or adjust a golden example if agents need something concrete to imitate.
4. Promote to `protocol/core.md` only if cases, rules, and examples are not enough.
