"""Recalculate every numeric example and table on the least-squares page."""
import math

import numpy as np


def fit(x, y, power=1, transform=False):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if transform:
        y = np.log(y)
    design = np.column_stack([x ** j for j in range(power + 1)])
    return np.linalg.lstsq(design, y, rcond=None)[0]


def test_printed_values():
    spending = [1.2, 0.8, 1.0, 1.3, 0.7, 0.8, 1.0, 0.6, 0.9, 1.1]
    sales = [101, 92, 110, 120, 90, 82, 93, 75, 91, 105]
    x, y = np.array(spending), np.array(sales)
    assert len(x) == 10 and len(y) == 10
    assert math.isclose(x.mean(), 0.94, abs_tol=1e-12)
    assert math.isclose(y.mean(), 95.9, abs_tol=1e-12)
    assert math.isclose(((x - x.mean()) ** 2).sum(), 0.444, abs_tol=1e-12)
    assert math.isclose(((x - x.mean()) * (y - y.mean())).sum(), 23.34, abs_tol=1e-12)
    b0, b1 = fit(x, y)
    assert math.isclose(b1, 52.6, abs_tol=0.05)
    assert math.isclose(b0, 46.5, abs_tol=0.05)
    assert math.isclose(b1 * 10_000, 526_000, abs_tol=500)

    latitude = [32.8, 33.9, 34.1, 37.9, 40.0, 40.8, 41.7, 42.2, 45.0]
    rate = [9.0, 5.9, 6.6, 5.8, 5.5, 3.0, 3.4, 3.1, 3.8]
    assert len(latitude) == len(rate) == 9
    straight = fit(latitude, rate)
    curved = fit(latitude, rate, power=2)
    logged = fit(latitude, rate, transform=True)
    for found, shown, tol in zip(straight, [20.6, -0.399], [0.05, 0.0005]):
        assert math.isclose(found, shown, abs_tol=tol)
    for found, shown, tol in zip(curved, [66.4, -2.81, 0.0314], [0.05, 0.005, 0.00005]):
        assert math.isclose(found, shown, abs_tol=tol)
    for found, shown, tol in zip(logged, [4.51, -0.0761], [0.005, 0.00005]):
        assert math.isclose(found, shown, abs_tol=tol)
    assert math.isclose(math.exp(-0.0761), 0.93, abs_tol=0.005)
    assert math.isclose(100 * (1 - math.exp(-0.0761)), 7, abs_tol=0.5)

    b0, b1 = fit([1, 2, 3], [2, 3, 5])
    assert math.isclose(b0, 1 / 3, abs_tol=1e-12)
    assert math.isclose(b1, 1.5, abs_tol=1e-12)
    assert 3 / 2 == 1.5
    assert math.isclose(10 / 3 - 1.5 * 2, 1 / 3, abs_tol=1e-12)
    assert math.isclose(fit([0, 1, 2], [0, 1, 2])[1], 1, abs_tol=1e-12)
    assert math.isclose(fit([0, 1, 2], [0, 1, 100])[1], 50, abs_tol=1e-12)

    # Linked ridge question: singular ordinary fit and unique ridge fit.
    matrix = np.ones((2, 2))
    assert np.linalg.det(matrix.T @ matrix) == 0
    assert np.allclose(np.linalg.eigvalsh(matrix.T @ matrix), [0, 4])
    ridge = np.linalg.solve(matrix.T @ matrix + np.eye(2), matrix.T @ [1, 3])
    assert np.allclose(ridge, [0.8, 0.8])


if __name__ == "__main__":
    test_printed_values()
