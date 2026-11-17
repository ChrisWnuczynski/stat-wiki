"""Checks for the robust-statistics page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "robust-statistics"
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

data = [1, 2, 3, 4, 20]
mean = sum(data) / 5
assert mean == 6
median = 3
l1_mean = sum(abs(v - mean) for v in data)
l1_med = sum(abs(v - median) for v in data)
l2_mean = sum((v - mean) ** 2 for v in data)
l2_med = sum((v - median) ** 2 for v in data)
assert l1_mean == 28 and l1_med == 21
assert l2_mean == 250 and l2_med == 295
wild = [5, 5, 5, 5, 100]
assert sum(wild) / 5 == 24
assert sum(abs(v - 5) for v in wild) == 95
assert "28" in prose and "21" in prose and "250" in prose

print(slug, "ok")
