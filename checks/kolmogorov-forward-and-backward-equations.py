"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

import numpy as np
from scipy.linalg import expm
from math import exp
Q=np.array([[-2.,2.],[3.,-3.]])
P=expm(Q)
assert np.allclose(P.sum(axis=1),1)
assert np.allclose(P,[[.6026951787996342,.3973048212003658],[.5959572318005487,.4040427681994513]])
assert np.allclose(P@Q,Q@P)
h=1e-5
assert np.allclose((expm((1+h)*Q)-expm((1-h)*Q))/(2*h),P@Q,atol=1e-8)
assert np.allclose(np.array([.6,.4])@Q,0)
assert abs((1-exp(-2))/2-.43233235838169365)<1e-14
for number in ['0.397305','0.602695','0.595957','0.404043','0.432332']:
    assert number in body

print("kolmogorov-forward-and-backward-equations checks passed")
