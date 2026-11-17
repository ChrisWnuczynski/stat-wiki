"""Independent numerical and algebraic checks for finite-irreducible-chains."""
import math
from pathlib import Path
import numpy as np


P=np.array([[.5,.5],[1.,0.]]);pi=np.array([2/3,1/3])
assert np.allclose(pi@P,pi)
assert np.allclose(np.linalg.matrix_power(P,6),[[.671875,.328125],[.65625,.34375]])
for n in range(15):assert np.allclose(np.linalg.matrix_power(P,n)[0,0],2/3+(-.5)**n/3)
A=np.array([[0,1],[1,0]]);assert np.array_equal(np.linalg.matrix_power(A,2),np.eye(2))
C=np.array([[0,1,0],[0,0,1],[1,0,0]]);assert np.array_equal(np.linalg.matrix_power(C,3),np.eye(3))
weather=np.array([[.9,.1],[.4,.6]]);assert np.allclose([.8,.2]@weather,[.8,.2]);assert abs((weather@weather)[0,1]-.15)<1e-14
assert 1/pi[0]==1.5


root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "finite-irreducible-chains.qmd").read_text()
source=(root / "research/content" / "finite-irreducible-chains.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['0.671875', '0.328125']:
    assert token in body, (token, "finite-irreducible-chains")
print("finite-irreducible-chains: numerical and algebraic checks passed")
