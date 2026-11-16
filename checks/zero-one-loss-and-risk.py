"""Check the zero–one risk calculations and preserved cost comparison."""

from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGE = (ROOT / "articles/zero-one-loss-and-risk.qmd").read_text()


def check_preserved_example() -> None:
    posterior = (F(7, 10), F(2, 10), F(1, 10))
    assert [1 - p for p in posterior] == [F(3, 10), F(8, 10), F(9, 10)]
    cost_one = posterior[1] * 5 + posterior[2]
    cost_two = posterior[0] + posterior[2]
    cost_three = posterior[0] + posterior[1] * 5
    assert (cost_one, cost_two, cost_three) == (F(11, 10), F(8, 10), F(17, 10))
    for token in ("(0.7,0.2,0.1)", "0.3", "0.8", "0.9", "1.1", "1.7"):
        assert token in PAGE, token


def check_new_example() -> None:
    pa, pb = F(4, 10), F(6, 10)
    qa, qb = F(8, 10), F(3, 10)
    bayes_risk = pa * (1 - qa) + pb * qb
    constant_risk = pa * qa + pb * qb
    assert bayes_risk == F(26, 100) and constant_risk == F(1, 2)
    pa, pb = F(2, 10), F(8, 10)
    qa, qb = F(75, 100), F(35, 100)
    bayes_risk = pa * (1 - qa) + pb * qb
    constant_risk = pa * qa + pb * qb
    assert (bayes_risk, constant_risk, constant_risk - bayes_risk) == (
        F(33, 100), F(43, 100), F(1, 10)
    )
    assert F(1, 100) + F(99, 100) == 1
    assert 1 - F(7, 10) == F(3, 10) and 1 - F(3, 10) == F(7, 10)
    for token in ("0.26", "0.50", "0.33", "0.43", "0.10", "99\\%", "0.01"):
        assert token in PAGE, token


def check_structure() -> None:
    for heading in (
        "## Motivating example",
        "## Definition",
        "## Worked example",
        "## Common misconceptions",
        "## Assumptions and limits",
        "## History",
    ):
        assert heading in PAGE, heading
    assert PAGE.count('title="Proof"') == 1
    assert "**Your turn.**" in PAGE
    for key in ("shalev_bendavid2014", "young_smith2005"):
        assert f'data-cite-key="{key}"' in PAGE, key
    for qid in ("ex-sl-08-1", "ex-sl-12-1", "ex-sl-12-2"):
        q = (ROOT / f"questions/{qid}.qmd").read_text()
        assert "## Worked answer" in q, qid


if __name__ == "__main__":
    check_preserved_example()
    check_new_example()
    check_structure()
    print("Zero–one risks, costs and answered bank items passed")
