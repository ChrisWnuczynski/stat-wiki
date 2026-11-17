"""Recompute the numerical examples, exercises and answers for sampling-distribution-of-the-ols-estimator."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "sampling-distribution-of-the-ols-estimator.qmd").read_text(encoding="utf-8")
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

x=np.arange(-2,3,dtype=float);X=np.column_stack([np.ones(5),x]);C=np.linalg.inv(X.T@X);H=X@C@X.T;A=C@X.T
assert np.allclose(C,np.diag([.2,.1]));checks+=1
assert np.allclose(H@H,H);checks+=1
assert np.allclose(A@(np.eye(5)-H),0);checks+=1
for v in [4*C[0,0],4*C[1,1]]:printed(v)
y=np.array([0.,1.,1.,3.,5.]);b=A@y;e=y-X@b;ss=e@e;s2=ss/3;se=math.sqrt(s2*C[1,1]);t=b[1]/se
for v in b:printed(v)
printed(ss);printed(s2,6);printed(se,6);printed(t,6)
near(np.trace(np.eye(5)-H),3);near(12-4,8)
print("sampling-distribution-of-the-ols-estimator:", checks, "numerical and rendered-value checks passed")
