"""Checks for the diversity-index concept page."""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/diversity-index.md").read_text()
pending = json.loads((root / "research/pending/diversity-index.json").read_text())
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
assert "## Check yourself" not in prose
answer = prose.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert pending["kind"] == "concept"
assert pending["topic"] == "Applications"
assert 2 <= len(pending["self_checks"]) <= 3
for item in pending["self_checks"]:
    assert "{cite:" not in item["answer"]

assert abs(0.6**2 + 0.3**2 + 0.1**2 - 0.46) < 1e-12
assert 6 * 5 + 3 * 2 + 1 * 0 == 36
assert 36 / 90 == 0.4
assert (0.5**2) + (0.5**2) == 0.5

print("diversity-index:", len(cites), "cites,", len(set(cites)), "keys")
