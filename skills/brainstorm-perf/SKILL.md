---
name: brainstorm-perf
description: "Trigger: test a brainstorm performance hypothesis, verify a bottleneck. Measure an existing idea with consent and isolation."
license: Apache-2.0
metadata:
  author: "AlvarezTDV"
  version: "1.0.0"
---

## Activation Contract
Use only for a specific existing brainstorm idea and an authorized performance hypothesis. Depend on the installed brainstorm contract; do not invent ideas or silently become a general test runner.

## Hard Rules
- Read [safety and consent](references/safety-and-consent.md) before copying data, launching processes or accessing services. No established isolation means no execution.
- Never change original code, configuration or data. Keep test artifacts inside the idea's original session `<ID>-test/` and preserve privacy.
- Require explicit idea-specific execution consent. Service destination, operation and credential/session need separate scope; read permission never authorizes writes.
- Use the session language. Do not invent timings, user motives, cleanup success or another root cause when evidence is missing.

## Decision Gates
| Condition | Action |
|---|---|
| Missing primary contract or existing idea | Explain and stop; never create a replacement idea. |
| Missing consent, isolation or tooling | Do not execute; explain the missing condition and safe alternatives. |
| Service access denied | Do not connect; use only authorized local evidence or report inconclusive. |
| Potential writes or persistent traces | Disclose before execution and request the required additional authorization. |

## Execution Steps
1. Resolve brainstorm and read its idea contract/decision workflow. Read the idea's acceptance criteria, original session and [measurement workflow](references/measurement-workflow.md).
2. Prepare a tailored, reproducible plan from [plan template](assets/test-plan.template.md); explain data, metrics, limits, effects and cleanup before consent.
3. After scoped consent, verify safety controls, snapshot relevant original state, then measure within the authorized bounds. Stop on unexpected access, mutations or resource use.
4. Verify original-state integrity and cleanup; preserve sanitized evidence and report residuals or uncertainty.
5. Use [results template](assets/test-results.template.md) to distinguish confirmed, not observed under tested conditions and inconclusive. Link results from the existing idea without changing its decision or implementing a fix.

## Output Contract
Create plan, scripts and sanitized evidence/results only under the resolved original-session `<ID>-test/`. Preserve earlier runs and record limitations. Report the conclusion and what it does not prove.

## References
Use the linked local resources and the installed primary contract. Instructions are not a sandbox; verify actual runtime controls rather than asserting safety from this document.
