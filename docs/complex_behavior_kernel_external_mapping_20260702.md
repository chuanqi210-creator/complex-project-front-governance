# Complex Behavior Kernel External Mapping 2026-07-02

Purpose: use high-quality external agent and project-governance work to improve Complex without increasing rule density. The output of this note is not another gate list. It is a compression rule: every borrowed idea must strengthen the seven-step `complex_behavior_kernel`.

## What Complex Should Borrow

| External work | Useful idea | Complex adoption | Anti-bloat boundary |
| --- | --- | --- | --- |
| Anthropic Building Effective Agents | Prefer simple, composable patterns; increase autonomy only when needed; use routing, parallelization, orchestrator-workers, evaluator-optimizer when the task justifies it | Put `complex_behavior_kernel` above the gate list; choose single-thread / subagent / reviewer / route-back by uncertainty and side effect | Do not add orchestration just because a framework exists |
| Anthropic agent evals | Agent quality needs task cases, graders, transcript/tool checks, and regression tests, not only final-answer review | Add `docs/behavior_regression_cases_20260702.json`, `docs/behavior_transcript_review_rules_20260702.json`, `tools/check_behavior_regression_pack.py`, and `tools/review_behavior_transcript.py` as the first behavior-regression and transcript-review layer | This is not yet a full LLM benchmark; marker review catches obvious omissions and forbidden moves, while human review still judges quality |
| LangGraph state and interrupts | Durable state plus explicit human interruption for actions that require external input or approval | Strengthen current state/next_route records and `decision_rights_matrix` for ask-user/manual-action boundaries | Do not require LangGraph runtime; borrow the persistence and interrupt concept |
| OpenAI Agents SDK guardrails, handoffs, tracing | Guardrails define what must be blocked or escalated; handoffs require clear ownership; tracing makes routes inspectable | Keep account/API/external-write boundaries explicit; use subagent/thread contracts; record route summaries and rollback routes | Do not expose hidden reasoning; trace decisions in recoverable summaries |
| DSPy / GEPA | Prompts and pipelines can be optimized against examples and metrics, not hand-written once forever | Treat `copy_ready_prompt`, `round_execution_prompt`, and behavior cases as optimizable artifacts | Do not install DSPy or create optimization jobs until a real project needs it |
| Reflexion and Self-Refine | Feedback should become reusable memory that improves the next trial | Convert repeated failures into behavior cases, golden examples, or protocol deltas | Avoid vague self-critique; only write back lessons that change future behavior |
| Tree of Thoughts / Graph of Thoughts | Open-ended reasoning should preserve multiple candidate paths and backtracking before convergence | Keep model-discovery candidate frameworks, argument maps, and discriminating probes | Do not force multi-path search on fixed evidence-fill tasks |

## The Seven-Step Compression Rule

When adding, keeping, deleting, or renaming any Complex mechanism, ask which behavior it improves:

1. Restore true state.
2. Classify project nature and convergence.
3. Assign decision rights and guardrails.
4. Pick one highest-leverage question.
5. Run the lightest useful validation or execution.
6. Deliver to the right audience.
7. Leave next-route recovery.

If a mechanism cannot improve at least one step, it should not be in the core protocol. It may belong in an example, external mapping, history note, or backlog.

## What This Changes Now

- New agents can start from the behavior kernel rather than memorizing every gate.
- Regression now has a behavior-case pack and transcript review rules, not only recovery-chain structure checks.
- Runtime Kit has golden examples for evidence-fill, model-discovery, and independent-review tasks.
- Future edits can delete, merge, or demote mechanisms using the same first-principles test.

## Sources

- Anthropic, "Building effective agents": https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, "Demystifying evals for AI agents": https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- LangGraph interrupts: https://docs.langchain.com/oss/python/langgraph/interrupts
- OpenAI Agents SDK guide: https://developers.openai.com/api/docs/guides/agents
- OpenAI Agents SDK guardrails: https://openai.github.io/openai-agents-python/guardrails/
- OpenAI Agents SDK handoffs: https://openai.github.io/openai-agents-python/handoffs/
- OpenAI Agents SDK tracing: https://openai.github.io/openai-agents-python/tracing/
- DSPy: https://dspy.ai/
- DSPy GEPA optimization: https://dspy.ai/getting-started/gepa-optimization/
- Reflexion: https://arxiv.org/abs/2303.11366
- Self-Refine: https://arxiv.org/abs/2303.17651
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
