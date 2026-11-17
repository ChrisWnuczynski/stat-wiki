"""Arithmetic for the memoryless-property depth pass."""
from math import exp
from pathlib import Path
from fractions import Fraction

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/memoryless-property.md").read_text(encoding="utf-8")
page = root / "articles/memoryless-property.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

assert abs(exp(-0.5) - 0.6065306597126334) < 1e-12
assert abs(exp(-3 / 8) - 0.6872892787909722) < 1e-12
assert abs(exp(-1) - 0.3678794411714423) < 1e-12
assert abs(exp(-3) - 0.04978706836786394) < 1e-12
assert (3 / 4) ** 4 == 81 / 256 == 0.31640625
assert (3 / 4) ** 6 == 729 / 4096
assert abs(729 / 4096 - 0.177978515625) < 1e-15
assert (1 - 0.25) / 0.25 == 3
assert 1 / 0.25 == 4

# Sum the point masses to distinguish the two integer-tail conventions.
p = Fraction(1, 4)
q = 1 - p
def trial_tail(k):
    return 1 - sum(p * q**(j - 1) for j in range(1, k + 1))

def failure_tail(k):
    return 1 - sum(p * q**j for j in range(k))

assert trial_tail(0) == 1 and trial_tail(1) == Fraction(3, 4)
for s in range(1, 7):
    assert trial_tail(s) == q**s  # P(X > s)
    assert trial_tail(s - 1) == q**(s - 1)  # P(X >= s)
    assert trial_tail(s - 1) - trial_tail(s) == p * q**(s - 1)
for r in range(4):
    for s in range(5):
        assert trial_tail(r + s) / trial_tail(r) == trial_tail(s)
        assert failure_tail(r + s) / failure_tail(r) == failure_tail(s)
assert "needing more than $s$ further trials" in prose
assert "needing more than $s$ further trials" in body
assert r"\Pr(K\ge r+s\mid K\ge r)=\Pr(K\ge s)" in prose

for printed in (
    "0.6065",
    "0.6873",
    "0.3679",
    "0.0498",
    "81/256",
    "0.31640625",
    "729/4096",
    "0.177978515625",
    "1000",
    "500",
    "30",
    "15",
):
    assert printed in prose, printed
    assert printed in body, printed

assert 'title="Proof"' in prose and prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose
assert prose.count('title="Answer"') == 4
assert "Check yourself" in prose
for key in ("grinstead_snell1997", "dodge2008"):
    assert f"{{{{cite:{key}}}}}" in prose
    assert f'data-cite-key="{key}"' in body
print("memoryless-property arithmetic passed")
