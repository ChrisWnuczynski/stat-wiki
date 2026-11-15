"""Check predictor, interaction, link, and offset calculations."""

from math import exp, isclose, log
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "articles" / "linear-predictor.qmd"


if __name__ == "__main__":
    page = PAGE.read_text(encoding="utf-8")
    def interaction(x, z):
        return 1 + 0.2 * x - 0.4 * z + 0.1 * x * z

    def expit(eta):
        return 1 / (1 + exp(-eta))

    eta2 = -2 + 0.5 * 2
    eta4 = -2 + 0.5 * 4
    odds2 = exp(eta2)
    odds4 = exp(eta4)
    exposure = 5
    base_eta = 0.3
    checks = [
        isclose(interaction(2, 1), 1.2),
        isclose(interaction(3, 1) - interaction(2, 1), 0.3),
        isclose(interaction(3, 0) - interaction(2, 0), 0.2),
        isclose(interaction(2, 1) - interaction(2, 0), -0.4 + 0.1 * 2),
        eta2 == -1,
        eta4 == 0,
        isclose(expit(eta2), 1 / (1 + exp(1))),
        isclose(expit(eta2), 0.2689414213699951),
        isclose(expit(eta4), 0.5),
        isclose(odds4 / odds2, exp(1)),
        isclose(expit(eta4) - expit(eta2), 0.2310585786300049),
        isclose(expit(-2), 0.11920292202211755),
        isclose(exp(log(exposure) + base_eta), exposure * exp(base_eta)),
        isclose(exp(base_eta + 0.4) / exp(base_eta), exp(0.4)),
        isclose(expit(-2) / (1 - expit(-2)), exp(-2)),
        "predictor equals $1.2$" in page,
        "equals $0.2$ when $z=0$ and $0.3$ when $z=1$" in page,
        "At $x=2$, $\\eta=-1$" in page,
        "odds are $e^{-1}\\approx0.368$" in page,
        "probability is $1/(1+e)\\approx0.269$" in page,
        "At $x=4$, $\\eta=0$" in page,
        "probability is $1/2$" in page,
        "=e\\approx2.718$" in page,
        "rises by about $0.231$" in page,
        "\\approx0.119$" in page,
    ]
    assert all(checks), [index for index, passed in enumerate(checks, 1) if not passed]
    print(f"linear-predictor arithmetic: {len(checks)} checks passed")
