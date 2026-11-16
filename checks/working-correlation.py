"""Numerical checks for the GEE working-correlation article."""

from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/working-correlation.qmd").read_text()
body = page.split("## See also", 1)[0]

m, rho = 4, F(-1, 2)
assert 1 - rho == F(3, 2)
assert 1 + (m - 1) * rho == F(-1, 2)
assert -F(1, m - 1) == -F(1, 3)

assert F(1 + 3 + 5, 3) == 3
pair_num = F(1 + 3, 1 + F(1, 2))
pair_weight = F(2, 1 + F(1, 2))
weighted = (pair_num + 5) / (pair_weight + 1)
assert pair_num == F(8, 3)
assert pair_weight == F(4, 3)
assert weighted == F(23, 7)
assert round(float(weighted), 6) == 3.285714

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "23/7", "3.285714",
    "-1/3", "-0.5", "1.5", "## Common misconceptions",
    "#assumptions-and-limits",
):
    assert fragment in body, f"Missing section or calculation: {fragment}"
assert body.count('title="Proof"') == 1
for qid in ("ex-ur-exchangeable-bound", "c-39", "c-40"):
    assert f"../questions/{qid}.qmd" in page
print("working-correlation matrix and weighted-GEE calculations passed")
