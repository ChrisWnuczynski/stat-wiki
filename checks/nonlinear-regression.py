"""Checks for nonlinear-regression."""
import json
import math
import re
from pathlib import Path

import numpy as np

root = Path(__file__).resolve().parents[1]
slug = "nonlinear-regression"
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
for key in set(cites):
    assert key in works, key
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
assert "## Check yourself" not in prose
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    prose,
    re.S,
)
assert answer, "missing answer callout"
assert "{{cite:" not in answer.group(1)
x = np.array([0.0, 1.0, 2.0])
y = np.array([4.0, 2.0, 1.2])

def sse(b0, b1):
    return float(np.sum((y - b0 * np.exp(-b1 * x)) ** 2))

start = sse(4.0, 0.7)
assert abs(start - 0.04581671056721662) < 1e-12
assert abs(start - 0.045817) < 5e-7
b0, b1 = 3.9742, 0.6389
fitted = b0 * np.exp(-b1 * x)
value = float(np.sum((y - fitted) ** 2))
assert abs(value - 0.01881756470437959) < 1e-12
assert abs(value - 0.018818) < 5e-7
assert abs(value - 0.0188) < 5e-4
assert abs(sse(3.9742, 0.7) - 0.049755050055525676) < 1e-12
assert abs(sse(4.2, 0.6389) - 0.08799787472431406) < 1e-12
mx, my = 1.0, 2.4
sxx = 2.0
sxy = -2.8
slope, intercept = sxy / sxx, my - (sxy / sxx) * mx
assert slope == -1.4 and abs(intercept - 3.8) < 1e-12
line = intercept + slope * x
assert abs(float(np.sum((y - line) ** 2)) - 0.24) < 1e-12
for printed in ("0.045817", "0.018818", "0.049755", "0.087998", "0.24"):
    assert printed in prose, printed
assert "p. 372, not linear" not in prose
assert abs(math.log(5) - 1.60943791243) < 1e-8
assert r"\ln 5" in prose
print(slug, "ok")
