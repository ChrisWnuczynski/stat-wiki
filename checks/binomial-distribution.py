"""Arithmetic printed in the binomial distribution depth pass."""
import math


def test_printed_values():
    n, p = 100, 0.02
    assert n * p == 2
    assert math.isclose(n * p * (1-p), 1.96)
    p0 = (1-p)**n
    p1 = n * p * (1-p)**(n-1)
    assert math.isclose(p0, 0.13262, abs_tol=0.000005)
    assert math.isclose(p1, 0.27065, abs_tol=0.000005)
    assert math.isclose(p0+p1, 0.40327, abs_tol=0.000005)
    assert math.isclose(math.exp(-2) * (1+2), 0.40601, abs_tol=0.000005)
    n, p = 200, 0.01
    assert math.isclose((1-p)**n, 0.13398, abs_tol=0.000005)
    assert math.isclose(math.exp(-2), 0.13534, abs_tol=0.000005)
    assert n*p == 2
    assert math.isclose(n*p*(1-p), 1.98)


if __name__ == "__main__":
    test_printed_values()
