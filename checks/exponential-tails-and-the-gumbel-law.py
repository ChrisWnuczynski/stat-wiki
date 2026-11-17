"""Independent numerical and algebraic checks for exponential-tails-and-the-gumbel-law."""
import math
from pathlib import Path
import numpy as np


import sympy as sp
n,a=sp.symbols('n a',positive=True);assert sp.limit((1-a/n)**n,n,sp.oo)==sp.exp(-a)
b=math.log(100);gmed=-math.log(math.log(2));exact=-math.log1p(-.5**.01)
assert abs(b-4.605170186)<1e-9
assert abs(gmed-.3665129206)<1e-10
assert abs(b+gmed-4.97168310657)<1e-10
assert abs(exact-4.97514684059)<1e-10
assert abs((1-.01)**100-.3660323412732292)<1e-13
assert abs(math.exp(-1)-.3678794411714423)<1e-13
assert abs((b+gmed)/2-2.48584155328)<1e-10


root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "exponential-tails-and-the-gumbel-law.qmd").read_text()
source=(root / "research/content" / "exponential-tails-and-the-gumbel-law.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['4.971683', '4.975147', '0.366032', '2.485842']:
    assert token in body, (token, "exponential-tails-and-the-gumbel-law")
print("exponential-tails-and-the-gumbel-law: numerical and algebraic checks passed")
