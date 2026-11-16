"""Check interaction contrasts, inherited data examples, and page structure."""

import csv
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "interaction.qmd").read_text()
body = page.split("## See also", 1)[0]


def contrast(cells):
    m00, m10, m01, m11 = cells
    return m11 - m01 - m10 + m00


worked = (10, 14, 12, 21)
practice = (8, 11, 13, 20)
assert contrast(worked) == 5
assert worked[1] - worked[0] == 4
assert worked[3] - worked[2] == 9
assert worked[2] - worked[0] == 2
assert worked[3] - worked[1] == 7
assert [10 + 4 * a + 2 * b + 5 * a * b for a, b in ((0, 0), (1, 0), (0, 1), (1, 1))] == list(worked)
assert 10 + 4 + 2 == 16
assert contrast(practice) == 4
assert practice[1] - practice[0] == 3
assert practice[3] - practice[2] == 7
assert practice[2] - practice[0] == 5
assert [8 + 3 * a + 5 * b + 4 * a * b for a, b in ((0, 0), (1, 0), (0, 1), (1, 1))] == list(practice)
assert 8 + 3 + 5 == 16

for printed in (
    "$\\mu_{00}=10$", "$\\mu_{10}=14$", "$\\mu_{01}=12$", "$\\mu_{11}=21$",
    "$14-10=4$", "$21-12=9$", "$9-4=5$", "$12-10=2$", "$21-14=7$",
    "$10+4A+2B+5AB$", "predict 16 rather than 21",
    "$\\mu_{00}=8$", "$\\mu_{10}=11$", "$\\mu_{01}=13$", "$\\mu_{11}=20$",
    "$11-8=3$", "$20-13=7$", "$7-3=4$", "$13-8=5$",
    "8+3A+5B+4AB", "$8+3+5=16$",
):
    assert printed in body, f"Missing worked or practice value: {printed}"

# Recalculate the wheat table using the 36 values printed in the inherited R example.
match = re.search(r"yield <- c\((.*?)\)\s*fertilizer <-", body, re.S)
assert match
values = [float(x) for x in re.findall(r"\d+\.\d+", match.group(1))]
assert len(values) == 36
cells = [[[values[f * 12 + r * 3 + k] for k in range(3)] for r in range(4)] for f in range(3)]
mean = lambda xs: sum(xs) / len(xs)
grand = mean(values)
fert = [mean([v for row in cells[f] for v in row]) for f in range(3)]
region = [mean([v for f in range(3) for v in cells[f][r]]) for r in range(4)]
cell_means = [[mean(cells[f][r]) for r in range(4)] for f in range(3)]
ss_region = 9 * sum((v - grand) ** 2 for v in region)
ss_fert = 12 * sum((v - grand) ** 2 for v in fert)
ss_inter = 3 * sum((cell_means[f][r] - fert[f] - region[r] + grand) ** 2 for f in range(3) for r in range(4))
ss_error = sum((v - cell_means[f][r]) ** 2 for f in range(3) for r in range(4) for v in cells[f][r])
assert abs(ss_region - 29.340) < .001
assert abs(ss_fert - 8.560) < .001
assert abs(ss_inter - .695) < .001
assert abs(ss_error - 20.885) < .001
assert abs((ss_inter / 6) / (ss_error / 24) - .1332) < .0001
assert abs((ss_inter + ss_error) / 30 - .719) < .001
assert [round(x, 2) for x in (region[0], region[3], *fert)] == [8.70, 10.96, 9.91, 10.61, 9.42]
for printed in ("29.340", "8.560", "0.695", "20.885", "0.1332", "$F=0.13$", "$0.719$", "8.70", "10.96", "10.61"):
    assert printed in body, printed

# The crop table is displayed only as rounded means, so check the printed simple effects.
assert [round(yes - no, 2) for no, yes in zip((3.20, 2.87, 5.70), (6.77, 9.01, 8.16))] == [3.57, 6.14, 2.46]
for printed in ("| No pesticide | 3.20 | 2.87 | 5.70 |", "| Pesticide | 6.77 | 9.01 | 8.16 |", "$3.57$", "$6.14$", "$2.46$", "$F=574$"):
    assert printed in body, printed

# Independently solve the four normal equations for the inherited birth-weight model.
rows = list(csv.DictReader((root / "sources/stat1301/data/birthwt.csv").open()))
assert len(rows) == 189
data = [([1., float(r["age"]), float(r["smoke"]), float(r["age"]) * float(r["smoke"])], float(r["bwt"])) for r in rows]
aug = [[sum(x[i] * x[j] for x, _ in data) for j in range(4)] + [sum(x[i] * y for x, y in data)] for i in range(4)]
for i in range(4):
    pivot = max(range(i, 4), key=lambda k: abs(aug[k][i]))
    aug[i], aug[pivot] = aug[pivot], aug[i]
    scale = aug[i][i]
    aug[i] = [v / scale for v in aug[i]]
    for j in range(4):
        if j != i:
            scale = aug[j][i]
            aug[j] = [v - scale * w for v, w in zip(aug[j], aug[i])]
coef = [row[-1] for row in aug]
assert all(abs(a - b) < .0005 for a, b in zip(coef, (2406.058, 27.731, 798.175, -46.572)))
assert abs(coef[1] + coef[3] - (-18.8)) < .05
for printed in ("2406.058", "27.731", "798.175", "-46.572", "$p=0.024$", "$27.73-46.57=-18.8$"):
    assert printed in body, printed

assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and body.count('title="Answer"') >= 3
assert body.count('title="Proof"') == 1 and "## Check yourself" in body
assert "da-interaction.png" in page and "da-birthwt-interaction.png" in page
for key in ("nist_interactions2002", "nist_two_way_anova2002", "dodge2008"):
    assert f'data-cite-key="{key}"' in body, key
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", page))
assert {"q-39", "q-40"} <= questions
print("interaction contrasts, inherited data, figures, and links passed")
