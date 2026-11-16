"""Check the median article's printed examples and proof."""

from fractions import Fraction
from pathlib import Path
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/median.md").read_text()
    page = (root / "articles/median.qmd").read_text()
    for match in re.finditer(r"\{\{cite:([^}]+)\}\}", prose):
        assert re.match(r" \((?:§|p\.)", prose[match.end():]), (
            f"Citation without location: {match.group()}"
        )
    for value in (
        r"$\tilde x=x_{(k+1)}$", r"$[x_{(k)},x_{(k+1)}]$",
        r"$\tilde x=\{x_{(k)}+x_{(k+1)}\}/2$",
        r"$m\in[0,1]$", r"$F_X(m-)\le1/2\le F_X(m)$",
        r"$5$", r"$(2+4+5+8+100)/5=119/5=23.8$", r"$1019/5=203.8$",
        r"$3+1+0+3+95=102$", r"$2+0+1+4+96=103$",
        r"$(4+8)/2=6$", r"$4+2+2+94=102$",
        r"$2+0+4+96=102$",
    ):
        assert value in page, f"Printed value missing: {value}"
    odd = [2, 4, 5, 8, 100]
    assert sorted(odd)[2] == 5
    assert Fraction(sum(odd), 5) == Fraction(119, 5)
    assert Fraction(sum([2, 4, 5, 8, 1000]), 5) == Fraction(1019, 5)
    assert sum(abs(x-5) for x in odd) == 102
    assert sum(abs(x-4) for x in odd) == 103
    even = [2, 4, 8, 100]
    assert Fraction(even[1]+even[2], 2) == 6
    assert sum(abs(x-6) for x in even) == sum(abs(x-4) for x in even) == 102
    assert page.count('collapse="true" title="Proof"') == 1
    assert len(set(re.findall(r"\.\./questions/([^.)]+)", page))) == 5
    assert not re.search(r"!\[[^\]]*\]\(", page)
    keys = set(re.findall(r'data-cite-key="([^"]+)"', page.split("## References")[0]))
    assert keys <= {
        "nist_location2002", "siegrist2022_quantiles", "siegrist2022_order_statistics",
        "siegrist2022_sample_variance", "schwertman_gilks_cameron1990",
    }, keys
    print("median printed values, question links, citations, and proof passed")
