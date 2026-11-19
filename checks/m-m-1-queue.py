"""Arithmetic checks for the M/M/1 article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

import math
from fractions import Fraction as F

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/m-m-1-queue.md").read_text(encoding="utf-8")
prose = shown(prose, "m-m-1-queue")
article = root / "articles/m-m-1-queue.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose and text in page, text


rho = F(3, 5)
assert 1 - rho == F(2, 5)
assert rho / (1 - rho) == F(3, 2)
assert rho ** 2 == F(9, 25)
assert F(1, 4) / F(3, 4) == F(1, 3)
rho2 = F(2, 3)
assert 1 - rho2 == F(1, 3)
assert rho2 ** 3 == F(8, 27)
assert rho2 / (1 - rho2) == 2
assert abs(math.exp(-3) - math.e ** -3) < 1e-12
require(r"\pi_0=2/5")
require(r"\frac{3}{2}")
require(r"9/25=0.36")
require(r"\pi_0=3/4")
require(r"L=2")
require(r"8/27")
require(r"e^{-3}")
print("m-m-1-queue checks passed")
