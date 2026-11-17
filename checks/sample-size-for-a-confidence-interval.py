"""Recompute numerical examples and exercise answers for sample-size-for-a-confidence-interval."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

assert math.ceil((1.96*10/2)**2)==97 and math.ceil((1.96*10)**2)==385
assert round(1.96*10/math.sqrt(96),4)==2.0004 and round(1.96*10/math.sqrt(97),4)==1.9901
assert math.ceil(1.96**2/(4*.03**2))==1068 and math.ceil(1.96**2/(4*.05**2))==385
assert math.ceil(385/.8)==482 and math.isclose(482*.8,385.6)
print('482 invitation assurance',stats.binom.sf(384,482,.8))
assert round(stats.binom.sf(384,482,.8),4)==.5543
assert math.isclose((1.96*6/1.5)**2,61.4656) and math.ceil((1.96*6/1.5)**2)==62
assert math.isclose((1.96*6/.75)**2,245.8624) and math.ceil((1.96*6/.75)**2)==246
p=np.linspace(0,1,101);assert np.all(p*(1-p)<=.25+1e-14)
assert math.ceil(100.2)==101 and 3**2==9
print("sample-size-for-a-confidence-interval: numerical checks passed")

N=10;pop=np.arange(N);sigma2=pop.var();n=4
from itertools import combinations
means=np.array([np.mean(v) for v in combinations(pop,n)])
assert np.isclose(means.var(),sigma2/n*(N-n)/(N-1))
