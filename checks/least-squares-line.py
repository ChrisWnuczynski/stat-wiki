"""Arithmetic for the least-squares-line depth pass."""
from math import sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/least-squares-line.md").read_text(encoding="utf-8")
page = root / "articles/least-squares-line.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

xs, ys = [0, 1, 2], [1, 1, 4]
mx, my = 1, 2
sxx = sum((x - mx) ** 2 for x in xs)
sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
assert sxx == 2 and sxy == 3
b1, b0 = 1.5, 0.5
resid = [y - (b0 + b1 * x) for x, y in zip(xs, ys)]
assert abs(sum(r * r for r in resid) - 1.5) < 1e-12
b = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
assert b == 1.8
origin = sum((y - b * x) ** 2 for x, y in zip(xs, ys))
assert abs(origin - 1.8) < 1e-12
assert abs(sqrt(1.5) - 1.224744871) < 1e-8
ys2 = [0, 0, 3]
my2 = 1
sxy2 = sum((x - mx) * (y - my2) for x, y in zip(xs, ys2))
assert sxy2 == 3 and (my2 - 1.5 * mx) == -0.5

for printed in ("1.5", "0.5", "1.8", "1.2247", "-0.5"):
    assert printed in prose and printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
print("least-squares-line arithmetic passed")
