"""Recalculate the discrete-law examples and assert their printed values."""

from fractions import Fraction as Q
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "discrete-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

# Ordered dice have a nonuniform sum and a nonuniform minimum.
pairs = [(a, b) for a in range(1, 7) for b in range(1, 7)]
assert len(pairs) == 36
sum_counts = {z: sum(a + b == z for a, b in pairs) for z in range(2, 13)}
assert [sum_counts[z] for z in range(2, 13)] == [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
assert Q(sum_counts[7], 36) == Q(1, 6)
assert Q(sum_counts[2], 36) == Q(1, 36)
min_counts = [sum(min(a, b) == z for a, b in pairs) for z in range(1, 7)]
assert min_counts == [11, 9, 7, 5, 3, 1]
assert sum(Q(z * n, 36) for z, n in enumerate(min_counts, 1)) == Q(91, 36)

# Three independent inspections, each with defect probability 1/4.
pmf = [Q(27, 64), Q(27, 64), Q(9, 64), Q(1, 64)]
assert sum(pmf) == 1
assert Q(3, 1) * Q(1, 4) ** 2 * Q(3, 4) == Q(9, 64)
assert sum(pmf[2:]) == Q(5, 32)
assert sum(pmf[:2]) == Q(27, 32)
assert sum(x * p for x, p in enumerate(pmf)) == Q(3, 4)

# Two independent trials, each with success probability 1/3.
practice = [Q(4, 9), Q(4, 9), Q(1, 9)]
assert sum(practice) == 1
assert sum(practice[1:]) == Q(5, 9)
assert sum(x * p for x, p in enumerate(practice)) == Q(2, 3)

for printed in (
    "$6/36$", "$1/36$", "$p_X(0)=27/64$", "$p_X(1)=27/64$",
    "$p_X(2)=9/64$", "$p_X(3)=1/64$", "$3(3/64)=9/64$",
    "$(9+1)/64=5/32$", "$F_X(1)=(27+27)/64=27/32$",
    "$3(1/4)=3/4$", "$(27+2\\cdot9+3)/64=3/4$",
    "$p_Y(0)=(2/3)^2=4/9$", "$p_Y(1)=2(1/3)(2/3)=4/9$",
    "$p_Y(2)=(1/3)^2=1/9$", "4/9+1/9=5/9$", "(4+2)/9=2/3$",
    "(6-|z-7|)/36$", ")/36=91/36$",
):
    assert printed in body, f"Missing printed value {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
assert "prob-discrete-pmfs.png" in page
assert "prob-02-random-variables-distribution-function.png" in page
for qid in ("ex-prob-wait-pmf", "ex-prob-joint-table"):
    assert f"../questions/{qid}.qmd" in page
for key in ("durrett2019", "grinstead_snell1997"):
    assert f'data-cite-key="{key}"' in body
print("discrete-distribution values, figures, sources and practice passed")
