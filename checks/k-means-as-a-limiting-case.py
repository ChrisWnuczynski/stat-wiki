"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

from scipy.special import expit
assert np.allclose([expit(4/e) for e in [2,1,.5]],[.88080,.98201,.99966],atol=5e-6)
x=np.array([0,1,5,6]);c=np.array([0,6]);d=(x[:,None]-c)**2;labels=d.argmin(1);means=np.array([x[labels==j].mean() for j in range(2)])
assert np.allclose(means,[.5,5.5]) and sum(d.min(1))==2 and sum((x-means[labels])**2)==1
for e in [2,1,.5,.1]:
 assert math.isclose(math.exp(-4/(2*e))/(2*math.exp(-4/(2*e))),.5)
 soft=-2*e*np.log(np.exp(-d/(2*e)).sum(1));mins=d.min(1)
 assert np.all(soft<=mins+1e-12) and np.all(soft>=mins-2*e*math.log(2)-1e-12)
for eps in [1,.1,.01]:
 odds=(.1/.9)*math.exp(-(9-1)/(2*eps))
 assert 0<odds<.1/.9
assert math.isclose(.2/(.2+.8),.2)
print("k-means-as-a-limiting-case: numerical checks passed")
