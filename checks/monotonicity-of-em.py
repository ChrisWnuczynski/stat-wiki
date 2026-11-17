"""Recompute article examples independently; public lidar data are from SemiPar."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "monotonicity-of-em.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

import math
q0=sp.Rational(4,5);theta0=sp.Rational(1,2);theta1=q0
like=lambda t:sp.Rational(1,5)+3*t/5
assert like(theta0)==sp.Rational(1,2) and like(theta1)==sp.Rational(17,25)
q1=sp.Rational(4,5)*theta1/like(theta1);assert q1==sp.Rational(16,17) and like(q1)==sp.Rational(13,17)
Q=q0*sp.log(theta1/theta0)+(1-q0)*sp.log((1-theta1)/(1-theta0))
KL=q0*sp.log(q0/q1)+(1-q0)*sp.log((1-q0)/(1-q1));gain=sp.log(like(theta1)/like(theta0))
assert abs(float(gain-Q-KL))<1e-14
for v,s in [(gain,'0.307485'),(Q,'0.192745'),(KL,'0.114740')]:assert f'{float(v):.6f}'==s and s in text
H=.8*math.log(.8)+.2*math.log(.2)
assert f'{H:.3f}'=='-0.500' and f'{math.log(.5):.3f}'=='-0.693' and f'{H-math.log(.5):.3f}'=='0.193'

print("monotonicity-of-em: numerical examples and generated-article assertions passed")
