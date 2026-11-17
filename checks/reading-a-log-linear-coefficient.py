"""Recompute the numerical examples, exercises and answers for reading-a-log-linear-coefficient."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "reading-a-log-linear-coefficient.qmd").read_text(encoding="utf-8")
checks = 0
def near(a, b, tol=1e-9):
    global checks
    assert math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol), (a,b)
    checks += 1
def printed(value, decimals=3):
    global checks
    token = f"{value:.{decimals}f}"
    assert token in article, ("Printed value missing",token)
    checks += 1

f=math.exp(.3)
for v in [f,math.exp(.6),math.exp(-.3),100*(f-1),5*f,5*math.exp(.6)]:printed(v,6)
printed(2*1.5);near(f*f,math.exp(.6));near(f*math.exp(-.3),1)
# Earlier speed/wet-road comparisons.
for b,h in [(.02,1),(.02,10),(-.5,1)]:near(math.exp(b*h),math.exp(b)**h)
near(math.exp(.1),1.1051709180756477)
# Unit-change and road-condition calculations from the interpretation.
printed(math.exp(.02),3);printed(math.exp(.2),2);printed(math.exp(-.5),2);printed(math.exp(.1),2)
near(100*(math.exp(.2)-1),22.140275816016985)


# Interaction contrast at z=4, and the one-unit factor at z=0.
printed(math.exp(-.2),6); printed(math.exp(.2),6)
near(math.exp(.2-.1*4), math.exp(-.2))
print("reading-a-log-linear-coefficient:", checks, "numerical and rendered-value checks passed")
