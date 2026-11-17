"""Checks for the harking concept page."""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/harking.md").read_text()
pending = json.loads((root / "research/pending/harking.json").read_text())
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

assert 20 * 0.05 == 1
assert abs(20 * 0.01 - 0.2) < 1e-12

print("harking:", len(cites), "cites,", len(set(cites)), "keys")
