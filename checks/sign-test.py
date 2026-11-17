"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
tail=sum(math.comb(12,k) for k in range(10,13))
assert tail==79
assert f'{tail/2**12:.6f}'=='0.019287'
assert f'{2*tail/2**12:.6f}'=='0.038574'
tail8=sum(math.comb(12,k) for k in range(8,13))
assert tail8==794 and f'{tail8/2**12:.6f}'=='0.193848'
x=np.array([3.5,5,8,6,7,6,5,7,5.5,6.5,7,8]);y=np.array([4,4.5,9,6.5,6.5,5.5,5.5,8,6.5,6,8,9])
assert (y>x).sum()==8 and np.count_nonzero(x==y)==0
assert 14-2==12

# Deepened research calculations.
import math
from math import comb
assert comb(6,5)+comb(6,6) == 7
assert 7/64 == 0.109375
assert comb(5,4)+comb(5,5) == 6 and 6/32 == 0.1875
assert f"{4/math.sqrt(3):.3f}" == "2.309"
assert comb(12,10)+comb(12,11)+comb(12,12) == 79
assert f"{79/4096:.6f}" == "0.019287"
assert comb(12,8)+comb(12,9)+comb(12,10)+comb(12,11)+comb(12,12) == 794
assert f"{794/4096:.6f}" == "0.193848"

text = (ROOT / "articles" / "sign-test.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("sign-test: all recomputed claims and generated-text checks passed")
