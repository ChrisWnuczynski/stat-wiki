"""Exact binomial MSE and inherited estimator-example checks."""

from math import comb, isclose
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
page = (ROOT / "articles/mean-squared-error.qmd").read_text()
content = (ROOT / "research/content/mean-squared-error.md").read_text()

def near(a, b, tol=5e-4):
    assert isclose(a, b, abs_tol=tol), (a, b)

for p in (.1, .25, .5, .9):
    pmf = [comb(4,x)*p**x*(1-p)**(4-x) for x in range(5)]
    near(sum(pmf), 1, 1e-12)
    raw = sum(q*(x/4-p)**2 for x,q in enumerate(pmf))
    smooth = sum(q*((x+1)/6-p)**2 for x,q in enumerate(pmf))
    near(raw, p*(1-p)/4, 1e-12)
    near(smooth, 1/36, 1e-12)
near(.5*(1-.5)/4, .0625)
near(.1*(1-.1)/4, .0225)
near(.25*(1-.25)/4, .046875)
near(1/36, .02778, 5e-6)
for n in (2,3,10,100):
    unbiased = 2/(n-1)
    mle = (2*n-1)/n**2
    near(((n-1)/n)**2 * unbiased + 1/n**2, mle, 1e-12)
    assert mle < unbiased
near(2/9, .222, .0005)
near(19/100, .190, .0005)
near(1/30, .033, .0005)
near(2/(11*12), .015, .0002)
near(1/(10*12), 1/120, 1e-12)
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert '{#assumptions-and-limits}' in page
assert 'Lead context' not in content
print("mean squared error examples, inherited numbers and structure passed")
