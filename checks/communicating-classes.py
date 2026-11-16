"""Arithmetic for the communicating-classes depth pass."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/communicating-classes.md").read_text(encoding="utf-8")
page = root / "articles/communicating-classes.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

P = [[0, 1], [1, 0]]
P2 = [[sum(P[i][k] * P[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert P2 == [[1, 0], [0, 1]]
pi = [1 / 2, 1 / 2]
piP = [sum(pi[i] * P[i][j] for i in range(2)) for j in range(2)]
assert piP == [1 / 2, 1 / 2]

A = [[0, 1 / 3, 2 / 3], [0, 0, 1], [1, 0, 0]]
# path a->c->a
assert abs((2 / 3) * 1 - 2 / 3) < 1e-12
# path a->b->c->a
assert abs((1 / 3) * 1 * 1 - 1 / 3) < 1e-12
import math
assert math.gcd(2, 3) == 1

for printed in ("2/3", "1/3", "1/2"):
    assert printed in prose, printed
    assert printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
for key in ("siegrist2022_markov_recurrence", "siegrist2022_markov_period"):
    assert f"{{{{cite:{key}}}}}" in prose
print("communicating-classes arithmetic passed")
