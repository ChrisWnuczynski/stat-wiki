"""Checks for ranking."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'ranking'
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
ranks = [3.5, 2, 3.5, 1]
assert sum(ranks) == 10
assert sum(ranks) == 4 * 5 / 2
tied = [2.5, 1, 2.5, 4]
assert sum(tied) == 10
assert (3 + 4) / 2 == 3.5
assert (2 + 3) / 2 == 2.5
assert "0.51" in prose
for printed in ("3.5", "2.5"):
    assert printed in prose, printed
print(slug, "ok", words)
