"""Check the standard-score page."""
import math
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/standard-score.md").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5 and len(set(keys)) >= 2
assert "**Your turn.**" in prose
assert (2+4+4+6)/4 == 4
assert (2-4)**2 + (6-4)**2 == 8
assert math.isclose((6-4)/math.sqrt(2), math.sqrt(2))
assert (4-4)/math.sqrt(2) == 0
assert math.isclose(2/math.sqrt(8/3), math.sqrt(1.5))
