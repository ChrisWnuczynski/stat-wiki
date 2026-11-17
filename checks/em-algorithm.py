"""Validate fractional counts, EM updates, and retained numerical example."""

from fractions import Fraction as F
from math import isclose, log
from pathlib import Path

page = (Path(__file__).resolve().parents[1] / 'articles/em-algorithm.qmd').read_text()
body = page.split('## See also', 1)[0]

r_head = F(8, 11)
r_tail = F(2, 9)
assert r_head == F(8,10)/ (F(8,10)+F(3,10))
assert r_tail == F(2,10)/ (F(2,10)+F(7,10))
na = 2*r_head+r_tail
nb = 3-na
assert na == F(166,99) and round(float(na),4)==1.6768
assert nb == F(131,99) and round(float(nb),4)==1.3232
assert na/3 == F(166,297) and round(float(na/3),4)==.5589
assert (2*r_head)/na == F(72,83) and round(float((2*r_head)/na),4)==.8675
assert (2*(1-r_head))/nb == F(54,131) and round(float((2*(1-r_head))/nb),4)==.4122
assert F(6,10)*F(7,10)/(F(6,10)*F(7,10)+F(4,10)*F(2,10)) == F(84,100)
assert F(6,10)*F(3,10)/(F(6,10)*F(3,10)+F(4,10)*F(8,10)) == F(36,100)
assert 2*F(84,100)+F(36,100) == F(204,100)
assert F(204,100)/3 == F(68,100)
assert F(9,10)+F(2,10)+F(5,10) == F(16,10)
assert F(1,5)+3*F(1,2) == F(17,10)
assert (F(1,5)+3*F(1,2))/F(16,10) == F(17,16)
assert isclose(float((F(8,10)+3*F(5,10))/F(14,10)),1.6428571428571428)
for printed in ('8/11', '0.7273', '2/9', '0.2222', '166/99', '1.6768',
                '131/99', '1.3232', '166/297', '0.5589', '72/83', '0.8675',
                '54/131', '0.4122', '0.84', '0.36', '2.04', '0.68', '1.0625', '1.643'):
    assert printed in body, f'Missing printed result {printed}'
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for key in ('dempster_laird_rubin1977', 'fraley_raftery2002'):
    assert f'data-cite-key="{key}"' in body
print('EM responsibilities and parameter-update arithmetic passed')
