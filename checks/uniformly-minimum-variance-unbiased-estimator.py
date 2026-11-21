"""Checks for the UMVU article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

from math import comb, exp

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/uniformly-minimum-variance-unbiased-estimator.md").read_text(encoding="utf-8")
prose = shown(prose, "uniformly-minimum-variance-unbiased-estimator")
article = root / "articles/uniformly-minimum-variance-unbiased-estimator.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

def U(n, k, t):
    if t < k:
        return 0.0
    return comb(t, k) * (1 / n) ** k * (1 - 1 / n) ** (t - k)

assert U(4, 1, 3) == 27 / 64 == 0.421875
assert round(exp(-3 / 4) * (3 / 4), 4) == 0.3543
assert U(4, 0, 2) == 0.5625
assert round(exp(-0.5), 4) == 0.6065
assert U(2, 0, 1) == 0.5

for printed in ("0.421875", "0.3543", "0.5625", "0.6065", "27", "64", "9/16"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("umvue checks passed")
