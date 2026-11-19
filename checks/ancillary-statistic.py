"""Checks for the ancillary-statistic article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown


import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/ancillary-statistic.md").read_text(encoding="utf-8")
prose = shown(prose, "ancillary-statistic")
article = root / "articles/ancillary-statistic.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

def centre(x):
    x = np.asarray(x, dtype=float)
    return x - x.mean()

a = centre([3, 5, 7])
assert np.allclose(a, [-2, 0, 2])
assert np.allclose(centre(np.array([3, 5, 7]) + 4), a)
assert np.allclose(centre(np.array([3, 5, 7]) + 10), a)
assert np.allclose(centre([1, 1, 4]), [-1, -1, 2])
assert np.isclose(centre([1, 1, 4]).sum(), 0)
assert np.allclose(centre(2 * np.array([3.0, 5, 7])), 2 * a)

assert "**Your turn.**" in prose and prose.count('title="Answer"') >= 3
print("ancillary-statistic checks passed")
