"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
x=np.arange(-2,3,dtype=float);y=x*x
X=np.column_stack([np.ones(5),x]);coef=np.linalg.lstsq(X,y,rcond=None)[0]
assert np.allclose(coef,[2,0]);assert np.allclose(y-X@coef,[2,-1,-2,-1,2])
assert np.isclose(np.sum((y-X@coef)**2),14)
assert np.isclose(np.mean((y-X@coef)**2),2.8)
z=np.array([-1.5,-.5,.5,1.5]);assert np.isclose(np.mean((z*z-2)**2),1.5625)
assert np.sum(y*y)==34
quad=np.column_stack([np.ones(5),x,x*x]);assert np.allclose(np.linalg.lstsq(quad,y,rcond=None)[0],[0,0,1])

text = (ROOT / "articles" / "underfitting.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("underfitting: all recomputed claims and generated-text checks passed")
