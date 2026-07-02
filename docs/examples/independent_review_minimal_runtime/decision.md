# Decision Example: Review Route

## Decision

- selected_route: clean-context independent review when independence is material; same-session diagnostic only when speed matters more than independence.
- decision_owner: main agent
- date: 2026-07-02

## Why

- Same-session review is still useful for catching obvious gaps, but it inherits the prior conversation's framing.
- True independent review needs context separation, a fact ledger, and a narrow output contract.
- Passing the full chat history to a reviewer can reproduce the same bias the review is supposed to detect.

## Rejected Routes

- same_session_roleplay_as_independent:
  - reason: false independence; high context-contamination risk.
- ask_user_to_open_new_session_manually_by_default:
  - reason: offloads agent-manageable setup work to the user.
- full_chat_dump_to_reviewer:
  - reason: too much persuasion, too many stale drafts, and weak reproducibility.

## Re-Evaluate If

- user says the review must judge intent expressed in the chat.
- reviewer cannot access artifacts from the fact ledger.
- the project becomes high-stakes enough to require a different reviewer or model family.
- authorization, public claims, external writes, or irreversible actions enter scope.
