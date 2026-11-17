"""Check research/content/probability-theory.md against its pending record."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/probability-theory.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/probability-theory.json").read_text(encoding="utf-8"))
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, len(keys)
assert len(set(keys)) >= 2, set(keys)
assert set(keys) <= set(pending["cite_keys"])
for heading in ('## Lead context', '## Definition', '## Statistical use', '## History', '## Connections'):
    assert heading in prose, heading
order = [prose.index(h) for h in ('## Lead context', '## Definition', '## Statistical use', '## History', '## Connections')]
assert order == sorted(order)
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert pending["action"] == "page"
assert pending["kind"] == "field"
assert "self_checks" not in pending
print("probability-theory passed")
