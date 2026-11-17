"""Checks for the conjoint-analysis concept page."""
import json, re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("conjoint-analysis", [])
prose = (root / "research/content/conjoint-analysis.md").read_text()
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5
assert len(set(cites)) >= 2
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = prose.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert 2 <= len(self_checks) <= 3
assert 2 + 3 == 5
assert 0 + 0 == 0
assert 2 / 5 == 0.4
assert 4 ** 3 * 3 ** 2 == 576

print("conjoint-analysis:", len(cites), "cites")
