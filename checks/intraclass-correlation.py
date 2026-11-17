"""Independent numerical and algebraic checks for intraclass-correlation."""
import math
from pathlib import Path
import numpy as np


import sympy as sp
sa,se,m=sp.symbols('sa se m',positive=True)
rho=sa/(sa+se)
assert sp.simplify((sa+se)*(1+(m-1)*rho)/m-(sa+se/m))==0
assert 3/(3+1)==.75
assert 1+9*.75==7.75
assert 4*7.75/10==3.1
assert 10/7.75==40/31
assert np.allclose(np.linalg.eigvalsh(np.ones((4,4))*3+np.eye(4)),[1,1,1,13])
assert -1/3 < 0 and (1+3*(-1/3))==0


root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "intraclass-correlation.qmd").read_text()
source=(root / "research/content" / "intraclass-correlation.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['7.75', '3.1', '40/31']:
    assert token in body, (token, "intraclass-correlation")
print("intraclass-correlation: numerical and algebraic checks passed")
