"""Check Bonferroni levels, dependence, and the generated interpretation."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import math
import re

root = Path(__file__).resolve().parents[1]
page = (root / "articles/bonferroni-correction.qmd").read_text()
body = page.split("## See also", 1)[0]


def section(rendered, ident):
    match = re.search(
        rf"^## [^\n]*\{{#{ident}\}}\n(.*?)(?=^## |\Z)",
        rendered, re.M | re.S,
    )
    assert match, f"missing generated section: {ident}"
    # The generator can link terms; keep the visible words and TeX intact.
    text = re.sub(r"\[([^\]\n]+)\]\([^\n)]+\)", r"\1", match[1])
    return " ".join(text.split())


def check_dependence_and_fdr(rendered):
    interpretation = section(rendered, "interpretation")
    for claim in (
        "all $m$ nulls are true",
        "the error events are independent",
        r"$\mathbb{P}(A_j)=\alpha/m$ for every $j$",
        r"the family-wise error is $1-(1-\alpha/m)^m$",
        r"A level bound $\mathbb{P}(A_j)\le\alpha/m$ alone does not give this equality",
        "Pairwise positive association alone does not order the family-wise error against independence",
        "With valid true-null $p$-values",
        r"$\mathrm{FWER}\le\alpha$ under arbitrary dependence",
    ):
        assert claim in interpretation, f"interpretation missing: {claim}"
    assert "Positive dependence makes the union smaller still" not in interpretation

    # Read the law from its explanation in this section, not unrelated numbers
    # elsewhere in the article. Fractions avoid simulation and rounding errors.
    masses = re.search(
        r"assign probability \$(0\.\d+)\$ to each of the four singleton-rejection outcomes, "
        r"\$(0\.\d+)\$ to the outcome where all four reject, and "
        r"\$(0\.\d+)\$ to no rejections", interpretation,
    )
    assert masses, "missing four-null probability law in interpretation"
    assert "All other outcomes have probability zero" in interpretation
    singleton, all_four, none = map(Fraction, masses.groups())
    assert (singleton, all_four, none) == tuple(map(Fraction, ("0.01234", "0.00016", "0.95048")))
    law = {frozenset({j}): singleton for j in range(4)}
    law[frozenset(range(4))] = all_four
    law[frozenset()] = none
    assert all(mass >= 0 for mass in law.values()) and sum(law.values()) == 1
    marginals = [sum(mass for outcome, mass in law.items() if j in outcome) for j in range(4)]
    alpha = Fraction("0.05")
    assert marginals == [alpha / 4] * 4
    for i, j in combinations(range(4), 2):
        joint = sum(mass for outcome, mass in law.items() if {i, j} <= outcome)
        assert joint == Fraction("0.00016")
        assert marginals[i] * marginals[j] == Fraction("0.00015625") < joint
    fwer = sum(mass for outcome, mass in law.items() if outcome)
    independent = 1 - math.prod(1 - marginal for marginal in marginals)
    assert fwer == Fraction("0.04952")
    assert independent == Fraction("0.0490702880859375")
    assert independent < fwer <= sum(marginals) == alpha
    for calculation in (
        r"$\mathbb{P}(A_j)=0.01234+0.00016=0.0125$",
        r"$\mathbb{P}(A_i\cap A_j)=0.00016>0.0125^2=0.00015625$",
        r"$\mathrm{FWER}=4\times0.01234+0.00016=0.04952$",
        r"$1-(0.9875)^4\approx0.049070288$",
    ):
        assert calculation in interpretation, f"interpretation missing calculation: {calculation}"

    limits = section(rendered, "assumptions-and-limits")
    for claim in (
        "$V$ count false rejections and $R$ count all rejections",
        r"$\mathrm{FDP}=V/R$ when $R>0$ and $0$ when $R=0$",
        r"$\mathrm{FDR}=\mathbb{E}(\mathrm{FDP})$",
        r"$\mathrm{FDP}\le\mathbf{1}_{\{V>0\}}$",
        r"$\mathrm{FDR}\le\mathbb{P}(V>0)=\mathrm{FWER}\le\alpha$",
        "different error targets",
    ):
        assert claim in limits, f"limits missing: {claim}"
    assert "It does not control the false discovery rate" not in limits
    for rejected in range(5):
        for false in range(rejected + 1):
            fdp = Fraction(false, rejected) if rejected else Fraction(0)
            assert fdp <= int(false > 0)
    # In this all-true-null example, FDR equals FWER, including the no-rejection outcome.
    fdr = sum(mass * (Fraction(len(outcome), len(outcome)) if outcome else 0)
              for outcome, mass in law.items())
    assert fdr == fwer


check_dependence_and_fdr(body)

assert 0.05 / 4 == 0.0125
assert abs(1 - 0.95 ** 4 - 0.18549375) < 1e-8
assert round(1 - 0.95 ** 4, 4) == 0.1855
assert round(1 - 0.9875 ** 4, 4) == 0.0491
assert round(1 - math.exp(-0.05), 4) == 0.0488
assert min(1, 4 * 0.02) == 0.08 and min(1, 4 * 0.01) == 0.04
assert min(1, 6 * 0.01) == 0.06
assert abs(4 * 0.0125 - 0.05) < 1e-12

for printed in ("0.1855", "0.0125", "0.0491", "0.0488", "0.08", "0.04", "0.06"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert body.count("![") >= 1
for key in ("hastie_esl2009", "dodge2008", "durrett2019"):
    assert f'data-cite-key="{key}"' in body
print("bonferroni levels, dependence, FDR, and practice passed")
