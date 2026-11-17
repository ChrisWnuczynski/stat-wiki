"""Checks for the nonlinear-regression page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "nonlinear-regression"
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
import numpy as np
x = np.array([0.0, 1.0, 2.0])
y = np.array([4.0, 2.0, 1.2])
b0, b1 = 3.9742, 0.6389
fitted = b0 * np.exp(-b1 * x)
sse = float(np.sum((y - fitted) ** 2))
assert abs(sse - 0.01881756470437959) < 1e-12
assert abs(sse - 0.0188) < 5e-4
# straight line
mx, my = 1.0, 2.4
sxx = 2.0
sxy = -2.8
slope, intercept = sxy / sxx, my - (sxy / sxx) * mx
assert slope == -1.4 and abs(intercept - 3.8) < 1e-12
line = intercept + slope * x
assert abs(float(np.sum((y - line) ** 2)) - 0.24) < 1e-12
assert "0.0188" in prose and "0.24" in prose
# your turn
assert abs(math.log(5) - 1.60943791243) < 1e-8
assert "ln 5" in prose or "ln5" in prose or r"\ln 5" in prose

print(slug, "ok")
