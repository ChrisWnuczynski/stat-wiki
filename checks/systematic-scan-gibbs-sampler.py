"""Check systematic-scan transitions and preserved article elements."""

from fractions import Fraction
from pathlib import Path
import re

page = (Path(__file__).resolve().parents[1] / "articles" / "systematic-scan-gibbs-sampler.qmd").read_text()
body = page.split("## See also", 1)[0]

pi = {(0, 0): Fraction(1, 2), (0, 1): Fraction(1, 6),
      (1, 0): Fraction(1, 12), (1, 1): Fraction(1, 4)}
assert sum(pi.values()) == 1

def x_given_z(x, z):
    return pi[x, z] / sum(pi[u, z] for u in (0, 1))

def z_given_x(z, x):
    return pi[x, z] / sum(pi[x, u] for u in (0, 1))

assert x_given_z(0, 0) == Fraction(6, 7)
assert z_given_x(1, 0) == Fraction(1, 4)
assert x_given_z(0, 0) * z_given_x(1, 0) == Fraction(3, 14)
assert z_given_x(1, 1) == Fraction(3, 4)
assert x_given_z(0, 1) == Fraction(2, 5)
assert z_given_x(1, 1) * x_given_z(0, 1) == Fraction(3, 10)
assert x_given_z(1, 0) * z_given_x(1, 1) == Fraction(3, 28)
assert z_given_x(1, 0) * x_given_z(1, 1) == Fraction(3, 20)

for printed in (
    r"$\pi(0,0)=1/2$", r"$\pi(1,1)=1/4$",
    r"$(6/7)(1/4)=3/14$", r"$(3/4)(2/5)=3/10$",
    r"$(1/7)(3/4)=3/28$", r"$(1/4)(3/5)=3/20$",
):
    assert printed in body, f"Missing printed example value: {printed}"

assert body.count('title="Proof"') == 1
assert body.count('title="Answer"') >= 1
assert "part1-fig-04-gibbs-staircase.png" in body
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", page))
assert len(questions) == 21, f"Expected 21 question links, got {len(questions)}"
print("systematic-scan-gibbs-sampler arithmetic, proof, figure, and links passed")
