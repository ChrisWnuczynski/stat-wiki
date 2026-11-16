"""Arithmetic checks for the restricted-maximum-likelihood article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/restricted-maximum-likelihood.md").read_text(encoding="utf-8")
article = root / "articles/restricted-maximum-likelihood.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose and text in page, text


xs = [1, 2, 3, 4, 10]
mean = sum(xs) / len(xs)
rss = sum((x - mean) ** 2 for x in xs)
assert mean == 4 and rss == 50
assert rss / 5 == 10 and rss / 4 == 12.5
ys = [2, 2, 2, 6]
mean2 = sum(ys) / 4
rss2 = sum((y - mean2) ** 2 for y in ys)
assert mean2 == 3 and rss2 == 12
assert rss2 / 4 == 3 and rss2 / 3 == 4

# The log-likelihood derivative vanishes at Q/nu.
nu, Q = 4, 50
sigma2 = Q / nu
score = -nu / (2 * sigma2) + Q / (2 * sigma2 ** 2)
assert abs(score) < 1e-12

require("12.5")
require("$50$")
print("restricted-maximum-likelihood checks passed")
