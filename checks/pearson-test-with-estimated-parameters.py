"""Recompute the mathematical claims and printed values for pearson-test-with-estimated-parameters."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"pearson-test-with-estimated-parameters.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
x=np.array([12,18,25,45]);n=x.sum();theta=(x[0]+x[1])/(2*n)
eq(n,100);eq(theta,.15)
e=n*np.array([theta,theta,.5-theta,.5-theta]);eq(e,[15,15,35,35])
eq((x-e)**2/e,[.6,.6,20/7,20/7])
t=float(np.sum((x-e)**2/e));eq(t,6.914285714285714)
eq(stats.chi2.sf(t,2),math.exp(-t/2))
eq(round(stats.chi2.sf(t,2),6),.031520)
eq(4-1-1,2);eq(6-1-2,3)
p=e/n;q=np.sqrt(p);A=np.array([1,1,-1,-1])/np.sqrt(p)
P=np.eye(4)-np.outer(q,q)-np.outer(A,A)/(A@A)
eq(P@P,P);eq(np.trace(P),2);eq(P@A,np.zeros(4));eq(P@q,np.zeros(4))
for token in ['6.914286', '0.031520']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"pearson-test-with-estimated-parameters: {count} mathematical and printed-value checks passed")
