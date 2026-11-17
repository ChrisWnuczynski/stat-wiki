"""Recompute numerical examples and exercise answers for universal-approximation."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'universal-approximation'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

r=lambda z:np.maximum(0,z)
x=np.linspace(0,1,10001);F=.25*x+.5*r(x-.25)+.5*r(x-.5)+.5*r(x-.75)
assert np.isclose(np.max(F-x*x),1/64) and np.min(F-x*x)>-1e-14
for knot in [0,.25,.5,.75,1]:
 val=.25*knot+.5*r(knot-.25)+.5*r(knot-.5)+.5*r(knot-.75)
 assert np.isclose(val,knot*knot)
assert .5*.25==1/8 and .25**2==1/16 and 1/8-1/16==1/16
assert 1/(4*5**2)==.01 and 1/(4*4**2)>.01
assert 2-1>.5
# A logistic ridge against a unit step keeps uniform error 1/2; only the bad set shrinks.
logit19 = math.log(19)
for slope in (20, 100):
    xs = np.linspace(0, 1, 1000001)
    ridge = 1/(1+np.exp(-slope*(xs-0.5)))
    step = (xs >= 0.5).astype(float)
    gap = np.abs(ridge-step)
    assert np.isclose(gap.max(), 0.5)
    assert np.isclose(np.mean(gap > 0.05), 2*logit19/slope, rtol=0, atol=2e-5)
assert math.isclose(2*logit19/20, 0.29444389791664405)
assert math.isclose(2*logit19/100, 0.05888877958332881)

# Match computed worked-example and practice results to their generated text.
assert f"1/64={np.max(F-x*x):.6f}" in worked
exercise_error=1/8-.25**2
assert f"1/16={exercise_error:g}$" in answer
intervals=math.ceil(math.sqrt(1/(4*.01)))
assert rf"m\ge{intervals}" in answer
print("universal-approximation: numerical checks passed")
