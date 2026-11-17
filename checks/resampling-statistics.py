"""Checks for resampling-statistics."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'resampling-statistics'
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
bib = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert set(cites) <= set(bib["works"])
headings = ['Lead context', 'Motivating example', 'Definition', 'Interpretation', 'Worked example', 'Connections', 'History']
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
from fractions import Fraction as F
sample = [1, 2, 3]
mean = F(sum(sample), 3)
assert mean == 2
theta = sum((F(x) - mean) ** 2 for x in sample) / 3
assert theta == F(2, 3)
assert theta / 3 == F(2, 9)
leave = []
for i in range(3):
    sub = [sample[j] for j in range(3) if j != i]
    m = sum(sub) / 2
    leave.append(sum((x - m) ** 2 for x in sub) / 2)
assert leave == [0.25, 1, 0.25]
avg = sum(leave) / 3
assert avg == 0.5
bias = (3 - 1) * (F(avg) - F(2, 3))
assert bias == F(-1, 3)
assert F(2, 3) - bias == 1
boot = [4, 6.5, 6.5, 9]
assert sum(boot) / 4 == 6.5
for printed in ("2/9", "0.2222", r"\tfrac{1}{3}", "6.5"):
    assert printed in prose, printed
print(slug, "ok", words)
