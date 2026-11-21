"""Check log-link means."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
from math import exp
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/positive-continuous-responses.md").read_text()
content = shown(content, "positive-continuous-responses")
article = root / "articles/positive-continuous-responses.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

assert round(exp(0.5), 3) == 1.649
assert round(exp(0.9), 3) == 2.460
assert round(exp(0.2), 3) == 1.221
assert abs(exp(0.5)*exp(0.4) - exp(0.9)) < 1e-12
assert 1/0.2 == 5 and abs(1/(-0.2) + 5) < 1e-12
assert round(10*exp(0.3), 3) == 13.499
assert round(exp(0.3), 3) == 1.350
for s in ("1.649", "2.460", "1.221", "13.499", "1.350"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("positive continuous response checks passed")
