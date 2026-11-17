"""Recompute article examples independently; public lidar data are from SemiPar."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "median-unbiased-estimators.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

x,t=sp.symbols('x t',positive=True)
for n in [1,2,3,5,9]:
 assert sp.simplify((t/2**sp.Rational(1,n)/t)**n)==sp.Rational(1,2)
 assert sp.integrate(x*n*x**(n-1)/t**n,(x,0,t))==n*t/(n+1)
 assert sum(sp.binomial(n,k) for k in range((n+1)//2,n+1))/2**n==sp.Rational(1,2) if n%2 else True
for v,s in [(5*sp.sqrt(2),'7.071068'),(7*sp.sqrt(2),'9.899495'),(2*sp.sqrt(2)/3,'0.942809')]:assert f'{float(v):.6f}'==s and s in text
assert sp.Rational(3,2)*7==sp.Rational(21,2)
z=[-1,0,1];pr=list(map(sp.Rational,['.1','.6','.3']))
assert [sum(p*abs(a-b) for a,p in zip(z,pr)) for b in [0,1,-1]]==[sp.Rational(2,5),sp.Rational(4,5),sp.Rational(6,5)]
assert pr[0]+pr[1]==sp.Rational(7,10) and pr[1]+pr[2]==sp.Rational(9,10)
assert sum(a*p for a,p in zip(z,pr))==sp.Rational(1,5)

print("median-unbiased-estimators: numerical examples and generated-article assertions passed")
