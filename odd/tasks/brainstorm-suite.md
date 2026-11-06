# Brainstorm skill suite
Objective: implement the agreed portable skills; author AlvarezTDV; branch feat/brainstorm-suite.
Route: inline; delivery ask-on-risk; chain feature-branch-chain (chosen); forecast ~900 authored lines plus the standard license. Runner: python -B -m unittest discover -s tests -v.

## Specs
- S1: "Para empezar, debe funcionar para cualquier CLI o programa que permita estar dentro de un proyecto, como opencode, no tiene nada que ver que solo sea claude code." Inspect project type, README and functional capabilities before proposing; degrade honestly when sources/tools are absent.
- S2: "Si, no debe modificar codigo, configuracion ni tocar nada del proyecto, solo lo de brainstorming." Runtime writes stay inside the selected project's brainstorming directory; no implementation of suggestions.
- S3: "Hasta 3 ideas por función o módulo existente." "Hasta 5 ideas para funciones o comportamientos nuevos." "Prioriza calidad sobre cantidad." The unit is a functional capability; technical functions qualify only for relevant bottleneck hypotheses. Proposals must be natural domain evolution, not speculative scaling.
- S4: "Carpeta brainstorming/ con una subcarpeta por sesión: YYYY-MM-DD-brainstorming. Si ya existe una de ese día, se agrega sufijo (-2, -3)." "summary.md" and one named Markdown file per idea; global index.md with F-01/M-01 IDs that are never reused. Categories feature/fix/ux/performance/dx; gameplay may replace ux for games.
- S5: "Impacto." "Esfuerzo estimado: S, M o L." "Complejidad tangible: archivos, módulos y funciones involucradas, con nombres cuando sea posible, sin depender del lenguaje." "Viabilidad: viable, medio viable o no viable, con lo que falta si aplica." "Riesgos." Include problem, justification, implementation outline, possible functions/libraries, acceptance and testing. Fix means improvement, not a bug/security audit. Exclude nonviable main candidates; retain only for a concrete reason.
- S6: "tambien que lo pueda hacer yo manualmente, yo manualmente escribiria dentro del md que está aceptada o descartada (dejar un espacio para poner si está aceptada o descartada para hacerlo más sencillo para mi)" Individual documents are authoritative; recognize manual edits without follow, avoid repeated ideas, synchronize derived summaries/index, and preserve human decisions and reasons.
- S7: "quiero que la justificación (motivo de descarte/motivo de aceptación) sea como una versión distinta al ADR" Include ID/title, state, context, rationale, consequences, accepted debt/problems and date. Ask one focused question if a reason is missing/vague; assist without inventing motives. "implementado es igual a aceptado, no hay que cambiar la justificacion solo porque paso de aceptado a implementado" Preserve rationale; if a rejected idea is implemented, ask about reconsideration before changing the decision and retain history.
- S8: "brainstorm debe funcionar por si sola, las otras 2 si o sí dependen de la primera, serían como opciones para el usuario." Follow is optional and enabled when available unless disabled; absence never blocks core state handling. Perf is called only after asking about a specific hypothesis and obtaining consent.
- S9: "brainstorm/2026-10-30-brainstorm/\"idea\"-test. algo así" Final canonical directory is brainstorming; locate tests in the idea's original session/<ID>-test. "que haga tests personalizados según el tipo de problema." Use representative project data read-only, isolated copies, no changes to originals, no disclosure of sensitive data. Distinguish confirmed/not observed under tested conditions/inconclusive; missing evidence never proves another cause.
- S10: "el usuario debe dar el veredicto final, que permita o no el acceso a otros servicios" No ambient credentials or automatic remote access. Disclose exact destination, operations/session, risks, costs, cleanup and residuals before consent. Read access does not authorize writes; temporary writes require separate consent and a separate test environment. Preserve audit logs, verify cleanup, and never promise zero traces. If isolation cannot be established, do not execute.
- S11: "Los documentos generados si, deben estar en el idioma de la sesión" "que esté escrita en inglés" "Prefiero el mixto del comienzo" Skill instructions/templates are English; render session-language documents with fixed sections, concise prose and comparison tables; never duplicate authoritative state in YAML.
- S12: "Prefiero la verdad apache 2.0" "Si,usemos AlvarezTDV para el autor y avisos, ahora haz todo lo contemplado." One root LICENSE, Apache-2.0 metadata, AlvarezTDV attribution; standalone distributions must carry license/notices. Preserve /.atl/ ignore. Deliver repository guidance and honest structural/scenario checks, not claims of cross-client runtime certification.
- S13: "Integrar brainstorm-perf al contrato del paquete"; "Corre pytest y git diff --check"; "Trackear todo en Git (cero untracked)"; "inicia una revisión nativa nueva de Gentle AI desde cero sobre el árbol actual con las 3 skills ya rastreadas en Git." Verify the existing perf implementation and package registrations, run the requested and repository checks, commit the complete package locally, and replace the old review only through a documented native archival operation. Do not manually delete authority or claim that archiving resolves findings. The user identifies R3-no-behavioral-contract-tests as refuted; verify the native record before adopting that classification.

## Tasks
- T1 [S1-S7,S11-S12] inline (new understood content, no writer trigger); complete; foundation 6a44b96 and standalone core d023d7b; five focused checks and ten standalone-snapshot checks pass; aggregate native review approved and acknowledged under T5.
- T2 [S6-S8,S11] inline (depends on T1 contract); complete; follow 93931bd; focused check and eleven exact-snapshot tests pass; aggregate native review approved and acknowledged under T5.
- T3 [S8-S13] inline (existing implementation and registrations understood; no writer trigger); complete in 7b7782b (201 authored changed lines); isolated pytest 13/13, unittest 13/13 and diff check pass; independent Risk item 2 validation found no blockers; native approval acknowledged under T5. Risk: item 2 (isolation, credentials and service-access instructions).
- T4 [S1-S12] inline coordination; complete at the explicitly documented instruction/structural level; independent checks and aggregate native review passed. Baseline 7819b29. Live-client enforcement/benchmark probes were not executed and are not certified. Chain strategy remains feature-branch-chain; publication needs separate authorization.
- T5 [S13] inline coordination (documented native archival binding verified); complete: old review natively archived with committed audit record, all three skills tracked, and new review-f34f20808c6b1e1f approved/acknowledged with authority burned. Candidate 09798bd includes all 25 package paths; no manual authority deletion or consumed-decline replay occurred. The missing-companion blocker did not recur; the sole new finding is a non-blocking runtime-scenario warning.

## Log
L1 — Original request, verbatim:
> Resumen de requisitos
>
> Alcance
>
> Se ejecuta en CLI (Claude Code), dentro del proyecto.
> Sirve para cualquier tipo de proyecto y es agnóstica al lenguaje y a las herramientas.
> Antes de proponer, identifica el tipo de proyecto, lee el README y lista las funciones existentes.
> Las ideas deben ser coherentes con el dominio del proyecto.
> Solo lectura: genera documentos y no modifica el código.
> Idioma: español.
>
> Cantidad
>
> Hasta 3 ideas por función o módulo existente.
> Hasta 5 ideas para funciones o comportamientos nuevos.
> Prioriza calidad sobre cantidad.
>
> Estructura de salida
>
> Carpeta brainstorming/ con una subcarpeta por sesión: YYYY-MM-DD-brainstorming. Si ya existe una de ese día, se agrega sufijo (-2, -3).
> summary.md: todas las ideas, categorizadas, con un resumen de por qué son candidatas.
> Un .md por idea, con el nombre asignado en el summary, que contiene el detalle.
> Categorías: feature (funcionalidad nueva), fix (mejora de una función existente), ux, performance y dx (experiencia del desarrollador). Para juegos, ux puede cambiar a gameplay.
>
> Memoria entre sesiones
>
> Índice global brainstorming/index.md con un ID por idea: F-01 para funciones nuevas y M-01 para mejoras.
> Cada idea tiene un estado: propuesta, aceptada, implementada o descartada.
> Las descartadas se registran con el motivo, para no volver a proponerlas.
> Las implementadas no se vuelven a proponer. Para detectarlas se revisan el código y el historial de git.
>
> Evaluación por idea
>
> Impacto.
> Esfuerzo estimado: S, M o L.
> Complejidad tangible: archivos, módulos y funciones involucradas, con nombres cuando sea posible, sin depender del lenguaje.
> Viabilidad: viable, medio viable o no viable, con lo que falta si aplica.
> Riesgos.
>
> Contenido de cada archivo de detalle
>
> Problema u oportunidad.
> Justificación: por qué hace falta.
> Pasos generales de implementación según el contexto del proyecto.
> Funciones propuestas y bibliotecas posibles, si aplican.
> Criterios de aceptación y forma de probarla.
>
> Alcance de fix
>
> Solo mejoras a funciones existentes. Bugs concretos y problemas de seguridad corresponden a una auditoría. Clasificación de viabilidad
> Viable: existen los puntos de integración, las bibliotecas necesarias son compatibles y no hay bloqueos visibles en el código.
> Medio viable: se puede hacer, pero faltan elementos concretos. La skill lista cuáles, por ejemplo una dependencia, una capa de datos o pruebas en el módulo afectado.
> No viable: faltan casi todos los elementos base. Implementarla exigiría construir una parte grande del proyecto desde cero o hacer cambios estructurales mayores. La skill explica el motivo. Quiero hacer una skill para hacer brainstorming para un proyecto, tengo ahí algunos requisitos, me gustaría que me ayudes a mejorarlo, hazme preguntas o si tienes dudas dimelo para aclararlo. Para empezar, debe funcionar para cualquier CLI o programa que permita estar dentro de un proyecto, como opencode, no tiene nada que ver que solo sea claude code. Aún no hagas la skill.

L2 — 2026-11-03 authorization, verbatim: "Si,usemos AlvarezTDV para el autor y avisos, ahora haz todo lo contemplado."
L3 — Current corrections are captured in S1-S12 and Engram requirements/decision-quality/fallback/output-templates/licensing; latest explicit decisions override L1's initial fixed Spanish/Claude scope.
L4 — Baseline: main at 7819b29; pre-existing untracked .gitignore contains /.atl/. Python 3.13.7 available; no skill code or test runner existed. Bundled skill-creator style guide applies until local guidance is created. No meaningful executable RED for prose; deterministic structural tests will observe missing-artifact RED before implementation. Native runtime behavior needs separate live-client evidence.
L5 — Resume request, verbatim: "Continua desde donde lo dejaste, elabora una revision para evitar que hayan errores debido a que la cuota se acabó."
L6 — Resume inspection confirmed only the task document and the previously authorized .gitignore exist as changes; no skill or tests had been written. UTF-8 readback confirms the task document is intact; PowerShell's default display decoding was misleading. Mirror was not saved before the interruption and is being established now.
L7 — Structural RED observed: 12 tests ran, 14 missing-artifact failures, exit 1. T1 focused run initially exposed absent category identifiers in the shared contract (six failures); corrected that contract and clarified create-versus-update safety. Recheck: five focused tests pass. Full metadata/companion suite remains for T4; no runtime certification claimed.
L8 — T2 focused check exposed that the primary used a shorthand companion name; corrected activation to exact brainstorm-follow/brainstorm-perf names. Recheck: follow test passes. T3 focused guardrail and evidence/template tests: two pass. All three skills and five templates now exist; standalone primary, localized output, protected human decisions and consent/isolation remain explicit.
L9 — Full suite: 12 tests pass; git diff --check and .atl ignore check pass. Independent verifier ses_e5c43ac3bffeR5aCwW1gNw3m6p reproduced one blocker: summary table header/data have seven cells but delimiter had eight. Added tests/test_template_tables.py; observed RED (8 != 7), corrected delimiter in one batch; recheck pending. Other S# met on instruction review, not live-client enforcement. No project scripts/services or credentials used. Native risk item 2 applies to perf's isolation and consent contract; no verifier tier inferred from model or size.
L10 — Correction GREEN: 13/13 tests pass. Independent recheck of the sole S11 blocker passes (seven cells throughout); parent spot-check of the reported regression command passes. Both owned temporary verifier copies were removed. No workspace scratch or cache remains; .atl stays ignored. No live-client enforcement, benchmark or service test was performed, and no such certification is claimed.
L11 — Delivery forecast is about 880 authored lines excluding the standard LICENSE (including tracking/tests/docs), above the review budget. Ask-on-risk requires one chain-strategy decision before the first commit; no commits, pushes or installation have occurred. Native review mode remains on; review of final work-unit candidates awaits their boundaries and separate native consent if due.
L12 — User chose "Integración por etapas (Recommended)": feature-branch-chain. Cache that strategy; only local commits are authorized, not pushes, PRs or installation. One slicing pass: foundation guidance/license; standalone core with its tests; follow with its tests; perf with its tests; final passive evidence closure. Stage cumulative README/catalog/tests per unit so each snapshot stands alone; preserve final workspace content. Review boundaries and observations will be recorded per commit before advancing.
L13 — Local units: foundation 6a44b96 (245 authored additions/deletions excluding 201-line standard LICENSE), core d023d7b (388 authored changed lines). Core's exact staged snapshot runs ten tests without companions; owned scratch removed. Native assessment from initial boundary 7819b29: medium/under_budget after both commits, no review started. Canonical inventories explicitly exclude later untracked units from committed-only assessment. The open slice must close before the named high-risk perf unit.
L14 — Follow unit 93931bd changes 85 authored lines and its exact staged snapshot passes eleven tests without perf; owned scratch removed. Assessment from 7819b29 remains medium/under_budget. Before committing the item-2 perf unit, close this pending slice through candidate-scoped native review (also explicitly requested by the user); no model verdict or global mode substitutes for native consent. Native selected lenses cover preservation of decisions/data, missing-resource failures, readable instructions and deterministic behavior.
L15 — 2026-11-05 user authorization and revised delivery request, verbatim:
> Como responsable humano del repositorio, autorizo e instruyo explícitamente resolver el bloqueo actual integrando la suite completa (brainstorm, brainstorm-follow y brainstorm-perf) bajo una nueva línea base limpia, en lugar de continuar la transacción review-7556343dd1757920 (ya que incluir brainstorm-perf excede el correction_budget de 200 líneas y el alcance congelado de genesis_paths, además de evitar el prompt de selección JSON de intended_untracked).
>
> Ejecuta exactamente estos pasos en orden:
>
> Integrar brainstorm-perf al contrato del paquete: Termina o verifica los archivos de skills/brainstorm-perf/ y regístrala formalmente en AGENTS.md (líneas 17-18), README.md (líneas 8-9), odd/tasks/brainstorm-suite.md y tests/test_skill_contracts.py (línea 9) para que el hallazgo R3-missing-performance-companion quede resuelto de raíz. (Ignora R3-no-behavioral-contract-tests, ya que fue refuted en el registro oficial).
>
> Ejecutar pruebas locales: Corre pytest y git diff --check para confirmar que todas las pruebas estructurales y de tablas pasan con las 3 skills incluidas.
>
> Trackear todo en Git (cero untracked): Haz git add (y el commit correspondiente si aplica) de todos los archivos de brainstorm-perf y de los archivos actualizados, asegurando que git status no deje archivos untracked pendientes que disparen el selector de intended_untracked.
>
> Reemplazar la transacción bloqueada por una revisión limpia: Con mi autorización expresa como usuario, elimina o archiva .git/gentle-ai/review-transactions/v2/review-7556343dd1757920 e inicia una revisión nativa nueva de Gentle AI desde cero sobre el árbol actual con las 3 skills ya rastreadas en Git.
L16 — Resume inspection: all five perf files and package registrations already exist in the preserved workspace. No skill behavior rewrite is needed; verification-only work reuses the recorded RED/GREEN evidence rather than inventing a new RED. The old native review did not include these files. The revised request authorizes their separate local integration commit before native archival; L14's old ordering is superseded, not its unresolved findings. Installed review abandon documents auditable quarantine with an exact eight-line v2 authorization binding; that binding and eligibility must be verified before any authority mutation. No manual deletion, new lineage or claim of native closure has occurred.
L17 — Step 2 observed: python -B -m pytest -p no:cacheprovider exits 1 (No module named pytest); python -B -m unittest discover -s tests -v passes all 13 tests; git diff --check exits 0. No cache was written. Following the user's required order, staging, commit, native archival and a fresh review have not run. Need explicit authorization for an isolated temporary pytest installation from public PyPI without credentials, or an explicit waiver accepting the repository's unittest runner instead. The prior native transaction and its unresolved findings remain preserved.
L18 — User selected "Instalar pytest aislado". A command-only worker installed pytest 9.2.0 in an external disposable venv using the explicitly authorized anonymous public package hosts; no project/global dependencies changed. Venv python -B -m pytest -p no:cacheprovider passes all 13 tests (exit 0), and the worker reports the unchanged workspace inventory. The earlier missing-module failure is resolved for this temporary verification environment, not hidden or claimed fixed globally. Native archival and findings remain pending.
L19 — Parent pytest spot check passes 13/13. Independent Risk item 2 verifier checked the full specification in a fresh external scratch snapshot: no isolation/consent/credential blockers; pytest and unittest both pass 13/13. Workspace hashes and inventory were unchanged. The verifier's optional extra static assertion was not a blocker or a runtime security test. Runtime enforcement remains unverified. The perf unit contains the five perf files, package catalog entries, structural tests and this tracking update; its rollback is that unit, not the independent core/follow commits. Native archival remains pending and must preserve the discarded findings in its audit record.
L20 — Integration commit 7b7782b includes all nine intended files, 197 insertions and four deletions. Git status was clean with zero untracked paths. A bounded read-only map and parent spot check of the stored refuter confirmed R3-missing-performance-companion corroborated and R3-no-behavioral-contract-tests refuted; no other corroborated severe finding was recorded. The old genesis manifest omits perf and has a 200-line correction budget. These facts describe the old candidate, not validation of the new one.
L21 — With the user's explicit repository-owner authorization, documented native review abandon ran once with the exact eight-line LF-only v2 binding derived from plain native status: lineage review-7556343dd1757920, revision 861443a1485c2d2d51a86e231c37d68ec403a4e320843d212306ad8f7d9af889, original snapshot 4f74d11369cc469884b983b1febef4947a5ce6787a921a180479421f8fc21430, reason operator_disposition and actor opencode. Native result review-reclaim-record/v1 reports status committed, preserving review-state.json under the transaction quarantine and auditing four discarded lens results with findings_present true. No manual deletion, repair, approval, receipt, mode toggle or decline replay occurred. The revised user request selects a new aggregate review from baseline 7819b29 after all three skills are tracked; source normalization and this evidence update precede that new candidate freeze.
L22 — Pre-freeze evidence commit 09798bd leaves Git clean with zero untracked files. Native assessment of the complete package from 7819b29 reports high risk after explicit item 2 escalation, review_due high_risk, 25 paths and 1106 changed lines. Exact preflight includes all three skills and intended_untracked []; no selection JSON was requested. User selected exactly "Revisar este cambio" in the new candidate's consent UI. Its exact granted invocation ran once, creating review-f34f20808c6b1e1f for target 55177d28137ea87d5a449de307e7ea28f1ae890735f3abdd185f4cc6bb467a24, candidate tree 899bd7aeb557c915ca723a644d5958575d1da0ad. Four provider-issued perspectives ran as a foreground group; the last admitted result approved the candidate. No refuter or correction was requested. The sole finding R3-scenarios-not-verified is a non-blocking WARNING: structural tests are not observed live-client behavior. It does not reopen review or authorize further correction.
L23 — The exact provider-issued acknowledgement ran once and returned gentle-ai.review-acknowledged/v1, action acknowledged, consumed revision 260a4fa2d92f6c43a35fa04305463cf070efedc8f5258184248decbec1822764 and authority burned for the exact new lineage/target. Native lifecycle stops here. This subsequent passive log closure does not change the reviewed skill/test bytes or claim to be part of that frozen candidate. Publishing, installation and pull requests remain unperformed and require separate authorization. Build/typecheck are not applicable to this instruction/template package; live-client scenarios and performance measurements were not executed. The parent removed both owned external verification directories and verified their absence; no project or global Python dependencies were changed. A final diff confirms all reviewed package bytes remain unchanged, with only this passive task log differing from 09798bd.
