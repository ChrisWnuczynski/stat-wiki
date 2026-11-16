"""Recompute Bayes-rule examples and check the printed article values."""

from fractions import Fraction
from pathlib import Path
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    source = (root / "research/content/bayes-rule.md").read_text()
    page = (root / "articles/bayes-rule.qmd").read_text()
    for match in re.finditer(r"\{\{cite:[^}]+\}\}", source):
        assert re.match(r" \((?:Ch\.|§|pp\.|p\.)", source[match.end():]), (
            f"Citation without location: {match.group()}"
        )
    printed = (
        r"$1\%$", r"$90\%$", r"$5\%$", r"$10{,}000$",
        r"$100$", r"$90$", r"$9{,}900$", r"$495$",
        r"\frac{90}{90+495}=\frac{2}{13}\approx0.1538",
        r"$0.90$", r"$0.154$", r"$99$",
        r"90/(90+99)=10/21\approx0.4762",
        r"80/100=0.8", r"\mathbb{P}(\theta>1/2\mid{\boldsymbol{x}})=0",
    )
    for value in printed:
        assert value in page, f"Printed value missing: {value}"
    prevalence = Fraction(1, 100)
    sensitivity = Fraction(9, 10)
    cohort = 10_000
    true_cases = prevalence * cohort
    noncases = cohort - true_cases
    true_positives = true_cases * sensitivity
    false_positives = noncases * Fraction(5, 100)
    posterior = true_positives / (true_positives + false_positives)
    assert (true_cases, noncases, true_positives, false_positives) == (100, 9900, 90, 495)
    assert posterior == Fraction(2, 13)
    assert round(float(posterior), 4) == 0.1538
    assert round(float(posterior), 3) == 0.154
    improved_false_positives = noncases * Fraction(1, 100)
    assert improved_false_positives == 99
    assert true_positives / (true_positives + improved_false_positives) == Fraction(10, 21)
    assert round(float(Fraction(10, 21)), 4) == 0.4762
    assert Fraction(80, 100) == Fraction(4, 5)
    assert page.count('collapse="true" title="Proof"') == 1
    keys = set(re.findall(r'data-cite-key="([^"]+)"', page.split("## References")[0]))
    opened = {"bayes1763", "wang2025_foundations", "hoff2013_bayes_estimators", "kass_raftery1995"}
    assert keys <= opened, f"Article cites unreviewed sources: {keys - opened}"
    for line in page.splitlines():
        if '<li id="cite_note-' in line:
            assert "cite-backlink" in line, f"Uncited bibliography item: {line[:100]}"
    print("bayes-rule printed values, arithmetic, citations, and proof passed")
