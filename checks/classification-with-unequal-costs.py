"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

def decision(p,fp,fn):return int((1-p)*fp<p*fn)
assert decision(.2,1,9)==1 and decision(.05,1,9)==0
assert math.isclose((1-.2),.8) and math.isclose(.2*9,1.8)
assert math.isclose((1-.05),.95) and math.isclose(.05*9,.45)
assert 4/(4+1)==.8 and decision(.7,4,1)==0
assert math.isclose((1-.7)*4,1.2)
for p in np.linspace(0,1,101):
 assert decision(p,4,1)==decision(p,40,10)
print("classification-with-unequal-costs: numerical checks passed")
