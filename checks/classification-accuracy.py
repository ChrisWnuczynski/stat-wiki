"""Exact confusion-matrix, prevalence and decision-threshold checks."""

import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def rates(tp: int, fn: int, fp: int, tn: int) -> tuple[F, F, F, F]:
    n = tp + fn + fp + tn
    return F(tp + tn, n), F(tp, tp + fn), F(tn, tn + fp), F(tp, tp + fp)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    article = (root / "articles/classification-accuracy.qmd").read_text()
    pending = json.loads((root / "research/pending/classification-accuracy.json").read_text())
    assert 20 + 180 == 200
    assert F(180, 200) == F("0.90")
    assert F(0, 20) == 0 and F(180, 180) == 1
    acc, sens, spec, prec = rates(15, 5, 20, 160)
    assert (acc, sens, spec, prec) == (F(7, 8), F(3, 4), F(8, 9), F(3, 7))
    assert F(15 + 160, 200) == F("0.875")
    assert round(float(spec), 4) == 0.8889
    assert round(float(prec), 4) == 0.4286
    acc2, sens2, spec2, prec2 = rates(18, 2, 36, 144)
    assert (acc2, sens2, spec2, prec2) == (F(81, 100), F(9, 10), F(4, 5), F(1, 3))
    assert 18 - 15 == 3 and 36 - 20 == 16
    assert round(float(prec2), 4) == 0.3333
    assert F(1, 10) * F(4, 5) + F(9, 10) * F(9, 10) == F("0.89")
    assert F(1, 2) * F(4, 5) + F(1, 2) * F(9, 10) == F("0.85")
    p, cfp, cfn = sp.symbols("p cfp cfn", positive=True)
    assert sp.solve(sp.Eq(cfp * (1 - p), cfn * p), p) == [cfp / (cfp + cfn)]
    for printed in (
        "180/200=0.90", "0/20=0", "175/200=0.875", "15/20=0.75",
        "8/9\\approx0.8889", "3/7\\approx0.4286", "162/200=0.81",
        "18/20=0.90", "144/180=0.80", "1/3\\approx0.3333",
        "15 | 5 | 20", "20 | 160 | 180",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    bank = pending["new_bank_questions"][0]
    assert bank["id"] == "depth-classification-prevalence"
    for printed in ("0.80", "0.90", "0.10", "0.50", "0.89", "0.85"):
        assert printed in bank["answer"] + bank["body"]
    print("classification accuracy arithmetic: 18 checks passed")


if __name__ == "__main__":
    main()
