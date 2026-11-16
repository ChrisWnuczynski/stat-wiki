"""Recompute sample correlations, inference example, and preserved cohort values."""

import csv
import json
import math
from pathlib import Path

from scipy.stats import t

root = Path(__file__).resolve().parents[1]
page = (root / "articles/sample-correlation-coefficient.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/sample-correlation-coefficient.json").read_text())


def sums(pairs):
    xs, ys = zip(*pairs)
    xbar, ybar = sum(xs) / len(xs), sum(ys) / len(ys)
    xx = sum((x - xbar) ** 2 for x in xs)
    yy = sum((y - ybar) ** 2 for y in ys)
    xy = sum((x - xbar) * (y - ybar) for x, y in pairs)
    return xbar, ybar, xx, yy, xy


def correlation(pairs):
    _, _, xx, yy, xy = sums(pairs)
    return xy / math.sqrt(xx * yy)


pairs = [(1, 1), (2, 2), (3, 4), (4, 3)]
assert sums(pairs) == (2.5, 2.5, 5.0, 5.0, 4.0)
assert math.isclose(correlation(pairs), 0.8)
assert math.isclose(correlation([(x, 10 - 2 * y) for x, y in pairs]), -0.8)
assert math.isclose(0.8**2, 0.64)
outlier = pairs + [(10, -10)]
assert sums(outlier) == (4, 0, 50, 130, -71)
assert correlation(outlier) < 0
curved = [(x, x * x) for x in (-2, -1, 0, 1, 2)]
assert sums(curved) == (0, 2, 10, 14, 0)
assert correlation(curved) == 0
assert sums([(3, 1), (3, 2), (3, 3), (3, 4)])[2] == 0

with (root / "sources/stat1301/data/heart.csv").open(newline="") as file:
    cohort = list(csv.DictReader(file))
assert len(cohort) == 299
creatinine = [float(row["serum_creatinine"]) for row in cohort]
log_creatinine = [math.log10(value) for value in creatinine]
for column, reported in (("serum_sodium", -0.26), ("age", 0.23)):
    actual = correlation(list(zip(log_creatinine, [float(row[column]) for row in cohort])))
    assert round(actual, 2) == reported


def moment_skew(values):
    mean = sum(values) / len(values)
    second = sum((v - mean) ** 2 for v in values) / len(values)
    third = sum((v - mean) ** 3 for v in values) / len(values)
    return third / second ** 1.5


assert round(moment_skew(creatinine), 1) == 4.4
assert round(moment_skew(log_creatinine), 1) == 1.6
assert math.isclose(0.25**2, 0.0625)
assert 0.23**2 < 0.06 < 0.26**2

sample_r, n = 0.438, 20
test_stat = sample_r * math.sqrt(n - 2) / math.sqrt(1 - sample_r**2)
assert abs(test_stat - 2.06) < 0.01  # displayed r and test were rounded separately
assert abs(2 * t.sf(abs(test_stat), n - 2) - 0.054) < 0.001
assert round(t.ppf(0.975, n - 2), 3) == 2.101
assert (2 * t.sf(abs(test_stat), n - 2)) > 0.05
assert 13**2 == 169
assert 0.5**2 == 0.25

for printed in ("2.5", "$S_{xx}=S_{yy}=5$", "$S_{xy}=4$", "0.8", "0.64", "-0.8", "$(10,-10)$", "$S_{xx}=0$", "1888", "2.06", "2.101", "0.054", "43.98", "3.92", "157.2", "0.285", "0.438", "-0.26", "0.23", "4.4", "1.6", "299"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert page.count("![") >= json.loads((root / "research/baseline.json").read_text())["sample-correlation-coefficient"]["figures"]
for key in ("pearson1896", "student1908_corr", "casella_berger2002", "nist_correlation2013", "strimmer2025_mva", "hannay2019_statsdata", "dodge2008"):
    assert f'data-cite-key="{key}"' in body, key
assert pending["self_checks"] == ["ex-inf-correlation-t", "ex-da-correlation-reading", "ex-sl-02-7"]
for slug in pending["self_checks"]:
    assert "## Worked answer" in (root / "questions" / f"{slug}.qmd").read_text()
    assert f"{slug}.qmd" in page
print("sample correlation arithmetic, original cohort and preservation passed")
