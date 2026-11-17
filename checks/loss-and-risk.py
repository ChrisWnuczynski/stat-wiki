"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

p=np.array([.2,.5,.3]);v=np.array([0,1,4]);mean=p@v
close(mean,1.7)
close(p@(v-mean)**2,2.41);close(p@(v-1)**2,2.9)
close(p@abs(v-1),1.1);close(p@abs(v-mean),1.38)
risk=lambda a,t:a*a+(a-1)**2*t*t
close([risk(1,0),risk(.5,0),risk(1,2),risk(.5,2)],[1,.25,1,1.25])
close(risk(.5,math.sqrt(3)),1);close(.2+.4**2,.36)
assert .36<.5 and 2**2==4
# Empirical absolute, square and maximum losses have distinct minimizers.
y=np.array([0,1,9]);grid=np.linspace(0,9,9001)
close(grid[np.argmin(((grid[:,None]-y)**2).sum(1))],10/3,tol=.001)
close(grid[np.argmin(abs(grid[:,None]-y).sum(1))],1)
close(grid[np.argmin(abs(grid[:,None]-y).max(1))],4.5)
print("loss-and-risk: numerical checks passed")
