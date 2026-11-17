"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

t=6*.488/1.1
assert round(t,2)==2.66 and round(stats.chi2.cdf(t,6),4)==.1501
q=stats.chi2.ppf(.05,6)
assert round(q,3)==1.635 and round(1.1*q/6,4)==.2998
assert round(stats.chi2.sf(15,10),4)==.1321
assert stats.chi2.cdf(q*1.1/.55,6)>.05
assert round(6*.488/1.1,4)==2.6618
assert round(stats.chi2.ppf(.05,6),4)==1.6354
print("chi-squared-test-for-a-variance: numerical checks passed")
