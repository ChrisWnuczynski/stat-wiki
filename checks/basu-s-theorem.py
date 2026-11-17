"""Independent numerical and symbolic checks, including generated article content."""
from pathlib import Path
import re
import math
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
rate,total,ratio=s.symbols('rate total ratio',positive=True)
J=s.Matrix([ratio*total,(1-ratio)*total]).jacobian([total,ratio])
assert s.simplify(abs(J.det()))==total
joint=rate**2*total*s.exp(-rate*total)
assert s.integrate(joint,(total,0,s.oo))==1
assert s.integrate(joint.subs(rate,1),(total,2,s.oo))==3*s.exp(-2)
assert abs(3*math.exp(-2)-.406006)<5e-7
assert abs(.25*3*math.exp(-2)-.101501)<5e-7
assert .4+1.6==2 and .4/2==.2
# A polynomial vanishing on an interval has zero coefficients (binomial completeness).
p=s.symbols('p');a,b,c=s.symbols('a b c')
poly=s.Poly(a*(1-p)**2+2*b*p*(1-p)+c*p*p,p)
assert s.solve(poly.all_coeffs(),[a,b,c])=={a:0,b:0,c:0}
restricted=3*(1-p)**2-10*p*(1-p)+3*p*p
assert restricted.subs(p,s.Rational(1,4))==restricted.subs(p,s.Rational(3,4))==0
# Expected range of n independent uniforms on an interval of length one.
u=s.symbols('u',positive=True)
for n in range(2,10):
    emax=s.integrate(u*n*u**(n-1),(u,0,1))
    emin=s.integrate(u*n*(1-u)**(n-1),(u,0,1))
    assert emax-emin==s.Rational(n-1,n+1)
# Actual two linked self-checks: a three-trial unbiased estimator and a singleton model.
p=s.symbols('p',real=True)
unbiased=sum(s.Rational(k*(k-1),6)*s.binomial(3,k)*p**k*(1-p)**(3-k) for k in range(4))
assert s.expand(unbiased)==p**2 and s.Rational(2*(2-1),6)==s.Rational(1,3)
zero_mean=sum((k-1)*s.binomial(2,k)*p**k*(1-p)**(2-k) for k in range(3))
assert s.expand(zero_mean)==2*p-1 and zero_mean.subs(p,s.Rational(1,2))==0
assert (s.Rational(1,2))**2>0  # nonzero q(0) and q(2) each occur with positive probability.
source=(ROOT/"research/content/basu-s-theorem.md").read_text()
article=(ROOT/"articles/basu-s-theorem.qmd").read_text().split("## See also",1)[0]
for needle in ['0.406006', '0.101501', '0.2']:
    assert needle in source and needle in article,needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}",source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("basu-s-theorem: calculations and article checks passed")
