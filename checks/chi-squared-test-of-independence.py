"""Printed values for the chi-squared test of independence."""

from pathlib import Path
from scipy.stats import chi2

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "chi-squared-test-of-independence.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]
figures = len(__import__("re").findall(r"!\[[^]]*\]\(", page))
assert figures >= 1

assert 30 * 28 / 60 == 14
assert 30 * 32 / 60 == 16
stat = 2 * (16 / 14) + 2 * (16 / 16)
assert abs(stat - 30 / 7) < 1e-12
assert round(stat, 3) == 4.286
assert round(chi2.ppf(0.95, 1), 3) == 3.841
assert round(1 - chi2.cdf(30 / 7, 1), 4) == 0.0384
assert (3 - 1) * (4 - 1) == 6
assert 12 - 1 - (2 + 3) == 6

for printed in ("4.286", "3.841", "0.0384", "30/7", "14", "16"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("chi-squared independence checks passed")
