"""Checks for probability-theory."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'probability-theory'
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
assert words >= 1500, words
assert "**Your turn.**" in prose
assert "## Check yourself" not in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden, "missing answer callout"
for block in hidden:
    assert "{cite:" not in block
from fractions import Fraction as F
assert F(1, 4) * 3 == F(3, 4)
assert F(3, 4) + F(1, 2) - F(1, 2) == F(3, 4)
assert 1 - F(3, 4) == F(1, 4)
assert F(1, 2) / F(3, 4) == F(2, 3)
assert F(1, 4) / F(3, 4) == F(1, 3)
assert F(1, 2) * F(1, 2) == F(1, 4)
assert F(3, 4) * F(1, 2) == F(3, 8)
for printed in ("3/4", "1/4", "2/3", "1/3"):
    assert printed in prose, printed
print(slug, "ok", words)
