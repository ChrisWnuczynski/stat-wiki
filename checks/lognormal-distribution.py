"""Check rank-160 lognormal infobox, both examples and preserved figures."""
from pathlib import Path
import json
import math
import sympy as sp
from scipy.stats import lognorm, norm

root=Path(__file__).resolve().parents[1]
page=(root/'articles/lognormal-distribution.qmd').read_text()
body=page.split('## See also')[0]

mu=math.log(100); sigma=.4
assert math.isclose(math.exp(mu),100)
assert math.isclose(math.exp(mu+sigma*sigma/2),108.32870676749586)
assert math.isclose(math.exp(mu-sigma*sigma),85.21437889662113)
z=math.log(150/100)/sigma
assert math.isclose(z,1.0136627702704106)
assert math.isclose(norm.sf(z),0.15537184730329506)
assert math.isclose(lognorm.sf(150,s=sigma,scale=100),norm.sf(z))
assert math.isclose(norm.ppf(.9),1.2815515655446004)
assert math.isclose(100*math.exp(sigma*norm.ppf(.9)),166.9661024055183)

assert math.isclose(50*math.exp(.2**2/2),51.01006700133779)
assert math.isclose(50*math.exp(-.2**2),48.03947195761616)
assert math.isclose(lognorm.sf(50*math.exp(.2),s=.2,scale=50),norm.sf(1))
assert math.isclose(norm.sf(1),0.15865525393145707)
assert math.isclose(math.exp(.5),1.6487212707001282)
assert math.isclose(lognorm.sf(math.e,s=1,scale=1),norm.sf(1))
assert math.isclose(math.exp(.6**2)-1,(math.exp(.6**2)-1)*math.exp(0))

m,s=sp.symbols('m s',real=True)
raw1=sp.exp(m+s*s/2); raw2=sp.exp(2*m+2*s*s)
assert sp.simplify(raw2-raw1**2-(sp.exp(s*s)-1)*sp.exp(2*m+s*s))==0
for literal in ('0.6','0.1587','1.6487','108.33','85.21','166.97','0.1554','1.0137','1.2816','51.01','48.04'):
    assert literal in body,literal
assert body.count('title="Proof"')==1
assert body.count('![')>=2
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example','Worked example','Common misconceptions','When the lognormal model fails','History'):
    assert f'## {heading}' in body,heading
for q in ('q-28','q-45','ex-lognormal-var'):
    assert f'../questions/{q}.qmd' in page
pending=root/'research/pending/lognormal-distribution.json'
selected=(json.loads(pending.read_text())['self_checks'] if pending.exists() else json.loads((root/'research/self-checks.json').read_text())['lognormal-distribution'])
assert selected==['q-28','q-45']
if not pending.exists():
    assert '## Check yourself' in body and body.count('title="Answer"')>=3
print('rank 160 lognormal moments, tails and preservation checks passed')
