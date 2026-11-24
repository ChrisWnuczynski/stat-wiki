"""Arithmetic checks for the multiple-testing article."""

import sys
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

root = Path(__file__).resolve().parents[1]
raw = (root / "research/content/multiple-testing.md").read_text()
text = shown(raw, "multiple-testing")
body = (root / "articles/multiple-testing.qmd").read_text().split("## See also", 1)[0]


def bh_false_proportion(p_values, true_null, level=Fraction(4, 100)):
    """False-discovery proportion of Benjamini–Hochberg at a rational level."""
    indexed = sorted(enumerate(p_values), key=lambda item: (item[1], item[0]))
    m = len(indexed)
    k = 0
    for rank, (_, p_value) in enumerate(indexed, start=1):
        if p_value * m <= level * rank:
            k = rank
    if k == 0:
        return Fraction(0)
    cutoff = indexed[k - 1][1]
    rejected = [i for i, p_value in enumerate(p_values) if p_value <= cutoff]
    false = sum(1 for i in rejected if true_null[i])
    return Fraction(false, len(rejected))


def _uniform_corner(i, low, high):
    """One point of the rectangle for true null i, with the other two above 0.04."""
    values = [Fraction(1, 2), Fraction(3, 5), Fraction(4, 5)]
    values[i] = (low + high) / 2
    return values


# Three independent uniform true-null p-values, and a false-null p-value that
# is 0 exactly when one true-null p-value lies in (0.01, 0.02] and the other
# two exceed 0.04. The six rectangles below are disjoint and contribute
# 0.041472 to the false discovery rate at level 0.04.
weight = Fraction(1, 100) * Fraction(96, 100) * Fraction(96, 100)
assert weight == Fraction(9216, 1_000_000)
bound = 3 * weight + 3 * weight / 2
assert bound == Fraction(41472, 1_000_000) == Fraction(648, 15625)
assert f"{float(bound):.6f}" == "0.041472"
assert bound > Fraction(4, 100)
for i in range(3):
    interior_f = _uniform_corner(i, Fraction(0), Fraction(1, 100))
    edge_f = _uniform_corner(i, Fraction(1, 100), Fraction(1, 100))
    interior_a = _uniform_corner(i, Fraction(1, 100), Fraction(2, 100))
    edge_a = _uniform_corner(i, Fraction(2, 100), Fraction(2, 100))
    assert bh_false_proportion(interior_f + [Fraction(1)], [True, True, True, False]) == 1
    assert bh_false_proportion(edge_f + [Fraction(1)], [True, True, True, False]) == 1
    assert bh_false_proportion(interior_a + [Fraction(0)], [True, True, True, False]) == Fraction(1, 2)
    assert bh_false_proportion(edge_a + [Fraction(0)], [True, True, True, False]) == Fraction(1, 2)
    assert interior_f[i] <= edge_f[i] == Fraction(1, 100)
    assert Fraction(1, 100) < interior_a[i] < edge_a[i] == Fraction(2, 100)
assert round(1 - 0.95 ** 20, 4) == 0.6415
assert round(0.95 ** 5, 5) == 0.77378
assert round(1 - 0.95 ** 5, 5) == 0.22622
ps = [0.004, 0.018, 0.040, 0.200]
thr = [0.10 * k / 4 for k in range(1, 5)]
assert [round(t, 3) for t in thr] == [0.025, 0.050, 0.075, 0.100]
k = max((i for i, (p, t) in enumerate(zip(ps, thr), 1) if p <= t), default=0)
assert k == 3
assert abs(0.10 / 4 - 0.025) < 1e-12
assert abs(0.05 / 20 - 0.0025) < 1e-12
for printed in ("0.6415", "0.77378", "0.22622", "0.004", "0.018", "0.040",
                "0.200", "0.025", "0.050", "0.075", "0.100", "0.0025"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
for required in ("independent of all the other", "0.009216", "0.041472",
                 "false-null $p$-values"):
    assert required in raw, required
    assert required in body, required
assert "When the test statistics of the true nulls are independent" not in raw
assert "When the test statistics of the true nulls are independent" not in body
print("multiple testing checks passed")
