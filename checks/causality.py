"""Checks for the causality page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/causality.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Motivating example", "Definition", "Properties", "Statistical use", "Worked example", "Common misconceptions", "History", "Connections"], headings
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
assert "## Check yourself" not in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden, "missing answer callout"
for block in hidden:
    assert "{cite:" not in block
for hit in re.finditer(r"\{\{cite:openintro2019\}\}\s*\(([^)]*)\)", prose):
    assert not re.search(r"\bp\.", hit.group(1)), hit.group(1)
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase
treated = [1, 0, 1, 1, 0]
untreated = [0, 0, 1, 0, 0]
assert sum(a != b for a, b in zip(treated, untreated)) == 2
assert sum(treated) / 5 == 0.6
assert sum(untreated) / 5 == 0.2
assert abs((sum(treated) / 5 - sum(untreated) / 5) - 0.4) < 1e-12
corrected = [0, 0, 0, 0, 0]
assert sum(corrected) / 5 == 0
assert 0.6 - 0 == 0.6
assert 0.2 / 0.1 == 2
assert 0.001 * 100000 == 100
assert 0.10 * 100000 == 10000

print("causality:", len(cites), "cites")
