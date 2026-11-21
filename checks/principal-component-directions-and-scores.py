"""Checks for principal-component directions and scores."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

from math import sqrt

import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/principal-component-directions-and-scores.md").read_text(encoding="utf-8")
prose = shown(prose, "principal-component-directions-and-scores")
article = root / "articles/principal-component-directions-and-scores.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

S = np.array([[2.0, 1.0], [1.0, 2.0]])
ev = np.linalg.eigvalsh(S)
assert np.allclose(sorted(ev), [1, 3])
a1 = np.array([1.0, 1.0]) / sqrt(2)
a2 = np.array([1.0, -1.0]) / sqrt(2)
assert np.allclose(S @ a1, 3 * a1)
assert np.allclose(S @ a2, 1 * a2)
x = np.array([2.0, 0.0])
assert np.isclose(a1 @ x, sqrt(2))
assert np.isclose(a2 @ x, sqrt(2))
recon = (a1 @ x) * a1
assert np.allclose(recon, [1, 1])
resid = x - recon
assert np.isclose(resid @ resid, 2)
y = np.array([0.0, 2.0])
assert np.isclose(a1 @ y, sqrt(2))
assert np.isclose(a2 @ y, -sqrt(2))
assert np.isclose(3 / 4, 0.75) and np.isclose(1 / 4, 0.25)

for printed in ("3/4", "1/4"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("pca checks passed")
