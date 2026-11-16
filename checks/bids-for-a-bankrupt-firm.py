"""Printed values for the bankrupt-firm bids article."""

from math import exp
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "bids-for-a-bankrupt-firm.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

assert round(exp(0.2679), 3) == 1.307
assert round(exp(0.2679), 2) == 1.31
assert round(0.2679 / 0.1228, 3) == 2.182
assert round(0.2679 / 0.1228, 2) == 2.18
s = 0.1793 / (2 * 0.0076)
assert round(s, 2) == 11.80
extra = 0.1793 * 11.80 - 0.0076 * 11.80 ** 2
assert round(extra, 4) == 1.0575
assert round(exp(1.0575), 3) == 2.879
assert round(exp(0.4813), 3) == 1.618

for printed in ("1.307", "1.31", "2.182", "2.18", "11.80", "1.0575", "2.879", "1.618", "0.2679"):
    assert printed in body, printed
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("bids checks passed")
