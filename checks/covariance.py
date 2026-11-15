"""Check the worked covariance examples using exact probabilities."""

from fractions import Fraction


def mean(values):
    return sum(map(Fraction, values), Fraction()) / len(values)


def variance(values):
    center = mean(values)
    return mean([(Fraction(x) - center) ** 2 for x in values])


def covariance(xs, ys):
    return mean([(Fraction(x) - mean(xs)) * (Fraction(y) - mean(ys))
                 for x, y in zip(xs, ys)])


if __name__ == "__main__":
    xs = (1, 2, 3)
    ys = (3, 4, 8)
    assert mean(xs) == 2
    assert mean(ys) == 5
    assert covariance(xs, ys) == Fraction(5, 3)
    assert variance(xs) == Fraction(2, 3)
    assert variance(ys) == Fraction(14, 3)
    assert variance(tuple(x + y for x, y in zip(xs, ys))) == Fraction(26, 3)
    assert variance(xs) + variance(ys) + 2 * covariance(xs, ys) == Fraction(26, 3)
    challenge = (8, 4, 3)
    assert mean(challenge) == 5
    assert covariance(xs, challenge) == Fraction(-5, 3)
    assert variance(challenge) == Fraction(14, 3)
    assert variance(tuple(x + y for x, y in zip(xs, challenge))) == 2
    assert variance(xs) + variance(challenge) + 2 * covariance(xs, challenge) == 2
    dependent = (-1, 0, 1)
    assert covariance(dependent, tuple(x*x for x in dependent)) == 0
    assert Fraction(-1) - Fraction(1, 4) * -1 == Fraction(-3, 4)
    print("covariance arithmetic: 14 exact checks passed")
