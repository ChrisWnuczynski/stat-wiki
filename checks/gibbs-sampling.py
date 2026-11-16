"""Check Gibbs-sweep fractions, inherited examples, and page structure."""

from fractions import Fraction
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "gibbs-sampling.qmd").read_text()
body = page.split("## See also", 1)[0]

joint = {
    (0, 0): Fraction(3, 10),
    (0, 1): Fraction(1, 10),
    (1, 0): Fraction(1, 5),
    (1, 1): Fraction(2, 5),
}
assert sum(joint.values()) == 1

def x_given_y(x, y):
    return joint[x, y] / sum(joint[a, y] for a in (0, 1))

def y_given_x(y, x):
    return joint[x, y] / sum(joint[x, b] for b in (0, 1))

forward = x_given_y(1, 0) * y_given_x(1, 1)
reverse = x_given_y(0, 1) * y_given_x(0, 0)
assert x_given_y(1, 0) == Fraction(2, 5)
assert y_given_x(1, 1) == Fraction(2, 3)
assert forward == Fraction(4, 15)
assert x_given_y(0, 1) == Fraction(1, 5)
assert y_given_x(0, 0) == Fraction(3, 4)
assert reverse == Fraction(3, 20)
assert forward != joint[1, 1]

# One X-then-Y sweep leaves the joint target invariant.
for x1 in (0, 1):
    for y1 in (0, 1):
        mass = sum(
            joint[x0, y0] * x_given_y(x1, y0) * y_given_x(y1, x1)
            for x0 in (0, 1) for y0 in (0, 1)
        )
        assert mass == joint[x1, y1]

for printed in (
    "$\\pi(0,0)=3/10$", "$\\pi(0,1)=1/10$",
    "$\\pi(1,0)=1/5$", "$\\pi(1,1)=2/5$",
    "=2/5", "=2/3", "=4/15", "=1/5", "=3/4", "=3/20",
    "\\pi(x_1,x_2)\\propto", "e^{-x_1x_2-x_1-x_2}",
):
    assert printed in body, f"Missing printed value: {printed}"

assert "## Motivating example" in body
assert "**Your turn.**" in body
assert body.count('title="Proof"') == 1
assert body.count('title="Answer"') >= 3
assert "## Check yourself" in body
assert "part1-fig-04-gibbs-staircase.png" in page
for key in ("geyer2005_markov_chain", "gelfand_smith1990"):
    assert f'data-cite-key="{key}"' in body, key
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", page))
assert {"q-04", "q-09", "q-59", "q-26"} <= questions
print("gibbs-sampling sweep fractions, proof, figure, and links passed")
