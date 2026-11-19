"""Verify the exercises that replaced same-page repeats."""

from fractions import Fraction
from math import exp, isclose, log, sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "research" / "content"


def prose(slug):
    return (CONTENT / f"{slug}.md").read_text(encoding="utf-8")


def need(slug, *parts):
    text = prose(slug)
    for part in parts:
        assert part in text, f"{slug} missing {part}"


if __name__ == "__main__":
    assert Fraction(2, 3) == Fraction(1, 1) / Fraction(3, 2)
    assert (Fraction(1, 3) ** 2) == Fraction(1, 9)
    need("acceptance-rejection-method", "1/M=2/3", "1/9")

    assert Fraction(10, 40) == Fraction(1, 4)
    need("conditional-probability", "10/40=1/4")

    assert 5 * 4 == 20
    assert 4 * 4 + 2 * 5 ** 2 == 66
    need("conditional-distribution", "5\\times 4=20", "16+50=66")

    assert Fraction(3, 2 * 3) == Fraction(1, 2)
    assert 4 + 9 + 2 * 3 == 19
    need("covariance", "3/(2\\times 3)=1/2", "4+9+2\\times 3=19")

    assert isclose(exp(-1.5), 0.22313016014842982)
    assert isclose(2 * log(2), 1.3862943611198906)
    need("exponential-distribution", "e^{-3/2}\\approx 0.22313", "1.386294")

    assert 1 + 4 + 9 == 14
    assert isclose(8 / (3.5 - 1), 3.2)
    need("full-conditionals-under-independent-priors", "1+4+9=14", "8/(3.5-1)=3.2")

    assert Fraction(6, 45) == Fraction(2, 15)
    need("hypergeometric-distribution", "6/45=2/15")

    assert 9 - 4 - 5 + 2 == 2
    assert 9 - 4 == 5
    need("interaction", "9-4-5+2=2", "9-4=5")

    pi1 = Fraction(1, 5) / Fraction(7, 10)
    assert pi1 == Fraction(2, 7)
    assert 1 - pi1 == Fraction(5, 7)
    # Balance: (1/2)(2/7) + (1/5)(5/7) = 2/7.
    assert Fraction(1, 2) * pi1 + Fraction(1, 5) * (1 - pi1) == pi1
    need("limiting-distribution", "(2/7,5/7)")

    ratio = (Fraction(6, 5) ** 3) * (Fraction(4, 5) ** 2)
    assert ratio == Fraction(3456, 3125)
    assert isclose(float(ratio), 1.10592)
    need("maximum-likelihood", "3456/3125=1.10592")

    assert (14 - 10) / sqrt(4) == 2
    need("normal-distribution", "(14-10)/2=2", "P(X\\le 14)=\\Phi(2)")
    # The undelimited normal probability on the lead stays for the other pass.
    assert "(P(X<496)=\\Phi(-1)\\approx0.1587)" in prose("normal-distribution")

    assert 3 / sqrt(9) == 1
    assert (5 - 4) / 1 == 1
    assert 9 - 1 == 8
    need("one-sample-t-test", "3/\\sqrt{9}=1", "9-1=8")

    groups = [(1, 3), (2, 2), (5, 5)]
    grand = sum(sum(g) for g in groups) / 6
    means = [sum(g) / 2 for g in groups]
    between = sum(2 * (m - grand) ** 2 for m in means)
    within = sum((y - m) ** 2 for g, m in zip(groups, means) for y in g)
    assert grand == 3 and means == [2, 2, 5]
    assert between == 12 and within == 2
    assert (between / 2) / (within / 3) == 9
    need("one-way-analysis-of-variance", "(12/2)/(2/3)=9")

    assert isclose(exp(-2.5), 0.0820849986238988)
    need("poisson-distribution", "\\lfloor 2.5\\rfloor=2", "e^{-2.5}\\approx 0.082085")

    assert isclose(0.9 * 0.8, 0.72)
    assert isclose(1 - 0.1 * 0.2, 0.98)
    need("reliability-function", "0.9\\times 0.8=0.72", "1-0.1\\times 0.2=0.98")

    margin = 2 / 1
    assert margin == 2
    assert Fraction(1, 4) == Fraction(1, 4)
    assert Fraction(2, 4) == Fraction(1, 2)
    text = (ROOT / "research" / "self-checks.json").read_text(encoding="utf-8")
    window = text.split('"linear-separators-and-the-margin"')[1].split('"markov-chain"')[0]
    assert '"ex-sl-17-1"' in window
    assert '"ex-sl-17-3"' in window

    print("replacement exercises passed")
