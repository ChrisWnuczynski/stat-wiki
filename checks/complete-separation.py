"""Arithmetic checks for the complete-separation article."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/complete-separation.md").read_text(encoding="utf-8")
article = root / "articles/complete-separation.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose, text
    assert text in page, text


def ell(beta, n=4):
    return n * (beta - math.log(1 + math.exp(beta)))


def score(beta):
    return 1 / (1 + math.exp(beta))


values = {0: -2.773, 1: -1.253, 2: -0.508, 5: -0.027}
for beta, shown in values.items():
    assert round(ell(beta), 3) == shown
    assert score(beta) > 0
assert ell(0) < ell(1) < ell(2) < ell(5) < 0
assert abs(ell(0) + 4 * math.log(2)) < 1e-12
# The contribution tends to 0 from below.
assert abs((10 - math.log(1 + math.exp(10))) - (-math.log(1 + math.exp(-10)))) < 1e-12
assert -math.log(1 + math.exp(-10)) > -0.001

require(r"-4\log 2\approx -2.773")
require(r"\ell(2)\approx -0.508")
require(r"\ell(5)\approx -0.027")
require(r"\approx -1.253")
print("complete-separation checks passed")
