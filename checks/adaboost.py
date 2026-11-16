"""Check one AdaBoost round."""
from math import exp, log, sqrt
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/adaboost.md").read_text()
article = root / "articles/adaboost.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

eps = 0.25
alpha = 0.5*log((1-eps)/eps)
assert round(alpha, 3) == 0.549
assert round(exp(alpha), 3) == 1.732
assert round(exp(-alpha), 3) == 0.577
Z = 2*sqrt(eps*(1-eps))
assert round(Z, 3) == 0.866
assert abs((0.25*exp(alpha))/Z - 0.5) < 1e-12
assert abs((0.25*exp(-alpha))/Z - 1/6) < 1e-12
assert round(0.5*log(9), 3) == 1.099
assert 0.5*log(1) == 0
for s in ("0.549", "1.732", "0.577", "0.866", "1/2", "1/6", "1.099"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("AdaBoost checks passed")
