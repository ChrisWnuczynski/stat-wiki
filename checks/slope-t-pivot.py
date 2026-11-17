"""Recompute the numerical examples, exercises and answers for slope-t-pivot."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "slope-t-pivot.qmd").read_text(encoding="utf-8")
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

n=6;sxx=17.5;b=1.2;s=.7;se=s/math.sqrt(sxx);t=b/se;c=stats.t.ppf(.975,4)
for v in [se,t,c,b-c*se,b+c*se,2*stats.t.sf(t,4),3*(b-c*se),3*(b+c*se),(b-1)/se]:printed(v,6)
printed(3*b)
x=np.arange(1,7,dtype=float);near(((x-x.mean())**2).sum(),17.5);near((((x-100)-(x-100).mean())**2).sum(),17.5)
# Heart-rate calculation already printed in the source example.
near(.1205/math.sqrt(2518),.0024013638,tol=1e-5)
near(.03865/.00240,16.1041666667,tol=1e-9)

# Independently refit all19 heart-rate/oxygen pairs in the carried example.
x=np.array([94,96,95,95,94,95,94,104,104,106,108,110,113,113,118,115,121,127,131])
y=np.array([.473,.753,.929,.939,.832,.983,1.049,1.178,1.176,1.292,1.403,1.499,1.529,1.599,1.749,1.746,1.897,2.040,2.231])
X=np.column_stack([np.ones(len(x)),x]);b=np.linalg.lstsq(X,y,rcond=None)[0]
S=np.sqrt(np.sum((y-X@b)**2)/(len(x)-2));C=np.linalg.inv(X.T@X);se=S*np.sqrt(np.diag(C))
near(x.mean(),107);near(np.sum((x-x.mean())**2),2518)
printed(b[0],3);printed(b[1],5);printed(S,4);printed(se[1],5);printed(se[0],3)
for endpoint in b[1]+stats.t.ppf([.025,.975],17)*se[1]:printed(endpoint,4)
printed(b[1]/se[1],1)
print("slope-t-pivot:", checks, "numerical and rendered-value checks passed")
