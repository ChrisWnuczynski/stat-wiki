"""Checks for the abundance-estimation concept page."""
import json, re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("abundance-estimation", [])
prose = (root / "research/content/abundance-estimation.md").read_text()
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5
assert len(set(cites)) >= 2
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = prose.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert 2 <= len(self_checks) <= 3
assert (15 * 20) / 5 == 60
assert (21 * 16) / 6 - 1 == 55
assert (15 * 20) / 10 == 30

print("abundance-estimation:", len(cites), "cites")
