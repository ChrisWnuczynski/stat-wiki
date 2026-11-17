"""Independent numerical and algebraic checks for exponential-loss."""
import math
from pathlib import Path
import numpy as np


import sympy as sp
f,p=sp.symbols('f p',real=True);L=p*sp.exp(-f)+(1-p)*sp.exp(f)
fstar=sp.log(p/(1-p))/2
assert sp.simplify(sp.diff(L,f).subs(f,fstar))==0
p0=.8;fs=.5*math.log(p0/(1-p0));assert abs(fs-math.log(2))<1e-14
assert abs(p0*math.exp(-fs)+(1-p0)*math.exp(fs)-.8)<1e-14
assert abs(math.exp(2)-7.38905609893065)<1e-13
assert abs(2*math.sqrt(.2*.8)-.8)<1e-14
assert np.allclose(np.array([.1,.1,.1,.1,.4])/.8,[.125,.125,.125,.125,.5])


root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "exponential-loss.qmd").read_text()
source=(root / "research/content" / "exponential-loss.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['0.693147', '7.389056', '0.125']:
    assert token in body, (token, "exponential-loss")
print("exponential-loss: numerical and algebraic checks passed")
