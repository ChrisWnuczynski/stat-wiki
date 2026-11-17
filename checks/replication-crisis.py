"""Checks for replication-crisis."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'replication-crisis'
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
bib = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert set(cites) <= set(bib["works"])
headings = ['Lead context', 'Definition', 'Properties', 'History', 'Connections']
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
assert words >= 1000, words
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert abs(35 / 97 - 0.360824742268) < 1e-9
assert 26 + 6 + 2 == 34
assert 20 / 32 == 0.625
assert abs(0.197 / 0.403 - 0.488833746898) < 1e-9
for printed in ("36.1", "0.403", "0.197", "0.51", "0.92"):
    assert printed in prose, printed
print(slug, "ok", words)
