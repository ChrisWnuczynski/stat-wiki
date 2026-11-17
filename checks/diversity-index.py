"""Checks for the diversity-index concept page."""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("diversity-index", [])
prose = (root / "research/content/diversity-index.md").read_text()
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = prose.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert 2 <= len(self_checks) <= 3
for item in self_checks:
    assert "{cite:" not in item["answer"]

assert abs(0.6**2 + 0.3**2 + 0.1**2 - 0.46) < 1e-12
assert 6 * 5 + 3 * 2 + 1 * 0 == 36
assert 36 / 90 == 0.4
assert (0.5**2) + (0.5**2) == 0.5

print("diversity-index:", len(cites), "cites,", len(set(cites)), "keys")
