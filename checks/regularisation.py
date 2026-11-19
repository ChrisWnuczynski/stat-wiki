"""Check the regularisation article's printed example, claims, and sources."""

from fractions import Fraction
from pathlib import Path
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/regularisation.md").read_text()
    page = (root / "articles/regularisation.qmd").read_text()
    body = page.split("## References", 1)[0]

    for match in re.finditer(r"\{\{cite:([^}]+)\}\}", prose):
        assert re.match(r" \((?:§|Summary|Abstract)", prose[match.end():]), match.group()
    for match in re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>', body, re.S):
        assert re.search(r'data-locator="[^"]+"', match.group(0)), match.group(0)[:220]

    for printed in (
        r"$\lambda=0$", r"$\lambda>0$", r"$\boldsymbol X^{\mathsf T}\boldsymbol X=I_p$",
        r"$\lambda=\sigma^2/\tau^2$", r"$\lambda=\sigma^2/b$",
        r"$\boldsymbol X=I_2$", r"$\boldsymbol y=(3,0.5)^{\mathsf T}$",
        r"$(3,0.5)^{\mathsf T}$", r"$\lambda=1$",
        r"$(3/2,0.5/2)^{\mathsf T}=(1.5,0.25)^{\mathsf T}$",
        r"$(3-1,\max(0.5-1,0))^{\mathsf T}=(2,0)^{\mathsf T}$",
    ):
        assert printed in body, f"Printed expression missing: {printed}"

    observed = (Fraction(3), Fraction(1, 2))
    assert tuple(v / 2 for v in observed) == (Fraction(3, 2), Fraction(1, 4))
    assert tuple(max(v - 1, 0) for v in observed) == (Fraction(2), Fraction(0))
    assert (Fraction(3, 2), Fraction(1, 4)) == (Fraction(15, 10), Fraction(25, 100))
    assert Fraction(1, 2) - 1 < 0 and Fraction(3) - 1 == 2

    assert page.count('collapse="true" title="Proof"') == 1
    questions = set(re.findall(r"\.\./questions/([^.)]+)", body))
    assert len(questions) >= 11
    assert {"ex-sl-16-3", "ex-sl-16-7", "depth-weight-update"} <= questions
    assert not re.search(r"!\[[^]]*\]\(", page)
    assert "{{cite:" not in page
    assert "the **regularisation**" not in body
    keys = set(re.findall(r'data-cite-key="([^"]+)"', body))
    assert keys <= {
        "hoerl_kennard1970", "tibshirani1996", "krogh_hertz1992",
        "loshchilov_hutter2019", "reinsch1967", "cawley_talbot2010",
    }, keys
    print("regularisation printed values, sources, links, and proof passed")
