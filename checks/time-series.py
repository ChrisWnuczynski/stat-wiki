"""Arithmetic for the time-series depth pass."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/time-series.md").read_text(encoding="utf-8")
page = root / "articles/time-series.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

ys = [123, 39, 78, 52, 110]
assert sum(ys) == 402 and sum(ys) / 5 == 80.4
m = 80.4
devs = [y - m for y in ys]
num = sum(devs[i] * devs[i - 1] for i in range(1, 5))
den = sum(d * d for d in devs)
assert abs(num - (-2436.76)) < 1e-9
assert abs(den - 5217.2) < 1e-9
assert abs(num / den - (-0.4671)) < 5e-5
ordered = [39, 52, 78, 110, 123]
od = [y - m for y in ordered]
num2 = sum(od[i] * od[i - 1] for i in range(1, 5))
assert abs(num2 - 2433.84) < 1e-9
assert abs(num2 / den - 0.4665) < 5e-5

phi = 0.5
g0 = 1 / (1 - phi ** 2)
assert abs(g0 - 4 / 3) < 1e-12
s = (3 / 4) * (1 / 2) + (1 / 2) * (1 / 4) + (1 / 4) * (1 / 8)
assert abs(s - 0.53125) < 1e-12
factor = 1 + 2 * s
assert factor == 2.0625
assert abs((g0 / 4) * factor - 0.6875) < 1e-12
assert (1 + phi) / (1 - phi) == 3
path = []
x = 0
for e in (1, -1, 0, 2):
    x += e
    path.append(x)
assert path == [1, 0, 0, 2]
assert -1 / 2 == -0.5

for printed in (
    "80.4", "-0.4671", "0.4665", "0.6875", "2.0625", "0.3333",
    "1.3333", "-2436.76", "5217.2", "2433.84",
):
    assert printed in prose, printed
    assert printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
for key in ("hyndman_athanasopoulos2021", "dodge2008"):
    assert f"{{{{cite:{key}}}}}" in prose
print("time-series arithmetic passed")
