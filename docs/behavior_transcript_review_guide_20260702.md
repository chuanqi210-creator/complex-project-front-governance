# Complex Behavior Transcript Review Guide

Purpose: close the gap between "the behavior regression cases exist" and "a real agent response followed them." The current structural checker proves that cases, triggers, and templates are present. Transcript review checks a concrete response or exported conversation against the expected behavior markers and forbidden moves.

## What This Adds

- `docs/behavior_transcript_review_rules_20260702.json`: marker groups and human-review questions for the 8 canonical behavior cases.
- `tools/review_behavior_transcript.py`: a small reviewer that checks a real transcript against one case.
- `tools/check_behavior_regression_pack.py`: still checks the case bank, and now also validates that every case has transcript review rules.

This is still not a full LLM benchmark. It is a practical middle layer:

1. Structural regression: are the cases and rules maintained?
2. Transcript review: did a real response include required behavior signals and avoid obvious forbidden moves?
3. Human review: did the response actually reduce user correction cost in context?
4. Future LLM judge: optional later layer if enough real transcripts accumulate.

## How To Use

Run rule validation:

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

The script returns JSON:

- `passed`: marker-level pass/fail.
- `required_passed`: how many required marker groups were found.
- `forbidden_results`: forbidden marker hits.
- `human_review_questions`: the questions a reviewer should still answer.

Pass means "no obvious marker-level regression." It does not mean the response was excellent. A good review still asks:

- Did the agent reduce user correction cost?
- Did it choose the right depth for this project?
- Did it preserve the main goal while handling local details?
- Did it avoid turning Complex into visible process burden?

## Promotion Rule

If a real transcript fails and the failure is repeated or high-impact:

1. Add or refine a marker group in `behavior_transcript_review_rules_20260702.json`.
2. Update the matching behavior case only if the expected behavior changed.
3. Add a golden example if users need a concrete artifact to imitate.
4. Promote to the main protocol only if examples and transcript rules are not enough.

This keeps Complex in the behavior-compression phase instead of returning to rule sprawl.
