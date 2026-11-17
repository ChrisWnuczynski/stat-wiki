"""Independent numerical and algebraic checks for gibbs-inequality."""
import math
from pathlib import Path
import numpy as np


p=np.array([.9,.1]);q=np.array([.5,.5]);gap=float(p@np.log(p/q))
assert abs(gap-.36806420716849714)<1e-14
assert abs(p@np.log(p)+.3250829733914482)<1e-14
assert abs(p@np.log(q)+.6931471805599453)<1e-14
assert abs(q@np.log(q/p)-.5108256237659907)<1e-14
for z in [.01,.1,.5,1,2,10,100]:assert math.log(z)<=z-1+1e-14
assert abs(-np.log([.5,.5]).mean()-math.log(2))<1e-14

assert math.log(2)>0

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "gibbs-inequality.qmd").read_text()
source=(root / "research/content" / "gibbs-inequality.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['0.368064', '0.510826']:
    assert token in body, (token, "gibbs-inequality")
print("gibbs-inequality: numerical and algebraic checks passed")
