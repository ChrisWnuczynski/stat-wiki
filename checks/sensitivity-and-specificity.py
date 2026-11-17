"""Recompute the mathematical claims and printed values for sensitivity-and-specificity."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"sensitivity-and-specificity.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
a,b,c,d=40,10,10,190
eq(a/(a+b),.8);eq(d/(c+d),.95);eq((a+d)/(a+b+c+d),.92);eq(a/(a+c),.8)
pi=.01;se=.8;sp=.95;pos=pi*se+(1-pi)*(1-sp)
eq(pos,.0575);eq(pi*se/pos,.1391304347826087);eq([10000*pi*se,10000*(1-pi)*(1-sp)],[80,495])
eq(.5*.8/(.5*.8+.5*.05),16/17)
# Reverse-conditional and threshold values in the accompanying examples.
eq([10*.8,190*.1],[8,19]);eq([100*.8,100*.1],[80,10]);eq(8/(8+19),8/27);eq(80/90,8/9)
diseased=np.array([.2,.6,.8]);healthy=np.array([.1,.3,.4])
eq([np.mean(diseased>=.5),np.mean(healthy<.5)],[2/3,1]);eq([np.mean(diseased>=.2),np.mean(healthy<.2)],[1,1/3])
for token in ['0.139130', '0.941176']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"sensitivity-and-specificity: {count} mathematical and printed-value checks passed")
