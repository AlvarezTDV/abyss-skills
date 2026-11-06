# Evidence-based project analysis

1. Resolve the explicitly selected project root, not an enclosing repository. Read README when present, relevant documentation, representative code and available read-only Git history. Inspect enough to understand behavior, not every file indiscriminately.
2. List functional capabilities and their current boundaries with path/symbol evidence. Do not count every method as a capability. Exclude generated brainstorming artifacts from claims about implemented project behavior.
3. Identify domain, users, project maturity and actual constraints. Proposals must be a natural progression from these facts, including maintenance. Do not invent user demand or add architecture for hypothetical scale.
4. Inspect existing ideas and implementation evidence before generating new ones. Match outcomes and scope, not merely titles. A renamed rejected or implemented idea is still a duplicate; link an existing proposed or accepted idea instead of recreating it.

## Limits and categories

- Offer at most 3 improvements per existing functional capability, across all categories combined; at most 5 new-capability ideas for the entire session. Prefer fewer strong ideas, including zero, over filling quotas.
- A specific slow or quadratic function may justify a performance hypothesis. Associate it with its owning capability and its improvement allowance; this is not an unlimited extra bucket. Complexity analysis alone does not prove a real bottleneck.
- Use one primary category: feature (new functionality), fix (improvement to an existing function, not concrete bug repair), ux, performance or dx. For games, gameplay may replace ux. The F/M identity tracks new versus improved capability, independently of category.
- Concrete bugs and security issues belong to an audit. Mention an encountered concern briefly as out of scope without expanding into an audit or exploiting it.

## Evaluation

Every candidate needs a grounded problem/opportunity, why it matters now, impact, S/M/L effort with reason, risks and tangible scope. Name relevant files, modules, functions and integration points when known; mark proposed names as proposed and unknown paths as unknown. Estimate scope, not fictional precision or unsupported schedules.
Provide a general implementation outline, optional proposed functions/libraries with compatibility evidence, and observable acceptance criteria paired with ways to test them. Do not implement the outline.

| Feasibility | Required evidence |
|---|---|
| viable | Integration points exist, necessary libraries are compatible, and no visible blocker remains. |
| partly viable | Concrete prerequisites are missing; list each dependency, data layer, test gap or compatibility check. |
| not viable | Most foundations are absent or major structural rebuilding is required; explain why. |

Unknown compatibility is not evidence of viability. Keep not viable items out of main candidates; retain one only for a concrete user-relevant reason, clearly separated and without manufacturing a recommendation. Translate feasibility labels to the session language, including medio viable in Spanish.

## Missing evidence

If README, history or tools are missing, reconstruct the safe portion from available sources and document limitations. Do not install dependencies, change settings, contact services or assume missing evidence proves implementation. Ask only if a missing fact prevents a consequential decision; do not block unrelated analysis.
