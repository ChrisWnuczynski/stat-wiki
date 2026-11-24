"""Check all printed examples and key calibration claims on p-value."""

from fractions import Fraction
from math import comb, isclose, sqrt
from pathlib import Path
import re
from scipy.stats import binom, binomtest, chi2, norm, t

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

# Asymmetric null: enumerate exact masses, then cross-check with SciPy.
masses = [Fraction(comb(10, j)*3**j*7**(10-j), 10**10)
          for j in range(11)]
assert sum(masses) == 1
mass_ordered_counts = [j for j, mass in enumerate(masses) if mass <= masses[0]]
assert mass_ordered_counts == [0, 7, 8, 9, 10]
p_mass = sum(masses[j] for j in mass_ordered_counts)
assert p_mass == Fraction(388396033, 10**10)
lower_inclusive = sum(masses[:1])  # P(K <= 0), including the observed count.
upper_inclusive = sum(masses[0:])  # P(K >= 0), also including it.
assert lower_inclusive == Fraction(7, 10)**10
assert upper_inclusive == 1
p_double = min(1, 2*min(lower_inclusive, upper_inclusive))
assert p_double == Fraction(564950498, 10**10)
assert f"{float(p_mass):.8f}" == "0.03883960"
assert f"{float(p_double):.8f}" == "0.05649505"
assert p_mass < Fraction(5, 100) < p_double
assert isclose(float(p_mass), binomtest(0, 10, .3).pvalue, abs_tol=1e-14)
assert isclose(float(p_double),
               min(1, 2*min(binom.cdf(0, 10, .3), binom.sf(-1, 10, .3))),
               abs_tol=1e-14)

# The answered bank questions chosen for the page use distinct null tails.
assert round(2*norm.sf(2.64), 4) == .0083  # bank says about .0082
counts = [234, 301, 256, 315, 274]
assert sum(counts) == 1380
stat_possum = sum((o-276)**2/276 for o in counts)
assert round(stat_possum, 2) == 15.63
assert round(chi2.sf(stat_possum, 4), 4) == .0036

for printed in ("0.199", "0.161", "0.208", "19.57", "2.575", "19.03",
                "18.97", "20.17", "0.020695", "0.041389", "299/4096",
                "0.072998", "0.145996", "0.6415", "0.0388396033",
                "0.03883960", "0.0564950498", "0.05649505"):
    assert printed in body, printed
assert body.count("![") == 2
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "{#worked-example}" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
practice = body.split("**Your turn.**", 1)[1].split("\n## ", 1)[0]
answer = re.search(r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::',
                   practice, re.S)
assert answer is not None, "The existing practice answer must stay folded"
assert "299/4096" in answer.group(1) and "0.145996" in answer.group(1)
assert "{{cite:" not in answer.group(1) and 'data-cite-key=' not in answer.group(1)
for key in ("siegrist2022_testing", "asa2016_pvalues",
            "siegrist2022_binomial_distribution", "agresti1992_exact_survey"):
    assert f'data-cite-key="{key}"' in body
print("p-value arithmetic and practice passed")
