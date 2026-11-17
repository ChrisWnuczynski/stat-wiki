"""Recompute the numerical examples, exercises and answers for r-s-distribution-interface."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "r-s-distribution-interface.qmd").read_text(encoding="utf-8")
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

f=stats.beta(3,9)
for v in [f.pdf(.25),f.cdf(.5),f.ppf(.5),*f.ppf([.025,.975]),f.sf(.5)]:printed(v,6)
printed(f.mean());near(f.cdf(f.ppf(.5)),.5);near(f.cdf(.5)+f.sf(.5),1)
for p in [.025,.5,.975]:near(f.cdf(f.ppf(p)),p)
print("r-s-distribution-interface:", checks, "numerical and rendered-value checks passed")
