"""Arithmetic checks for the structure function article."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/structure-function.md").read_text()
body = (root / "articles/structure-function.qmd").read_text().split("## See also", 1)[0]

def r(p):
    return 3 * p ** 2 * (1 - p) + p ** 3

assert abs(r(0.9) - 0.972) < 1e-12
assert abs(3 * 0.81 * 0.1 - 0.243) < 1e-12
assert abs(0.9 ** 3 - 0.729) < 1e-12
assert abs(r(0.8) - 0.896) < 1e-12
assert abs(3 * 0.64 * 0.2 - 0.384) < 1e-12
assert abs(0.8 ** 3 - 0.512) < 1e-12
assert abs(0.9 * 0.8 - 0.72) < 1e-12

def phi(x):
    x1, x2, x3 = x
    return x1 * x2 + x1 * x3 + x2 * x3 - 2 * x1 * x2 * x3

assert phi((1, 1, 0)) == 1 and phi((1, 0, 0)) == 0 and phi((1, 1, 1)) == 1
for printed in ("0.972", "0.243", "0.729", "0.896", "0.384", "0.512", "0.72"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("structure function checks passed")
