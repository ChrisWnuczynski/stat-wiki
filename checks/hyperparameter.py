"""Verify numerical hierarchy examples and preserved page material."""

from fractions import Fraction as Q
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "hyperparameter.qmd").read_text()
body = page.split("## See also", 1)[0]

def beta_mean(a, b, y, n):
    return Q(a + y, a + b + n)


# New two-clinic illustration and practice calculation.
assert Q(2, 2 + 3) == Q(2, 5)
assert beta_mean(2, 3, 1, 4) == Q(3, 9) == Q(1, 3)
assert beta_mean(2, 3, 16, 40) == Q(18, 45) == Q(2, 5)
assert Q(5, 9) * Q(2, 5) + Q(4, 9) * Q(1, 4) == Q(1, 3)
assert Q(5, 45) == Q(1, 9)
assert beta_mean(1, 4, 2, 5) == Q(3, 10)
assert Q(1, 2) * Q(1, 5) + Q(1, 2) * Q(2, 5) == Q(3, 10)

# Inherited current-study and q-23 values.
assert 14 - 4 == 10
assert beta_mean(2, 8, 4, 10) == Q(6, 20) == Q(3, 10)
assert beta_mean(2, 8, 40, 100) == Q(42, 110) == Q(21, 55)
assert Q(2, 10) == Q(1, 5)
assert Q(10, 20) == Q(1, 2)
assert Q(10, 110) == Q(1, 11)
assert round(float(Q(42, 110)), 4) == .3818

for printed in (
    "$2/5=0.4$", "$1/4$", "$3/9=1/3$", "$18/45=0.4$",
    "$5/9$", "$5/45=1/9$", "$1/5=0.2$", "$3/10=0.3$",
    "$5/10=1/2$", "$(1/2)(0.2)+(1/2)(2/5)=0.3$",
    "$y=4$ of $n=14$", "70 earlier control studies", "0.3818",
    "10/20=1/2", "10/110=1/11",
):
    assert printed in body, f"Missing printed number {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
assert "## Properties" in body and "Marginal hyperposterior" in body
assert "Rat-tumour hierarchy" in body and "Rat-tumour studies and hierarchical shrinkage" in body
for qid in ("q-02", "c-02"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="gelman_bda2013"' in body
print("hyperparameter calculations, examples, sources and practice passed")
