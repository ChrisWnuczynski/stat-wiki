"""Checks for the Chapman–Kolmogorov article."""

from pathlib import Path

import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/chapman-kolmogorov-equations.md").read_text(encoding="utf-8")
article = root / "articles/chapman-kolmogorov-equations.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

P = np.array([[0.8, 0.2], [0.4, 0.6]])
P2 = P @ P
assert np.allclose(P2, [[0.72, 0.28], [0.56, 0.44]])
assert np.isclose(0.8 * 0.2 + 0.2 * 0.6, 0.28)
assert np.isclose(0.4 * 0.8 + 0.6 * 0.4, 0.56)
assert np.isclose(0.72 * 0.8 + 0.28 * 0.4, 0.688)
P3 = P2 @ P
assert np.isclose(P3[0, 0], 0.688)

for printed in ("0.72", "0.28", "0.56", "0.44", "0.16", "0.12", "0.32", "0.24", "0.688"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("chapman-kolmogorov checks passed")
