"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

x=np.array([[0,0],[1,0],[0,1],[1,1]],float)
y=np.array([-1,-1,-1,1]);scores=x@np.ones(2)-1.5
close(scores,[-1.5,-.5,-.5,.5]);assert np.all(y*scores>0)
close(min(y*scores),.5);close(.5/np.sqrt(2),.3535533906)
close((x[[1,2]].mean(0)),x[[0,3]].mean(0))
xor=np.array([-1,1,1,-1]);f=x[:,0]+x[:,1]-2*x[:,0]*x[:,1]-.5
assert np.all(xor*f>0)
close(np.array([-1,1])*np.array([-1,1]),[1,1]);close(2/np.linalg.norm([3,4]),.4)
# Recompute all boundary slopes quoted in the definition.
close([-a/b for a,b in [(1,-2),(.5,1),(1,1),(2,1)]],[.5,-.5,-1,-2])
print("linear-separability: numerical checks passed")
