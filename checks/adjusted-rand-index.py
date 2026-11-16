"""Printed values for the adjusted Rand index article."""

from math import comb
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "adjusted-rand-index.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

assert comb(3, 2) == 3
assert comb(6, 2) == 15
assert comb(2, 2) == 1
I = 2 * comb(2, 2)
assert I == 2
row_pairs = 2 * comb(3, 2)
assert row_pairs == 6
apart = 15 - 6 - 6 + 2
assert apart == 5
assert round(7 / 15, 4) == 0.4667
expect = 6 * 6 / 15
assert expect == 2.4
ari = (2 - 2.4) / (6 - 2.4)
assert abs(ari - (-1 / 9)) < 1e-12
assert round(ari, 3) == -0.111
assert (6 - 2.4) / (6 - 2.4) == 1

for printed in ("0.4667", "2.4", "-0.111", "15", "7/15"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("adjusted Rand index checks passed")
