"""Checks for the environmental-statistics field page."""
import json, re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/environmental-statistics.md").read_text()
pending = json.loads((root / "research/pending/environmental-statistics.json").read_text())
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
for heading in ("## Lead context", "## Definition", "## Statistical use", "## History", "## Connections"):
    assert heading in prose, heading
assert pending["kind"] == "field" and pending["topic"] == "Applications"
assert "self_checks" not in pending
print("environmental-statistics:", len(cites), "cites")
