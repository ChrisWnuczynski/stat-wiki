"""Recompute the numerical examples, exercises and answers for power-function."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "power-function.qmd").read_text(encoding="utf-8")
checks = 0
def near(a, b, tol=1e-9):
    global checks
    assert math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol), (a,b)
    checks += 1
def printed(value, decimals=3):
    global checks
    token = f"{value:.{decimals}f}"
    assert token in article, ("Printed value missing",token)
    checks += 1

c=stats.norm.ppf(.95);d=math.sqrt(25)/2;p=stats.norm.sf(c-d)
printed(d);printed(c,6);printed(p,6);printed(1-p,6)
for v in [stats.binom.sf(8,10,.5),stats.binom.sf(8,10,.8)]:printed(v,6)
for p0 in [0.,.1,.5,.8,1.]:near(10*p0**9*(1-p0)+p0**10,stats.binom.sf(8,10,p0))
# Preserve and recompute the displayed serve-test tails and t-test powers.
for p0,expected in [(.6,.0271),(.9,.816),(.8,.398)]:near(stats.binom.sf(12,15,p0),expected,tol=.001)
for n in [5,50]:near(stats.nct.sf(stats.t.ppf(.95,n-1),n-1,math.sqrt(n)/2),.239 if n==5 else .967,tol=.001)
near(stats.norm.sf(stats.norm.ppf(.975)-2)+stats.norm.cdf(-stats.norm.ppf(.975)-2),.5160052739761748,tol=1e-3)
# Compare both serve rules displayed in the power-curve caption.
printed(stats.binom.sf(11,15,.6),3);printed(stats.binom.sf(12,15,.6),3)
# Tuning-fork variance example: carry the stated chi-square cutoff without premature rounding.
cutoff=1.635*1.1/6;printed(cutoff,3)
printed(6*cutoff/.3,3);printed(stats.chi2.cdf(6*cutoff/.3,6),2)


# Larger sample and a smaller departure for the same normal test.
printed(stats.norm.sf(c-5),6); printed(1-stats.norm.cdf(c-1.25),6); printed(stats.binom.sf(8,10,.9),6)
near(math.sqrt(100)/2,5); near(stats.norm.sf(c-5),0.9996033849954737)
print("power-function:", checks, "numerical and rendered-value checks passed")
