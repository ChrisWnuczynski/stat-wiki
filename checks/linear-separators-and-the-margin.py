"""Check the numeric geometry in the linear-separator depth page."""
from fractions import Fraction as F
from pathlib import Path

text = (Path(__file__).parents[1] / "research/content/linear-separators-and-the-margin.md").read_text()
page = (Path(__file__).parents[1] / "articles/linear-separators-and-the-margin.qmd").read_text()
points = [((-1, 0), -1), ((-1, 2), -1), ((1, 0), 1), ((1, 2), 1), ((-2, 1), -1), ((2, 1), 1)]
w = (F(1), F(0))
b = F(0)
scores = [y * (sum(w[j] * x[j] for j in range(2)) + b) for x, y in points]
assert scores == [1, 1, 1, 1, 2, 2]
assert min(scores) == 1 and 2 / sum(a*a for a in w) ** F(1, 2) == 2
assert sum(a*a for a in w) == 1
candidate = (F(1, 2), F(1))
score = sum(w[j] * candidate[j] for j in range(2)) + b
assert score == F(1, 2)
assert max(F(0), 1-score) == F(1, 2)
scaled = tuple(2*a for a in w)
assert sum(scaled[j]*candidate[j] for j in range(2)) == 1
assert sum(scaled[j]*candidate[j] for j in range(2)) / 2 == score
for token in ("(-1,0)", "(-1,2)", "(1,0)", "(1,2)", "(-2,1)", "(2,1)", "1/2", "2/\\lVert w\\rVert", "0.5"):
    assert token in text, token
    assert token in page, token
print("linear-separator geometry: 15 checks passed")
