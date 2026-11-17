"""Checks for regression-analysis."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'regression-analysis'
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
bib = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert set(cites) <= set(bib["works"])
headings = ['Lead context', 'Motivating example', 'Definition', 'Properties', 'Statistical use', 'Worked example', 'Common misconceptions', 'History', 'Connections']
positions = []
for heading in headings:
    idx = prose.find("## " + heading)
    assert idx != -1, heading
    positions.append(idx)
assert positions == sorted(positions)
found = re.findall(r"^## .+$", prose, flags=re.M)
assert found == ["## " + h for h in headings], found
for phrase in (
    'not a claim',
    'not claimed',
    'this page',
    'Dodge states',
    'the manual',
    'question book',
    'question bank',
    'letter opener',
    'Wikipedia',
    'Grokipedia',
):
    assert phrase not in prose, phrase
for match in re.finditer(r"\{\{cite:openintro2019\}\}\s*\(([^)]*)\)", prose):
    locator = match.group(1)
    assert "p." not in locator, locator
    assert "Ch." in locator or "§" in locator, locator
words = len(prose.split())
assert words >= 1500, words
assert "**Your turn.**" in prose
assert "## Check yourself" not in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden, "missing answer callout"
for block in hidden:
    assert "{cite:" not in block
from fractions import Fraction as F
xs = [0, 1, 2]
ys = [1, 3, 3]
n = 3
mx = F(sum(xs), n)
my = F(sum(ys), n)
assert mx == 1 and my == F(7, 3)
sxx = sum((F(x) - mx) ** 2 for x in xs)
sxy = sum((F(x) - mx) * (F(y) - my) for x, y in zip(xs, ys))
assert sxx == 2 and sxy == 2
b1 = sxy / sxx
b0 = my - b1 * mx
assert b1 == 1 and b0 == F(4, 3)
fitted = [b0 + b1 * x for x in xs]
resid = [F(y) - f for y, f in zip(ys, fitted)]
rss = sum(r * r for r in resid)
assert rss == F(2, 3)
null = sum((F(y) - my) ** 2 for y in ys)
assert null == F(8, 3)
assert (null - rss) / null == F(3, 4)
assert b0 + b1 * 4 == F(16, 3)
# Your turn
xs2, ys2 = [1, 3], [2, 6]
mx2, my2 = 2, 4
sxx2 = sum((x - mx2) ** 2 for x in xs2)
sxy2 = sum((x - mx2) * (y - my2) for x, y in zip(xs2, ys2))
assert sxx2 == 2 and sxy2 == 4
assert sxy2 / sxx2 == 2
assert my2 - 2 * mx2 == 0
for link in (
    "simple-linear-regression.qmd",
    "multiple-linear-regression.qmd",
    "ordinary-least-squares.qmd",
    "polynomial-least-squares.qmd",
    "nonlinear-regression.qmd",
):
    assert link in prose, link
for printed in ("4/3", "2/3", "8/3", "3/4"):
    assert printed in prose, printed
print(slug, "ok", words)
