"""Recompute numerical examples and exercise answers for two-state-continuous-time-chain."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'two-state-continuous-time-chain'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

a,b=2.,3.;Q=np.array([[-a,a],[b,-b]]);pi=np.array([b,a])/(a+b)
P=linalg.expm(Q);expected=np.array([[.602695,.397305],[.595957,.404043]])
assert np.allclose(P,expected,atol=5e-7)
assert round(math.exp(-5),6)==.006738 and round(1-math.exp(-2),6)==.864665
assert np.allclose(pi@Q,0) and np.allclose(pi@P,pi)
assert np.allclose(linalg.expm(.3*Q)@linalg.expm(.7*Q),P)
assert 1/(1+4)==.2 and np.isclose(.2*(1-math.exp(-5*math.log(2)/5)),.1)
for r in [.5,2]:
 t=.7;odd=sum(stats.poisson.pmf(n,r*t) for n in range(1,100,2));assert np.isclose(odd,.5*(1-math.exp(-2*r*t)))

# Match computed worked-example and practice results to their generated text.
assert f'{P[0,0]:.6f}&{P[0,1]:.6f}' in worked and f'{P[1,0]:.6f}&{P[1,1]:.6f}' in worked
assert rf"\approx{1-math.exp(-2):.6f}" in worked
assert f"1/(1+4)={1/(1+4):g}" in answer
assert f"0.2(1-1/2)={.2*(1-math.exp(-5*math.log(2)/5)):g}" in answer
print("two-state-continuous-time-chain: numerical checks passed")
