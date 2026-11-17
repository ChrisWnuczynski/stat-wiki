"""Recompute worked examples and inspect generated mathematical claims."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "joint-distribution-and-density.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

x,y=sp.symbols('x y',nonnegative=True);f=x+y;F=x*y*(x+y)/2
assert sp.diff(F,x,y)==f
assert sp.integrate(sp.integrate(f,(x,0,1)),(y,0,1))==1
rect=sp.integrate(sp.integrate(f,(y,0,sp.Rational(1,2))),(x,sp.Rational(1,4),sp.Rational(3,4)))
assert rect==sp.Rational(3,16)
EX=sp.integrate(sp.integrate(x*f,(y,0,1)),(x,0,1));EXY=sp.integrate(sp.integrate(x*y*f,(y,0,1)),(x,0,1))
assert EX==sp.Rational(7,12) and EXY==sp.Rational(1,3) and EXY-EX**2==-sp.Rational(1,144)
assert sp.integrate(y*(y+sp.Rational(1,2)),(y,0,1))==EX
for token in ['3/16','-1/144','7/12']:assert token in text,token

print("joint-distribution-and-density: symbolic/numerical recomputation and article assertions passed")
