"""Recompute the interpolation and constant-fit examples."""

from pathlib import Path
from fractions import Fraction

body = (Path(__file__).resolve().parents[1] / "articles/overfitting.qmd").read_text().split("## See also")[0]

def mse(y, pred):
    return sum((a - b) ** 2 for a, b in zip(y, pred)) / len(y)

x = [-1, 0, 1]
y = [0, 1, 0]
q = lambda z: 1 - z * z
assert [q(z) for z in x] == y and mse(y, [q(z) for z in x]) == 0
c = Fraction(sum(y), len(y))
assert c == Fraction(1, 3)
assert sum((Fraction(a) - c) ** 2 for a in y) == Fraction(2, 3)
assert mse(y, [c] * len(y)) == Fraction(2, 9)
assert round(float(Fraction(2, 9)), 3) == .222
assert q(2) == -3 and (0 - q(2)) ** 2 == 9
assert (0 - c) ** 2 == Fraction(1, 9)
assert round(float(Fraction(1, 9)), 3) == .111

y2 = [0, 2, 0]
q2 = lambda z: 2 - 2 * z * z
assert [q2(z) for z in x] == y2
c2 = Fraction(sum(y2), len(y2))
assert c2 == Fraction(2, 3)
assert sum((Fraction(a) - c2) ** 2 for a in y2) == Fraction(8, 3)
assert mse(y2, [c2] * len(y2)) == Fraction(8, 9)
assert round(float(Fraction(8, 9)), 3) == .889
assert q2(2) == -6 and (0 - q2(2)) ** 2 == 36
assert (0 - c2) ** 2 == Fraction(4, 9)
assert round(float(Fraction(4, 9)), 3) == .444

for printed in (
    "(-1,0),(0,1),(1,0)", "1-x^2", "1/3", "2/3", "2/9", "0.222",
    "-3", "1/9", "0.111", "0.02", "0.18", "2-2x^2", "8/3",
    "8/9", "0.889", "-6", "36", "4/9", "0.444",
):
    assert printed in body, f"Missing printed value: {printed}"
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("james_islr2013",):
    assert f'data-cite-key="{key}"' in body
print("overfitting examples, proof and citations passed")
