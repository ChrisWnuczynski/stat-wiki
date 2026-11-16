"""Check central-limit examples, proof, figures, and question links."""

from math import comb, erf, exp, factorial, sqrt
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "central-limit-theorem.qmd").read_text()
body = page.split("## See also", 1)[0]

def phi(x):
    return (1 + erf(x / sqrt(2))) / 2

exact_binomial = sum(comb(20, j) for j in range(9)) / 2**20
plain_binomial = phi((8 - 10) / sqrt(5))
corrected_binomial = phi((8.5 - 10) / sqrt(5))
assert abs(exact_binomial - 0.2517) < 0.0001
assert abs(plain_binomial - 0.186) < 0.001
assert abs(corrected_binomial - 0.251) < 0.001

approx_total = 1 - phi((60 - 25 * 2) / (sqrt(25) * 2))
exact_total = exp(-30) * sum(30**j / factorial(j) for j in range(25))
approx_average = 1 - phi((2.5 - 2) / (2 / sqrt(36)))
assert abs(approx_total - 0.1587) < 0.0001
assert abs(exact_total - 0.1572) < 0.0001
assert abs(approx_average - 0.0668) < 0.0001

for printed in (
    "$25(2)=50$", "$\\sqrt{25(2^2)}=10$", "$(60-50)/10=1$",
    "$\\Pr\\{\\operatorname{Poisson}(30)\\le24\\}\\approx0.1572$",
    "$2/\\sqrt{36}=1/3$", "$(2.5-2)/(1/3)=1.5$",
    "$\\mathbb P(\\overline X_{36}>2.5)\\approx1-\\Phi(1.5)\\approx0.0668$",
    "$0.2517$", "=0.186,", "=0.251,",
):
    assert printed in body, f"Missing printed example value: {printed}"

assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and body.count('title="Answer"') >= 3
assert "## Motivating example" in body and "## Examples" in body
assert "## Check yourself" in body
assert "prob-clt.png" in page and "prob-binomial-normal.png" in page
for key in ("siegrist2022_clt", "cameron2004_asymptotic", "daw1966_normal_history"):
    assert f'data-cite-key="{key}"' in body, key
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", page))
assert len(questions) == 8, questions
assert {"ex-prob-clt-binomial-band", "ex-prob-voltage-mean"} <= questions
print("central-limit-theorem arithmetic, proof, figures, and links passed")
