"""Structural checks, not certification of an agent's runtime behavior."""

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("brainstorm", "brainstorm-follow", "brainstorm-perf")
SECTIONS = (
    "Activation Contract", "Hard Rules", "Decision Gates",
    "Execution Steps", "Output Contract", "References",
)


class SkillContracts(unittest.TestCase):
    def text(self, relative):
        path = ROOT / relative
        self.assertTrue(path.is_file(), f"Missing artifact: {relative}")
        content = path.read_text(encoding="utf-8")
        self.assertNotIn("\ufffd", content, f"Invalid text: {relative}")
        self.assertFalse(content.startswith("\ufeff"), f"Unexpected BOM: {relative}")
        return content

    def requires(self, relative, phrases):
        text = self.text(relative).casefold()
        for phrase in phrases:
            with self.subTest(file=relative, phrase=phrase):
                self.assertTrue(phrase.casefold() in text, f"Missing contract term: {phrase}")

    def test_skill_metadata_and_section_order(self):
        # Validate the intentionally small YAML subset used here, not arbitrary YAML.
        for name in SKILLS:
            with self.subTest(skill=name):
                text = self.text(f"skills/{name}/SKILL.md")
                match = re.fullmatch(r"---\n(.*?)\n---\n(.*)", text, re.S)
                self.assertIsNotNone(match, "Expected YAML frontmatter and Markdown")
                header, body = match.groups()
                self.assertIn(f"name: {name}\n", header + "\n")
                self.assertIn("license: Apache-2.0", header)
                self.assertRegex(header, r'(?m)^  author: "AlvarezTDV"$')
                self.assertRegex(header, r'(?m)^  version: "\d+\.\d+\.\d+"$')
                description = re.search(r'(?m)^description: (".*")$', header)
                self.assertIsNotNone(description)
                description = json.loads(description.group(1))
                self.assertTrue(description.startswith("Trigger:"))
                self.assertLessEqual(len(description), 250)
                actual = re.findall(r"^## (.+)$", body, re.M)
                self.assertEqual(actual, list(SECTIONS))
                self.assertLess(len(body.split()), 650, "Move details into references")
                self.assertNotIn("Keywords", body)

    def test_all_skills_are_present(self):
        self.assertEqual(
            sorted(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")),
            sorted(SKILLS),
        )

    def test_local_resource_links(self):
        self.assertTrue((ROOT / "skills").is_dir(), "Missing skill package")
        for name in SKILLS:
            root = ROOT / "skills" / name
            self.assertTrue(root.is_dir(), name)
            for path in root.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
                    if "{{" in target or target.startswith("#"):
                        continue
                    with self.subTest(path=path.relative_to(ROOT), target=target):
                        self.assertNotRegex(target, r"^[a-zA-Z]+:")
                        resolved = (path.parent / target.split("#", 1)[0]).resolve()
                        self.assertTrue(resolved.is_relative_to(root.resolve()))
                        self.assertTrue(resolved.is_file(), f"Broken reference: {target}")

    def test_core_analysis_and_limits(self):
        self.requires("skills/brainstorm/references/project-analysis.md", (
            "README", "functional capabilities", "at most 3", "at most 5",
            "natural", "quadratic", "audit", "partly viable", "not viable",
            "missing", "compatible", "do not install",
        ))

    def test_identity_and_output_contract(self):
        self.requires("skills/brainstorm/references/idea-contract.md", (
            "YYYY-MM-DD-brainstorming", "-2", "F-01", "M-01", "never reuse",
            "single source of truth", "manual", "symlink", "session language",
            "feature", "fix", "ux", "performance", "dx", "gameplay",
        ))

    def test_decision_contract(self):
        self.requires("skills/brainstorm/references/decision-workflow.md", (
            "one focused question", "rationale", "do not invent", "rejected",
            "accepted", "implemented", "history", "partial", "confirmation",
        ))

    def test_follow_is_optional(self):
        self.requires("skills/brainstorm/SKILL.md", (
            "standalone", "unavailable", "disabled", "brainstorm-follow",
        ))
        self.requires("skills/brainstorm-follow/references/follow-workflow.md", (
            "brainstorm", "explicit", "do not generate", "derived", "manual",
        ))

    def test_idea_template_has_single_editable_status(self):
        text = self.text("skills/brainstorm/assets/idea.template.md")
        self.assertEqual(len(re.findall(r"^Status:", text, re.M)), 1)
        for heading in (
            "In brief", "Problem or opportunity", "Evaluation", "Tangible complexity",
            "Implementation outline", "Acceptance and tests", "Decision",
            "Implementation evidence", "Decision history",
        ):
            self.assertIn(f"## {heading}", text)
        for field in ("Impact:", "Effort:", "Feasibility:", "Missing elements:", "Risks:"):
            self.assertIn(field, text)

    def test_summary_and_index_templates(self):
        self.requires("skills/brainstorm/assets/index.template.md", (
            "source of truth", "| ID |", "Last synchronized",
        ))
        self.requires("skills/brainstorm/assets/summary.template.md", (
            "Project panorama", "Functional capabilities", "Ideas", "Limitations",
        ))

    def test_perf_authorization_and_isolation(self):
        self.requires("skills/brainstorm-perf/references/safety-and-consent.md", (
            "do not execute", "read-only", "credentials", "audit logs",
            "separate test environment", "consent", "cleanup", "residual",
            "symlink", "original", "network", "logs", "timeout",
        ))

    def test_perf_measurements_and_evidence(self):
        self.requires("skills/brainstorm-perf/references/measurement-workflow.md", (
            "confirmed", "not observed", "inconclusive", "representative",
            "repetitions", "end-to-end", "original session", "ID", "-test",
        ))
        self.requires("skills/brainstorm-perf/assets/test-plan.template.md", (
            "Hypothesis", "Design", "Access and consent", "Reproduction", "Cleanup plan",
        ))
        self.requires("skills/brainstorm-perf/assets/test-results.template.md", (
            "Conclusion:", "Measurements", "Original-state checks", "Cleanup and privacy",
        ))

    def test_repository_license_and_registration(self):
        self.requires("LICENSE", ("Apache License", "Version 2.0", "Redistribution"))
        self.requires("NOTICE", ("AlvarezTDV", "2026"))
        self.assertFalse(list((ROOT / "skills").glob("*/LICENSE*")))
        self.requires("AGENTS.md", SKILLS)
        self.requires("README.md", (*SKILLS, "Apache-2.0", "standalone", "LICENSE"))
        self.requires(".gitignore", ("/.atl/",))


if __name__ == "__main__":
    unittest.main()
