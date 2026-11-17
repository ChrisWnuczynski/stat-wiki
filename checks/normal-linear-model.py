"""Verify rank-165 normal-model calculations and retained material."""
from pathlib import Path
import json
import math
import numpy as np
from scipy.stats import t

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/normal-linear-model.qmd').read_text()
body = page.split('## See also')[0]

def fit(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    design = np.stack((np.ones(len(x)), x), axis=1)
    beta = np.linalg.lstsq(design, y, rcond=None)[0]
    fitted = design @ beta
    residual = y - fitted
    rss = residual @ residual
    return x, y, beta, fitted, residual, rss

# New four-point worked example, with exact displayed rounding.
x, y, b, fitted, residual, rss = fit((0, 1, 2, 3), (1, 2, 2, 4))
assert abs(x.mean()-1.5) < 1e-12 and abs(y.mean()-2.25) < 1e-12
assert abs(np.sum((x-x.mean())**2)-5) < 1e-12
assert abs(np.sum((x-x.mean())*(y-y.mean()))-4.5) < 1e-12
assert np.allclose(b, (.9, .9))
assert np.allclose(fitted, (.9, 1.8, 2.7, 3.6))
assert np.allclose(residual, (.1, .2, -.7, .4))
assert abs(np.sum(residual)) < 1e-12 and abs(x@residual) < 1e-12
assert abs(rss-.7) < 1e-12 and 4-2 == 2
assert abs(rss/2-.35) < 1e-12 and abs(rss/4-.175) < 1e-12
se = math.sqrt(.35/5)
assert abs(se-.2646) < .0001
assert abs(t.ppf(.975, 2)-4.303) < .001
lo, hi = .9-t.ppf(.975,2)*se, .9+t.ppf(.975,2)*se
assert abs(lo-(-.238)) < .001 and abs(hi-2.038) < .001

# New Your-turn example.
x, y, b, fitted, residual, rss = fit((0, 1, 2), (1, 3, 2))
assert np.allclose(b, (1.5, .5))
assert np.allclose(fitted, (1.5, 2, 2.5))
assert np.allclose(residual, (-.5, 1, -.5))
assert abs(rss-1.5) < 1e-12 and 3-2 == 1
assert abs(rss/(3-2)-1.5) < 1e-12 and abs(rss/3-.5) < 1e-12

# Preserved 19-pair heart-rate and oxygen-intake exercise.
heart = [94, 96, 95, 95, 94, 95, 94, 104, 104, 106, 108, 110, 113, 113, 118, 115, 121, 127, 131]
oxygen = [.473, .753, .929, .939, .832, .983, 1.049, 1.178, 1.176, 1.292,
          1.403, 1.499, 1.529, 1.599, 1.749, 1.746, 1.897, 2.040, 2.231]
x, y, b, fitted, residual, rss = fit(heart, oxygen)
assert len(x) == 19 and abs(x.mean()-107.0) < 1e-12
sxx = np.sum((x-x.mean())**2)
assert abs(sxx-2518) < 1e-10
s = math.sqrt(rss/17)
s1 = s/math.sqrt(sxx)
s0 = s*math.sqrt(np.sum(x*x)/(len(x)*sxx))
for actual, printed, tol in ((b[0],-2.804,.001), (b[1],.03865,.00001),
                             (s,.1205,.0001), (s1,.00240,.00001),
                             (s0,.258,.001), (b[1]/s1,16.1,.1),
                             (t.ppf(.975,17),2.110,.001),
                             (b[1]-t.ppf(.975,17)*s1,.0336,.0001),
                             (b[1]+t.ppf(.975,17)*s1,.0437,.0001)):
    assert abs(actual-printed) < tol, (actual, printed)

for literal in ('0.9+0.9x', '0.175', '0.2646', '4.303', '-0.238', '2.038',
                '0.473', '2.231', '107.0', '2518', '-2.804', '0.03865',
                '0.1205', '0.00240', '0.258', '2.110', '0.0336',
                '0.0437', '16.1', '1805'):
    assert literal in body, literal
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example', 'Worked example', 'Common misconceptions', 'History'):
    assert f'## {heading}' in body, heading
assert body.count('![') == 0
for link in ('ordinary-least-squares.qmd', 'simple-linear-regression.qmd',
             'multiple-linear-regression.qmd', 'general-linear-hypothesis.qmd'):
    assert link in page, link
selected = json.loads((root / 'research/self-checks.json').read_text())['normal-linear-model']
assert selected == ['ex-inf-extra-ss', 'ex-inf-prediction-width']
print('rank 165 normal linear model arithmetic and preservation checks passed')
