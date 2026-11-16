"""Check the inverse-Gamma examples and preservation in the generated page."""

from fractions import Fraction
from pathlib import Path
import re

page = (Path(__file__).resolve().parents[1] / "articles" / "inverse-gamma-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

for printed in (
    r"$1/5$", r"$1/3$", r"$S_0=1^2+2^2+3^2=14$",
    r"\operatorname{InvGamma}(9/2,9)", r"18/7\approx2.571",
    r"18/11\approx1.636", r"14/3\approx4.667",
    r"$S_0=1^2+(-1)^2=2$", r"\operatorname{InvGamma}(3,4)",
    r"$4/(3-1)=2$", r"$4/(3+1)=1$",
    r"$2/(3-1)=1$", r"$2/(3+1)=1/2$",
    r"$2^2/[(3-1)^2(3-2)]=1$",
):
    assert printed in body, f"Missing printed example value: {printed}"

assert Fraction(1, 4 + 1) == Fraction(1, 5)
assert Fraction(1, 4 - 1) == Fraction(1, 3)
assert sum(v * v for v in (1, 2, 3)) == 14
assert (Fraction(3) + Fraction(3, 2), Fraction(2) + Fraction(14, 2)) == (Fraction(9, 2), Fraction(9))
assert Fraction(9) / (Fraction(9, 2) - 1) == Fraction(18, 7)
assert Fraction(9) / (Fraction(9, 2) + 1) == Fraction(18, 11)
assert round(float(Fraction(18, 7)), 3) == 2.571
assert round(float(Fraction(18, 11)), 3) == 1.636
assert round(float(Fraction(14, 3)), 3) == 4.667
assert sum(v * v for v in (1, -1)) == 2
assert (Fraction(2) + 1, Fraction(3) + 1) == (3, 4)
assert Fraction(4, 3 - 1) == 2
assert Fraction(4, 3 + 1) == 1
assert Fraction(2, 3 - 1) == 1
assert Fraction(2, 3 + 1) == Fraction(1, 2)
assert Fraction(2**2, (3 - 1)**2 * (3 - 2)) == 1

assert body.count('title="Proof"') == 1
assert body.count("../reference/plots/inverse-gamma-distribution-") == 2
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", body))
assert len(questions) == 19, f"Expected 19 question links, got {len(questions)}"
assert all(key in body for key in ('data-cite-key="stan_functions2026"', 'data-cite-key="gelman2006"', 'data-cite-key="raiffa_schlaifer1961"'))
print("inverse-gamma-distribution printed values, proof, figures, and question links passed")
