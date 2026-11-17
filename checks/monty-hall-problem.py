"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

from itertools import product
for q in [0,.25,.5,.8,1]:
 atoms={('A','B'):F(str(q))/3,('A','C'):(1-F(str(q)))/3,('B','C'):F(1,3),('C','B'):F(1,3)}
 total=sum(v for (prize,opened),v in atoms.items() if opened=='B')
 stay=atoms[('A','B')]/total;switch=atoms[('C','B')]/total
 close(float(stay),q/(1+q));close(float(switch),1/(1+q))
 assert sum(v for (prize,opened),v in atoms.items() if prize!='A')==F(2,3)
 if q==.5:assert total==F(1,2) and stay==F(1,3) and switch==F(2,3)
 if q==.8:assert stay==F(4,9) and switch==F(5,9)
 if q==.25:assert stay==F(1,5) and switch==F(4,5)
# An ignorant host's named empty-door observation has equal likelihood under A and C.
close((1/3*.5)/(1/3*.5+1/3*.5),.5)
close((10-1)/10,.9)
print("monty-hall-problem: numerical checks passed")
