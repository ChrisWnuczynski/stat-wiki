"""Recompute posterior means, modes, weights, and risk in the page's examples."""

from fractions import Fraction
from math import isclose, sqrt
from pathlib import Path
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/posterior-mean.md").read_text()
    for marker in re.finditer(r"\{\{cite:([^}]+)\}\}", prose):
        assert re.match(r" \((?:p\.|pp\.|Ch\.)", prose[marker.end():]), (
            f"Citation without a location: {marker.group()}"
        )
    for printed in (
        r"\operatorname{Beta}(9,5)",
        "9/14\\approx0.643",
        "(4/14)(1/2)+(10/14)(7/10)=9/14",
        "(9-1)/(9+5-2)=2/3",
        "=3/196\\approx0.0153",
        r"\sqrt{3}/14\approx0.124",
        "$0.700$",
        "$0.057$",
        "1/4+1=5/4",
        "(1/5)(0)+(4/5)(3)=2.4",
        r"\sqrt{0.8}\approx0.894",
        "sampling standard deviation $2$",
        "=2.4",
        "=0.8",
        r"\operatorname{Beta}(4,8)",
        "4/12=1/3",
        "(4-1)/(4+8-2)=3/10",
    ):
        assert printed in prose, f"Worked value missing from article source: {printed}"
    prior_a, prior_b, x, n = 2, 2, 7, 10
    post_a, post_b = prior_a + x, prior_b + n - x
    post_mean = Fraction(post_a, post_a + post_b)
    post_mode = Fraction(post_a - 1, post_a + post_b - 2)
    prior_weight = Fraction(prior_a + prior_b, prior_a + prior_b + n)
    data_weight = Fraction(n, prior_a + prior_b + n)
    prior_precision = Fraction(1, 4)
    data_precision = Fraction(4, 4)
    normal_precision = prior_precision + data_precision
    checks = [
        (post_a, post_b) == (9, 5),
        post_mean == Fraction(9, 14),
        prior_weight == Fraction(4, 14),
        data_weight == Fraction(10, 14),
        prior_weight + data_weight == 1,
        prior_weight * Fraction(1, 2) + data_weight * Fraction(7, 10) == post_mean,
        post_mode == Fraction(2, 3),
        Fraction(post_a * post_b, (post_a + post_b) ** 2 * (post_a + post_b + 1)) == Fraction(3, 196),
        isclose(float(Fraction(3, 196)), 0.0153, abs_tol=0.00005),
        isclose(sqrt(3) / 14, 0.124, abs_tol=0.0005),
        isclose(float(Fraction(7, 10) - post_mean), 0.057, abs_tol=0.0005),
        normal_precision == Fraction(5, 4),
        Fraction(3, 1) / normal_precision == Fraction(12, 5),
        1 / normal_precision == Fraction(4, 5),
        Fraction(prior_precision, normal_precision) == Fraction(1, 5),
        Fraction(data_precision, normal_precision) == Fraction(4, 5),
        isclose(sqrt(0.8), 0.894, abs_tol=0.0005),
        (1 + 3, 1 + 10 - 3) == (4, 8),
        Fraction(4, 12) == Fraction(1, 3),
        Fraction(4 - 1, 4 + 8 - 2) == Fraction(3, 10),
        Fraction(3, 3 + 9) == Fraction(1, 4),
        Fraction(3 - 1, 3 + 9 - 2) == Fraction(1, 5),
    ]
    assert all(checks)
    generated = root / "articles/posterior-mean.qmd"
    if generated.exists():
        page = generated.read_text()
        for unopened in ("gelman_bda2013", "raiffa_schlaifer1961", "box_tiao1973", "jeffreys1961"):
            assert f'data-cite-key="{unopened}"' not in page, f"Unopened source still cited: {unopened}"
        for printed in (r"\operatorname{Beta}(9,5)", "=2.4", "=0.8", "part1-fig-01-credible-regions.png"):
            assert printed in page, f"Worked value or figure missing from generated article: {printed}"
    print(f"posterior-mean arithmetic: {len(checks)} checks passed")
