# Project brainstorming without changing the project

Use **brainstorm** to understand the full project and propose its next natural steps. Use its companions only when helpful; follow is enabled by default when available, perf requires explicit consent for a concrete idea.

## Workflow

1. Select the project root. Read its README when present, other useful documentation, representative code and available read-only history. List functional capabilities, evidence and gaps before proposing.
2. Reconcile prior individual idea documents, including manual edits. Skip duplicates in every state; preserve rejected reasons and implementation evidence. Missing follow never disables this step.
3. Generate fewer, better ideas: at most three improvements per existing capability across categories, and five new-capability ideas in total. These are ceilings, not quotas.
4. Write a dated session, individual details, summary and global index. The individual document remains authoritative.
5. Help the user decide through one focused question at a time. A reason must identify the actual context and trade-off; a legitimate product preference need not have fabricated metrics.
6. Offer perf only if measurement would resolve a meaningful hypothesis. A refusal does not block brainstorming or acceptance of other ideas.

## Requests

- “Explore this project and propose its natural next steps.”
- “Accept F-01 because our users need exports for offline reporting.”
- “Reject M-02.” → ask for the missing reason, then help make it specific.
- “Check whether M-03 is implemented.” → inspect evidence, not just names or commit messages.
- “Test the suspected bottleneck in M-04.” → identify the idea, disclose the plan, confirm consent, then use perf if safe isolation exists.

These are intent examples, not commands guaranteed by every CLI. The real conversation and generated files use the current session language.

## Decisions and implementation

Status values represent proposed, accepted, rejected or implemented. Spanish equivalents include propuesta, aceptada, descartada and implementada. Grammar variants and other languages are interpreted by meaning, not assumed to be new states.
Edit the idea's visible status and its rationale, or decide by chat. You need not edit the index, metadata or history. An explicit human decision is never silently overwritten by detection.
An accepted idea may gain implementation evidence without changing its rationale or its protected status. If the user authorizes the accepted-to-implemented transition, preserve the reason and decision date; add an implementation date.
If a rejected idea appears implemented, retain rejection, show evidence and ask why it was reconsidered. Record the user's explanation and preserve the previous decision before changing status.

## Performance and privacy

Use representative project data without changing originals. A function's quadratic complexity alone does not prove it dominates a realistic workload. Investigate the relevant end-to-end flow, repeat measurements and document conditions.
Use isolated working copies, constrained writes and disabled external access unless explicitly authorized. A directory name is not a sandbox. Do not load original startup hooks or execute arbitrary project code until isolation is established.
Service access is read-only by default and requires exact destination, operation and credential/session authorization. Writes need separate permission in a separate test environment. Disclose costs, cleanup limits and unavoidable logs; do not erase audit records. No safe isolation means no execution, not permission to improvise.

## Limits of the collection

These are agent instructions, not an enforcement engine or continuously running watcher. Follow acts during an authorized invocation; it does not install background monitoring. Filesystem restrictions, credentials and isolation must be supported and checked in the active runtime.
Missing README, Git, benchmark tools or libraries do not stop unrelated safe analysis. Report missing proof, do not automatically install dependencies, and use an inconclusive measurement result when appropriate. Structural tests do not establish cross-client runtime compatibility.
