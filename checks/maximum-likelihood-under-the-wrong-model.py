"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

for m,v,n,sd in [(4,12,100,.3464101615),(4,2,100,.1414213562)]:
 A=1/m;B=v/m**2
 close(B/A**2/n,v/n);close(math.sqrt(v/n),sd)
close(math.sqrt(4/100),.2);close(math.sqrt(12/4),math.sqrt(3))
close(math.sqrt(9/400),.15);close(math.sqrt(36/400),.3)
# Population expected Poisson log-likelihood is maximized at its true mean.
from scipy.optimize import minimize_scalar
for mean in [2,4,9]:
 f=lambda l:-(mean*math.log(l)-l)
 opt=minimize_scalar(f,bounds=(.01,20),method='bounded')
 close(opt.x,mean,tol=2e-5)
print("maximum-likelihood-under-the-wrong-model: numerical checks passed")
