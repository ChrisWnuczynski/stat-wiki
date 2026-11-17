"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

assert math.isclose(.6-.4,.2) and math.isclose(1-.2**2,.96)
assert round(math.sqrt(96),4)==9.7980
print('biased negative endpoint',stats.binom.cdf(49,100,.6))
assert round(stats.binom.cdf(49,100,.6),5)==.01676
assert round(math.sqrt(24),4)==4.8990 and math.isclose(.2*96,2*math.sqrt(.96*96))
assert round(stats.norm.sf(2),5)==.02275
print('symmetric exact tail',stats.binom.sf(60,100,.5))

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'drift-and-scale-of-a-random-walk'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

assert f"{math.sqrt(100*.96):.4f}" in worked_example
assert f"{stats.binom.cdf(49,100,.6):.5f}" in worked_example
assert f"{math.sqrt(25*.96):.4f}" in your_turn
horizon=(2*math.sqrt(.96)/.2)**2
assert f"n={horizon:.0f}" in your_turn
assert f"25(0.2)={25*.2:.0f}" in your_turn

print("drift-and-scale-of-a-random-walk: numerical checks passed")
