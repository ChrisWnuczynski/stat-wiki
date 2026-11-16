"""Check Markov and Chebyshev numbers, including the exponential tail."""
from pathlib import Path
import math

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

assert round(1 - sum(math.exp(-2) * 2 ** k / math.factorial(k) for k in range(10)), 6) == 0.000046
for printed in ("1/6", "0.01", "0.2", "0.0352", "0.4", "1.5", "0.002479", "0.1667", "0.000046"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert 'data-cite-key="durrett2019"' in body
assert 'data-cite-key="dodge2008"' in body
print("markov inequality bounds and practice passed")
