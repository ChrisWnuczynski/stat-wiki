"""Check stochastic identities, transition powers, and periodic counterexamples."""
from pathlib import Path
import re
import sympy as s
root=Path(__file__).resolve().parents[1]
C=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
P=(s.eye(3)+C)/2
u=s.Matrix([[s.Rational(1,3)]*3])
assert u*P==u and u*C==u
assert P*s.ones(3,1)==s.ones(3,1)
assert s.ones(1,3)*P==s.ones(1,3)
assert list((P**4)[0,:])==[s.Rational(5,16),s.Rational(5,16),s.Rational(3,8)]
assert all(v>0 for v in P**2)
assert C**3==s.eye(3) and C!=C.T
for n in range(1,10):
    assert (C**n)[0,0]==int(n%3==0)
    assert u*P**n==u
assert u*s.eye(3)==u
body=(root/"articles/doubly-stochastic-matrix.qmd").read_text().split("## See also",1)[0]
for text in ["5/16","3/8","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["ex-sp-doubly-stochastic","ex-sp-deterministic-cycle"]:
    assert f"../questions/{q}.qmd" in body
print("doubly-stochastic-matrix: identities, powers and article checks passed")
