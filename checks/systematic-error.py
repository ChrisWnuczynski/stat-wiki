"""Checks for the systematic-error page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "systematic-error"
prose = (root / f"research/content/{slug}.md").read_text(encoding="utf-8")
pending = json.loads((root / f"research/pending/{slug}.json").read_text(encoding="utf-8"))
cites = re.findall(r"{{cite:([a-z0-9_]+)}}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
assert "## Check yourself" not in prose
answer = re.search(
    r'::: {\.callout-tip collapse="true" title="Answer"}(.*?):::',
    prose,
    re.S,
)
assert answer, "missing answer callout"
assert "{{cite:" not in answer.group(1)
scs = pending["self_checks"]
assert 2 <= len(scs) <= 3
for item in scs:
    assert "{{cite:" not in item["answer"]

import math
reads = [21.4, 21.7, 21.2, 21.5]
mean = sum(reads) / 4
assert abs(mean - 21.45) < 1e-12
assert abs(mean - 20 - 1.45) < 1e-12
ss = sum((v - mean) ** 2 for v in reads)
assert abs(ss - 0.13) < 1e-12
assert abs(math.sqrt(0.13 / 12) - 0.10408329997330664) < 1e-12
gauge = [12, 11, 13]
assert sum(gauge) / 3 == 12
assert abs(sum(gauge) / 3 - 10 - 2) < 1e-12
assert "1.45" in prose and "0.13" in prose

print(slug, "ok")
