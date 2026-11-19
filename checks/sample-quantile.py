"""Quantile conventions and all values printed on the sample-quantile page."""
import csv
import math
from pathlib import Path

import numpy as np
from scipy.stats import norm


ROOT = Path(__file__).resolve().parents[1]


def empirical_inverse(data, p):
    ordered = sorted(data)
    return ordered[math.ceil(len(ordered) * p) - 1]


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "sample-quantile.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    sample = [2, 4, 8, 10]
    assert empirical_inverse(sample, 0.25) == 2
    assert empirical_inverse(sample, 0.5) == 4
    assert math.isclose(np.quantile(sample, 0.25), 3.5)
    assert math.isclose(np.quantile(sample, 0.5), 6)
    assert 1 + 3 * 0.25 == 1.75
    assert 1 + 3 * 0.5 == 2.5

    turn = [2, 4, 8, 10, 14]
    assert 1 + 4 * 0.25 == 2
    assert 1 + 4 * 0.75 == 4
    assert list(np.quantile(turn, [0.25, 0.75])) == [4, 10]
    assert 10 - 4 == 6

    with (ROOT / "sources/stat1301/data/heart.csv").open() as source:
        ages = np.array([float(row["age"]) for row in csv.DictReader(source)])
    assert len(ages) == 299
    assert math.isclose(ages.mean(), 60.83, abs_tol=0.005)
    assert np.median(ages) == 60
    assert list(np.quantile(ages, [0.25, 0.75])) == [51, 70]
    assert np.ptp(ages) == 55 and ages.min() == 40 and ages.max() == 95
    assert 70 - 51 == 19
    assert math.isclose(ages.std(ddof=1), 11.89, abs_tol=0.005)
    assert math.isclose(19 / 11.9, 1.6, abs_tol=0.005)
    assert math.isclose(norm.ppf(0.75) - norm.ppf(0.25), 1.35, abs_tol=0.005)

    assert np.quantile([1, 3], 0.5) == 2
    assert np.quantile([1, 9], 0.5) == 5
    assert 2 ** 2 == 4
    assert empirical_inverse([1, 3, 5, 9, 12], 0.6) == 5
    assert 1 + 4 * 0.6 == 3.4
    assert math.isclose(np.quantile([1, 3, 5, 9, 12], 0.6), 6.6)
    assert empirical_inverse([2, 2, 2, 9], 0.75) == 2
    assert 1 + 3 * 0.75 == 3.25
    assert math.isclose(np.quantile([2, 2, 2, 9], 0.75), 3.75)

    milk = sorted([1.035, 1.019, 1.068, 1.084, 1.077, 0.998,
                   1.041, 1.037, 1.051, 1.102])
    assert milk[2] == 1.035 and milk[7] == 1.077
    assert np.allclose(np.quantile(milk, [0.25, 0.75]), [1.0355, 1.07475])


if __name__ == "__main__":
    test_printed_values()
