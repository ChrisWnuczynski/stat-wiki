"""Recompute the mathematical claims and printed values for properties-of-a-probability."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"properties-of-a-probability.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
a=.3;b=.4;both=.1
union=a+b-both;eq(union,.6);eq(1-union,.4);eq(a+b-2*both,.5)
eq([both,a-both,b-both,1-union],[.1,.2,.3,.4]);eq(a*b,.12)
eq(max(a,b),.4);eq(min(1,a+b),.7)
eq((1-a)*(1-b),.42);eq(a+b-a*b,.58)
eq(.2*.2,.04);eq(.1+.2+.3,.6)
for token in ['0.58', '0.42']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"properties-of-a-probability: {count} mathematical and printed-value checks passed")
