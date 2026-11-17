"""Recompute numerical examples and exercise answers for simple-variables-and-expectation."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'simple-variables-and-expectation'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

assert np.dot([0,100,500],[.7,.2,.1])==70
assert np.dot([10,110,510],[.7,.2,.1])==80
for m in range(1,10):
 n=2**m;v=np.arange(n)/n;assert np.isclose(v.mean(),.5-2**(-m-1))
assert [np.arange(2**m).mean()/2**m for m in [1,2,3]]==[.25,.375,.4375]
assert np.isclose(2*.3+5*.2,1.6) and np.isclose(6*.3+9*.2+4*.5,5.6)
x=np.array([0,.3,2.7,9]);last=np.zeros(len(x))
for m in range(1,20):
 s=np.floor(2**m*np.minimum(x,m))/2**m;assert np.all(s>=last) and np.all(s<=x);last=s
assert math.isclose(3*.4,3*.1+3*.3) and math.isclose(3*.4,1.2)

# Match computed worked-example and practice results to their generated text.
assert f"(0.1)={np.dot([0,100,500],[.7,.2,.1]):g}$" in worked
assert f"expectation to ${np.dot([10,110,510],[.7,.2,.1]):g}$" in worked
assert '$'+','.join(f'{np.arange(2**m).mean()/2**m:g}' for m in [1,2,3])+'$' in worked
assert f"={2*.3+5*.2:g}$" in answer and f"giving ${6*.3+9*.2+4*.5:g}$" in answer
print("simple-variables-and-expectation: numerical checks passed")
