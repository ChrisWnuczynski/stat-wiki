"""Checks for multivariate-statistics."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "multivariate-statistics"
md = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
for key in set(cites):
    assert key in works, key
assert "**Your turn.**" in md
assert "## Check yourself" not in md
answer = md.split('::: {.callout-tip collapse="true" title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{{cite:" not in answer
heads = re.findall(r"^## (.+)$", md, re.M)
assert heads == [
    "Lead context",
    "Motivating example",
    "Intuition",
    "Definition",
    "Properties",
    "Worked example",
    "Assumptions and limits",
    "Connections",
]
assert len(md.split()) >= 1500
xs = [1, 2, 3]
ys = [2, 3, 1]
assert sum(xs) / 3 == 2 and sum(ys) / 3 == 2
dx = [x - 2 for x in xs]
dy = [y - 2 for y in ys]
assert sum(a * a for a in dx) == 2
assert sum(b * b for b in dy) == 2
assert sum(a * b for a, b in zip(dx, dy)) == -1
assert (-1 / 2) / (1 ** 0.5) == -0.5
pts = [(0, 0), (2, 0), (0, 2), (2, 2)]
mx = sum(p[0] for p in pts) / 4
my = sum(p[1] for p in pts) / 4
assert mx == 1 and my == 1
assert sum((p[0] - mx) * (p[1] - my) for p in pts) == 0
assert r"-\frac12" in md or "-1/2" in md
print(slug, "ok")
