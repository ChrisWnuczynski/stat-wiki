"""Arithmetic for the Hotelling T-squared depth pass."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
from math import sqrt

from scipy.stats import f

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/hotelling-s-t2-test.md").read_text(encoding="utf-8")
prose = shown(prose, "hotelling-s-t2-test")
page = root / "articles/hotelling-s-t2-test.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

# identity example
assert 5 * (2 ** 2 + 0) == 20
# bivariate
quad = 0.5 + 0.5
assert quad == 1
T2 = 6 * quad
assert T2 == 6
transformed = ((6 - 2) / ((6 - 1) * 2)) * T2
assert abs(transformed - 2.4) < 1e-12
crit = float(f.ppf(0.95, 2, 4))
tail = float(f.sf(2.4, 2, 4))
assert round(crit, 3) == 6.944
assert round(tail, 4) == 0.2066
# p = 1
t2 = 5 * (2 ** 2) / 1
assert t2 == 20
assert round(2 * sqrt(5), 4) == 4.4721
# your turn
assert 6 * (0.5 * 4) == 12
for printed in ("2.4", "6.944", "0.2066", "4.4721", "20", "12"):
    assert printed in prose and printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
print("hotelling-s-t2-test arithmetic passed")
