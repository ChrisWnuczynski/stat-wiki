"""Arithmetic checks for the polynomial kernel article."""
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/polynomial-kernel.md").read_text()
body = (root / "articles/polynomial-kernel.qmd").read_text().split("## See also", 1)[0]

def K(x, xp):
    return (1 + sum(a * b for a, b in zip(x, xp))) ** 2

assert K((1, 2), (3, 0)) == 16
h = (1, math.sqrt(2), 2 * math.sqrt(2), 1, 4, 2 * math.sqrt(2))
hp = (1, 3 * math.sqrt(2), 0, 9, 0, 0)
assert abs(sum(a * b for a, b in zip(h, hp)) - 16) < 1e-12
assert K((1, 0), (0, 1)) == 1
assert (1 * 0 + 0 * 1) ** 2 == 0
assert K((1, 1), (1, 1)) == 9
assert math.comb(4, 2) == 6
assert math.comb(5, 2) == 10
for printed in ("16", "6", "10", "9", "$(1+0)^2=1$"):
    assert printed in text or (printed == "$(1+0)^2=1$" and "(1+0)^2=1" in text)
    assert printed in body or (printed == "$(1+0)^2=1$" and "(1+0)^2=1" in body)
assert "**Your turn.**" in body and 'title="Proof"' in body
print("polynomial kernel checks passed")
