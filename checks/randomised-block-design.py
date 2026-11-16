"""Arithmetic checks for the randomised block design article."""
from pathlib import Path
import numpy as np
from scipy.stats import f as fdist

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/randomised-block-design.md").read_text()
body = (root / "articles/randomised-block-design.qmd").read_text().split("## See also", 1)[0]
Y = np.array([[4.0, 7], [5, 6], [6, 8]])
b, t = Y.shape
grand = Y.mean()
ss_t = b * np.sum((Y.mean(0) - grand) ** 2)
ss_b = t * np.sum((Y.mean(1) - grand) ** 2)
resid = Y - Y.mean(1)[:, None] - Y.mean(0)[None, :] + grand
ss_e = np.sum(resid ** 2)
ss_tot = np.sum((Y - grand) ** 2)
assert grand == 6 and ss_t == 6 and ss_b == 3 and ss_e == 1 and ss_tot == 10
F = (ss_t / 1) / (ss_e / 2)
assert F == 12
assert round(1 - fdist.cdf(F, 1, 2), 3) == 0.074
assert (3 / 2) / 0.5 == 3
Z = np.array([[3.0, 5], [4, 6]])
gz = Z.mean()
rz = Z - Z.mean(1)[:, None] - Z.mean(0)[None, :] + gz
assert abs(np.sum(rz ** 2)) < 1e-12
for printed in ("SS}_{\\mathrm{treatment}}=6", "SS}_{\\mathrm{blocks}}=3",
                "SS}_{\\mathrm{error}}=1", "6+3+1=10", "$F=12$", "0.074",
                "$F=3$", "$(2,2)$", "0.5"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body
print("randomised block design checks passed")
