"""Checks for the Wald-test article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown


from scipy.stats import norm

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/wald-test.md").read_text(encoding="utf-8")
prose = shown(prose, "wald-test")
article = root / "articles/wald-test.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

zcrit = norm.ppf(0.975)
assert round(zcrit, 3) == 1.960

def two_sided(z):
    return 2 * (1 - norm.cdf(z))

assert abs(0.8 / 0.25 - 3.2) < 1e-12
assert round(two_sided(3.2), 4) == 0.0014
assert abs(1.2 / 0.4 - 3) < 1e-12
assert round(two_sided(3), 4) == 0.0027
assert round(two_sided(1), 4) == 0.3173
assert round(two_sided(1.96), 4) == 0.0500

for printed in ("3.2", "0.0014", "0.0027", "0.3173", "0.0500", "1.960"):
    assert printed in target, printed
assert "**Your turn.**" in prose and prose.count('title="Answer"') >= 3
print("wald-test checks passed")
