"""Independent arithmetic checks for research/content/variance.md."""

from fractions import Fraction
from math import isclose, sqrt


def weighted_moments(values, probabilities):
    assert sum(probabilities) == 1
    mean = sum(value * probability for value, probability in zip(values, probabilities))
    second = sum(value * value * probability for value, probability in zip(values, probabilities))
    variance = sum((value - mean) ** 2 * probability for value, probability in zip(values, probabilities))
    assert variance == second - mean * mean
    return mean, variance


if __name__ == "__main__":
    assert weighted_moments([10], [Fraction(1)]) == (10, 0)
    assert weighted_moments([0, 20], [Fraction(1, 2)] * 2) == (10, 100)
    mean, variance = weighted_moments([-2, 0, 4], [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)])
    assert (mean, variance) == (Fraction(1, 2), Fraction(19, 4))
    assert isclose(sqrt(variance), 2.179449471770337)
    assert weighted_moments([1, 3, 5], [Fraction(1, 3)] * 3) == (3, Fraction(8, 3))
    assert Fraction(1) + Fraction(2) ** 2 == 5
    print("variance arithmetic: 5 checks passed")
