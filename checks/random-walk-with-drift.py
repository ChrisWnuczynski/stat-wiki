"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

s0,mu,sigma,n=100,.5,2,16
close(s0+n*mu,108);close(n*sigma*sigma,64);close(math.sqrt(n)*sigma,8);close(stats.norm.cdf(1),.8413447461)
close(120+9*.5,124.5);close(math.sqrt(9)*2,6)
close(25*(-.2),-5);close(25*.64,16);close(math.sqrt(25*.64),4)
close(min(4,10)*3,12)
# Build covariance directly from shared independent increments.
L=np.tril(np.ones((10,10)));cov=3*L@L.T
for i in range(10):
 for j in range(10):close(cov[i,j],3*min(i+1,j+1))
# Forecast error combines independent future noise and estimated drift.
T,h,var=21,5,4
close(h*var+h*h*var/(T-1),25)
x=np.array([100,101,103,102,105]);close(np.diff(x).mean(),(x[-1]-x[0])/(len(x)-1))
print("random-walk-with-drift: numerical checks passed")
