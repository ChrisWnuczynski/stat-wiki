"""Exact and numerical checks for the posterior-odds theorem examples."""

from fractions import Fraction as F
from math import comb, sqrt
from pathlib import Path

from scipy.stats import norm


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/posterior-odds-factorisation.qmd").read_text()
    # New four-component example and its hidden follow-up.
    m0 = F(comb(4, 3)) * F(1, 2) ** 4
    m1 = F(comb(4, 3)) * F(3, 4) ** 3 * F(1, 4)
    assert m0 == F(1, 4) and m1 == F(27, 64)
    bf = m1 / m0
    assert bf == F(27, 16) and float(bf) == 1.6875
    prior_odds = F(1, 5) / F(4, 5)
    assert prior_odds == F(1, 4)
    post_odds = bf * prior_odds
    assert post_odds == F(27, 64)
    assert post_odds / (1 + post_odds) == F(27, 91)
    assert round(float(F(27, 91)), 4) == 0.2967
    m04, m14 = F(1, 2) ** 4, F(3, 4) ** 4
    assert m04 == F(1, 16) and m14 == F(81, 256)
    assert m14 / m04 == F(81, 16) == F("5.0625")
    assert (m14 / m04) * prior_odds == F(81, 64)
    assert (F(81, 64) / (1 + F(81, 64))) == F(81, 145)
    assert round(float(F(81, 145)), 4) == 0.5586
    # Pre-existing worked answer: Bayes factor 4 updates 1:9 to 4:9.
    assert F(4) * F(1, 9) == F(4, 9)
    assert F(4, 9) / (1 + F(4, 9)) == F(4, 13)
    assert 1 - F(4, 13) == F(9, 13)
    # Pre-existing normal IQ example, checked from its exact conjugate update.
    variance = F(15 * 15 * 10 * 10, 15 * 15 + 10 * 10)
    mean = F(15 * 15 * 135 + 10 * 10 * 100, 15 * 15 + 10 * 10)
    assert variance == F(900, 13) and mean == F(1615, 13)
    sd = sqrt(float(variance))
    assert round(float(variance), 4) == 69.2308
    assert round(float(mean), 4) == 124.2308
    assert round(sd, 4) == 8.3205
    z = norm.ppf(0.975)
    assert round(z, 6) == 1.959964
    assert round(float(mean) - z * sd, 3) == 107.923
    assert round(float(mean) + z * sd, 3) == 140.539
    post0 = norm.cdf((130 - float(mean)) / sd)
    prior0 = norm.cdf((130 - 100) / 15)
    assert round(post0, 4) == 0.7560
    assert round(1 - post0, 4) == 0.2440
    assert round(post0 / (1 - post0), 4) == 3.0977
    assert round(prior0, 5) == 0.97725
    assert round(prior0 / (1 - prior0), 4) == 42.9558
    bf01 = (post0 / (1 - post0)) / (prior0 / (1 - prior0))
    assert round(bf01, 4) == 0.0721
    assert round(1 / bf01, 2) == 13.87
    for printed in (
        "27/16", "1.6875", "27:64", "27/91", "0.2967", "81/256",
        "81/16", "5.0625", "81:64", "81/145", "0.5586", "frac4{13}",
        "frac9{13}", "69.2308", "124.2308", "8.3205", "107.923",
        "140.539", "0.7560", "0.2440", "3.0977", "0.97725",
        "42.9558", "0.0721", "13.87",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    print("posterior-odds-factorisation arithmetic: 32 checks passed")


if __name__ == "__main__":
    main()
