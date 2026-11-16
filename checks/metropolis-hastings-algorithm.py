"""Check rank-64 finite-state Hastings calculations and rendered practice."""
from pathlib import Path
from fractions import Fraction as F

root=Path(__file__).resolve().parents[1]
body=(root/'articles/metropolis-hastings-algorithm.qmd').read_text().split('## See also')[0]
pi=(F(1,4),F(3,4))
q_ab,q_ba=F(4,5),F(2,5)
r=pi[1]*q_ba/(pi[0]*q_ab)
assert r==F(3,2)
a_ab,a_ba=min(1,r),min(1,1/r)
assert (a_ab,a_ba)==(1,F(2,3))
p_ab,p_ba=q_ab*a_ab,q_ba*a_ba
assert (p_ab,p_ba)==(F(4,5),F(4,15))
assert pi[0]*p_ab==pi[1]*p_ba==F(1,5)
assert 1-p_ba==F(11,15)
pi2=(F(2,3),F(1,3)); qab2,qba2=F(3,5),F(1,5)
r2=pi2[1]*qba2/(pi2[0]*qab2)
assert r2==F(1,6)
assert qab2*r2==F(1,10)
assert pi2[0]*qab2*r2==pi2[1]*qba2==F(1,15)
for printed in ('1.5','0.6667','0.2667','0.7333','0.0667','11/15','4/15'):
 assert printed in body,printed
assert body.count('title="Proof"')==1
for heading in ('Motivating example','Worked example','Common misconceptions','Assumptions and limits','History','Check yourself'):
 assert f'## {heading}' in body
assert '**Your turn.**' in body and body.count('title="Answer"')>=3
for key in ('gelfand_smith1990','metropolis1953','hastings1970'):
 assert f'data-cite-key="{key}"' in body
for qid in ('c-12','c-14'):
 assert f'../questions/{qid}.qmd' in (root/'articles/metropolis-hastings-algorithm.qmd').read_text()
print('Hastings ratios, transition flows and practice passed')
