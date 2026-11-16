"""Arithmetic checks for the normal sample theorem article."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/normal-sample-theorem.md").read_text(encoding="utf-8")
article = root / "articles/normal-sample-theorem.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose, text
    assert text in page, text


xs = [2, 4, 4, 6]
mean = sum(xs) / len(xs)
ss = sum((x - mean) ** 2 for x in xs)
s2 = ss / 3
assert mean == 4 and ss == 8 and abs(s2 - 8 / 3) < 1e-12
assert (3 * s2) / 4 == 2
t = (mean - 3) / math.sqrt(s2 / 4)
assert abs(t - math.sqrt(1.5)) < 1e-12
assert round(t, 3) == 1.225

ys = [1, 2, 3, 6]
mean2 = sum(ys) / 4
ss2 = sum((y - mean2) ** 2 for y in ys)
assert mean2 == 3 and ss2 == 14
t2 = mean2 / math.sqrt((ss2 / 3) / 4)
assert abs(t2 - 3 * math.sqrt(6 / 7)) < 1e-12
assert round(t2, 3) == 2.777

# Milk-carton t statistic quoted as about -4.87.
se = 0.0317 / math.sqrt(10)
milk_t = (1.0512 - 1.10) / se
assert round(milk_t, 2) == -4.87

require("1.0512")
require("0.0317")
require("-4.87")
require("$s^2=8/3$")
require("1.225")
require("$s^2=14/3$")
require("2.777")
print("normal-sample-theorem checks passed")
