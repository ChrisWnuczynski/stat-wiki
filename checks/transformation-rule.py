"""Verify the transformation examples and preserved source calculations."""
import math
from pathlib import Path

assert 1/6 * (1/2) == 1/12
assert math.isclose(1/12, 0.08333, abs_tol=5e-6)
assert 1/(2*3) == 1/6
assert (4*1+5, 4*3+5) == (9, 17)
assert 1/2 * 1/4 == 1/8
assert (13-9)/8 == 1/2
assert math.isclose(math.gamma(0.5), math.sqrt(math.pi))
assert (1**2-4, 3**2-4) == (-3, 5)
assert math.isclose((math.sqrt(5+4)-1)/2, 1)
assert math.isclose(math.gamma(2), 1)  # integral of u exp(-u)
assert math.isclose((4**2-2**2)/4**2, 3/4)
assert math.isclose((4**2)/(16), 1)  # integral of r/8 from zero to four

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/transformation-rule.md").read_text()
for value in ("1/6", "1/12", "0.08333", "1/8", "1/2", "(9,17)"):
    assert value in prose, value
page = root / "articles/transformation-rule.qmd"
if page.exists():
    body = page.read_text()
    for preserved in ("Box–Muller", "Gamma}(2,1)", "0<v<1", "square of a standard normal",
                      r"16\pi", r"4\pi", "3/4", "r/8", "-3<y<5"):
        assert preserved.lower() in body.lower(), preserved
