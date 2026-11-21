"""Arithmetic checks for quadratic discriminant analysis."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
import math

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/quadratic-discriminant-analysis.md").read_text()
text = shown(text, "quadratic-discriminant-analysis")
body = (root / "articles/quadratic-discriminant-analysis.qmd").read_text().split("## See also", 1)[0]

def delta(x, mu, var):
    return -0.5 * math.log(var) - 0.5 * (x - mu) ** 2 / var + math.log(0.5)

c = 9 + 4 * math.log(4)
disc = 36 + 12 * c
r1 = (-6 + math.sqrt(disc)) / 6
r2 = (-6 - math.sqrt(disc)) / 6
assert round(r1, 3) == 1.418 and round(r2, 3) == -3.418
assert abs(delta(r1, 0, 1) - delta(r1, 3, 4)) < 1e-9
assert round(delta(0, 0, 1), 3) == -0.693
assert round(delta(0, 3, 4), 3) == -2.511
assert round(delta(-4, 0, 1), 3) == -8.693
assert round(delta(-4, 3, 4), 3) == -7.511
assert round(delta(3, 0, 1), 3) == -5.193
assert round(delta(3, 3, 4), 3) == -1.386
assert 2 * 1 + 1 * 2 / 2 + 1 == 4
assert 2 * 1 + 2 * 1 + 1 == 5
for printed in ("1.418", "-3.418", "-0.693", "-2.511", "-8.693", "-7.511",
                "-5.193", "-1.386", "$4$", "$5$"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("quadratic discriminant analysis checks passed")
