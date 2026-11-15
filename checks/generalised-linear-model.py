"""Check the GLM article's printed contrasts and preserved figures."""

from fractions import Fraction
from math import exp, isclose, log
from pathlib import Path
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/generalised-linear-model.md").read_text()
    page = (root / "articles/generalised-linear-model.qmd").read_text()
    for match in re.finditer(r"\{\{cite:([^}]+)\}\}", prose):
        assert re.match(r" \((?:Summary|Introduction|Ch\.|§|pp\.|p\.)", prose[match.end():]), (
            f"Citation without location: {match.group()}"
        )
    printed = (
        r"$\eta=\log 2+x\log 3$", r"$2$ at $x=0$ and $6$ at $x=1$",
        r"$6/2=3$", r"$2/(1+2)=2/3$", r"$6/(1+6)=6/7$",
        r"$6/7-2/3=4/21\approx0.1905$", r"$\log18$",
        r"$18$", r"$18/19\approx0.9474$",
        r"\exp(2.595)\approx 13.4", r"\exp(-0.01495)\approx 0.985",
        r"\exp(-0.1495)\approx 0.861", r"\exp(0.2093)\approx 1.233",
        r"$1.16$", r"$1.23$", r"$2646.1$", r"$1249.9$",
        r"$69$", r"$67$", r"$8.881$",
    )
    for value in printed:
        assert value in page, f"Printed value missing: {value}"
    assert isclose(exp(log(2)), 2)
    assert isclose(exp(log(2) + log(3)), 6)
    assert isclose(exp(log(2) + 2*log(3)), 18)
    assert Fraction(6, 7) - Fraction(2, 3) == Fraction(4, 21)
    assert round(float(Fraction(4, 21)), 4) == 0.1905
    assert round(float(Fraction(18, 19)), 4) == 0.9474
    coef = (2.5949644, -0.0149475, 0.2092975)
    assert round(exp(coef[0]), 1) == 13.4
    assert round(exp(coef[1]), 3) == 0.985
    assert round(exp(10*coef[1]), 3) == 0.861
    assert round(exp(coef[2]), 3) == 1.233
    assert round(2**coef[2], 2) == 1.16
    assert round(1249.9/67) == 19
    assert 70-1 == 69 and 70-3 == 67
    assert isclose(2646.1-1249.9, 1396.2)
    for figure in ("links.png", "fish-scatterplots-2024.png", "fish-latitude-smooth-2024.png"):
        assert figure in page, f"Figure lost: {figure}"
    assert page.count('collapse="true" title="Proof"') == 1
    keys = set(re.findall(r'data-cite-key="([^"]+)"', page.split("## References")[0]))
    assert keys <= {"nelder_wedderburn1972", "sas2012_glm", "wood2025_mgcv_docs"}, keys
    print("generalised-linear-model printed values, figures, citations, and proof passed")
