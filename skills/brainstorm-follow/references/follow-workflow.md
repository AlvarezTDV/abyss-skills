# Follow existing ideas

## Dependency and scope

Resolve the installed brainstorm package using the client's skill registry/discovery mechanism or an explicitly supplied location. Read its `references/idea-contract.md` and `references/decision-workflow.md`, not its entire generation workflow. Do not assume a sibling directory, fetch a dependency or rewrite client configuration. If unavailable, report the missing dependency and leave files unchanged.
Follow is enabled by default when installed and not explicitly disabled. Its autonomy is limited to an authorized invocation: no background watcher, scheduled job or automatic service access. Brainstorm must still recognize manual edits, synchronize its own derived outputs and avoid duplicates without follow. Do not generate new ideas.

## Reconcile

1. Resolve the selected project and existing idea files with the shared path-containment checks. With no ideas, direct the user to brainstorm without creating a new session.
2. Resolve the user's ID/path/title to one idea; ambiguous or conflicting identities require a question. Read the individual document, its decision history and the current instruction. Do not trust a stale derived index row over manual text.
3. Record an explicit chat decision, or recognize a changed manual state and preserve its rationale. If the user already explained the reason, do not ask again. If missing/vague, retain the chosen state, ask one focused question and wait; protect that state from duplicate proposals while awaiting the answer.
4. Use the primary decision workflow for all status transitions, wording assistance, acceptance-to-implementation handling and rejected-but-implemented reconsideration. It owns the definitions; do not maintain a divergent state machine here.
5. For an implementation check, compare actual behavior and all acceptance criteria with code and available read-only Git history. Names, TODOs and commit messages alone are not proof. Do not execute project commands, contact services or install tools. Partial evidence stays partial; note exactly what cannot be established.
6. Update the idea's evidence/history only when warranted. Synchronize the global index and affected original-session summaries as derived views. Preserve stable IDs, dates and unrelated manual prose; no silent rewrites or new sessions.
7. Read back updated fields/links and report whether each requested action was completed, awaiting user input or unsupported by evidence. Missing Git does not by itself block conclusive code inspection; missing proof never becomes invented certainty.

## Response shape

Translate and keep this in chat, not a new report file:

```text
Tracking updates:
- <ID>: <recognized decision/change and evidence>.
Unchanged:
- <ID>: <reason, such as partial implementation>.
Needs your decision:
- <one concrete unresolved question, only when needed>.
Limitations:
- <unavailable evidence or none identified>.
```

If a question is required, present only the next focused question and wait; do not continue with dependent updates or a batch of questions. On the next invocation, resume from the authoritative document and the user's answer, not a guessed earlier intention.
