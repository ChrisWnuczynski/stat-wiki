"""Check the printed probability and odds conversions in the page."""
from fractions import Fraction as F
from pathlib import Path

text = (Path(__file__).parents[1] / "research/content/interpreting-a-logistic-regression.md").read_text()
page = (Path(__file__).parents[1] / "articles/interpreting-a-logistic-regression.qmd").read_text()
for p0, r, p1, diff, rr in [
    (F(1, 4), F(2), F(2, 5), F(3, 20), F(8, 5)),
    (F(1, 5), F(3), F(3, 7), F(8, 35), F(15, 7)),
]:
    odds0 = p0 / (1-p0)
    odds1 = r * odds0
    assert odds1 / (1+odds1) == p1
    assert p1-p0 == diff
    assert p1/p0 == rr
    assert (p1/(1-p1)) / odds0 == r
for token in ("1/4", "1/3", "2/5", "0.4", "8/5", "1.6", "3/20", "0.15", "1/5", "3/4", "3/7", "8/35", "15/7"):
    assert token in text, token
    assert token in page, token
print("logistic interpretation arithmetic: 21 checks passed")
