"""Independently recompute the article's finite examples."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "normal-inverse-gamma-prior.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

x=list(map(sp.Integer,[1,2,3]));n=3;bar=sum(x)/n;S=sum((v-bar)**2 for v in x)
k0=sp.Integer(2);a0=sp.Integer(3);b0=sp.Integer(4);m0=sp.Integer(0)
k=k0+n;m=(k0*m0+n*bar)/k;a=a0+sp.Rational(n,2);b=b0+S/2+k0*n*(bar-m0)**2/(2*k)
assert (bar,S,k,m,a,b)==(2,2,5,sp.Rational(6,5),sp.Rational(9,2),sp.Rational(37,5))
assert b/(a-1)==sp.Rational(74,35)
assert b/(a*k)==sp.Rational(74,225) and b/(k*(a-1))==sp.Rational(74,175)
assert b/a*(1+1/k)==sp.Rational(148,75)
assert b0+S/2==5
mu,mm,barvar=sp.symbols('mu mm barvar');kap,nn=sp.symbols('kap nn',positive=True)
mnew=(kap*mm+nn*barvar)/(kap+nn)
assert sp.simplify(nn*(mu-barvar)**2+kap*(mu-mm)**2-(kap+nn)*(mu-mnew)**2-kap*nn*(barvar-mm)**2/(kap+nn))==0
for token in ['74/35','74/225','74/175','148/75','37/5']:assert token in text,token

print("normal-inverse-gamma-prior: exact example recomputation and generated-article assertions passed")
