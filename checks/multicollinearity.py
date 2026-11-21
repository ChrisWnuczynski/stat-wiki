"""Arithmetic for the multicollinearity depth pass."""

import sys
import json
import re
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
from math import sqrt

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/multicollinearity.md").read_text(encoding="utf-8")
prose = shown(prose, "multicollinearity")
page = root / "articles/multicollinearity.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

s11, s22, s12 = 10, 50, 22
assert s12 ** 2 / (s11 * s22) == 0.968
r = s12 / (s11 * s22) ** 0.5
assert round(r, 4) == 0.9839
assert abs(1 / (1 - 0.968) - 31.25) < 1e-12
assert round(sqrt(31.25), 3) == 5.590
det = s11 * s22 - s12 ** 2
assert det == 16
# responses
s1y, s2y = 7, 17
b1 = (s1y * s22 - s2y * s12) / det
b2 = (s2y * s11 - s1y * s12) / det
assert b1 == -1.5 and b2 == 1
assert s1y / s11 == 0.7
assert 10 * 40 - 20 ** 2 == 0
assert 1 / (1 - 0.36) == 1.5625

for printed in ("0.968", "0.9839", "31.25", "5.590", "-1.5", "0.7", "1.5625", "0.032"):
    assert printed in prose, printed
    assert printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
assert "{{cite:dodge2008}}" in prose

# Recompute the separate self-check designs from their actual question givens.
questions = {q["id"]: q for q in json.loads((root / "sources/depth-questions.json").read_text(encoding="utf-8"))}

def vector(question, name):
    match = re.search(re.escape(name) + r"=\(([^)]+)\)", question["body"])
    assert match, (question["id"], name)
    return [Fraction(v.strip()) for v in match.group(1).split(",")]

def cross(a, b):
    assert len(a) == len(b)
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b))

q1, q2, q3 = [questions[f"depth-multicollinearity-q{i}"] for i in (1, 2, 3)]
a, b = vector(q1, "x_1"), vector(q1, "x_2")
e11, e22, e12 = cross(a, a), cross(b, b), cross(a, b)
assert (e11, e22, e12) == (10, 34, 18)
assert e11 * e22 - e12 ** 2 == 16  # Full rank with an intercept.
er2 = e12 ** 2 / (e11 * e22)
assert er2 == Fraction(81, 85)
assert 1 - er2 == Fraction(4, 85) and 1 / (1 - er2) == Fraction(85, 4)
assert "1-r^2=4/85" in q1["answer"] and "85/4=21.25" in q1["answer"]

a2, b2_exact = vector(q2, "x_1"), vector(q2, "x_2")
assert "intercept" in q2["body"]
assert all(v == 3 * u + 2 for u, v in zip(a2, b2_exact))
assert cross(a2, a2) * cross(b2_exact, b2_exact) - cross(a2, b2_exact) ** 2 == 0
assert "(b_0-2t,b_1-3t,b_2+t)" in q2["answer"]
for u, v in zip(a2, b2_exact):
    assert 1 + 2 * u + 3 * v == (1 - 2 * 7) + (2 - 3 * 7) * u + (3 + 7) * v

a3, b3, y3 = [vector(q3, name) for name in ("x_1", "x_2", "y")]
assert (a3, b3) == (a, b)
e1y, e2y = cross(a3, y3), cross(b3, y3)
assert (e1y, e2y) == (2, 2)
simple = e1y / e11
partial = (e22 * e1y - e12 * e2y) / (e11 * e22 - e12 ** 2)
assert simple == Fraction(1, 5) and partial == 2
assert "2/10=0.2" in q3["answer"] and "(34\\cdot2-18\\cdot2)/16=2" in q3["answer"]
for printed in ("21.25", "4/85", "2/10=0.2", "b_0-2t"):
    assert printed in prose and printed in body, printed
authored = (root / "research/content/multicollinearity.md").read_text(encoding="utf-8")
for distinct in ("(2,5,6,7,10)", "(5,8,11,14,17)", "(4,3,4,5,4)", "21.25", "2/10=0.2", "b_0-2t"):
    assert distinct not in authored, distinct
print("multicollinearity arithmetic passed")
