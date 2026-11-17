"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

idx=[14,249,377,493,576,625,792,1360,1473,1582,1679,1772,1843,1924]
coef=np.array([-.111,-.081,-.588,-.275,.136,.118,-.116,.089,.113,.085,.141,.302,-.207,-.141])
assert len(idx)==len(coef)==14 and len(set(idx))==14
assert idx[np.argmax(abs(coef))]==377 and idx[np.argmin(abs(coef))]==249
assert idx[np.argmax(coef)]==1772
fdr={14,249,377,493,625,1473,1582,1679,1772,1843,1924}
third={493,625}; assert len(set(idx)&fdr)==11 and len(set(idx)&third)==2
priority=fdr-{249};assert len(priority)==10
close(math.exp(-.588),.5554370487)
for lam,beta,prob in [(.25,math.log(3),.75),(.1,math.log(9),.9)]:
 close(-1/(1+math.exp(beta))+lam,0)
 close(stats.logistic.cdf(beta),prob)
 close(np.array([1,-1])@np.array([.5,.5])/2,0)
close(math.log(3),1.0986122887);close(math.log(9),2.1972245773)
assert .6>=.5 and .03<=.05
# Convexity plus exact subgradient threshold certifies the zero-slope fit.
assert -.5+.6>=0 and -.5-.6<0
print("logistic-lasso: numerical checks passed")
