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
from scipy.special import expit
from math import exp
z=np.array([-2,-1,0,1,2,3.]);x=np.array([0,1,0,1,0,1.]);y=2*x+z*z
B=np.column_stack([np.ones(6),z,z*z]);M=np.eye(6)-B@np.linalg.solve(B.T@B,B.T)
assert np.allclose(M@B,0)
assert abs(x@M@x-48/35)<1e-13
assert abs(x@M@y-96/35)<1e-13
assert abs((x@M@y)/(x@M@x)-2)<1e-13
assert abs(np.linalg.lstsq(np.column_stack([np.ones(6),x]),y,rcond=None)[0][1]-3)<1e-13
assert abs(exp(.4)-1.4918246976412703)<1e-14
assert abs(expit(-1)-.2689414213699951)<1e-14
assert abs(expit(-.6)-.35434369377420455)<1e-14
assert '0.085402' in body and '48' in body

print("partially-linear-model checks passed")
