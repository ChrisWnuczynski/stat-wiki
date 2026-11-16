"""Printed values for the stochastic gradient descent article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "stochastic-gradient-descent.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

grads = [3 - x for x in (2, 4, 6)]
assert grads == [1, -1, -3]
assert sum(grads) == -3
assert sum(grads) / 3 == -1
assert 3 - 0.5 * (-3) == 4.5
assert 3 - 0.5 * (-1) == 3.5

grads2 = [2 - x for x in (2, 4, 6)]
assert grads2 == [0, -2, -4]
assert sum(grads2) == -6
assert 2 - 0.2 * (-2) == 2.4
assert 2 - 0.2 * (-6) == 3.2

for printed in ("1", "-1", "-3", "4.5", "3.5", "2.4", "3.2", "0.5", "0.2", "1/r"):
    assert printed in body, printed
assert "1/r" in body
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("stochastic gradient descent checks passed")
