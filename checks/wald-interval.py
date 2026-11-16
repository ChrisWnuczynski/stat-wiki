"""Printed values for the Wald interval article."""

from pathlib import Path
from math import sqrt

from scipy.stats import norm

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "wald-interval.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

assert round(norm.ppf(0.975), 2) == 1.96
se = sqrt(0.40 * 0.60 / 100)
assert abs(se - sqrt(0.0024)) < 1e-15
assert round(se, 4) == 0.0490
half = 1.96 * round(se, 4)
assert round(half, 3) == 0.096
assert round(0.40 - 0.096, 3) == 0.304
assert round(0.40 + 0.096, 3) == 0.496

se_fair = sqrt(0.5 * 0.5 / 100)
assert se_fair == 0.05
assert abs(1.96 * 0.05 - 0.098) < 1e-12
assert round(0.50 - 0.098, 3) == 0.402
assert round(0.50 + 0.098, 3) == 0.598

se10 = sqrt(0.1 * 0.9 / 100)
assert abs(se10 - 0.03) < 1e-12
assert abs(1.96 * 0.03 - 0.0588) < 1e-12
assert round(0.10 - 0.0588, 4) == 0.0412
assert round(0.10 + 0.0588, 4) == 0.1588
assert 0 * (1 - 0) / 100 == 0
# p(1-p) peaks at 1/2.
assert 0.5 * 0.5 == 0.25

for printed in ("0.0490", "0.096", "0.304", "0.496", "0.05", "0.098",
                "0.402", "0.598", "0.03", "0.0588", "0.0412", "0.1588", "1.96"):
    assert printed in body, printed
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("wald interval checks passed")
