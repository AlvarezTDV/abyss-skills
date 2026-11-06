---
name: brainstorm-follow
description: "Trigger: follow brainstorm ideas, accept or reject an idea, check implementation. Reconcile existing decisions and evidence."
license: Apache-2.0
metadata:
  author: "AlvarezTDV"
  version: "1.0.0"
---

## Activation Contract
Use for existing brainstorm ideas and authorized decision tracking. This optional companion depends on brainstorm; locate its installed resources by skill name. Do not create proposals or run continuously in the background.

## Hard Rules
- Write only inside the selected project's `brainstorming/`. Never modify project code, configuration, original data or Git state.
- Use the session language. Preserve human reasons, explicit manual decisions and the original idea ID/session.
- Load brainstorm's shared idea contract and decision workflow before updates. If the dependency cannot be found, explain the limitation; the primary skill remains usable without this companion.
- Ask one focused question and wait when a decision reason or consequential interpretation is unresolved. Do not infer user motives or run project tests/services.

## Decision Gates
| Condition | Action |
|---|---|
| User disabled follow | Do not invoke automatically; primary still handles core states. |
| No prior ideas | Explain that brainstorm must create ideas first. |
| Manual state conflicts with an index | Preserve the detail document and reconcile derived views. |
| Rejected idea appears implemented | Keep its decision; ask about reconsideration. |

## Execution Steps
1. Read [follow workflow](references/follow-workflow.md) and the primary resources it names.
2. Identify target ideas from explicit IDs, paths or unambiguous titles. Read details/history before source evidence and state changes.
3. Apply explicit chat decisions or recognize manual edits. Help formulate missing reasons, never fabricate them.
4. Inspect implementation against acceptance criteria using available read-only evidence; record limitations and protect human decisions.
5. Synchronize affected summaries/index, read back changes and report outcomes without generating a new session or ideas.

## Output Contract
Update existing idea documents and derived views only. Reply briefly with changed IDs, evidence, unresolved questions and limitations. Use the workflow's response shape; do not create a separate tracking report by default.

## References
The local workflow identifies exact shared resources to load from brainstorm. Missing optional follow must never disable the primary skill's deduplication or manual-state recognition.
