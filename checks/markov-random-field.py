"""Arithmetic checks for the Markov random field article."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/markov-random-field.md").read_text()
body = (root / "articles/markov-random-field.qmd").read_text().split("## See also", 1)[0]
assert abs(0.8 * 0.8 - 0.64) < 1e-12
joint = 0.5 * 0.64 + 0.5 * 0.04
assert abs(joint - 0.34) < 1e-12
assert abs(0.5 * 0.8 + 0.5 * 0.2 - 0.5) < 1e-12
assert abs(0.5 * 0.5 - 0.25) < 1e-12
assert abs(0.2 * 0.2 - 0.04) < 1e-12
assert abs(0.5 * 0.16 + 0.5 * 0.16 - 0.16) < 1e-12
for printed in ("0.64", "0.34", "0.25", "0.32", "0.02", "0.04", "0.16"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("markov random field checks passed")
