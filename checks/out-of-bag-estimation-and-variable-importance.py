"""Printed values for out-of-bag estimation and variable importance."""

from math import exp
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "out-of-bag-estimation-and-variable-importance.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

omit = (4 / 5) ** 5
assert abs(omit - 1024 / 3125) < 1e-12
assert round(omit, 4) == 0.3277
assert round(exp(-1), 4) == 0.3679
drops = [round(0.80 - 0.60, 2), round(0.70 - 0.60, 2), round(0.90 - 0.90, 2)]
assert drops == [0.20, 0.10, 0.00]
assert abs(sum(drops) / 3 - 0.10) < 1e-12
assert (1 / 2) ** 2 == 0.25
assert abs((0.20 + 0.10 + 0.15) / 3 - 0.15) < 1e-12

for printed in ("0.3277", "0.3679", "0.80", "0.70", "0.90", "0.60", "0.20", "0.10", "0.00", "0.25", "0.15"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("out-of-bag checks passed")
