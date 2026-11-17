"""Checks for morans-i."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "morans-i"
md = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5
assert len(set(cites)) >= 2
for key in set(cites):
    assert key in works, key
assert "## Motivating example" in md
assert "## Worked example" in md
assert "**Your turn.**" in md
assert '::: {.callout-tip collapse="true" title="Answer"}' in md
answer = md.split('::: {.callout-tip collapse="true" title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{{cite:" not in answer
assert "## Check yourself" not in md
dev = [-2, -1, 1, 2]
ss = sum(v * v for v in dev)
pairs = [(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 2)]
num = sum(dev[i] * dev[j] for i, j in pairs)
I = (4 / 6) * (num / ss)
assert ss == 10 and num == 6 and abs(I - 0.4) < 1e-12
dev2 = [-0.5, 0.5, 0.5, -0.5]
ss2 = sum(v * v for v in dev2)
num2 = sum(dev2[i] * dev2[j] for i, j in pairs)
I2 = (4 / 6) * (num2 / ss2)
assert abs(ss2 - 1) < 1e-12 and abs(num2 + 0.5) < 1e-12 and abs(I2 + 1 / 3) < 1e-12
assert "0.4" in md and "-1/3" in answer
assert "Ch. 8)" not in md
print(slug, "ok")
