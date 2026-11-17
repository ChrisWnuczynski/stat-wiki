"""Checks for pearson-distribution."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'pearson-distribution'
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
bib = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert set(cites) <= set(bib["works"])
headings = ['Lead context', 'Motivating example', 'Intuition', 'Definition', 'Properties', 'Worked example', 'Assumptions and limits', 'Connections']
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
import math
half = math.sqrt(0.0101)
assert abs(0.5 + half - 0.600498756) < 1e-8
assert abs(0.5 - half - 0.399501244) < 1e-8
assert round(0.5 + half, 4) == 0.6005
assert round(0.5 - half, 4) == 0.3995
p, gamma = 3, 2
mu2 = (p + 1) / gamma ** 2
mu3 = 2 * (p + 1) / gamma ** 3
mu4 = 3 * (p + 1) * (p + 3) / gamma ** 4
assert mu2 == 1 and mu3 == 1 and mu4 == 4.5
assert 1 / math.sqrt(p + 1) == 0.5
assert mu4 / mu2 ** 2 == 4.5
p, gamma = 8, 1
mu2 = (p + 1) / gamma ** 2
mu4 = 3 * (p + 1) * (p + 3) / gamma ** 4
assert mu2 == 9
assert abs(1 / math.sqrt(p + 1) - 1 / 3) < 1e-12
assert mu4 / mu2 ** 2 == 11 / 3
for printed in ("0.3995", "0.6005", "9/2", "11/3"):
    assert printed in prose, printed
print(slug, "ok", words)
