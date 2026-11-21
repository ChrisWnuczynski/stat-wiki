"""Check the three-point least-squares slope."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/regression-slope.md").read_text()
content = shown(content, "regression-slope")
article = root / "articles/regression-slope.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

xs, ys = (1, 2, 4), (1, 2, 6)
n = 3
xb, yb = sum(xs)/n, sum(ys)/n
sxx = sum((x-xb)**2 for x in xs)
sxy = sum((x-xb)*(y-yb) for x, y in zip(xs, ys))
syy = sum((y-yb)**2 for y in ys)
assert abs(xb - 7/3) < 1e-12 and yb == 3
assert abs(sxx - 14/3) < 1e-12 and sxy == 8 and syy == 14
slope = sxy/sxx
assert abs(slope - 12/7) < 1e-12 and round(slope, 3) == 1.714
intercept = yb - slope*xb
assert abs(intercept + 1) < 1e-9
assert abs(sxy/syy - 4/7) < 1e-12 and round(4/7, 3) == 0.571
assert abs(7/12 - 0.583) < 0.0005
assert abs(-1 + (12/7)*3 - 29/7) < 1e-9 and round(29/7, 3) == 4.143
xs2, ys2 = (0, 1, 2), (1, 3, 5)
xb2, yb2 = 1, 3
sxx2 = sum((x-xb2)**2 for x in xs2)
sxy2 = sum((x-xb2)*(y-yb2) for x, y in zip(xs2, ys2))
assert sxx2 == 2 and sxy2 == 4 and sxy2/sxx2 == 2
for s in ("1.714", "0.571", "0.583", "4.143", "12/7", "4/7"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("regression slope checks passed")
