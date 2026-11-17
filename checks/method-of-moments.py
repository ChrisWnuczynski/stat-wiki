"""Recompute worked examples and inspect generated mathematical claims."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "method-of-moments.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

x=list(map(sp.Integer,[1,2,3,6]));m=sum(x)/4;m2=sum(t*t for t in x)/4;v=m2-m*m
assert m==3 and m2==sp.Rational(25,2) and v==sp.Rational(7,2)
a=m*m/v;b=m/v;assert a==sp.Rational(18,7) and b==sp.Rational(6,7)
assert a/b==3 and a/b**2==sp.Rational(7,2)
m_new=2*m;v_new=4*v;assert m_new*m_new/v_new==a and m_new/v_new==sp.Rational(3,7)
assert sum((t-m)**2 for t in x)/3==sp.Rational(14,3)
assert 12-3**2==3 and 1-sp.Rational(3,2)==-sp.Rational(1,2)
for token in ['18}{7','6}{7','3/7','14/3']:assert token in text,token

print("method-of-moments: symbolic/numerical recomputation and article assertions passed")
