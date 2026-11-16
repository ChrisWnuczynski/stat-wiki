"""Check Conway–Maxwell–Poisson series at lambda=1, nu=2."""
import math
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/conway-maxwell-poisson-distribution.qmd").read_text().split("## See also", 1)[0]
Z = sum(1/math.factorial(x)**2 for x in range(0, 40))
ps = [(1/math.factorial(x)**2)/Z for x in range(40)]
mean = sum(x*ps[x] for x in range(40))
var = sum((x-mean)**2 * ps[x] for x in range(40))
assert abs(Z - 2.2796) < 5e-5
assert abs(ps[0] - 0.4387) < 5e-5
assert abs(mean - 0.6978) < 5e-5
assert abs(var - 0.5131) < 5e-5
assert var < mean
assert abs(math.exp(-1) - 0.3679) < 5e-5
for s in ("2.2796", "0.4387", "0.6978", "0.5131", "0.3679"):
    assert s in body, s
assert "**Your turn.**" in body and "Check yourself" in body
assert body.count('title="Proof"') == 1
print("com-poisson passed")
