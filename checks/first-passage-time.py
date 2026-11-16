"""Arithmetic checks for the first-passage-time article."""

from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/first-passage-time.md").read_text(encoding="utf-8")
article = root / "articles/first-passage-time.qmd"
page = article.read_text(encoding="utf-8") if article.is_file() else prose


def require(text: str) -> None:
    assert text in prose, text
    assert text in page, text


require(r"$h_2=2/5$")
require(r"$e_2=2(5-2)=6$")
require(r"$3/5$")
require(r"\frac{135}{211}")
require(r"0.640")
require(r"$2/5=0.4$")
require(r"$h_4=4/6=2/3$")
require(r"$e_4=4(6-4)=8$")
require(r"$h_5=5/8$")
require(r"$e_5=5(8-5)=15$")
require("8/15")
require("1/4")

assert F(2, 5) == F(2, 5)
assert 2 * (5 - 2) == 6
assert 4 * (6 - 4) == 8
assert 5 * (8 - 5) == 15
p, q, d, x = F(3, 5), F(2, 5), 5, 2
ratio = q / p
h = (1 - ratio**x) / (1 - ratio**d)
assert h == F(135, 211)
assert round(float(h), 3) == 0.640
assert h > F(2, 5)

# Fair duration identity used in the proof.
def rhs(x, d):
    return 1 + F(1, 2) * (x + 1) * (d - x - 1) + F(1, 2) * (x - 1) * (d - x + 1)

for d in (5, 6, 8):
    for x in range(1, d):
        assert rhs(x, d) == x * (d - x)

h1 = (1 - F(1, 2)) / (1 - F(1, 2) ** 4)
assert h1 == F(8, 15)
assert F(8, 15) > F(1, 4)
print("first-passage-time checks passed")
