"""Recompute the mathematical examples and inspect the generated article."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "lebesgue-decomposition.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

a,b,c=sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,4)
assert a+b+c==1
x=sp.symbols('x');density=sp.Rational(1,4)
assert sp.integrate(density,(x,0,2))==b
assert a+sp.Rational(1,2)*sp.Rational(1,4)+c*sp.Rational(1,2)==sp.Rational(1,2)
assert b*sp.Rational(1,2)==sp.Rational(1,4)
assert sp.Rational(3,10)+sp.Rational(7,10)==1
m=sp.symbols('m',positive=True,integer=True)
assert sp.limit((sp.Rational(2,3))**m,m,sp.oo)==0
assert sp.limit(sp.Rational(1,2)**m,m,sp.oo)==0
for token in ['1/8+1/8=1/2','1/4','3^{-m}']:assert token in text,token

print("lebesgue-decomposition: exact calculations and generated-article assertions passed")
