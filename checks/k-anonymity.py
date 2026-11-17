"""Checks for the k-anonymity concept page."""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("k-anonymity", [])
prose = (root / "research/content/k-anonymity.md").read_text()
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

assert min(3, 1) == 1
assert min(3, 2) == 2

print("k-anonymity:", len(cites), "cites,", len(set(cites)), "keys")
