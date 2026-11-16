"""Arithmetic checks for the mini-batch article."""
from itertools import combinations
from pathlib import Path

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/mini-batch.md").read_text()
body = (root / "articles/mini-batch.qmd").read_text().split("## See also", 1)[0]
y = (1, 3, 5, 7)
full = -sum(y) / 4
assert full == -4
assert -(1 + 5) / 2 == -3
assert -(3 + 7) / 2 == -5
grads = [-(a + b) / 2 for a, b in combinations(y, 2)]
assert grads == [-2, -3, -4, -4, -5, -6]
assert abs(sum(grads) / 6 + 4) < 1e-12
assert abs(-(1 + 3 + 7) / 3 + 11 / 3) < 1e-12
assert round(-11 / 3, 5) == -3.66667
for printed in ("-4", "-3", "-5", "-2", "-6", "-24/6", "-11/3", "-3.66667", "-7"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("mini-batch checks passed")
