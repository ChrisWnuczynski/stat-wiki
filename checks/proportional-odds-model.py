"""Arithmetic checks for the proportional-odds article."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/proportional-odds-model.md").read_text(encoding="utf-8")
article = root / "articles/proportional-odds-model.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose and text in page, text


p2 = 0.5
p3 = 1 / (1 + math.e)
assert abs(p3 - 0.268941) < 5e-7
assert abs((p2 - p3) - 0.231059) < 5e-6
assert abs(math.exp(0.5) - 1.648721) < 1e-5
assert round(math.exp(0.5), 3) == 1.649
p2_0 = 1 / (1 + math.e)
p3_0 = 1 / (1 + math.exp(2))
assert abs(p2_0 - 0.268941) < 5e-7
assert abs(p3_0 - 0.119203) < 5e-7
assert p2_0 > p3_0
require("0.268941")
require("0.231059")
require("1.649")
require("0.119203")
print("proportional-odds-model checks passed")
