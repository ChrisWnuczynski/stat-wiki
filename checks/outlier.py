"""Recompute the numerical examples and bound on the outlier page."""

from pathlib import Path
from math import isclose, sqrt
from statistics import mean, median, stdev

root = Path(__file__).resolve().parents[1]
page = (root / "articles/outlier.qmd").read_text()
body = page.split("## See also", 1)[0]

sample = [2, 3, 3, 4, 5, 6, 7, 8, 20]
assert sum(sample) == 58 and len(sample) == 9
assert median(sample) == 5
assert isclose(mean(sample), 58 / 9)
assert round(mean(sample), 2) == 6.44
assert sum(sample[:-1]) == 38 and mean(sample[:-1]) == 4.75
assert round(mean(sample) - mean(sample[:-1]), 2) == 1.69
q1, q3 = 3, 7
iqr = q3 - q1
assert iqr == 4 and (q1 - 1.5 * iqr, q3 + 1.5 * iqr) == (-3, 13)
assert [x for x in sample if x < -3 or x > 13] == [20]

small = [0, 0, 0, 0, 10]
assert mean(small) == 2 and isclose(stdev(small), sqrt(20))
assert round(stdev(small), 3) == 4.472
z = (10 - mean(small)) / stdev(small)
assert isclose(z, 4 / sqrt(5)) and round(z, 3) == 1.789
assert round(z, 2) == 1.79
scaled = [0, 0, 0, 0, 1000]
assert isclose((1000 - mean(scaled)) / stdev(scaled), z)

practice = [1, 2, 2, 3, 4, 5, 6, 7, 18]
assert median(practice) == 4
assert (practice[2], practice[6]) == (2, 6)
assert practice[6] - practice[2] == 4
assert (2 - 1.5 * 4, 6 + 1.5 * 4) == (-4, 12)
assert [x for x in practice if x < -4 or x > 12] == [18]

new_bank = [1, 2, 3, 3, 4, 5, 6, 7, 16]
assert median(new_bank) == 4
assert (new_bank[2], new_bank[6]) == (3, 6)
assert new_bank[6] - new_bank[2] == 3
assert (3 - 1.5 * 3, 6 + 1.5 * 3) == (-1.5, 10.5)
assert [x for x in new_bank if x < -1.5 or x > 10.5] == [16]
new_z = [0, 0, 0, 24]
assert mean(new_z) == 6 and stdev(new_z) == 12
assert sum((x - 6) ** 2 for x in new_z) == 432
assert (24 - 6) / 12 == 1.5 and 3 / sqrt(4) == 1.5

for printed in (
    "2,3,3,4,5,6,7,8,20", "58/9", "6.44", "38/8", "4.75", "1.69",
    "Q_1=3", "Q_3=7", "IQR=4", "=-3", "=13", "1.789", "4.472",
    "1,2,2,3,4,5,6,7,18", "Q_1=2", "Q_3=6", "=-4", "=12",
    "1.5IQR", "3IQR", "n-1", "\\sqrt n", "1000",
):
    assert printed in body, f"Missing displayed value: {printed}"
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("dodge2008", "nist_handbook2002"):
    assert f'data-cite-key="{key}"' in body
print("outlier numerical examples, proof and citations passed")
