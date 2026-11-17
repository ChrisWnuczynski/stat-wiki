"""Independent calculations and generated-output checks for this article."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
import sympy as s
w=s.Matrix([3,4]); x=s.Matrix([2,3]); b=-5
score=w.dot(x)+b;norm=s.sqrt(w.dot(w));foot=x-score*w/w.dot(w)
assert score==13 and norm==5 and score/norm==s.Rational(13,5)
assert foot==s.Matrix([s.Rational(11,25),s.Rational(23,25)])
assert w.dot(foot)+b==0 and (x-foot).norm()==s.Rational(13,5)
assert (w.dot(s.Matrix([2,1]))+b)/norm==1 and b/norm==-1
assert 2/norm==s.Rational(2,5)
a=s.symbols("a",positive=True)
assert s.simplify(a*score/(a*norm)-score/norm)==0
assert s.sqrt(8)==2*s.sqrt(2)

xp=s.Matrix([3,3]);xm=s.Matrix([1,1]);alpha=s.Rational(1,4)
ws=alpha*(xp-xm);bs=-2
assert ws==s.Matrix([s.Rational(1,2),s.Rational(1,2)])
assert ws.dot(xp)+bs==1 and ws.dot(xm)+bs==-1
assert 2/ws.norm()==(xp-xm).norm()==2*s.sqrt(2)
source=(ROOT/"research/content/distance-to-a-hyperplane.md").read_text()
article=(ROOT/"articles/distance-to-a-hyperplane.qmd").read_text().split("## See also",1)[0]
for needle in ['13/5=2.6', '11/25,23/25', '0.4']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("distance-to-a-hyperplane: calculations and article checks passed")
