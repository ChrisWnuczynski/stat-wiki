"""Checks for risk-assessment."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'risk-assessment'
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
bib = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert set(cites) <= set(bib["works"])
headings = ['Lead context', 'Intuition', 'Definition', 'Statistical use', 'Assumptions and limits', 'History']
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
assert abs(0.04 / 0.02 - 2) < 1e-12
assert abs(0.04 - 0.02 - 0.02) < 1e-12
assert 500 / 10000 == 0.05
assert 1000 / 10000 == 0.10
assert (1000 / 10000) / (500 / 10000) == 2
assert abs(0.001 - 1 / 1000) < 1e-15
for printed in ("0.02", "0.04", "0.001"):
    assert printed in prose, printed
print(slug, "ok", words)
