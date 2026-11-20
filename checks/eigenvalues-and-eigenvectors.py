"""Check the eigenvalue examples and preserved page elements."""

from fractions import Fraction
from pathlib import Path
import re

page = (Path(__file__).resolve().parents[1] / "articles" / "eigenvalues-and-eigenvectors.qmd").read_text()
body = page.split("## See also", 1)[0]

assert (2 + 1, 2 - 1) == (3, 1)
assert (5 + 2, 5 - 2) == (7, 3)
assert Fraction(3, 3 + 1) == Fraction(3, 4)
assert Fraction(7, 7 + 3) == Fraction(7, 10)
assert 4 * 3 == 12 and 4 * 1 == 4

for printed in (
    r"(\lambda-3)(\lambda-1)=0$", r"$3/(3+1)=3/4=75\%$",
    r"$\sqrt{4(3)}=2\sqrt3$", r"$\sqrt{4(1)}=2$",
    r"(\lambda-7)(\lambda-3)$", r"$7/(7+3)=7/10=70\%$",
):
    assert printed in body, f"Missing printed example value: {printed}"

assert body.count('title="Proof"') == 1
assert body.count('title="Answer"') >= 1
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", page))
# Preserve the original exercises and the four independently migrated checks.
expected_questions = {
    "depth-gram-matrix-q1",
    "depth-loadings-q1",
    "depth-loadings-q2",
    "depth-principal-component-directions-and-scores-q1",
    "ex-sl-01-1",
    "ex-sl-01-4",
    "ex-sl-02-3",
    "ex-sl-02-7",
    "ex-sl-02-9",
    "ex-sl-03-1",
    "ex-sl-03-3",
    "ex-sl-03-4",
    "ex-sl-03-5",
    "ex-sl-03-7",
    "ex-sl-08-8",
    "ex-sl-17-5",
    "ex-sl-18-1",
    "ex-sl-18-2",
    "ex-ur-exchangeable-bound",
}
assert questions == expected_questions, questions ^ expected_questions
assert 'data-cite-key="strimmer2025_mva"' in body
print("eigenvalues-and-eigenvectors arithmetic, proof, and links passed")
