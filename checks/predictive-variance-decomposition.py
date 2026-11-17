"""Recompute the mathematical claims and printed values for predictive-variance-decomposition."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"predictive-variance-decomposition.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
w=np.array([.75,.25]);means=np.array([0.,4.]);v=np.array([1.,9.]);m=w@means
within=w@v;between=w@(means-m)**2;second=w@(v+means**2)
eq(m,1);eq(within,3);eq(between,3);eq(second,7);eq(second-m*m,6)
eq(within+between,6);eq(w@(np.array([2.,2.])-2)**2,0)
eq(.5*1+.5*1,1);eq(2+1,3)
eq(stats.norm.var(scale=np.sqrt(2+3)),5)
for token in ['$6$', '7-1=6']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"predictive-variance-decomposition: {count} mathematical and printed-value checks passed")
