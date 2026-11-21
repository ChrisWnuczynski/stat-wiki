"""Check the fill-in means."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/missing-data.md").read_text()
content = shown(content, "missing-data")
article = root / "articles/missing-data.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

assert (10+14+18)/3 == 14
assert (10+6+14+18)/4 == 12
assert (10+22+14+18)/4 == 16
assert (4+4+10)/3 == 6
assert 16-14 == 2 and 14-12 == 2
for s in ("14", "12", "16", "6"):
    need(s)
assert 'title="Proof"' not in content
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("missing data checks passed")
