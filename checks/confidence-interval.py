"""Check every numerical value used in the confidence-interval examples."""

from math import isclose, sqrt
from pathlib import Path
from statistics import NormalDist


if __name__ == "__main__":
    page = (Path(__file__).resolve().parents[1] / "articles" / "confidence-interval.qmd").read_text()
    printed = (
        "20(0.95)=19",
        r"0.95^{20}\approx0.3585",
        "178/\\sqrt{51}=24.92",
        "1136\\pm50.1=(1085.9,\\ 1186.1)",
        "40.56",
        "(1.03,\\ 3.27)",
        "(1.02,\\ 1.81)",
        "2\\Phi(2)-1=0.9545",
        "c=z_{0.995}=2.576",
    )
    for value in printed:
        assert value in page, f"Value missing from generated article: {value}"
    assert isclose(0.95**20, 0.3585, abs_tol=0.00005)
    assert 20 * 0.95 == 19
    assert isclose(178 / sqrt(51), 24.92, abs_tol=0.005)
    assert isclose(2.009 * 178 / sqrt(51), 50.1, abs_tol=0.05)
    assert isclose(1136 - 50.1, 1085.9, abs_tol=1e-9)
    assert isclose(1136 + 50.1, 1186.1, abs_tol=1e-9)
    assert isclose(24 * 1.3**2, 40.56, abs_tol=1e-9)
    assert isclose(40.56 / 39.36, 1.03, abs_tol=0.005)
    assert isclose(40.56 / 12.40, 3.27, abs_tol=0.005)
    assert isclose(sqrt(40.56 / 39.36), 1.02, abs_tol=0.005)
    assert isclose(sqrt(40.56 / 12.40), 1.81, abs_tol=0.005)
    normal = NormalDist()
    assert isclose(2 * normal.cdf(2) - 1, 0.9545, abs_tol=0.00005)
    assert isclose(normal.inv_cdf(0.995), 2.576, abs_tol=0.0005)
    print("confidence-interval arithmetic and printed values passed")
