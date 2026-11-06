"""Check comparison-table structure, not live-agent behavior."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TemplateTables(unittest.TestCase):
    def test_template_table_arity(self):
        paths = list((ROOT / "skills").rglob("*.template.md"))
        self.assertTrue(paths, "No templates were checked")
        for path in paths:
            width = None
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if not line.startswith("|"):
                    width = None
                    continue
                actual = len(line.strip().strip("|").split("|"))
                if width is None:
                    width = actual
                with self.subTest(path=str(path.relative_to(ROOT)), line=number):
                    self.assertEqual(actual, width)


if __name__ == "__main__":
    unittest.main()
