"""Arithmetic for the Fisher-scoring depth pass."""
from math import exp, log
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/fisher-scoring.md").read_text(encoding="utf-8")
page = root / "articles/fisher-scoring.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

a = exp(2)
assert abs(a - 7.38905609893065) < 1e-12
assert round(a, 4) == 7.3891
b1 = 1 + 3 / a
assert abs(b1 - 1.406005849709838) < 1e-12
assert round(b1, 4) == 1.4060
assert round(exp(b1), 4) == 4.0796
assert round(log(3), 4) == 1.0986
assert abs(exp(log(3)) - 3) < 1e-12

for printed in ("7.3891", "1.4060", "4.0796", "1.0986", "2"):
    assert printed in prose, printed
    assert printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
assert "{{cite:rstats_glm2026}}" in prose
print("fisher-scoring arithmetic passed")
