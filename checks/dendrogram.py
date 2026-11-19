"""Printed-value checks for the dendrogram depth pass."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "dendrogram.md").read_text(encoding="utf-8")


def single_linkage_height(left: list[float], right: list[float]) -> float:
    return min(abs(a - b) for a in left for b in right)


def main() -> None:
    points = [0, 1, 4, 10]
    h1 = single_linkage_height([0], [1])
    h2 = single_linkage_height([0, 1], [4])
    h3 = single_linkage_height([0, 1, 4], [10])
    assert (h1, h2, h3) == (1, 3, 6)
    assert max(abs(a - b) for a in (0, 1) for b in (4,)) == 4
    h11 = single_linkage_height([10], [11])
    h_cross = single_linkage_height([0, 1, 4], [10, 11])
    assert h11 == 1 and h_cross == 6
    assert "0.5" in PROSE and ("height $7$" in PROSE or "height \\(7\\)" in PROSE)
    for token in ("\\{0,1\\}", "3", "6"):
        assert token in PROSE or token.strip("\\") in PROSE
    assert "1" in PROSE and "11" in PROSE
    article = ROOT / "articles" / "dendrogram.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "0.5" in body and "11" in body
    print("dendrogram checks passed")


if __name__ == "__main__":
    main()
