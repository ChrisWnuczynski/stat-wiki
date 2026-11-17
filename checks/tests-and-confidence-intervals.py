"""Recompute numerical examples and exercise answers for tests-and-confidence-intervals."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

c=stats.t.ppf(.975,15);lo,hi=12-c,12+c
assert round(c,5)==2.13145 and round(lo,5)==9.86855 and round(hi,5)==14.13145
assert round(2*stats.t.sf(2,15),5)==.06395 and round(2*stats.t.sf(3,15),5)==.00897
assert round(stats.t.sf(2,15),5)==.03197 and round(12-stats.t.ppf(.95,15),5)==10.24695
for null in np.linspace(5,20,100):assert (abs(12-null)>c)==(null<lo or null>hi)
assert [2.1<=x<=4.7 for x in [2,3,5]]==[False,True,False]
assert 1-.01==.99
print("tests-and-confidence-intervals: numerical checks passed")
