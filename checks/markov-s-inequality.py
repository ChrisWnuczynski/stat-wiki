"""Check Markov bounds, the indicator proof, and infinite-mean tails."""
from pathlib import Path
import math

from scipy.integrate import quad

root = Path(__file__).resolve().parents[1]
page = (root / "articles/markov-s-inequality.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 10 / 60 == 1 / 6
assert 25 / 50 ** 2 == 0.01
assert 4 / 20 == 0.2
assert 9 / 256 == 0.03515625
assert round(9 / 256, 4) == 0.0352
assert 6 / 15 == 0.4
assert 6 / 4 == 1.5
assert round(math.exp(-6), 6) == 0.002479
assert round(1 / 6, 4) == 0.1667

# The indicator comparison is an inequality, including above the threshold.
for a in (0.25, 1, 7):
    for x, expected_rhs in ((0, 0), (a / 2, 0), (a, a), (2 * a, a)):
        rhs = a * int(x >= a)
        assert rhs == expected_rhs
        assert x >= rhs
        assert (x == rhs) == (x in (0, a))

# X=b/U is finite for U in (0,1). Midpoints give exact proportions for
# these dyadic thresholds and independently check the stated survival law.
for b in (0.25, 1, 7):
    xs = [b / ((i + 0.5) / 4096) for i in range(4096)]
    assert all(math.isfinite(x) and x > b for x in xs)
    for multiple, expected in ((0.5, 1), (1, 1), (2, 0.5),
                               (4, 0.25), (16, 0.0625), (4096, 1 / 4096)):
        a = multiple * b
        tail = sum(x >= a for x in xs) / len(xs)
        assert tail == expected == min(1, b / a)

    # Each additional dyadic interval near zero contributes b*log(2).
    # This checks the improper-integral calculation, not a finite sample mean.
    previous = 0
    for k in range(1, 9):
        truncated_mean, _ = quad(lambda u: b / u, 2.0 ** -k, 1)
        assert math.isclose(truncated_mean, b * k * math.log(2), rel_tol=1e-10)
        assert math.isclose(truncated_mean - previous, b * math.log(2), rel_tol=1e-10)
        previous = truncated_mean

# Check the generated article, so either original error left unfixed fails.
proof = body.split('title="Proof"', 1)[1].split("\n## ", 1)[0]
assert r"a\,1_{\{X\ge a\}}=a\le X" in proof
assert "$X=2a$" in proof
assert "the two sides agree on" not in proof
limits = body.split("{#assumptions-and-limits}", 1)[1].split("\n## ", 1)[0]
for required in (
    "finite almost surely", "continuity from above",
    r"\mathrm{P}(X\ge a)\to 0", "fixed positive threshold",
    "uniform upper bound smaller than $1$", "$b>0$", "$X=b/U$",
    r"U\sim\operatorname{Uniform}(0,1)",
    r"\mathrm{E} X=b\int_0^1\frac{1}{u}\,du=\infty",
    r"\mathrm{P}(X\ge a)=\mathrm{P}(U\le b/a)=\min\{1,b/a\}",
    r"\mathrm{P}(X\ge b)=1", r"\mathrm{P}(X\ge 2b)=1/2",
):
    assert required in limits, required
assert r"\mathrm{P}(X\ge a)=1$ for every finite $a$" not in limits

assert round(1 - sum(math.exp(-2) * 2 ** k / math.factorial(k) for k in range(10)), 6) == 0.000046
for printed in ("1/6", "0.01", "0.2", "0.0352", "0.4", "1.5", "0.002479", "0.1667", "0.000046"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert 'data-cite-key="durrett2019"' in body
assert 'data-cite-key="dodge2008"' in body
print("markov inequality bounds, indicator proof, infinite-mean tails and practice passed")
