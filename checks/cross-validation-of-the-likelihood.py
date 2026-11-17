"""Independent numerical and algebraic checks for cross-validation-of-the-likelihood."""
import math
from pathlib import Path
import numpy as np


a=np.array([.8,.7,.1,.6]);b=np.array([.6,.6,.4,.6])
assert abs(np.log(a).mean()+.8483073030032446)<1e-13
assert abs(np.log(b).mean()+.6121919007930319)<1e-13
assert np.log(b).sum()>np.log(a).sum()
assert np.allclose(np.log(b/.5)-np.log(a/.5),np.log(b)-np.log(a))
assert 10*(9*5+1)+10*5+1==511
assert 1/3*(math.exp(-.5)+1+math.exp(-2))/math.sqrt(2*math.pi)>0


root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "cross-validation-of-the-likelihood.qmd").read_text()
source=(root / "research/content" / "cross-validation-of-the-likelihood.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['-0.848307', '-0.612192']:
    assert token in body, (token, "cross-validation-of-the-likelihood")
print("cross-validation-of-the-likelihood: numerical and algebraic checks passed")
