"""Recompute the worked likelihood ratios and boundary case."""

from math import exp, factorial, isclose


def poisson_likelihood(rate, counts):
    return exp(-len(counts) * rate) * rate ** sum(counts) / factorial_product(counts)


def factorial_product(counts):
    result = 1
    for count in counts:
        result *= factorial(count)
    return result


if __name__ == "__main__":
    observed = [1, 3, 2]
    assert poisson_likelihood(2, observed) > poisson_likelihood(1, observed)
    assert isclose(poisson_likelihood(2, observed) / poisson_likelihood(1, observed), 64 * exp(-3))
    assert isclose(64 * exp(-3), 3.1863723755432924)
    assert isclose(6 / 2 - 3, 0)
    assert -6 / 2**2 < 0
    challenge = [0, 2, 1]
    assert isclose(poisson_likelihood(1, challenge) / poisson_likelihood(2, challenge), exp(3) / 8)
    assert isclose(exp(3) / 8, 2.5106921153984585)
    assert isclose(3 / 1 - 3, 0)
    assert isclose(0.7**7 * 0.3**3 / (0.5**10), 2.2769316864)
    assert all(poisson_likelihood(0, [0, 0, 0]) > poisson_likelihood(rate, [0, 0, 0])
               for rate in (0.01, 0.1, 1, 2))
    print("likelihood arithmetic and boundary: 10 checks passed")
