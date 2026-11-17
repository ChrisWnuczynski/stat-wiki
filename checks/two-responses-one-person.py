"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
var=(4+9-2*3)/100;assert np.isclose(var,.07) and f'{math.sqrt(var):.6f}'=='0.264575'
assert f'{math.sqrt(.13):.6f}'=='0.360555'
assert np.isclose((4+9+6)/100,.19) and f'{math.sqrt(.19):.6f}'=='0.435890'
assert f'{.0035/.0017:.6f}'=='2.058824'
assert f'{.0508/.0051:.6f}'=='9.960784'
assert np.isclose(.2-.2*.8,.04)
assert np.isclose((.2-.2*.8)/math.sqrt(.2*.8*.8*.2),.25)
assert np.isclose((0-.2*.8)/math.sqrt(.2*.8*.8*.2),-1)
assert np.all(np.linalg.eigvalsh([[4,3],[3,9]])>0)
for age in [0,20,40,60]:
 severity=6.7118+.0035*age
 prob=1/(1+math.exp(-(-3.6891+.0508*age)))
 assert severity>0 and 0<prob<1
critical=-2*math.log(.05)
assert np.isclose(stats.chi2.ppf(.95,2),critical)
assert f'{critical:.6f}'=='5.991465'
assert f'{math.sqrt(critical):.6f}'=='2.447747'
z=stats.norm.ppf(.975)
assert f'{z:.6f}'=='1.959964'
assert f'{2*z*z:.6f}'=='7.682918'
assert 2*z*z>critical and math.sqrt(critical)>z
assert round(.0035/.0017,1)==2.1 and round(.0508/.0051,1)==10.0
assert [round(math.exp(a),6) for a in [3.594,-.321,-.518]]==[36.379302,0.725423,0.595711]

text = (ROOT / "articles" / "two-responses-one-person.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("two-responses-one-person: all recomputed claims and generated-text checks passed")
