"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

z=1.96
assert round(z*z/(20+z*z),4)==.1611
assert round(1-.025**(1/20),4)==.1684
assert round(z*z/(10+z*z),4)==.2775
p1=55/160;p2=60/192;d=p1-p2;se=math.sqrt(p1*(1-p1)/160+p2*(1-p2)/192)
assert d==.03125 and round(se,6)==.050288
assert round(d-z*se,4)==-.0673 and round(d+z*se,4)==.1298
assert round(p1,3)==.344 and round(p2,3)==.312
assert round(math.sqrt(.344*.656/160+.313*.688/192),4)==.0503
print("interval-for-a-proportion: numerical checks passed")
