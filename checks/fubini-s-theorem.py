"""Recompute the mathematical examples and inspect the generated article."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "fubini-s-theorem.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

x,y,t=sp.symbols('x y t',positive=True)
assert sp.integrate(sp.integrate(6*x,(x,0,y)),(y,0,1))==1
assert sp.integrate(sp.integrate(6*x,(y,x,1)),(x,0,1))==1
assert sp.integrate(y*3*y**2,(y,0,1))==sp.Rational(3,4)
assert sp.integrate(x*6*x*(1-x),(x,0,1))==sp.Rational(1,2)
assert sum(sp.Rational(7-k,6) for k in range(1,7))==sp.Rational(7,2)
assert sp.limit(sp.log(1+t),t,sp.oo)==sp.oo
# Exact infinite row/column sums: a_mn=1[m=n]-1[m=n+1].
def a(m,n):return int(m==n)-int(m==n+1)
assert sum(a(1,n) for n in range(1,10))==1
for m in range(2,20):assert sum(a(m,n) for n in range(1,2*m+1))==0
for n in range(1,20):assert sum(a(m,n) for m in range(1,2*n+2))==0
for N in range(2,20):assert sum(abs(a(m,n)) for m in range(1,N+1) for n in range(1,N+1))==2*N-1
N=sp.symbols('N',positive=True);assert sp.limit(2*N-1,N,sp.oo)==sp.oo
for token in ['3/4','1/2','3.5']: assert token in text,token

print("fubini-s-theorem: exact calculations and generated-article assertions passed")
