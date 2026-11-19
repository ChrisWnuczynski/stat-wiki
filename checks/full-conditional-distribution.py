"""Check the full-conditional article's printed arithmetic and Gibbs claims."""

from fractions import Fraction
from pathlib import Path
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/full-conditional-distribution.md").read_text()
    page = (root / "articles/full-conditional-distribution.qmd").read_text()
    body = page.split("## References", 1)[0]

    for match in re.finditer(r"\{\{cite:[^}]+\}\}", prose):
        assert re.match(r" \((?:§|Abstract)", prose[match.end():]), match.group()
    for match in re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>', body, re.S):
        assert re.search(r'data-locator="[^"]+"', match.group(0)), match.group(0)[:220]

    for printed in (
        r"$\pi(0,0\mid y)=2/5$", r"$\pi(0,1\mid y)=1/10$",
        r"$\pi(1,0\mid y)=1/5$", r"$\pi(1,1\mid y)=3/10$",
        r"$\Pr(X=0\mid Z=0,y)=(2/5)/(3/5)=2/3$",
        r"$\Pr(X=1\mid Z=0,y)=1/3$",
        r"$\Pr(Z=1\mid X=0,y)=(1/10)/(1/2)=1/5$",
        r"$(2/3)(1/5)=2/15$",
        r"$\pi(0,1\mid y)=1/10$",
    ):
        assert printed in body, f"Printed value missing: {printed}"

    joint = {
        (0, 0): Fraction(2, 5), (0, 1): Fraction(1, 10),
        (1, 0): Fraction(1, 5), (1, 1): Fraction(3, 10),
    }
    assert sum(joint.values()) == 1
    assert joint[0, 0] + joint[1, 0] == Fraction(3, 5)
    assert joint[0, 0] + joint[0, 1] == Fraction(1, 2)
    assert joint[0, 0] / Fraction(3, 5) == Fraction(2, 3)
    assert joint[1, 0] / Fraction(3, 5) == Fraction(1, 3)
    assert joint[0, 1] / Fraction(1, 2) == Fraction(1, 5)
    assert Fraction(2, 3) * Fraction(1, 5) == Fraction(2, 15)
    assert joint[0, 1] == Fraction(1, 10) != Fraction(2, 15)

    assert page.count('collapse="true" title="Proof"') == 1
    assert "{{cite:" not in page
    assert len(set(re.findall(r"\.\./questions/([^.)]+)", body))) == 23
    assert not re.search(r"!\[[^]]*\]\(", page)
    keys = set(re.findall(r'data-cite-key="([^"]+)"', body))
    assert keys <= {
        "geman_geman1984", "gelfand_smith1990", "geyer2005_markov_chain", "chen_ip2015",
    }, keys
    print("full-conditional printed values, citations, links, and proof passed")
