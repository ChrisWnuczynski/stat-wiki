"""Check three-point SVM KKT values and the retained margin cases."""

from math import isclose, sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/support-vectors-and-their-multipliers.qmd").read_text()
body = page.split("## See also", 1)[0]

points = [((0, 0), -1), ((2, 0), 1), ((3, 2), 1)]
w = (1, 0)
b = -1
alphas = (.5, .5, 0)
score = lambda x: sum(a * z for a, z in zip(w, x)) + b
assert [y * score(x) for x, y in points] == [1, 1, 2]
assert isclose(sum(a * y for a, (_, y) in zip(alphas, points)), 0)
assert all(isclose(sum(a * y * x[j] for a, (x, y) in zip(alphas, points)), w[j]) for j in (0, 1))
assert isclose(2 / sqrt(sum(v*v for v in w)), 2)

changed = [((0, 0), -1), ((1.5, 0), 1), ((3, 2), 1)]
w2 = (4 / 3, 0)
b2 = -1
alpha2 = (8 / 9, 8 / 9, 0)
score2 = lambda x: sum(a * z for a, z in zip(w2, x)) + b2
assert [round(y * score2(x), 10) for x, y in changed] == [1, 1, 3]
assert isclose(sum(a * y for a, (_, y) in zip(alpha2, changed)), 0)
assert all(isclose(sum(a * y * x[j] for a, (x, y) in zip(alpha2, changed)), w2[j]) for j in (0, 1))
assert isclose(2 / sqrt(sum(v*v for v in w2)), 1.5)

C = 2
assert 0 < 1.3 < C and C == 2
assert all(v >= 0 for v in (0, 1.3, C))
for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "## Common misconceptions",
    "0.03", "1", "100", "8/9", "1.5", "## Assumptions and limits",
):
    assert fragment in body, f"Missing retained or added calculation: {fragment}"
assert body.count('title="Proof"') == 1
for qid in ("ex-sl-17-2", "ex-sl-17-3", "ex-sl-17-6", "ex-sl-17-8", "ex-sl-17-9"):
    assert f"../questions/{qid}.qmd" in page
print("support-vector multipliers and KKT calculations passed")
