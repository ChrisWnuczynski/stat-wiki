"""Recompute article examples independently; public lidar data are from SemiPar."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "multinomial-logistic-regression.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

scores=[sp.Integer(0),sp.log(2),sp.log(3)]
def softmax(xs):
 w=[sp.exp(x) for x in xs];return [sp.simplify(x/sum(w)) for x in w]
p=softmax(scores);assert p==[sp.Rational(1,6),sp.Rational(1,3),sp.Rational(1,2)]
assert softmax([x-scores[2] for x in scores])==p
assert softmax([x+1000 for x in scores])==p
assert softmax([0,sp.log(4),sp.log(3)])==[sp.Rational(1,8),sp.Rational(1,2),sp.Rational(3,8)]
assert sum([p[0],p[1],p[2]-1])==0
assert f'{float(-sp.log(p[2])):.6f}'=='0.693147'
z=sp.symbols('z0:3',real=True);loss=sp.log(sum(sp.exp(x) for x in z))-z[2]
for k in range(3):assert sp.simplify(sp.diff(loss,z[k])-(sp.exp(z[k])/sum(sp.exp(x) for x in z)-(1 if k==2 else 0)))==0

print("multinomial-logistic-regression: numerical examples and generated-article assertions passed")
