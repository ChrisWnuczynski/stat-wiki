"""Check the three-node clique weights."""
from math import exp
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/hammersley-clifford.md").read_text()
article = root / "articles/hammersley-clifford.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

assert round(exp(0.5), 3) == 1.649
assert round(exp(0.3), 3) == 1.350
weights = [1, 1, 1, 1, exp(0.5), 1, exp(0.3), exp(0.8)]
assert round(sum(weights), 3) == 10.224
assert round(exp(0.5)/(1+exp(0.5)), 3) == 0.622
assert round(exp(0.3)/(1+exp(0.3)), 3) == 0.574
for s in ("1.649", "1.350", "10.224", "0.622", "0.574", "0.5", "0.3"):
    need(s)
assert 'title="Proof"' not in content
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("Hammersley–Clifford checks passed")
