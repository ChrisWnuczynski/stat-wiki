"""Check the exponential-family article's displayed examples and notation."""

from fractions import Fraction
from math import exp, factorial, isclose, log
from pathlib import Path
import json
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/exponential-family.md").read_text()
    page = (root / "articles/exponential-family.qmd").read_text()
    body = page.split("## References", 1)[0]
    todo = json.loads((root / "proofs-todo.json").read_text())

    for match in re.finditer(r"\{\{cite:([^}]+)\}\}", prose):
        assert re.match(r" \((?:§|Summary|Introduction|Ch\.)", prose[match.end():]), match.group()
    for match in re.finditer(r'<sup[^>]*data-cite-key="([^"]+)"[^>]*>.*?</sup>', body, re.S):
        assert re.match(r"\s*\((?:§|Ch\.|Summary|Details|Sec\.|p\.|pp\.|Introduction)", body[match.end():]), match.group(1)

    for printed in (
        r"$\eta=\theta/e(\phi)$", r"$A(\eta)=-c(\theta)/e(\phi)$",
        r"$\eta=\mu/\sigma^2$", r"$\eta=\log\lambda$",
        r"$A(\eta)=e^\eta$", r"$A(\eta)=n\log(1+e^\eta)$",
        r"$S=1+0+2+1=4$", r"$\lambda^4e^{-4\lambda}$",
        r"$\hat\lambda=S/4=1$", r"$\lambda^{2-1}e^{-\lambda}$",
        r"$2+4=6$", r"$1+4=5$", r"$6/5=1.2$",
        r"$d\lambda/d\eta=\lambda$", r"$\alpha=2$", r"$\nu=1$",
        r"$\alpha'=2+4=6$", r"$\nu'=1+4=5$",
        r"$e^{\beta_1}$", r"$100(e^{\beta_1}-1)\%$",
    ):
        assert printed in body, f"Printed expression missing: {printed}"

    counts = (1, 0, 2, 1)
    total = sum(counts)
    assert total == 4 and len(counts) == 4
    assert Fraction(total, len(counts)) == 1
    assert (2 + total, 1 + len(counts)) == (6, 5)
    assert Fraction(6, 5) == Fraction(12, 10)
    assert round(6 / 5, 1) == 1.2
    assert isclose(exp(log(2)), 2.0)
    assert isclose((exp(log(2)) ** total) * exp(-4 * 2) / factorial(1) / factorial(0) / factorial(2) / factorial(1), 8 * exp(-8))
    assert 2 * Fraction(5, 100) == Fraction(10, 100)
    assert 2 * Fraction(51, 100) > 1
    assert (3 * 2, 6 * 2) == (6, 12)

    assert page.count('collapse="true" title="Proof"') == 1
    assert r"\nabla_c\log a" not in body
    assert r"\beta\leftarrow\beta+n" not in body
    assert r"\mathbf X_i" not in body.split("## Check yourself", 1)[0]
    assert "{{cite:" not in body
    assert not re.search(r"!\[[^\]]*\]\(", page)
    assert len(set(re.findall(r"\.\./questions/([^.)]+)", body))) == 7
    keys = set(re.findall(r'data-cite-key="([^"]+)"', body))
    assert keys <= {
        "nelder_wedderburn1972", "diaconis_ylvisaker1979",
        "geyer2022_exp_family", "geyer2025_conjugate",
        "sas2012_glm", "siegrist2020_poisson_process", "rstats_family2026",
        "brown1964_sufficiency", "gelman_bda2013",
    }, keys
    assert {"diaconis_ylvisaker1979", "brown1964_sufficiency"} <= keys
    assert any(x["slug"] == "exponential-family#property-pitman-koopman-darmois-informal-form" for x in todo)
    print("exponential-family printed values, symbols, citations, preservation, and proof passed")
