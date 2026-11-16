"""Arithmetic and normalization printed in the Gaussian kernel article."""
import math
from pathlib import Path


def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "gaussian-kernel.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    assert math.isclose(phi(0), 0.39894, abs_tol=0.000005)
    assert math.isclose(phi(1), 0.24197, abs_tol=0.000005)
    assert math.isclose(phi(2), 0.05399, abs_tol=0.000005)

    data = [0, 2, 4]
    kde = lambda h: sum(phi((2 - xi) / h) for xi in data) / (len(data) * h)
    assert math.isclose(kde(2), 0.14715, abs_tol=0.000005)
    assert math.isclose(kde(1), 0.16897, abs_tol=0.000005)

    rbf = lambda sigma: math.exp(-(2 - 0) ** 2 / (2 * sigma * sigma))
    assert math.isclose(rbf(1), 0.13534, abs_tol=0.000005)
    assert math.isclose(rbf(2), 0.60653, abs_tol=0.000005)
    assert math.comb(2 + 2, 2) == 6

    # The linked self-checks use a different KDE sample and Gram matrix.
    linked_kde = (phi(1) + phi(0) + phi(2)) / 3
    assert math.isclose(linked_kde, 0.2316, abs_tol=0.00005)
    a, b = math.exp(-0.5), math.exp(-2)
    det = 1 - 2 * a * a + 2 * a * a * b - b * b
    assert math.isclose(1 - a * a, 0.632, abs_tol=0.0005)
    assert math.isclose(det, 0.3455, abs_tol=0.00005)


if __name__ == "__main__":
    test_printed_values()
