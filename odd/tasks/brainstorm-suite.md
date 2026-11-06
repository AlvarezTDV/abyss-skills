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

## Tasks
- T1 [S1-S7,S11-S12] inline (new understood content, no writer trigger); verified; foundation 6a44b96 and standalone core d023d7b; five focused checks and ten standalone-snapshot checks pass; native medium/under_budget slice pending.
- T2 [S6-S8,S11] inline (depends on T1 contract); implemented, focused check passes; optional follow workflow, decision reconciliation and checks; full-suite gate T4; commit pending.
- T3 [S8-S12] inline (depends on T1 contract); implemented, two focused checks pass; perf workflow, safety/consent, templates and checks; full-suite and independent verification gate T4; commit pending. Risk: item 2 (isolation, credentials and service-access instructions).
- T4 [S1-S12] inline coordination; structural and independent checks verified, delivery needs decision; full suite passes 13 tests and the S11 blocker is resolved. Baseline 7819b29. Live-client enforcement/benchmark probes not executed. Chain strategy, work-unit commits and native candidate review remain pending.

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
