"""Recompute the numerical examples, exercises and answers for spatial-poisson-process."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "spatial-poisson-process.qmd").read_text(encoding="utf-8")
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

lam=2;area=1.5;mean=lam*area
printed(mean);printed(stats.poisson.pmf(0,mean),6);printed(stats.poisson.sf(1,mean),6)
u=lam*math.pi*.5**2
for v in [u,math.exp(-u),1-math.exp(-u),math.sqrt(math.log(2)/(lam*math.pi)),1/math.sqrt(2),math.sqrt(math.log(2)/(4*math.pi))]:printed(v,6)
near(math.exp(-lam*math.pi*(math.sqrt(math.log(2)/(lam*math.pi)))**2),.5)
for q in [.2,.7]:near(math.exp(mean*((1-q+q*.8)-1)),math.exp(mean*q*(.8-1)))
print("spatial-poisson-process:", checks, "numerical and rendered-value checks passed")
