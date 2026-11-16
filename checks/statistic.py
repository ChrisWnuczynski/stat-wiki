"""Verify the sample summaries and challenge in the statistic article."""

from fractions import Fraction
from pathlib import Path


def summaries(values):
    n = len(values)
    average = Fraction(sum(values), n)
    sample_variance = sum((Fraction(x) - average) ** 2 for x in values) / (n - 1)
    return average, sample_variance, max(values) - min(values)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/statistic.md").read_text()
    for printed in ("(1+3+5+7)/4=4", "7-1=6", "20/3", "6.67", "(3-1)=4", "value is $0$"):
        assert printed in prose, f"Worked value missing from article source: {printed}"
    first = (1, 3, 5, 7)
    assert sum(first) == 16
    assert summaries(first)[0] == 4
    assert tuple((x - 4) ** 2 for x in first) == (9, 1, 1, 9)
    assert sum((x - 4) ** 2 for x in first) == 20
    assert summaries(first)[1] == Fraction(20, 3)
    assert round(float(summaries(first)[1]), 2) == 6.67
    assert summaries(first)[2] == 6
    challenge = (2, 4, 6)
    assert summaries(challenge)[0] == 4
    assert summaries(challenge)[1] == 4
    assert summaries(challenge)[2] == 4
    assert (summaries(challenge)[0] - 4) / 2 == 0
    generated = root / "articles/statistic.qmd"
    if generated.exists():
        page = generated.read_text()
        for printed in (r"\overline X-\mu", "t_{n-1}"):
            assert printed in page, f"Classification answer missing from generated page: {printed}"
    print("statistic arithmetic and printed values passed")
