"""Recompute the mathematical claims and printed values for posterior-class-probability."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"posterior-class-probability.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
a=.2*.6;b=.8*.1;eq([a,b],[.12,.08]);eq(a+b,.2)
eq(a/(a+b),.6);eq(b/(a+b),.4);eq((.2/.8)*(.6/.1),1.5)
eq(4/(4+1),.8);eq(.5*.6/(.5*.6+.5*.1),6/7)
eq(5*a/(5*a+5*b),.6);eq(2/(2+1),2/3)
eq([1-.6,1-.4],[.4,.6]);eq([4*.4,1*.6],[1.6,.6])
for token in ['0.857143', '0.20']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"posterior-class-probability: {count} mathematical and printed-value checks passed")
