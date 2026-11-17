"""Recompute numerical examples and exercise answers for range."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

a=np.array([4,8,9,11,13]);b=np.array([4,8,9,11,130])
assert np.ptp(a)==9 and np.ptp(b)==126 and np.median(a)==np.median(b)==9
assert np.ptp(b)/np.ptp(a)==14 and np.diff(np.quantile(a,[.25,.75]))[0]==3
A=np.array([2,4,6,8,10]);B=np.array([2,2,6,10,10])
assert np.ptp(A)==np.ptp(B)==8 and A.mean()==B.mean()==6
assert A.var(ddof=1)==10 and B.var(ddof=1)==16
assert round(A.std(ddof=1),3)==3.162
assert np.diff(np.quantile(A,[.25,.75]))[0]==4 and np.diff(np.quantile(B,[.25,.75]))[0]==8
for x,r in [([3,5,8,12],9),([3,5,8,12,7],9),([3,5,8,12,7,20],17)]:
 assert np.ptp(x)==r and np.ptp(100-2*np.array(x))==2*r
assert np.ptp([1000])==0 and np.ptp([0,1000000])==1000000
assert np.ptp([0,0,0,10,10])==np.ptp([0,4,5,6,10])==10
assert 5-(-2)==7 and math.isclose(1.8*8,14.4)
print("range: numerical checks passed")
