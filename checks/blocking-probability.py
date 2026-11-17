"""Independent numerical and symbolic checks, including generated article content."""
from pathlib import Path
import re
import math
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
la=s.Rational(2);mu=s.Rational(3);K=2
weights=s.Matrix([[1,la/mu,(la/mu)**2]])
pi=weights/sum(weights)
assert pi==s.Matrix([[9,6,4]])/19
Q=s.Matrix([[-la,la,0],[mu,-la-mu,la],[0,mu,-mu]])
assert pi*Q==s.zeros(1,3)
assert pi*(s.eye(3)+Q/5)==pi
assert la*(1-pi[2])==mu*(1-pi[0])==s.Rational(30,19)
assert abs(float(pi[2])-.210526)<5e-7
assert abs(float(la*(1-pi[2]))-1.578947)<5e-7
assert sum([s.Rational(1,3)]*3)==1
P=s.Matrix([[0,1,0],[s.Rational(1,3),0,s.Rational(2,3)],[0,1,0]])
assert s.Matrix([[1,3,2]])/6*P==s.Matrix([[1,3,2]])/6
rho=la/mu
assert 1-rho==s.Rational(1,3) and rho**3==s.Rational(8,27)
assert rho/(1-rho)==2 and 1/(mu-la)==1
rho=s.symbols('rho',positive=True)
for capacity in range(1,8):
    Z=sum(rho**j for j in range(capacity+1));B=rho**capacity/Z
    occupancy=sum(j*rho**j for j in range(capacity+1))/Z
    assert s.simplify(s.diff(B,rho)-B*(capacity-occupancy)/rho)==0
    assert s.simplify((capacity-occupancy)*Z)==sum((capacity-j)*rho**j for j in range(capacity))
assert s.Rational(1,4)/(1+s.Rational(1,2)+s.Rational(1,4))==s.Rational(1,7)
assert s.Rational(4,7)==4/(s.Rational(1)+2+4)
# A stationary nonergodic counterexample: occupancy is fixed by a Bernoulli draw.
# Its long-run full fraction is0or1 on each path, while its stationary probability is1/2.
I=s.eye(2);mixture=s.Matrix([[s.Rational(1,2),s.Rational(1,2)]])
assert mixture*I==mixture
assert s.Matrix([[1,0]])*I**1000==s.Matrix([[1,0]])
assert s.Matrix([[1,0]])*I**1000!=mixture
source=(ROOT/"research/content/blocking-probability.md").read_text()
article=(ROOT/"articles/blocking-probability.qmd").read_text().split("## See also",1)[0]
for needle in ['0.210526', '1.578947', '30/19']:
    assert needle in source and needle in article,needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}",source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert 'stationary ergodic system' in article
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("blocking-probability: calculations and article checks passed")
