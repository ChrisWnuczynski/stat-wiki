"""Printed values for the complete-data likelihood article."""

from math import log
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "complete-data-likelihood.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

c1 = 0.4 * 0.5
c2 = 0.6 * 0.8
assert c1 == 0.2 and c2 == 0.48
assert abs(c1 * c2 - 0.096) < 1e-12
assert round(log(0.096), 3) == -2.343
o1 = 0.4 * 0.5 + 0.6 * 0.1
o2 = 0.4 * 0.2 + 0.6 * 0.8
assert o1 == 0.26 and o2 == 0.56
assert abs(o1 * o2 - 0.1456) < 1e-12
assert round(log(0.1456), 3) == -1.927
assert abs(0.6 * 0.1 - 0.06) < 1e-12
assert abs(0.06 * 0.48 - 0.0288) < 1e-12

for printed in ("0.096", "-2.343", "0.1456", "-1.927", "0.0288", "0.26", "0.56", "0.48"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("complete-data likelihood checks passed")
