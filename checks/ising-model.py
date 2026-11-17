"""Independent numerical and algebraic checks for ising-model."""
import math
from pathlib import Path
import numpy as np


from itertools import product
states=np.array(list(product([-1,1],repeat=2)));b=.5
weights=np.exp(b*states[:,0]*states[:,1]);p=weights/weights.sum()
assert abs(weights.sum()-4.510503860825523)<1e-14
assert abs(p[states[:,0]==states[:,1]].sum()-.731058578630005)<1e-14
assert abs(math.exp(-2*b)-.36787944117144233)<1e-14
assert abs(1/(1+math.exp(-2*b))-.7310585786300049)<1e-14
for s1,s2 in states:
 ratio=math.exp(b*(-s1)*s2)/math.exp(b*s1*s2)
 assert abs(ratio-math.exp(-2*b*s1*s2))<1e-14
assert 20*20==400 and 2**400>10**120


root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "ising-model.qmd").read_text()
source=(root / "research/content" / "ising-model.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['4.510504', '0.731059', '0.367879']:
    assert token in body, (token, "ising-model")
print("ising-model: numerical and algebraic checks passed")
