"""Recompute the numerical examples, exercises and answers for pearson-dispersion-ratio."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "pearson-dispersion-ratio.qmd").read_text(encoding="utf-8")
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

x=np.array([1.,2.,8.,9.]);y=np.array([4.,5.,5.,6.]);near(x.mean(),5);near(y.mean(),5)
xp=((x-x.mean())**2/x.mean()).sum();yp=((y-y.mean())**2/y.mean()).sum()
printed(xp);printed(yp);printed(xp/3,6);printed(yp/3,6);printed(math.sqrt(xp/3),6);printed(2.4/math.sqrt(xp/3),6);printed(xp/2)
near(4**.5,2)
print("pearson-dispersion-ratio:", checks, "numerical and rendered-value checks passed")
