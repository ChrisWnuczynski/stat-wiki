"""Verify the sample summaries and challenge in the statistic article."""

from fractions import Fraction


def summaries(values):
    n = len(values)
    average = Fraction(sum(values), n)
    sample_variance = sum((Fraction(x) - average) ** 2 for x in values) / (n - 1)
    return average, sample_variance, max(values) - min(values)


if __name__ == "__main__":
    first = (1, 3, 5, 7)
    assert sum(first) == 16
    assert summaries(first)[0] == 4
    assert tuple((x - 4) ** 2 for x in first) == (9, 1, 1, 9)
    assert sum((x - 4) ** 2 for x in first) == 20
    assert summaries(first)[1] == Fraction(20, 3)
    assert summaries(first)[2] == 6
    challenge = (2, 4, 6)
    assert summaries(challenge)[0] == 4
    assert summaries(challenge)[1] == 4
    assert summaries(challenge)[2] == 4
    assert (summaries(challenge)[0] - 4) / 2 == 0
    print("statistic arithmetic: 10 exact checks passed")
