"""Check rank-159 beta update, predictive arithmetic and original material."""
from pathlib import Path
from fractions import Fraction
import json
import math
from scipy.stats import beta

root=Path(__file__).resolve().parents[1]
page=(root/'articles/beta-binomial-conjugacy.qmd').read_text()
body=page.split('## See also')[0]

a,b,n,x=2,3,20,7
ap,bp=a+x,b+n-x
assert (ap,bp)==(9,16) and (n-x)==13
assert Fraction(ap,ap+bp)==Fraction(9,25) and Fraction(a,a+b)==Fraction(2,5)
assert Fraction(x,n)==Fraction(7,20)
var=Fraction(ap*bp,(ap+bp)**2*(ap+bp+1))
assert var==Fraction(144,16250) and math.isclose(float(var),0.008861538461538462)
assert math.isclose(beta.var(ap,bp),float(var))
pred2=Fraction(ap*(ap+1),(ap+bp)*(ap+bp+1))
assert pred2==Fraction(9,65) and math.isclose(float(pred2),0.13846153846153847)
assert Fraction(9,25)**2==Fraction(81,625) and math.isclose(float(Fraction(81,625)),0.1296)
assert (1+4,1+5-4)==(5,2)
assert Fraction(5,7)==Fraction(5,7)
assert Fraction(2*3,7*8)==Fraction(3,28)
assert 1-Fraction(3,28)==Fraction(25,28)
for literal in ('3$ heads in $10','30$ heads in $100','Beta}(9,16)','9/25=0.36','0.00886','9/65','0.1385','0.1296','Beta}(5,2)','5/7','25/28','0.8929'):
    assert literal in body,literal
assert body.count('title="Proof"')==1
assert '**Your turn.**' in body and body.count('title="Answer"')>=1
assert body.count('![')>=1
for q in ('q-06','q-17','ex-ur-posterior-mean','q-23'):
    assert f'../questions/{q}.qmd' in page
pending=root/'research/pending/beta-binomial-conjugacy.json'
selected=(json.loads(pending.read_text())['self_checks'] if pending.exists() else json.loads((root/'research/self-checks.json').read_text())['beta-binomial-conjugacy'])
assert selected==['ex-ur-posterior-mean','q-23']
if not pending.exists():
    assert '## Check yourself' in body and body.count('title="Answer"')>=3
print('rank 159 posterior, prediction and preservation checks passed')
