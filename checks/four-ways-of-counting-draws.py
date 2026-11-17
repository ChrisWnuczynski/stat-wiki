from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
import itertools,math
from fractions import Fraction as F
labels='ABC'
ordered=list(itertools.product(labels,repeat=2))
no_rep=list(itertools.permutations(labels,2))
sets=list(itertools.combinations(labels,2));multisets=list(itertools.combinations_with_replacement(labels,2))
assert list(map(len,[ordered,no_rep,sets,multisets]))==[9,6,3,6]
assert sum(tuple(sorted(t))==('A','A') for t in ordered)==1
assert sum(tuple(sorted(t))==('A','B') for t in ordered)==2
assert math.comb(6,3)==20 and math.perm(5,3)==60
assert math.comb(23,2)==253 and math.comb(20,5)==15504
for n,target in [(23,.507),(40,.891),(50,.970)]:
 p=1-math.prod((365-i)/365 for i in range(n));assert abs(p-target)<.0006
assert F(4*3*2,52*51*50)==F(1,5525)
assert F(12*8*4,52*51*50)==F(16,5525)
assert F(36*35*34,52*51*50)==F(21,65)
printed=['1/9','2/9','20','60']

article=(ROOT/"articles"/"four-ways-of-counting-draws.qmd").read_text()
for token in printed:
    assert token in article,("four-ways-of-counting-draws",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["four-ways-of-counting-draws"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("four-ways-of-counting-draws: numerical examples, self-checks and generated text verified")
