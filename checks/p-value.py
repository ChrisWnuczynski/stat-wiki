"""Check all printed examples and key calibration claims on p-value."""

from math import comb, sqrt
from pathlib import Path
from scipy.stats import binom, chi2, norm, t

root = Path(__file__).resolve().parents[1]
body = (root / "articles/p-value.qmd").read_text().split("## See also", 1)[0]

# Both inherited worked examples and the figures.
assert round(2*binom.cdf(10, 100, .15), 3) == .199
assert round(2*norm.cdf((10-15)/sqrt(12.75)), 3) == .161
assert round(2*norm.cdf((10.5-15)/sqrt(12.75)), 3) == .208
assert round(norm.ppf(.975), 3) == 1.960
assert round(2*norm.sf(2.30), 3) == .021
stat = (19.57-19)/(1.40/sqrt(40))
assert round(stat, 3) == 2.575
assert round(t.ppf(.99, 39), 2) == 2.43
assert round(t.sf(stat, 39), 3) == .007
assert round(19.57-t.ppf(.99, 39)*1.40/sqrt(40), 2) == 19.03
ci = (19.57-t.ppf(.995, 39)*1.40/sqrt(40),
      19.57+t.ppf(.995, 39)*1.40/sqrt(40))
assert tuple(round(z, 2) for z in ci) == (18.97, 20.17)

# Researched exact binomial example and hidden answer.
tail20 = sum(comb(20, j) for j in range(15, 21))/2**20
assert sum(comb(20, j) for j in range(15, 21)) == 21700
assert round(tail20, 6) == .020695
assert round(2*tail20, 6) == .041389
tail12 = sum(comb(12, j) for j in range(9, 13))/2**12
assert sum(comb(12, j) for j in range(9, 13)) == 299
assert round(tail12, 6) == .072998
assert round(2*tail12, 6) == .145996
assert round(1-.95**20, 4) == .6415

# The answered bank questions chosen for the page use distinct null tails.
assert round(2*norm.sf(2.64), 4) == .0083  # bank says about .0082
counts = [234, 301, 256, 315, 274]
assert sum(counts) == 1380
stat_possum = sum((o-276)**2/276 for o in counts)
assert round(stat_possum, 2) == 15.63
assert round(chi2.sf(stat_possum, 4), 4) == .0036

for printed in ("0.199", "0.161", "0.208", "19.57", "2.575", "19.03",
                "18.97", "20.17", "0.020695", "0.041389", "299/4096",
                "0.072998", "0.145996", "0.6415"):
    assert printed in body, printed
assert body.count("![") == 2
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "{#worked-example}" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("siegrist2022_testing", "asa2016_pvalues"):
    assert f'data-cite-key="{key}"' in body
print("p-value arithmetic and practice passed")
