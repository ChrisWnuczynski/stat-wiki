"""Checks for the resampling-statistics page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "resampling-statistics"
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

from itertools import product
obs = (1, 2, 3)
means = [sum(s) / 3 for s in product(obs, repeat=3)]
assert len(means) == 27
assert abs(sum(means) / 27 - 2) < 1e-12
var = sum((m - 2) ** 2 for m in means) / 27
assert abs(var - 2 / 9) < 1e-12
theta = 2 / 3
reps = (0.25, 1.0, 0.25)
avg = sum(reps) / 3
bias = 2 * (avg - theta)
assert abs(bias - (-1 / 3)) < 1e-12
assert abs(theta - bias - 1) < 1e-12
boot = [4, 6.5, 6.5, 9]
assert abs(sum(boot) / 4 - 6.5) < 1e-12
assert "2/9" in prose or "2/9" in prose

print(slug, "ok")
