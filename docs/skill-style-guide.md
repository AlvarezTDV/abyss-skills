# Skill authoring standard

Use this repository's conventions in addition to the Agent Skills format.

## Package

- Place each skill at `skills/<name>/SKILL.md`. Keep names lowercase with hyphens.
- Require `name`, a quoted single-line `description`, `license: Apache-2.0`, and string `metadata.author: "AlvarezTDV"` / `metadata.version` fields.
- Start descriptions with `Trigger:` and explain both intent and use; target 160 characters, maximum 250.
- Do not invent universal `depends_on`, permission or activation fields. Express dependencies, consent and fallback in instructions; client support varies.

## Instructions

Use these sections in order: Activation Contract, Hard Rules, Decision Gates, Execution Steps, Output Contract, References.
Target 180–450 tokens in the body; recommended maximum 700, hard maximum 1000. Move detail into local references rather than compressing or omitting safety rules.
Write imperative English. Templates are English source material; the agent translates labels, explanatory text and state values for session-language output.

## Resources and ownership

- Use `references/` for procedures and `assets/` for templates. Add executable scripts only for a demonstrated need, not speculative scaffolding.
- Link directly to local resources; preserve their directory layout. Shared core contracts belong to brainstorm. Companions discover its installed root without assuming sibling paths or a particular client.
- Do not duplicate authoritative status in YAML. Keep state, decision and history inside the individual idea document; derived views link back to it.
- Root LICENSE/NOTICE cover repository distributions. Include them when packaging selected directories separately.

## Verification

Run `python -B -m unittest discover -s tests -v` and `git diff --check`.
Tests intentionally validate only the small YAML subset this collection uses; they are not a general YAML parser or evidence that a model follows every instruction.
Use `tests/scenarios.md` for fresh-agent runtime probes. Report observed behavior, not assumed conformance; never use real credentials or production services in repository tests.
