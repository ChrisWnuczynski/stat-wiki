"""Recompute the mathematical claims and printed values for prior-sensitivity."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"prior-sensitivity.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
priors=[(5,5),(1,1),(.6,.6)]
post=[(a+3,b+7) for a,b in priors]
eq(post,[[8,12],[4,8],[3.6,7.6]])
means=[a/(a+b) for a,b in post];eq(means,[.4,1/3,9/28])
for a,b in post: assert stats.beta.cdf(.5,a,b)>0
probs=[stats.beta.cdf(.5,a,b) for a,b in post]
eq(probs,[.8203582763671875,.88671875,.8956615279061715])
post2=[(a+30,b+70) for a,b in priors];eq(post2,[[35,75],[31,71],[30.6,70.6]])
means2=[a/(a+b) for a,b in post2];eq(means2,[.3181818181818182,.30392156862745096,.3023715415019763])
eq(max(means)-min(means),.07857142857142857);eq(max(means2)-min(means2),.015810276679841917)
eq(10/(10+10)*.2,.1);eq(20/(20+80),.2)
eq((4-1)/(4+8-2),.3);eq(4/12,1/3)
for token in ['0.820358', '0.886719', '0.895662', '0.015810']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"prior-sensitivity: {count} mathematical and printed-value checks passed")
