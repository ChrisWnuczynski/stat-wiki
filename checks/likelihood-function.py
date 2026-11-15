"""Recompute the worked likelihood ratios and boundary case."""

from math import comb, exp, factorial, isclose
from pathlib import Path


def poisson_likelihood(rate, counts):
    return exp(-len(counts) * rate) * rate ** sum(counts) / factorial_product(counts)


def factorial_product(counts):
    result = 1
    for count in counts:
        result *= factorial(count)
    return result


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/likelihood-function.md").read_text()
    for printed in ("3.186", "3.19", "2.511", "2^6", "\\widehat\\lambda=2"):
        assert printed in prose, f"Worked value missing from article source: {printed}"
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
    assert round(0.7**7 * 0.3**3 / (0.5**10), 2) == 2.28
    spark_values = [comb(10, 2) * p**2 * (1 - p) ** 8 for p in (0.4, 0.3, 0.2)]
    assert [round(v, 3) for v in spark_values] == [0.121, 0.233, 0.302]
    chapter = (root / "sources/stat2004/chapters/inf-02-estimation.qmd").read_text()
    for printed in ("0.121", "0.233", "0.302"):
        assert printed in chapter, f"Spark-plug value missing from source chapter: {printed}"
    generated = root / "articles/likelihood-function.qmd"
    if generated.exists():
        page = generated.read_text()
        for printed in ("2.28",):
            assert printed in page, f"Original worked value missing from generated page: {printed}"
    assert all(poisson_likelihood(0, [0, 0, 0]) > poisson_likelihood(rate, [0, 0, 0])
               for rate in (0.01, 0.1, 1, 2))
    print("likelihood arithmetic, boundary, and printed values passed")
