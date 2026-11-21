"""Checks for the Cramér–Rao article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown


root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/cramer-rao-lower-bound.md").read_text(encoding="utf-8")
prose = shown(prose, "cramer-rao-lower-bound")
article = root / "articles/cramer-rao-lower-bound.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

theta, n = 0.25, 20
bound = theta * (1 - theta) / n
assert bound == 0.009375
assert (0.5 * 0.5) / 10 == 0.025
# one Bernoulli score variance
assert abs(theta * (1 - theta) / (theta * (1 - theta)) ** 2 - 1 / (theta * (1 - theta))) < 1e-12
# one Poisson score variance is 1/lambda
lam = 2.0
assert abs((lam / lam ** 2) - (1 / lam)) < 1e-12

for printed in ("0.009375", "0.025"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("cramer-rao checks passed")
