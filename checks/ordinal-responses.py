"""Printed-value checks for ordinal responses."""

from __future__ import annotations

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "ordinal-responses.md").read_text(encoding="utf-8")


def expit(z: float) -> float:
    return 1 / (1 + math.exp(-z))


def main() -> None:
    assert abs((1.2 - 0.5 * 2) - 0.2) < 1e-12
    assert abs((0.2 - 0.5 * 2) - (-0.8)) < 1e-12
    upper, top = expit(0.2), expit(-0.8)
    assert f"{upper:.4f}" == "0.5498"
    assert f"{top:.4f}" == "0.3100"
    assert f"{1 - upper:.4f}" == "0.4502"
    assert f"{upper - top:.4f}" == "0.2398"
    assert abs((1 - upper) + (upper - top) + top - 1) < 1e-12
    assert f"{math.exp(-0.5):.4f}" == "0.6065"
    assert f"{math.exp(0.5):.4f}" == "1.6487"
    for token in ("0.5498", "0.3100", "0.4502", "0.2398", "0.6065", "1.6487"):
        assert token in PROSE, token
    article = ROOT / "articles" / "ordinal-responses.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "0.5498" in body and "1.6487" in body
    print("ordinal-responses checks passed")


if __name__ == "__main__":
    main()
