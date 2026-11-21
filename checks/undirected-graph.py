"""Arithmetic for the undirected-graph depth pass."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/undirected-graph.md").read_text(encoding="utf-8")
prose = shown(prose, "undirected-graph")
page = root / "articles/undirected-graph.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

K = [
    [1, -0.5, 0],
    [-0.5, 1, -0.5],
    [0, -0.5, 1],
]
det2 = K[0][0] * K[1][1] - K[0][1] * K[1][0]
assert abs(det2 - 0.75) < 1e-12
# cofactor expansion
det = (
    K[0][0] * (K[1][1] * K[2][2] - K[1][2] * K[2][1])
    - K[0][1] * (K[1][0] * K[2][2] - K[1][2] * K[2][0])
    + K[0][2] * (K[1][0] * K[2][1] - K[1][1] * K[2][0])
)
assert abs(det - 0.5) < 1e-12
# inverse (1,3) via adjugate / det: cofactor C13 = det of minor removing row0 col2, sign (-1)^{1+3}=+
minor = K[1][0] * K[2][1] - K[1][1] * K[2][0]
# indices: remove row 0, col 2: [[-0.5, 1], [0, -0.5]]
minor = (-0.5) * (-0.5) - 1 * 0
assert abs(minor - 0.25) < 1e-12
sigma13 = minor / det
assert abs(sigma13 - 0.5) < 1e-12
for printed in ("1/2", "3/4"):
    assert printed in prose and printed in body
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
print("undirected-graph arithmetic passed")
