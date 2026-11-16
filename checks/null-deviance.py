"""Printed-value checks for the null deviance."""

from __future__ import annotations

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "null-deviance.md").read_text(encoding="utf-8")


def bernoulli_null(successes: int, n: int) -> float:
    p = successes / n
    failures = n - successes
    return -2 * (successes * math.log(p) + failures * math.log(1 - p))


def main() -> None:
    d = bernoulli_null(3, 4)
    assert abs(d - 4.498681156950466) < 1e-12
    assert f"{d:.4f}" == "4.4987"
    assert abs(bernoulli_null(1, 4) - d) < 1e-12
    assert abs((4.4987 - 1.4987) - 3) < 1e-9
    assert "4.4987" in PROSE and "1.4987" in PROSE
    assert "4/5" in PROSE
    article = ROOT / "articles" / "null-deviance.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "4.4987" in body
        assert "cholest" in body  # the page's earlier code block remains
    print("null-deviance checks passed")


if __name__ == "__main__":
    main()
