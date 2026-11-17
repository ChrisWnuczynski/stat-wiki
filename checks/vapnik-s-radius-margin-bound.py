"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
def bound(D,rho,p):return min(math.ceil(D*D/(rho*rho)),p)+1
assert bound(6,2,20)==10
assert bound(6,4,20)==4
assert bound(6,2,4)==5
assert bound(4,3,10)==3
assert bound(30,10,20)==10
assert 6**2/2**2==3**2/1**2==9
assert min(30,7)+1==8

text = (ROOT / "articles" / "vapnik-s-radius-margin-bound.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("vapnik-s-radius-margin-bound: all recomputed claims and generated-text checks passed")
