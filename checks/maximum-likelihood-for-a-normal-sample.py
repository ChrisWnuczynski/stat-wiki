"""Recompute worked examples and inspect generated mathematical claims."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "maximum-likelihood-for-a-normal-sample.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

x=[sp.Integer(t) for t in [1,2,4,5]];n=len(x);m=sum(x)/n;S=sum((t-m)**2 for t in x)
assert m==3 and S==10 and S/n==sp.Rational(5,2) and S/(n-1)==sp.Rational(10,3)
assert f'{float(sp.sqrt(S/n)):.6f}'=='1.581139'
diff=-n*sp.log(sp.Rational(5,2))/2-S/(2*sp.Rational(5,2))-(-n*sp.log(5)/2-S/10)
assert sp.simplify(diff-(2*sp.log(2)-1))==0 and f'{float(diff):.6f}'=='0.386294'
assert sum(t*t for t in x)/n==sp.Rational(23,2)
v=sp.symbols('v',positive=True);profile=-n*sp.log(v)/2-S/(2*v)
assert sp.solve(sp.diff(profile,v),v)==[sp.Rational(5,2)]
for token in ['2.5','1.581139','0.386294','11.5']:assert token in text,token

print("maximum-likelihood-for-a-normal-sample: symbolic/numerical recomputation and article assertions passed")
