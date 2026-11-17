"""Checks for pearson-distribution."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "pearson-distribution"
text = (root / "research/content" / f"{slug}.md").read_text()
pending = json.loads((root / "research/pending" / f"{slug}.json").read_text())
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", text)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert set(cites) <= set(pending["cite_keys"])
for heading in (
    "Lead context",
    "Motivating example",
    "Intuition",
    "Definition",
    "Properties",
    "Statistical use",
    "Worked example",
    "Common misconceptions",
    "Assumptions and limits",
    "Connections",
    "History",
):
    assert f"## {heading}" in text, heading
assert "**Your turn.**" in text
assert '::: {.callout-tip collapse="true" title="Answer"}' in text
answer = text.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{{cite:" not in answer
assert 2 <= len(pending["self_checks"]) <= 3
for item in pending["self_checks"]:
    assert "{{cite:" not in item["answer"]
assert pending["kind"] == "concept"
assert pending["topic"] == "Probability distributions"
assert pending["action"] == "page"

# n = 100 boundary for a trigonometric integral.
half = math.sqrt(0.0101)
assert abs(0.5 + half - 0.600498756) < 1e-8
assert abs(0.5 - half - 0.399501244) < 1e-8
assert round(0.5 + half, 4) == 0.6005
assert round(0.5 - half, 4) == 0.3995

# Type III, p = 3, gamma = 2.
p, gamma = 3, 2
mu2 = (p + 1) / gamma**2
mu3 = 2 * (p + 1) / gamma**3
mu4 = 3 * (p + 1) * (p + 3) / gamma**4
assert mu2 == 1 and mu3 == 1 and mu4 == 4.5
assert mu3 / mu2**1.5 == 1
assert 0.5 * mu3 / mu2**1.5 == 0.5
assert 1 / math.sqrt(p + 1) == 0.5
assert mu4 / mu2**2 == 4.5

# Your turn: p = 8, gamma = 1.
p, gamma = 8, 1
mu2 = (p + 1) / gamma**2
mu4 = 3 * (p + 1) * (p + 3) / gamma**4
assert mu2 == 9
assert 1 / math.sqrt(p + 1) == 1 / 3
assert mu4 / mu2**2 == 11 / 3

for printed in ("0.3995", "0.6005", "9/2", "11/3"):
    assert printed in text, printed
print(slug, "ok")
