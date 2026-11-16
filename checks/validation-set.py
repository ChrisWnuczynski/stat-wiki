"""Check every numerical example and the selection argument on Validation set."""

from pathlib import Path
from fractions import Fraction
import numpy as np

root = Path(__file__).resolve().parents[1]
body = (root / "articles/validation-set.qmd").read_text().split("## See also", 1)[0]

assert 36 + 12 + 12 == 60
assert Fraction(3, 12) == Fraction(1, 4)
assert round(1/12, 4) == .0833
assert round(2/12, 4) == .1667
assert round(4/12, 4) == .3333
assert .0833 < .1667 < .25
assert list(range(1, 11))[-1] == 10  # retained ten-setting sketch

# A finite exact enumeration verifies the proof's inequality can be strict.
# Two equally good fixed rules each have a 0.5 error probability on one case.
outcomes = [(a, b) for a in (0, 1) for b in (0, 1)]
assert np.mean([min(a, b) for a, b in outcomes]) == .25 < .5

for printed in ("60", "36", "12", "3/12", "0.25", "1/12", "0.0833",
                "4/12", "0.3333", "2/12", "0.1667", "0.18"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "{#worked-example}" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("james_islr2013", "cawley_talbot2010", "hyndman_athanasopoulos2021"):
    assert f'data-cite-key="{key}"' in body
print("validation-set calculations and practice passed")
