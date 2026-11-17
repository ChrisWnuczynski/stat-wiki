"""Check stationary MA arithmetic, counterexamples, and preserved Wold material."""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/stationarity-of-a-time-series.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = {'self_checks': json.loads((root / 'research/self-checks.json').read_text())['stationarity-of-a-time-series'], 'new_bank_questions': [next(q for q in json.loads((root / 'sources/depth-questions.json').read_text()) if q['id'] == qid) for qid in ['depth-stationarity-changing-laws']]}


def ma1(theta, variance):
    g0 = variance * (1 + theta * theta)
    g1 = variance * theta
    return g0, g1, g1 / g0, 2 * (g0 - g1)


assert ma1(0.5, 4) == (5, 2, 0.4, 6)
g0, g1, rho, diffvar = ma1(-0.25, 4)
assert (g0, g1, round(rho, 4), diffvar) == (4.25, -1, -0.2353, 10.5)
assert sum([0.5 * (-1), 0.5 * 1]) == 0
assert sum([0.5 * (-1) ** 2, 0.5 * 1 ** 2]) == 1
assert sum([0.25 * (-2**0.5) ** 2, 0.5 * 0, 0.25 * (2**0.5) ** 2]) == 1.0000000000000002
assert sum([0.25 * (-2**0.5), 0.25 * 2**0.5]) == 0
assert [4 * t for t in (1, 2, 5)] == [4, 8, 20]
for printed in ("0.5", "0.25", "0.4", "4.25", "-0.2353", "10.5", "4t", "2/5", "Wold decomposition"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "wold-decomposition.qmd" in page
assert page.count("![") >= json.loads((root / "research/baseline.json").read_text())["stationarity-of-a-time-series"]["figures"]
for key in ("hyndman_athanasopoulos2021", "pishro_nik2014", "horak_muller_vrbova1987", "dodge2008"):
    assert f'data-cite-key="{key}"' in body, key
for unread in ("wold1938", "brockwell_davis1991", "box_jenkins1970", "matheron1963", "yule1927", "khinchin1934"):
    assert f'data-cite-key="{unread}"' not in body
assert pending["self_checks"] == ["ex-sp-increments-and-levels", "ex-sp-same-marginals", "depth-stationarity-changing-laws"]
for slug in pending["self_checks"][:2]:
    assert "## Worked answer" in (root / "questions" / f"{slug}.qmd").read_text()
assert pending["new_bank_questions"][0]["topic_code"] == "T1"
assert pending["new_bank_questions"][0]["answer"]
proof_debt = json.loads((root / "proofs-todo.json").read_text())
assert any(item["slug"] == "wold-decomposition" for item in proof_debt)
print("stationarity arithmetic, preservation and Wold debt passed")
