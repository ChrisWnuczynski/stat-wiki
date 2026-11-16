"""Check multinomial probabilities and moments."""
import math
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/multinomial-distribution.qmd").read_text().split("## See also", 1)[0]

def multi(n, xs, ps):
    c = math.factorial(n)
    for x in xs:
        c //= math.factorial(x)
    pr = c
    for x, p in zip(xs, ps):
        pr *= p**x
    return pr
assert abs(multi(3, [1,1,1], [0.5, 1/3, 1/6]) - 1/6) < 1e-12
assert abs(multi(3, [3,0,0], [0.5, 1/3, 1/6]) - 1/8) < 1e-12
assert abs(multi(10, [2,3,5], [0.2, 0.3, 0.5]) - 0.08505) < 1e-10
assert 3*(1/2)*(1/2) == 0.75
assert -3*(1/2)*(1/3) == -0.5
assert 3*(1/6) == 0.5
for s in ("1/6", "0.08505", "1/8"):
    assert s in body, s
assert "**Your turn.**" in body and "Check yourself" in body
assert 'data-cite-key="dodge2008"' in body
assert body.count('title="Proof"') == 1
print("multinomial passed")
