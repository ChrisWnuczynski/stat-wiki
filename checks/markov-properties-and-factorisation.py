"""Arithmetic checks for the Markov properties article."""

import math
from fractions import Fraction as F
from pathlib import Path

import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/markov-properties-and-factorisation.md").read_text(encoding="utf-8")
article = root / "articles/markov-properties-and-factorisation.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose and text in page, text


joint = F(3, 4) * F(1, 2) * F(2, 3)
assert joint == F(1, 4)
marginal_joint = F(3, 4) * F(2, 3) * F(1, 2) + F(1, 4) * F(1, 3) * F(1, 2)
assert marginal_joint == F(7, 24)
assert F(3, 4) * F(1, 2) + F(1, 4) * F(1, 2) == F(1, 2)
assert F(1, 4) == F(6, 24)

K = np.array([[2.0, -1, 0], [-1, 3, -1], [0, -1, 2]])
sigma = np.linalg.inv(K)
expect = np.array([[5, 2, 1], [2, 4, 2], [1, 2, 5]], float) / 8
assert np.allclose(sigma, expect)
assert abs(np.linalg.det(K) - 8) < 1e-9
corr = (1 / 8) / (5 / 8)
assert abs(corr - 0.2) < 1e-12
assert abs(1 / math.sqrt(6) - 0.408248290463863) < 1e-12

require(r"\frac14")
require(r"\frac{7}{24}")
require("6/24")
require(r"\frac12")
require("0.2")
require("0.408")
require(r"\det K=8")
print("markov-properties-and-factorisation checks passed")
