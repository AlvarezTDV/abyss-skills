# Interactive, traceable decisions

## Read before acting

Read the idea, its history, existing reasons and the user's current instruction. A chat decision and a manual edit have equal authority. A new explicit user instruction can revise an earlier decision; automated inference cannot. Compare the visible status with recorded history to recognize manual edits. If accepted/rejected status has no recorded origin, treat it conservatively as a human decision.

Keep ID/title, status, context, rationale, consequences, accepted debt/possible problems, decision date and concise history in the existing idea file. Do not require a separate ADR, another ID or an exhaustive questionnaire.

## Help formulate the reason

- If a reason is absent or vague ("better", "too complex", "not useful"), ask one focused question about the actual problem, constraint or trade-off and wait. Do not ask again when a sufficient reason was already supplied.
- Explain the relevant concepts and consequences using available evidence. Offer a concise formulation based on what the user said; request confirmation when the formulation adds meaning. Do not invent motives, demand quantitative proof for a legitimate preference or overrule a decision merely because you disagree.
- A useful rationale states the decision, project context and accepted trade-off. Record uncertainty honestly. Context/consequences may be drafted from verified facts; label predictions, and do not present a proposed debt as user-accepted until confirmed.
- When a manual decision lacks a reason, retain its status and deduplicate it immediately; ask for the reason rather than reverting it or quietly substituting an explanation. Preserve a sufficient existing reason and date.

## State and evidence

| Situation | Action |
|---|---|
| Proposed, no protected human decision, full implementation proven | May mark implemented automatically; record evidence/date and that historical motivation is unknown if absent. Do not invent a past user acceptance reason. |
| Human accepted status; implementation found | Add evidence/date without overwriting the explicit status. A user-authorized accepted-to-implemented transition keeps the same rationale and decision date. |
| Rejected but apparently implemented | Keep rejected. Present the evidence and ask why it was reconsidered; help formulate a reason, then change only with confirmation. Retain the prior rejection and reason in history. |
| Partial or ambiguous implementation | Record partial/uncertain evidence; do not mark implemented. |
| User explicitly changes a decision | Record the new rationale/date, preserve previous history, then synchronize derived views. |

Assess implementation against all observable acceptance criteria, not a matching symbol, commit title or file existence. Inspect relevant code and available read-only Git history; use existing test evidence only if actually applicable. Do not execute project commands or contact services just to infer status; performance execution belongs to consented perf. Missing history alone need not invalidate conclusive code evidence, but disclose it.

Record each transition once with date, origin (chat/manual/automatic), prior/new status and confirmed reason/evidence. Preserve substantive manual text. For a changed acceptance rationale, record reconsideration; do not silently replace it. Synchronize index and affected summaries after meaningful changes; do not generate a new session for routine follow or renumber an existing idea.
