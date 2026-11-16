"""Check Dirichlet updates, moments, figures and printed example numbers."""

from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/dirichlet-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

prior, counts = (2, 3, 5), (4, 1, 0)
post = tuple(a + x for a, x in zip(prior, counts))
assert post == (6, 4, 5)
assert sum(prior) == 10 and sum(post) == 15
assert F(prior[0], sum(prior)) == F(1, 5)
assert F(post[0], sum(post)) == F(2, 5)

ad_counts = (53, 57, 147, 93, 38, 113)
assert sum(ad_counts) == 501
ad_post = tuple(x + 1 for x in ad_counts)
assert ad_post == (54, 58, 148, 94, 39, 114)
assert sum(ad_post) == 507
assert round(float(F(54, 507)), 4) == .1065
assert round(float(F(53, 501)), 4) == .1058

exam_counts = (8, 6, 16, 12, 4, 14)
assert sum(exam_counts) == 60
exam_post = tuple(x + 1 for x in exam_counts)
assert exam_post == (9, 7, 17, 13, 5, 15)
assert sum(exam_post) == 66
assert round(float(F(17, 66)), 4) == .2576
assert round(float(F(16, 60)), 4) == .2667

restaurant_counts = (63, 19, 3, 38)
assert sum(restaurant_counts) == 123
assert sum((45.79, 28.60, 8.36, 21.25)) == 104
assert sum((108.79, 47.60, 11.36, 59.25)) == 227

worked_prior, worked_counts = (1, 1, 1), (2, 3, 1)
worked_post = tuple(a + x for a, x in zip(worked_prior, worked_counts))
assert worked_post == (3, 4, 2) and sum(worked_post) == 9
assert F(worked_post[1], 9) == F(4, 9)
assert round(float(F(4, 9)), 6) == .444444
assert F(4 * 5, 9**2 * 10) == F(2, 81)
assert round(float(F(2, 81)), 6) == .024691
assert -F(3 * 4, 9**2 * 10) == -F(2, 135)
assert round(float(-F(2, 135)), 6) == -.014815

turn_prior, turn_counts = (1, 2, 1), (3, 0, 1)
turn_post = tuple(a + x for a, x in zip(turn_prior, turn_counts))
assert turn_post == (4, 2, 2) and sum(turn_post) == 8
assert tuple(F(a, 8) for a in turn_post) == (F(1, 2), F(1, 4), F(1, 4))
assert F(turn_post[0] + turn_post[2], 8) == F(3, 4)
assert F(4 * 4, 8**2 * 9) == F(1, 36)
assert round(float(F(1, 36)), 6) == .027778

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "0.444444", "0.024691",
    "-0.014815", "0.027778", "54/507", "53/501",
    "## Common misconceptions", "#assumptions-and-limits",
):
    assert fragment in body, f"Missing section or calculation: {fragment}"
assert body.count('title="Proof"') == 1
assert page.count("![") >= 3, "Lost Dirichlet plots or simplex diagrams"
assert "α=(2,3,4)" in page and "../figures/part1-fig-05-dirichlet-simplex.png" in page
for qid in ("q-22", "ex-applied-restaurant", "exr-beta-hidden-inside-dirichlet", "exr-make-the-simplex-integral-equal-one"):
    assert f"../questions/{qid}.qmd" in page
print("dirichlet updates, moments and baseline figures passed")
