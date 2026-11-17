"""Checks for polynomial-least-squares."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'polynomial-least-squares'
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
assert "**Your turn.**" in prose
assert "## Check yourself" not in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden, "missing answer callout"
for block in hidden:
    assert "{cite:" not in block
# Four-point quadratic and the straight line on the same points.
xs = [0, 1, 2, 3]
ys = [1, 2, 2, 5]
# Claimed coefficients 1.2, -0.3, 0.5
b0, b1, b2 = 1.2, -0.3, 0.5
fitted = [b0 + b1 * x + b2 * x * x for x in xs]
resid = [y - f for y, f in zip(ys, fitted)]
assert abs(sum(r * r for r in resid) - 0.8) < 1e-12
n = 4
sx, sx2, sx3, sx4 = 6, 14, 36, 98
sy, sxy, sx2y = 10, 21, 55
assert abs(n * b0 + sx * b1 + sx2 * b2 - sy) < 1e-12
assert abs(sx * b0 + sx2 * b1 + sx3 * b2 - sxy) < 1e-12
assert abs(sx2 * b0 + sx3 * b1 + sx4 * b2 - sx2y) < 1e-12
mx, my = 1.5, 2.5
sxx = sum((x - mx) ** 2 for x in xs)
sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
slope = sxy / sxx
intercept = my - slope * mx
assert abs(slope - 1.2) < 1e-12 and abs(intercept - 0.7) < 1e-12
line = [intercept + slope * x for x in xs]
assert abs(sum((y - f) ** 2 for y, f in zip(ys, line)) - 1.8) < 1e-12
# Your turn: (x-1)^2
assert [1 - 2 * x + x * x for x in (0, 1, 2)] == [1, 0, 1]
for printed in ("1.2", "0.8", "1.8", "0.7"):
    assert printed in prose, printed
print(slug, "ok", words)
