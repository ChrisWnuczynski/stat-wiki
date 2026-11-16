"""Verify FWER, Bonferroni calculations, and baseline material."""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/family-wise-error-rate.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/family-wise-error-rate.json").read_text())

assert round(1 - 0.95**10, 4) == 0.4013
assert round(1 - 0.995**10, 4) == 0.0489
assert round(1 - (1 - 0.05 / 4) ** 4, 4) == 0.0491
assert round(1 - 0.95**5, 4) == 0.2262
assert 0.05 / 5000 == 1e-5
assert [p for p in [0.004, 0.015, 0.030, 0.20] if p <= 0.05 / 4] == [0.004]
assert [p for p in [0.002, 0.009, 0.014, 0.070, 0.30] if p <= 0.05 / 5] == [0.002, 0.009]
assert 5 * 4 // 2 == 10 and 0.05 / 10 == 0.005
for printed in ("0.05", "0.4013", "0.0489", "5000", "10^{-5}", "0.004", "0.015", "0.030", "0.20", "0.0125", "0.0491", "0.002", "0.009", "0.014", "0.070", "0.30", "0.01", "0.2262"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "ex-inf-tukey-corn.qmd" in page and "ex-da-bonferroni.qmd" in page
assert page.count("![") >= json.loads((root / "research/baseline.json").read_text())["family-wise-error-rate"]["figures"]
for key in ("benjamini_hochberg1995", "nist_bonferroni2002", "dodge2008", "bonferroni1936", "hastie_esl2009"):
    assert f'data-cite-key="{key}"' in body, key
assert pending["self_checks"] == ["ex-sl-18-3", "ex-inf-tukey-corn"]
for slug in pending["self_checks"]:
    assert "## Worked answer" in (root / "questions" / f"{slug}.qmd").read_text()
print("FWER arithmetic and preservation passed")
