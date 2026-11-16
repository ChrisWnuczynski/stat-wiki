"""Check numerical claims printed on the generated cross-validation article."""

from fractions import Fraction
from pathlib import Path


if __name__ == "__main__":
    page = (Path(__file__).resolve().parents[1] / "articles" / "cross-validation.qmd").read_text()
    printed = (
        "eleven observations in three folds of sizes four, four, and three",
        "one error in the first fold, none in the second, and one in the third",
        r"2/11\approx0.1818",
        r"(1/4+0+1/3)/3=7/36\approx0.1944",
        "the training error at $k=1$ is zero",
    )
    for value in printed:
        assert value in page, f"Value missing from generated article: {value}"
    assert Fraction(1 + 0 + 1, 4 + 4 + 3) == Fraction(2, 11)
    assert (Fraction(1, 4) + Fraction(0, 4) + Fraction(1, 3)) / 3 == Fraction(7, 36)
    assert round(2 / 11, 4) == 0.1818
    assert round(7 / 36, 4) == 0.1944
    print("cross-validation arithmetic and printed values passed")
