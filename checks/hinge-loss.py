"""Check hinge values and the penalised criterion."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/hinge-loss.md").read_text()
content = shown(content, "hinge-loss")
article = root / "articles/hinge-loss.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

def hinge(m):
    return max(0, 1-m)
assert [hinge(m) for m in (1.4, 0.25, -0.5)] == [0, 0.75, 1.5]
assert 0+0.75+1.5 == 2.25
assert (1-4)**2 == 9 and hinge(4) == 0
assert hinge(1) == 0 and hinge(-2) == 3
assert hinge(0.2) == 0.8
assert 2.25 + 1 == 3.25
for s in ("0.75", "1.5", "2.25", "3.25", "0.8"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("hinge loss checks passed")
