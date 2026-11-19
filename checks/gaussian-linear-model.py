"""Check the four-point Gaussian linear fit and the t comparison."""

import math
from pathlib import Path
import numpy as np
from numpy.linalg import inv
from scipy.stats import t

root = Path(__file__).resolve().parents[1]
page = (root / "articles/gaussian-linear-model.qmd").read_text()
body = page.split("## See also", 1)[0]

x = np.array([0.0, 1, 2, 3])
X = np.column_stack([np.ones(4), x])
xtx = X.T @ X
assert int(round(np.linalg.det(xtx))) == 20
xtx_inv = inv(xtx)
assert abs(xtx_inv[1, 1] - 0.2) < 1e-12

y = np.array([0.0, 1, 1, 2])
beta = xtx_inv @ (X.T @ y)
assert np.allclose(beta, [0.1, 0.6])
resid = y - X @ beta
sse = float(resid @ resid)
assert abs(sse - 0.2) < 1e-12
assert abs(sse / 2 - 0.1) < 1e-12
se = math.sqrt(0.1 * 0.2)
assert abs(se - math.sqrt(1 / 50)) < 1e-12
assert round(se, 4) == 0.1414
ratio = 0.6 / se
assert abs(ratio - 3 * math.sqrt(2)) < 1e-12
assert round(ratio, 3) == 4.243
tc = t.ppf(0.975, 2)
assert round(tc, 4) == 4.3027
assert round(tc * se, 4) == 0.6085
assert round(0.6 - 0.6085, 4) == -0.0085
assert round(0.6 + 0.6085, 4) == 1.2085
assert round(2 * 0.1414, 4) == 0.2828

y2 = np.array([0.0, 1, 3, 2])
beta2 = xtx_inv @ (X.T @ y2)
assert abs(beta2[1] - 0.8) < 1e-10
sse2 = float((y2 - X @ beta2) @ (y2 - X @ beta2))
assert abs(sse2 - 1.8) < 1e-10
assert abs(sse2 / 2 - 0.9) < 1e-12
assert round(math.sqrt(0.18), 4) == 0.4243
assert abs(math.sqrt(9) * se - math.sqrt(0.18)) < 1e-12

for printed in (
    "0.6", "0.1", "0.2", "0.1414", "4.243", "4.3027", "0.6085",
    "1.2085", "0.2828", "1.8", "0.9", "0.4243", "20",
):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("depth-gaussian-linear-model-q1", "depth-gaussian-linear-model-q2"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="hastie_esl2009"' in body
print("gaussian linear model checks passed")
