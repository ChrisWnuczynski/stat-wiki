"""Checks for rounding."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("rounding", [])
slug = "rounding"
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

import math
shares = [285/600*30, 150/600*30, 90/600*30, 75/600*30]
assert shares == [14.25, 7.5, 4.5, 3.75]
assert sum(shares) == 30
half_up = [math.floor(x+0.5) for x in shares]
assert half_up == [14, 8, 5, 4]
assert sum(half_up) == 31
assert 14+7+5+4 == 30
exact = [30*x/3534 for x in (2451, 780, 198, 105)]
shown = [round(x, 2) for x in exact]
assert shown == [20.81, 6.62, 1.68, 0.89]
assert abs(sum(shown) - 30) < 1e-9
nearest = [math.floor(x+0.5) for x in shown]
assert nearest == [21, 7, 2, 1]
assert sum(nearest) == 31
assert 21+6+2+1 == 30
assert abs(0.851+0.150 - 1.001) < 1e-12
assert abs(2.5+2.5+3.2 - 8.2) < 1e-12
assert math.floor(2.5+0.5)+math.floor(2.5+0.5)+math.floor(3.2+0.5) == 9

print(slug, "ok")
