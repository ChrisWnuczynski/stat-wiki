"""Check the philosophy-of-statistics field article against its pending file."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/philosophy-of-statistics.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/philosophy-of-statistics.json").read_text(encoding="utf-8"))
keys = re.findall(r"{{cite:([^}]+)}}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert "self_checks" not in pending
assert pending["kind"] == "field"
