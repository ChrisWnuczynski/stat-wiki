"""Checks for ranking."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("ranking", [])
slug = "ranking"
text = (root / "research/content" / f"{slug}.md").read_text()
cites = re.findall(r"\{{cite:([a-z0-9_]+)\}}", text)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert "**Your turn.**" in text
assert '::: {.callout-tip collapse="true" title="Answer"}' in text
answer = text.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert 2 <= len(self_checks) <= 3
for item in self_checks:
    assert "{cite:" not in item["answer"]

def ranks(values):
    order = sorted(values)
    out = []
    for v in values:
        idxs = [i+1 for i,x in enumerate(order) if x == v]
        out.append(sum(idxs)/len(idxs))
    return out
assert ranks([8,3,8,1]) == [3.5, 2, 3.5, 1]
assert sum(ranks([8,3,8,1])) == 10
assert ranks([4,1,4,9]) == [2.5, 1, 2.5, 4]
assert sum(ranks([4,1,4,9])) == 10
assert 4*5/2 == 10
assert "3.5" in text and "2.5" in text
assert "37,457" in text

print(slug, "ok")
