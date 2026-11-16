"""Check partial-correlation arithmetic and the chain matrix."""
import math
import numpy as np
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/partial-correlation.qmd").read_text().split("## See also", 1)[0]

def partial(rxy, rxz, ryz):
    return (rxy - rxz*ryz)/math.sqrt((1-rxz**2)*(1-ryz**2))

p = partial(0.8, 0.6, 0.5)
assert abs(math.sqrt(0.48) - 0.6928) < 5e-5
assert abs(p - 0.7217) < 5e-5
assert abs(partial(0.3, 0.6, 0.5)) < 1e-12
assert abs(partial(0.5, 0.5, 0.5) - 1/3) < 1e-12
assert abs(partial(0.4, 0.8, 0.5)) < 1e-12
assert -(-0.3)/math.sqrt(1*1) == 0.3
K = np.array([[1, -0.5, 0], [-0.5, 1, -0.5], [0, -0.5, 1]], float)
S = np.linalg.inv(K)
assert np.allclose(S, [[1.5,1,0.5],[1,2,1],[0.5,1,1.5]])
assert abs(S[0,2]/math.sqrt(S[0,0]*S[2,2]) - 1/3) < 1e-12
for s in ("0.7217", "0.6928", "1/3", "0.3"):
    assert s in body, s
assert body.count('title="Proof"') >= 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="dodge2008"' in body
print("partial correlation passed")
