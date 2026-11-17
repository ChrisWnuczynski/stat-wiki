"""Recompute the mathematical examples and inspect the generated article."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "gambler-s-ruin.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

p=sp.Rational(3,5);q=1-p;d=5;r=q/p
h=lambda x:sp.cancel((1-r**x)/(1-r**d))
assert h(2)==sp.Rational(135,211) and 1-h(2)==sp.Rational(76,211)
assert (d*h(2)-2)/(p-q)==sp.Rational(1265,211)
assert h(1)==sp.Rational(81,211)
for x in range(1,d):assert sp.simplify(h(x)-p*h(x+1)-q*h(x-1))==0
assert h(0)==0 and h(d)==1
for v,s in [(h(2),'0.639810'),(1-h(2),'0.360190'),((d*h(2)-2)/(p-q),'5.995261'),(h(1),'0.383886')]:assert f'{float(v):.6f}'==s and s in text
assert 2*(5-2)==6 and 4*(10-4)==24

print("gambler-s-ruin: exact calculations and generated-article assertions passed")
