"""Recompute the numerical examples, exercises and answers for sampling-law-of-the-normal-mean-and-scatter."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "sampling-law-of-the-normal-mean-and-scatter.qmd").read_text(encoding="utf-8")
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

S=np.array([[4.,1.],[1.,9.]]);c=np.array([1.,-1.]);printed(np.linalg.det(S));printed(c@S@c/10);printed(c@S@c);printed(c@S@c/20)
assert np.all(np.linalg.eigvalsh(S)>0);checks+=1
assert np.allclose(9*S,[[36,9],[9,81]]);checks+=1
assert np.allclose(19*S,[[76,19],[19,171]]);checks+=1
# Deterministic orthogonal decomposition verifies the mean/scatter identity.
z=np.arange(20,dtype=float).reshape(10,2)/3;x=z@np.linalg.cholesky(S).T+np.array([2.,-1.]);m=x.mean(axis=0);A=(x-m).T@(x-m)
assert np.allclose((x-np.array([2.,-1.])).T@(x-np.array([2.,-1.])),A+10*np.outer(m-np.array([2.,-1.]),m-np.array([2.,-1.])));checks+=1
near(np.linalg.matrix_rank(A),1)
# Divisor n scales the Wishart expectation by (n-1)/n.
near((10-1)/10,0.9)
assert np.allclose((9/10)*S,np.array([[3.6,.9],[.9,8.1]]));checks+=1
printed(0.9,1)
print("sampling-law-of-the-normal-mean-and-scatter:", checks, "numerical and rendered-value checks passed")
