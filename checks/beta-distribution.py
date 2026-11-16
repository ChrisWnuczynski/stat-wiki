"""Check beta-distribution arithmetic, source examples and page structure."""

from math import isclose
from pathlib import Path

from scipy.stats import beta

root = Path(__file__).resolve().parents[1]
body = (root / "articles/beta-distribution.qmd").read_text().split("## See also", 1)[0]

# Source example, infobox and retained question examples.
assert isclose(beta.mean(2, 3), .4)
assert isclose(beta.var(2, 3), .04)
assert isclose(beta.cdf(.5, 2, 3), 11 / 16)
assert isclose(beta.sf(.5, 2, 3), 5 / 16)
assert (2 + 3, 3 + 7) == (5, 10)
assert (2 + 30, 3 + 70) == (32, 73)
assert (2 + 4, 8 + 6) == (6, 14)
assert (2 + 40, 8 + 60) == (42, 68)
assert isclose(42 / 110, .38181818181818183)
assert isclose(10 / 110, 1 / 11)

# Researched worked example and hidden answer.
assert (2 + 8, 3 + 2) == (10, 5)
assert isclose(beta.mean(10, 5), 10 / 15)
assert round((10 - 1) / (10 + 5 - 2), 6) == .692308
assert round(beta.sf(.5, 10, 5), 6) == .910217
assert (2 + 3, 3 + 1) == (5, 4)
assert round(beta.mean(5, 4), 6) == .555556
assert round(beta.sf(.5, 5, 4), 6) == .636719

for printed in ("0.6875", "0.3818", "0.04", "0.666667", "0.692308",
                "0.910217", "0.555556", "0.636719"):
    assert printed in body, printed
assert body.count("![") == 4
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body
assert "{#worked-example}" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("gelman_bda2013", "siegrist2022_beta"):
    assert f'data-cite-key="{key}"' in body
print("beta-distribution arithmetic and practice passed")
