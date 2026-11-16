"""Check quadratic forms and chi-squared tails."""
from math import exp
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/multivariate-central-limit-theorem.md").read_text()
article = root / "articles/multivariate-central-limit-theorem.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

assert 80*(0.04+0.01) == 4
assert round(exp(-2), 4) == 0.1353
assert 20*0.25 == 5
assert round(exp(-2.5), 4) == 0.0821
assert (1+1)/80 == 0.025
for s in ("0.1353", "0.0821", "0.025", "0.2", "0.1", "0.5"):
    need(s)
assert 'title="Proof"' not in content
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("multivariate central limit theorem checks passed")
