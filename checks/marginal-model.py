"""Verify marginal-risk, cluster-precision and Bernoulli-bound calculations."""

import json
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/marginal-model.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = {'self_checks': json.loads((root / 'research/self-checks.json').read_text())['marginal-model'], 'new_bank_questions': [next(q for q in json.loads((root / 'sources/depth-questions.json').read_text()) if q['id'] == qid) for qid in ['depth-marginal-risk-contrast', 'depth-marginal-bernoulli-bound', 'depth-marginal-working-covariance']], 'proofs_todo': [next(q for q in json.loads((root / 'proofs-todo.json').read_text()) if q['slug'] == qid) for qid in ['marginal-model#property-gee-robust-consistency']]}

control = [(0, 0), (0, 0), (1, 1), (0, 0)]
treated = [(1, 1), (1, 1), (0, 0), (1, 1)]
pc = sum(sum(pair) for pair in control) / 8
pt = sum(sum(pair) for pair in treated) / 8
assert (pc, pt, pt - pc) == (0.25, 0.75, 0.5)
odds_ratio = (pt / (1 - pt)) / (pc / (1 - pc))
assert odds_ratio == 9
assert round(math.log(odds_ratio), 4) == 2.1972


def sample_variance(values):
    mean = sum(values) / len(values)
    return sum((v - mean) ** 2 for v in values) / (len(values) - 1)


c_means = [sum(pair) / 2 for pair in control]
t_means = [sum(pair) / 2 for pair in treated]
assert c_means == [0, 0, 1, 0] and t_means == [1, 1, 0, 1]
assert sample_variance(c_means) == sample_variance(t_means) == 0.25
cluster_se = math.sqrt(sample_variance(c_means) / 4 + sample_variance(t_means) / 4)
naive_se = math.sqrt(pc * (1 - pc) / 8 + pt * (1 - pt) / 8)
assert round(cluster_se, 4) == 0.3536
assert round(naive_se, 4) == 0.2165
assert cluster_se > naive_se

treated_changed = treated.copy()
treated_changed[0] = (1, 0)
pt_changed = sum(sum(pair) for pair in treated_changed) / 8
assert pt_changed == 5 / 8 == 0.625
assert pt_changed - pc == 3 / 8 == 0.375
assert math.isclose((pt_changed / (1 - pt_changed)) / (pc / (1 - pc)), 5)

pa, pb = 0.2, 0.8
joint_max = min(pa, pb)
cov_max = joint_max - pa * pb
sd_product = math.sqrt(pa * (1 - pa) * pb * (1 - pb))
assert math.isclose(cov_max, 0.04)
assert math.isclose(sd_product, 0.16)
assert math.isclose(cov_max / sd_product, 0.25)
assert 0.6 > cov_max / sd_product

for printed in ("1986", "$2/8=0.25$", "$6/8=0.75$", "$0.50$", "$9$", "2.1972", "$0.25$", "0.3536", "0.2165", "$5/8=0.625$", "$0.625-0.25=0.375$", "0.2", "0.8", "0.04", "0.16", "$0.6$"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert page.count("![") >= json.loads((root / "research/baseline.json").read_text())["marginal-model"]["figures"]
for key in ("liang_zeger1986",):
    assert f'data-cite-key="{key}"' in body, key
assert 'data-cite-key="zeger_liang_albert1988"' not in body
for slug in ("c-38", "c-40"):
    assert f"{slug}.qmd" in page
assert pending["self_checks"] == [item["id"] for item in pending["new_bank_questions"]]
assert all(item["answer"] and item["topic_code"] == "C3" for item in pending["new_bank_questions"])
assert pending["proofs_todo"][0]["slug"] == "marginal-model#property-gee-robust-consistency"
print("marginal risk, uncertainty, feasibility and preservation passed")
