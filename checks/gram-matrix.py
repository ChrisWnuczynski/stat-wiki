"""Arithmetic checks for the Gram-matrix article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown


import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/gram-matrix.md").read_text(encoding="utf-8")
prose = shown(prose, "gram-matrix")
article = root / "articles/gram-matrix.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

X = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
K = X @ X.T
assert np.allclose(K, [[1, 0, 1], [0, 1, 1], [1, 1, 2]])
ev = np.linalg.eigvalsh(K)
assert np.allclose(sorted(ev), [0, 1, 3])
c = np.array([1.0, -1.0, 0.5])
assert np.isclose(c @ K @ c, 2.5)
assert np.isclose(np.linalg.norm(X.T @ c) ** 2, 2.5)

K2 = np.array([[1.0, -1.0], [-1.0, 1.0]])
assert np.allclose(sorted(np.linalg.eigvalsh(K2)), [0, 2])
assert np.isclose(np.array([1.0, 1.0]) @ K2 @ np.array([1.0, 1.0]), 0)

K3 = np.diag([4.0, 9.0])
assert np.allclose(sorted(np.linalg.eigvalsh(K3)), [4, 9])
cancel = np.array([1.0, 1.0, -1.0])
assert np.isclose(cancel @ K @ cancel, 0)

for printed in ("2.5", "0", "1", "3", "4", "9"):
    assert printed in target
assert 'title="Proof"' in prose
assert "**Your turn.**" in prose and 'collapse="true"' in prose
assert "## Check yourself" in prose
assert prose.count('title="Answer"') >= 3
print("gram-matrix checks passed")
