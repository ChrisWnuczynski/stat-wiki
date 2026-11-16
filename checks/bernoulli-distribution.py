"""Check the numerical Bernoulli examples, structure and preserved figures."""

from fractions import Fraction
from pathlib import Path
from math import comb

root = Path(__file__).resolve().parents[1]
page = (root / "articles/bernoulli-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

p = Fraction(3, 10)
assert 1-p == Fraction(7, 10)
assert p*(1-p) == Fraction(21, 100)
assert comb(3, 2)*p**2*(1-p) == Fraction(189, 1000)
assert p**3 == Fraction(27, 1000)
turn = Fraction(3, 5)
assert comb(4, 3)*turn**3*(1-turn) == Fraction(216, 625)
assert 1-(1-turn)**4 == Fraction(609, 625)
assert float(Fraction(216, 625)) == .3456
assert round(float(Fraction(609, 625)), 4) == .9744
assert Fraction(1, 5)*Fraction(4, 5) == Fraction(4, 25)
assert 10*Fraction(1, 5) == 2
assert 10*Fraction(4, 25) == Fraction(8, 5)
assert Fraction(1, 2)*(1-Fraction(1, 2)) == Fraction(1, 4)

for printed in ("0.35", "0.2", "0.8", "0.16", "1/5", "4/25", "8/5",
                "0.30", "0.70", "0.21", "0.189", "0.027", "0.60",
                "0.40", "0.3456", "0.9744"):
    assert printed in body, printed
assert page.count("../reference/plots/bernoulli-distribution-") == 2
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("siegrist2022_bernoulli_intro", "siegrist2022_binomial_distribution", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
print("Bernoulli distribution calculations and practice passed")
