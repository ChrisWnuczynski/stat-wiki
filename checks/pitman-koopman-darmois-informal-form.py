"""Recompute the numerical examples, exercises and answers for pitman-koopman-darmois-informal-form."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "pitman-koopman-darmois-informal-form.qmd").read_text(encoding="utf-8")
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

a=[1,2,6];b=[0,4,5];near(sum(a),9);near(sum(b),9)
rat=math.prod(math.factorial(x) for x in b)/math.prod(math.factorial(x) for x in a);printed(rat)
for lam in [.5,1.,3.,8.]:near(math.exp(stats.poisson.logpmf(a,lam).sum()-stats.poisson.logpmf(b,lam).sum()),rat)
near(sum(a+[4]),13);near(sum(b+[4]),13)
print("pitman-koopman-darmois-informal-form:", checks, "numerical and rendered-value checks passed")
