"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='local-minima-plateaus-and-symmetry'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

u,v=sp.symbols('u v',real=True); L=u*u-v*v
check(sp.Matrix([sp.diff(L,z) for z in [u,v]]).subs({u:0,v:0})==sp.zeros(2,1))
check(set(sp.hessian(L,[u,v]).eigenvals())=={-2,2})
step=[sp.Rational(4,5)*u,sp.Rational(6,5)*v]
check(L.subs(dict(zip([u,v],step)),simultaneous=True)==sp.Rational(16,25)*u*u-sp.Rational(36,25)*v*v)
close([float(z.subs({u:1,v:sp.Rational(1,10)})) for z in step],[.8,.12])
close([L.subs({u:1,v:sp.Rational(1,10)}),L.subs({u:sp.Rational(4,5),v:sp.Rational(3,25)})],[.99,.6256])
f=lambda x:2*max(x,0)+3*max(-x,0)
g=lambda x:.5*max(4*x,0)+3*max(-x,0)
check([f(x) for x in [-2,2]]==[6,4])
check(all(f(x)==g(x) for x in [-2,-1,0,1,2]))
t=sp.symbols('t',real=True)
check(sp.diff(t**4,t).subs(t,0)==0 and sp.diff(t**4,t,2).subs(t,0)==0)
check(math.factorial(3)==6)
sig=lambda x:1/(1+math.exp(-x))
close([sig(-z) for z in [-3,0,3]],[1-sig(z) for z in [-3,0,3]])
# Hidden sigmoid sign compensation a*h+b = -a*(1-h)+(b+a).
a,h,b=sp.symbols('a h b');check(sp.expand(-a*(1-h)+(b+a)-(a*h+b))==0)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['0.6256', '0.99', '0.8', '0.12', 'up to $m!$']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
