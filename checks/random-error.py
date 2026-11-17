"""Checks for random-error."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'random-error'
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
readings = [9.7, 10.2, 9.9, 10.4]
mean = sum(readings) / len(readings)
assert abs(mean - 10.05) < 1e-12
ssd = sum((r - mean) ** 2 for r in readings)
assert abs(ssd - 0.29) < 1e-12
assert abs(mean - 10 - 0.05) < 1e-12
three = [8, 10, 12]
assert sum(three) / 3 == 10
assert sum((r - 10) ** 2 for r in three) == 8
assert sum(three) / 3 - 10 == 0
for printed in ("10.05", "0.29", "0.05"):
    assert printed in prose, printed
print(slug, "ok", words)
