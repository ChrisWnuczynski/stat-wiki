"""Check all numerical skewness examples against the generated article."""

import csv
import math
from fractions import Fraction as F
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/skewness.qmd").read_text()
body = page.split("## See also", 1)[0]


def moment_skew(values):
    mean = sum(values) / len(values)
    m2 = sum((x - mean) ** 2 for x in values) / len(values)
    m3 = sum((x - mean) ** 3 for x in values) / len(values)
    return m3 / m2 ** 1.5


with (root / "sources/stat1301/data/heart.csv").open(newline="") as stream:
    serum = [float(row["serum_creatinine"]) for row in csv.DictReader(stream)]
assert len(serum) == 299
assert math.isclose(sum(serum) / len(serum), 1.3938795986622075)
assert sorted(serum)[149] == 1.1 and max(serum) == 9.4
assert round(moment_skew(serum), 1) == 4.4
assert round(moment_skew([math.log(x) for x in serum]), 1) == 1.6
assert abs(moment_skew([1 / x for x in serum])) < .01

# Five observations and the practice sample, using the n-divisor convention.
worked = [F(x) for x in (1, 2, 2, 3, 7)]
assert sum(worked) / 5 == 3
assert sum((x - 3) ** 2 for x in worked) / 5 == F(22, 5)
assert sum((x - 3) ** 3 for x in worked) / 5 == F(54, 5)
g1 = moment_skew(worked)
assert round(g1, 3) == 1.170
assert round(math.sqrt(20) * g1 / 3, 3) == 1.744
practice = [F(x) for x in (1, 1, 2, 4)]
assert sum(practice) / 4 == 2
assert sum((x - 2) ** 2 for x in practice) / 4 == F(3, 2)
assert sum((x - 2) ** 3 for x in practice) / 4 == F(3, 2)
assert round(moment_skew(practice), 4) == .8165
assert round(math.sqrt(12) * moment_skew(practice) / 2, 4) == 1.4142
assert round(math.sqrt(20) / 3, 2) == 1.49

# A zero-skew nonsymmetric law and a median transformation counterexample.
law = {F(-3): F(1, 20), F(-1): F(1, 2), F(1): F(1, 4), F(2): F(1, 5)}
assert sum(law.values()) == 1
assert sum(x * p for x, p in law.items()) == 0
assert sum(x ** 3 * p for x, p in law.items()) == 0
assert sum(x ** 2 * p for x, p in law.items()) > 0
assert law.get(F(3), 0) == 0
assert (F(1) + F(4)) / 2 == F(5, 2)
assert (F(1) + F(1, 4)) / 2 == F(5, 8)
assert 1 / F(5, 2) == F(2, 5)

for printed in (
    "299 observations", "$1.1$", "$9.4$", "$1.394$", "$4.4$", "$1.6$",
    "$n=5$", "$1.49$", "$-3,-1,1,2$", "$1/20,1/2,1/4,1/5$",
    "$2.5$", "=0.625", "=0.4$", "$1,2,2,3,7$", "$m_2=(4+1+1+0+16)/5=22/5=4.4$",
    "$m_3=(-8-1-1+0+64)/5=54/5=10.8$", "$g_1=(54/5)/(22/5)^{3/2}\\approx1.170$",
    "$G_1=\\sqrt{20}\\,g_1/3\\approx1.744$", "$1,1,2,4$", "\\approx0.8165", "\\approx1.4142",
):
    assert printed in body, f"Missing printed number {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
assert "../figures/da-creatinine-shape.png" in body
for qid in ("ex-da-correlation-reading", "ex-prob-ten-components"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="nist_skewness2002"' in body
print("skewness examples, source data, proof and practice passed")
