"""Checks for kurtosis."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("kurtosis", [])
slug = "kurtosis"
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

def moments(v):
    n = len(v)
    m = sum(v)/n
    m2 = sum((x-m)**2 for x in v)/n
    m4 = sum((x-m)**4 for x in v)/n
    return m2, m4, m4/m2**2
assert moments([1,2,3,4,5]) == (2, 6.8, 1.7)
assert moments([1,1,1,1,6])[2] == 3.25
m2, m4, k = moments([0,0,0,0,0,6])
assert m2 == 5 and m4 == 105 and k == 4.2
assert "1.7" in text and "3.25" in text and "4.2" in text
assert "2.96" in text and "5.9" in text and "6,693" in text

print(slug, "ok")
