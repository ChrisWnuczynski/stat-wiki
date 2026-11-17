"""Recompute the numerical examples, exercises and answers for squared-error-of-an-average."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "squared-error-of-an-average.qmd").read_text(encoding="utf-8")
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

f=np.array([1.,4.,7.]);y=5.;m=f.mean();a=np.mean((f-y)**2);d=np.mean((f-m)**2)
for v in [m,(m-y)**2,a,d]:printed(v)
near(a-d,(m-y)**2)
w=np.array([.25,.5,.25]);mw=w@f;aw=w@(f-y)**2;dw=w@(f-mw)**2
for v in [aw,dw]:printed(v)
near(aw-dw,(mw-y)**2);printed(0.);printed(4/10+9/10);printed(4/10)
near(np.var(f,ddof=1),9)
# Existing two-member examples and the weighted identity, independently expanded.
for values,target in [([3,7],4),([6,6],4),([6,6,6],5)]:
 f=np.array(values,dtype=float);near((f.mean()-target)**2,np.mean((f-target)**2)-np.mean((f-f.mean())**2))
# Two-member illustrations, including identical predictions.
f=np.array([3.,7.]);y=4.;near(f.mean(),5);near((f.mean()-y)**2,1);near(np.mean((f-y)**2),5);near(np.mean((f-f.mean())**2),4)
f=np.array([6.,6.]);near(np.var(f),0);near((f.mean()-y)**2,4)


# Four predictions whose average hits the outcome.
g=np.array([2.,2.,2.,6.]); yy=3.
near((g.mean()-yy)**2,0); near(np.mean((g-yy)**2),3); near(np.mean((g-g.mean())**2),3)
printed(3,3)
print("squared-error-of-an-average:", checks, "numerical and rendered-value checks passed")
