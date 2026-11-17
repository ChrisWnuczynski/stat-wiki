"""Recompute the numerical examples, exercises and answers for posterior-predictive-target."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "posterior-predictive-target.qmd").read_text(encoding="utf-8")
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

a=3;b=9;n=4
mean=a/(a+b);var=a*b/((a+b)**2*(a+b+1));k=np.arange(n+1);prob=stats.betabinom.pmf(k,n,a,b)
printed(mean);printed(var,6);near(prob.sum(),1);printed(float(prob@k));printed(float(prob@(k-n*mean)**2),6);printed(n*mean*(1-mean));printed(prob[0],6);printed((1-mean)**n,6);printed(mean*(1-mean),6)
near(n*mean*(1-mean)*(a+b+n)/(a+b+1),float(prob@(k-n*mean)**2))
# Recompute the reference-prior regression example's variance and scales.
near(8/(4-1),8/3);near(.1+16/40,.5)
for h in [.1,.5]:near(math.sqrt(2*(1+h))**2,2*(1+h))
# All displayed reference-prior regression posterior endpoints use the supplied t quantile.
n=10;p=2;sse=16;nu=n-p;s2=sse/nu;a=nu/2;b=sse/2;C=np.diag([1/10,1/40]);betahat=np.array([1.,2.]);critical=2.306
near(a,4);near(b,8);near(s2,2);printed(b/(a-1),4)
slope_scale=math.sqrt(s2*C[1,1]);printed(critical*slope_scale,4)
for endpoint in betahat[1]+np.array([-1.,1.])*critical*slope_scale:printed(endpoint,3)
for value in [0.,4.]:
 z=np.array([1.,value]);h=z@C@z;near(h,.1 if value==0 else .5);near(z@betahat,1 if value==0 else 9)
 printed(math.sqrt(s2*(1+h)),4)
 if value==0:
  for scale in [math.sqrt(s2*h),math.sqrt(s2*(1+h))]:
   printed(critical*scale,4)
   for endpoint in z@betahat+np.array([-1.,1.])*critical*scale:printed(endpoint,3)

print("posterior-predictive-target:", checks, "numerical and rendered-value checks passed")
