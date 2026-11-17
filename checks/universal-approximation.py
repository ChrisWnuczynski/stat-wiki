"""Recompute numerical examples and exercise answers for universal-approximation."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

r=lambda z:np.maximum(0,z)
x=np.linspace(0,1,10001);F=.25*x+.5*r(x-.25)+.5*r(x-.5)+.5*r(x-.75)
assert np.isclose(np.max(F-x*x),1/64) and np.min(F-x*x)>-1e-14
for knot in [0,.25,.5,.75,1]:
 val=.25*knot+.5*r(knot-.25)+.5*r(knot-.5)+.5*r(knot-.75)
 assert np.isclose(val,knot*knot)
assert .5*.25==1/8 and .25**2==1/16 and 1/8-1/16==1/16
assert 1/(4*5**2)==.01 and 1/(4*4**2)>.01
assert 2-1>.5
print("universal-approximation: numerical checks passed")
