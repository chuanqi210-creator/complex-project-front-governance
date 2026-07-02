# Question Template

Use this file to avoid asking the user low-value questions. Ask only when the answer changes direction, evidence threshold, delivery form, permissions, or high-cost execution.

## Complex Setup Question Card

Use `complex_setup_question_card` when a project starts with "use Complex", "按 Complex 推进", "读取 Complex", or a similar request and the important operating choices are not yet explicit.

Ask briefly, or state safe defaults if the task is low risk:

- Delivery: Who is the output for, and is it human-readable, machine-recovery, teacher/expert-facing, third-party-facing, or mixed?
- Capabilities: May the agent use web, browser, databases, accounts, APIs, skills, plugins, or external methods? Which require explicit authorization?
- Collaboration: Should the main thread handle this first, or should subagents, parallel checks, or long-running threads be considered?
- Cadence: Should this be one round with a clear next route, or continuous cadence until the user stops it?
- Project nature: Is the model, formula, research frame, or evidence table already fixed, or should the agent first protect divergent model discovery?
- Autonomy: Should the agent use "strong autonomy + guardrails" for reversible project details, or ask before each strategic adjustment?
- Boundaries: Are there privacy, payment, publishing, account, evidence, or real-world action limits?

Safe default if unanswered:

- Main thread first.
- One round first, then leave `next_route`.
- Read-only local and public sources only.
- No external account, payment, publishing, or irreversible action.
- Strong autonomy + guardrails: the agent may decide reversible, low-side-effect project details, but must ask before goal changes, external authorization, irreversible actions, delivery-public-voice changes, or high-risk claims.
- Human-readable delivery that a third party can understand.

User-visible trigger guide:

> You can say these steering words to guide the agent: "开启 Plan 模式 / 先规划再执行", "模型发现型 / 先发散研究框架 / 不要早收敛", "证据填充型 / 模型和指标已定", "连续节拍 / 总规划别丢 / 每轮 prompt 重水化", "每拍窄 Goal / 自动进入下一拍 / 不等我说继续", "少问我 / 能推进就继续 / 我给目录你自己读", "自动启用合适子代理 / 只读审核线程 / 每轮清上下文", "独立评审 / 客观审查 / 避免上下文污染", "外部工具 / 账号 / API / skill", "目标仓库边界对账 / 真人工边界 / 剩余可自动小拍", "编排预检 / Goal mode / 长期线程 / automation / Beat Router / stop condition", and "只要人看版".
> You can also say "先设计提示词/prompt", "多线程/子代理", "完整扫描 Complex", or "先做问题-观点-论据图" when those operating choices matter.
> You can also say "强自治+护栏", "让 AI 自行判断细节", "动态推进", "只在高风险时问我", or "AI 自己调路线，但保留理由" when you want the agent to handle route, depth, tool, and collaboration details unless a real boundary is crossed.
> In continuous cadence, a clear queued `next_route` should auto-execute when low-risk and reversible. The agent should not ask the user to say "continue" unless a real authorization, external-write, irreversible-action, high-risk, turn, or tool boundary exists. Continuous cadence also means per-beat narrow goals, round prompt rehydration, and automatic start of the next queued beat when safe.
> Independent review means context separation every review beat. If clean context, a read-only audit lane, or a fact-ledger-only packet is unavailable, label the result as same-session diagnostic review instead of independent review.
> In downstream repositories, steering words must be reconciled with local project boundaries. A true external-input/manual-action gate blocks only unsafe or impossible work; the agent should still run allowed residual beats before pausing.
> Plan mode must design an orchestration contract when continuous cadence, Goal mode, long-running threads, subagents, automation, or independent review are requested. Subagents are short-lived workers; user-visible long-running Codex threads and automations are different resources with different authorization boundaries.
> When scanning Complex from another project, resolve the authoritative Complex source separately from the target project. Prefer the user-provided path, then `/Users/chuchenqidawang/Documents/complex-project-front-governance`, then sibling Complex repository names. A target repo with no `Complex` directory does not mean Complex is unavailable.

## Complex Prompt Bootstrap Card

Use `complex_prompt_bootstrap_gate` when the user wants to scan Complex first, design a project prompt, and only then execute the project.

Ask briefly, or state safe defaults if the task is low risk:

- Project: What is the project goal, and what material should the prompt assume exists?
- Execution: Should the generated prompt be used in this thread after confirmation, or copied into a new project/thread?
- Plan mode: If the current interface supports Plan mode, should the agent first remind the user to enable it for protocol scan, prompt design, and plan generation before execution?
- Cadence: Should the prompt default to one round with `next_route`, or continuous cadence with scheduled refresh?
- Project nature: Should the prompt treat this as evidence filling, model discovery, mixed discovery-to-evidence, or execution delivery?
- Steering words: Which of these should be preserved in the generated prompt: model discovery, evidence fill, continuous cadence, fewer questions, independent review, external tools, human-readable only?
- Capabilities: Which tools, browser paths, accounts, APIs, skills, plugins, or subagents may the prompt authorize or only list as candidates?
- Autonomy: Should the prompt default to strong autonomy with guardrails, and which decisions must still ask the user?
- Delivery: Who will read the result, and should the prompt enforce human-readable, machine-recovery, teacher/expert-facing, third-party-facing, or mixed delivery?

Safe default if unanswered:

- Design only first; do not execute until the user confirms.
- Main thread first, one round first, then leave `next_route`.
- Read-only local and public sources only.
- No account, API write, payment, publishing, or irreversible action.
- Strong autonomy + guardrails for reversible project details; ask before goal, authorization, irreversible, delivery-public-voice, or high-risk-claim changes.
- Human-readable delivery that a third party can understand.

Required output before execution:

- `protocol_scan_summary`
- `startup_questions_or_defaults`
- `project_prompt_design_rationale`
- `copy_ready_prompt`
- `execution_bridge`

## Question Candidate

- Question:
- Why it matters:
- What happens if unanswered:
- Maximum rework risk:

## Type

- Goal or scope:
- Evidence standard:
- Tool or account permission:
- Collaboration structure:
- Delivery audience:
- Style or granularity:
- External action or irreversible cost:

## Recommended Default

- Default if user does not answer:
- Why this default is safe:
- What will be recorded as an assumption:

## Final Asked Question

Ask one concise question:

>

## Answer and Plan Patch

- User answer:
- Plan patch:
- Main goal changed: yes / no
