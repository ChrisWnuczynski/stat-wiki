"""Recompute the numerical examples, exercises and answers for sampling-distribution-of-the-regression-estimators."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "sampling-distribution-of-the-regression-estimators.qmd").read_text(encoding="utf-8")
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

x=np.arange(1,6,dtype=float);X=np.column_stack([np.ones(5),x]);C=4*np.linalg.inv(X.T@X)
for v in [C[1,1],C[0,0],C[0,1],4/5,.5]:printed(v)
rho=C[0,1]/math.sqrt(C[0,0]*C[1,1]);printed(rho,6)
printed(math.sqrt(C[1,1]),6);printed(2*math.sqrt(C[1,1]),6)
u=x-x.mean();assert np.allclose(4*np.linalg.inv(np.column_stack([np.ones(5),u]).T@np.column_stack([np.ones(5),u])),np.diag([.8,.4]));checks+=1
near(np.sum((np.array([1,1,3,5,5])-3)**2),16)
near(np.array([1,3])@C@np.array([1,3]),.8)

# Fitted-mean variance two units from the centre.
near(4*(1/5+4/10),2.4)
printed(2.4,3)
print("sampling-distribution-of-the-regression-estimators:", checks, "numerical and rendered-value checks passed")
