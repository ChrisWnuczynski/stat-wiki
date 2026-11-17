"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='fisher-s-linear-discriminant-analysis'
NEEDLES=['25', '28', '507/136', '197']

S=s.Matrix([[2,1],[1,2]]);d=s.Matrix([2,1]);a=S.inv()*d
J=lambda a,S,d:(a.T*d)[0]**2/(2*(a.T*S*a)[0])
assert a==s.Matrix([1,0]) and J(a,S,d)==1 and J(d,S,d)==s.Rational(25,28)
assert J(a,2*S,d)==s.Rational(1,2)
S=s.Matrix([[s.Rational(4,3),s.Rational(2,3)],[s.Rational(2,3),s.Rational(2,3)]]);d=s.Matrix([-3,-2])
assert S.inv()*d==s.Matrix([-s.Rational(3,2),-s.Rational(3,2)])
assert J(S.inv()*d,S,d)==s.Rational(15,4)
assert (d.T*S*d)[0]==s.Rational(68,3) and J(d,S,d)==s.Rational(507,136)
assert 3*10+10*11//2+2==87 and 3*10+3*10*11//2+2==197
# For a rank-deficient covariance, contrast outside the range is unbounded.
Sn=s.diag(1,0);dn=s.Matrix([0,1]);eps=s.symbols('eps',positive=True)
assert J(s.Matrix([eps,1]),Sn,dn)==1/(2*eps**2)

if '--math-only' not in sys.argv:
 source=(ROOT/'research/content'/f'{SLUG}.md').read_text()
 article=(ROOT/"articles"/f'{SLUG}.qmd').read_text().split('## See also',1)[0]
 for needle in NEEDLES:assert needle in article,(SLUG,needle)
 assert len(re.findall(r'\{\{cite:[^}]+\}\}',source))>=5
 assert len(set(re.findall(r'\{\{cite:([^}]+)\}\}',source)))>=2
 assert 'Your turn' in article and 'collapse="true" title="Answer"' in article
 assert '## Check yourself {#check-yourself}' in article
 section=article.split('## Check yourself {#check-yourself}',1)[1].split('\n## ',1)[0]
 ids=re.findall(r'(?m)^### .*\{#self-check-([^}]+)\}',section)
 assert len(ids) in (2,3) and section.count('collapse="true" title="Answer"')==len(ids),(SLUG,ids)
 for qid in ids:assert (ROOT/'questions'/f'{qid}.qmd').exists()
 for ans in re.findall(r'::: \{[^\n]*title="Answer"[^\n]*\}\n(.*?)\n:::',article,re.S):assert 'cite-ref' not in ans
print(SLUG+': independent calculations and article checks passed')
