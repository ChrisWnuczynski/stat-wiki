"""Numerical and structural checks for the critical-region article."""

from pathlib import Path
from math import comb, isclose, sqrt
from scipy.stats import binom, chi2, norm, t

ROOT = Path(__file__).resolve().parents[1]
page = (ROOT / "articles/critical-region.qmd").read_text()
source = (ROOT / "research/content/critical-region.md").read_text()

def near(actual, expected, tol=5e-4):
    assert isclose(actual, expected, abs_tol=tol), (actual, expected)

assert sum(comb(10, k) for k in range(8, 11)) == 56
near(binom.sf(7, 10, 0.5), 0.0546875, 1e-12)
near(binom.sf(8, 10, 0.5), 0.0107421875, 1e-12)
assert sum(comb(12, k) for k in range(10, 13)) == 79
near(binom.sf(9, 12, 0.5), 79 / 4096, 1e-12)
near(norm.sf(1.645), 0.05, 2e-5)
near(norm.sf(1.960) * 2, 0.05, 2e-5)
near(t.ppf(.99, 39), 2.43, .005)
near((19.57-19)/(1.4/sqrt(40)), 2.575, .005)
near(t.sf((19.57-19)/(1.4/sqrt(40)), 39), .007, .0001)
near(t.ppf(.05, 6), -1.943, .001)
near(chi2.ppf(.05, 6), 1.635, .001)
near(chi2.cdf(6*.488/1.1, 6), .15, .001)
near(binom.sf(12, 15, .6), .0271, .0001)
near(binom.sf(12, 15, .9), .816, .001)
near(binom.sf(12, 15, .8), .398, .001)
near(7/sqrt(101), .6965, .0001)
near(1.960*7/sqrt(101), 1.365, .001)
near(norm.cdf((11-10.658)/.4), .804, .001)
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert '## Common misconceptions' in page
assert '{#assumptions-and-limits}' in page
assert "Lead context" not in source
print("critical region examples, inherited figures and structure passed")
