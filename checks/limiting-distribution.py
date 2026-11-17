"""Independent calculations and generated-output checks for this article."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
import sympy as s
P=s.Matrix([[s.Rational(4,5),s.Rational(1,5)],[s.Rational(2,5),s.Rational(3,5)]])
pi=s.Matrix([[s.Rational(2,3),s.Rational(1,3)]])
assert pi*P==pi
assert (P**2)[1,0]==s.Rational(14,25)
assert (P**5)[1,0]==s.Rational(2062,3125)
assert s.Rational(2,3)-(P**5)[1,0]==s.Rational(64,9375)
assert (P**5)[0,0]==s.Rational(2094,3125)
assert float((P**5)[0,0])==.67008
Q=s.Matrix([[0,1],[1,0]]);assert Q**2==s.eye(2)
# Recompute the six-stone example copied into the generated article.
M=s.Matrix([[0,s.Rational(1,3),0,s.Rational(1,3),s.Rational(1,3),0],[s.Rational(1,2),0,s.Rational(1,2),0,0,0],[s.Rational(1,2),0,0,s.Rational(1,2),0,0],[0,0,0,0,0,1],[0,0,0,s.Rational(1,2),0,s.Rational(1,2)],[0,0,s.Rational(1,2),0,s.Rational(1,2),0]])
stationary=s.Matrix([[12,4,20,25,22,36]])/119
assert stationary*M==stationary and sum(stationary)==1
assert abs(float((M**10)[0,0])-.1049)<.00005

# Both selected self-check calculations.
W=s.Matrix([[s.Rational(9,10),s.Rational(1,10)],[s.Rational(2,5),s.Rational(3,5)]])
assert (W**2)[0,1]==s.Rational(3,20)
assert s.Matrix([[s.Rational(4,5),s.Rational(1,5)]])*W==s.Matrix([[s.Rational(4,5),s.Rational(1,5)]])
C=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
assert C**3==s.eye(3)
assert s.Matrix([[1,1,1]])/3*C==s.Matrix([[1,1,1]])/3
source=(ROOT/"research/content/limiting-distribution.md").read_text()
article=(ROOT/"articles/limiting-distribution.qmd").read_text().split("## See also",1)[0]
for needle in ['0.65984', '0.67008', '64/9375']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "where $0<p<1$" in article
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("limiting-distribution: calculations and article checks passed")
