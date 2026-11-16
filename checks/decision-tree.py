"""Verify printed numerical claims in the decision-tree depth section."""
from fractions import Fraction as F
from pathlib import Path


body = Path("articles/decision-tree.qmd").read_text().split("## See also", 1)[0]
for token in ("0.46875", "0.20833", "0.26042", "0.44444", "0.17778",
              "30/64", "5/18", "5/24", "4/9", "8/25", "4/15", "8/45",
              'title="Proof"', 'title="Answer"'):
    assert token in body, token
assert body.count('title="Proof"') == 1

root = 2 * F(3, 8) * F(5, 8)
assert root == F(30, 64) == F(46875, 100000)
assert 2 * F(1, 6) * F(5, 6) == F(5, 18)
weighted = F(6, 8) * F(5, 18)
assert weighted == F(5, 24) and round(float(weighted), 5) == .20833
assert root - weighted == F(25, 96) and round(float(root-weighted), 5) == .26042
practice = 2 * F(2, 6) * F(4, 6)
assert practice == F(4, 9) and round(float(practice), 5) == .44444
assert 2 * F(1, 5) * F(4, 5) == F(8, 25)
assert F(5, 6) * F(8, 25) == F(4, 15)
assert practice - F(4, 15) == F(8, 45)
assert round(float(F(8, 45)), 5) == .17778
print("decision-tree impurity arithmetic and structure passed")
