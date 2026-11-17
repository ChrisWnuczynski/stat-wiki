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
assert len(questions) == 15, f"Expected 15 question links, got {len(questions)}"
assert 'data-cite-key="golub_vanloan2013"' in body
print("eigenvalues-and-eigenvectors arithmetic, proof, and links passed")
