"""Check the numerical pooling and conditional shrinkage calculations."""
from math import isclose
from pathlib import Path

assert (4*80+25*68)/29 == 2020/29
assert isclose(2020/29, 69.66, abs_tol=0.005)
assert 4*25/(100+4*25) == .5
assert .5*80+.5*70 == 75
w = 25*25/(100+25*25)
assert isclose(w, .86207, abs_tol=5e-6)
assert isclose(w*68+(1-w)*70, 68.28, abs_tol=.005)
assert 9*25/(100+9*25) == 9/13
assert isclose(9/13, .69231, abs_tol=5e-6)
assert isclose(70+72/13, 75.54, abs_tol=.005)
assert 100*25/(100+9*25) == 100/13
assert isclose(100/13, 7.69, abs_tol=.005)
root = Path(__file__).resolve().parents[1]
source = (root / "research/content/complete-pooling-no-pooling-and-partial-pooling.md").read_text()
for number in ("2020/29", "69.66", "625/725", "0.86207", "68.28", "9/13", "75.54", "7.69"):
    assert number in source
page = root / "articles/complete-pooling-no-pooling-and-partial-pooling.qmd"
if page.exists():
    rendered = page.read_text()
    for preserved in ("Complete pooling", "No pooling", "Partial pooling", "../questions/exr-pooling.qmd", "../questions/q-23.qmd"):
        assert preserved in rendered
