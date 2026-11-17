"""Verify radius-angle change of variables, normal moments and exact example pairs."""
from pathlib import Path
import sympy as s
import re
root=Path(__file__).resolve().parents[1]
r,theta=s.symbols("r theta",positive=True)
polar=s.Matrix([r*s.cos(theta),r*s.sin(theta)])
assert s.simplify(polar.jacobian([r,theta]).det())==r
assert s.simplify(polar.dot(polar))==r*r
u=s.symbols("u",positive=True)
assert s.integrate(-2*s.log(u),(u,0,1))==2
assert s.integrate(s.cos(theta)**2,(theta,0,2*s.pi))/(2*s.pi)==s.Rational(1,2)
assert s.integrate(s.cos(theta),(theta,0,2*s.pi))==0
assert round(float(s.sqrt(2*s.log(2))),3)==1.177 and s.cos(s.pi/2)==0
for v,target in [(s.Rational(1,6),s.Matrix([1,s.sqrt(3)])),(s.Rational(5,6),s.Matrix([1,-s.sqrt(3)]))]:
    pair=polar.subs({r:2,theta:2*s.pi*v}).applyfunc(s.simplify)
    assert pair==target and pair.dot(pair)==4
assert 3**2==9 and 15-10==5
body=(root/"articles/box-muller-method.qmd").read_text().split("## See also",1)[0]
for text in ["e^{-2}","5/6","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert 'title="Proof"' in body and len(re.findall('class="cite-ref"',body))>=5
for q in ["ex-prob-generate-normal","ex-prob-generate-uniform"]:assert f"../questions/{q}.qmd" in body
print("box-muller-method: Jacobian, radial moments, exact draws and article checks passed")
