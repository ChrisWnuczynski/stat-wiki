"""Arithmetic for the simple-linear-regression depth pass."""
from math import sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/simple-linear-regression.md").read_text(encoding="utf-8")
page = root / "articles/simple-linear-regression.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8")
leading = body.split("## See also", 1)[0]

xs = [2, 4, 6, 8, 10]
ys = [3, 4, 8, 9, 11]
n = 5
mx, my = sum(xs) / n, sum(ys) / n
sxx = sum((x - mx) ** 2 for x in xs)
sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
b1 = sxy / sxx
b0 = my - b1 * mx
assert (mx, my, sxx, sxy) == (6, 7, 40, 42)
assert b1 == 1.05 and abs(b0 - 0.70) < 1e-12
fitted = [b0 + b1 * x for x in xs]
resid = [y - f for y, f in zip(ys, fitted)]
assert abs(sum(r * r for r in resid) - 1.90) < 1e-12
assert abs(sqrt(19 / 30) - 0.7958224257542215) < 1e-12
assert abs(sqrt(19 / 1200) - 0.12583057392117916) < 1e-12
assert abs(b0 + b1 * 7 - 8.05) < 1e-12

ys2 = [3, 4, 8, 9, 20]
my2 = sum(ys2) / n
sxy2 = sum((x - mx) * (y - my2) for x, y in zip(xs, ys2))
b1b, b0b = sxy2 / sxx, my2 - (sxy2 / sxx) * mx
assert sxy2 == 78 and b1b == 1.95 and abs(b0b - (-2.90)) < 1e-12

xs3, ys3 = [0, 1, 2], [1, 3, 2]
mx3, my3 = 1, 2
sxx3 = sum((x - mx3) ** 2 for x in xs3)
sxy3 = sum((x - mx3) * (y - my3) for x, y in zip(xs3, ys3))
assert sxx3 == 2 and sxy3 == 1
b1c, b0c = 0.5, 1.5
sse3 = sum((y - (b0c + b1c * x)) ** 2 for x, y in zip(xs3, ys3))
assert sse3 == 1.5

for printed in (
    "1.05", "0.70", "1.90", "0.7958", "0.1258", "8.05",
    "1.95", "-2.90", "0.5", "1.5", "40", "42",
):
    assert printed in prose, printed
    assert printed in leading, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
for key in ("nist_ls_straight2002", "nist_linear_least_squares_pmd2002", "dodge2008"):
    assert f"{{{{cite:{key}}}}}" in prose
print("simple-linear-regression arithmetic passed")
