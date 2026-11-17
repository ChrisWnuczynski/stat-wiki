"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

import sympy as sp
z=sp.symbols('z')
G=sp.Rational(1,5)+sp.Rational(1,2)*z+sp.Rational(3,10)*z*z
mean=sp.diff(G,z).subs(z,1)
variance=sp.diff(G,z,2).subs(z,1)+mean-mean**2
assert (mean,variance)==(sp.Rational(11,10),sp.Rational(49,100))
assert [sp.expand(G**2).coeff(z,i) for i in range(5)]==[sp.Rational(4,100),sp.Rational(20,100),sp.Rational(37,100),sp.Rational(30,100),sp.Rational(9,100)]
H=G**2;m=sp.diff(H,z).subs(z,1)
assert m==sp.Rational(22,10)
assert sp.diff(H,z,2).subs(z,1)+m-m*m==sp.Rational(98,100)
assert G.subs(z,0)**3==sp.Rational(8,1000)
assert sp.simplify(2*(sp.Rational(7,10)+sp.Rational(3,10)*z-1)-sp.Rational(6,10)*(z-1))==0
assert '0.49' in body and '0.98' in body and '0.008' in body


# Exact linked Bernoulli-MGF and critical-offspring exercises.
p_bernoulli = .4
assert abs(2*p_bernoulli-.8)<1e-14
assert abs(2*p_bernoulli*(1-p_bernoulli)-.48)<1e-14
assert abs(p_bernoulli**2-.16)<1e-14
import sympy as sp
s=sp.symbols('s')
f=sp.Rational(2,5)+s/5+sp.Rational(2,5)*s**2
assert sp.diff(f,s).subs(s,1)==1
assert sp.factor(f-s)==sp.Rational(2,5)*(s-1)**2

print("probability-generating-function checks passed")
