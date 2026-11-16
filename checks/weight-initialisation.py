"""Printed values for the weight-initialisation article."""

from math import sqrt

from pathlib import Path
from scipy.stats import norm

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "weight-initialisation.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

sigma = 1 / sqrt(4)
assert sigma == 0.5
assert 4 * sigma ** 2 == 1
assert sigma ** 2 * (1 + 3) == 1
assert round(2 * norm.cdf(1) - 1, 4) == 0.6827

a = sqrt(6 / 8)
assert round(a, 4) == 0.8660
assert abs(a ** 2 / 3 - 0.25) < 1e-12

assert abs(1 / 3 - 0.333333333333) < 1e-12
assert 9 * (1 / 3) ** 2 == 1
assert 2 / 16 == 0.125
assert round(sqrt(6) / 4, 4) == 0.6124
assert round(100 ** -0.5, 4) == 0.1
assert round(sqrt(2 / 104), 4) == 0.1387

for printed in ("0.6827", "0.8660", "0.25", "0.125", "0.6124", "0.1387", "0.1"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("weight initialisation checks passed")
