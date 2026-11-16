"""Numerical identities printed in the survival-function article."""
import math
from pathlib import Path

s = math.exp(-1)
assert abs(s - 0.367879) < 5e-7
assert abs(s*s - 0.135335) < 5e-7
assert abs(1 - (1-s)**2 - 0.600424) < 5e-7
assert 1 / 0.02 == 50
assert abs(0.72 / 0.9 - 0.8) < 1e-12
assert abs(0.9 - 0.72 - 0.18) < 1e-12
assert abs(0.5/0.8 - 0.625) < 1e-12
assert abs(3*0.9**2 - 2*0.9**3 - 0.972) < 1e-12
assert math.isclose(math.log(2), 0.69, abs_tol=0.004)
assert 2-0.5 == 1.5 and 1.5-2/3 == 5/6
assert math.isclose(1-(1-0.9**2)**2, 0.964, abs_tol=0.0002)
assert 20/1000 == 1/50

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/survival-function.md").read_text()
for printed in ("0.367879", "0.135335", "0.600424", "0.625", "0.18", "0.8"):
    assert printed in prose
page_path = root / "articles/survival-function.qmd"
if page_path.exists():
    page = page_path.read_text()
    for preserved in ("prob-system-survival.png", "0.972", "1000 hours", "$50$ hours", r"\frac5{6\lambda}"):
        # The generated page includes numbers from the chapter and its linked examples.
        assert preserved in page, preserved
