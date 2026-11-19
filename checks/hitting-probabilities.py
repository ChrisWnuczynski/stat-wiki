"""Solve hitting probabilities and durations from their transition equations."""
from pathlib import Path
import re
import sympy as s
root=Path(__file__).resolve().parents[1]
Q=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,s.Rational(1,2)],[0,s.Rational(1,2),0]])
h=(s.eye(3)-Q).inv()*s.Matrix([0,0,s.Rational(1,2)])
e=(s.eye(3)-Q).inv()*s.ones(3,1)
assert list(h)==[s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]
assert list(e)==[3,4,3]
def hit(i,m,p):
    r=(1-p)/p
    return s.Rational(i,m) if p==s.Rational(1,2) else s.cancel((1-r**i)/(1-r**m))
assert [hit(i,4,s.Rational(3,5)) for i in [1,2,3]]==[s.Rational(27,65),s.Rational(9,13),s.Rational(57,65)]
assert round(float(hit(1,4,s.Rational(3,5))),4)==.4154
assert hit(5,8,s.Rational(1,2))==s.Rational(5,8)
assert 5*(8-5)==15
assert hit(1,4,s.Rational(2,3))==s.Rational(8,15)
for p in [s.Rational(1,2),s.Rational(3,5),s.Rational(2,3)]:
    for i in [1,2,3]:
        assert hit(i,4,p)==p*hit(i+1,4,p)+(1-p)*hit(i-1,4,p)
body=(root/"articles/hitting-probabilities.qmd").read_text().split("## See also",1)[0]
for text in ["27/65","9/13","57/65","8/15","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["depth-hitting-probabilities-q1", "depth-hitting-probabilities-q2"]:
    assert f"../questions/{q}.qmd" in body
print("hitting-probabilities: linear systems, recurrences and article checks passed")
