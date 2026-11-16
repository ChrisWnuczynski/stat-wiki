"""Arithmetic checks for the Hastings correction article."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/hastings-correction.md").read_text()
body = (root / "articles/hastings-correction.qmd").read_text().split("## See also", 1)[0]

def ratio(p_star, p, j_back, j_fwd):
    return (p_star * j_back) / (p * j_fwd)

r = ratio(0.5, 0.2, 0.1, 0.4)
assert abs(r - 0.625) < 1e-12
assert abs(0.5 / 0.2 - 2.5) < 1e-12
assert abs(ratio(0.5, 0.2, 0.4, 0.1) - 10) < 1e-12
assert min(2.5, 1) == 1 and min(0.625, 1) == 0.625
for printed in ("0.625", "2.5", "0.375", "=10", "0.4", "0.1", "0.2", "0.5"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("hastings correction checks passed")
