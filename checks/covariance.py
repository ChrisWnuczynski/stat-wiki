"""Check the worked covariance examples using exact probabilities."""

from fractions import Fraction
from pathlib import Path


def mean(values):
    return sum(map(Fraction, values), Fraction()) / len(values)


def variance(values):
    center = mean(values)
    return mean([(Fraction(x) - center) ** 2 for x in values])


def covariance(xs, ys):
    return mean([(Fraction(x) - mean(xs)) * (Fraction(y) - mean(ys))
                 for x, y in zip(xs, ys)])


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/covariance.md").read_text()
    for printed in ("5/3", "14/3", "26/3", "16/3", "-5/3", "-10/3"):
        assert printed in prose, f"Worked value missing from article source: {printed}"
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
    generated = root / "articles/covariance.qmd"
    if generated.exists():
        page = generated.read_text()
        assert "prob-correlation" in page
        for printed in ("-3/4", r"\tfrac13", r"\tfrac23"):
            assert printed in page, f"Original worked value missing from generated page: {printed}"
    print("covariance arithmetic and printed values passed")
