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

from scipy.special import expit
import numpy as np
from math import exp,log
abilities=np.array([0.,.8,1.4]);shifted=abilities+5
pairs=[(1,0),(2,0),(2,1)]
probs=[expit(abilities[i]-abilities[j]) for i,j in pairs]
assert np.allclose(probs,[.6899744811276125,.8021838885585817,.6456563062257954])
assert np.allclose(probs,[expit(shifted[i]-shifted[j]) for i,j in pairs])
assert abs(exp(1.4)-exp(.6)*exp(.8))<1e-14
assert 3*log(.8/.2)>0
assert abs((2*3)/(1+2*3)-6/7)<1e-14
assert '0.802184' in body and '6/7' in body

print("paired-comparison checks passed")
