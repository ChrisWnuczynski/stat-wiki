"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
x=[Fraction(0),Fraction(1),Fraction(10)];mu=sum(x)/3
one=sum((v-mu)**2 for v in x);two=Fraction(1,2)
assert mu==Fraction(11,3) and one==Fraction(182,3)==Fraction(546,9)
assert f'{float(one):.6f}'=='60.666667'
reduction=Fraction(2,3)*(Fraction(1,2)-10)**2
assert reduction==Fraction(361,6)==one-two
assert f'{float(reduction):.6f}'=='60.166667'
assert sum((v-v)**2 for v in x)==0
assert (7-7)**2+(7-7)**2==0

# Deepened research calculations.
from fractions import Fraction as F
assert F(182, 3) - F(1, 2) == F(361, 6)
assert f"{float(F(361, 6)):.6f}" == "60.166667"

text = (ROOT / "articles" / "why-the-raw-sum-of-squares-cannot-choose.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("why-the-raw-sum-of-squares-cannot-choose: all recomputed claims and generated-text checks passed")
