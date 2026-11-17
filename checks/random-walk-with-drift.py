"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='random-walk-with-drift'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

s0,mu,sigma,n=100,.5,2,16
close(s0+n*mu,108);close(n*sigma*sigma,64);close(math.sqrt(n)*sigma,8);close(stats.norm.cdf(1),.8413447461)
close(120+9*.5,124.5);close(math.sqrt(9)*2,6)
close(25*(-.2),-5);close(25*.64,16);close(math.sqrt(25*.64),4)
close(min(4,10)*3,12)
# Build covariance directly from shared independent increments.
L=np.tril(np.ones((10,10)));cov=3*L@L.T
for i in range(10):
 for j in range(10):close(cov[i,j],3*min(i+1,j+1))
# Forecast error combines independent future noise and estimated drift.
T,h,var=21,5,4
close(h*var+h*h*var/(T-1),25)
x=np.array([100,101,103,102,105]);close(np.diff(x).mean(),(x[-1]-x[0])/(len(x)-1))
# Compare computed values with the worked example and hidden answer.
assert f"N({s0+n*mu:g},{n*sigma*sigma:g})" in EXAMPLE
assert rf"\approx{stats.norm.cdf(1):.6f}" in EXAMPLE
assert f"forecast is ${120+9*mu:g}$" in EXAMPLE
assert f"mean is $25(-0.2)={25*(-.2):g}$" in ANSWER
assert f"variance is $25(0.64)={25*.64:g}$" in ANSWER
print("random-walk-with-drift: numerical checks passed")
