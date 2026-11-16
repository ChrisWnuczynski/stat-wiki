"""Check the two-variable correlation loadings."""
from math import sqrt
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/loadings.md").read_text()
article = root / "articles/loadings.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

# characteristic polynomial lambda^2 - 2 lambda + 0.36 = 0
disc = 4 - 1.44
assert abs(disc - 2.56) < 1e-12
roots = ((2+disc**0.5)/2, (2-disc**0.5)/2)
assert abs(roots[0]-1.8) < 1e-12 and abs(roots[1]-0.2) < 1e-12
assert abs(1.8/2 - 0.9) < 1e-12
assert round(sqrt(0.9), 3) == 0.949
assert round(1/sqrt(2), 3) == 0.707
assert abs(0.6*sqrt(0.25) - 0.3) < 1e-12
assert abs(0.2/2 - 0.1) < 1e-12
for s in ("1.8", "0.2", "0.9", "0.949", "0.707", "0.3", "0.1"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("loadings checks passed")
