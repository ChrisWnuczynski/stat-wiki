"""Recompute the mathematical claims and printed values for scree-plot."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"scree-plot.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
l=np.array([5.,2.,1.,.5,.5]);eq(l.sum(),9);c=np.cumsum(l)/l.sum()
eq(c[1],7/9);eq(c[2],8/9);eq(c[3],8.5/9)
eq(np.argmax(c>=.8)+1,3);eq(np.argmax(c>=.9)+1,4)
eq(100*(1-c[1]),22.22222222222222);eq(-np.diff(l),[3,1,.5,0])
R=.6**np.abs(np.subtract.outer(np.arange(8),np.arange(8)))
eig=np.linalg.eigvalsh(R)[::-1];cum=100*np.cumsum(eig)/eig.sum()
eq(np.round(cum),[39,62,75,83,89,93,97,100]);eq(np.trace(R),8);eq(eig.mean(),1)
for token in ['77.777778', '88.888889', '94.444444']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"scree-plot: {count} mathematical and printed-value checks passed")
