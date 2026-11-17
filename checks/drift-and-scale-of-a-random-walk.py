"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

assert math.isclose(.6-.4,.2) and math.isclose(1-.2**2,.96)
assert round(math.sqrt(96),4)==9.7980
print('biased negative endpoint',stats.binom.cdf(49,100,.6))
assert round(stats.binom.cdf(49,100,.6),5)==.01676
assert round(math.sqrt(24),4)==4.8990 and math.isclose(.2*96,2*math.sqrt(.96*96))
assert round(stats.norm.sf(2),5)==.02275
print('symmetric exact tail',stats.binom.sf(60,100,.5))
print("drift-and-scale-of-a-random-walk: numerical checks passed")
