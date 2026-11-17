"""Checks for the feature-selection research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/feature-selection.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/feature-selection.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
headings = [
    "## Lead context",
    "## Motivating example",
    "## Intuition",
    "## Definition",
    "## Properties",
    "## Statistical use",
    "## Worked example",
    "## Common misconceptions",
    "## Assumptions and limits",
    "## Connections",
    "## History",
]
positions = [prose.index(heading) for heading in headings]
assert positions == sorted(positions)
assert "**Your turn.**" in prose
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    prose,
    re.S,
)
assert answer and "{{cite:" not in answer.group(1)
assert "## Check yourself" not in prose
checks = pending["self_checks"]
assert 2 <= len(checks) <= 3
assert all("{{cite:" not in item["answer"] for item in checks)

cases = ((0, 0, 1), (1, 0, 1), (2, 1, 3))
mean_y = Fraction(sum(y for _, _, y in cases), 3)
assert mean_y == Fraction(5, 3)
rss_intercept = sum((Fraction(y) - mean_y) ** 2 for _, _, y in cases)
assert rss_intercept == Fraction(8, 3)

# Least squares of y on x with an intercept: slope 1, intercept 2/3.
fitted_x = [Fraction(2, 3) + x for x, _, _ in cases]
rss_x = sum((Fraction(y) - fit) ** 2 for (_, _, y), fit in zip(cases, fitted_x))
assert rss_x == Fraction(2, 3)

# The line 1 + 2z fits every case.
fitted_z = [1 + 2 * z for _, z, _ in cases]
rss_z = sum((Fraction(y) - fit) ** 2 for (_, _, y), fit in zip(cases, fitted_z))
assert rss_z == 0
assert rss_z < rss_x < rss_intercept

assert 2 ** 20 == 1_048_576
assert 1 + 20 * 21 // 2 == 211
assert "8/3" in prose and "2/3" in prose and r"1{,}048{,}576" in prose and "211" in prose
print("feature-selection checks passed")
