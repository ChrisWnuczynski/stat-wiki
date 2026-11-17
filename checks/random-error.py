"""Checks for the random-error page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("random-error", [])
slug = "random-error"
prose = (root / f"research/content/{slug}.md").read_text(encoding="utf-8")
cites = re.findall(r"{{cite:([a-z0-9_]+)}}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "**Your turn.**" in prose
answer = re.search(
    r'::: {\.callout-tip collapse="true" title="Answer"}(.*?):::',
    prose,
    re.S,
)
assert answer, "missing answer callout"
assert "{{cite:" not in answer.group(1)
scs = self_checks
assert 2 <= len(scs) <= 3
for item in scs:
    assert "{{cite:" not in item["answer"]

import math
reads = [9.7, 10.2, 9.9, 10.4]
mean = sum(reads) / 4
assert abs(mean - 10.05) < 1e-12
ss = sum((v - mean) ** 2 for v in reads)
assert abs(ss - 0.29) < 1e-12
assert abs(math.sqrt(ss / 3) - 0.3109) < 5e-5
assert abs(math.sqrt(ss / 12) - 0.1555) < 5e-5
assert abs(mean - 10) - 0.05 < 1e-12
turn = [8, 10, 12]
assert sum(turn) / 3 == 10
assert sum((v - 10) ** 2 for v in turn) == 8
assert "0.29" in prose and "10.05" in prose

print(slug, "ok")
