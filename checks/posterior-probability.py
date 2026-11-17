"""Checks for posterior-probability."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = 'posterior-probability'
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
bib = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert set(cites) <= set(bib["works"])
headings = ['Lead context', 'Motivating example', 'Definition', 'Properties', 'Worked example', 'Assumptions and limits', 'History']
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
assert F(1, 4) * F(1, 2) == F(1, 8)
assert F(3, 4) * F(1, 6) == F(1, 8)
assert F(1, 8) + F(1, 8) == F(1, 4)
assert F(1, 8) / F(1, 4) == F(1, 2)
assert (F(1, 2) / F(1, 6)) * (F(1, 4) / F(3, 4)) == 1
assert F(1, 2) * F(1, 2) == F(1, 4)
assert F(1, 2) * F(1, 6) == F(1, 12)
assert F(1, 4) + F(1, 12) == F(1, 3)
assert F(1, 4) / F(1, 3) == F(3, 4)
# Carrier: prior 1/2, likelihoods 1/4 and 1.
carrier = (F(1, 4) * F(1, 2)) / (F(1, 4) * F(1, 2) + 1 * F(1, 2))
assert carrier == F(1, 5)
assert abs(float(carrier) - 0.2) < 1e-12
for printed in ("1/2", "3/4", "1/5", "0.2"):
    assert printed in prose, printed
assert "posterior-hypothesis-probability.qmd" in prose
print(slug, "ok", words)
