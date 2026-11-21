"""Arithmetic checks for the Voronoi tessellation article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
import math

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/voronoi-tessellation.md").read_text()
text = shown(text, "voronoi-tessellation")
body = (root / "articles/voronoi-tessellation.qmd").read_text().split("## See also", 1)[0]

def dist(p, c):
    return math.hypot(p[0] - c[0], p[1] - c[1])

assert round(dist((2, 1), (0, 0)), 3) == 2.236
assert round(dist((2, 1), (6, 2)), 3) == 4.123
assert dist((4, 0), (0, 0)) == 4
assert round(dist((4, 0), (6, 2)), 3) == 2.828
assert abs(dist((3, 1), (0, 0)) - math.sqrt(10)) < 1e-12
assert abs(dist((1, 5), (0, 0)) ** 2 - 26) < 1e-12
assert abs(dist((1, 5), (4, 0)) ** 2 - 34) < 1e-12
assert 3 * 2 + 1 == 7 and 3 * 6 + 2 == 20 and 3 * 4 + 0 == 12
for printed in ("2.236", "4.123", "2.828", "3x+y=10", "$4$", r"\sqrt{8}", r"\sqrt{26}", r"\sqrt{34}", r"\sqrt{10}"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("voronoi tessellation checks passed")
