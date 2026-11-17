"""Checks for fat-tails."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "fat-tails"
text = (root / "research/content" / f"{slug}.md").read_text()
pending = json.loads((root / "research/pending" / f"{slug}.json").read_text())
cites = re.findall(r"\{{cite:([a-z0-9_]+)\}}", text)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert set(cites) <= set(pending["cite_keys"])
for heading in ("Motivating example", "Worked example", "Intuition", "Definition", "Properties", "Statistical use", "Common misconceptions", "Assumptions and limits", "Connections", "History", "Lead context"):
    assert f"## {heading}" in text, heading
assert "**Your turn.**" in text
assert '::: {.callout-tip collapse="true" title="Answer"}' in text
answer = text.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert 2 <= len(pending["self_checks"]) <= 3
for item in pending["self_checks"]:
    assert "{cite:" not in item["answer"]
assert pending["kind"] == "concept"

def kurt(v):
    n = len(v)
    m = sum(v)/n
    m2 = sum((x-m)**2 for x in v)/n
    m4 = sum((x-m)**4 for x in v)/n
    return m4/m2**2
assert kurt([1,2,3,4,5]) == 1.7
assert kurt([1,1,1,1,6]) == 3.25
# unit exponential central fourth moment
# raw moments 1,2,6,24
mu4 = 24 - 4*6 + 6*2 - 4*1 + 1
assert mu4 == 9
assert abs(math.exp(-4) - 0.01831563888873418) < 1e-15
assert abs(math.exp(-1) - 0.36787944117) < 1e-8
assert "0.018316" in text
assert "1.7" in text and "3.25" in text
assert "6,693" in text and "998.389" in text

print(slug, "ok")
