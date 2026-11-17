"""Checks for harmonic-mean."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("harmonic-mean", [])
slug = "harmonic-mean"
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

from fractions import Fraction as F
assert F(3) / (F(1,5)+F(1,10)+F(1,15)) == F(90,11)
assert (5+10+15)/3 == 10
assert F(3) / (F(1,100)+F(1,200)+F(1,300)) == F(1800,11)
assert round(1800/11) == 164
assert abs(36/11 - 3.272727) < 1e-6
assert abs(31/6 - 5.166666) < 1e-6
# Dodge's six-value illustration
recs = [1, F(1,2), F(1,3), F(1,4), F(1,5), F(1,100)]
H = 6 / sum(recs)
assert round(float(H), 2) == 2.62
assert round(115/6, 2) == 19.17
assert "90/11" in text or "90}{11" in text or r"\frac{90}{11}" in text
assert "8.1818" in text
assert "164" in text

print(slug, "ok")
