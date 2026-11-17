"""Recompute numerical examples and exercise answers for residuals-in-a-glm."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

def pd(y,mu):return np.sign(y-mu)*math.sqrt(2*((y*math.log(y/mu) if y else 0)-(y-mu)))
assert round((1-.7)/math.sqrt(.7*.3),3)==.655 and round(-.7/math.sqrt(.7*.3),2)==-1.53
assert round((7-2)/math.sqrt(2),2)==3.54 and round((45-50)/math.sqrt(50),2)==-.71
assert round(pd(7,2),4)==2.7457 and round(pd(45,50),4)==-.7194 and round(pd(55,50),4)==.6958
assert round(math.sqrt(-2*math.log(.7)),4)==.8446 and round(-math.sqrt(-2*math.log(.3)),4)==-1.5518
assert round(math.sqrt(2*math.log(2)),4)==1.1774
assert round(-math.sqrt(3),4)==-1.7321 and round(pd(0,3),4)==-2.4495
assert round(stats.poisson.pmf(7,2),6)!=round(stats.poisson.pmf(45,50),6)
for delta in [.001,-.001]:
 exact=pd(50+delta,50)**2;approx=delta**2/50-delta**3/(3*50**2);assert np.isclose(exact,approx,rtol=1e-6,atol=1e-14)
assert 4/math.sqrt(4)==2 and sum(x*x for x in [-1,0,2,-3])==14
print("residuals-in-a-glm: numerical checks passed")
