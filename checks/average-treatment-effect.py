"""Checks for the average-treatment-effect page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/average-treatment-effect.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Motivating example", "Definition", "Interpretation", "Worked example", "Connections", "History"], headings
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
assert "## Check yourself" not in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden, "missing answer callout"
for block in hidden:
    assert "{cite:" not in block
for match in re.finditer(r"\{\{cite:openintro2019\}\}\s*\(([^)]*)\)", prose):
    assert not re.search(r"\bp\.", match.group(1)), match.group(1)
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase

treated = [1, 0, 1, 0, 1, 0, 0, 1]
control = [1, 1, 0, 0, 1, 1, 0, 0]
assert len(treated) == 8 and len(control) == 8
differ = sum(a != b for a, b in zip(treated, control))
assert differ == 4
assert sum(treated) == 4 and sum(control) == 4
assert sum(treated) / 8 - sum(control) / 8 == 0
changed = treated[:-1] + [0]
assert sum(changed) == 3
assert sum(changed) / 8 - sum(control) / 8 == -1 / 8
assert "three patients" not in prose.lower()
assert "four of the eight" in prose.lower()
assert 10 / 20 == 0.5
assert abs((0.2 - 0.3) - (-0.1)) < 1e-12
assert 0.2 / 0.1 == 2
assert 0.001 * 100000 == 100
assert 0.10 * 100000 == 10000

print("average-treatment-effect:", len(cites), "cites")
