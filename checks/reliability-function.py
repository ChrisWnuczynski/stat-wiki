"""Recompute the numerical examples, exercises and answers for reliability-function."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "reliability-function.qmd").read_text(encoding="utf-8")
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

p=[.9,.8,.7]
def rel(p):
 return sum(float(x[0] and (x[1] or x[2]))*math.prod(pi if xi else 1-pi for pi,xi in zip(p,x)) for x in itertools.product([0,1],repeat=3))
r=rel(p);printed(r);printed(.9*.9,2);printed(1-.1*.1,2)
for i,step in [(0,.01),(1,.01),(2,.1)]:
 q=p.copy();q[i]+=step;printed(rel(q)-r,6)
printed(rel([.9,.8,.8]));printed(stats.binom.sf(1,3,.9))
near(2*.9**2+2*.9**3-5*.9**4+2*.9**5,.97848)
near(1-(1-.9**2)**2,.9639)
near((.97848-.9639)/(1-.9639),.4038781163434903)
near(3/2-2/3,5/6)
# Enumerate all 32 bridge states to check the polynomial independently.
def bridge(state):
 a,b,c,d,e=state
 return (a and d) or (b and e) or (a and c and e) or (b and c and d)
bridge_prob=sum(float(bridge(state))*math.prod(.9 if bit else .1 for bit in state) for state in itertools.product([0,1],repeat=5))
near(bridge_prob,2*.9**2+2*.9**3-5*.9**4+2*.9**5);printed(bridge_prob,4)
printed(1-(2*.1**2+2*.1**3),3);printed(1-(1-.81)**2,3)
# Survival integrals verify the two stated mean-lifetime constants at rate one.
from scipy.integrate import quad
near(quad(lambda t:2*math.exp(-t)-math.exp(-2*t),0,np.inf)[0],3/2)
near(quad(lambda t:3*math.exp(-2*t)-2*math.exp(-3*t),0,np.inf)[0],5/6)
printed(.9*(.9+.9-.9**2),3)


# Series and parallel reliabilities of the same three components.
printed(.9*.8*.7,3); printed(1-.1*.2*.3,3)
near(.9*.8*.7,.504); near(1-.006,.994)
print("reliability-function:", checks, "numerical and rendered-value checks passed")
