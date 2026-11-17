"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='levy-s-continuity-theorem'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

from scipy.stats import norm,binom
from scipy.integrate import quad
values=[math.cos(1/math.sqrt(n))**n for n in [1,10,100]]
close(values,[.5403023058681398,.6013593951422658,.6060240772159909]);close(math.exp(-.5),.6065306597126334)
t,n=sp.symbols('t n',positive=True)
check(sp.limit(sp.cos(t/n),n,sp.oo)==1)
check(sp.limit(sp.exp(-n*t*t/2),n,sp.oo)==0)
check(sp.exp(-n*0)==1)
close([norm.cdf(2/np.sqrt(n)) for n in [1e4,1e6]],[.5079783137169019,.5007978840288801])
# Numerically check the smoothing identity in the tightness proof on a full finite law.
N=10;xs=(2*np.arange(N+1)-N)/math.sqrt(N);ps=binom.pmf(np.arange(N+1),N,.5);h=.8
left=sum(ps*(1-np.sinc(h*xs/np.pi)))
right=quad(lambda z:1-math.cos(z/math.sqrt(N))**N,-h,h)[0]/(2*h)
close(left,right)
check(sum(ps[abs(xs)>2/h])<=2*left+1e-12)
check(np.allclose(np.exp(3j*np.array([0.,.3,1.])),[1,complex(math.cos(.9),math.sin(.9)),complex(math.cos(3),math.sin(3))],rtol=1e-12,atol=1e-12))

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['0.601359', '0.606024', '0.606531', 'tightness']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
