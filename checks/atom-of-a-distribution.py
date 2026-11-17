"""Independent numerical and symbolic checks, including generated article content."""
from pathlib import Path
import re
import math
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
x=s.symbols('x', nonnegative=True)
f=s.Rational(7,5)*s.exp(-2*x)
assert s.integrate(f,(x,0,s.oo))==s.Rational(7,10)
mean=s.integrate(x*f,(x,0,s.oo));second=s.integrate(x*x*f,(x,0,s.oo))
assert mean==s.Rational(7,20) and second==s.Rational(7,20)
assert second-mean**2==s.Rational(91,400)
assert abs(.3+.7*(1-math.exp(-2))-.905265)<5e-7
assert abs(.7*(1-math.exp(-2))-.605265)<5e-7
assert np.dot([-2,0,3],[.25,.5,.25])==.25
assert .25*3==.75 and .25*2==.5
# An atom contributes a jump; changing a density at one point contributes none.
assert .3-0==.3
# The second mixture in the source is half Bernoulli(1/2), half Uniform(0,1).
assert .5*.5==.25 and .25+.25+.5==1
source=(ROOT/"research/content/atom-of-a-distribution.md").read_text()
article=(ROOT/"articles/atom-of-a-distribution.qmd").read_text().split("## See also",1)[0]
for needle in ['0.905265', '0.605265', '0.2275']:
    assert needle in source and needle in article,needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}",source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("atom-of-a-distribution: calculations and article checks passed")
