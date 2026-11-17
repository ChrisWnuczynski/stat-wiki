"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

n,x=10,7;p=x/n
score=lambda z:x/z-(n-x)/(1-z)
close(score(p),0); assert -x/p**2-(n-x)/(1-p)**2<0
close((.7**7*.3**3)/.5**10,2.2769316864)
close(math.sqrt(.7*.3/10),.1449137675);close(p/(1-p),7/3)
close(.9**10,.3486784401)
close(3/12,.25);close(math.sqrt(.25*.75/12),.125);close(.25/.75,1/3)
close((1+8)/(2+10),.75);close((1/2+8/10)/2,.65)
for n in [1,5,10]:
 grid=np.linspace(0,1,1001)
 assert np.argmax((1-grid)**n)==0 and np.argmax(grid**n)==1000
for p in [.1,.5,.9]:
 xx=np.arange(11);prob=stats.binom.pmf(xx,10,p)
 close(prob@(xx/10),p);close(prob@(xx/10-p)**2,p*(1-p)/10)

from scipy.optimize import minimize_scalar
opt=minimize_scalar(lambda p:-(7*math.log(p)+3*math.log(1-p)),bounds=(1e-8,.2),method="bounded")
close(opt.x,.2,tol=1e-5);close(min(.7,.2),.2)

print("maximum-likelihood-for-a-binomial-proportion: numerical checks passed")
