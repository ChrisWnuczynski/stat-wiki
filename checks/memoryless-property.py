"""Arithmetic for the memoryless-property depth pass."""
from math import exp
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/memoryless-property.md").read_text(encoding="utf-8")
page = root / "articles/memoryless-property.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

assert abs(exp(-0.5) - 0.6065306597126334) < 1e-12
assert abs(exp(-3 / 8) - 0.6872892787909722) < 1e-12
assert abs(exp(-1) - 0.3678794411714423) < 1e-12
assert abs(exp(-3) - 0.04978706836786394) < 1e-12
assert (3 / 4) ** 4 == 81 / 256 == 0.31640625
assert (3 / 4) ** 6 == 729 / 4096
assert abs(729 / 4096 - 0.177978515625) < 1e-15
assert (1 - 0.25) / 0.25 == 3
assert 1 / 0.25 == 4

for printed in (
    "0.6065",
    "0.6873",
    "0.3679",
    "0.0498",
    "81/256",
    "0.31640625",
    "729/4096",
    "0.177978515625",
    "1000",
    "500",
    "30",
    "15",
):
    assert printed in prose, printed
    assert printed in body, printed

assert 'title="Proof"' in prose and prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose
assert prose.count('title="Answer"') == 4
assert "Check yourself" in prose
for key in ("grinstead_snell1997", "dodge2008"):
    assert f"{{{{cite:{key}}}}}" in prose
    assert f'data-cite-key="{key}"' in body
print("memoryless-property arithmetic passed")
