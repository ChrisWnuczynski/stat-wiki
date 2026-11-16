"""Check exponential holding times."""
from math import exp
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/holding-time.md").read_text()
article = root / "articles/holding-time.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

assert round(exp(-3), 4) == 0.0498
assert round(exp(-2), 4) == 0.1353
assert 6/10 == 0.6 and 2/4 == 0.5 and 3/4 == 0.75
assert abs(1/10 - 0.1) < 1e-12 and abs(1/4 - 0.25) < 1e-12
for s in ("0.0498", "0.1353", "0.6", "0.25", "0.5", "0.75", "0.1"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("holding time checks passed")
