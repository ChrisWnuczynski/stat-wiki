"""Checks for the polynomial-least-squares page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "polynomial-least-squares"
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

xs = [0, 1, 2, 3]
ys = [1, 2, 2, 5]
# normal equations for degree 2
# solved coefficients
b0, b1, b2 = 1.2, -0.3, 0.5
fitted = [b0 + b1 * x + b2 * x * x for x in xs]
resid = [y - f for y, f in zip(ys, fitted)]
assert abs(sum(r * r for r in resid) - 0.8) < 1e-12
# line
n = 4
mx, my = sum(xs) / n, sum(ys) / n
sxx = sum((x - mx) ** 2 for x in xs)
sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
slope = sxy / sxx
intercept = my - slope * mx
line_sse = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
assert abs(line_sse - 1.8) < 1e-12
assert "0.8" in prose and "1.8" in prose and "1.2" in prose
# your turn (x-1)^2
for x, y in ((0, 1), (1, 0), (2, 1)):
    assert y == 1 - 2 * x + x * x

print(slug, "ok")
