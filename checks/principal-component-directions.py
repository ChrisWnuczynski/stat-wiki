"""Recompute the mathematical claims and printed values for principal-component-directions."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"principal-component-directions.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
S=np.array([[2.,1.],[1.,2.]])
Q=np.array([[1.,1.],[1.,-1.]])/np.sqrt(2)
eq(Q.T@Q,np.eye(2));eq(Q.T@S@Q,np.diag([3.,1.]));eq(np.trace(S),4)
x=np.array([2.,0.]);t=x@Q;eq(t,[np.sqrt(2),np.sqrt(2)])
rec=t[0]*Q[:,0];eq(rec,[1,1]);eq(np.sum((x-rec)**2),2)
eq(3/4,.75);eq(1/4,.25);eq((-t[0])*(-Q[:,0]),rec)
for a in [np.array([1.,0.]),np.array([0.,1.]),np.array([1.,1.])/np.sqrt(2)]:eq(a@(2*np.eye(2))@a,2)
u=np.array([-1.,0.,1.]);eq(np.mean((u-u.mean())*(u*u-(u*u).mean())),0)
for token in ['75', '25']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"principal-component-directions: {count} mathematical and printed-value checks passed")
