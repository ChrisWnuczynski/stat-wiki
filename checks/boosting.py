"""Printed-value checks for the boosting depth pass."""

from __future__ import annotations

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "boosting.md").read_text(encoding="utf-8")


def alpha(eps: float) -> float:
    return 0.5 * math.log((1 - eps) / eps)


def main() -> None:
    assert abs(alpha(0.25) - 0.5493061443340549) < 1e-12
    assert f"{alpha(0.25):.4f}" == "0.5493"
    assert "0.5493" in PROSE
    # ε = 1/4, weights sum to 1: correct group and incorrect group each total 1/2.
    eps = 0.25
    grow_wrong = math.exp(alpha(eps))
    grow_right = math.exp(-alpha(eps))
    wrong = eps * grow_wrong
    right = (1 - eps) * grow_right
    assert abs(wrong - right) < 1e-12
    normaliser = wrong + right
    assert abs(wrong / normaliser - 0.5) < 1e-12
    # three correct cases share the correct half
    assert abs((0.25 * grow_right) / normaliser - 1 / 6) < 1e-12
    assert abs((0.25 * grow_wrong) / normaliser - 0.5) < 1e-12
    assert "1/6" in PROSE and "1/2" in PROSE
    assert abs((1 - 0.2) / 0.2 - 4) < 1e-12
    assert "1/5" in PROSE
    assert f"{alpha(0.4):.4f}" == "0.2027"
    assert "0.2027" in PROSE
    assert abs(0.6 / 0.4 - 1.5) < 1e-12
    assert abs(0.6 - 0.2 - 0.4) < 1e-12
    assert "0.4" in PROSE
    # ESL full-log coefficient is twice the half-log coefficient.
    assert abs(math.log(0.75 / 0.25) - 2 * alpha(0.25)) < 1e-12
    article = ROOT / "articles" / "boosting.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        for token in ("0.5493", "1/6", "0.2027"):
            assert token in body, token
    print("boosting checks passed")


if __name__ == "__main__":
    main()
