"""Checks for sample variance and standard deviation."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

from math import sqrt

import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/sample-variance-and-standard-deviation.md").read_text(encoding="utf-8")
prose = shown(prose, "sample-variance-and-standard-deviation")
article = root / "articles/sample-variance-and-standard-deviation.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

x = np.array([2.0, 4.0, 4.0, 8.0])
assert x.mean() == 4.5
ss = np.sum((x - x.mean()) ** 2)
assert ss == 19
assert np.isclose(ss / 3, 19 / 3)
assert round(sqrt(19 / 3), 4) == 2.5166
assert np.isclose(ss / 4, 4.75)
y = np.array([2.0, 4.0, 4.0, 8.0, 4.0])
assert y.mean() == 4.4
assert np.isclose(np.sum((y - y.mean()) ** 2), 19.2)
assert np.isclose(y.var(ddof=1), 4.8)
assert np.isclose(10 / 5, 2) and np.isclose(10 / 6, 5 / 3)

for printed in ("4.5", "19/3", "2.5166", "4.75", "4.4", "19.2", "4.8"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("sample-variance checks passed")
