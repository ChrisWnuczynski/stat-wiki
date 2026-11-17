"""Independent numerical and symbolic checks, including generated article content."""
from pathlib import Path
import re
import math
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
t=s.symbols('t',real=True)
prob=[s.binomial(3,k)*s.Rational(1,4)**k*s.Rational(3,4)**(3-k) for k in range(4)]
phi=sum(pk*s.exp(s.I*t*k) for k,pk in enumerate(prob))
assert s.simplify(phi-(s.Rational(3,4)+s.exp(s.I*t)/4)**3)==0
assert s.simplify(phi.subs(t,s.pi))==s.Rational(1,8)
assert s.simplify(phi.subs(t,s.pi/2))==s.Rational(9,32)+s.I*s.Rational(13,32)
mean=s.simplify(s.diff(phi,t).subs(t,0)/s.I)
second=s.simplify(-s.diff(phi,t,2).subs(t,0))
assert mean==s.Rational(3,4) and second-mean**2==s.Rational(9,16)
assert s.simplify(sum(pk*s.exp(s.I*t*(2*k-1)) for k,pk in enumerate(prob))-s.exp(-s.I*t)*phi.subs(t,2*t))==0
assert abs(math.cos(1/2)**4-.593133)<5e-7
assert abs(math.cos(1/10)**100-.606024)<5e-7
assert abs(math.exp(-.5)-.606531)<5e-7
z=s.symbols('z');mgf=1/(1-z)
for n in range(1,9): assert s.diff(mgf,z,n).subs(z,0)==s.factorial(n)
p=s.symbols('p');assert s.expand(p*p+(1-p)**2)==1-2*p+2*p*p
source=(ROOT/"research/content/characteristic-functions.md").read_text()
article=(ROOT/"articles/characteristic-functions.qmd").read_text().split("## See also",1)[0]
for needle in ['0.593133', '0.606024', '0.606531']:
    assert needle in source and needle in article,needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}",source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("characteristic-functions: calculations and article checks passed")
