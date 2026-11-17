"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

assert round(2*stats.norm.cdf(1)-1,4)==.6827
assert round(2*stats.norm.cdf(1.96)-1,4)==.9500
assert round(2*stats.norm.cdf(2)-1,4)==.9545
print('normal multiplier with estimated SD:',2*stats.t.cdf(1.96,9)-1)
assert round(math.sqrt(.95*.05/40),4)==.0345
rng=np.random.default_rng(28);covered=[]
for i in range(40):
 x=rng.normal(10,1,10);half=stats.t.ppf(.975,9)*x.std(ddof=1)/math.sqrt(10)
 covered.append(abs(x.mean()-10)<half)
assert sum(covered)==38
assert math.isclose(math.sqrt(.9*.1/100),.03) and 100*.1==10
assert round(2*stats.t.cdf(1.96,9)-1,4)==.9184
assert math.isclose(40*.95,38)
print("coverage: numerical checks passed")
