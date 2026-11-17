"""Checks for tail."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("tail", [])
slug = "tail"
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

z = (1190-1100)/200
assert z == 0.45
assert abs(1 - 0.6736 - 0.3264) < 1e-12
assert abs(1 - 0.8413447 - 0.1586553) < 1e-12
assert abs(math.exp(-2) - 0.1353352832366) < 1e-12
assert abs(math.exp(-4) - 0.0183156388887) < 1e-12
assert abs(1 - math.exp(-2) - 0.864664716763) < 1e-9
for printed in ("0.3264", "0.6736", "0.8413447", "0.1586553", "0.135335"):
    assert printed in text, printed

print(slug, "ok")
