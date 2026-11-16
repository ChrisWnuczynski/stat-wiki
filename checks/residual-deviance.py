"""Verify printed deviance arithmetic and section structure."""
from math import isclose, log
from pathlib import Path


body = Path("articles/residual-deviance.qmd").read_text().split("## See also", 1)[0]
for token in ("0.77259", "2.77259", "4.25601", "1.48342", "0.44629",
              "0.71335", "1.15964", "0.0084", "0.0339", "0.0255",
              "0.76", "0.68", 'title="Proof"', 'title="Answer"'):
    assert token in body, token
assert body.count('title="Proof"') == 1

def pois_d(y, mu):
    return 2*((y*log(y/mu) if y else 0) - (y-mu))

first = pois_d(2,1)
second = pois_d(0,1)
third = pois_d(3,3)
assert round(first,5) == .77259
assert second == 2 and third == 0
d_fit = first + second + third
assert isclose(d_fit, 4*log(2)) and round(d_fit,5) == 2.77259
d_null = sum(pois_d(y,5/3) for y in (2,0,3))
assert round(d_null,5) == 4.25601
assert round(d_null-d_fit,5) == 1.48342
assert 3-2 == 1
success, failure = -2*log(.8), -2*log(.7)
assert round(success,5) == .44629
assert round(failure,5) == .71335
assert round(success+failure,5) == 1.15964
assert isclose(.0339-.0084,.0255)
f_wafer = (.0255/4)/(.0084/1)
assert round(f_wafer,2) == .76
print("residual-deviance likelihood arithmetic and structure passed")
