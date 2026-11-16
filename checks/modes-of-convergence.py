"""Check the new convergence counterexamples and page structure."""

from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / "articles/modes-of-convergence.qmd").read_text().split("## See also", 1)[0]

n = 10
p = Fraction(1, n**3)
assert p == Fraction(1, 1000)
assert p * n**2 == Fraction(1, 10)
assert p * n**4 == 10
q = Fraction(1, n**2)
assert q == Fraction(1, 100)
assert q * n == Fraction(1, 10)
assert q * n**2 == 1
assert Fraction(1, 20) == Fraction(5, 100)

for printed in ("0.001", "0.01", "0.1", "10", "1/n^3", "1/n^2",
                "1/n", "L^1", "L^2", "1/2"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("siegrist_convergence_prob", "siegrist_convergence_dist", "siegrist_convergence_lp"):
    assert f'data-cite-key="{key}"' in body
print("modes of convergence calculations and practice passed")
