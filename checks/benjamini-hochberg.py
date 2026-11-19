"""Checks for the Benjamini–Hochberg article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown


import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/benjamini-hochberg.md").read_text(encoding="utf-8")
prose = shown(prose, "benjamini-hochberg")
article = root / "articles/benjamini-hochberg.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

def largest(ps, q):
    ps = np.asarray(ps, dtype=float)
    thr = np.arange(1, len(ps) + 1) * q / len(ps)
    ok = np.where(ps <= thr + 1e-15)[0]
    strict = np.where(ps < thr - 1e-15)[0]
    return (int(ok.max()) + 1 if len(ok) else 0,
            int(strict.max()) + 1 if len(strict) else 0,
            thr)

ps = [0.001, 0.012, 0.020, 0.039, 0.30]
k_closed, k_strict, thr = largest(ps, 0.05)
assert np.allclose(thr, [0.01, 0.02, 0.03, 0.04, 0.05])
assert k_closed == 4 and k_strict == 4
k2, _, thr2 = largest(ps, 0.02)
assert np.allclose(thr2, [0.004, 0.008, 0.012, 0.016, 0.020])
assert k2 == 1
tie = [0.001, 0.012, 0.030, 0.20, 0.40]
assert largest(tie, 0.05)[:2] == (3, 2)
assert largest([0.04, 0.20, 0.30, 0.40, 0.50], 0.05)[0] == 0

for printed in ("0.001", "0.012", "0.039", "0.30", "0.01", "0.04", "0.004", "0.008"):
    assert printed in target, printed
assert "**Your turn.**" in prose and prose.count('title="Answer"') >= 3
print("benjamini-hochberg checks passed")
