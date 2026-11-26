"""Arithmetic checks for the sigma-algebra article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/sigma-algebra.md").read_text(encoding="utf-8")
article = root / "articles/sigma-algebra.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose, text
    assert text in page, text


atoms = {"{1}", "{2}", "{3,4}"}
assert len(atoms) == 3
assert 2 ** 3 == 8
assert 2 ** 4 == 16
require(r"$2^3=8$")
require(r"$2^4=16$")
require(r"$\mathbb{P}(\{1\})=1/3$")
require(r"$\mathbb{P}(\{2,3\})=2/3$")
print("sigma-algebra checks passed")
