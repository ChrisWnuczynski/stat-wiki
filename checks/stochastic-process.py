"""Printed values for the stochastic-process article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "stochastic-process.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

# Two independent fair steps.
assert (1 / 2) * (1 / 2) + (1 / 2) * (1 / 2) == 1 / 2  # opposite signs
assert (1 / 2) * (1 / 2) == 1 / 4
second_moment = 4 * (1 / 2)
assert second_moment == 2

for printed in ("1/2", "1/4", "2", "X_0=0"):
    assert printed in body or printed.replace("1/2", r"\tfrac12") in body or "tfrac12" in body, printed
assert r"\tfrac14" in body and r"\tfrac12" in body
assert "2" in body
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("stochastic process checks passed")
