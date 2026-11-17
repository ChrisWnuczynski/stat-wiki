"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

z=1.96
assert round(z*z/(20+z*z),4)==.1611
assert round(1-.025**(1/20),4)==.1684
assert round(z*z/(10+z*z),4)==.2775
p1=55/160;p2=60/192;d=p1-p2;se=math.sqrt(p1*(1-p1)/160+p2*(1-p2)/192)
assert d==.03125 and round(se,6)==.050288
assert round(d-z*se,4)==-.0673 and round(d+z*se,4)==.1298
assert round(p1,3)==.344 and round(p2,3)==.312
assert round(math.sqrt(.344*.656/160+.313*.688/192),4)==.0503

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'interval-for-a-proportion'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

assert f"{z*z/(20+z*z):.4f}" in worked_example
assert f"{1-.025**(1/20):.4f}" in worked_example
assert f"={z*z/(10+z*z):.4f}" in your_turn
assert f"{d-z*se:.3f}" in article and f"{d+z*se:.3f}" in article

print("interval-for-a-proportion: numerical checks passed")
