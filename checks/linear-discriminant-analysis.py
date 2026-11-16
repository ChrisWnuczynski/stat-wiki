"""Check both the retained LDA calculation and the researched extension."""

from math import exp, log, sqrt
from pathlib import Path
import numpy as np

root = Path(__file__).resolve().parents[1]
body = (root / "articles/linear-discriminant-analysis.qmd").read_text().split("## See also", 1)[0]

# Retained two-class example from the original source chapter.
a = np.array([(3, 3), (1, 1), (3, 2), (1, 2)], dtype=float)
b = np.array([(6, 5), (4, 3), (6, 4), (4, 4)], dtype=float)
mu1, mu2 = a.mean(0), b.mean(0)
assert np.array_equal(mu1, [2, 2]) and np.array_equal(mu2, [5, 4])
scatter = (a - mu1).T @ (a - mu1)
assert np.array_equal(scatter, [[4, 2], [2, 2]])
sigma = (scatter + (b-mu2).T @ (b-mu2)) / 6
assert np.allclose(sigma, [[4/3, 2/3], [2/3, 2/3]])
assert np.isclose(np.linalg.det(sigma), 4/9)
inverse = np.linalg.inv(sigma)
assert np.allclose(inverse, [[1.5, -1.5], [-1.5, 3]])
beta = inverse @ (mu1-mu2)
alpha = -.5 * (mu1 @ inverse @ mu1 - mu2 @ inverse @ mu2)
assert np.allclose(beta, [-1.5, -1.5]) and np.isclose(alpha, 9.75)
x = np.array([5, 1.4])
assert np.isclose(x.sum(), 6.4) and alpha + x @ beta > 0
assert np.isclose(3*x[0]+2*x[1], 17.8)
assert np.isclose((x-mu1) @ inverse @ (x-mu1), 19.98)
assert np.isclose((x-mu2) @ inverse @ (x-mu2), 20.28)
assert np.isclose(np.linalg.eigvalsh(sigma)[-1], 1+sqrt(5)/3)
assert np.isclose((sqrt(5)-1)/2, .61803398875)

# Separate one-dimensional prior example and its hidden answer.
boundary = 1 + .5*log(4)
assert round(boundary, 6) == 1.693147
def posterior(x, pi1=.8, pi2=.2):
    f1 = exp(-x*x/2)
    f2 = exp(-(x-2)**2/2)
    return pi2*f2/(pi1*f1+pi2*f2)

z1 = 2*1.4-2-log(4)
z2 = 2*1.8-2-log(4)
assert round(z1, 6) == -.586294 and round(z2, 6) == .213706
assert round(posterior(1.4), 6) == .357486
assert round(posterior(1.4, .5, .5), 6) == .689974
assert round(posterior(1.8), 6) == .553224
assert 500 > 90-2 == 88

for value in ("1.693147", "-0.586294", "0.357486", "0.689974",
              "0.213706", "0.553224", "9.75", "19.98", "20.28", "17.8",
              "500", "88"):
    assert value in body, value
question = (root / "questions/ex-sl-08-3.qmd").read_text()
assert np.isclose((9.75+log(2))/1.5, 6.96209812037)
assert np.isclose((9.75+log(2))/1.5-6.5, .46209812037)
assert "6.962" in question and "0.462" in question
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "{#worked-example}" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert 'data-cite-key="james_islr2013"' in body
print("linear discriminant analysis calculations and practice passed")
