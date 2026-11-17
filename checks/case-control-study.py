"""Checks for the case-control-study page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/case-control-study.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Motivating example", "Intuition", "Definition", "Properties", "Worked example", "Assumptions and limits", "Connections"], headings
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
assert (24 * 30) / (16 * 10) == 4.5
assert (24 * 34) / (16 * 10) == 5.1
assert 40 / 80 == 0.5

print("case-control-study:", len(cites), "cites")
