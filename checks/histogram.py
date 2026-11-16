"""Check the histogram's bin arithmetic, scales, figure and question proposals."""

import json
from fractions import Fraction as F
from math import pi, sqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGE = (ROOT / "articles/histogram.qmd").read_text()
BANK = json.loads((ROOT / "sources/depth-questions.json").read_text())
SELECTED = json.loads((ROOT / "research/self-checks.json").read_text())["histogram"]
PENDING = {"new_bank_questions": [q for q in BANK if q["id"] in SELECTED], "self_checks": SELECTED}


def counts(values, edges):
    return [sum(a <= x < b for x in values) for a, b in zip(edges, edges[1:])]


def check_worked_example() -> None:
    values = [F(2, 10), F(4, 10), F(8, 10), F(11, 10), F(12, 10), F(14, 10),
              F(18, 10), F(21, 10), F(24, 10), F(26, 10), F(30, 10), F(57, 10)]
    assert len(values) == 12
    c = counts(values, [0, 1, 2, 3, 4, 5, 6])
    assert c == [3, 4, 3, 1, 0, 1]
    density = [F(k, 12) for k in c]
    assert density == [F(1, 4), F(1, 3), F(1, 4), F(1, 12), 0, F(1, 12)]
    assert sum(density) == 1
    assert counts(values, [0, 2, 4, 6]) == [7, 4, 1]
    wide_density = [F(k, 24) for k in (7, 4, 1)]
    assert [round(float(x), 4) for x in wide_density] == [0.2917, 0.1667, 0.0417]
    assert sum(2 * x for x in wide_density) == 1
    for token in ("3,4,3,1,0,1", "0.3333", "0.0833", "7,4,1", "0.2917", "0.1667", "0.0417"):
        assert token in PAGE, token


def check_turn_and_bank() -> None:
    turn = [F(2, 10), F(6, 10), F(9, 10), F(11, 10), F(14, 10), F(18, 10), F(22, 10), F(36, 10)]
    assert counts(turn, [0, 1, 2, 4]) == [3, 3, 2]
    heights = [F(3, 8), F(3, 8), F(2, 16)]
    assert heights == [F(375, 1000), F(375, 1000), F(125, 1000)]
    assert heights[0] + heights[1] + 2 * heights[2] == 1
    assert counts([F(9, 10), F(11, 10), F(19, 10), F(21, 10)], [0, 1, 2, 3]) == [1, 2, 1]
    assert counts([F(9, 10), F(11, 10), F(19, 10), F(21, 10)], [F(-1, 2), F(1, 2), F(3, 2), F(5, 2)]) == [0, 2, 2]

    questions = PENDING["new_bank_questions"]
    assert [q["id"] for q in questions] == PENDING["self_checks"]
    assert all(q["topic_code"] == "D2" and q["body"] and q["answer"] for q in questions)
    bank_one = questions[0]
    assert F(6, 10) / F(2, 10) == 3 and F(4, 10) / F(8, 10) == F(1, 2)
    assert 3 * F(2, 10) == F(6, 10) and F(1, 2) * F(8, 10) == F(4, 10)
    assert "height $3$" in bank_one["answer"] or "Height $3$" in bank_one["answer"]
    bank_two = questions[1]
    bank_values = [F(4, 10), F(6, 10), F(14, 10), F(16, 10), F(24, 10)]
    assert counts(bank_values, [0, 1, 2, 3]) == [2, 2, 1]
    assert counts(bank_values, [F(-1, 2), F(1, 2), F(3, 2), F(5, 2)]) == [1, 2, 2]
    assert "(2,2,1)" in bank_two["answer"] and "(1,2,2)" in bank_two["answer"]


def check_sources_and_structure() -> None:
    scott_constant = (24 * sqrt(pi)) ** (1 / 3)
    assert abs(scott_constant - 3.49) < 0.001
    p, n, width = F(1, 4), 20, F(1, 2)
    assert p / width == F(1, 2)
    assert p * (1 - p) / (n * width**2) == F(3, 80)
    assert F(20, 100) / 2 == F(200, 1000) / 2 == F(1, 10)
    assert "3.49" in PAGE
    assert (ROOT / "figures/da-creatinine-shape.pdf").is_file()
    source = (ROOT / "sources/stat1301/chapters/da-02-descriptive-statistics.qmd").read_text()
    assert "299 patients" in source and "1.10" in source and "9.40" in source and "da-creatinine-shape.pdf" in source
    assert "299 patients" in PAGE and "9" in PAGE
    assert "1.10" in PAGE and "9.40" in PAGE and "0.20/2=0.10" in PAGE
    assert PAGE.count("![") == 1
    assert 'fig-alt="Three panels' in PAGE
    assert PAGE.count('title="Proof"') == 1 and "**Your turn.**" in PAGE
    for heading in ("## Motivating example", "## Definition", "## Properties", "## Worked example",
                    "## Statistical use", "## Common misconceptions", "## Assumptions and limits", "## History"):
        assert heading in PAGE, heading
    for key in ("nist_histogram", "scott1979_histograms", "numpy_histogram_bins",
                "dodge2008", "chicco_jurman2020", "r_histogram_classes"):
        assert f'data-cite-key="{key}"' in PAGE, key


if __name__ == "__main__":
    check_worked_example()
    check_turn_and_bank()
    check_sources_and_structure()
    print("Histogram counts, density areas, source figure and bank questions passed")
