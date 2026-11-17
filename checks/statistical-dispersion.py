"""Checks for statistical-dispersion."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("statistical-dispersion", [])
slug = "statistical-dispersion"
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
vals = [2,4,4,7,8]
mean = sum(vals)/5
assert mean == 5
ss = sum((x-mean)**2 for x in vals)
assert ss == 24
assert ss/4 == 6
assert sum(abs(x-mean) for x in vals)/5 == 2
assert max(vals)-min(vals) == 6
fam = [0,0,1,1,2,3,6]
assert max(fam)-min(fam) == 6
m = F(sum(fam), 7)
aad = sum(abs(F(x)-m) for x in fam)/7
assert aad == F(76, 49)
assert abs(math.sqrt(25.52) - 5.05) < 0.01
assert 34/50 == 0.68 and 48/50 == 0.96
assert "25.52" in text and "5.05" in text
# a point 10 units out adds 100; a point 2 units out adds 4
assert 10**2 == 100 and 2**2 == 4

print(slug, "ok")
