"""Recompute the numerical examples, exercises and answers for squared-error-is-not-the-logistic-likelihood."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "squared-error-is-not-the-logistic-likelihood.qmd").read_text(encoding="utf-8")
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

import sympy as sp
z=sp.symbols('z',real=True);o=1/(1+sp.exp(-z))
for y in [0,1]:
 LS=(o-y)**2/2;LB=-y*sp.log(o)-(1-y)*sp.log(1-o)
 assert sp.simplify(sp.diff(LS,z)-(o-y)*o*(1-o))==0;checks+=1
 assert sp.simplify(sp.diff(LB,z)-(o-y))==0;checks+=1
# Check curvature, including a concrete non-convex square-loss point.
for label in [0,1]:
    half=(o-label)**2/2
    proposed=(o*(1-o))**2+(o-label)*o*(1-o)*(1-2*o)
    assert sp.simplify(sp.diff(half,z,2)-proposed)==0;checks+=1
    logloss=-label*sp.log(o)-(1-label)*sp.log(1-o)
    assert sp.simplify(sp.diff(logloss,z,2)-o*(1-o))==0;checks+=1
assert float(sp.diff((o-1)**2/2,z,2).subs(z,math.log(.01/.99)))<0;checks+=1
for v in [-.99,-.99*.01*.99,-2*.99*.01*.99,-math.log(.01),.5*.99**2,-.1,-.018,.18,.99,.99*.99*.01]:printed(v,6)
# The existing 0.9 and 0.99 output examples share the same conventions.
near(2*.99*.01,.0198);near(.99*.01,.0099)
p=sp.symbols('p',positive=True);q=sp.symbols('q',real=True)
assert sp.expand(p*(1-q)**2+(1-p)*q**2-p*(1-p)-(q-p)**2)==0;checks+=1
print("squared-error-is-not-the-logistic-likelihood:", checks, "numerical and rendered-value checks passed")
