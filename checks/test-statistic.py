"""Check the test-statistic page."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/test-statistic.md").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5 and len(set(keys)) >= 2
assert "**Your turn.**" in prose
assert 8*7*6*5*4*3*2*1 // (7*6*5*4*3*2*1) == 8  # C(8,7)
assert (8+1)/256 == 9/256
assert 1/256 == 1/256
