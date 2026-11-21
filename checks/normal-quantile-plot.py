"""Check normal scores and reference lines."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
from scipy.stats import norm
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/normal-quantile-plot.md").read_text()
content = shown(content, "normal-quantile-plot")
article = root / "articles/normal-quantile-plot.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

scores = [round(float(norm.ppf(i/5)), 3) for i in (1, 2, 3, 4)]
assert scores == [-0.842, -0.253, 0.253, 0.842]
line = [round(10 + 2*z, 2) for z in scores]
assert line == [8.32, 9.49, 10.51, 11.68]
scores3 = [round(float(norm.ppf(p)), 3) for p in (0.25, 0.5, 0.75)]
assert scores3 == [-0.674, 0.0, 0.674]
assert round(5 + 2*(-0.674), 2) == 3.65
assert round(5 + 2*0.674, 2) == 6.35
for s in ("-0.842", "-0.253", "0.253", "0.842", "8.32", "9.49", "10.51", "11.68",
          "-0.674", "0.674", "3.65", "6.35"):
    need(s)
assert 'title="Proof"' not in content
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("normal quantile plot checks passed")
