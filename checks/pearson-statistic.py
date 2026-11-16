"""Arithmetic printed in the Pearson statistic article and its linked checks."""
import math
from pathlib import Path

from scipy.stats import chi2


def pearson(observed, expected):
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "pearson-statistic.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    expected = [93 / 4, 93 / 2, 93 / 4]
    contributions = [(o - e) ** 2 / e for o, e in zip([23, 50, 20], expected)]
    assert expected == [23.25, 46.5, 23.25]
    assert all(math.isclose(x, y, abs_tol=0.0005) for x, y in zip(contributions, [0.003, 0.263, 0.454]))
    chicken = sum(contributions)
    assert math.isclose(chicken, 0.72043, abs_tol=0.000005)
    assert math.isclose(chicken, 0.72, abs_tol=0.005)
    assert math.isclose(chi2.ppf(0.95, 2), 5.991, abs_tol=0.0005)
    assert math.isclose(chi2.sf(chicken, 2), 0.698, abs_tol=0.0005)
    assert math.isclose(chi2.sf(chicken, 2), 0.70, abs_tol=0.005)

    die = pearson([14, 22, 16, 25, 19, 24], [20] * 6)
    assert die == 4.9
    assert sum([36, 4, 16, 25, 1, 16]) == 98
    assert math.isclose(chi2.ppf(0.95, 5), 11.07, abs_tol=0.005)
    assert math.isclose(chi2.sf(die, 5), 0.43, abs_tol=0.005)

    assert pearson([7, 13, 8, 12], [10] * 4) == 2.6
    assert 8 - 1 - 1 == 6
    assert (4 - 1) * (5 - 1) == 12
    assert 10 - 1 - 2 == 7
    assert 10 - 1 == 9

    # Linked bank questions are answered and have distinct worked content.
    expansion = 2 * 24 * math.log(24 / 20)
    assert math.isclose(expansion, 8.751, abs_tol=0.0005)
    assert math.isclose(8.8 - expansion, 0.049, abs_tol=0.0005)
    row, col, n = [70, 100], [90, 80], 170
    fitted = [[r * c / n for c in col] for r in row]
    two_by_two = pearson([40, 30, 50, 50], sum(fitted, []))
    assert math.isclose(two_by_two, 0.843, abs_tol=0.0005)
    assert math.isclose(math.sqrt(two_by_two), 0.918, abs_tol=0.0005)


if __name__ == "__main__":
    test_printed_values()
