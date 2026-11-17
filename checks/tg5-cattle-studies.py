"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
nest=[3,1,1,4,1,1,1,1,1,1,1]
assert len(nest)==11 and sum(nest)==16
assert len(nest)+3==14 and sum(nest)+3==19
v,tau2=.2**2,.1**2
prec=1/v+1/tau2
mean=(.3/v+.1/tau2)/prec
assert np.isclose(prec,125) and np.isclose(mean,.14)
assert np.isclose(1/prec,.008)
assert f'{math.sqrt(1/prec):.6f}'=='0.089443'
assert np.isclose((.3/.01+.1/.01)/(1/.01+1/.01),.2)
assert np.isclose(1/(1/.01+1/.01),.005)
assert np.isclose((.3/v+0/tau2)/prec,.06)

text = (ROOT / "articles" / "tg5-cattle-studies.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("tg5-cattle-studies: all recomputed claims and generated-text checks passed")
