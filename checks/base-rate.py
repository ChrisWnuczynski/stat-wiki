"""Checks for the base-rate page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/base-rate.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Motivating example", "Intuition", "Definition", "Properties", "Worked example", "Assumptions and limits", "Connections"], headings
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
match = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::',
    prose,
    re.S,
)
assert match, "missing answer callout"
assert "{cite:" not in match.group(1)
assert "## Check yourself" not in prose
for hit in re.finditer(r"\{\{cite:openintro2019\}\}\s*\(([^)]*)\)", prose):
    assert not re.search(r"\bp\.", hit.group(1)), hit.group(1)
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase

num = 0.0035 * 0.89
den = num + 0.9965 * 0.07
assert abs(num / den - 0.04275) < 5e-4
num2 = 0.20 * 0.89
den2 = num2 + 0.80 * 0.07
assert abs(num2 / den2 - 0.76068376) < 1e-6
assert abs((0.01 * 0.90) / (0.01 * 0.90 + 0.99 * 0.05) - 0.1538461538) < 1e-9

print("base-rate:", len(cites), "cites")
