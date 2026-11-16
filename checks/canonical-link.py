"""Arithmetic printed in the canonical-link article."""
import math


def test_printed_values():
    b0, b1 = math.log(1/3), math.log(2)
    odds0, odds1 = math.exp(b0), math.exp(b0+b1)
    p0, p1 = odds0/(1+odds0), odds1/(1+odds1)
    assert math.isclose(odds0, 1/3)
    assert math.isclose(odds1, 2/3)
    assert math.isclose(p0, 1/4)
    assert math.isclose(p0, 0.25)
    assert math.isclose(p1, 2/5)
    assert math.isclose(p1, 0.40)
    assert math.isclose(p1-p0, 0.15)
    assert math.isclose(odds1/odds0, 2)
    poisson_means = [math.exp(math.log(3)+x*math.log(2)) for x in (0,1,2)]
    for got, expected in zip(poisson_means, (3,6,12)):
        assert math.isclose(got, expected)


if __name__ == "__main__":
    test_printed_values()
