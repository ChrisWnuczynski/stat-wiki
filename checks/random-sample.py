"""Check the random-sample page's printed arithmetic and preserved material."""

from fractions import Fraction
from pathlib import Path
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/random-sample.md").read_text()
    assert "the iid assumption fails and a model with a batch effect is needed" in prose
    page = (root / "articles/random-sample.qmd").read_text()
    for match in re.finditer(r"\{\{cite:([^}]+)\}\}", prose):
        assert re.match(r" \((?:§|pp\.|p\.)", prose[match.end():]), (
            f"Citation without location: {match.group()}"
        )
    for value in (
        r"$p=1/4$", r"$(x_1,x_2,x_3,x_4)=(1,0,1,0)$",
        r"$\bar x=2/4=1/2$", r"$s^2=\{2(1-1/2)^2+2(0-1/2)^2\}/3=1/3$",
        r"$(1/4)^2(3/4)^2=9/256$", r"$\binom42(9/256)=27/128$",
        r"$\mathbb E\bar X=p=1/4$", r"$\operatorname{Var}(\bar X)=p(1-p)/4=3/64$",
        r"$3/16$", r"$\sigma^2/n$", r"$\chi^2_{n-1}$",
    ):
        assert value in page, f"Printed value missing: {value}"
    p = Fraction(1, 4)
    x = [1, 0, 1, 0]
    mean = Fraction(sum(x), len(x))
    assert mean == Fraction(1, 2)
    assert sum((Fraction(v)-mean)**2 for v in x)/3 == Fraction(1, 3)
    assert p**2*(1-p)**2 == Fraction(9, 256)
    assert 6*p**2*(1-p)**2 == Fraction(27, 128)
    assert p*(1-p)/4 == Fraction(3, 64)
    assert p*(1-p) == Fraction(3, 16)
    assert page.count('collapse="true" title="Proof"') == 1
    assert len(set(re.findall(r"\.\./questions/([^.)]+)", page))) == 13
    assert not re.search(r"!\[[^\]]*\]\(", page)
    keys = set(re.findall(r'data-cite-key="([^"]+)"', page.split("## References")[0]))
    assert keys <= {
        "siegrist2022_random_samples", "siegrist2022_sample_variance",
        "siegrist2022_normals", "fisher1922", "nelder_wedderburn1972",
        "statistics_canada2003_survey",
    }, keys
    print("random-sample printed values, question links, citations, and proof passed")
