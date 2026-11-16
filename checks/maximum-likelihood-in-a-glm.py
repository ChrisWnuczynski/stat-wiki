"""Arithmetic checks for maximum likelihood in a GLM."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/maximum-likelihood-in-a-glm.md").read_text(encoding="utf-8")
article = root / "articles/maximum-likelihood-in-a-glm.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose and text in page, text


assert abs(math.e - 2.718282) < 5e-7
assert abs(2 / math.e - 0.735759) < 5e-7
assert abs(math.log(2) - 0.693147) < 5e-7
assert math.exp(2 / math.e) > 2
assert abs((2 - math.exp(math.log(2)))) < 1e-12
require("2.718282")
require("0.735759")
require("0.693147")
require(r"\log 2")
print("maximum-likelihood-in-a-glm checks passed")
