"""Independent calculations and generated-output checks for this article."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
import sympy as s
x=s.symbols("x");f=s.Rational(1,4)+s.Rational(3,4)*x*x
assert s.solve(f-x,x)==[s.Rational(1,3),1]
assert s.diff(f,x).subs(x,1)==s.Rational(3,2)
assert f.subs(x,s.Rational(1,4))==s.Rational(19,64)
q=s.Rational(0)
for n in range(12):
 nxt=f.subs(x,q);assert q<=nxt<=s.Rational(1,3);q=nxt
assert s.Rational(1,3)**3==s.Rational(1,27)
assert s.solve(s.Rational(3,4)+x*x/4-x,x)==[1,3]
assert s.factor(s.Rational(2,5)+x/5+s.Rational(2,5)*x*x-x)==2*(x-1)**2/5

source=(ROOT/"research/content/extinction-criterion.md").read_text()
article=(ROOT/"articles/extinction-criterion.qmd").read_text().split("## See also",1)[0]
for needle in ['19/64', '1/27', 'm>1']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("extinction-criterion: calculations and article checks passed")
