"""Recompute the numerical examples, exercises and answers for random-seed."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "random-seed.qmd").read_text(encoding="utf-8")
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

def states(seed,n):
 out=[]
 for _ in range(n):out.append(seed);seed=(5*seed+1)%8
 return out
assert states(1,9)==[1,6,7,4,5,2,3,0,1];checks+=1
assert states(3,9)==[3,0,1,6,7,4,5,2,3];checks+=1
assert states(0,4)==[0,1,6,7];checks+=1
for v in [1/8,6/8,7/8,0/8]:printed(v)
assert len(set(states(1,8)))==8;checks+=1
for seed in range(8):assert len(set(states(seed,8)))==8;checks+=1
print("random-seed:", checks, "numerical and rendered-value checks passed")
