# abyss-skills

Portable, project-aware Agent Skills by **AlvarezTDV**. Skill instructions are English; conversations and generated documents follow the session language.

## Skills

| Skill | Use it to | Requirement |
|---|---|---|
| [brainstorm](skills/brainstorm/SKILL.md) | Understand a project and propose natural, traceable improvements. | Standalone. |
| [brainstorm-follow](skills/brainstorm-follow/SKILL.md) | Reconcile decisions, manual edits and implementation evidence. | brainstorm and existing idea documents. |
| [brainstorm-perf](skills/brainstorm-perf/SKILL.md) | Investigate an authorized, idea-specific performance hypothesis. | brainstorm, an existing idea and explicit consent. |

## Use

1. Make the selected skill directories available through your client's supported skill-loading mechanism, preserving their resources. Companions also need the complete brainstorm directory; discover it by skill name, not a hard-coded home path.
2. Open the project you want to analyze and request brainstorming. If your client cannot discover skills, explicitly load the relevant `SKILL.md` and its referenced files.
3. Review `brainstorming/index.md` and the dated session. Decide by chat or by editing the idea's visible status and rationale.
4. Follow is enabled when available unless disabled. Perf is only offered for a relevant hypothesis and never runs without consent. Neither companion is necessary to generate ideas or respect existing decisions.

Cloning this repository does not automatically install skills in every client. No particular CLI, language, database, Git history or benchmark framework is required. Missing capabilities are reported rather than silently installed.

## Output and boundaries

Only the analyzed project's `brainstorming/` directory is writable during skill use. Code, configuration and original data stay unchanged. Performance tests are tailored to the problem, isolated and stored in the idea's original session as `<ID>-test/`; access to services requires separately scoped consent.

See the [workflow](docs/brainstorming-workflow.md) for states, privacy and examples of requests. The files in `assets/` are output templates, not suggestions to execute project code.

## Development

Follow [AGENTS.md](AGENTS.md) and the [style guide](docs/skill-style-guide.md). Run `python -B -m unittest discover -s tests -v` with Python 3.10 or later; tests use only the standard library. They check structure, references and required contract elements, **not** live-client compliance or performance behavior. [Scenario probes](tests/scenarios.md) describe the separate runtime checks.

## License and attribution

Copyright 2026 AlvarezTDV. Licensed under **Apache-2.0**; see [LICENSE](LICENSE) and [NOTICE](NOTICE). One root license covers this repository. Any separately distributed skill package must also carry the license and applicable notices; no permanent per-skill duplicates are needed. Preserve required notices when redistributing; no public credit is required for each execution. This license does not automatically relicense analyzed projects or every generated output; reproducing protected template content may carry its own obligations.
