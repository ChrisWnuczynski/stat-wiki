"""Arithmetic checks for the soft-margin primal article."""

from pathlib import Path

import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/soft-margin-primal.md").read_text(encoding="utf-8")
article = root / "articles/soft-margin-primal.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

beta = np.array([1.0, 0.0])
assert np.isclose(0.5 * beta @ beta, 0.5)
assert np.isclose(1 / np.linalg.norm(beta), 1)
margins = np.array([2.0, 0.5, -0.25])
slacks = np.maximum(0, 1 - margins)
assert np.allclose(slacks, [0, 0.5, 1.25])
assert np.isclose(slacks.sum(), 1.75)
assert np.isclose(0.5 + 2 * slacks.sum(), 4)
assert np.isclose(0.5 + 1 * slacks.sum(), 2.25)
assert np.isclose(0.2 + 5 * 0.8, 4.2)
assert np.isclose(max(0, 1 - 1.4), 0)

for printed in ("0.5", "1.25", "1.75", "2.25", "4.2", "-0.25"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("soft-margin-primal checks passed")
