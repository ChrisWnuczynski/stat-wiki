"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

p13=stats.binom.sf(12,15,.6);p12=stats.binom.sf(11,15,.6)
assert round(p13,5)==.02711 and round(p12,5)==.09050
assert 1/32==.03125 and 2/32==.0625
z=3*math.sqrt(101)/7;p=2*stats.norm.sf(z);print('blood pressure',z,p)
t=(19.57-19)/(1.4/math.sqrt(40))
assert round(t,3)==2.575 and round(stats.t.sf(t,39),3)==.007
assert round(stats.t.ppf(.99,39),2)==2.43
assert round(p,6)==.000017
print("ingredients-of-a-hypothesis-test: numerical checks passed")
