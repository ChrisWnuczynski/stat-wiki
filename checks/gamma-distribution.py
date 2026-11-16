"""Check rank-65 gamma formulas, waiting-time examples and preserved figures."""
from pathlib import Path
import math
from scipy.stats import gamma

root=Path(__file__).resolve().parents[1]
page=(root/'articles/gamma-distribution.qmd').read_text(); body=page.split('## See also')[0]
a,rate=3,2
assert a/rate==1.5 and a/rate**2==0.75
assert math.isclose(gamma.sf(2,a,scale=1/rate),13*math.exp(-4),rel_tol=1e-12)
assert math.isclose(13*math.exp(-4),0.2381033055535443)
assert math.isclose(1-13*math.exp(-4),0.7618966944464557)
assert math.isclose(gamma.sf(3,2,scale=1),4*math.exp(-3),rel_tol=1e-12)
assert math.isclose(4*math.exp(-3),0.19914827347145578)
assert math.isclose(1+1/2,1.5) and math.isclose(1+1/4,1.25)
assert math.isclose(2/(4/3)**2,1.125)
assert math.isclose(gamma.mean(3,scale=.5),1.5)
assert math.isclose(gamma.var(3,scale=.5),.75)
for printed in ('1.5','0.75','0.2381','0.7619','0.1991','1.25','1.125','4/3','0.4060'):
 assert printed in body,printed
assert body.count('title="Proof"')==1
assert body.count('![')>=3
for heading in ('Motivating example','Worked example','Common misconceptions','Assumptions and limits','History','Check yourself'):
 assert f'## {heading}' in body
assert '**Your turn.**' in body and body.count('title="Answer"')>=3
for key in ('siegrist2022_gamma','siegrist2022_gamma_waiting','nist_gamma_handbook'):
 assert f'data-cite-key="{key}"' in body
for qid in ('c-10','c-23'):
 assert f'../questions/{qid}.qmd' in page
print('gamma moments, tails, parameterizations and practice passed')
