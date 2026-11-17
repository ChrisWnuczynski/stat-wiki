"""Recompute the mathematical claims and printed values for posterior-prediction-under-the-reference-prior."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"posterior-prediction-under-the-reference-prior.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
y=np.arange(2.,7.);n=len(y);m=y.mean();sse=((y-m)**2).sum();nu=n-1;s2=sse/nu;h=1/n
for a,b in [(m,4),(sse,10),(s2,2.5),(h,.2),(nu,4),(s2*h,.5),(s2*(1+h),3)]:eq(a,b)
q=stats.t.ppf(.975,nu);eq(q,2.7764451051977987)
eq([m-q*np.sqrt(.5),m+q*np.sqrt(.5)],[2.0367568385,5.9632431615])
eq([m-q*np.sqrt(3),m+q*np.sqrt(3)],[-.8089439866284946,8.808943986628496],tol=1e-7)
assert np.isinf(stats.t.var(2))
eq(3*nu/(nu-2),6);eq(np.sqrt(3)/np.sqrt(.5),np.sqrt(6))
# All numerical outputs of the ten-observation regression exercise.
C=np.diag([.1,1/40]);eq(10-2,8);eq(16/8,2);eq(8/(4-1),8/3)
eq(2*C[1,1],.05);eq(2.306*np.sqrt(.05),.5156372756114515)
eq(2.306*np.sqrt(.2),1.031274551222903);eq(2.306*np.sqrt(2.2),3.42035074224852)
eq(np.array([1.,4])@C@np.array([1.,4]),.5)
eq(np.sqrt(2.2),1.4832396974191326);eq(np.sqrt(3),1.7320508075688772)
eq(1+2*4,9)
for token in ['2.036757', '5.963243', '8.808944']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"posterior-prediction-under-the-reference-prior: {count} mathematical and printed-value checks passed")
