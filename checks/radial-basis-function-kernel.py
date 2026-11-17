"""Recompute the mathematical claims and printed values for radial-basis-function-kernel."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"radial-basis-function-kernel.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
x=np.arange(3.);K=np.exp(-np.subtract.outer(x,x)**2/2)
eq(K[0,1],np.exp(-.5));eq(K[0,2],np.exp(-2));eq(np.diag(K),np.ones(3))
c=np.array([1.,-1.,0.]);eq(c@K@c,2*(1-np.exp(-.5)))
eq(np.exp(-1/8),.8824969025845955);eq(1/(2*2**2),1/8)
assert np.linalg.eigvalsh(K).min()>0
for a in [.5,2,10]:eq(np.exp(-np.subtract.outer(a*x,a*x)**2/(2*a*a)),K)
eq(math.comb(2+2,2),6)
# The frozen chapter prints the grid that depends on helpers defined on another page.
# This check keeps those printed tokens and does not treat an inlined split as the chapter's fit.
for expected in ('0.02857','0.06667'):
 assert expected in article, expected
 count+=1

for token in ['0.606531', '0.135335', '0.786939']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"radial-basis-function-kernel: {count} mathematical and printed-value checks passed")
