"""Arithmetic for the Pareto depth pass."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/pareto-distribution.md").read_text(encoding="utf-8")
page = root / "articles/pareto-distribution.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

assert abs(2.5 / 1.5 - 5 / 3) < 1e-12
assert abs(2.5 / (1.5 ** 2 * 0.5) - 20 / 9) < 1e-12
assert round(5 / 3, 4) == 1.6667
assert round(20 / 9, 4) == 2.2222
assert round(2 ** 0.4, 4) == 1.3195
assert round(2 ** (-2.5), 4) == 0.1768
assert abs(4 * 2 / 3 - 8 / 3) < 1e-12
assert round(8 / 3, 4) == 2.6667
assert (2 / 4) ** 4 == 1 / 16 == 0.0625
assert 1.5 / 0.5 == 3

for printed in ("1.6667", "2.2222", "1.3195", "0.1768", "2.6667", "0.0625", "20/9"):
    assert printed in prose, printed
    assert printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "Check yourself" in prose
assert prose.count('title="Answer"') == 4
assert "{{cite:scipy_pareto2026}}" in prose
print("pareto-distribution arithmetic passed")
