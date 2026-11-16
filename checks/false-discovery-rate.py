"""Printed-value checks for the false-discovery-rate depth pass."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "false-discovery-rate.md").read_text(encoding="utf-8")


def largest(ps: list[float], alpha: float) -> int:
    m = len(ps)
    passed = [j for j, p in enumerate(ps, start=1) if p < alpha * j / m]
    return max(passed, default=0)


def main() -> None:
    ps = [0.001, 0.04, 0.06, 0.8]
    assert [round(0.1 * j / 4, 10) for j in range(1, 5)] == [0.025, 0.05, 0.075, 0.1]
    assert largest(ps, 0.1) == 3
    assert largest(ps, 0.05) == 1
    assert not (0.04 < 0.05 * 2 / 4)
    assert 0.06 < 0.1 * 3 / 4
    assert largest([0.01, 0.04], 0.05) == 2
    for token in ("0.025", "0.075", "0.0125", "0.0375", "0.001", "0.8"):
        assert token in PROSE, token
    # Q <= indicator
    for v, r in ((0, 0), (0, 3), (2, 4), (4, 4)):
        q = 0 if r == 0 else v / r
        assert q <= (1 if v >= 1 else 0)
    article = ROOT / "articles" / "false-discovery-rate.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "0.025" in body and "0.0125" in body
    print("false-discovery-rate checks passed")


if __name__ == "__main__":
    main()
