"""Checks for the three binary links."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

from math import exp

from scipy.stats import norm

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/logit-probit-and-complementary-log-log-links.md").read_text(encoding="utf-8")
prose = shown(prose, "logit-probit-and-complementary-log-log-links")
article = root / "articles/logit-probit-and-complementary-log-log-links.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

def logit(eta):
    return 1 / (1 + exp(-eta))

def clog(eta):
    return 1 - exp(-exp(eta))

assert round(logit(0.5), 4) == 0.6225
assert round(float(norm.cdf(0.5)), 4) == 0.6915
assert round(clog(0.5), 4) == 0.8077
assert round(logit(-0.5), 4) == 0.3775
assert round(float(norm.cdf(-0.5)), 4) == 0.3085
assert round(clog(-0.5), 4) == 0.4548
assert round(1 - 0.8077, 4) == 0.1923
assert round(clog(0), 4) == 0.6321
assert round(exp(0.5), 4) == 1.6487
assert abs(logit(-0.5) - (1 - logit(0.5))) < 1e-12

for printed in ("0.6225", "0.6915", "0.8077", "0.3775", "0.3085", "0.4548", "0.1923", "0.6321", "1.6487"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("links checks passed")
