"""Check the numeric precision examples and the researched article structure."""

from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / "articles/precision.qmd").read_text().split("## See also", 1)[0]

prior = Fraction(1, 4)
data = Fraction(4, 9)
post = prior + data
assert post == Fraction(25, 36)
assert 1 / post == Fraction(36, 25)
mean = (prior * 10 + data * 12) / post
assert mean == Fraction(282, 25)
assert prior / post == Fraction(9, 25)
assert data / post == Fraction(16, 25)

prior_turn = Fraction(1, 16)
data_turn = Fraction(3, 12)
post_turn = prior_turn + data_turn
assert post_turn == Fraction(5, 16)
assert 1 / post_turn == Fraction(16, 5)
assert (prior_turn * 20 + data_turn * 24) / post_turn == Fraction(116, 5)

for printed in ("0.25", "0.4444", "25/36", "0.6944", "36/25", "1.44",
                "282", "11.28", "9/25", "36\\%", "16/25", "64\\%",
                "20", "16", "24", "12", "5/16", "3.2", "116/5", "23.2"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert 'data-cite-key="gelman_bda2013"' in body
print("precision calculations and practice passed")
