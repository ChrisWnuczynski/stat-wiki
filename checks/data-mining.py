"""Checks for the data-mining field page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/data-mining.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/data-mining.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
positions = [prose.index(h) for h in ['## Lead context', '## Definition', '## Statistical use', '## History', '## Connections']]
assert positions == sorted(positions)
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert "self_checks" not in pending
print("data-mining checks passed")
