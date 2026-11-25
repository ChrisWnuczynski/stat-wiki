"""Check numerical claims printed on the generated cross-validation article."""

from fractions import Fraction
from pathlib import Path
import re


if __name__ == "__main__":
    page = (Path(__file__).resolve().parents[1] / "articles" / "cross-validation.qmd").read_text()
    worked = page.split("## Worked example", 1)[1].split("\n## ", 1)[0]
    example, exercise = worked.split("**Your turn.**", 1)
    printed = (
        "eleven observations in three folds of sizes four, four, and three",
        "no errors in the first fold, one in the second, and two in the third",
        r"3/11\approx0.2727",
        r"(0+1/4+2/3)/3=11/36\approx0.3056",
    )
    for value in printed:
        assert value in example, f"Value missing from visible worked example: {value}"
    answer = re.search(
        r'^::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::',
        exercise,
        re.M | re.S,
    )
    assert answer, "Exercise answer must remain folded"
    visible = example + exercise[:answer.start()] + exercise[answer.end():]
    for value in ("2/11", "0.1818"):
        assert value not in visible, f"Exercise answer leaked outside its fold: {value}"
    assert r"2/11\approx0.1818" in answer.group(1)
    assert r"1/6\approx0.1667" in answer.group(1)
    assert "the training error at $k=1$ is zero" in page
    assert Fraction(0 + 1 + 2, 4 + 4 + 3) == Fraction(3, 11)
    assert (Fraction(0, 4) + Fraction(1, 4) + Fraction(2, 3)) / 3 == Fraction(11, 36)
    assert round(3 / 11, 4) == 0.2727
    assert round(11 / 36, 4) == 0.3056
    print("cross-validation arithmetic and printed values passed")
