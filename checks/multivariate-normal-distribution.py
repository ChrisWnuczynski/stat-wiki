"""Check the multivariate-normal worked examples and preserved page elements."""

from fractions import Fraction
from pathlib import Path
import re

page = (Path(__file__).resolve().parents[1] / "articles" / "multivariate-normal-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 4 * 9 - 1 == 35
assert 1 + Fraction(5 - 2, 9) == Fraction(4, 3)
assert 4 - Fraction(1, 9) == Fraction(35, 9)
assert 4 + 9 + 2 == 15
assert 1 + Fraction(-1 - 2, 9) == Fraction(2, 3)
assert 4 + 9 - 2 == 11
assert 1 + 1 + 2 * Fraction(3, 5) == Fraction(16, 5)

for printed in (
    r"$|\Sigma|=35$", r"$1+(1/9)(5-2)=4/3$",
    r"$4-1^2/9=35/9$", r"\operatorname N(4/3,35/9)",
    r"$T=X_1+X_2\sim\operatorname N(3,4+9+2(1)=15)$",
    r"$P(T>3)=1/2$", r"$1+(1/9)(-1-2)=2/3$",
    r"\operatorname N(2/3,35/9)", r"$4+9-2(1)=11$",
    r"\operatorname N(-1,11)",
):
    assert printed in body, f"Missing printed example value: {printed}"

assert body.count('title="Proof"') == 1
assert body.count('title="Answer"') >= 1
assert body.count("../reference/plots/multivariate-normal-distribution-") == 2
assert "prob-correlation.png" in body
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", body))
assert len(questions) == 11, f"Expected 11 question links, got {len(questions)}"
assert all(key in body for key in (
    'data-cite-key="strimmer2025_mva"',
    'data-cite-key="wang2025_foundations"',
    'data-cite-key="stigler2010_galton_multivariate"',
))
print("multivariate-normal-distribution arithmetic, proof, figures, and links passed")
