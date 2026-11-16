"""Check leave-one-out residuals for the three-point line."""
import numpy as np
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/leave-one-out-cross-validation.qmd").read_text().split("## See also", 1)[0]
X = np.array([[1,1],[1,2],[1,3]], float)
y = np.array([1.,2,6])
H = X @ np.linalg.inv(X.T @ X) @ X.T
beta = np.linalg.lstsq(X, y, rcond=None)[0]
assert np.allclose(beta, [-2, 2.5])
resid = y - H @ y
assert np.allclose(resid, [0.5, -1, 0.5])
lev = np.diag(H)
assert np.allclose(lev, [5/6, 1/3, 5/6])
loo = resid / (1-lev)
assert np.allclose(loo, [3, -1.5, 3])
assert abs(np.mean(loo**2) - 6.75) < 1e-9
assert abs(np.mean(resid**2) - 0.5) < 1e-9
assert abs(0.4/0.8 - 0.5) < 1e-12
assert abs(-0.3/(3/4) - (-0.4)) < 1e-12
assert 20-2 == 18
for s in ("6.75", "0.5", "-1.5", "3.5", "5/6"):
    assert s in body, s
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="hastie_esl2009"' in body
print("loocv passed")
