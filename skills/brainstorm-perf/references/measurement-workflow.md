# Investigate one performance hypothesis

1. Locate brainstorm's shared `references/idea-contract.md` and `references/decision-workflow.md`. Resolve one existing idea ID/path and its original session from the actual document location, not the latest folder or global index alone. If unavailable or ambiguous, stop and explain; never fabricate an idea to make the dependency fit.
2. Use `<original session>/<ID>-test/` for plan, custom scripts and results. Preserve earlier results and use a new run subdirectory for repeated investigations. Keep a link from the original idea; no new idea ID or automatic acceptance is created.
3. Define the hypothesis from the actual module/flow and inspect its implementation. Separate a slow isolated operation from a bottleneck in the end-to-end user flow. A quadratic algorithm on tiny input may be irrelevant; a cheap function called repeatedly may dominate. Do not infer a project bottleneck from an unrelated toy benchmark.
4. Select representative project data and realistic workloads, with a user-relevant criterion for problematic performance. Inspect code paths and environment effects without executing them yet. Choose metrics appropriate to the hypothesis: latency distribution, CPU, memory, allocations, query count or scaling with volume. List missing prerequisites instead of installing them.
5. Write a plan with named tools, environment, dataset characterization, warm-up policy when relevant, repetitions, multiple relevant volumes, expected noise, resource budgets and stopping conditions. Use stable conditions and record versions. Define what evidence would support or weaken the hypothesis before measuring. For requests that could alter data or services, apply the safety workflow first.
6. Present the plan, get the required consent, verify isolation and baseline original-state checks, then execute only the approved operations. Capture repeated observations, variation and errors; do not cherry-pick the fastest/slowest run. If representative execution is impossible, an extracted microbenchmark can support only its narrow local claim, not end-to-end impact.
7. Classify results using the table below. Explain contribution to the overall flow and uncertainties. An improvement is not demonstrated until a legitimate comparison exists; this skill does not implement fixes merely to produce one.
8. Verify original-state integrity and cleanup, then write sanitized results and link them from the idea. Updating technical evidence must not overwrite the human decision/rationale. Disclose if unavailable history or tooling limits reproduction. Ask only for the concrete missing decision; do not turn inconclusive evidence into endless testing.

| Conclusion | Meaning |
|---|---|
| confirmed | Repeated representative measurements support the defined performance hypothesis and relevant contribution to the measured flow. Scope the claim to those conditions. |
| not observed under tested conditions | Measurements did not show the hypothesized effect in this workload/environment; this does not prove universal absence. |
| inconclusive | Missing isolation, tools, data, access, reproducibility or excessive noise prevents a justified verdict. Name what is missing. |

No evidence for the hypothesis does not prove another cause. List alternative explanations only as hypotheses with their missing evidence. Report the actual commands, environment differences and evidence provenance without secrets. Do not label a static complexity estimate as a measured timing or assert that cleanup succeeded without checking it.
