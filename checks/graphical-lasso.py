"""Verify the graphical-lasso KKT candidates without an estimator implementation."""
from pathlib import Path
import re
import sympy as s
root=Path(__file__).resolve().parents[1]
singular=s.Matrix([[1,1],[1,1]])
assert singular.det()==0
assert set((singular+s.Rational(1,5)*s.eye(2)).eigenvals())=={s.Rational(1,5),s.Rational(11,5)}
S=s.Matrix([[1,s.Rational(3,5)],[s.Rational(3,5),1]])
W=s.Matrix([[s.Rational(6,5),s.Rational(2,5)],[s.Rational(2,5),s.Rational(6,5)]])
K=W.inv()
assert K==s.Matrix([[s.Rational(15,16),-s.Rational(5,16)],[-s.Rational(5,16),s.Rational(15,16)]])
assert W-S==s.Rational(1,5)*K.applyfunc(s.sign)
assert set(K.eigenvals())=={s.Rational(5,8),s.Rational(5,4)}
assert -K[0,1]/s.sqrt(K[0,0]*K[1,1])==s.Rational(1,3)
Wzero=s.Rational(8,5)*s.eye(2); Kzero=Wzero.inv()
Z=(Wzero-S)/s.Rational(3,5)
assert Kzero==s.Rational(5,8)*s.eye(2)
assert Z[0,0]==Z[1,1]==1 and all(abs(v)<=1 for v in Z)
# Conditional and marginal associations differ in the linked three-variable example.
K3=s.Matrix([[1,-s.Rational(1,5),0],[-s.Rational(1,5),1,s.Rational(3,10)],[0,s.Rational(3,10),1]])
assert all(v>0 for v in K3.eigenvals())
assert K3.inv()[0,2]!=0
body=(root/"articles/graphical-lasso.qmd").read_text().split("## See also",1)[0]
assert r"For $\lambda>0$" in body
for text in ["15/16","5/16","0.625","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["depth-graphical-lasso-q1", "depth-graphical-lasso-q2"]:
    assert f"../questions/{q}.qmd" in body
print("graphical-lasso: exact KKT and article checks passed")
