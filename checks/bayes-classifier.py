"""Check numeric Bayes decisions, risks and researched structure."""

from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / "articles/bayes-classifier.qmd").read_text().split("## See also", 1)[0]

w_a = Fraction(1, 5) * Fraction(3, 5)
w_b = Fraction(4, 5) * Fraction(1, 10)
assert (w_a, w_b) == (Fraction(12, 100), Fraction(8, 100))
p_a, p_b = w_a / (w_a + w_b), w_b / (w_a + w_b)
assert (p_a, p_b) == (Fraction(3, 5), Fraction(2, 5))
assert 3 * p_b == Fraction(6, 5) and p_a == Fraction(3, 5)
q = Fraction(1, 5)
assert (1-q) * 1 == Fraction(4, 5)
assert q * 8 == Fraction(8, 5)
assert Fraction(1, 9) < q

for printed in ("0.20", "0.60", "0.80", "0.10", "0.12", "0.08", "0.40",
                "1.20", "0.50", "1.60", "1/9", "0.1111", "20\\%"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert 'data-cite-key="james_islr2013"' in body
print("Bayes classifier calculations and practice passed")
