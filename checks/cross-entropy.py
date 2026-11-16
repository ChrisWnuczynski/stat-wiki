"""Verify rank-162 cross-entropy calculations and preserved material."""
from pathlib import Path
import json
import math

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/cross-entropy.qmd').read_text()
body = page.split('## See also')[0]

def entropy(p, q):
    return -sum(a * math.log(b) for a, b in zip(p, q) if a)

p = (.8, .2)
q = (.6, .4)
assert abs(entropy(p, q) - .5919186454) < 1e-10
assert abs(entropy(p, p) - .5004024235) < 1e-10
assert abs(entropy(p, q) - entropy(p, p) - .09151622185) < 1e-10
assert abs(entropy(q, p) - .7776612958) < 1e-10
assert abs(-math.log(.6) - .5108256238) < 1e-10
assert abs(-math.log(.4) - .9162907319) < 1e-10
u = (.5, .5)
v = (.9, .1)
assert abs(entropy(u, v) - 1.2039728043) < 1e-10
assert abs(entropy(u, u) - .69314718056) < 1e-10
assert abs(entropy(u, v) - entropy(u, u) - .5108256238) < 1e-10
for s in ('0.8,0.2', '0.6,0.4', '0.5919', '0.5004', '0.0915',
          '0.5108', '0.9163', '0.7777', '0.5,0.5', '0.9,0.1',
          '1.2040', '0.6931', '0.01'):
    assert s in body, s
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example', 'Worked example', 'Common misconceptions', 'History'):
    assert f'## {heading}' in body, heading
assert body.count('![') == 0
for qid in ('ex-sl-12-1', 'ex-sl-16-2'):
    assert f'../questions/{qid}.qmd' in page
pending = root / 'research/pending/cross-entropy.json'
selected = (json.loads(pending.read_text())['self_checks'] if pending.exists()
            else json.loads((root / 'research/self-checks.json').read_text())['cross-entropy'])
assert selected == ['ex-sl-12-1', 'ex-sl-16-2']
if not pending.exists():
    assert '## Check yourself' in body and body.count('title="Answer"') >= 3
print('rank 162 cross-entropy numerical and preservation checks passed')
