"""Arithmetic printed in the Fisher information article."""
import math


def test_printed_values():
    n, successes = 20, 14
    p = successes / n
    info = n / (p * (1 - p))
    assert p == 0.7
    assert math.isclose(info, 95.2381, abs_tol=0.00005)
    assert math.isclose(info ** -0.5, 0.10247, abs_tol=0.000005)
    n, successes = 50, 20
    p = successes / n
    info = n / (p * (1 - p))
    assert p == 0.4
    assert math.isclose(info, 208.3333, abs_tol=0.00005)
    assert math.isclose(info ** -0.5, 0.06928, abs_tol=0.000005)


if __name__ == "__main__":
    test_printed_values()
