"""Recompute numerical examples and exercise answers for two-sample-hotelling-t2-test."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

S=np.array([[4.,1],[1,9]]);d=np.array([2.,1]);q=d@np.linalg.solve(S,d);T=120/22*q;F=19/40*T
assert np.allclose(np.linalg.inv(S),np.array([[9,-1],[-1,4]])/35)
assert np.isclose(q,36/35) and round(T,6)==5.610390 and round(F,6)==2.664935
assert round(stats.f.sf(F,2,19),6)==.095462 and round(40/19*stats.f.ppf(.95,2,19),6)==7.414512
A=np.array([[2,1],[0,.5]]);assert np.isclose((A@d)@np.linalg.solve(A@S@A.T,A@d),q)
assert 2.5*4/4==2.5 and round(math.sqrt(2.5),6)==1.581139
# Scalar reduction of the unequal-covariance moment formula to Welch.
v=np.array([4/10,9/12]);n=np.array([10,12]);w=v/v.sum()
f=(1+1)/np.sum((w*w+w*w)/(n-1));welch=v.sum()**2/np.sum(v*v/(n-1))
assert np.isclose(f,welch)
print("two-sample-hotelling-t2-test: numerical checks passed")
