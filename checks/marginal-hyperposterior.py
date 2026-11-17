"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='marginal-hyperposterior'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

from scipy.special import beta as beta_function
from scipy.integrate import quad
observations=[(1,2),(2,2)]
def marginal(a,b):return np.prod([beta_function(a+y,b+n-y)/beta_function(a,b) for y,n in observations])
close([marginal(1,1),marginal(2,2)],[1/18,3/50]);close(marginal(2,2)/marginal(1,1),27/25)
w=np.array([marginal(1,1),marginal(2,2)]);w=w/w.sum();close(w,[25/52,27/52])
close(w@np.array([3/4,2/3]),147/208)
for a,b in [(1,1),(2,2)]:
 for y,n in observations:
  integral=quad(lambda q:q**y*(1-q)**(n-y)*q**(a-1)*(1-q)**(b-1)/beta_function(a,b),0,1)[0]
  close(integral,beta_function(a+y,b+n-y)/beta_function(a,b))
m,k=sp.symbols('m k',positive=True);ab=sp.Matrix([m*k,(1-m)*k]);check(sp.simplify(ab.jacobian([m,k]).det())==k)
check(sp.Rational(1+1,1+1+2)==sp.Rational(1,2) and sp.Rational(2+1,2+2+2)==sp.Rational(1,2))

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['1/18', '3/50', '27/25', '147/208', '25/52']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
