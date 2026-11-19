"""Check rank-66 response-family examples and retained material."""
from pathlib import Path
from math import exp,isclose,sqrt
from scipy.stats import norm

body=(Path(__file__).resolve().parents[1]/'articles/random-component.qmd').read_text().split('## See also')[0]
assert isclose(.5*6**2,18) and isclose(.5*12**2,72)
assert isclose(exp(-6),0.0024787521766663585)
assert isclose(norm.cdf(-sqrt(6)),0.007152939217714809)
assert isclose(.8*(1-.8),.16)
assert isclose(1-exp(-.8)*(1+.8),0.1912078645890012)
for value in ('$6$','$18$','$72$','0.00248','0.00715','0.16','0.1912'):
 assert value in body,value
assert body.count('title="Proof"')==1
assert '**Your turn.**' in body and body.count('title="Answer"')>=3
for anchor in ('motivating-example','worked-example','properties','common-misconceptions','assumptions-and-limits','history','check-yourself'):
 assert f'{{#{anchor}}}' in body
assert 'Support, spread and dependence' in body
for key in ('nelder_wedderburn1972','sas2012_glm','zhou2020_glm'):
 assert f'data-cite-key="{key}"' in body
for qid in ('c-16','q-45'):
 assert f'../questions/{qid}.qmd' in body
print('random component family moments, support and practice passed')
