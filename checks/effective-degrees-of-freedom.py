"""Numerical and preservation checks for the effective-degrees-of-freedom page."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PAGE = (ROOT / "articles/effective-degrees-of-freedom.qmd").read_text()
EXAM = (ROOT / "sources/prep/chapters/alan.qmd").read_text()


def check_spectral_example() -> None:
    original = sum(sp.Rational(1, 1 + d) for d in (0, 0, 1, 9))
    assert original == sp.Rational(13, 5)  # 2.6
    assert original - 1 == sp.Rational(8, 5)  # centred smooth: 1.6
    assert "2.6" in PAGE and "1.6" in PAGE

    penalties = (0, 0, 2, 6)
    weights = [1 / (1 + sp.Rational(1, 2) * d) for d in penalties]
    assert weights == [1, 1, sp.Rational(1, 2), sp.Rational(1, 4)]
    assert sum(weights) == sp.Rational(11, 4)  # 2.75
    y = sp.Matrix([2, 1, 4, -4])
    assert sp.diag(*weights) * y == sp.Matrix([2, 1, 2, -1])
    assert "2.75" in PAGE and "(2,1,2,-1)" in PAGE

    turn_weights = [sp.Rational(1, 1 + d) for d in penalties]
    assert turn_weights == [1, 1, sp.Rational(1, 3), sp.Rational(1, 7)]
    assert sum(turn_weights) == sp.Rational(52, 21)
    assert round(float(sum(turn_weights)), 4) == 2.4762
    assert "52/21" in PAGE and "2.4762" in PAGE


def check_definitions_and_limits() -> None:
    assert sp.eye(3).trace() == 3
    assert sp.diag(1, 1, sp.Rational(1, 2), sp.Rational(1, 4)).trace() == sp.Rational(11, 4)
    assert sp.limit(1 / (1 + sp.Symbol("t") * 2), sp.Symbol("t"), sp.oo) == 0
    assert abs(0 - 3) > 2 and abs(0 - 1) <= 2
    assert ((0 + 1) / 2, (0 + 1) / 2) == (0.5, 0.5)
    for token in (
        "## Motivating example",
        "## Definition",
        "## Properties",
        "## Worked example",
        "## Statistical use",
        "## Common misconceptions",
        "## Assumptions and limits",
        'title="Proof"',
        "**Your turn.**",
        "8.881",
        "2.011",
        "(0.5,0.5)",
    ):
        assert token in PAGE, token
    assert PAGE.count('title="Proof"') == 1
    for source in ("efron2004_prediction_error", "wood2025_mgcv_docs", "dodge2008"):
        assert f'data-cite-key="{source}"' in PAGE, source
    assert "s(latitude) 8.881" in EXAM and "s(cholesterol) 2.011" in EXAM


if __name__ == "__main__":
    check_spectral_example()
    check_definitions_and_limits()
    print("Effective degrees of freedom examples and preserved numbers passed")
