"""Numerical and structural checks for the flat-prior article."""

from math import isclose, sqrt
from pathlib import Path
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[1]
page = (ROOT / "articles/flat-prior.qmd").read_text()
content = (ROOT / "research/content/flat-prior.md").read_text()

def near(a, b, tol=1e-10):
    assert isclose(a, b, abs_tol=tol), (a, b)

mean = sum((9, 11, 10, 12)) / 4
near(mean, 10.5)
near(2**2/4, 1)
near(sqrt(2**2/4), 1)
near(mean - 1.96, 8.54)
near(mean + 1.96, 12.46)
practice_mean = sum((6, 9, 12, 9)) / 4
near(practice_mean, 9)
near(3**2/4, 2.25)
near(sqrt(3**2/4), 1.5)
near(practice_mean-1.96*1.5, 6.06)
near(practice_mean+1.96*1.5, 11.94)
near(norm.cdf(1.96)-norm.cdf(-1.96), .95, 1e-4)
for p in (.1, .3, .5, .8):
    odds = p/(1-p)
    jac = odds/(1+odds)**2
    near(jac, p*(1-p))
    near(1/jac, 1/(p*(1-p)))
for C, M in ((10**4, 2), (10**4, 10), (100, 5)):
    near((2*M)/(2*C), M/C)
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert '{#assumptions-and-limits}' in page
assert 'Lead context' not in content
print("flat prior posterior, Jacobian, numbers and structure passed")
