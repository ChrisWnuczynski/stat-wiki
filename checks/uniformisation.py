"""Recompute numerical examples and exercise answers for uniformisation."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

Q=np.array([[-2.,2],[3,-3]])
for gamma in [3.,5.,10.]:
 R=np.eye(2)+Q/gamma;assert np.min(R)>=0 and np.allclose(R.sum(axis=1),1)
 result=sum(stats.poisson.pmf(n,gamma)*np.linalg.matrix_power(R,n) for n in range(100))
 assert np.allclose(result,linalg.expm(Q))
R=np.array([[.6,.4],[.6,.4]]);assert np.allclose(R@R,R)
assert round(.4*(1-math.exp(-5)),6)==.397305 and np.isclose(.6*2+.4*3,2.4) and np.isclose(5-2.4,2.6)
assert 1-4/3<0 and np.isclose(1-4/5,.2)
assert np.isclose(stats.poisson.sf(20,5),8.1093e-8,rtol=1e-5,atol=0)
M=20;P=sum(stats.poisson.pmf(n,5)*np.linalg.matrix_power(R,n) for n in range(M+1))
assert np.allclose(P.sum(axis=1),stats.poisson.cdf(M,5))
assert np.max(linalg.expm(Q)-P)<=stats.poisson.sf(M,5)+1e-14
assert np.allclose(linalg.expm(np.zeros((2,2))),np.eye(2))
print("uniformisation: numerical checks passed")
