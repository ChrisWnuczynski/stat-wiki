"""Independent calculations and generated-output checks for this article."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
import math
import sympy as s
u=s.symbols("u",positive=True);lam=s.symbols("lambda",positive=True)
q=-s.log(1-u)/lam
assert s.simplify(1-s.exp(-lam*q)-u)==0
assert abs(-math.log(.2)/2-.8047189562170503)<1e-14
assert abs(math.log(2)/2-.34657359027997264)<1e-14
assert [next(x for x,c in zip([0,2,5],[.2,.7,1]) if z<=c) for z in [.1,.6,.9]]==[0,2,5]
x=s.symbols("x");assert s.Rational(1,8)**s.Rational(1,3)==s.Rational(1,2)
assert s.Rational(3,4)**3-s.Rational(1,2)**3==s.Rational(19,64)
assert s.integrate(3*x**3,(x,0,1))==s.Rational(3,4)
assert 10+5*.5==12.5

# All five closed-form inverses are verified against their defining CDFs.
a,b,eta,k,mu,scale,x0,gamma=s.symbols("a b eta k mu scale x0 gamma",positive=True)
assert s.simplify(((a+(b-a)*u)-a)/(b-a)-u)==0
qw=eta*(-s.log(1-u))**(1/k)
for z in [.01,.2,.5,.8,.99]:
    quant=3*(-math.log(1-z))**(1/1.7)
    assert abs(1-math.exp(-(quant/3)**1.7)-z)<1e-14
ql=mu+scale*s.log(u/(1-u))
assert s.simplify(1/(1+s.exp(-(ql-mu)/scale))-u)==0
# atan(tan(v))=v on the quantile branch v in (-pi/2,pi/2).
for z in [.01,.2,.5,.8,.99]:
    qc=2+3*math.tan(math.pi*(z-.5))
    assert abs(.5+math.atan((qc-2)/3)/math.pi-z)<1e-14
source=(ROOT/"research/content/inverse-transform-method.md").read_text()
article=(ROOT/"articles/inverse-transform-method.qmd").read_text().split("## See also",1)[0]
for needle in ['0.804719', '0.346574', '19/64']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("inverse-transform-method: calculations and article checks passed")
