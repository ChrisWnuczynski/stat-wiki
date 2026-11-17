"""Field-page checks for statistical-process-control."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
md = (root / "research/content/statistical-process-control.md").read_text()
meta = json.loads((root / "research/pending/statistical-process-control.json").read_text())
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "**Your turn.**" not in md
assert "## Check yourself" not in md
for heading in ("## Lead context", "## Definition", "## Statistical use", "## History", "## Connections"):
    assert heading in md, heading
assert meta["action"] == "page"
assert meta["kind"] == "field"
assert set(cites) <= set(meta["cite_keys"])
print("statistical-process-control checks passed")
