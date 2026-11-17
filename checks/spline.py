"""Recompute the mathematical claims and printed values for spline."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"spline.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
g=lambda x:x+2*np.maximum(x,0)**3
eq(g(np.array([-1.,0.,1.])),[-1,0,3]);eq(6*2,12)
eq(integrate.quad(lambda x:(12*x)**2,0,1)[0],48)
eq(integrate.quad(lambda x:(6*x)**2,0,1)[0],12)
eq(3+4,7);eq(3+2,5);eq(6*1,6)
# Basis derivative joins and penalty null space by exact symbolic differentiation.
import sympy as sp
x=sp.symbols('x');right=x+2*x**3;left=x
for order,value in [(0,0),(1,1),(2,0)]:
 eq(float(sp.diff(right,x,order).subs(x,0)),value);eq(float(sp.diff(left,x,order).subs(x,0)),value)
eq(float(sp.diff(4-3*x,x,2)),0)
for token in ['48', '12']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"spline: {count} mathematical and printed-value checks passed")
