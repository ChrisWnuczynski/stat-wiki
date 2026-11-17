"""Recompute the numerical examples, exercises and answers for observational-study."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "observational-study.qmd").read_text(encoding="utf-8")
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

A=np.array([40/80,2/20]);B=np.array([12/20,16/80])
near((40+2)/100,.42);near((12+16)/100,.28)
for v in [.42,.28,.14,*A,*B,float(A.mean()),float(B.mean()),float((A-B).mean()),float(A@[.25,.75]),float(B@[.25,.75])]:printed(v)
near(A.mean()-B.mean(),-.1);near(A@[.25,.75]-B@[.25,.75],-.1)
print("observational-study:", checks, "numerical and rendered-value checks passed")
