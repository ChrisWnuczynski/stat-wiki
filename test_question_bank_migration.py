"""Protect existing exercise placements and independently readable depth prompts.

Run after build_wiki.py. These are the selections lost during the original
migration, including its incidental changes to chapter-question fallbacks.
"""
import json
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "margin-of-error": {"ex-da-juice-variance", "ex-da-melbourne-oil"},
    "designed-experiment": {"depth-blinding-design-roles", "depth-blinding-risk-difference"},
    "posterior-hypothesis-probability": {"q-44", "ex-applied-iq"},
    "proportional-odds-model": {"c-24", "q-46"},
    "likelihood-function": {"ex-inf-no-uniform-risk", "ex-inf-shrunk-mean"},
    "explanatory-variable": {"ex-inf-advertising-r2", "ex-inf-correlation-t"},
    "expectation": {"depth-mgf-bernoulli-sum", "ex-prob-affine-uniform-mean"},
    "variance": {"depth-mgf-domain", "ex-prob-affine-uniform-mean"},
    "consistent-estimator": {"ex-inf-two-standard-errors", "ex-inf-exponential-mle"},
    "unbiased-estimator": {"ex-inf-poisson-umvu", "ex-inf-exponential-mle"},
    "correlation": {"ex-da-correlation-reading", "ex-sl-01-2"},
    "mean-vector-and-covariance-matrix": {"ex-sl-01-2", "ex-sl-01-4"},
    "joint-probability-mass-function": {"ex-prob-cdf-of-maximum", "ex-prob-independent-exponentials"},
    "hazard-rate": {"ex-prob-component-five-years", "ex-prob-bridge-paths"},
    "pooled-variance": {"ex-inf-variance-ratio-interval", "ex-inf-green-voters"},
    "proper-prior-and-proper-posterior": {"c-01", "c-05"},
    "gaussian-linear-model": {"ex-inf-normal-equations", "depth-reference-prior-update"},
}


def check_section(text):
    return "\n".join(re.findall(
        r"(?ms)^## Check yourself[^\n]*\n.*?(?=^## |\Z)", text))


class SourceMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions = json.loads((ROOT / "sources/depth-questions.json").read_text())
        cls.by_id = {q["id"]: q for q in cls.questions}

    def test_migrated_prompts_supply_their_own_context(self):
        for question in self.questions:
            if not re.fullmatch(r"depth-.+-q[1-3]", question["id"]):
                continue
            with self.subTest(question=question["id"]):
                prompt = question["body"]
                self.assertNotRegex(prompt, r"(?i)worked example|displayed|part\s*\(")
                self.assertNotRegex(prompt, r"(?i)\b(?:matrix|formula|example|covariance)\s+(?:above|below)\b|\b(?:the|this) example\b")
                self.assertNotRegex(prompt, r"(?i)^\s*Practice question\b")
                self.assertNotRegex(prompt, r"^[^\n.!?$]{2,70}: ")
                self.assertTrue("?" in prompt or re.search(
                    r"(?i)\b(?:find|compute|show|explain|give|write|name|compare|evaluate|use|construct|divide)\b", prompt),
                    "A prompt must ask a question or give a mathematical task")
                self.assertNotIn("{{cite:", question["answer"])

    def test_existing_exercises_have_no_migrated_copies(self):
        # A handwritten section that still identifies a canonical exercise must
        # not also generate a second question with a depth-<page>-qN identity.
        for path in (ROOT / "research/content").glob("*.md"):
            section = check_section(path.read_text())
            if not re.search(r"(?:questions/|\{#self-check-(?:ex-|c-\d|q-\d|depth-|exr-))", section):
                continue
            prefix = f"depth-{path.stem}-q"
            with self.subTest(page=path.stem):
                self.assertFalse(any(qid.startswith(prefix) for qid in self.by_id))

    def test_added_givens_match_exact_calculations(self):
        # A changed prompt must retain the numerical answer of its calculation.
        p11, p21 = Fraction(4, 5), Fraction(2, 5)
        p2_11 = p11*p11 + (1-p11)*p21
        self.assertEqual(p2_11, Fraction(18, 25))
        self.assertEqual(p2_11*p11 + (1-p2_11)*p21, Fraction(86, 125))
        variance = (4*Fraction(4, 3) + 2*sum(
            (4-h)*Fraction(4, 3)*Fraction(1, 2)**h for h in range(1, 4))) / 16
        self.assertEqual(variance, Fraction(11, 16))
        self.assertIn("0.6875", self.by_id["depth-time-series-q2"]["answer"])
        self.assertEqual(Fraction(1, 2)*Fraction(4, 5)*Fraction(1, 5)*2, Fraction(4, 25))
        self.assertIn("0.16", self.by_id["depth-markov-random-field-q2"]["answer"])


class RenderedMigrationTests(unittest.TestCase):
    def test_original_selected_exercises_remain(self):
        for slug, expected in EXPECTED.items():
            with self.subTest(page=slug):
                path = ROOT / "articles" / f"{slug}.qmd"
                self.assertTrue(path.is_file(), "Run build_wiki.py before this test")
                section = check_section(path.read_text())
                ids = re.findall(r"\{#self-check-([^}]+)\}", section)
                self.assertEqual(set(ids), expected)
                self.assertEqual(len(ids), len(set(ids)), "An exercise is repeated")
                for qid in expected:
                    # Some handwritten checks identify their exercise in the
                    # heading; all existing explicit links must also survive.
                    source = ROOT / "research/content" / f"{slug}.md"
                    raw = source.read_text() if source.exists() else ""
                    link = f"../questions/{qid}.qmd"
                    if link in raw or slug in {
                        "expectation", "variance", "likelihood-function",
                        "explanatory-variable", "unbiased-estimator",
                    }:
                        self.assertIn(link, section)

    def test_restored_links_are_live_and_answers_stay_collapsed(self):
        for slug in ("brier-score", "margin-of-error", "addiction-data", "blocks-in-analysis-of-variance"):
            with self.subTest(page=slug):
                source = (ROOT / "research/content" / f"{slug}.md").read_text()
                page = (ROOT / "articles" / f"{slug}.qmd").read_text()
                for qid in re.findall(r"\.\./questions/([^/)]+)\.qmd", check_section(source)):
                    self.assertIn(f"../questions/{qid}.qmd", page)
                    self.assertTrue((ROOT / "questions" / f"{qid}.qmd").is_file())
                self.assertGreaterEqual(check_section(page).count('collapse="true" title="Answer"'), 2)


if __name__ == "__main__":
    unittest.main()
