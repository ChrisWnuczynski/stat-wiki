"""Arithmetic checks for Lloyd's K-means article."""

import math
from math import comb
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/lloyd-s-k-means-algorithm.md").read_text(encoding="utf-8")
article = root / "articles/lloyd-s-k-means-algorithm.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose and text in page, text


def stirling(n, k):
    return sum((-1) ** (k - j) * comb(k, j) * j**n for j in range(k + 1)) // math.factorial(k)


assert stirling(4, 2) == 7
assert stirling(10, 3) == 9330
# First example: centres 0.5 and 10, sum of squares 0.5.
assert (0 - 0.5) ** 2 + (1 - 0.5) ** 2 + (10 - 10) ** 2 == 0.5
# Second example: centres 0 and 9, sum of squares 2.
assert (8 - 9) ** 2 + (10 - 9) ** 2 == 2
require("0.5")
require("=2$")
require("$S(4,2)=7$")
require("$S(10,3)=9330$")
print("lloyd-s-k-means-algorithm checks passed")
