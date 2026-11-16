"""Check new ANOVA arithmetic and retained corn/cold-sore calculations."""

from math import isclose, sqrt
from pathlib import Path

from scipy.stats import f

root = Path(__file__).resolve().parents[1]
page = (root / "articles/one-way-analysis-of-variance.qmd").read_text()
body = page.split("## See also", 1)[0]


def table(groups):
    n = sum(map(len, groups))
    k = len(groups)
    grand = sum(map(sum, groups)) / n
    means = [sum(x) / len(x) for x in groups]
    between = sum(len(x) * (m - grand) ** 2 for x, m in zip(groups, means))
    within = sum(sum((y - m) ** 2 for y in x) for x, m in zip(groups, means))
    F = (between / (k - 1)) / (within / (n - k))
    return n, k, grand, means, between, within, F


worked = table([[7, 8, 9], [8, 9, 10], [11, 12, 13]])
assert worked[:2] == (9, 3)
assert isclose(worked[2], 29 / 3)
assert worked[3] == [8, 9, 12]
assert isclose(worked[4], 26) and isclose(worked[5], 6)
assert isclose(worked[4] + worked[5], 32)
assert isclose(worked[6], 13)
assert isclose(f.sf(13, 2, 6), 27 / 4096)
assert round(f.sf(13, 2, 6), 6) == .006592

turn = table([[4, 5, 6], [6, 7, 8]])
assert turn[3] == [5, 7]
assert isclose(turn[4], 6) and isclose(turn[5], 4)
assert isclose(turn[6], 6)
assert round(-sqrt(6), 6) == -2.449490

corn = table([
    [46.2, 51.9, 48.7], [49.2, 58.6, 57.4], [60.3, 58.7, 60.4],
    [48.9, 51.4, 44.6], [52.5, 54.0, 49.3],
])
assert (corn[0], corn[1]) == (15, 5)
assert round(corn[2], 2) == 52.81
assert [round(x, 2) for x in corn[3]] == [48.93, 55.07, 59.80, 48.30, 51.93]
assert round(corn[4], 1) == 270.3 and round(corn[5], 1) == 105.7
assert round(corn[4] + corn[5], 1) == 375.9
assert round(corn[6], 2) == 6.39 and round(f.sf(corn[6], 4, 10), 3) == .008
assert round(sqrt(corn[5] / 10), 2) == 3.25

cold = table([
    [5, 8, 7, 7, 10, 8], [4, 6, 6, 3, 5, 6], [6, 4, 4, 5, 4, 3],
    [7, 4, 6, 6, 3, 5], [9, 3, 5, 7, 7, 6],
])
assert (cold[0], cold[1]) == (30, 5)
assert [round(x, 3) for x in cold[3]] == [7.5, 5, 4.333, 5.167, 6.167]
assert round(cold[4], 3) == 36.467 and round(cold[5], 3) == 58.5
assert round(cold[6], 3) == 3.896
assert round(f.sf(cold[6], 4, 25), 5) == .01359

assert isclose((67.475 / 3) / (935.5 / 36), .86557, rel_tol=.001)
assert round(f.sf((67.475 / 3) / (935.5 / 36), 3, 36), 2) == .47

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "27/4096", "0.006592",
    "-2.449490", "## Common misconceptions", "#assumptions-and-limits",
):
    assert fragment in body, f"Missing section or calculation: {fragment}"
assert body.count('title="Proof"') == 1
assert page.count("![") >= 6
for qid in ("ex-inf-anova-two-groups", "ex-da-sickle-anova", "ex-da-bonferroni", "ex-da-isotopia-wages"):
    assert f"../questions/{qid}.qmd" in page
print("one-way ANOVA worked and inherited tables passed")
